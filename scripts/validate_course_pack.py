#!/usr/bin/env python3
"""Validate evidence, textbook coverage, visuals, timing, HTML, and PDF.

New checks (v2):
- No file:/// or Windows local paths in HTML/PDF
- No residual &lt; &gt; &amp;lt; HTML tags in visible text
- No duplicate heading IDs
- No empty <details> blocks (summary only, no body)
- All image src, CSS href, JS src links are valid
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


EVIDENCE_FIELDS = {
    "unit_id", "title", "official_duration", "source_type", "source_locator",
    "content_evidence", "first_locator", "last_locator", "evidence_size",
    "visual_support", "summary_location", "status",
}
COVERAGE_FIELDS = {
    "concept_id", "chapter", "concept", "source_units", "lecture_evidence",
    "explanation", "reasoning", "example", "boundaries", "visual",
    "quick_check", "application", "status",
}
VISUAL_FIELDS = {
    "visual_id", "source_unit", "locator", "visual_type", "teaching_role",
    "action", "rights_basis", "asset_path", "caption", "status",
}
ALLOWED_ACTIONS = {
    "EXTRACT", "REBUILD_EXACT", "REDRAW_CONCEPT", "AI_ILLUSTRATE",
    "TEXT_ONLY", "BLOCKED",
}
REQUIRED_QA_CHECKS = {
    "objective_traceability", "prerequisite_order", "source_accuracy",
    "labeled_synthesis", "correct_examples", "feedback_guidance",
    "compression_integrity", "time_estimate_assumptions", "visible_limitations",
}
REQUIRED_FORMAT_CHECKS = {
    "markdown_complete", "html_offline_desktop_mobile_print",
    "pdf_visual_review", "format_parity",
}
EXPECTED_ITEM_FIELDS = {
    "item_id", "title", "expected_order", "source_locator", "item_status",
    "attempt_count", "last_error", "blocking_impact", "next_action",
    "acquired", "processed", "verified", "reconstructed",
}
DEPENDENCY_PHRASES = (
    "建议回看", "请观看原视频", "见原视频", "需看原图", "回到视频",
    "watch the original video", "see the original video", "see original figure",
)


def read_ledger(path: Path, fields: set[str], errors: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        errors.append(f"missing ledger: {path}")
        return []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        actual = set(reader.fieldnames or [])
        missing = fields - actual
        if missing:
            errors.append(f"{path}: missing columns {sorted(missing)}")
        rows = list(reader)
    if not rows:
        errors.append(f"{path}: contains no rows")
    return rows


def blank(value: str | None) -> bool:
    return not value or not value.strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def locator_resolves(root: Path, locator: str) -> bool:
    locator = locator.strip()
    if re.match(r"^https?://", locator, re.I):
        return True
    file_part = re.split(r"[#?]", locator, maxsplit=1)[0].strip()
    if not file_part:
        return False
    path = (root / file_part).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError:
        return False
    return path.is_file()


def pack_path(root: Path, relative: str | Path, label: str, errors: list[str]) -> Path:
    path = (root / relative).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError:
        errors.append(f"{label} escapes the course pack: {relative}")
        return root / "__invalid_path__"
    return path


def read_json(path: Path, errors: list[str]) -> dict:
    if not path.exists():
        errors.append(f"missing JSON record: {path}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON record {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path}: root must be an object")
        return {}
    return value


def validate_completion_state(root: Path, manifest: dict, errors: list[str]) -> tuple[dict, dict]:
    run_path = pack_path(root, manifest.get("run_ledger", "run-ledger.json"), "run_ledger", errors)
    qa_path = pack_path(root, manifest.get("qa_record", "evidence/learning-qa.json"), "qa_record", errors)
    run = read_json(run_path, errors)
    qa = read_json(qa_path, errors)
    if not run or not qa:
        return run, qa
    if run.get("schema_version") != 1:
        errors.append(f"{run_path}: unsupported schema_version")
    if qa.get("schema_version") != 1:
        errors.append(f"{qa_path}: unsupported schema_version")

    required_text = (
        "run_id", "started_at", "last_updated_at", "learner", "outcome",
        "declared_scope", "requested_artifact_level", "target_artifact_level",
        "delivery_contract", "artifact_status", "integrity_status",
        "checkpoint_status", "artifact_revision", "qa_profile", "learning_qa",
    )
    for field in required_text:
        if blank(str(run.get(field, ""))):
            errors.append(f"{run_path}: blank {field}")

    resource = run.get("resource")
    if not isinstance(resource, dict):
        errors.append(f"{run_path}: resource must be an object")
    else:
        for field in ("identity", "edition", "source_set_revision", "access_class", "processing_eligibility"):
            if blank(str(resource.get(field, ""))):
                errors.append(f"{run_path}: blank resource.{field}")
        if resource.get("processing_eligibility") not in {"eligible", "eligible_limited", "eligible_as_separate_source"}:
            errors.append(f"{run_path}: instructional reconstruction is not processing-eligible")

    if run.get("requested_artifact_level") != "reconstructed learning artifact":
        errors.append(f"{run_path}: formal pack requires requested_artifact_level reconstructed learning artifact")
    if run.get("target_artifact_level") != "reconstructed learning artifact":
        errors.append(f"{run_path}: formal pack requires target_artifact_level reconstructed learning artifact")
    if run.get("delivery_contract") != "three_primary_files":
        errors.append(f"{run_path}: formal pack requires delivery_contract three_primary_files")
    if run.get("artifact_status") != "complete" or run.get("integrity_status") != "pass":
        errors.append(f"{run_path}: artifact_status must be complete and integrity_status must be pass")
    if run.get("checkpoint_status") != "sealed":
        errors.append(f"{run_path}: checkpoint_status must be sealed")
    if run.get("completion_name") != "reconstructed learning artifact complete":
        errors.append(f"{run_path}: invalid or missing formal completion_name")
    blockers = run.get("blockers")
    if not isinstance(blockers, list) or blockers:
        errors.append(f"{run_path}: blockers must be an empty list at completion")

    items = run.get("expected_items")
    if not isinstance(items, list) or not items:
        errors.append(f"{run_path}: expected_items must contain the declared scope")
        items = []
    ids: list[str] = []
    orders: list[int] = []
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            errors.append(f"{run_path}: expected_items[{index}] must be an object")
            continue
        missing = EXPECTED_ITEM_FIELDS - set(item)
        if missing:
            errors.append(f"{run_path}: expected_items[{index}] missing {sorted(missing)}")
        item_id = str(item.get("item_id", "")).strip()
        if not item_id:
            errors.append(f"{run_path}: expected_items[{index}] has blank item_id")
        ids.append(item_id)
        try:
            orders.append(int(item.get("expected_order")))
            int(item.get("attempt_count"))
        except (TypeError, ValueError):
            errors.append(f"{run_path}: expected_items[{index}] order and attempt_count must be integers")
        if item.get("item_status") != "READY":
            errors.append(f"{run_path}: expected_items[{index}] is not READY")
        if not locator_resolves(root, str(item.get("source_locator", ""))):
            errors.append(f"{run_path}: expected_items[{index}].source_locator does not resolve")
        for flag in ("acquired", "processed", "verified", "reconstructed"):
            if item.get(flag) is not True:
                errors.append(f"{run_path}: expected_items[{index}].{flag} must be true")
    if len(ids) != len(set(ids)):
        errors.append(f"{run_path}: expected item IDs are not unique")
    if orders and sorted(orders) != list(range(1, len(orders) + 1)):
        errors.append(f"{run_path}: expected_order must be unique and contiguous from 1")

    coverage = run.get("coverage")
    if not isinstance(coverage, dict):
        errors.append(f"{run_path}: coverage must be an object")
    else:
        expected = len(items)
        actual_rollup = {"expected": expected}
        for flag in ("acquired", "processed", "verified", "reconstructed"):
            actual_rollup[flag] = sum(item.get(flag) is True for item in items if isinstance(item, dict))
        for key, actual in actual_rollup.items():
            if coverage.get(key) != actual:
                errors.append(f"{run_path}: coverage.{key}={coverage.get(key)!r}, item rows require {actual}")
        if any(actual_rollup[key] != expected for key in ("acquired", "processed", "verified", "reconstructed")):
            errors.append(f"{run_path}: all coverage totals must equal expected at formal completion")

    if qa.get("qa_profile") != "reconstructed_learning_artifact":
        errors.append(f"{qa_path}: wrong qa_profile")
    if qa.get("artifact_revision") != run.get("artifact_revision"):
        errors.append(f"{qa_path}: artifact_revision does not match the run ledger")
    if qa.get("learning_qa") != "pass" or run.get("learning_qa") != "pass":
        errors.append(f"{qa_path}: current Learning QA must pass in both records")
    if qa.get("failed_checks") != []:
        errors.append(f"{qa_path}: failed_checks must be empty at completion")
    if blank(str(qa.get("sealed_at", ""))):
        errors.append(f"{qa_path}: missing sealed_at")

    for group, required in (("checks", REQUIRED_QA_CHECKS), ("format_checks", REQUIRED_FORMAT_CHECKS)):
        rows = qa.get(group)
        if not isinstance(rows, list):
            errors.append(f"{qa_path}: {group} must be a list")
            continue
        by_name = {str(row.get("check")): row for row in rows if isinstance(row, dict)}
        missing = required - set(by_name)
        if missing:
            errors.append(f"{qa_path}: {group} missing {sorted(missing)}")
        for name in required & set(by_name):
            row = by_name[name]
            allowed_results = {"pass"} if group == "format_checks" else {"pass", "not_applicable"}
            if row.get("result") not in allowed_results:
                errors.append(f"{qa_path}: {group}.{name} did not pass")
            if blank(str(row.get("evidence", ""))):
                errors.append(f"{qa_path}: {group}.{name} has no evidence")
            if row.get("result") == "not_applicable" and blank(str(row.get("reason", ""))):
                errors.append(f"{qa_path}: {group}.{name} needs a not_applicable reason")
    return run, qa


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack_dir", nargs="?", default=".")
    parser.add_argument("--allow-no-pdf", action="store_true")
    args = parser.parse_args()
    root = Path(args.pack_dir).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    manifest_path = root / "book-manifest.json"
    if not manifest_path.exists():
        print("ERROR missing book-manifest.json")
        return 1
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR invalid manifest: {exc}")
        return 1

    run, _qa = validate_completion_state(root, manifest, errors)

    chapters = manifest.get("chapters") or []
    if not chapters:
        errors.append("manifest chapters is empty")
    chapter_paths: list[Path] = []
    for item in chapters:
        relative = item.get("path") if isinstance(item, dict) else item
        path = pack_path(root, str(relative), "chapter path", errors)
        chapter_paths.append(path)
        if not path.exists():
            errors.append(f"missing chapter: {relative}")

    evidence_path = pack_path(root, manifest.get("evidence_ledger", "evidence/evidence-ledger.csv"), "evidence_ledger", errors)
    coverage_path = pack_path(root, manifest.get("concept_coverage_ledger", "evidence/concept-coverage.csv"), "concept_coverage_ledger", errors)
    visual_path = pack_path(root, manifest.get("visual_ledger", "evidence/visual-ledger.csv"), "visual_ledger", errors)
    evidence = read_ledger(evidence_path, EVIDENCE_FIELDS, errors)
    coverage = read_ledger(coverage_path, COVERAGE_FIELDS, errors)
    visuals = read_ledger(visual_path, VISUAL_FIELDS, errors)

    expected_ids = {
        str(item.get("item_id", "")).strip()
        for item in run.get("expected_items", []) if isinstance(item, dict)
    }
    evidence_ids = {row.get("unit_id", "").strip() for row in evidence}
    if expected_ids and expected_ids != evidence_ids:
        errors.append(
            f"expected item IDs and evidence unit IDs differ: "
            f"missing evidence={sorted(expected_ids - evidence_ids)}, "
            f"undeclared evidence={sorted(evidence_ids - expected_ids)}"
        )

    # ── evidence rows ─────────────────────────────────────────────
    for row_number, row in enumerate(evidence, start=2):
        if row.get("status", "").strip().upper() != "READY":
            errors.append(f"{evidence_path}:{row_number}: evidence unit is not READY")
        for field in EVIDENCE_FIELDS - {"status"}:
            if blank(row.get(field)):
                errors.append(f"{evidence_path}:{row_number}: blank {field}")
        if not locator_resolves(root, row.get("source_locator", "")):
            errors.append(f"{evidence_path}:{row_number}: source_locator does not resolve")

    # ── concept coverage rows ─────────────────────────────────────
    for row_number, row in enumerate(coverage, start=2):
        if row.get("status", "").strip().upper() != "READY":
            errors.append(f"{coverage_path}:{row_number}: concept is not READY")
        for field in COVERAGE_FIELDS - {"status"}:
            if blank(row.get(field)):
                errors.append(f"{coverage_path}:{row_number}: blank {field}")
        source_ids = {
            token.strip() for token in re.split(r"[,;|]", row.get("source_units", "")) if token.strip()
        }
        unknown = source_ids - evidence_ids
        if unknown:
            errors.append(f"{coverage_path}:{row_number}: unknown source_units {sorted(unknown)}")

    # ── visual rows ───────────────────────────────────────────────
    for row_number, row in enumerate(visuals, start=2):
        action = row.get("action", "").strip().upper()
        status = row.get("status", "").strip().upper()
        if action not in ALLOWED_ACTIONS:
            errors.append(f"{visual_path}:{row_number}: invalid action {action!r}")
        if action == "BLOCKED" or status != "READY":
            errors.append(f"{visual_path}:{row_number}: visual is not READY")
        for field in VISUAL_FIELDS - {"status"}:
            if blank(row.get(field)):
                errors.append(f"{visual_path}:{row_number}: blank {field}")
        if action != "TEXT_ONLY" and blank(row.get("asset_path")):
            errors.append(f"{visual_path}:{row_number}: asset_path required for {action}")
        asset = row.get("asset_path", "").strip()
        if asset and not asset.upper().startswith("NOT_NEEDED") and not pack_path(root, asset, "visual asset", errors).exists():
            errors.append(f"{visual_path}:{row_number}: missing asset {asset}")
        if action == "EXTRACT" and blank(row.get("rights_basis")):
            errors.append(f"{visual_path}:{row_number}: EXTRACT requires rights_basis")

    # ── chapter dependency checks ─────────────────────────────────
    combined = ""
    for path in chapter_paths:
        if path.exists():
            text = path.read_text(encoding="utf-8")
            combined += "\n" + text
            for line_number, line in enumerate(text.splitlines(), start=1):
                lower = line.lower()
                if any(phrase in lower for phrase in DEPENDENCY_PHRASES) and "blocked" not in lower:
                    errors.append(f"{path}:{line_number}: unresolved dependency on original course")

    # ── visual asset embedded in chapters ─────────────────────────
    for row_number, row in enumerate(visuals, start=2):
        action = row.get("action", "").strip().upper()
        asset = row.get("asset_path", "").strip()
        if action != "TEXT_ONLY" and asset and Path(asset).name not in combined:
            errors.append(f"{visual_path}:{row_number}: visual asset is not embedded in any chapter")

    # ── HTML file checks ──────────────────────────────────────────
    output_dir = pack_path(root, manifest.get("output_dir", "dist"), "output_dir", errors)
    basename = manifest.get("output_basename", "course-book")
    markdown_path = pack_path(root, manifest.get("canonical_markdown", f"dist/{basename}.md"), "canonical_markdown", errors)
    html_path = pack_path(root, manifest.get("standalone_html", f"dist/{basename}-standalone.html"), "standalone_html", errors)
    pdf_path = pack_path(root, manifest.get("pdf", f"dist/{basename}.pdf"), "pdf", errors)

    if not markdown_path.exists() or not markdown_path.read_text(encoding="utf-8", errors="replace").strip():
        errors.append(f"missing or empty canonical Markdown: {markdown_path}")
    else:
        expected_markdown = "\n\n".join(
            path.read_text(encoding="utf-8").strip() for path in chapter_paths if path.exists()
        ).rstrip() + "\n"
        if markdown_path.read_text(encoding="utf-8") != expected_markdown:
            errors.append(f"{markdown_path}: does not exactly match the ordered chapter master")
        content_hash = sha256(markdown_path)
        for label, recorded in (
            ("manifest build_content_sha256", manifest.get("build_content_sha256")),
            ("run ledger artifact_content_sha256", run.get("artifact_content_sha256")),
            ("QA artifact_content_sha256", _qa.get("artifact_content_sha256")),
        ):
            if recorded != content_hash:
                errors.append(f"{label} does not match current canonical Markdown")

    if not html_path.exists():
        errors.append(f"missing HTML: {html_path}")
    else:
        html_text = html_path.read_text(encoding="utf-8", errors="replace")
        html_lower = html_text.lower()

        # Basic structure
        for required in ("<nav", 'class="cover"', 'class="chapter"'):
            if required not in html_lower:
                errors.append(f"{html_path}: missing required structure {required}")

        # ── NEW: No file:/// or Windows paths ────────────────────
        path_patterns = [
            (r"file:///[A-Za-z]:", "file:/// Windows path"),
            (r"file:///", "file:/// path"),
            (r"[A-Z]:\\Users\\", "Windows absolute path (C:\\Users\\)"),
            (r"[A-Z]:/Users/", "Windows absolute path (C:/Users/)"),
        ]
        for pattern, desc in path_patterns:
            matches = re.findall(pattern, html_text)
            if matches:
                errors.append(f"{html_path}: contains {desc}: {matches[0][:80]}...")

        # ── NEW: No residual escaped HTML tags ───────────────────
        # Check for &lt;br&gt; &lt;/summary&gt; &lt;/details&gt; etc.
        residual_patterns = [
            (r"&lt;br\s*/?&gt;", "escaped <br> tag"),
            (r"&lt;/summary&gt;", "escaped </summary> tag"),
            (r"&lt;summary&gt;", "escaped <summary> tag"),
            (r"&lt;/details&gt;", "escaped </details> tag"),
            (r"&lt;details&gt;", "escaped <details> tag"),
        ]
        for pattern, desc in residual_patterns:
            matches = re.findall(pattern, html_text)
            if matches:
                errors.append(f"{html_path}: contains residual {desc} ({len(matches)} occurrence(s))")

        # ── NEW: Duplicate heading IDs ───────────────────────────
        id_matches = re.findall(r'<h[1-6]\s+id="([^"]+)"', html_text)
        seen_ids: dict[str, int] = {}
        for hid in id_matches:
            seen_ids[hid] = seen_ids.get(hid, 0) + 1
        duplicates = {k: v for k, v in seen_ids.items() if v > 1}
        if duplicates:
            errors.append(f"{html_path}: duplicate heading IDs: {duplicates}")

        # ── NEW: Empty <details> blocks ──────────────────────────
        # Find <details>...</details> with no content between </summary> and </details>
        details_blocks = re.findall(
            r'<details>(.*?)</details>', html_text, re.DOTALL
        )
        for idx, block in enumerate(details_blocks):
            # Remove <summary>...</summary>
            after_summary = re.sub(r'<summary>.*?</summary>', '', block, flags=re.DOTALL).strip()
            if not after_summary:
                errors.append(f"{html_path}: empty <details> block #{idx+1} (summary only, no body)")

        # Standalone resource checks. Ordinary <a href> source links are allowed.
        img_srcs = re.findall(r'<img[^>]+src="([^"]+)"', html_text)
        for src in img_srcs:
            if not src.startswith("data:"):
                errors.append(f"{html_path}: non-inlined image resource: {src}")

        # Check CSS links (<link rel="stylesheet" href="...">)
        for match in re.finditer(r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"', html_text):
            url = match.group(1)
            errors.append(f"{html_path}: linked stylesheet is forbidden in standalone HTML: {url}")

        # Check JS links (<script src="...">)
        for match in re.finditer(r'<script[^>]*src="([^"]+)"', html_text):
            url = match.group(1)
            errors.append(f"{html_path}: external script src is forbidden in standalone HTML: {url}")
        if re.search(r'@import\s+|url\(\s*["\']?(?!data:|#)', html_text, re.I):
            errors.append(f"{html_path}: CSS contains a non-inlined dependency")

    # ── PDF checks ────────────────────────────────────────────────
    if not pdf_path.exists():
        if args.allow_no_pdf:
            warnings.append(f"PDF missing but allowed by flag: {pdf_path}")
        else:
            errors.append(f"missing PDF: {pdf_path}")
    else:
        if pdf_path.read_bytes()[:4] != b"%PDF":
            errors.append(f"{pdf_path}: not a valid PDF signature")
        # ── NEW: Check PDF for file:/// paths ──────────────────
        pdf_content = pdf_path.read_bytes()
        # "file:///" as bytes
        if b"file:///" in pdf_content:
            # Find the specific string to report
            idx = pdf_content.find(b"file:///")
            snippet = pdf_content[max(0, idx-20):idx+60]
            errors.append(f"{pdf_path}: contains file:/// path: {snippet!r}")
        try:
            try:
                import pymupdf

                document = pymupdf.open(str(pdf_path))
                page_count = document.page_count
                extracted = "".join(page.get_text() for page in document)
            except ImportError:
                from pypdf import PdfReader

                document = PdfReader(str(pdf_path))
                page_count = len(document.pages)
                extracted = "".join(page.extract_text() or "" for page in document.pages)
            if page_count < 1:
                errors.append(f"{pdf_path}: PDF has no pages")
            if not extracted.strip():
                errors.append(f"{pdf_path}: PDF has no extractable text")
        except ImportError:
            warnings.append("No supported PDF parser; PDF page-count and text extraction were not checked")
        except Exception as exc:
            errors.append(f"{pdf_path}: PDF structure/text check failed: {exc}")

    artifact_hashes = _qa.get("artifact_hashes") if isinstance(_qa, dict) else None
    if not isinstance(artifact_hashes, dict):
        errors.append("QA artifact_hashes must be an object")
    else:
        for key, path in (
            ("canonical_markdown", markdown_path),
            ("standalone_html", html_path),
            ("pdf", pdf_path),
        ):
            if not path.exists() or artifact_hashes.get(key) != sha256(path):
                errors.append(f"QA artifact_hashes.{key} does not match the delivered file")

    # ── Time field checks ─────────────────────────────────────────
    time_fields = (
        "estimated_reading_minutes", "estimated_practice_minutes",
        "estimated_project_minutes", "estimated_review_minutes",
    )
    try:
        parts = [float(manifest.get(field, 0)) for field in time_fields]
        total = float(manifest.get("estimated_total_study_minutes", 0))
        runtime = float(manifest.get("source_runtime_minutes", 0))
        if total <= 0 or abs(total - sum(parts)) > 1:
            errors.append("estimated_total_study_minutes must equal reading + practice + project + review")
        if runtime > 0 and parts[0] < runtime * 0.5:
            warnings.append("reading time is below 50% of source runtime; review for over-compression")
        visible_text = re.sub(r"\x60\x60\x60.*?\x60\x60\x60", "", combined, flags=re.S)
        visible_text = re.sub(r"[#>*_\x60|\\[\\]()~-]", "", visible_text)
        cjk = len(re.findall(r"[\u3400-\u9fff]", visible_text))
        latin_words = len(re.findall(r"\b[\w'-]+\b", visible_text))
        estimated_from_text = cjk / 400 + latin_words / 220
        if parts[0] > 0 and estimated_from_text > 0:
            ratio = parts[0] / estimated_from_text
            if ratio > 1.6 or ratio < 0.6:
                warnings.append(
                    f"declared reading time differs from text estimate: declared {parts[0]:.0f} min, "
                    f"estimated {estimated_from_text:.1f} min"
                )
    except (TypeError, ValueError):
        errors.append("manifest time fields must be numeric")

    # ── Report ────────────────────────────────────────────────────
    for message in errors:
        print(f"ERROR {message}")
    for message in warnings:
        print(f"WARN  {message}")
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
