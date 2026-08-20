# Publishing and Delivery

Read this reference when preparing downloadable files or claiming a learning artifact is formally complete.

Publishing means preparing and validating the artifact. It never authorizes an external upload, post, repository creation or change, commit, push, or other remote mutation.

## Choose the delivery contract

| Request state | Required delivery |
|---|---|
| **Formal complete learning artifact** | Create three downloadable files: Markdown (`.md`), self-contained HTML (`.html`), and PDF (`.pdf`). |
| **Quick preview, outline, recommendation, or interim checkpoint** | Return the smallest useful format, normally Markdown in chat or as a file. |
| **User explicitly requests particular format or formats** | Deliver exactly those formats; do not add unwanted formats. |

A request to complete, finish, publish, make the full course, or provide a downloadable final course counts as a formal complete artifact unless the user explicitly narrows the output.

A preview may be called a completed preview. It must not be called a formally completed course.

## Required learning content

Every final artifact contains:

1. learner and outcome;
2. prerequisites and expected time;
3. learning path or unit structure;
4. learner-appropriate explanations, examples, and practice;
5. checks for understanding;
6. source and provenance notes;
7. integrity gaps, uncertainty, and access limitations;
8. compression or omission notes;
9. next steps, including when to return to the original source.

## Canonical content and format parity

For formal three-format delivery:

1. write Markdown as the canonical content master;
2. derive HTML and PDF from the same approved content rather than rewriting them independently;
3. preserve equivalent title, unit order, explanations, examples, exercises, checks, source notes, integrity gaps, compression notes, and next steps;
4. return downloadable links or file paths supported by the host for all three files.

Equivalent does not mean byte-identical. Navigation, pagination, and format-specific styling may differ while the learning substance remains the same.

## Self-contained HTML

The HTML edition must be a complete document with:

- semantic heading hierarchy;
- a navigable table of contents;
- readable responsive typography;
- accessible and descriptive link text;
- print styles;
- no required remote runtime dependency;
- working internal navigation and local assets.

Prefer embedded styles and small embedded assets. If a local asset is necessary, keep it beside the artifact and verify the link rather than assuming it resolves.

## PDF

The PDF edition must:

- preserve headings and usable source links;
- use embedded or reliably available fonts for every language used;
- contain extractable text unless the requested source genuinely requires image-only pages;
- avoid clipped text, broken tables, unintended blank pages, orphaned headings, and poor page breaks.

Use available document or PDF capabilities for creation and visual inspection. Do not treat successful file generation as visual verification.

## Pre-delivery verification

Before claiming completion, verify:

- every required file exists and is non-empty;
- every delivered format contains the required learning-content elements;
- the learning structure and substantive content are equivalent across formats;
- HTML navigation, links, and local assets work;
- PDF page count is non-zero and text is extractable;
- non-Latin characters, including Chinese when present, render correctly;
- representative PDF pages have been visually inspected, including a title page, a dense lesson page, a table or list page when present, and a source-notes page;
- no representative page shows clipping, unintended blank space, broken tables, missing glyphs, or bad heading breaks.

Report completed checks briefly with the final links.

## Missing capabilities or failed rendering

Required formats do not become optional because a renderer is missing or generation fails.

When a required format cannot be produced:

1. preserve and validate any completed formats;
2. name the blocked format and the unavailable capability or error;
3. state the exact remaining work;
4. report partial progress without claiming formal completion.

Do not silently downgrade a formal complete delivery to Markdown only.
