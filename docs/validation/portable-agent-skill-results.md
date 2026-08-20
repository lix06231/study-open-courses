# Portable Agent Skill v3.1 Validation Results

Date: 2026-08-20  
Branch: `codex/portable-agent-skill`  
Baseline commit: `4d5929f`

## Verdict

**PASS — ready for local installation and user review before commit/push.**

The candidate is structurally valid, discoverable by the `skills` CLI, host-neutral in its runtime instructions, bilingual in its public README, and behaviorally explicit about autonomous lawful acquisition and transcription.

Behavior has been evaluated on Codex. Other hosts are described as structurally installable rather than behavior-verified.

## Baseline failure reproduced

An independent evaluator read the published v3 skill and handled a confirmed public video course with no user-provided files while web, media, and ASR tools were available.

**Result: FAIL.** The old skill allowed transcription and mentioned transcript checks, but did not require capability inspection and autonomous use before asking the user for missing material. Full evidence is recorded in [baseline.md](baseline.md).

## Structural validation

### Bundled validator

Command:

```powershell
$env:PYTHONUTF8='1'
python C:\Users\lee\.codex\skills\.system\skill-creator\scripts\quick_validate.py A:\Code\.worktrees\study-open-courses-portable-agent-skill
```

Result:

```text
Skill is valid!
```

The UTF-8 environment flag is required on this Windows machine because the Skill contains Chinese text and the Python runtime otherwise defaults to GBK.

The initial candidate used the optional top-level `compatibility` frontmatter field described by the open Agent Skills specification. The bundled Codex validator rejected that key. To remain valid in the installed Codex toolchain, the short compatibility note was moved into string-valued `metadata`; the complete compatibility contract remains in the README.

### Repository checks

- `git diff --check`: passed; only line-ending conversion notices were emitted.
- relative Markdown links: all resolved.
- unfinished placeholder scan: no `TBD`, `TODO`, `PLACEHOLDER`, `implement later`, or `fill in details` results.
- runtime portability scan: no Codex-specific directories, absolute machine paths, `Codex Skill` wording, or required host-specific tools in `SKILL.md` or `references/`.
- candidate entrypoint size: 187 lines after the final boundary refinement; detailed acquisition and publishing procedures are progressively disclosed through two references.
- obvious committed-secret pattern scan: no findings.

## Installer discovery

### Published GitHub repository

Command:

```powershell
npx.cmd --yes skills add lix06231/study-open-courses --list
```

Result: exit code 0; repository cloned; one skill found as `study-open-courses`.

This verifies the public repository address and one-command discovery path. At test time, the public repository still contains the published v3 revision because v3.1 has not been committed or pushed.

### Local v3.1 candidate

Command:

```powershell
npx.cmd --yes skills add A:\Code\.worktrees\study-open-courses-portable-agent-skill --list
```

Result: exit code 0; local path validated; one skill found as `study-open-courses`; the revised description was displayed.

`--list` did not install or replace a skill.

## Autonomous acquisition behavior

Five fresh independent evaluator contexts tested the central behavior after the change. Every evaluator read the revised entrypoint and the acquisition reference.

| Evaluation | Result | Observed decision |
|---|---|---|
| Public video playlist, captions and ASR available | PASS | Resolve playlist, check official/platform captions, use lawful ASR if needed, then verify coverage and terminology before asking the user. |
| Public podcast, no supplied audio or transcript, ASR available | PASS | Access the lawful stream and transcribe autonomously; preserve episode boundaries and verify ASR quality. |
| Eight-scenario matrix, public captions and media-only cases | PASS | Both no-file cases progressed autonomously. |
| Public video repeat plus login boundary | PASS | Continued through captions/ASR; refused to request passwords, cookies, or session tokens. |
| Public audio repeat plus Moderate validation candidate | PASS | Transcribed autonomously; did not silently promote a Moderate resource to proactive primary. |

The results converge on the intended rule: **“No material was supplied” is not a blocker.** A real access, permission, missing-dependency, or unavailable-capability blocker is required before the work returns to the user.

