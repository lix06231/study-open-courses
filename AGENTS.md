# study-open-courses shared project rules

## Ownership

- This is a shared project. Primary Agent: `Codex`.
- Before editing, read `README.md`, `SKILL.md`, and every file under `.agent/`.
- Record active work in `.agent/TASKS.md`, file ownership in `.agent/OWNERSHIP.md`, and cross-agent context in `.agent/HANDOFF.md`.
- Two Agents must not edit the same file at the same time.

## Authoritative files

- `SKILL.md` and `references/` are the authoritative runtime source because the repository must remain directly installable as an Agent Skill.
- `docs/validation/` stores behavioral evidence. A claim that the Skill is fixed requires a recorded RED failure and GREEN result.
- `deliverables/` is reserved for validated release packages and reports; do not duplicate working source there.

## Paid-resource boundary

- Paid, subscription-gated, trial-gated, credit-gated, institution-entitled, or purchase-linked instructional content is report-only.
- The Agent may mention a paid resource from public metadata when it is especially suitable, but must state that payment is required and must continue looking for free-access alternatives.
- The Agent must not open gated lessons, use a user's paid login state, download, record, capture, transcribe, OCR, extract, translate, or reconstruct paid instructional content, even when the user has purchased it or explicitly authorizes the action.
- A public preview or official free edition is a separate, limited source. Never use it to infer or reconstruct gated portions.

## Git and release boundary

- Local branches and commits are allowed for approved project work.
- Do not push, open a pull request, merge, publish a release, or modify a remote without separate user authorization.
- Preserve unrelated user changes and never commit credentials, cookies, tokens, paid-course media, transcripts, or private learner data.
