# Multi-format publishing validation

Date: 2026-08-20

## Structural validation

`quick_validate.py` reported `Skill is valid!` for the updated repository skill. No trailing whitespace or unfinished placeholders were found in the changed skill, README, design, or plan files.

## Behavioral regression

An independent evaluator re-read the updated skill and tested four request states.

### A. Formal complete course with downloadable deliverables

**PASS.** Markdown, self-contained HTML, and PDF are mandatory. Completion requires all three files, absolute local links, cross-format content equivalence, HTML navigation checks, and PDF text/font/visual checks.

### B. Outline preview with no files requested

**PASS.** A lightweight Markdown response is allowed. It may be called a completed preview but not a completed formal-course delivery.

### C. Formal course explicitly requested as PDF only

**PASS.** The explicit-format route overrides the default bundle. Only the PDF is delivered and it must contain the complete artifact content and pass PDF verification.

### D. Formal complete course without a usable HTML/PDF renderer

**PASS.** The required formats do not silently disappear. The work cannot be called complete; the response must identify the blocked formats and exact remaining work.

## Conclusion

The previously failing invariant now passes: a formal complete learning artifact defaults to `.md + .html + .pdf`, while previews and explicit format requests retain appropriate flexibility.
