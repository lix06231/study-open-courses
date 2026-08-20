# Multi-format Publishing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make formal complete-course deliveries default to verified Markdown, HTML, and PDF files.

**Architecture:** Add a positive output contract to the publishing stage, keeping Markdown as the canonical content source and deriving HTML/PDF from it. Preserve a narrow exception for previews and explicit single-format requests, with visible failure when a required renderer is unavailable.

**Tech Stack:** Markdown skill instructions, HTML, PDF tooling available in the runtime, Codex skill validation.

## Global Constraints

- The change applies to formal complete learning artifacts, not discovery or interim responses.
- Local file generation does not authorize external upload.
- Required formats cannot silently degrade to Markdown only.
- Repository and installed copies must end with identical `SKILL.md` hashes.
- Do not commit or push.

---

### Task 1: Record the failing behavior

**Files:**
- Create: `docs/validation/multi-format-baseline.md`

**Interfaces:**
- Consumes: Current installed skill and the complete-course request.
- Produces: Evidence that Markdown-only currently complies.

- [ ] Record the evaluator's FAIL result and exact publishing wording that caused it.

### Task 2: Add the publishing contract

**Files:**
- Modify: `SKILL.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: The approved multi-format design.
- Produces: A discoverable default output rule and user-facing documentation.

- [ ] Add the formal-delivery predicate and `.md + .html + .pdf` contract.
- [ ] Define Markdown as canonical and require cross-format equivalence.
- [ ] Define HTML and PDF quality checks.
- [ ] Define quick-preview and explicit-format behavior separately.
- [ ] Define visible blocking behavior when a renderer is unavailable.
- [ ] Update README examples and final-delivery explanation.

### Task 3: Verify and install

**Files:**
- Create: `docs/validation/multi-format-results.md`
- Modify: `C:\Users\lee\.codex\skills\study-open-courses\SKILL.md`

**Interfaces:**
- Consumes: Updated repository skill.
- Produces: Structural and behavioral evidence plus an identical installed copy.

- [ ] Run `quick_validate.py` on the repository skill.
- [ ] Re-run the same complete-course scenario and require PASS.
- [ ] Test preview, explicit PDF-only, and missing-renderer cases for correct routing.
- [ ] Copy the validated `SKILL.md` to the installed skill directory.
- [ ] Run validation on the installed copy and compare SHA-256 hashes.
- [ ] Report Git status without committing or pushing.
