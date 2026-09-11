# HTML and PDF Publishing

Use this specification when file creation is available. Preserve Markdown source, but deliver a cohesive course book rather than a folder the learner must assemble mentally.

## Required structure

```text
course-pack/
├── book-manifest.json
├── run-ledger.json
├── chapters/
│   └── 01-....md
├── evidence/
│   ├── evidence-ledger.csv
│   ├── concept-coverage.csv
│   ├── visual-ledger.csv
│   └── learning-qa.json
├── assets/
│   └── ...used teaching visuals...
├── sources/
│   └── ...permitted transcripts/captions/source records...
└── dist/
    ├── course-book.html
    ├── course-book-standalone.html
    ├── course-book.md
    ├── course-book.pdf
    ├── course-book.css
    ├── course-book.js
    └── assets/
```

Additional indexes, glossary, exercises, and planning files may remain in Markdown, but every file promised by an index or manifest must exist.

## Manifest

Create `book-manifest.json` with at least:

```json
{
  "title": "Course title",
  "subtitle": "AI-enhanced course book",
  "language": "zh-CN",
  "author": "",
  "source_runtime_minutes": 0,
  "estimated_reading_minutes": 0,
  "estimated_practice_minutes": 0,
  "estimated_project_minutes": 0,
  "estimated_review_minutes": 0,
  "estimated_total_study_minutes": 0,
  "evidence_ledger": "evidence/evidence-ledger.csv",
  "concept_coverage_ledger": "evidence/concept-coverage.csv",
  "visual_ledger": "evidence/visual-ledger.csv",
  "run_ledger": "run-ledger.json",
  "qa_record": "evidence/learning-qa.json",
  "chapters": [
    {"path": "chapters/01-introduction.md", "title": "Introduction"}
  ],
  "output_dir": "dist",
  "output_basename": "course-book",
  "canonical_markdown": "dist/course-book.md",
  "standalone_html": "dist/course-book-standalone.html",
  "pdf": "dist/course-book.pdf"
}
```

All time fields describe the generated artifact and its actual activities. `estimated_total_study_minutes` must equal reading + practice + project + review. Keep source runtime separate.

## Build

Create the deterministic structure first when starting a new pack:

```bash
python /path/to/study-open-courses/scripts/init_course_pack.py ./course-pack --title "Course title"
```

Then run from the course-pack directory:

```bash
python /path/to/study-open-courses/scripts/build_course_book.py book-manifest.json
```

The builder assembles the ordered chapters into canonical Markdown, creates the editable multi-file HTML, creates standalone HTML with local images/CSS/JS embedded, and exports the same content to PDF when Chrome, Chromium, or Edge is available. If no supported PDF engine exists, the completed formats remain useful but the formal pack remains incomplete until a PDF is exported or the learner explicitly changes the delivery contract.

Do not maintain separate hand-edited HTML and PDF bodies. They drift. Generate both from the same chapter sources and stylesheet.

### Three-primary-file contract (single-file HTML)

For a formal reconstructed course, the delivery contract in `SKILL.md` requires exactly three primary files from one canonical master: one complete Markdown, one **literally single-file self-contained HTML**, and one complete PDF. The multi-file `dist/course-book.html` plus its sibling `course-book.css` / `course-book.js` are build intermediates and editable assets, not the delivered HTML. The builder always writes `dist/course-book-standalone.html`; the legacy `--single-file` flag remains accepted but is no longer required. CSS, JS, and every local image are embedded. Remote runtime images are rejected rather than silently leaving an online dependency. The delivered three files are `course-book.md`, `course-book-standalone.html`, and `course-book.pdf`. DOCX, ZIP, split lesson files, and the multi-file HTML are optional extras only and never replace the three primary files.

> **Engineering adaptations:** the builder creates a temporary print copy with every `<details>` answer opened, prints it, and removes the temporary file; the interactive HTML remains collapsible. For CDP document outlines, tagged-PDF support, or a renderer fallback, use the bundled `scripts/export_pdf_cdp.js` as described in `references/build-and-pdf-pitfalls.md`. Never cite an unbundled helper as the required production path.

## Reading experience

The HTML course book must provide:

- a cover/title area and visible course/version/source note;
- a navigable table of contents;
- responsive phone, tablet, and desktop layout;
- readable Chinese and Latin typography;
- code, formulas, tables, and figures that do not overflow;
- figure captions and alt text;
- visually distinct provenance boxes;
- collapsible answers when the source Markdown uses `<details>`;
- print styles with page breaks, margins, and hidden interactive controls.

PDF must have usable pagination, headings, figures, captions, page margins, and selectable text. It must not be a set of screenshot pages.

## Validate

After Learning QA and rendered-file inspection, bind the review to the exact files:

```bash
python /path/to/study-open-courses/scripts/seal_course_pack.py .
```

Then run the completion validator:

```bash
python /path/to/study-open-courses/scripts/validate_course_pack.py .
```

Resolve every error before calling the pack complete. Warnings identify likely over-compression or suspicious time claims and require human/agent review, but do not demand meaningless padding.

The validator is a completion gate, not a general draft linter. Run it only after filling the run ledger, item coverage, Learning QA evidence, format-review evidence, and all three formal deliverables. It validates those records and sealed file hashes against each other; it does not replace the Agent's content or visual judgment. Follow [run-ledger-schema.md](run-ledger-schema.md) for the record fields and state transitions.
