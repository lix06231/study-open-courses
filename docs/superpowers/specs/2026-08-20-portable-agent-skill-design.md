# study-open-courses Portable Agent Skill Upgrade Design

Date: 2026-08-20  
Status: Approved and implemented  
Target release: v3.1

## 1. Goal

Upgrade `study-open-courses` from a Codex-oriented package into a portable Agent Skill for human learning.

The project must continue to solve one focused problem:

> Select, acquire, verify, reconstruct, compress, and publish trustworthy learning resources for a human learner.

It must not become a general-purpose content summarizer, a universal “knowledge distillation” tool, or a pipeline for injecting arbitrary content into models.

## 2. Success criteria

The upgrade is complete when:

1. `SKILL.md` follows the open Agent Skills format and avoids depending on Codex-only concepts.
2. The core workflow remains learner-first: Community Validation is the admission gate, while Learner Fit determines ranking.
3. A confirmed course can proceed even when the user supplies no transcript, notes, or files.
4. When lawful access and host capabilities permit, the agent finds captions or transcribes audio/video without handing solvable acquisition work back to the user.
5. Acquisition, transcription, integrity checks, provenance, reconstruction, compression, and publishing remain distinct stages.
6. Formal complete-course delivery preserves the existing multi-format contract: Markdown, self-contained HTML, and PDF by default unless the user requests specific formats.
7. `README.md` is detailed, approachable, and bilingual in English and Simplified Chinese.
8. The README includes a copyable one-command installation path and honest compatibility notes.
9. The repository passes structural validation and realistic behavior checks before the installed copy is synchronized.

## 3. Package structure

```text
study-open-courses/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
│   ├── source-acquisition.md
│   └── publishing.md
└── docs/
```

`SKILL.md` remains the portable entrypoint. It contains routing, core principles, the end-to-end workflow, decision boundaries, and links to conditional references.

`references/source-acquisition.md` contains the detailed Source Resolver, Content Ingestion, transcription, Integrity Check, and Evidence & Provenance procedures. Agents read it when a task needs content acquisition or source verification.

`references/publishing.md` contains deliverable contracts, Markdown/HTML/PDF generation, validation, and partial-delivery rules. Agents read it when producing a formal downloadable artifact.

The split follows progressive disclosure: a learner asking only for course recommendations should not need to load media-transcription or PDF-production details.

## 4. Portable skill contract

The frontmatter will retain the required `name` and a discriminating `description` beginning with “Use when…”. It will add:

- `license: MIT`
- string-valued metadata for author, version, and a short compatibility note describing internet, media, and document-rendering dependencies

Instructions will use host-neutral language such as “available tools or capabilities” and “downloadable links or host-supported file paths.” Codex may be listed as a verified host in the README, but it will not define the skill’s architecture.

The compatibility note stays under `metadata` because the bundled Codex validator used by this project currently accepts `metadata` but rejects a top-level `compatibility` key. The skill remains valid without that optional top-level field, while the README carries the complete compatibility explanation.

Compatibility claims will distinguish three levels:

1. **Format compatible:** the package follows the Agent Skills structure.
2. **Installer supported:** the `skills` CLI recognizes the target agent.
3. **Behavior verified:** realistic scenarios were actually run on that host.

The release may claim behavioral verification on Codex only unless other hosts are tested. Automatic transcription and HTML/PDF production depend on the tools available in the selected host.

## 5. Learning workflow

The core workflow remains:

1. Entry routing
2. Learning Goal
3. Learning Resource Discovery
4. Community Validation
5. Learner Fit Ranking
6. Learning Suitability
7. Source Resolver
8. Content Ingestion
9. Integrity Check
10. Evidence & Provenance
11. Learning Reconstruction
12. Learning Compression
13. Publishing

The defining ranking rule remains:

> Popularity is a filter, not the ranking. Community evidence controls admission; learner fit controls order.

The skill accepts multiple learning-source types—courses, video series, books, PDFs, podcasts, interviews, tutorials, official documentation, or a small source bundle—but every accepted source must serve an explicit human learning goal.

## 6. Autonomous source acquisition and transcription

Once the learner confirms a primary resource, absence of user-provided material is not a reason to stop. The agent must run Source Resolver and pursue the best lawful, usable source in this order:

1. native or official text;
2. official transcript or captions;
3. platform-provided captions;
4. official notes, slides, or handouts;
5. lawfully accessible audio or video.

