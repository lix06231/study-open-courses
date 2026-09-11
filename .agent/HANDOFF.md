# Handoff

## Current state

- Primary Agent: Codex
- Active branch: `codex/v4.1-deterministic-pipeline`
- Repository root: `D:\Lix-Agent\02-Shared-Projects\study-open-courses`
- Remote changes: `codex/v4.1-deterministic-pipeline` was pushed to `origin` on 2026-09-11; merge, release creation, and marketplace publication remain separate actions.
- Runtime version in this repository: 4.1.0
- Implementation status: the v3.2 policy gates are preserved. v4.1 adds a deterministic init/build/seal/validate pipeline, machine-readable run and QA records, reconciled item coverage, exact artifact hashes, offline standalone assets, printable `<details>` answers, source-locator checks, and course-pack path containment.
- v3.2.1 adds a hard delivery-intent contract after a Kilo run downgraded “帮我写一份课程” and substituted multi-file HTML/PDF output. Kilo's uncommitted v3.1 runtime overwrite was backed up before restoring v3.2.
- Installed copy: synchronized to v4.1.0; the previous v3.2.2 copy is preserved at `C:\Users\lee\.codex\skills\study-open-courses.backup-20260907-2045`.

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
- The 2026-09-11 user request authorizes this v4.1 branch push only; merge, release creation, and marketplace publication remain separate actions.
