---
name: study-open-courses
description: Use when a person wants to choose, assess, acquire, reconstruct, compress, or publish a course or other learning resource for human study. Applies to courses, books, PDFs, video or podcast series, tutorials, interviews, and official documentation; not generic summarization or model knowledge injection.
license: MIT
metadata:
  author: "lix06231"
  version: "3.2"
  compatibility: "Internet access is needed for discovery; media, transcription, OCR, and rendering depend on host capabilities."
---

# Study Open Courses

Turn trustworthy source material into something a person can actually learn from.

**Core principle:** 大众验证负责入围，学习适配负责排名。 Community validation is the admission gate for a proactively recommended primary resource; learner fit determines the order among admitted resources.

This is a learner-first workflow. It accepts multiple content types only when they serve a human learning goal. It is not a general-purpose summarizer, arbitrary content distiller, or model knowledge-ingestion pipeline.

## Free-Access Processing Gate

Classify every identifiable resource before Community Validation, any instructional-content access, or inclusion in a processing-primary candidate set. Only `free_access` sources enter the processing-primary candidate set.

Record `access_class` and `processing_eligibility` for every candidate or named resource:

| `access_class` | `processing_eligibility` | Required handling |
|---|---|---|
| `free_access` | `eligible` | Real instructional content is reachable without payment, subscription, trial, credits, institutional entitlement, or a purchased account. It may proceed subject to platform, copyright, and authorization rules. A free account login is allowed when no paid entitlement is involved. |
| `paid_or_entitlement_gated` | `report_only` | Use public metadata and community evidence only. Never open gated lessons or use a paid authenticated session. |
| `public_excerpt` | `eligible_limited` | Process only the excerpt's actual public coverage. Never infer the paid remainder or call the excerpt complete. |
| `official_free_edition` | `eligible_as_separate_source` | Treat as a separate source with its own version, scope, completeness, validation, and provenance. |
| `unknown` | `blocked_pending_classification` | Do not ingest. Resolve access status or continue discovery. |

`report_only` forbids opening gated lessons; using a paid authenticated session; downloading; capturing; recording; ASR; OCR; extracting; translating; compressing; or reconstructing gated instructional content. This is a Skill policy, not a legal-rights estimate. User purchase, explicit authorization, lack of DRM, a logged-in browser, a deadline, personal-use intent, or technical feasibility cannot override it.

For a goal-only task, an especially suitable `paid_or_entitlement_gated` resource may appear only in a clearly separate “paid option for manual study” note based on public metadata. State that payment is required, do not imply inspection of gated content, and continue looking for `free_access` alternatives.

## Route the request

### The user named a resource

Assess that resource directly. Do not restart with generic recommendations.

Record `Discovery: not applicable` and `Candidate Ranking: not applicable`. Record validation strength and learner fit descriptively rather than as rejection gates, together with suitability, access class, processing eligibility, and content completeness. A user-specified resource with weak or unverifiable community validation may still be used; disclose the limitation and suggest a validated anchor or supplement only when that would materially improve learning reliability.

Run the Free-Access Processing Gate before any instructional-content access. For a user-named `paid_or_entitlement_gated` resource, assess only public metadata and community evidence, explain the processing boundary, suggest studying the original manually if the learner chooses to purchase it, and offer `free_access` alternatives. Only content already publicly accessible and classified `eligible_limited` may be processed as an excerpt, and only to its actual public coverage. User-authored notes and reflections may support tutoring only when they do not reproduce gated instructional content. A purchase, login, authorization, or copied gated excerpt never creates an exception.

### The user named only a learning goal

Reuse everything already known. Ask only questions that would change the resource choice, normally no more than four:

- What do they want to learn?
- What is their current level?
- What should they understand or be able to do afterward?
- How much time can they invest?

Then discover candidates, classify access before validation, and exclude every non-`free_access` source from the processing-primary candidate set. Prefer resources with an existing teaching structure, but allow a book, PDF, video or podcast series, tutorial, long interview, official documentation, or deliberate small source bundle when it fits better. Recommend one to three candidates with one clear primary choice.

Before the learner confirms a Moderate `free_access` fallback, inspect only public metadata and a representative public sample needed for assessment. Do not bulk-acquire or reconstruct that resource. A reasonable search records discovery routes, evidence sources, candidates rejected, and why continued search is unlikely to change the decision.

