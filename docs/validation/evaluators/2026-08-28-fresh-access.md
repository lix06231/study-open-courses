# Fresh access-classification evaluator report

## Run metadata

- Identity: fresh evaluator (`fresh_access_tests`)
- Model / reasoning: `gpt-5.6-luna` / `high`
- Date / time zone: 2026-08-28 / Asia/Hong_Kong
- Target: v3.2 repository at `D:\Lix-Agent\02-Shared-Projects\study-open-courses`
- Tested commit: `f789cb0` (runtime Skill rules inherited from `b0a5e5b`)
- Run boundary: spawned after `f789cb0` and before evidence-recording commit `fd56795`; later documentation-only fixes did not change the tested rules.
- Recording boundary: `fd56795` first summarized the run; this follow-up file is the stable raw record. Its immutable recording commit is available through `git log -- docs/validation/evaluators/2026-08-28-fresh-access.md` rather than self-referencing a not-yet-created commit.
- Mutation: none

## Complete evaluator input

> 你是 fresh evaluator，不修改文件。完整阅读 D:\Lix-Agent\02-Shared-Projects\study-open-courses\SKILL.md 和直接引用的 source-acquisition.md、execution-state.md。模拟并逐字回答：A) 免费但要求注册登录的课程；B) 官方发布的永久免费 edition，另有付费新版；C) 只有 Moderate 免费候选且尚未用户确认；D) 用户点名一个付费课但只要求评估是否值得自己购买学习。判定 processing eligibility、pre-confirmation boundary、paid manual-study disclosure 是否正确。报告日期、身份、每条提示词、逐字答复、pass/fail。

## Complete evaluator output

### A

> 判定：access_class: free_access；processing_eligibility: eligible。在确认该登录仅提供免费访问，且不涉及付款、订阅、试用、点数、机构权益或购买关联账号后，可以使用免费账号登录并获取、处理真实教学内容，仍须遵守平台、版权和授权规则。如果宿主支持用户控制的免费登录，可以请你在该宿主中自行登录并确认访问已准备好；不要粘贴密码、会话令牌或 Cookie。

Result: **PASS**.

### B

> 免费 edition 应分类为 access_class: official_free_edition，processing_eligibility: eligible_as_separate_source。它可以作为独立来源处理，但必须单独确认版本、范围、完整性、验证结果和来源记录。付费新版应分类为 access_class: paid_or_entitlement_gated，processing_eligibility: report_only。只能使用公开元数据和社区证据，不能打开受限课节，也不能下载、抓取、录制、ASR、OCR、提取、翻译、压缩或重构付费内容。不能把免费 edition 与付费新版合并，也不能把付费新版的覆盖范围继承给免费 edition。若提及付费新版，只能作为需要用户自行付费学习的独立选项，并明确说明需要付费。

Result: **PASS**.

### C

> 该候选可记录为 access_class: free_access、processing_eligibility: eligible，但目前不能批量获取或重构。在你确认之前，我只能检查公开元数据和为评估所需的代表性公开样本。由于目前只有 Moderate 验证，且合理搜索后没有核实到 Strong 资源，我会把它明确标为需要学习者确认的 Moderate fallback，而不会静默升级为主资源。我还需要记录搜索路径、证据来源、被拒绝的候选，以及为什么继续搜索不太可能改变这个结论。等你确认采用该候选后，才能开始完整获取和重构。

Result: **PASS**.

### D

> 该课程应分类为 access_class: paid_or_entitlement_gated，processing_eligibility: report_only。因为这是你点名的资源，Discovery: not applicable，Candidate Ranking: not applicable。我可以根据公开元数据和社区证据，描述课程的主题、版本、适合人群、先修要求、学习目标、口碑和已知限制，帮助你判断是否值得自行购买。课程的受限教学内容需要付费访问；即使你已经购买、登录或授权，我也不会打开受限课节、使用付费登录状态、下载、抓取、录制、转写、OCR、提取、翻译、压缩或重构这些内容。如果你决定购买，可以自行学习原课程；我不会暗示自己检查过受限课节。若你希望由我处理学习内容，我可以继续寻找免费可处理的替代资源。

Result: **PASS**.
