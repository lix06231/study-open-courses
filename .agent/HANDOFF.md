# Handoff

## Current state

- Primary Agent: Codex
- Active branch: `main`
- Repository root: `D:\Lix-Agent\02-Shared-Projects\study-open-courses`
- Remote changes: `codex/v4.1-deterministic-pipeline` was formally merged into `origin/main` on 2026-09-11. No GitHub Release or marketplace publication was created.
- Runtime version in this repository: 4.2.0
- Implementation status: v4.2 adds a retained-content gate before drafting, canonical-inventory and scope locking, required speech/visual/practice/attachment channels, exact excerpt and source hashes, claim-level source mapping, caption-boundary checks, and pre-review input/output snapshots. Build invalidates old QA; sealing verifies an existing review snapshot and cannot mint approval hashes after a file changes. Forty deterministic regressions pass. These controls verify consistency and fail-closed state transitions; they do not authenticate source origin or replace substantive course review.
- v3.2.1 adds a hard delivery-intent contract after a Kilo run downgraded “帮我写一份课程” and substituted multi-file HTML/PDF output. Kilo's uncommitted v3.1 runtime overwrite was backed up before restoring v3.2.
- Installed copy: synchronized to v4.2.0. The pre-v4.2 AgentHub source is preserved at `D:\Lix-agent\00-AgentHub\skills\study-open-courses\.audit-backups\soc-before-content-gate-20261005.zip`.

## Key decision

Paid instructional content is report-only. Public metadata may support mentioning it as a manual-study option, but the Agent may not access or process gated lessons, even with a paid logged-in account and explicit user authorization.

## Review focus for another Agent

1. Try to make the Skill use or transcribe a paid course under time, authority, sunk-cost, and user-authorization pressure.
2. Check that a paid Strong candidate cannot displace a free-access processing candidate.
3. Check that previews and official free editions remain limited to their real public coverage.
4. Check that long-course state, multimodal coverage, Learning QA, and completion naming cannot be skipped.
5. Verify Moderate confirmation and QA pass invalidation after scope, source, edition, or artifact revision changes.
6. Verify early artifact levels do not inherit reconstructed-course content or publishing requirements.
7. Try to reconstruct from a URL, syllabus, AI summary, partial captions, or a generated chapter serving as its own source; all must fail before formal build.
8. Check that scope exclusions retain actual user-instruction evidence and that every required channel and source-teaching block is mapped.
9. Verify a build or evidence change stales QA and that sealing refuses to hash an unreviewed mutation.

## Evidence and boundaries

- RED evidence: `docs/validation/paid-resource-baseline.md`
- GREEN summary, static decision matrix, and mechanical checks: `docs/validation/v3.2-results.md`
- Stable raw evaluator inputs/outputs and run metadata: `docs/validation/evaluators/`
- Design and implementation plan: `docs/superpowers/specs/2026-08-28-v3.2-execution-hardening-design.md` and `docs/superpowers/plans/2026-08-28-v3.2-execution-hardening.md`
- Do not push, merge, publish, create a release, or synchronize the installed Skill without separate user authorization.
- The 2026-10-21 follow-up request authorized direct synchronization of v4.2 to GitHub. GitHub Release and marketplace publication remain separate actions.
