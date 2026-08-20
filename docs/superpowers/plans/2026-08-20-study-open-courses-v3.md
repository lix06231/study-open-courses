# study-open-courses v3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a new, installable `study-open-courses` skill that turns trustworthy source material into human-learning artifacts while preserving learner fit, integrity, and provenance.

**Architecture:** Keep the first release self-contained at the repository root with `SKILL.md` as the executable workflow and `README.md` as the human-facing positioning document. Treat resource discovery/acquisition and learning reconstruction as separate phases connected by explicit integrity and provenance gates.

**Tech Stack:** Markdown, YAML frontmatter, Git, Codex skill validator.

## Global Constraints

- The skill serves human learning, not model knowledge injection.
- It is not a universal content distiller.
- Community validation is an admission gate for proactive primary recommendations; learner fit determines ranking after admission.
- User-specified resources may be processed despite weak validation, but the limitation must be disclosed.
- Source acquisition, integrity verification, reconstruction, compression, and publishing remain distinguishable stages.
- Do not create a GitHub repository, add a remote, commit, push, or open a pull request without separate authorization.

---

### Task 1: Establish the behavioral baseline

**Files:**
- Create: `docs/validation/baseline.md`

**Interfaces:**
- Consumes: The approved v3 design and realistic learning requests.
- Produces: Observed failure patterns that `SKILL.md` must correct.

- [ ] **Step 1: Define baseline scenarios**

Record requests that expose the important decisions:

1. A beginner with two hours and no named resource asks to learn AI.
2. A user names a new course with almost no learner evidence.
3. A famous advanced course competes with a well-validated beginner course.
4. A user asks to turn a novel into a two-hour distilled course.
5. A course landing page exposes only a syllabus.
6. Multiple transcripts contain missing and duplicated lessons.

- [ ] **Step 2: Run scenarios without the new skill**

Use a fresh evaluator without showing it the approved v3 design. Capture whether it overweights fame or views, skips provenance, accepts a syllabus as content, compresses before reconstruction, or treats experiential work as replaceable.

- [ ] **Step 3: Record exact findings**

Write `docs/validation/baseline.md` with scenario, observed decision, failure or success, and the specific guidance needed. Do not invent failures that were not observed.

### Task 2: Write the installable skill

**Files:**
- Create: `SKILL.md`
- Create: `.gitignore`

**Interfaces:**
- Consumes: `docs/validation/baseline.md` and the approved design.
- Produces: An automatically discoverable skill with a complete v3 decision workflow.

- [ ] **Step 1: Write frontmatter and scope**

Use the exact skill name `study-open-courses`. The description must trigger on choosing, acquiring, reconstructing, compressing, or publishing open learning resources and must exclude generic summarization or model-memory tasks.

- [ ] **Step 2: Encode entry routing and selection gates**

Specify the named-resource route and goal-only route. Define lightweight questions, resource discovery, Community Validation classifications, and Learner Fit Ranking without requiring fake numerical precision.

- [ ] **Step 3: Encode suitability and source handling**

Define the three Learning Suitability outcomes. Separate Source Resolver from Content Ingestion and require lawful, complete, real instructional content rather than landing-page metadata.

- [ ] **Step 4: Encode integrity and provenance**

Require coverage, order, duplicate, gap, transcript, and version checks. Require source URL, version/date, lesson mapping, missing material, and uncertainty records.

- [ ] **Step 5: Encode reconstruction, compression, and publishing**

Make reconstruction learner-centered with prerequisites, explanation, examples, practice, and checks for understanding. Permit compression only afterward and require publication output to expose sources, limitations, omissions, and next steps.

- [ ] **Step 6: Add a minimal `.gitignore`**

Ignore operating-system files, editor settings, temporary validation output, caches, and secrets without hiding the skill or documentation.

### Task 3: Explain product positioning

**Files:**
- Create: `README.md`

**Interfaces:**
- Consumes: The final `SKILL.md` terminology and workflow.
- Produces: A human-readable explanation consistent with the executable skill.

- [ ] **Step 1: Explain the learner-first promise**

Describe the product as verified resource selection plus faithful source acquisition plus learning reconstruction. Include the short principle: “大众验证负责入围，学习适配负责排名.”

- [ ] **Step 2: Contrast adjacent approaches**

Add a comparison covering target user, accepted inputs, acquisition/reconstruction separation, traceability, compression policy, and final artifact. Explain which cangjie-style ideas are borrowed and which universal-distillation/model-injection assumptions are rejected.

- [ ] **Step 3: Document workflow and installation**

Show the v3 stages, supported input types, limits, repository layout, local installation concept, and an example request without claiming unavailable automation.

### Task 4: Validate behavior and packaging

**Files:**
- Create: `docs/validation/v3-results.md`
- Modify: `SKILL.md` only when observed validation results justify a correction.
- Modify: `README.md` only when it contradicts the validated skill.

**Interfaces:**
- Consumes: Completed `SKILL.md`, README, baseline scenarios, and the local validator.
- Produces: Evidence that v3 changes the target decisions and remains installable.

- [ ] **Step 1: Run structural validation**

Run:

```powershell
$env:PYTHONUTF8 = '1'
python C:\Users\lee\.codex\skills\.system\skill-creator\scripts\quick_validate.py A:\Code\study-open-courses
```

Expected: the validator reports a valid skill with no malformed frontmatter or scaffold placeholders.

- [ ] **Step 2: Re-run the behavioral scenarios with the skill**

Verify the evaluator asks only material questions, applies Community Validation before fit ranking, warns but accepts user-specified weak resources, routes experiential work appropriately, refuses metadata-only ingestion, and exposes gaps and provenance.

- [ ] **Step 3: Compare baseline and v3**

Write `docs/validation/v3-results.md` with observable outcomes for every scenario. Label remaining unknowns rather than claiming success without evidence.

- [ ] **Step 4: Review repository state**

Run:

```powershell
git -C A:\Code\study-open-courses status --short --branch
git -C A:\Code\study-open-courses diff --check
```

Expected: only intended untracked or modified files, no whitespace errors, no remote mutation, and no commit.

- [ ] **Step 5: Stop before Git publication**

Report the validated files and current Git state. Ask for separate authorization before any commit, remote creation, push, or pull request.
