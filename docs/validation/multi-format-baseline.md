# Multi-format publishing baseline

Date: 2026-08-20

Request evaluated: “请使用 study-open-courses 把已确认且内容完整的一门课程重构成正式完整课程，做好后给我可下载成果。”

An independent evaluator read the installed v3 skill and returned **FAIL** for the invariant “formal complete-course delivery defaults to `.md + .html + .pdf`.”

Observed behavior:

- no file extension was mandatory;
- Markdown-only complied if it contained the nine required content elements;
- HTML and PDF were not required;
- the phrases “Match the artifact to the suitability decision,” “Every final artifact must contain,” and “Publishing means preparing the artifact” governed artifact type, content, and upload authorization but not output format.

This failure justifies a positive output-shape contract rather than another general warning.
