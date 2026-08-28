# Project changelog

## 2026-08-28

- Migrated the existing Git repository to `D:\Lix-Agent\02-Shared-Projects\study-open-courses` as a shared project.
- Verified 100 files, 235,848 bytes, zero SHA-256 mismatches, HEAD `683238c`, and a clean `git fsck` before deleting the A-drive copies.
- Designated Codex as Primary Agent and started the v3.2 execution-hardening work on branch `codex/v3.2-execution-hardening`.
- Recorded a new paid-course baseline: v3.1 allows an Agent to use an authenticated paid course and transcribe it when the user authorizes access.
- Added the v3.2 Free-Access Processing Gate. Paid and entitlement-gated instructional content is report-only even after purchase, login, or explicit authorization; especially suitable paid resources may be disclosed only as manual-study options while free alternatives are sought.
- Added explicit artifact levels, persistent run-ledger state, five coverage totals, resume-first execution, batch failure isolation, provisional reconstruction, and deadline scope freeze.
- Added complete speech/visual/practice/attachment acquisition, visual-only teaching checks, stronger ASR verification, translation verification, and expanded source-manifest fields.
- Added artifact-level Learning QA before every exact completion label, plus literal one-file HTML and damaged-PDF failure rules.
- Updated the English and Chinese README for v3.2 and added `docs/validation/v3.2-results.md` with decision-scenario and mechanical validation evidence.
- Added representative verbatim evidence from three fresh simulated evaluator groups covering paid-resource pressure, access classification, resumption, multimodal gaps, ASR, translation, deadlines, Learning QA, self-contained HTML, and damaged PDF behavior.
- Corrected README validation wording to distinguish simulated evaluator behavior from static/structural checks and from untested hosts or models; synchronized completed implementation-plan checkboxes and project state.
- Persisted stable raw evaluator reports with complete prompts and returned outputs, model/reasoning identity, date/time zone, exact tested commit `f789cb0`, and the later evidence-recording boundary.
- Kept release boundaries unchanged: no push, merge, publication, release, or installed-copy synchronization was authorized or performed.
