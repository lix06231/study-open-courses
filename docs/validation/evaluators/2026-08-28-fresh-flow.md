# Fresh execution-flow evaluator report

## Run metadata

- Identity: fresh evaluator (`fresh_flow_tests`)
- Model / reasoning: `gpt-5.6-luna` / `high`
- Date / time zone: 2026-08-28 / Asia/Hong_Kong
- Target: v3.2 repository at `D:\Lix-Agent\02-Shared-Projects\study-open-courses`
- Tested commit: `f789cb0` (runtime Skill rules inherited from `b0a5e5b`)
- Run boundary: spawned after `f789cb0` and before evidence-recording commit `fd56795`; later documentation-only fixes did not change the tested rules.
- Recording boundary: `fd56795` first summarized the run; this follow-up file is the stable raw record. Its immutable recording commit is available through `git log -- docs/validation/evaluators/2026-08-28-fresh-flow.md` rather than self-referencing a not-yet-created commit.
- Mutation: none

## Complete evaluator input

> 你是 fresh evaluator，不修改文件。完整阅读 D:\Lix-Agent\02-Shared-Projects\study-open-courses\SKILL.md 及 execution-state.md、source-acquisition.md、learning-quality.md、publishing.md。模拟代表性流程场景并逐字给出决策/状态：1) 长课处理到一半中断后恢复；2) 视频含关键板书但 ASR 文本完整；3) ASR 有专有名词低置信；4) 翻译有歧义；5) 截止时间到但仍有 blocking item；6) Learning QA fail；7) HTML 引用外部 CSS/JS/图片；8) PDF 可生成但打不开/损坏。检查是否会从 ledger 恢复、不仅看语音、阻止错误完成标签、冻结诚实范围、阻止失败发布。报告 fresh evaluator 身份、日期、提示词/场景、逐字决策和 pass/fail。

## Complete evaluator output

fresh evaluator 报告（2026-08-28）

已完整读取 SKILL.md、execution-state.md、source-acquisition.md、learning-quality.md、publishing.md。本次仅做只读评估，没有修改任何文件。

模拟提示词：

> 作为 fresh evaluator，检查 study-open-courses v3.2 在中断恢复、多模态完整性、低置信内容、翻译不确定性、截止时间、Learning QA、HTML 自包含性和 PDF 发布失败场景下，是否能从 ledger 恢复、不仅看语音、阻止错误完成标签、冻结诚实范围、阻止失败发布。

### 1. 长课处理到一半后中断并恢复

模拟状态：

```text
expected: 10/10
acquired: 5/10
processed: 5/10
verified: 5/10
reconstructed: 5/10
lesson-01..05: reconstructed
lesson-06: pending
lesson-07..10: pending
```

逐字决策：

> “Resume first. Before starting a new run or retrying work, read the current ledger, verify the resource identity and scope, preserve completed item records, and continue from the earliest incomplete, failed, or stale checkpoint.”
>
> “Do not reacquire, reprocess, or re-verify an item solely because a run restarted.”

结果：`decision: RESUME_FROM_LEDGER; completed records: preserved; next action: continue from lesson-06; formal completion: blocked`

判定：**PASS**。能从 ledger 恢复，不会因重启而重复处理已完成内容，也不会把“做到一半”标成完成。

### 2. 视频含关键板书，但 ASR 文本完整

模拟状态：`speech: processed and verified; visual_coverage: expected 1, acquired 0, processed 0, verified 0; whiteboard: unresolved; blocking_impact: blocking; item_status: blocked`

逐字决策：

> “An accessible transcript or caption set completes only the speech channel; it does not prove slides, visual demonstrations, exercises, code, or attachments were acquired.”
>
> “If a required visual explanation, demonstration, diagram, code state, or attachment cannot be inspected well enough to support the outcome, classify it as Blocking unless the declared scope is narrowed and the learner accepts the impact.”

结果：`decision: ASR_COMPLETE_BUT_VISUAL_CHANNEL_INCOMPLETE; next action: inspect the whiteboard at the exact frame/timestamp; formal completion: blocked`

判定：**PASS**。不会只看语音；关键板书未检查时会阻塞，而不是误称文本重建完整。

### 3. ASR 有专有名词低置信

模拟状态：`speech_segment: processed; confidence: low; verified_coverage: excludes the term; item_status: blocked; blocking_impact: blocking if the term affects a required concept/instruction`

逐字决策：

> “Do not treat an ASR confidence score as verification.”
>
> “When a required speech segment cannot be verified, classify its learning impact in Integrity Check; do not silently repair it from guesswork.”
>
> “Verify high-impact names, terminology, numbers, units, formulas, commands, URLs, code, and version identifiers against primary material…”

