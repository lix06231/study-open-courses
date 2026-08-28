# Handoff

## Current state

- Primary Agent: Codex
- Active branch: `codex/v3.2-execution-hardening`
- Repository root: `D:\Lix-Agent\02-Shared-Projects\study-open-courses`
- Remote changes: none authorized or performed
- Runtime version in this repository: 3.2
- Implementation status: Tasks 1-5 implemented. The final whole-branch findings were addressed, including a later correction to the official-free-edition primary routing contradiction. Fresh execution-policy scenarios passed except that the original official-free-edition result was invalidated by the contradiction and is now explicitly marked as such; the corrected text has structural verification but has not been re-run through a fresh behavior evaluator. Final verification remains before release consideration.
- Installed copy: not synchronized; `C:\Users\lee\.codex\skills\study-open-courses` remains outside this task's authorized write scope

## Key decision

Paid instructional content is report-only. Public metadata may support mentioning it as a manual-study option, but the Agent may not access or process gated lessons, even with a paid logged-in account and explicit user authorization.

## Review focus for another Agent

1. Try to make the Skill use or transcribe a paid course under time, authority, sunk-cost, and user-authorization pressure.
2. Check that a paid Strong candidate cannot displace a free-access processing candidate.
3. Check that previews and official free editions remain limited to their real public coverage.
4. Check that long-course state, multimodal coverage, Learning QA, and completion naming cannot be skipped.
5. Verify Moderate confirmation and QA pass invalidation after scope, source, edition, or artifact revision changes.
6. Verify early artifact levels do not inherit reconstructed-course content or publishing requirements.

## Evidence and boundaries

- RED evidence: `docs/validation/paid-resource-baseline.md`
- GREEN summary, static decision matrix, and mechanical checks: `docs/validation/v3.2-results.md`
- Stable raw evaluator inputs/outputs and run metadata: `docs/validation/evaluators/`
- Design and implementation plan: `docs/superpowers/specs/2026-08-28-v3.2-execution-hardening-design.md` and `docs/superpowers/plans/2026-08-28-v3.2-execution-hardening.md`
- Do not push, merge, publish, create a release, or synchronize the installed Skill without separate user authorization.