## Follow the learner-first workflow

Use the stages in order. A task may stop after recommendation or assessment when that is all the user requested.

1. Learning Goal or named-resource intake
2. Learning Resource Discovery (goal-only; `not applicable` for a named resource)
3. Free-Access Processing Gate
4. Community Validation
5. Learner Fit Ranking (goal-only; `not applicable` for a named resource)
6. Learning Suitability
7. Source Resolver
8. Content Ingestion
9. Integrity Check
10. Evidence & Provenance
11. Learning Reconstruction
12. Learning Compression when useful
13. Learning QA at the declared artifact level
14. Publishing

Do not reconstruct a faithful course from a landing page, syllabus, table of contents, review, or search snippet. Those are discovery metadata, not instructional content.

## Select the learning resource

### Community Validation

Apply this gate before ranking resources that the skill proactively recommends as the primary source. Do not treat views, enrollment, institutional fame, creator claims, or a polished syllabus alone as proof.

Consider the combined evidence:

- sustained learner adoption or readership;
- review quality and completion feedback;
- independent discussion in relevant communities;
- repeated recommendations from independent sources;
- credible institution or domain-expert standing;
- time for reputation and corrections to accumulate;
- freshness for subjects that change quickly.

Assign one evidence-backed state:

| State | Primary-source use |
|---|---|
| **Strong** | Eligible for proactive primary recommendation. |
| **Moderate** | Eligible as a candidate; keep looking for a strong option when practical. |
| **Weak** | Normally supplemental, unless the user specified it. |
| **Unverifiable** | Do not proactively present it as a proven primary resource. |

A proactive primary recommendation requires Strong validation. If only Moderate candidates remain after a reasonable search, say that no Strong option was verified and present the Moderate option only as a disclosed fallback that requires the learner's confirmation. Do not silently promote it to primary.

Use these boundaries:

- **Strong:** multiple independent signals agree, including evidence beyond the creator or publisher, with meaningful learner experience or enough scrutiny for limitations to surface.
- **Moderate:** at least one substantive independent signal exists, but breadth, duration, completion evidence, or cross-source agreement is limited.
- **Weak:** signals are sparse, shallow, mostly anecdotal, or dominated by launch publicity, raw traffic, the creator, or the publisher.
- **Unverifiable:** reliable external learner-validation evidence cannot be found or the resource is too new for a defensible assessment.

Do not promote a resource to Strong from one metric or review. Do not demote a specialist resource merely because its absolute audience is small. State the supporting evidence and what could not be verified. Popularity is one signal inside validation, never the ranking itself.

### Learner Fit Ranking

Rank admitted candidates by:

- learner level and prerequisites;
- desired outcome;
- available time;
- teaching quality and clarity;
- content completeness;
- freshness and version relevance;
- language, cost, registration, region, and accessibility.

Use qualitative reasoning rather than fabricated decimal scores. A famous advanced course should lose to a well-validated beginner course when the learner is a beginner.

## Decide Learning Suitability

Choose one outcome before acquisition or compression:

| Outcome | Use when | Result |
|---|---|---|
| **Course reconstruction** | Knowledge, skills, technical subjects, or structured methods can be taught through progression and practice. | Build a learnable course. |
| **Assisted learning** | The original experience matters, but guidance can improve understanding. | Produce a reading, viewing, or listening companion with context and questions. |
| **Do not replace the original** | Literary, artistic, experiential, or context-dependent value would be destroyed by substitution. | Explain the limit and support engagement with the original. |

Suitability is not a quality judgment. A great novel can be a poor candidate for replacement.

## Resolve, acquire, and verify source content

Keep acquisition separate from learning reconstruction.

Whenever a named or identifiable resource's real content must be acquired, reconstructed, compressed, or published, first apply the Free-Access Processing Gate. If `processing_eligibility` permits the requested content work, read [references/source-acquisition.md](references/source-acquisition.md) and [references/execution-state.md](references/execution-state.md) before acquiring or processing it. This is required even when the resource has not become the primary recommendation and even when the user supplied no transcript, notes, or files. `report_only` resources never proceed to content work.

The required outcome is one of:

- a complete-enough source manifest, integrity result, and provenance map;
- a deliberately narrowed learning scope supported by the acquired evidence;
- a precise blocker that identifies the permission, access, missing dependency, or unavailable host capability.