If only audio or video is available, the agent must inspect the host for relevant capabilities, including media access, caption extraction, download where permitted, and speech-to-text. When access is lawful and authorized and a usable tool exists, it must transcribe autonomously.

The agent asks the user only when a real blocker remains, such as:

- authentication, payment, or region restrictions;
- unclear permission or copyright boundaries;
- inaccessible or broken sources;
- unavailable transcription/media tooling;
- a material choice that would change the learning resource or scope.

Transcription is an ingestion step, not a final learning artifact. Before reconstruction, the agent checks lesson order and count, duplicate or missing segments, language, timing discontinuities, and error-prone names or technical terms. Low-confidence passages are marked rather than silently invented.

Copyright boundaries remain explicit: the agent may use lawfully accessed content to reconstruct a learning resource, but it does not redistribute a raw copyrighted transcript merely because it created one during ingestion.

## 7. Publishing contract

Delivery depends on the request:

| Request | Required delivery |
|---|---|
| Formal complete learning artifact | Markdown, self-contained HTML, and PDF |
| Quick preview or outline | Smallest useful chat format; no files required |
| Explicit format request | Exactly the requested format or formats |
| Missing required renderer | Report partial progress and the precise blocker; do not claim completion |

For formal three-format delivery, all formats must carry equivalent course structure and required learning content. Validation includes non-empty files, working HTML navigation and local resources, extractable PDF text, non-zero PDF page count, correct Chinese characters, and visual inspection of representative PDF pages for clipping, blank pages, broken tables, and poor page breaks.

External publishing—GitHub pushes, repository creation, posts, uploads, or other remote mutations—always requires separate authorization.

## 8. README design

The README will be one bilingual document with language jump links. English appears first for repository discoverability, followed by a complete Simplified Chinese version.

Each language section contains:

1. a clear one-sentence promise;
2. why this project exists;
3. what makes it different from generic summarization or model-oriented distillation;
4. the complete workflow in readable form;
5. quick installation;
6. agent-specific installation examples;
7. realistic quick-start prompts;
8. autonomous source acquisition and transcription behavior;
9. output formats;
10. compatibility and capability matrix;
11. limits, copyright, and safety boundaries;
12. validation status;
13. repository structure;
14. contributing and license.

The primary installation command will be:

```bash
npx skills add lix06231/study-open-courses -g
```

Non-interactive examples may target Codex, Claude Code, Gemini CLI, and Cursor using the CLI’s documented agent identifiers. The README will not imply that installer recognition equals full behavioral testing.

## 9. Validation plan

Validation has four layers:

### 9.1 Structural validation

- validate frontmatter, naming, relative references, and unfinished placeholders;
- verify every referenced file exists;
- confirm the main entrypoint stays concise enough for progressive disclosure.

### 9.2 Portability audit

- scan core instructions for Codex-only paths, tool names, or UI assumptions;
- verify host-specific notes live in README compatibility guidance rather than the core workflow;
- check repository discovery with the `skills` CLI.

### 9.3 Behavior scenarios

Run independent evaluations for at least these cases:

1. confirmed public course, captions available, no user files;
2. public video with no captions, speech-to-text capability available;
3. private, paid, or login-gated resource;
4. accessible media but no transcription capability;
5. request to reproduce a raw copyrighted transcript;
6. goal-only learner needing recommendations;
7. formal complete-course request requiring Markdown, HTML, and PDF;
8. explicit PDF-only request.
9. scanned or image-only PDF with no reliable text layer and OCR capability available.

Expected results are autonomous progress when tools and permission allow, including page-aware OCR with layout-gap reporting, a precise blocker when tools or permission do not allow progress, no unlicensed transcript redistribution, learner-fit ranking after validation, and correct output-format behavior.

### 9.4 Installation synchronization

Only after repository validation passes, synchronize the updated skill into the local Codex skill directory and check for accidental same-name nesting. Remote commit and push remain a separate, explicitly authorized step.

## 10. Non-goals

This upgrade will not:

- become a generic article, meeting, or entertainment summarizer;
- promise bypasses for logins, payment, DRM, regional controls, or copyright restrictions;
- bundle a downloader, speech model, browser, or renderer into every installation;
- claim identical behavior across untested agents;
- require three output files for a quick recommendation or outline preview;
- publish or modify remote systems without explicit user authorization.

## 11. References used for the design

- [Agent Skills specification](https://agentskills.io/specification)
- [Vercel Skills CLI](https://github.com/vercel-labs/skills)
- [Anthropic Skills repository](https://github.com/anthropics/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
