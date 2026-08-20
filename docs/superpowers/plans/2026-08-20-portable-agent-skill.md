# Portable Agent Skill Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert `study-open-courses` into a portable, bilingual Agent Skill that autonomously resolves or transcribes lawful learning sources when users provide no content files.

**Architecture:** Keep a host-neutral `SKILL.md` as the compact workflow router. Move acquisition/transcription and multi-format publishing mechanics into two focused references, then describe installation, compatibility, examples, and boundaries in a complete English/Chinese README.

**Tech Stack:** Agent Skills Markdown/YAML format, Git, PowerShell 7, Python `quick_validate.py`, Vercel `skills` CLI.

## Global Constraints

- The product is for human learning, not general content distillation or model knowledge injection.
- Community Validation is the primary-resource admission gate; Learner Fit determines ranking.
- Acquisition and processing remain separate, with explicit integrity and provenance checks.
- When access is lawful and authorized and host tools exist, missing user-supplied material triggers autonomous caption discovery or transcription.
- Formal complete delivery defaults to equivalent Markdown, self-contained HTML, and PDF unless the user requests exact formats.
- Compatibility claims must separate format compatibility, installer support, and behavior verification.
- Do not commit, push, publish, upload, or mutate remote systems without separate authorization.

---

### Task 1: Establish behavioral and repository baselines

**Files:**
- Modify: `docs/validation/baseline.md`

**Interfaces:**
- Consumes: current `SKILL.md`, `README.md`, Git state
- Produces: evidence of the current transcription and portability gaps for Tasks 2–5

- [x] **Step 1: Record repository status and current structure**

Run read-only Git status, file listing, and line-count checks. Record the commit, cleanliness, and present files.

- [x] **Step 2: Run a no-new-guidance acquisition scenario**

Give an independent evaluator a confirmed public video course with no user-supplied transcript and ask it to decide the next action from the current skill. Record whether it is required to inspect caption/ASR tools and continue autonomously.

- [x] **Step 3: Audit Codex-specific wording**

Search `SKILL.md` and `README.md` for Codex paths, tool names, local-link assumptions, and claims of cross-agent support. Record each portability gap.

- [x] **Step 4: Preserve the baseline as test evidence**

Append a dated “portable v3.1 baseline” section to `docs/validation/baseline.md` containing observable results, not inferred intent.

### Task 2: Extract the source-acquisition contract

**Files:**
- Create: `references/source-acquisition.md`
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: confirmed primary resource, user authorization, host capabilities
- Produces: source manifest, integrity result, provenance map, or precise blocker

- [x] **Step 1: Write source-acquisition behavior checks**

Define expected outcomes for public captions, media-only plus ASR, login-gated media, unavailable ASR, and raw-transcript redistribution requests.

- [x] **Step 2: Create the focused acquisition reference**

Specify the source priority, autonomous continuation contract, blocker conditions, manifest fields, ASR quality checks, integrity classification, evidence mapping, and copyright boundary.

- [x] **Step 3: Route to the reference from `SKILL.md`**

Keep acquisition purpose and required outcome in the entrypoint. Require reading `references/source-acquisition.md` whenever a named or identifiable resource's real content must be assessed, acquired, reconstructed, compressed, or published.

- [x] **Step 4: Check progressive disclosure**

Verify that recommendation-only tasks do not need the detailed acquisition reference and that reconstruction tasks cannot skip it.

### Task 3: Extract the publishing contract and make it host-neutral

**Files:**
- Create: `references/publishing.md`
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: reconstructed learning master and requested delivery state
- Produces: requested downloadable artifact formats or an honest partial-delivery report

- [x] **Step 1: Preserve all current output invariants**

Carry forward the formal MD+HTML+PDF default, exact-format override, preview exception, content-equivalence checks, HTML navigation checks, PDF text and visual checks, and no-silent-downgrade rule.

- [x] **Step 2: Create the publishing reference**

Replace Codex-only local-path and tool language with host-neutral downloadable-link and capability language while preserving local-file delivery where supported.

- [x] **Step 3: Route publishing tasks from `SKILL.md`**

Require reading `references/publishing.md` only when preparing formal files or validating a final learning artifact.

- [x] **Step 4: Verify external mutation boundaries**

Confirm that “Publishing” prepares artifacts and never implies permission to push, upload, post, or create remote repositories.