If lawful access is available and the host has useful capabilities, continue through text extraction, caption discovery, OCR, media access, or speech-to-text without asking the user to perform those solvable steps. “No material was supplied” is not itself a blocker.

Never bypass authentication, payment, DRM, regional restrictions, copyright boundaries, platform rules, or the user's authorization. Never ask the user to reveal a password, session token, cookie, or other reusable credential; when supported, ask them to authenticate through the host or browser they control and then confirm access.

## Reconstruct learning

### Learning Reconstruction

Use the run ledger and completion rules in [references/execution-state.md](references/execution-state.md). Reconstruction may be provisional while independent batches finish or dependencies are unresolved, but it must be visibly labeled provisional and revisable. Do not call a formal artifact complete until global integrity passes, no blocking item or unresolved status remains, and every coverage rollup matches the declared scope.

Do not merely summarize the source in its original order. Rebuild it around the learner's target outcome:

1. define the outcome and prerequisites;
2. sequence concepts by dependency;
3. explain each concept in learner-appropriate language;
4. preserve essential examples and add clearly labeled explanations when needed;
5. add practice, reflection, or application;
6. add checks for understanding and feedback guidance;
7. connect each unit to the next and to the final outcome.

Preserve distinctions among source fact, instructor position, community experience, and new synthesis.

### Learning Compression

Compress only after the learning structure works. Choose depth from the learner's goal and time, not from a target reduction ratio.

Preserve prerequisites, causal links, worked examples needed for transfer, practice, and known limitations. Record what was omitted, merged, or deferred. If compression would break learning or replace an essential experience, shorten the scope rather than pretending the learning outcome remains unchanged.

### Learning QA

Before using any exact artifact-level completion name—`metadata index complete`, `source coverage map complete`, `curriculum map complete`, or `reconstructed learning artifact complete`—read [references/learning-quality.md](references/learning-quality.md), even when the work has not reached reconstruction. Apply the matching artifact-level schema/profile and every learner-facing check that is applicable to the declared level; early levels must record why any full learner check is not applicable, rather than omit it. A reconstructed learning artifact, or any artifact claiming learner-ready teaching, must pass the full learner-facing check set. Record the single gate result `learning_qa: pass` or `learning_qa: fail` with the profile, evidence, affected units, and correction or next action. Every exact completion name requires `learning_qa: pass`; a failure returns the work to reconstruction, compression, or scope clarification and cannot be hidden by a polished format or an artifact at a lower level.

## Publish the learning artifact

Match the artifact to the suitability decision: course, study guide, reading/viewing/listening companion, lesson plan, workbook, or curriculum map.

Every final artifact must contain:

1. learner and outcome;
2. prerequisites and expected time;
3. learning path or unit structure;
4. explanations, examples, and practice appropriate to the goal;
5. checks for understanding;
6. source and provenance notes;
7. integrity gaps, uncertainty, and access limitations;
8. compression or omission notes;
9. next steps, including when to return to the original source.

When preparing downloadable files or claiming a formal course is complete, read and follow [references/learning-quality.md](references/learning-quality.md) and [references/publishing.md](references/publishing.md). A formal complete learning artifact defaults to equivalent Markdown, self-contained HTML, and PDF unless the user explicitly requests particular formats. Here, self-contained HTML literally means one `.html` file with embedded permitted styles and small assets; requested sidecars are an offline package, not self-contained HTML. A preview, recommendation, outline, or interim checkpoint does not require the three-file bundle.

Publishing prepares the artifact. It does not authorize an upload, post, repository change, push, or other external mutation.

## Stop conditions

Pause and explain the smallest required next input only when:

- no candidate meets the primary-source validation gate and the user did not specify one;
- allowed discovery and available acquisition capabilities were attempted, but only metadata remains for a requested faithful reconstruction;
- a blocking source segment or prerequisite is missing;
- the run ledger has a blocking item, unresolved status, or a coverage total that does not match the declared scope;
- Learning QA fails for the declared artifact and scope;
- the requested compression would falsely imply replacement of an irreducible work;
- access, copyright, platform rules, authorization, or unavailable host capabilities block the requested ingestion or publication.

Offer the smallest honest alternative: a validated substitute, a supplemental resource, an original companion guide, a narrower course, or an assisted-learning artifact.
