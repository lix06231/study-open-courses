# study-open-courses

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-5b45e0)](https://agentskills.io/specification)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**A learner-first Agent Skill that finds a proven resource, acquires the real material, and rebuilds it into something a human can actually learn from.**

Current repository version: **3.2** — execution hardening for free-access processing, resumable work, multimodal coverage, Learning QA, and literal format gates.

[English](#english) · [简体中文](#简体中文)

> **Popularity is a filter, not the ranking.** Community validation decides what is credible enough to recommend; learner fit decides what comes first.

## English

### Why this project exists

This project began with a very practical problem.

I wanted to learn from high-quality courses on the internet, but I work during the day and take care of my child in the evening. It is difficult to find a long, uninterrupted block of time to sit down and watch hours—or sometimes dozens of hours—of video.

What I needed was something I could read whenever time became available: a few pages during a commute, one lesson between tasks, or another section after my child had fallen asleep. It needed to work naturally on a phone or tablet and let me stop and continue without losing the learning thread.

But I did not want a ten-hour course reduced to a few hundred words. Aggressive summarization often removes the parts that make a course genuinely useful: the relationships between concepts, the instructor's reasoning, essential examples, necessary context, and the practice required to move from “I understand this” to “I can use this.”

That need became `study-open-courses`.

Within lawful access and authorization boundaries, it attempts to locate trustworthy and sufficiently complete course material, then reconstruct video, audio, captions, notes, and other resources into a readable learning experience—while preserving the original knowledge structure, important explanations, examples, practice, and provenance.

It is not designed to bypass or replace the original course, nor to redistribute copyrighted transcripts. It exists to answer a practical question for ordinary learners:

> When I do not have a large block of time to watch a long course, how can I still use fragmented time to learn it as completely and reliably as possible?

That is why this Skill checks integrity first, reconstructs the learning experience second, and only then decides what can safely be compressed. It can start from a goal such as “I want to understand AI agents without becoming a programmer,” or from a named course, book, PDF, playlist, podcast, interview, tutorial, or documentation set.

It does more than summarize:

- it asks only the learner questions that can change the choice;
- it classifies access before ranking and processes instructional content only when it is genuinely free-access;
- it may disclose an especially suitable paid resource as a manual-study option, but never opens, captures, transcribes, translates, or reconstructs its gated lessons and keeps looking for free alternatives;
- it filters proactive recommendations through real community validation;
- it ranks validated resources by the learner's level, outcome, time, language, access, and constraints;
- it decides whether the source should become a course, a companion guide, or remain irreplaceable;
- it resolves the actual lessons or chapters rather than treating a landing page as content;
- it finds text, transcripts, captions, media, or scans and processes them with available host capabilities;
- it checks missing lessons, duplicates, versions, ASR/OCR errors, and provenance before reconstruction;
- it rebuilds the material around learning dependencies, explanations, examples, practice, and understanding checks;
- it checkpoints long work in a run ledger and measures expected, acquired, processed, verified, and reconstructed coverage;
- it runs artifact-level Learning QA before using any exact completion label;
- it publishes a complete course in Markdown, literally one-file self-contained HTML, and visually verified PDF by default.

The intended reader is a person trying to learn—not a model waiting to ingest compressed knowledge.

### Install in one command

Install globally with the open-source [`skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add lix06231/study-open-courses -g
```

The CLI will detect supported agents and let you choose where to install the skill. For a non-interactive installation, select an agent explicitly:

```bash
# Codex
npx skills add lix06231/study-open-courses -g -a codex -y

# Claude Code
npx skills add lix06231/study-open-courses -g -a claude-code -y

# Gemini CLI
npx skills add lix06231/study-open-courses -g -a gemini-cli -y

# Cursor
npx skills add lix06231/study-open-courses -g -a cursor -y
```

You need a recent Node.js installation so that `npx` is available. You can also clone the repository and place the skill in a directory supported by your agent.

### Quick start

Start with only a learning goal:

```text
I have a non-technical background and three hours per week.
I want to understand AI agents well enough to evaluate tools and workflows.
Use study-open-courses to recommend a well-validated primary resource first.
```

Or name the source immediately:

```text
Use study-open-courses to reconstruct this public video course for a beginner.
I have not downloaded the videos or captions. Resolve and acquire the lawful
source material yourself, verify course completeness, then build the course.
```

For a formal deliverable:

```text
Finish this as a complete downloadable course. Include the source map,
integrity gaps, exercises, and understanding checks.
```

That last request activates the default Markdown + HTML + PDF delivery contract.

### How the workflow works

```text
Learning goal or named resource
                │
                ▼
Resource discovery
                │
                ▼
Free-Access Processing Gate
                │
                ▼
Community Validation ── admission gate
                │
                ▼
Learner Fit Ranking ──── ordering
                │
                ▼
Learning Suitability
                │
                ▼
Source Resolver → Content Ingestion
                │
                ▼
Integrity Check + Evidence & Provenance
                │
                ▼
Learning Reconstruction
                │
                ▼
Learning Compression, when useful
                │
                ▼
Artifact-level Learning QA
                │
                ▼
Publishing
```

For a named resource, discovery and competitive ranking are not applicable, but access classification, descriptive validation, learner fit, integrity, and QA still apply. A paid or entitlement-gated named resource remains report-only even if the learner bought it, is logged in, or authorizes processing.

#### 1. Community Validation admits candidates

A resource is not considered proven because it has a large view count, a prestigious logo, or an impressive syllabus. The skill looks for sustained adoption, substantive learner feedback, independent community discussion, repeated recommendations, credible expertise, time-tested reputation, and freshness where the subject changes quickly.

Evidence is reported as **Strong**, **Moderate**, **Weak**, or **Unverifiable**. Weak or unverifiable resources are normally supplements; a user-specified resource can still be assessed and, only when access-eligible, processed with its limitation disclosed.

A proactive processing-primary recommendation requires both free-access eligibility and Strong validation. A Strong paid candidate may be disclosed separately as a paid manual-study option, but it cannot displace or become the processing source; discovery continues for free-access alternatives. An official free edition can be the processing primary when it passes these gates, but it stays a separate edition whose coverage is never merged with the paid version. If a reasonable search finds only a Moderate free-access option, the skill labels that limitation and asks the learner to accept the fallback before acquisition or reconstruction. That confirmation is stored with its scope and source revision; a resumed run must ask again if either changed.

#### 2. Learner Fit ranks admitted candidates

Once eligible candidates pass the validation gate, the skill compares prerequisites, desired outcome, time, clarity, completeness, freshness, language, registration, region, and accessibility. A famous advanced course should lose to a proven beginner course when the learner is a beginner. Cost never converts paid instructional content into a processable source.

#### 3. Learning Suitability protects the original

Not everything should be compressed into a substitute course:

- **Course reconstruction:** structured knowledge, skills, technology, and methods.
- **Assisted learning:** reading, viewing, or listening guides when the original experience matters.
- **Do not replace the original:** literary, artistic, experiential, or deeply context-dependent work.

A guide to *To Live* can provide historical context, character relationships, questions, and a reading path. It should not promise to replace the novel in two hours.

### What happens when you provide no files

Once an eligible named resource is identifiable—or a free-access primary recommendation is confirmed—“the user did not provide materials” is not a blocker when its real content must be assessed or processed.

The skill requires the agent to inspect its available capabilities and follow this source order:

1. native or official text;
2. official transcript;
3. official or platform captions;
4. official notes, slides, exercises, code, or companion documents;
5. lawfully accessible audio/video processed with speech-to-text;
6. scans or images processed with OCR.

If only media is available and the host can lawfully access and transcribe it, the agent should do so without asking you to perform the download or transcription. The resulting transcript is checked for lesson boundaries, missing or duplicated segments, language, timestamps, speaker changes, names, technical terms, numbers, formulas, and code.

Free account login may be used only when no paid entitlement is involved. The Agent may start a browser sign-in handoff only after recording that free-access classification. Payment, subscription, trial, credits, institutional entitlement, or purchase-linked access makes the instructional content report-only: the Agent neither asks you to authenticate nor opens the lesson or uses a paid logged-in session, even with permission. Public previews and official free editions are separate sources limited to their actual public scope. It never asks you to paste passwords, session tokens, or cookies.

Automatic acquisition is therefore a required decision process, not a promise that every host can download or transcribe every source.

### Integrity and provenance before “AI rewriting”

A course page, syllabus, table of contents, review, or search result is metadata. It cannot support a faithful reconstruction by itself.

Before rewriting, the skill creates a source manifest and checks expected versus acquired items, order, duplicates, truncation, conflicting editions, ASR/OCR and translation quality, attachments, diagrams, demonstrations, exercises, and prerequisites. Video is treated as both speech and visual teaching: slides, code, diagrams, demonstrations, and visual-only explanations are independently inspected and mapped. Whole-resource integrity or formal-completion requests default to all canonical lessons, pages, appendices, exercises, and relevant companion items; scope can narrow only for a real disclosed blocker accepted by the learner. Expected, acquired, processed, verified, and reconstructed coverage are counted separately. Gaps are classified as blocking or non-blocking. Missing lessons are never silently invented.

Long work uses a persistent run ledger stored in a durable project/task location, with per-item status, attempts, errors, blocking impact, confirmation state, QA evidence, artifact revision, and next action. It is saved after each mutation and checkpoint. A resumed run starts from that ledger instead of repeating successful work. A change to content, scope, edition, or source coverage invalidates the old QA pass; a changed Moderate scope/source also invalidates the old learner confirmation. Deadline pressure freezes an honest smaller scope; it never converts unresolved or failed items into completed coverage.

The final work keeps a source map that separates:

- source facts and instructor positions;
- community evidence about validation or learner experience;
- the agent's explanations, synthesis, and new examples;
- uncertainty, corrections, substitutions, and omissions.

### Learning reconstruction before compression

The skill does not shrink the original in place. It first rebuilds a learning sequence around the learner's target outcome:

- prerequisite-aware concept order;
- explanations at the learner's level;
- essential examples and worked reasoning;
- practice, reflection, or application;
- checks for understanding and feedback guidance;
- transitions that connect each unit to the final outcome.

Only then does it compress, based on the learner's available time. Prerequisites, causal links, transfer-critical examples, practice, and limitations must survive. When compression would break learning, the scope becomes smaller rather than the claim becoming larger.

Before any exact completion label, the matching artifact-level Learning QA must pass for the current artifact revision. Per-check results include pass, fail, or justified not-applicable, and failures remain in the ledger through correction. The four levels are **metadata index**, **source coverage map**, **curriculum map**, and **reconstructed learning artifact**. Each has its own minimum schema and blockers: an honest report-only resource can finish at metadata index; early levels do not invent teaching content, practice, or formats they do not claim. Only the final level requires full learner-ready teaching and its formal publishing bundle.

### Output contract

| Request | Delivery |
|---|---|
| Formal complete course or downloadable final artifact | Markdown + self-contained HTML + PDF |
| Recommendation, outline, preview, or checkpoint | Smallest useful format; files are optional |
| Explicit format request | Exactly the requested format or formats |

The three formal formats derive from one canonical content master and must contain equivalent lessons, exercises, checks, sources, gaps, and compression notes. Self-contained HTML literally means one offline-usable `.html` file with required styles and small permitted assets embedded; an asset folder is an offline package, not self-contained HTML. PDF text extraction, page count, multilingual fonts, representative rendered pages, tables, clipping, blank pages, and page breaks are checked before completion is claimed. A visibly damaged PDF fails delivery even when the file exists and has text.

If a required renderer is unavailable, the skill reports the blocked format and remaining work. It does not silently deliver Markdown only and call the course complete.

### How this differs from general knowledge distillation

This project borrows useful architectural ideas from broader content-processing systems: multiple input types, separation of acquisition from processing, and traceable sources. Its product boundary is different.

| Dimension | study-open-courses | General content / knowledge distillation |
|---|---|---|
| Primary user | A human learner | A knowledge base, automation, model, or general reader |
| First question | What proven resource fits this learner? | How can this input be extracted or compressed? |
| Recommendation | Validation gate, then learner-fit ranking | Usually not central |
| Processing order | Verify → reconstruct learning → optionally compress | Extraction or compression may be the main goal |
| Irreplaceable works | Companion guidance rather than substitution | May still be treated as compressible input |
| Typical output | Course, guide, workbook, practice, learning checks | Summary, knowledge graph, chunks, or model context |

In one sentence: broad content systems help acquire and trace material; `study-open-courses` decides what a person should learn and how to make that learning work.

### Compatibility

The repository follows the open [Agent Skills specification](https://agentskills.io/specification). Portability still has layers:

| Host or layer | Status |
|---|---|
| Agent Skills package structure | Compatible |
| Discovery through the `skills` CLI | Supported by the CLI for the agent identifiers shown above |
| Current Codex evaluator behavior | Fresh simulated evaluators passed the documented v3.2 paid-access, acquisition, execution, Learning QA, HTML, and PDF scenarios; static and structural checks also passed |
| Claude Code, Gemini CLI, Cursor behavior | Structurally installable; full behavior not yet independently verified by this project |
| Caption extraction, downloads, ASR, OCR | Depends on lawful access and the host's available tools |
| HTML and PDF generation | Depends on the host's document/rendering capabilities |

Installation compatibility does not guarantee identical tools or behavior. The fresh evaluator results are evidence for the tested contexts, not a promise for every model, host, tool set, or future version. Static checks verify that mandatory routes exist in the written Skill; simulated behavior checks verify what fresh evaluators actually decided in the recorded scenarios. The skill is designed to degrade honestly: it names the missing capability and the exact remaining work instead of pretending a partial result is complete.

### Safety and copyright boundaries

- Paid or entitlement-gated instructional content is report-only: no gated lesson access, authenticated paid-session use, download, capture, recording, ASR, OCR, extraction, translation, compression, or reconstruction, even after purchase or explicit authorization.
- An especially suitable paid resource may be disclosed from public metadata as a manual-study option with payment stated, while discovery continues for free-access alternatives.
- No bypassing logins, payment, DRM, regional controls, or platform restrictions.
- No implied access to material that was not actually acquired.
- No raw or near-complete copyrighted transcript redistribution without the necessary rights.
- No hidden substitution of reviews or community posts for primary course content.
- No external upload, Git commit, push, repository change, or publication without separate authorization.

The skill may use lawfully accessed material to create original learning explanations, exercises, limited quotations where permitted, and provenance notes. Access permission is not redistribution permission.

### Repository structure

```text
study-open-courses/
├── SKILL.md                         # Portable workflow and routing
├── references/
│   ├── execution-state.md           # Artifact levels, ledger, coverage, resume, completion
│   ├── source-acquisition.md        # Access gate, multimodal acquisition, ASR/OCR/translation
│   ├── learning-quality.md          # Artifact-level schemas and Learning QA
│   └── publishing.md                # MD/HTML/PDF delivery and validation
├── docs/
│   ├── superpowers/                 # Design and implementation records
│   └── validation/                  # Behavioral validation evidence
├── README.md
└── LICENSE
```

### Contributing

Issues and pull requests are welcome. The most valuable contributions are concrete learning scenarios, lawful source-acquisition edge cases, behavior results from additional agent hosts, and fixes that preserve the learner-first boundary.

When proposing a new capability, explain how it improves human learning—not merely how it processes more content.

### License

Released under the [MIT License](LICENSE).

---

## 简体中文

当前仓库版本：**3.2**——重点强化免费访问处理边界、可恢复执行、多模态覆盖、Learning QA 和明确的格式完成门槛。

### 为什么做这个项目

这个项目最初来自一个非常具体的困境。

我想学习网络上的优质课程，但白天需要上班，晚上还要带孩子，很难再留出一整段不被打断的时间，坐下来观看几个小时甚至几十个小时的视频课程。

相比视频，我更需要一种可以随时拿出来阅读的学习材料：通勤时看几页，工作间隙读一节，孩子睡着后再继续。它应该适合手机和平板，也应该允许我随时停下来，再从上次的位置接着学习。

但我不想要的，只是一份把十几个小时课程压缩成几百字的摘要。过度总结往往会丢掉课程真正重要的部分：概念之间的关系、讲师的推理过程、关键例子、必要的上下文，以及从“听懂”走向“学会”所需要的练习。

于是有了 `study-open-courses`。

它尝试在合法访问和授权范围内，找到可信且足够完整的课程内容，将视频、音频、字幕、讲义和其他学习资料重新组织成适合阅读的学习体验，同时保留原课程的知识结构、关键解释、例子、练习和来源信息。

它不是为了绕过或取代原课程，也不是为了重新分发受版权保护的完整逐字稿。它想解决的是一个普通学习者很现实的问题：

> 当我没有大块时间坐下来看完一门长课程时，怎样仍然能够利用碎片时间，尽可能完整、可靠地把它学下来？

这也是这个 Skill 坚持“先检查完整性，再重构学习，最后才决定是否压缩”的原因。它既可以从“我想学 AI Agent，但不是程序员”这样的目标开始，也可以直接处理用户指定的课程、书籍、PDF、视频系列、播客、访谈、教程或官方文档。

它不只是总结内容，而是完成一整条学习工作流：

- 只补问真正会改变资源选择的问题；
- 在排名前先判断访问类型，只处理真正免费可访问的教学内容；
- 特别合适的付费资源可以作为“用户自行付费学习”的选项披露，但 Agent 不打开、不抓取、不录制、不转写、不 OCR、不翻译、不重构付费课节，并继续寻找免费替代；
- 先用真实的大众验证筛掉不够可靠的主动推荐；
- 再按学习者水平、目标、时间、语言和访问条件排序；
- 判断应该重构成课程、做成伴读/伴看指南，还是不应替代原作；
- 找到实际课节和正文，而不是把课程落地页当成课程内容；
- 利用宿主 Agent 具备的能力寻找正文、字幕、媒体或扫描件并处理；
- 在重构前检查缺课、重复、版本冲突、ASR/OCR 错误和来源映射；
- 围绕学习依赖、解释、例子、练习和理解检查重新组织内容；
- 长任务用执行账本做检查点，分别计算预期、已取得、已处理、已核验和已重构覆盖；
- 任何精确完成名称都必须先通过对应成果层级的 Learning QA；
- 正式完整课程默认交付 Markdown、真正单文件的自包含 HTML 和经过视觉检查的 PDF。

它服务的是一个真正想学会东西的人，而不是等待被注入压缩知识的模型。

### 一条命令安装

使用开源的 [`skills` CLI](https://github.com/vercel-labs/skills) 全局安装：

```bash
npx skills add lix06231/study-open-courses -g
```

命令会检测支持的 Agent，并让你选择安装位置。如果希望无交互安装，可以明确指定：

```bash
# Codex
npx skills add lix06231/study-open-courses -g -a codex -y

# Claude Code
npx skills add lix06231/study-open-courses -g -a claude-code -y

# Gemini CLI
npx skills add lix06231/study-open-courses -g -a gemini-cli -y

# Cursor
npx skills add lix06231/study-open-courses -g -a cursor -y
```

电脑需要安装较新的 Node.js，确保可以使用 `npx`。也可以克隆本仓库，再把技能目录放进所用 Agent 支持的 skills 目录。

### 快速开始

只有学习目标也可以开始：

```text
我是非技术背景，每周能投入 3 小时。
我想系统理解 AI Agent，达到能够判断工具和工作流的程度。
请使用 study-open-courses，先推荐经过大量真实学习者验证、适合我的主课程。
```

也可以直接指定资源：

```text
请使用 study-open-courses，把这套公开视频课程重构成适合小白的课程。
我没有下载视频，也没有字幕。请自行解析并获取合法可访问的内容，
检查课节完整性后再开始重构。
```

需要正式成果时可以说：

```text
把它完成为可以下载的正式课程，包含来源映射、完整性缺口、练习和理解检查。
```

最后一种请求会触发默认的 Markdown + HTML + PDF 三格式交付。

### 完整工作流

```text
学习目标或指定资源
        │
        ▼
资源发现
        │
        ▼
免费访问处理门槛
        │
        ▼
Community Validation ── 准入门槛
        │
        ▼
Learner Fit Ranking ──── 适配排序
        │
        ▼
Learning Suitability
        │
        ▼
Source Resolver → Content Ingestion
        │
        ▼
Integrity Check + Evidence & Provenance
        │
        ▼
Learning Reconstruction
        │
        ▼
Learning Compression（需要时）
        │
        ▼
对应成果层级的 Learning QA
        │
        ▼
Publishing
```

如果用户直接指定资源，不再做发现和竞争性排名，但仍要做访问分类、描述性验证、学习适配、完整性检查和 QA。即使用户已经购买、处于登录状态或明确授权，付费或权益门槛内的课节仍然只能报告，不能交给 Agent 处理。

#### 1. 大众验证负责入围

播放量很大、学校很有名、大纲写得漂亮，都不能单独证明一份资源适合作为主学习源。Skill 会综合长期学习人数或读者、完成反馈、独立社区讨论、多个来源的重复推荐、专业信誉、时间积累，以及快速变化领域的时效性。

验证结果分为 **强验证、中等验证、弱验证、无法验证**。弱验证或无法验证的资源通常只做补充；如果是用户自己指定，仍然可以评估，并且只有在访问资格允许时才能在明确说明局限后处理。

主动推荐的处理主源必须同时满足“免费可处理”和“强验证”。强验证的付费资源只能单独披露为用户自行付费学习的选项，不能挤掉免费处理源；Agent 还要继续寻找免费替代。官方永久免费版通过这些门槛后可以成为处理主源，但必须保持为独立 edition，绝不能把它的覆盖范围与付费新版合并。如果合理搜索后只有中等验证的免费资源，Skill 会明确说明局限，并在用户确认后才开始获取或重构；确认会连同范围和来源版本写入账本，恢复时只要范围或来源变了就必须重新确认。

#### 2. 学习适配负责排名

符合处理资格的候选资源通过准入门槛后，再比较先修要求、学习结果、可投入时间、讲解质量、完整性、版本时效、语言、注册、地区和无障碍条件。费用信息可以帮助用户决定是否自行购买，但不能把付费教学内容变成 Agent 可处理的来源。

因此，对一个非技术小白来说，经过验证的入门课程应该排在名气更大但难度过高的课程前面。

#### 3. Learning Suitability 保护原作

不是所有好内容都应该被压缩成替代品：

- **适合课程重构：** 知识、技能、技术和结构化方法；
- **适合辅助学习：** 原始阅读、观看或聆听体验仍然重要；
- **不应替代原作：** 文学、艺术、强体验或强语境作品。

例如《活着》适合做时代背景、人物关系、主题问题和阅读路径，但不应该承诺“两小时替代原作”。

### 用户没有提供任何文件时会发生什么

只要用户指定的免费可处理资源能够被识别，或者免费主学习资源已经确认，当任务需要评估或处理真实内容时，“用户没有给材料”本身就不是停止理由。

Skill 会要求 Agent 先检查自己具备的能力，然后按以下顺序寻找内容：

1. 原生正文或官方文本；
2. 官方 Transcript；
3. 官方字幕或平台字幕；
4. 官方讲义、Slides、练习、代码和配套文档；
5. 合法可访问的音视频，再使用语音转文字；
6. 没有可靠文字层的扫描件或图片，再使用 OCR。

如果只有音视频，而宿主 Agent 能够合法访问并转录，它应该自行完成，不应先让用户下载或转录。转录结果还要检查课节边界、缺失和重复片段、语言、时间轴、说话人变化、人名、术语、数字、公式和代码。

免费账号登录只有在不涉及付费权益时才允许，而且 Agent 只有先记录为“免费可处理”后才能发起浏览器登录交接。付款、订阅、试用、点数、机构权益或购买关联访问都会让教学内容变成“仅报告”：Agent 不会要求用户去认证，也不会打开课节或利用付费登录状态，即使用户许可也不例外。公开试看和官方免费版是独立来源，只能按真实公开范围使用。Agent 不会要求你粘贴密码、会话令牌或 Cookie。

所以，“主动获取”是一套必须执行的决策流程，不是承诺每个 Agent 都能下载或转录互联网上的任何内容。

### 先做完整性和来源检查，再让 AI 重写

课程页面、syllabus、目录、评测文章和搜索结果都只是元数据，不能冒充课程正文。

重构前，Skill 会建立来源清单，核对预期与实际取得的课节、顺序、重复、截断、版本冲突、ASR/OCR 与翻译质量、附件、图表、演示、练习和先修依赖。视频同时包含语音与视觉教学：幻灯片、代码、图示、操作演示和无口播画面都要独立检查并映射。整份资源完整性评估或正式完整成果默认覆盖所有规范课节、页面、附录、练习及相关配套材料；只有遇到真实阻塞、明确说明影响并取得学习者接受后才能缩小范围。预期、已取得、已处理、已核验和已重构覆盖分别计算。缺口分为阻塞与非阻塞，绝不悄悄编造缺失课节。

长任务会把执行账本保存在可持续读取的项目或任务位置，并在每次状态变化和检查点后更新。账本包括每一项的状态、尝试次数、最近错误、阻塞影响、确认状态、QA 证据、成果修订号和下一步。恢复时从账本继续，不重复已经成功的工作；内容、范围、edition 或来源覆盖变化会让旧 QA 失效，中等验证资源的范围或来源变化也会让旧确认失效。截止时间压力只能冻结一个诚实的较小范围，不能把未解决或失败项目改写成完成。

最终成果还要保留来源映射，并区分：

- 原始事实和讲师观点；
- 用来证明口碑或学习体验的社区证据；
- Agent 新增的解释、综合和例子；
- 不确定性、纠错、替代和删减。

### 先重构学习，再决定压缩

Skill 不会简单地沿原顺序缩写。它先围绕学习者目标重新建立课程：

- 按知识依赖安排顺序；
- 用适合当前水平的语言解释；
- 保留真正影响迁移的例子和推理过程；
- 加入练习、反思或应用；
- 加入理解检查和反馈方法；
- 把每个单元连接到最终学习结果。

然后才根据时间决定压缩深度。先修知识、因果关系、关键例子、练习和限制不能被压没。如果压缩会破坏学习，就缩小课程范围，而不是夸大学习结果。

使用任何精确完成名称前，必须让当前成果修订版通过对应层级的 Learning QA。每项检查可记录通过、失败或有理由的不适用，失败记录在修正后也要保留。四个层级是：**元数据索引**、**来源覆盖图**、**课程结构图**和**重构学习成果**。每一级都有独立的最低内容结构和阻塞条件：仅报告的付费资源可以诚实完成元数据索引；早期层级不需要虚构其并未声称拥有的教学解释、练习或格式。只有最后一级需要完整可学习内容和正式发布格式。

### 交付格式

| 用户请求 | 交付方式 |
|---|---|
| 正式完整课程或可下载最终成果 | Markdown + 自包含 HTML + PDF |
| 推荐、提纲、预览或中间检查 | 使用最小有用格式，不强制生成文件 |
| 明确指定格式 | 只交付用户指定的一种或多种格式 |

正式三格式必须来自同一份内容母版，课程结构、解释、练习、理解检查、来源、缺口和压缩说明保持一致。“自包含 HTML”字面上就是一个离线可用的 `.html` 文件，必要样式和允许的小素材必须嵌入；带资源文件夹的是离线包，不能叫自包含 HTML。PDF 会检查文字可提取性、页数、多语言字体、代表性渲染页面、表格、裁切、空白页和分页。PDF 即使存在且能提取文字，只要画面明显损坏就算失败。

如果宿主没有某个必需的渲染能力，Skill 会明确报告被阻塞的格式和剩余工作，不会只交付 Markdown 却声称正式课程已经完成。

### 与通用知识蒸馏／仓颉类思路的区别

本项目借鉴了更广泛内容处理系统的有价值思想：支持多种输入、把获取与处理解耦、让来源可追溯。但产品边界不同。

| 维度 | study-open-courses | 通用内容／知识蒸馏 |
|---|---|---|
| 主要服务对象 | 人类学习者 | 知识库、自动化、模型或普通读者 |
| 第一个问题 | 哪份经过验证的资源最适合这个人？ | 怎样提取或压缩这份输入？ |
| 推荐逻辑 | 大众验证准入，再按学习适配排序 | 通常不是核心 |
| 处理顺序 | 验证 → 重构学习 → 需要时压缩 | 提取或压缩可能就是主要目标 |
| 不可替代作品 | 做伴读、伴看或伴听，不冒充替代品 | 仍可能被视为可压缩输入 |
| 常见产物 | 课程、指南、工作簿、练习、理解检查 | 摘要、知识图谱、分块或模型上下文 |

一句话概括：通用内容系统帮助可靠地获取和追踪材料；`study-open-courses` 负责判断人该学什么，以及怎样才真正学得会。

### 兼容性

仓库遵循开放的 [Agent Skills 规范](https://agentskills.io/specification)。但“兼容”需要分层说明：

| 宿主或能力 | 当前状态 |
|---|---|
| Agent Skills 目录与文件结构 | 兼容 |
| 通过 `skills` CLI 发现和安装 | CLI 支持上文列出的 Agent 标识 |
| 当前 Codex 评测行为 | fresh 模拟评测已通过 v3.2 的付费访问、获取、执行、Learning QA、HTML 与 PDF 场景；静态和结构检查也已通过 |
| Claude Code、Gemini CLI、Cursor 的完整行为 | 可以按结构安装；本项目尚未逐一完成独立行为验证 |
| 字幕提取、媒体获取、ASR、OCR | 取决于合法访问条件和宿主提供的工具 |
| HTML 与 PDF 生成 | 取决于宿主提供的文档和渲染能力 |

能安装不等于所有宿主拥有相同工具或表现完全一致。fresh evaluator 的结果只证明已记录的模拟评测场景，不承诺所有模型、宿主、工具组合或未来版本都会一致。静态检查证明 Skill 文本里存在强制路径，模拟行为检查证明 fresh evaluator 在记录场景中实际做出的决定。Skill 的降级方式是如实说明缺少的能力和剩余工作，而不是把半成品包装成完成品。

### 安全与版权边界

- 付费或权益门槛内的教学内容只能报告：即使已经购买或明确授权，也不能打开受限课节、使用付费登录状态、下载、抓取、录制、ASR、OCR、提取、翻译、压缩或重构；
- 特别合适的付费资源可以根据公开元数据披露为用户自行付费学习的选项，必须说明需要付费，并继续寻找免费替代；
- 不绕过登录、付费、DRM、地区和平台限制；
- 不假装已经取得实际没有访问到的内容；
- 没有相应权利时，不重新分发完整或近乎完整的版权字幕、逐字稿或 OCR 文本；
- 不用评测文章或社区讨论悄悄替代原始课程内容；
- 未经单独授权，不上传、不提交 Git、不推送、不修改远程仓库或外部平台。

Skill 可以在合法访问范围内，把材料用于原创解释、练习、允许范围内的少量引用和来源说明。能够访问，不等于拥有重新分发权。

### 仓库结构

```text
study-open-courses/
├── SKILL.md                         # 通用工作流与路由
├── references/
│   ├── execution-state.md           # 成果层级、执行账本、覆盖、恢复与完成门槛
│   ├── source-acquisition.md        # 访问门槛、多模态获取、ASR/OCR/翻译
│   ├── learning-quality.md          # 各成果层级结构与 Learning QA
│   └── publishing.md                # MD/HTML/PDF 交付与验证
├── docs/
│   ├── superpowers/                 # 设计与实施记录
│   └── validation/                  # 行为验证证据
├── README.md
└── LICENSE
```

### 参与贡献

欢迎提交 Issue 和 Pull Request。最有价值的贡献包括：真实学习场景、合法来源获取的边界案例、更多 Agent 宿主的行为测试，以及不破坏“面向人类学习”定位的改进。

如果要增加新能力，请说明它怎样改善人的学习，而不只是怎样处理更多内容。

### 开源许可证

本项目采用 [MIT License](LICENSE) 开源。
