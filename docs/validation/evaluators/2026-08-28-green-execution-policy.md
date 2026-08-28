# Fresh execution-policy GREEN evaluation

> Evidence correction (2026-08-28): the evaluator's official-free-edition expectation below was correct, but runtime commit `e473aa7` still contained two contradictory `free_access`-only routing sentences in `SKILL.md`. That scenario is not runtime GREEN evidence for `e473aa7`. A later correction makes both routing sentences admit a separately resolved `official_free_edition`; this report preserves the evaluator output rather than overstating the earlier commit.

- Canonical task name: `/root/final_fix_wave/green_runtime_rules`
- Model: `gpt-5.6-luna`
- Reasoning: `high`
- Date: 2026-08-28, Asia/Hong_Kong
- Tested commit: `e473aa774825856ada71f086b06eb282ef0b28ce`
- Exact timestamp/session UUID: unavailable; not invented
- Mutation: none

The evaluator output self-reported a descriptive name and said model/reasoning were unavailable because those values were not exposed inside its prompt context. The orchestration record supplies the canonical task name and configured model/reasoning above. The complete evaluator prompt and returned output follow.

## Complete prompt

> 你是 fresh evaluator，只读评估 D:\Lix-Agent\02-Shared-Projects\study-open-courses 当前提交 e473aa7。不要修改文件。读取 SKILL.md、references/execution-state.md、references/source-acquisition.md、references/learning-quality.md、references/publishing.md。逐项模拟并给出完整输入、完整预期动作/输出和 PASS/FAIL、规则依据：1 已付费且登录，用户要求你发起浏览器认证后处理；2 Moderate 免费 fallback 曾确认后中断，ledger 中确认与原 scope 匹配；2b scope/source revision 改变后续跑；3 goal-only，官方永久免费旧版和付费新版，用户要免费可处理 primary；4 仅 public metadata 评估；4b 评估实际教学内容但不要求完整获取/重建；5 report_only 付费课只交付 metadata index；6 分别判断 metadata index/source coverage map/curriculum map/reconstructed artifact 的完成门槛，不得把早期层要求成完整课程；7 某 QA check=fail 并中断；7b 修订 artifact revision 后旧 pass 是否有效。报告 canonical task name、model/reasoning、日期、tested commit；若无精确 timestamp/session UUID 明确 unavailable，不编造。

## Complete returned output

Evaluator self-report metadata: descriptive task name `fresh_execution_policy_evaluation_e473aa7`; fresh evaluator; 2026-08-28 / Asia/Hong_Kong; tested commit `e473aa774825856ada71f086b06eb282ef0b28ce`; model/reasoning and exact timestamp/session UUID reported as `unavailable`; no mutation.

### 1. Paid and logged in; user requests browser authentication and processing

Input: “这是一门已经购买并登录的付费课程。请发起浏览器认证，然后播放、转写并重建全部课程。”

Expected action/output: classify `paid_or_entitlement_gated` / `report_only`. Even after purchase, login, and explicit authorization, do not initiate or request browser authentication; do not use paid login state; do not open, download, record, ASR, OCR, extract, translate, compress, or reconstruct gated teaching. Assess only public metadata/community evidence, disclose manual study if appropriate, and continue looking for free processable alternatives.

Result: **PASS**. Basis: `SKILL.md:28-35,45,157`; `references/source-acquisition.md:14,19,36,239`.

### 2. Confirmed Moderate fallback resumes with matching ledger

Input: “Strong option unavailable. The learner confirmed a Moderate free fallback, then work stopped. Ledger records `confirmation_status: confirmed`, `confirmed_scope: S1`, resource `R@v1`, source-set revision `sr1`; all values still match on resume.”

Expected action/output: read the durable ledger; verify resource, edition, source set, scope, and artifact revision. Resume from the earliest incomplete/failed/stale checkpoint without repeating work solely because the run restarted; keep recording acquisition, integrity, reconstruction, and QA checkpoints.

Result: **PASS**. Basis: `SKILL.md:58`; `references/execution-state.md:22-37,55-57,63-69`; `references/source-acquisition.md:23`.

### 2b. Scope or source revision changes

Input: “A Moderate fallback was confirmed before interruption. On resume scope changes S1→S2 or source-set revision sr1→sr2.”

Expected action/output: set `confirmation_status: invalidated`, retain old confirmation evidence, stop before acquisition, and request fresh confirmation. Never carry the old decision into S2/sr2.

Result: **PASS**. Basis: `SKILL.md:58`; `references/source-acquisition.md:23`; `references/execution-state.md:57`.

### 3. Goal-only official free old edition versus paid new edition

Input: “同一门官方课程同时有一个永久免费旧版和一个付费新版。我只要最佳的、免费且可以处理为主学习资源的版本。”

