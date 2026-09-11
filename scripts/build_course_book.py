#!/usr/bin/env python3
"""Build a responsive HTML course book and export to PDF via CDP.

Fixes in this version:
- Proper <details>/<summary> handling (no escaped tags, no empty boxes)
- Globally unique heading IDs (h2 as prefix for h3)
- Sidebar TOC shows only chapters and section titles (h1/h2)
- PDF via CDP: no default headers/footers, generate PDF bookmarks
- Bundles CSS, JS, SVG into dist/
- Generates single-file HTML and dist.zip
"""

from __future__ import annotations

import argparse
import base64
import csv
import html
import hashlib
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.parse import urlparse

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSET_DIR = SKILL_DIR / "assets"


# ── utilities ──────────────────────────────────────────────────────────

def safe_pack_path(root: Path, relative: str | Path) -> Path:
    path = (root / relative).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"path escapes the course pack: {relative}") from exc
    return path

def slugify(text: str, fallback: str) -> str:
    slug = re.sub(r"[^\w\u3400-\u9fff-]+", "-", text.lower(), flags=re.UNICODE)
    return slug.strip("-") or fallback


def rewrite_images(text: str, source_dir: Path, output_dir: Path) -> str:
    """Rewrite image paths relative to output_dir, and for single-file
    mode convert to data URIs."""
    pattern = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+[\"']([^\"']*)[\"'])?\)")

    def replace(match: re.Match[str]) -> str:
        alt, target, title = match.group(1), match.group(2), match.group(3)
        parsed = urlparse(target)
        if parsed.scheme or target.startswith(("#", "data:")):
            rewritten = target
        else:
            absolute = (source_dir / target).resolve()
            rewritten = os.path.relpath(absolute, output_dir).replace(os.sep, "/")
        title_part = f' "{title}"' if title else ""
        return f"![{alt}]({rewritten}{title_part})"

    return pattern.sub(replace, text)


def inline_markup(text: str) -> str:
    """Render inline markdown to HTML. Preserves raw <details>, <summary>,
    <br> tags while escaping everything else."""
    # Protect raw HTML tags we want to keep
    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"\x00HTML{len(protected)-1}\x00"

    text = re.sub(r"<(details|/details|summary|/summary|br)\s*/?>", protect, text, flags=re.I)

    escaped = html.escape(text, quote=True)

    # Inline code
    code_tokens: list[str] = []

    def protect_code(match: re.Match[str]) -> str:
        code_tokens.append(f"<code>{match.group(1)}</code>")
        return f"\x01CODE{len(code_tokens)-1}\x01"

    escaped = re.sub(r"\x60([^\x60]+)\x60", protect_code, escaped)

    # Images
    escaped = re.sub(
        r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+&quot;([^&]*)&quot;)?\)",
        lambda m: (
            f'<figure><img src="{m.group(2)}" alt="{m.group(1)}" loading="lazy">'
            + (f"<figcaption>{m.group(3)}</figcaption>" if m.group(3) else "")
            + "</figure>"
        ),
        escaped,
    )
    # Links
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    # Bold
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    # Italic
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    # Strikethrough
    escaped = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", escaped)

    for index, token in enumerate(code_tokens):
        escaped = escaped.replace(f"\x01CODE{index}\x01", token)

    # Restore protected HTML tags
    for index, tag in enumerate(protected):
        escaped = escaped.replace(f"\x00HTML{index}\x00", tag)

    return escaped


def is_table_separator(line: str) -> bool:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


# ── details block processor ──────────────────────────────────────────

def _process_details_block(lines: list[str], chapter_prefix: str) -> tuple[str, str]:
    """Process a full <details>...</details> block. Returns (rendered_html, toc_entries)."""
    block_text = "\n".join(lines)
    # Extract <summary>...</summary>
    summary_match = re.search(r"<summary>(.*?)</summary>", block_text, re.DOTALL)
    if not summary_match:
        return "", ""

    summary_raw = summary_match.group(1).strip()
    summary_html = re.sub(r"<br\s*/?>", "<br>", summary_raw, flags=re.I)

    # Content after </summary> and before </details>
    body_text = re.sub(r"<summary>.*?</summary>", "", block_text, flags=re.DOTALL)
    body_text = re.sub(r"</?details>", "", body_text, flags=re.I).strip()

    # Skip empty details boxes
    if not body_text:
        return "", ""

    # Render body as markdown
    body_html, _ = render_markdown_lines(body_text.splitlines(), chapter_prefix)

    return f"<details>\n<summary>{summary_html}</summary>\n{body_html}\n</details>", ""