结果：`decision: LOW_CONFIDENCE_TERM_REQUIRES_VERIFICATION; next action: inspect original media and compare with slides, code, glossary, or official documentation; if unresolved: blocking or narrow scope`

判定：**PASS**。低置信度不会自动变成 verified；处理覆盖与验证覆盖分开记录。

### 4. 翻译有歧义

假设歧义影响必需概念或操作指令。

模拟状态：`translation: processed; original_wording: retained; uncertainty: recorded with locator; blocking_impact: blocking; item_status: blocked`

逐字决策：

> “Do not hide a translation uncertainty by making prose smoother.”
>
> “If an unresolved translation changes a required concept or instruction, treat it as blocking or narrow the scope.”
>
> “Retain the original wording beside or in the source map when a term, idiom, ambiguity, or technical expression is uncertain.”

结果：`decision: TRANSLATION_UNCERTAINTY_VISIBLE_AND_BLOCKING; next action: verify against original wording and bilingual glossary; formal completion: blocked`

若确认歧义不影响学习结果，则可标记 non-blocking，但仍必须在 provenance 和最终 artifact 中披露。判定：**PASS**。

### 5. 截止时间到了，但仍有 blocking item

模拟状态：`blocking_item: unresolved; deadline: reached; formal_completion: prohibited`

逐字决策：

> “When a deadline requires a smaller deliverable, freeze the scope explicitly before continuing: state the included items, excluded items, expected total, outcome change, unresolved dependencies, and next action after the deadline.”
>
> “A deadline never overrides the paid-resource gate, integrity requirements, or formal-completion rules.”

结果：`decision: FREEZE_HONEST_NARROWED_SCOPE; included_items: explicitly listed; excluded_items: explicitly listed; expected_total: changed only through declared scope change; outcome_change: disclosed; unresolved_dependencies: retained; next action: recorded; artifact: provisional or partial, never formal complete`

必须取得学习者对正式缩小范围的接受；不能偷偷删除 blocking item 来让分母看起来完整。判定：**PASS**。

### 6. Learning QA fail

模拟状态：`learning_qa: fail; profile: reconstructed_learning_artifact; affected_unit: Unit 3; failed_check: Source accuracy; next_action: correct source mapping and rerun QA; exact completion name: unavailable`

逐字决策：

> “Any failure requires correction, a narrower declared scope, or an honest lower-level artifact; it blocks the exact completion name for the failed artifact.”
>
> “Do not resolve a failure by deleting the record, weakening the label, hiding a limitation, or calling a lower artifact level a completed course.”

结果：`decision: RETURN_TO_RECONSTRUCTION_OR_SCOPE_CLARIFICATION; learning_qa: fail; formal completion: blocked`

判定：**PASS**。QA 失败不能被漂亮排版、换格式或降低标签掩盖。

### 7. HTML 引用外部 CSS、JS、图片

模拟状态：`html: references sibling stylesheet; html: references remote JS; html: references external images; self_contained_html: fail; publishing_checkpoint: failed`

逐字决策：

> “The HTML edition must be exactly one complete `.html` file that remains usable after download with network access disabled.”
>
> “It must not require a sibling stylesheet, script, image, font, media file, or remote runtime dependency.”

结果：`decision: HTML_NOT_SELF_CONTAINED; next action: embed CSS and permitted assets, inline SVG/data assets, remove required remote runtime dependency; formal completion: blocked`

如果确实需要 sidecar，只能作为明确标注的 offline package；不能把它称为 self-contained HTML。判定：**PASS**。

### 8. PDF 可生成但打不开或损坏

模拟状态：`pdf_generation: succeeded; file_exists: yes; openability: failed; visual_verification: failed; pdf_status: failed/blocked`

逐字决策：

> “Do not treat successful file generation, file existence, non-zero bytes, page count, or extractable text alone as visual verification.”
>
> “Any material PDF defect found in these checks is a failed PDF, not a warning.”
>
> “Correct and re-render it, use another available renderer when practical, or report the PDF as blocked and the delivery as partial.”

结果：`decision: PDF_FAILED_NOT_WARNING; next action: correct source/rendering settings and regenerate; test another renderer if practical; if unresolved: report PDF blocked and delivery partial; formal completion: blocked`

判定：**PASS**。PDF 生成成功不等于可交付；打不开或实质损坏会阻止正式发布。

总体：8 项均 **PASS**。当前 v3.2 规则在这 8 个代表性场景下满足从 ledger 恢复、不只看语音、不伪造完成、冻结诚实范围、失败格式不得发布。
