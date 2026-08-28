# Publishing and Delivery

Read this reference when preparing downloadable files or claiming a learning artifact is formally complete. Complete Learning QA first under [learning-quality.md](learning-quality.md); format polish cannot turn `learning_qa: fail` into a completed artifact.

Publishing means preparing and validating the artifact. It never authorizes an external upload, post, repository creation or change, commit, push, or other remote mutation.

## Choose the delivery contract

| Request state | Required delivery |
|---|---|
| **Formal complete learning artifact** | Create three downloadable files: Markdown (`.md`), one literally self-contained HTML file (`.html`), and PDF (`.pdf`). |
| **Quick preview, outline, recommendation, or interim checkpoint** | Return the smallest useful format, normally Markdown in chat or as a file. |
| **User explicitly requests particular format or formats** | Deliver exactly those formats; do not add unwanted formats. |

A request to complete, finish, publish, make the full course, or provide a downloadable final course counts as a formal complete artifact unless the user explicitly narrows the output.

A preview may be called a completed preview. It must not be called a formally completed course.

## Required content by artifact level

Metadata indexes, source coverage maps, and curriculum maps use their artifact-specific schemas in [learning-quality.md](learning-quality.md). They need only the format requested by the user or the smallest useful durable format; they do not require invented instructional explanations, exercises, learner checks, or the three-format course bundle. A `report_only` resource may publish a metadata index when that level's gate passes.

Every reconstructed learning artifact or other learner-ready teaching artifact contains:

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

The HTML edition must be exactly one complete `.html` file that remains usable after download with network access disabled. It must contain every required style and every required small permitted asset inside that file: use embedded CSS and embedded data assets or inline SVG where applicable. It must not require a sibling stylesheet, script, image, font, media file, or remote runtime dependency.

The one-file HTML edition must also contain:

- semantic heading hierarchy;
- a navigable table of contents;
- readable responsive typography;
- accessible and descriptive link text;
- print styles;
- no required remote runtime dependency; and
- working internal navigation.

If required sidecar assets are explicitly requested or genuinely needed, deliver and verify them as an **offline package** with its file list and paths. Do not call that package self-contained HTML, and do not silently substitute it for the required one-file HTML edition.

## PDF

The PDF edition must:

- preserve headings and usable source links;
- use embedded or reliably available fonts for every language used;
- contain extractable text unless the requested source genuinely requires image-only pages;
- avoid clipped text, broken tables, unintended blank pages, orphaned headings, and poor page breaks.

Use available document or PDF capabilities for creation and visual inspection. Do not treat successful file generation, file existence, non-zero bytes, page count, or extractable text alone as visual verification. A PDF with clipped text, broken tables, unintended blank pages, missing glyphs, unusable links, or other material rendering damage has **failed**; correct the source or rendering settings and generate it again. When practical, test another available renderer before reporting the PDF blocked.

## Pre-delivery verification

Before claiming completion, verify the declared artifact level's own schema, current QA pass, provenance, scope, and absence of blockers. Apply the remaining file and format checks only to formats actually required for that artifact level. For a formal reconstructed learning artifact, verify:

- `learning_qa: pass` is recorded for the declared artifact and scope;
- every required file exists and is non-empty, while recognizing that this alone never establishes completion;
- every delivered format contains the required learning-content elements;
- the learning structure and substantive content are equivalent across formats;
- HTML is one self-contained file, its navigation and links work, and no required sidecar or remote asset remains;
- PDF page count is non-zero and text is extractable;
- non-Latin characters, including Chinese when present, render correctly;
- representative PDF pages have been visually inspected, including a title page, a dense lesson page, a table or list page when present, and a source-notes page;
- no representative page shows clipping, unintended blank space, broken tables, missing glyphs, unusable links, or bad heading breaks.

Any material PDF defect found in these checks is a failed PDF, not a warning. Correct and re-render it, use another available renderer when practical, or report the PDF as blocked and the delivery as partial. Report completed checks briefly with the final links.

## Missing capabilities or failed rendering

Required formats do not become optional because a renderer is missing, a PDF is damaged, or generation fails.

When a required format cannot be produced:

1. preserve and validate any completed formats;
2. name the blocked format and the unavailable capability or error;
3. state the exact remaining work;
4. report partial progress without claiming formal completion.

Do not silently downgrade a formal complete delivery to Markdown only.