# ── markdown → HTML renderer ──────────────────────────────────────────

def render_markdown_lines(lines: list[str], chapter_prefix: str, *, global_heading_counter: list[int] | None = None) -> tuple[str, list[tuple[int, str, str]]]:
    """Render markdown lines to HTML. Returns (html, toc_entries)."""
    out: list[str] = []
    toc: list[tuple[int, str, str]] = []
    paragraph: list[str] = []
    in_code = False
    code_lang = ""
    code_lines: list[str] = []
    list_type: str | None = None
    recent_h2_slug = ""
    heading_index = global_heading_counter if global_heading_counter is not None else [0]

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            joined = " ".join(x.strip() for x in paragraph)
            rendered = inline_markup(joined)
            if re.fullmatch(r"\s*!\[[^\]]*\]\([^)]+\)\s*", joined):
                out.append(rendered)
            else:
                out.append("<p>" + rendered + "</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        # ── details block detection ──────────────────────────────
        if re.match(r"^<details>", stripped, flags=re.I):
            # Collect entire details block
            block_lines = []
            while index < len(lines):
                block_lines.append(lines[index])
                if re.match(r"^\s*</details>", lines[index].strip(), flags=re.I):
                    index += 1
                    break
                index += 1
            flush_paragraph()
            close_list()
            details_html, _ = _process_details_block(block_lines, chapter_prefix)
            if details_html:
                out.append(details_html)
            continue

        # ── code fences ──────────────────────────────────────────
        if stripped.startswith("\x60\x60\x60"):
            flush_paragraph()
            close_list()
            if not in_code:
                in_code = True
                code_lang = stripped[3:].strip()
                code_lines = []
            else:
                language = f' class="language-{html.escape(code_lang)}"' if code_lang else ""
                out.append(f"<pre><code{language}>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                in_code = False
            index += 1
            continue
        if in_code:
            code_lines.append(line)
            index += 1
            continue

        # ── tables ───────────────────────────────────────────────
        if index + 1 < len(lines) and "|" in line and is_table_separator(lines[index + 1]):
            flush_paragraph()
            close_list()
            headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            out.append('<div class="table-wrap"><table><thead><tr>')
            out.extend(f"<th>{inline_markup(cell)}</th>" for cell in headers)
            out.append("</tr></thead><tbody>")
            for row in rows:
                out.append("<tr>")
                out.extend(f"<td>{inline_markup(cell)}</td>" for cell in row)
                out.append("</tr>")
            out.append("</tbody></table></div>")
            continue

        # ── headings ─────────────────────────────────────────────
        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            title = heading.group(2).strip()
            heading_index[0] += 1

            # Build globally unique anchor
            anchor_parts = [chapter_prefix]
            if level == 2:
                recent_h2_slug = slugify(re.sub(r"[*_\x60]", "", title), str(heading_index[0]))
            if level >= 3 and recent_h2_slug:
                anchor_parts.append(recent_h2_slug)
            anchor_parts.append(slugify(re.sub(r"[*_\x60]", "", title), str(heading_index[0])))
            anchor = "-".join(anchor_parts)

            out.append(f'<h{level} id="{anchor}">{inline_markup(title)}</h{level}>')
            toc.append((level, re.sub(r"[*_\x60]", "", title), anchor))
            index += 1
            continue

        # ── list items ───────────────────────────────────────────
        item = re.match(r"^[-*+]\s+(.+)$", stripped)
        numbered = re.match(r"^\d+[.)]\s+(.+)$", stripped)
        if item or numbered:
            flush_paragraph()
            desired = "ul" if item else "ol"
            if list_type != desired:
                close_list()
                out.append(f"<{desired}>")
                list_type = desired
            out.append(f"<li>{inline_markup((item or numbered).group(1))}</li>")
            index += 1
            continue

        # ── blockquotes / provenance ─────────────────────────────
        if stripped.startswith(">"):
            flush_paragraph()
            close_list()
            body = stripped.lstrip(">").strip()
            label_match = re.match(
                r"\[(Course teaching|AI explanation|AI supplement|Current-context update|Uncertain)\]\s*(.*)",
                body, flags=re.I,
            )
            if label_match:
                label = label_match.group(1)
                css = slugify(label, "note")
                out.append(
                    f'<aside class="provenance {css}"><strong>{html.escape(label)}</strong>'
                    f"<p>{inline_markup(label_match.group(2))}</p></aside>"
                )
            else:
                out.append(f"<blockquote>{inline_markup(body)}</blockquote>")
            index += 1
            continue

        # ── horizontal rule ──────────────────────────────────────
        if stripped in {"---", "***", "___"}:
            flush_paragraph()
            close_list()
            out.append("<hr>")
            index += 1
            continue

        # ── blank line ───────────────────────────────────────────
        if not stripped:
            flush_paragraph()
            close_list()
        else:
            paragraph.append(line)
        index += 1

    flush_paragraph()
    close_list()
    if in_code:
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(out), toc


def render_markdown(text: str, chapter_prefix: str, *, global_heading_counter: list[int] | None = None) -> tuple[str, list[tuple[int, str, str]]]:
    return render_markdown_lines(text.splitlines(), chapter_prefix, global_heading_counter=global_heading_counter)


# ── SVG → data URI ──────────────────────────────────────────────────

def file_to_data_uri(asset_path: Path) -> str:
    """Convert a local asset to a data URI for the standalone edition."""
    mime = mimetypes.guess_type(asset_path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(asset_path.read_bytes()).decode()}"


# ── single-file HTML generator ───────────────────────────────────────

def generate_single_file(html_path: Path, output_path: Path, course_pack_root: Path,
                         assets_dir: Path, dist_dir: Path) -> None:
    """Generate a single-file HTML with all local CSS, JS, and images inlined."""
    import re as _re

    content = html_path.read_text(encoding="utf-8")

    # Inline CSS
    css_path = dist_dir / "course-book.css"
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        content = content.replace(
            '<link rel="stylesheet" href="course-book.css">',
            f"<style>\n{css}\n</style>"
        )

    # Inline JS
    js_path = dist_dir / "course-book.js"
    if js_path.exists():
        js = js_path.read_text(encoding="utf-8")
        content = content.replace(
            '<script src="course-book.js"></script>',
            f"<script>\n{js}\n</script>"
        )

    # Inline every local image type, not only SVG.
    def replace_image_ref(match: _re.Match[str]) -> str:
        tag = match.group(0)
        src_match = _re.search(r'src="([^"]+)"', tag)
        if not src_match:
            return tag
        src = src_match.group(1)
        if src.startswith("data:"):
            return tag
        if src.startswith(("http://", "https://", "//")):
            raise ValueError(f"standalone HTML contains a remote image: {src}")
        asset_abs = (dist_dir / src.split("?", 1)[0].split("#", 1)[0]).resolve()
        try:
            asset_abs.relative_to(course_pack_root.resolve())
        except ValueError as exc:
            raise ValueError(f"standalone HTML image escapes the course pack: {src}") from exc
        if not asset_abs.is_file():
            raise FileNotFoundError(f"standalone HTML image is missing: {src}")
        data_uri = file_to_data_uri(asset_abs)
        return tag.replace(f'src="{src}"', f'src="{data_uri}"')

    content = _re.sub(r'<img[^>]+src="[^"]+"[^>]*>', replace_image_ref, content)

    # A standalone document may keep ordinary source links, but no runtime asset.
    if _re.search(r'<(?:script|img)[^>]+src="(?!data:)[^"]+"', content, _re.I):
        raise ValueError("standalone HTML still contains a non-data src")
    if _re.search(r'<link[^>]+(?:stylesheet|preload)[^>]+href=', content, _re.I):
        raise ValueError("standalone HTML still contains a linked stylesheet or preload")
    if _re.search(r'@import\s+|url\(\s*["\']?(?:https?:|//)', content, _re.I):
        raise ValueError("standalone HTML CSS still contains a remote runtime dependency")

    output_path.write_text(content, encoding="utf-8")


# ── browser / PDF ────────────────────────────────────────────────────

def find_browser() -> str:
    """Find Chrome or Edge executable."""
    for name in ("google-chrome", "chrome", "chromium", "chromium-browser", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    candidates = []
    for variable in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA"):
        root = os.environ.get(variable)
        if root:
            candidates.extend([
                Path(root) / "Google/Chrome/Application/chrome.exe",
                Path(root) / "Microsoft/Edge/Application/msedge.exe",
            ])
    result = str(next((candidate for candidate in candidates if candidate.exists()), "")) or None
    if not result:
        raise FileNotFoundError("No Chrome or Edge browser found")
    return result


def export_pdf_cli(browser: str, html_path: Path, pdf_path: Path) -> None:
    """Export PDF using browser CLI: no default headers/footers, generate
    a PDF outline (bookmarks) from the heading structure."""
    command = [
        browser, "--headless", "--disable-gpu", "--no-sandbox",
        "--disable-dev-shm-usage", "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw", "--virtual-time-budget=5000",
        "--generate-pdf-outline",
        f"--print-to-pdf={pdf_path.resolve()}",
        html_path.resolve().as_uri(),
    ]
    result = subprocess.run(command, capture_output=True, text=True, timeout=120)
    if result.returncode != 0 or not pdf_path.exists():
        raise RuntimeError((result.stderr or result.stdout or "browser PDF export failed").strip())


def export_pdf(html_path: Path, pdf_path: Path, book_title: str = "", project_root: Path | None = None) -> None:
    """Export PDF with every collapsible answer forced open for printing."""
    browser = find_browser()
    print_path = html_path.with_name(f"{html_path.stem}.print-tmp.html")
    print_html = re.sub(r"<details(?![^>]*\bopen\b)", "<details open", html_path.read_text(encoding="utf-8"), flags=re.I)
    print_html = re.sub(r'loading=["\']lazy["\']', 'loading="eager"', print_html, flags=re.I)
    print_path.write_text(print_html, encoding="utf-8")
    try:
        export_pdf_cli(browser, print_path, pdf_path)
    finally:
        print_path.unlink(missing_ok=True)
    print("CLI PDF export succeeded")


# ── printable TOC & page measurement ──────────────────────────────

def build_print_toc(chapter_infos: list[dict], page_map: dict[str, int | str]) -> str:
    """Build the printable table of contents placed right after the cover.

    chapter_infos: [{number, title, h1_text, anchor, sections:[{title, anchor}]}]
    page_map: anchor -> physical PDF page (1-based); placeholder "—" if unknown.
    """
    rows: list[str] = []
    for info in chapter_infos:
        page = page_map.get(info["anchor"], "—")
        rows.append(
            f'<a class="toc-row toc-chapter" href="#{info["anchor"]}">'
            f'<span class="toc-title">{html.escape(info["title"])}</span>'
            f'<span class="toc-dots"></span>'
            f'<span class="toc-page">{page}</span></a>'
        )
        for sec in info["sections"]:
            page = page_map.get(sec["anchor"], "")
            rows.append(
                f'<a class="toc-row toc-section" href="#{sec["anchor"]}">'
                f'<span class="toc-title">{html.escape(sec["title"])}</span>'
                f'<span class="toc-dots"></span>'
                f'<span class="toc-page">{page}</span></a>'
            )
    return (
        '<section class="print-toc">'
        '<div class="chapter-kicker">CONTENTS</div>'
        '<h1 id="print-toc-heading">目录</h1>'
        '<p class="toc-note">本目录可打印使用：点击任意条目即可在 PDF 中跳转到对应位置，'
        '右侧数字为该章/节的起始页码（与页面底部页码一致）。在线阅读时还可使用侧栏的"搜索章节"快速定位。</p>'
        '<div class="toc-block">' + "\n".join(rows) + "</div></section>"
    )


def measure_heading_pages(pdf_path: Path, chapter_infos: list[dict]) -> dict[str, int]:
    """Locate every chapter/section start page in the PDF via text search.

    Returns {anchor: physical_page_1based}. Prefers PyMuPDF for reliable CJK
    text extraction; falls back to pypdf.
    """

    def extract_page_texts() -> list[str]:
        try:
            import pymupdf  # PyMuPDF: far more reliable CJK extraction than pypdf
            doc = pymupdf.open(str(pdf_path))
            try:
                return [page.get_text() for page in doc]
            finally:
                doc.close()
        except ImportError:
            from pypdf import PdfReader
            reader = PdfReader(str(pdf_path))
            return [page.extract_text() or "" for page in reader.pages]

    texts = [re.sub(r"\s+", "", raw or "") for raw in extract_page_texts()]

    def flat(text: str) -> str:
        return re.sub(r"\s+", "", text)

    # Chapter start pages: h1 text AND the per-chapter evidence declaration
    # ("证据声明") appear on the same page — the printable TOC never contains it.
    chapter_starts: list[int] = []
    for info in chapter_infos:
        h1_flat = flat(info["h1_text"])
        hit = None
        for i, t in enumerate(texts):
            if h1_flat in t and "证据声明" in t:
                hit = i
                break
        if hit is None:  # fallback: h1 alone, skipping cover/TOC region
            for i in range(3, len(texts)):
                if h1_flat in texts[i]:
                    hit = i
                    break
        if hit is None:
            raise RuntimeError(f"chapter start page not found: {info['title']}")
        chapter_starts.append(hit)

    page_map: dict[str, int] = {}
    for ci, info in enumerate(chapter_infos):
        start = chapter_starts[ci]
        end = chapter_starts[ci + 1] if ci + 1 < len(chapter_starts) else len(texts)
        page_map[info["anchor"]] = start + 1
        for sec in info["sections"]:
            sec_flat = flat(sec["title"])
            hit = None
            for i in range(start, end):
                if sec_flat in texts[i]:
                    hit = i
                    break
            page_map[sec["anchor"]] = (hit + 1) if hit is not None else (start + 1)
    return page_map


def outline_stats(pdf_path: Path) -> tuple[int, list[str]]:
    """Return (top_level_bookmark_count, [indented titles]) via pypdf."""
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    titles: list[str] = []

    def walk(items: object, depth: int = 0) -> None:
        for item in items:
            if isinstance(item, list):
                walk(item, depth + 1)
            else:
                titles.append(("  " * depth) + str(getattr(item, "title", item)))

    walk(reader.outline)
    top = len([i for i in reader.outline if not isinstance(i, list)])
    return top, titles


def inject_outline(pdf_path: Path, chapter_infos: list[dict], page_map: dict[str, int]) -> bool:
    """Inject PDF bookmarks (chapters + sections) with pypdf.

    page_map values are 1-based physical page numbers. Returns True on success.
    """
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        print("WARNING: pypdf not available; skip bookmark injection", file=sys.stderr)
        return False

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)
    count = 0
    for info in chapter_infos:
        chap_page = page_map.get(info["anchor"])
        if chap_page is None:
            continue
        parent = writer.add_outline_item(info["title"], chap_page - 1)
        count += 1
        for sec in info["sections"]:
            sec_page = page_map.get(sec["anchor"])
            if sec_page is not None:
                writer.add_outline_item(sec["title"], sec_page - 1, parent=parent)
                count += 1
    tmp = pdf_path.with_name(pdf_path.stem + ".outline.tmp.pdf")
    try:
        with open(tmp, "wb") as fh:
            writer.write(fh)
        tmp.replace(pdf_path)
    finally:
        tmp.unlink(missing_ok=True)
    print(f"Injected PDF outline bookmarks: {count}")
    return True


# ── asset bundling ───────────────────────────────────────────────────

def bundle_assets(assets_dir: Path, dist_dir: Path) -> None:
    """Copy SVG assets to dist/assets/."""
    target = dist_dir / "assets"
    target.mkdir(parents=True, exist_ok=True)
    for svg in assets_dir.glob("*.svg"):
        shutil.copy2(svg, target / svg.name)


# ── dist.zip ─────────────────────────────────────────────────────────

def create_dist_zip(dist_dir: Path, pack_dir: Path) -> Path:
    """Create dist.zip containing all dist files."""
    zip_path = pack_dir / "dist.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(dist_dir.rglob("*")):
            if file_path.is_file() and "__pycache__" not in file_path.parts:
                arcname = file_path.relative_to(pack_dir)
                zf.write(file_path, arcname)
    return zip_path


# ── main ─────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", nargs="?", default="book-manifest.json")
    parser.add_argument("--html-only", action="store_true")
    parser.add_argument("--single-file", action="store_true", help="Compatibility flag; standalone HTML is always generated")
    parser.add_argument("--zip", action="store_true", help="Also create dist.zip")
    args = parser.parse_args()

    manifest_path = Path(args.manifest).resolve()
    root = manifest_path.parent
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    output_dir = safe_pack_path(root, manifest.get("output_dir", "dist"))
    output_dir.mkdir(parents=True, exist_ok=True)
    basename = manifest.get("output_basename", "course-book")

    chapters = manifest.get("chapters", [])
    if not chapters:
        raise ValueError("manifest chapters must not be empty")

    # ── Render chapters ────────────────────────────────────────────
    chapters_html: list[str] = []
    chapter_markdown: list[str] = []
    toc_entries: list[tuple[int, str, str]] = []
    chapter_infos: list[dict] = []
    global_heading_counter = [0]  # mutable across chapters

    for number, item in enumerate(chapters, start=1):
        relative = item["path"] if isinstance(item, dict) else item
        source = safe_pack_path(root, relative)
        text = rewrite_images(source.read_text(encoding="utf-8"), source.parent, output_dir)
        chapter_markdown.append(source.read_text(encoding="utf-8").strip())
        chapter_prefix = f"c{number}"

        rendered, chapter_toc = render_markdown(
            text, chapter_prefix, global_heading_counter=global_heading_counter
        )
        title = item.get("title", source.stem) if isinstance(item, dict) else source.stem
        chapters_html.append(
            f'<section class="chapter" data-chapter="{number}">'
            f'<div class="chapter-kicker">Chapter {number:02d}</div>{rendered}</section>'
        )
        # Printable-TOC info: chapter h1 text/anchor + its sections (h2)
        h1_title = chapter_toc[0][1] if chapter_toc else title
        h1_anchor = chapter_toc[0][2] if chapter_toc else f"chapter-{number}"
        chapter_infos.append({
            "number": number,
            "title": title,
            "h1_text": h1_title,
            "anchor": h1_anchor,
            "sections": [{"title": s[1], "anchor": s[2]} for s in chapter_toc if s[0] == 2],
        })
        # TOC: only chapter title (h1) and section titles (h2)
        toc_entries.append((1, title, h1_anchor))
        toc_entries.extend(entry for entry in chapter_toc if entry[0] == 2)

    # ── Build sidebar TOC ──────────────────────────────────────────
    toc_html = "\n".join(
        f'<a class="toc-level-{level}" href="#{anchor}">{html.escape(title)}</a>'
        for level, title, anchor in toc_entries
    )
    sidebar_toc = f'<a class="toc-level-1" href="#print-toc-heading">目录</a>\n{toc_html}'

    # ── Copy CSS/JS to dist ─────────────────────────────────────────
    shutil.copyfile(ASSET_DIR / "course-book.css", output_dir / "course-book.css")
    shutil.copyfile(ASSET_DIR / "course-book.js", output_dir / "course-book.js")

    # ── Bundle SVG assets to dist ───────────────────────────────────
    assets_dir = root / "assets"
    if assets_dir.exists():
        bundle_assets(assets_dir, output_dir)

    # ── Build HTML (two passes: printable TOC page numbers) ────────
    title = html.escape(str(manifest.get("title", "Course Book")))
    subtitle = html.escape(str(manifest.get("subtitle", "")))
    author = html.escape(str(manifest.get("author", "")))
    source_note = html.escape(str(manifest.get("source_note", "")))
    language = html.escape(str(manifest.get("language", "en")))
    metadata = " · ".join(value for value in (author, source_note) if value)

    def build_document(page_numbers: dict[str, int]) -> str:
        print_toc_html = build_print_toc(chapter_infos, page_numbers)
        return f"""<!doctype html>
<html lang="{language}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><link rel="stylesheet" href="course-book.css"></head>
<body>
<button class="nav-toggle" aria-label="Toggle table of contents">☰</button>
<aside class="sidebar"><div class="sidebar-title">{title}</div>
<label class="search-label">搜索章节<input id="toc-search" type="search" placeholder="输入章节标题，如 3.4"></label>
<nav>{sidebar_toc}</nav></aside>
<main><header class="cover"><div class="eyebrow">SELF-CONTAINED STUDY EDITION</div>
<h1>{title}</h1><p class="subtitle">{subtitle}</p><p class="metadata">{metadata}</p></header>
{print_toc_html}
{''.join(chapters_html)}</main><script src="course-book.js"></script></body></html>"""

    html_path = output_dir / f"{basename}.html"
    markdown_path = output_dir / f"{basename}.md"
    markdown_path.write_text("\n\n".join(chapter_markdown).rstrip() + "\n", encoding="utf-8")
    manifest["build_content_sha256"] = hashlib.sha256(markdown_path.read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Canonical Markdown: {markdown_path}")
    html_path.write_text(build_document({}), encoding="utf-8")
    print(f"HTML (pass 1): {html_path}")

    # ── PDF (two passes: measure heading pages, rebuild with real numbers)
    if not args.html_only:
        pdf_path = output_dir / f"{basename}.pdf"
        try:
            export_pdf(html_path, pdf_path, title, root)
        except Exception as exc:
            print(f"PDF BLOCKED: {exc}", file=sys.stderr)
            return 2
        print(f"PDF (pass 1): {pdf_path}")

        measured: dict[str, int] = {}
        try:
            measured = measure_heading_pages(pdf_path, chapter_infos)
            print(f"Measured heading pages: {len(measured)}")
        except Exception as exc:
            print(f"WARNING: page measurement failed ({exc}); TOC keeps placeholder numbers", file=sys.stderr)

        if measured:
            html_path.write_text(build_document(measured), encoding="utf-8")
            print(f"HTML (pass 2): {html_path}")
            try:
                export_pdf(html_path, pdf_path, title, root)
                print(f"PDF (pass 2): {pdf_path}")
            except Exception as exc:
                print(f"PDF BLOCKED (pass 2): {exc}", file=sys.stderr)
                return 2
            try:  # sanity: pagination must be stable across passes
                re_measured = measure_heading_pages(pdf_path, chapter_infos)
                drift = {k: v for k, v in re_measured.items() if measured.get(k) != v}
                print("Page drift after pass 2:", drift if drift else "none")
            except Exception as exc:
                print(f"WARNING: re-measure failed: {exc}", file=sys.stderr)
            inject_outline(pdf_path, chapter_infos, measured)

        try:
            count, outline_titles = outline_stats(pdf_path)
            print(f"PDF outline bookmarks: {count} top-level / {len(outline_titles)} total")
            if not outline_titles:
                print("WARNING: PDF outline is EMPTY", file=sys.stderr)
        except Exception as exc:
            print(f"WARNING: cannot read PDF outline: {exc}", file=sys.stderr)

    # ── Single-file HTML (always required for the formal contract) ──
    single_path = output_dir / f"{basename}-standalone.html"
    generate_single_file(html_path, single_path, root, assets_dir, output_dir)
    print(f"Single-file HTML: {single_path}")

    # ── dist.zip ───────────────────────────────────────────────────
    if args.zip:
        zip_path = create_dist_zip(output_dir, root)
        print(f"ZIP: {zip_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