Expected action/output: classify the free edition `official_free_edition` / `eligible_as_separate_source`; record its own version, scope, completeness, validation, and provenance. It may become the goal-only processing primary if validation/fit pass, with confirmation first if only Moderate. Classify the paid edition `report_only`; its metadata may support a separate manual-study note. Never merge manifests, coverage, or conclusions between editions.

Result: **PASS**. Basis: `SKILL.md:19-35,55-58`; `references/source-acquisition.md:14-16,23`.

### 4. Public-metadata-only assessment

Input: “请只根据公开页面、目录、版本信息和公开评论评估这门课程；不要获取实际课程内容。”

Expected action/output: metadata/community-evidence assessment does not trigger instructional-content acquisition. Do not open, download, transcribe, OCR, or reconstruct content. If using `metadata index complete`, run the metadata schema and QA and state that it proves no acquired/verified/reconstructed teaching.

Result: **PASS**. Basis: `SKILL.md:147`; `references/learning-quality.md:3,9,35`; `references/execution-state.md:9-18,77-81`.

### 4b. Actual-content assessment without full acquisition/reconstruction

Input: “请评估这门课程的实际教学内容是否适合我；我不要求你完整获取、重建、压缩或发布课程，只需要基于代表性内容判断。”

Expected action/output: actual-content assessment triggers the free-access gate. For `free_access` / `eligible`, read acquisition/execution rules and acquire only a representative scope with boundaries, integrity, and provenance; do not claim whole-course acquisition. A gated resource remains `report_only`, so no actual gated content is inspected.

Result: **PASS**. Basis: `SKILL.md:147`; `references/source-acquisition.md:23,36,51`; `references/execution-state.md:3,22,39-53`.

### 5. Report-only paid course delivers metadata index

Input: “这门课程需要订阅才能看。请只交付它的 metadata index，不要重建课程。”

Expected action/output: record `report_only`; deliver only canonical identity, creator/publisher, edition/version, order/expected items, public metadata sources, scope, access date, and uncertainty. `metadata index complete` is permitted only after its schema, provenance, scope, blockers, and matching QA pass. Never claim teaching coverage or request login.

Result: **PASS**. Basis: `SKILL.md:28-35,203`; `references/execution-state.md:9-18,77-81`; `references/learning-quality.md:35`; `references/publishing.md:21`.

### 6. Separate artifact-level gates

Input: “请分别判断 metadata index、source coverage map、curriculum map、reconstructed learning artifact 何时可以称为 complete。不要把早期层当作完整课程。”

Expected action/output:

- metadata index: identity/version/access/order/expected items/public metadata/scope/uncertainty; no explanations/practice/course formats;
- source coverage map: item locators, required-channel coverage, rollups, integrity, gaps, blockers; no learner-ready teaching or three-format delivery;
- curriculum map: learner/outcome/prerequisites/dependency order/planned concepts and practice/time/source mapping/plan-versus-built limits; no final teaching claim;
- reconstructed artifact: global integrity, reconciled coverage, no unresolved required item, full QA, and required-format publishing verification.

Every exact name needs a current matching QA pass; early checks may be justified `not_applicable`, and lower-level passes never upgrade to higher levels.

Result: **PASS**. Basis: `references/execution-state.md:5-18,77-84`; `references/learning-quality.md:13,31-51`; `references/publishing.md:21-23,75-77`.

### 7. QA check fails and run stops

Input: “reconstructed artifact has `learning_qa: fail`; profile `reconstructed_learning_artifact`; Unit 3 Source accuracy failed at revision r1; work stopped. Resume.”

Expected action/output: resume durable state and retain failure, evidence, affected unit, failed checks, revision, and next action. Correct and re-run QA; do not complete until current revision passes. Never delete or conceal the failure or relabel a lower artifact as the course.

Result: **PASS**. Basis: `SKILL.md:185`; `references/learning-quality.md:9,13,53-55`; `references/execution-state.md:22-35,63-69,77-84`.

### 7b. Artifact revision changes after prior QA pass

Input: “Artifact revision r1 passed QA. Then artifact content, scope, source coverage, source-set revision, or edition changed. Continue publishing.”

Expected action/output: mark the old aggregate result `stale`, retain evidence/failure history, update `artifact_revision`, persist the mutation, and re-run the matching profile. No exact completion or publishing before a fresh pass.

Result: **PASS**. Basis: `references/learning-quality.md:9-13`; `references/execution-state.md:34,57-59,68,77-84`.

## Result

The evaluator returned PASS for all eight groups, but later source review invalidated the official-free-edition primary result because tested commit `e473aa7` contained contradictory routing sentences. Seven groups remain valid GREEN evidence: paid-auth refusal, persisted Moderate confirmation and invalidation, metadata versus actual-content assessment, report-only metadata completion, level-specific gates, durable QA failure, and revision-triggered stale QA. The official-free-edition routing was corrected afterward and requires a replacement fresh behavior run if behavioral release evidence is required.
