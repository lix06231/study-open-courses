# Baseline behavior before study-open-courses v3

Date: 2026-08-20

Method: a fresh evaluator received six realistic requests without access to the v3 design or repository. The observations below summarize its actual decisions; they are not invented failure cases.

## Results

### 1. Goal only: beginner, two hours, learn what AI is

The evaluator inferred a non-technical orientation, proposed a two-hour path, preferred stable and validated materials, checked access constraints, and separated source-derived content from its additions.

**Baseline strength:** lightweight intake and learner-oriented planning already worked.

**Guidance still needed:** make the intake limit and the transition from discovery to Community Validation explicit and reusable.

### 2. User specifies a one-day-old course with about 300 views

The evaluator did not equate low views with low quality. It proposed checking the author, full content, audience, structure, citations, and samples, while treating the course as a candidate or supplement until stronger evidence existed.

**Baseline strength:** it disclosed weak validation instead of rejecting the user-specified source.

**Guidance still needed:** distinguish user-specified handling from proactive primary-source admission, and classify validation consistently as strong, moderate, weak, or unverifiable.

### 3. Famous advanced MIT course versus AI for Everyone

The evaluator chose AI for Everyone for a non-technical beginner with two hours. It treated fame as insufficient evidence of fit and proposed checking current prerequisites, length, and access.

**Baseline strength:** learner fit already beat institutional fame.

**Guidance still needed:** formalize the order: validation admits candidates; fit ranks admitted candidates.

### 4. Replace the novel *To Live* with a two-hour distilled course

The evaluator offered a reading guide and thematic course, preserved the distinction between analysis and literary experience, avoided extensive copyrighted reproduction, and disclosed that the artifact could not replace the original.

**Baseline strength:** Learning Suitability was recognized.

**Guidance still needed:** provide stable suitability outcomes that also cover skill-based and experience-heavy materials.

### 5. Generate a complete textbook from a Coursera landing page and syllabus

The evaluator refused to claim that metadata was the full course. It offered either an explicitly original companion guide or a faithful reconstruction after obtaining transcripts or notes, while recording source and access date.

**Baseline strength:** metadata was not confused with instructional content.

**Guidance still needed:** make Source Resolver and Content Ingestion separate gates and specify a content-source preference order.

### 6. Transcripts with a missing lesson and a duplicated lesson

The evaluator proposed a manifest, missing/duplicate checks, version comparison, source mapping, explicit gaps, and a dependency-sensitive decision about whether to continue.

**Baseline strength:** it did not silently invent missing content.

**Guidance still needed:** standardize the Integrity Check record and require it before reconstruction or compression.

## Cross-scenario conclusion

The no-skill baseline did not exhibit the crude failures the v3 design anticipated. The actual weakness was inconsistency across requests: there was no single workflow contract connecting selection, suitability, acquisition, integrity, provenance, reconstruction, compression, and publishing. The new skill should therefore use a positive staged recipe, not a long prohibition list.

Specific additions justified by the baseline:

- two entry routes with minimal intake;
- Community Validation as an admission gate with four qualitative states;
- Learner Fit Ranking only after admission;
- three Learning Suitability outcomes;
- distinct Source Resolver and Content Ingestion stages;
- a required integrity manifest and provenance map;
- reconstruction before optional compression;
- a publishing contract that exposes sources, gaps, interpretation, omissions, and next steps.

## Portable v3.1 baseline

Date: 2026-08-20

An independent evaluator received the published v3 `SKILL.md` and this scenario: a confirmed, lawfully accessible public video course; no transcript, notes, audio, or video supplied by the user; a playlist is available; and the host has web, media-download, and speech-to-text capabilities.

**Result: FAIL.**

The old skill says to continue looking for lawful transcripts, captions, notes, slides, documents, or media and lists authorized audio/video transcription as an ingestion option. It also checks transcript timing, speakers, OCR, and obvious recognition problems. However, the wording does not require the agent to inspect available host capabilities and use them before asking the user for missing material.

The escape routes are observable in these clauses:

- ingestion happens “when available and appropriate”;
- when content cannot be acquired, the agent may “ask for the missing material”;
- metadata-only reconstruction is a stop condition.

The baseline therefore permits an agent to hand acquisition back to the user without first attempting captions or available ASR. Passing guidance must require autonomous capability discovery and lawful ingestion before that stop condition applies.

### Portability audit

The published README calls the project a “Codex Skill” and describes manual installation into Codex's skill directory. The published `SKILL.md` also requires “absolute local paths” and refers to a “PDF-specific skill.” Those phrases are not fatal to the learning workflow, but they tie packaging and delivery to one host's vocabulary. The portable revision must replace them with Agent Skills terminology and capability-dependent host-neutral language.