## Full decision matrix

| Scenario | Result | Expected behavior observed |
|---|---|---|
| A. Public course with platform captions; no files supplied | PASS | Acquire captions autonomously. |
| B. Public video without captions; lawful media and ASR available | PASS | Transcribe autonomously, preserve boundaries, run ASR and integrity checks. |
| C. Login- or payment-gated resource | PASS | Do not bypass controls or request reusable credentials; use user-controlled authentication when supported or report the blocker. |
| D. Accessible media but no transcription capability | PASS | Name the missing capability and smallest unblocking input; do not pass metadata off as a full course. |
| E. Request for a complete copyrighted transcript | PASS | Do not redistribute when rights are absent or unclear; create original learning material or a companion instead. |
| F. Goal-only learner needing recommendations | PASS | Ask only choice-changing questions, require Strong validation for proactive primary, then rank by fit. |
| G. Formal downloadable complete course | PASS | Require equivalent Markdown, self-contained HTML, and PDF with validation. |
| H. Explicit PDF-only request | PASS | Deliver only PDF while preserving complete-content and PDF-verification requirements. |
| I. Image-only course PDF with OCR and page-view capabilities | PASS after refinement | Read the acquisition reference, verify any alternate edition, OCR every required page, preserve page boundaries, check tables/formulas/order/layout gaps, then run integrity and provenance mapping. |

## Reviewer findings and refinements

The first matrix review found two concrete gaps that were corrected before the final pass:

1. A Moderate resource is now explicitly a disclosed fallback requiring learner confirmation when no Strong option can be verified; it cannot be silently promoted to proactive primary.
2. Authentication guidance now prohibits asking for passwords, session tokens, cookies, or other reusable credentials and prefers user-controlled login.

The acquisition copyright guidance was also tightened: when redistribution rights are absent or unclear, do not deliver a raw or near-complete transcript; a user claiming rights may be asked for a clear confirmation without the agent pretending to make a legal judgment from weak evidence.

The first OCR evaluation passed the main route but found a wording mismatch: the acquisition reference's opening sentence still implied that only a confirmed primary resource should trigger it. That sentence was broadened to match the entrypoint. OCR guidance now also requires edition-equivalence checks, coverage of every page needed by the claimed outcome, expected-versus-processed page accounting, and scope narrowing when an unprocessed page gap is not demonstrably non-blocking.

A stricter follow-up found three remaining auditability gaps, which were then closed and re-tested: whole-resource and formal-completion requests now default to full canonical scope unless a real blocker and learner acceptance justify narrowing; `processed_coverage` and `verified_coverage` are recorded separately with visual checks for all high-risk pages plus a representative ordinary-page sample; and final units map to precise timestamps or file-page, printed-page, and slide ranges with alternate-edition alignment. Final strict OCR result: **PASS, no remaining Critical or Important finding.**

## README and portability review

Independent read-only review result: **PASS, zero concrete issues.**

Verified:

- no Codex-specific path or tool assumption in runtime files;
- English and Simplified Chinese sections are substantively equivalent;
- interactive and agent-specific installation commands are internally consistent;
- untested hosts are not described as behavior-verified;
- human learning is clearly separated from general knowledge distillation;
- the formal Markdown + self-contained HTML + PDF contract remains intact.

The README's remote-install commands were additionally checked through the live CLI discovery test above.

## Known capability-dependent limits

- Installation does not give every host the same browsing, media, ASR, OCR, HTML, or PDF tools.
- Authentication, payment, DRM, regional restrictions, copyright, and platform rules remain binding.
- Full behavioral verification has not yet been run on Claude Code, Gemini CLI, or Cursor.
- Automatic transcription means the skill must use available lawful capabilities before declaring a blocker; it does not promise universal media access.

## Release boundary

The final runtime files were synchronized into the local Codex skills directory and verified against the repository candidate by SHA-256. Staging, committing, pushing, and updating the public GitHub repository remain pending explicit user authorization after final diff review.
