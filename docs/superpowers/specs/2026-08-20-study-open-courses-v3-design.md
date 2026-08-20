# study-open-courses v3 Design

## Purpose

`study-open-courses` helps a human choose trustworthy learning resources, obtain their real content, and reconstruct that content into a learnable course or study guide. It is not a general-purpose content distiller and is not intended to inject condensed knowledge into a model.

## Repository shape

The repository is one installable skill:

```text
study-open-courses/
|-- SKILL.md
|-- README.md
|-- references/          # Add only if conditional detail cannot stay concise
|-- docs/superpowers/    # Design and implementation records
`-- .gitignore
```

The first version should remain self-contained unless validation shows that `SKILL.md` is too large or hard to navigate.

## Entry routes

1. If the user supplies a specific course, book, video series, podcast, PDF, website, or documentation set, assess that resource directly. Do not restart with generic recommendations.
2. If the user supplies only a learning goal, ask at most the few questions that materially affect selection: topic, current level, desired outcome, and available time. Reuse known context and then recommend one to three candidates.

## Required workflow

1. **Learning Goal** establishes the learner's current state and desired outcome.
2. **Learning Resource Discovery** finds courses first, while allowing books, video series, podcasts, interviews, tutorials, official documentation, and deliberate multi-source combinations.
3. **Community Validation** is a gate for resources proactively recommended as the primary source. Popularity alone is not a rank. Validation considers sustained learner adoption, review quality, independent discussion, institutional or expert standing, time accumulation, and completion feedback. Classify evidence as strong, moderate, weak, or unverifiable.
4. **Learner Fit Ranking** ranks candidates that pass the gate by learner level, goal, time, quality, completeness, freshness, and accessibility.
5. **Learning Suitability** decides whether the material can be reconstructed as a course, should remain an assisted-reading experience, or should not be treated as a substitute for the original work.
6. **Source Resolver** identifies the newest, complete, lawful, and highest-quality content source. A landing page or syllabus is not treated as the course content.
7. **Content Ingestion** acquires real instructional material, preferring native text or official transcripts, then official/platform captions, slides or notes, and finally audio/video transcription when appropriate and authorized.
8. **Integrity Check** checks coverage, ordering, missing segments, duplicates, transcription quality, and version consistency before reconstruction.
9. **Evidence & Provenance** preserves source URLs, resource versions, access dates, lesson-to-source mappings, gaps, and uncertainty. Claims must remain distinguishable from interpretation.
10. **Learning Reconstruction** reorganizes material around prerequisites, explanations, examples, practice, checks for understanding, and progression. It does not merely summarize in source order.
11. **Learning Compression** shortens only after reconstruction. It preserves learning dependencies and labels omissions; it never optimizes for maximum density at the expense of learnability.
12. **Publishing** produces an appropriate human-learning artifact with clear structure, source notes, limitations, and next actions. It must not imply that publication, upload, or external mutation is authorized.

## Boundaries borrowed from cangjie-style workflows

- Accept multiple source types without promising that every source should be distilled.
- Keep source acquisition separate from learning reconstruction.
- Preserve traceability from the published lesson back to source material.
- Do not inherit a universal-content scope, model-memory orientation, or the assumption that compression is always desirable.

## README positioning

The README must explain that:

- this skill is learner-first rather than model-first;
- it chooses and reconstructs educational resources rather than distilling arbitrary content;
- community validation controls admission to proactive primary recommendations, while learner fit controls ranking;
- literary, artistic, experiential, or incomplete works may receive guidance rather than replacement;
- provenance and integrity are required before compression or publication.

## Validation

- Frontmatter and skill folder naming pass `quick_validate.py`.
- A goal-only scenario triggers lightweight questions and validated recommendations.
- A user-specified weakly validated resource is processed with an explicit warning instead of being rejected.
- A popular but mismatched resource loses to a better-fit resource after both pass validation.
- A novel or experiential work is routed to assisted learning, not replacement.
- A syllabus-only source is rejected as insufficient content.
- A final learning artifact exposes provenance, gaps, and compression decisions.

## Authorization and Git

Initialize only a local repository at `A:\Code\study-open-courses`. Do not create a GitHub repository, add a remote, commit, push, or open a pull request without separate authorization.
