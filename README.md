# study-open-courses

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-5b45e0)](https://agentskills.io/specification)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**A learner-first Agent Skill that finds a proven resource, acquires the real material, and rebuilds it into something a human can actually learn from.**

[English](#english) · [简体中文](#简体中文)

> **Popularity is a filter, not the ranking.** Community validation decides what is credible enough to recommend; learner fit decides what comes first.

## English

### Why this project exists

Finding a famous course is easy. Finding the right course for one person—and turning its real content into a trustworthy, usable learning path—is much harder.

`study-open-courses` gives an agent a complete learning workflow. It can start from a goal such as “I want to understand AI agents without becoming a programmer,” or from a named course, book, PDF, playlist, podcast, interview, tutorial, or documentation set.

It does more than summarize:

- it asks only the learner questions that can change the choice;
- it filters proactive recommendations through real community validation;
- it ranks validated resources by the learner's level, outcome, time, language, access, and constraints;
- it decides whether the source should become a course, a companion guide, or remain irreplaceable;
- it resolves the actual lessons or chapters rather than treating a landing page as content;
- it finds text, transcripts, captions, media, or scans and processes them with available host capabilities;
- it checks missing lessons, duplicates, versions, ASR/OCR errors, and provenance before reconstruction;
- it rebuilds the material around learning dependencies, explanations, examples, practice, and understanding checks;
- it publishes a complete course in Markdown, self-contained HTML, and PDF by default.

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
Publishing
```

#### 1. Community Validation admits candidates

A resource is not considered proven because it has a large view count, a prestigious logo, or an impressive syllabus. The skill looks for sustained adoption, substantive learner feedback, independent community discussion, repeated recommendations, credible expertise, time-tested reputation, and freshness where the subject changes quickly.

Evidence is reported as **Strong**, **Moderate**, **Weak**, or **Unverifiable**. Weak or unverifiable resources are normally supplements, although a user-specified resource can still be processed with its limitation disclosed.

A proactive primary recommendation requires Strong validation. If a reasonable search finds only Moderate options, the skill labels that limitation and asks the learner to accept the fallback rather than silently promoting it.

#### 2. Learner Fit ranks admitted candidates

Once candidates pass the validation gate, the skill compares prerequisites, desired outcome, time, clarity, completeness, freshness, language, cost, registration, region, and accessibility. A famous advanced course should lose to a proven beginner course when the learner is a beginner.

#### 3. Learning Suitability protects the original

Not everything should be compressed into a substitute course:

- **Course reconstruction:** structured knowledge, skills, technology, and methods.
- **Assisted learning:** reading, viewing, or listening guides when the original experience matters.
- **Do not replace the original:** literary, artistic, experiential, or deeply context-dependent work.

A guide to *To Live* can provide historical context, character relationships, questions, and a reading path. It should not promise to replace the novel in two hours.

### What happens when you provide no files

Once a named resource is identifiable—or a primary recommendation is confirmed—“the user did not provide materials” is not a blocker when its real content must be assessed or processed.

The skill requires the agent to inspect its available capabilities and follow this source order:

1. native or official text;
2. official transcript;
3. official or platform captions;
4. official notes, slides, exercises, code, or companion documents;
5. lawfully accessible audio/video processed with speech-to-text;
6. scans or images processed with OCR.

If only media is available and the host can lawfully access and transcribe it, the agent should do so without asking you to perform the download or transcription. The resulting transcript is checked for lesson boundaries, missing or duplicated segments, language, timestamps, speaker changes, names, technical terms, numbers, formulas, and code.

The agent pauses only for a real blocker: authentication, payment, DRM, region restrictions, copyright or permission ambiguity, inaccessible material, unavailable host capabilities, or a missing dependency that changes the learning outcome. It never asks you to paste passwords, session tokens, or cookies; when the host supports it, you authenticate in the interface you control.

Automatic acquisition is therefore a required decision process, not a promise that every host can download or transcribe every source.

### Integrity and provenance before “AI rewriting”

A course page, syllabus, table of contents, review, or search result is metadata. It cannot support a faithful reconstruction by itself.

Before rewriting, the skill creates a source manifest and checks expected versus acquired items, order, duplicates, truncation, conflicting editions, ASR/OCR quality, attachments, diagrams, exercises, and prerequisites. Whole-resource integrity or formal-completion requests default to all canonical lessons, pages, appendices, exercises, and relevant companion items; scope can narrow only for a real disclosed blocker accepted by the learner. For scanned material, processed pages and visually verified pages are tracked separately, and final units map back to precise page or slide ranges. Gaps are classified as blocking or non-blocking. Missing lessons are never silently invented.

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

### Output contract

| Request | Delivery |
|---|---|
| Formal complete course or downloadable final artifact | Markdown + self-contained HTML + PDF |
| Recommendation, outline, preview, or checkpoint | Smallest useful format; files are optional |
| Explicit format request | Exactly the requested format or formats |

The three formal formats derive from one canonical content master and must contain equivalent lessons, exercises, checks, sources, gaps, and compression notes. HTML navigation and local assets are verified. PDF text extraction, page count, multilingual fonts, representative pages, tables, clipping, blank pages, and page breaks are checked before completion is claimed.

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
| Codex behavior | Tested for the core workflow and delivery decisions |
| Claude Code, Gemini CLI, Cursor behavior | Structurally installable; full behavior not yet independently verified by this project |
| Caption extraction, downloads, ASR, OCR | Depends on lawful access and the host's available tools |
| HTML and PDF generation | Depends on the host's document/rendering capabilities |

Installation compatibility does not guarantee identical tools or behavior. The skill is designed to degrade honestly: it names the missing capability and the exact remaining work instead of pretending a partial result is complete.

### Safety and copyright boundaries

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
│   ├── source-acquisition.md        # Source resolution, ASR/OCR, integrity, provenance
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

### 为什么做这个项目

找到一门“名气很大的课”并不难。真正困难的是：替一个具体的人找到此刻最合适的学习资源，拿到足够完整、可信的真实内容，再把它重构成一条确实能学会的路径。

`study-open-courses` 是一套面向**人类学习**的通用 Agent Skill。它既可以从“我想学 AI Agent，但不是程序员”这样的学习目标开始，也可以直接处理用户指定的课程、书籍、PDF、视频系列、播客、访谈、教程或官方文档。

它不只是总结内容，而是完成一整条学习工作流：

- 只补问真正会改变资源选择的问题；
- 先用真实的大众验证筛掉不够可靠的主动推荐；
- 再按学习者水平、目标、时间、语言和访问条件排序；
- 判断应该重构成课程、做成伴读/伴看指南，还是不应替代原作；
- 找到实际课节和正文，而不是把课程落地页当成课程内容；
- 利用宿主 Agent 具备的能力寻找正文、字幕、媒体或扫描件并处理；
- 在重构前检查缺课、重复、版本冲突、ASR/OCR 错误和来源映射；
- 围绕学习依赖、解释、例子、练习和理解检查重新组织内容；
- 正式完整课程默认交付 Markdown、自包含 HTML 和 PDF。

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
Publishing
```

#### 1. 大众验证负责入围

播放量很大、学校很有名、大纲写得漂亮，都不能单独证明一份资源适合作为主学习源。Skill 会综合长期学习人数或读者、完成反馈、独立社区讨论、多个来源的重复推荐、专业信誉、时间积累，以及快速变化领域的时效性。

验证结果分为 **强验证、中等验证、弱验证、无法验证**。弱验证或无法验证的资源通常只做补充；如果是用户自己指定，仍然可以处理，但必须明确说明局限。

主动推荐的主学习源必须达到强验证。如果经过合理搜索后只有中等验证选项，Skill 会明确说明没有找到强验证资源，并在用户确认后才把它作为退而求其次的主源，不会静默升级。

#### 2. 学习适配负责排名

候选资源通过准入门槛后，再比较先修要求、学习结果、可投入时间、讲解质量、完整性、版本时效、语言、费用、注册、地区和无障碍条件。

因此，对一个非技术小白来说，经过验证的入门课程应该排在名气更大但难度过高的课程前面。

#### 3. Learning Suitability 保护原作

不是所有好内容都应该被压缩成替代品：

- **适合课程重构：** 知识、技能、技术和结构化方法；
- **适合辅助学习：** 原始阅读、观看或聆听体验仍然重要；
- **不应替代原作：** 文学、艺术、强体验或强语境作品。

例如《活着》适合做时代背景、人物关系、主题问题和阅读路径，但不应该承诺“两小时替代原作”。

### 用户没有提供任何文件时会发生什么

只要用户指定的资源能够被识别，或者主学习资源已经确认，当任务需要评估或处理真实内容时，“用户没有给材料”本身就不是停止理由。

Skill 会要求 Agent 先检查自己具备的能力，然后按以下顺序寻找内容：

1. 原生正文或官方文本；
2. 官方 Transcript；
3. 官方字幕或平台字幕；
4. 官方讲义、Slides、练习、代码和配套文档；
5. 合法可访问的音视频，再使用语音转文字；
6. 没有可靠文字层的扫描件或图片，再使用 OCR。

如果只有音视频，而宿主 Agent 能够合法访问并转录，它应该自行完成，不应先让用户下载或转录。转录结果还要检查课节边界、缺失和重复片段、语言、时间轴、说话人变化、人名、术语、数字、公式和代码。

只有真正遇到阻塞才暂停：登录、付费、DRM、地区限制、版权或授权不清、资源不可访问、宿主没有相应工具，或者关键缺失会改变课程目标。Agent 不会要求你粘贴密码、会话令牌或 Cookie；宿主支持时，应由你在自己控制的界面完成登录。

所以，“主动获取”是一套必须执行的决策流程，不是承诺每个 Agent 都能下载或转录互联网上的任何内容。

### 先做完整性和来源检查，再让 AI 重写

课程页面、syllabus、目录、评测文章和搜索结果都只是元数据，不能冒充课程正文。

重构前，Skill 会建立来源清单，核对预期与实际取得的课节、顺序、重复、截断、版本冲突、ASR/OCR 质量、附件、图表、练习和先修依赖。整份资源完整性评估或正式完整成果默认覆盖所有规范课节、页面、附录、练习及相关配套材料；只有遇到真实阻塞、明确说明影响并取得学习者接受后才能缩小范围。扫描材料会分别记录“已处理页面”和“已视觉核验页面”，最终单元必须映射到具体页码或幻灯片范围。缺口分为阻塞与非阻塞，绝不悄悄编造缺失课节。

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

### 交付格式

| 用户请求 | 交付方式 |
|---|---|
| 正式完整课程或可下载最终成果 | Markdown + 自包含 HTML + PDF |
| 推荐、提纲、预览或中间检查 | 使用最小有用格式，不强制生成文件 |
| 明确指定格式 | 只交付用户指定的一种或多种格式 |

正式三格式必须来自同一份内容母版，课程结构、解释、练习、理解检查、来源、缺口和压缩说明保持一致。HTML 会检查目录导航与本地资源；PDF 会检查文字可提取性、页数、多语言字体、代表页面、表格、裁切、空白页和分页。

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
| Codex 核心流程与交付决策 | 已进行行为验证 |
| Claude Code、Gemini CLI、Cursor 的完整行为 | 可以按结构安装；本项目尚未逐一完成独立行为验证 |
| 字幕提取、媒体获取、ASR、OCR | 取决于合法访问条件和宿主提供的工具 |
| HTML 与 PDF 生成 | 取决于宿主提供的文档和渲染能力 |

能安装不等于所有宿主拥有相同工具或表现完全一致。Skill 的降级方式是如实说明缺少的能力和剩余工作，而不是把半成品包装成完成品。

### 安全与版权边界

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
│   ├── source-acquisition.md        # 来源解析、ASR/OCR、完整性、可追溯性
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