### Task 4: Finalize the portable `SKILL.md`

**Files:**
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: learner request and conditional reference files
- Produces: host-neutral decisions across discovery, validation, suitability, acquisition, reconstruction, compression, and publishing

- [x] **Step 1: Update frontmatter**

Retain `name` and a third-person `Use when...` description. Add MIT license and string metadata for author, version, and a concise capability-dependent compatibility note. Keep the note in `metadata` so the package passes the bundled Codex validator, which currently rejects a top-level `compatibility` key.

- [x] **Step 2: Preserve the learner-first workflow**

Retain both entry routes, qualitative validation states, Learner Fit criteria, suitability outcomes, reconstruction requirements, compression boundaries, and stop conditions.

- [x] **Step 3: Remove host-specific assumptions**

Use generic “agent,” “host,” “available capabilities,” and “supported downloadable links or paths” wording. Keep platform examples illustrative rather than required.

- [x] **Step 4: Check scope boundaries**

Verify that arbitrary summarization, meeting digestion, entertainment condensation, and model knowledge injection remain out of scope.

### Task 5: Rewrite the bilingual README

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: final skill contract and verified installation behavior
- Produces: an English/Chinese public project page with runnable installation and accurate expectations

- [x] **Step 1: Build the English section**

Include promise, motivation, differentiators, workflow, installation, quick starts, autonomous acquisition/transcription, outputs, compatibility, limits, validation, structure, contributing, and license.

- [x] **Step 2: Build the complete Simplified Chinese section**

Provide the same substantive information naturally in Chinese rather than a shortened summary.

- [x] **Step 3: Add the primary one-command installer**

Use `npx skills add lix06231/study-open-courses -g`, plus clearly labeled non-interactive examples for supported agent identifiers.

- [x] **Step 4: Make compatibility claims evidence-bounded**

State that the package follows the Agent Skills format, the CLI recognizes named agents, Codex behavior is verified, and transcription/rendering still depend on host capabilities.

### Task 6: Validate behavior, structure, and installation discovery

**Files:**
- Create: `docs/validation/portable-agent-skill-results.md`
- Modify: files from Tasks 2–5 only if tests expose a defect

**Interfaces:**
- Consumes: completed repository candidate
- Produces: auditable pass/fail evidence and a release-readiness verdict

- [x] **Step 1: Run structural validation**

Run the bundled `quick_validate.py`, verify every relative reference, scan for placeholders, and run `git diff --check`.

- [x] **Step 2: Test repository discovery**

Run `npx skills add lix06231/study-open-courses --list` or the closest non-mutating CLI discovery command and capture the result.

- [x] **Step 3: Run independent forward scenarios**

Evaluate the nine scenarios in the design spec against the updated skill, including the scanned/image-only PDF and OCR case. Record each decision and whether it meets the expected contract.

- [x] **Step 4: Audit bilingual parity and links**

Check that both language sections include the same key promises, installation commands are internally consistent, and all repository links and relative files resolve.

- [x] **Step 5: Write the validation report**

Record commands, results, known capability-dependent limits, and a final release-readiness verdict without overstating cross-host testing.

### Task 7: Synchronize the local installation and prepare handoff

**Files:**
- Update after validation: `C:\Users\lee\.codex\skills\study-open-courses\SKILL.md`
- Update after validation: `C:\Users\lee\.codex\skills\study-open-courses\references\source-acquisition.md`
- Update after validation: `C:\Users\lee\.codex\skills\study-open-courses\references\publishing.md`

**Interfaces:**
- Consumes: validated repository candidate
- Produces: locally installed portable skill and an uncommitted Git diff ready for user review

- [x] **Step 1: Copy only the runtime skill files**

Synchronize `SKILL.md` and `references/` into the existing installed skill directory. Do not copy repository docs into the runtime package unless required.

- [x] **Step 2: Validate the installed copy**

Run `quick_validate.py` against the installed directory and inspect for accidental `study-open-courses/study-open-courses` nesting.

- [x] **Step 3: Review the complete Git diff**

Check status, changed-file scope, whitespace, secrets, unexpected binaries, and generated artifacts.

- [x] **Step 4: Stop before Git mutation**

Report the files and validation verdict. Request explicit authorization before staging, committing, or pushing the v3.1 changes.
