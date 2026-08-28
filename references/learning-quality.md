# Learning Quality Assurance

Read this reference before using any exact artifact-level completion name, including early metadata and planning artifacts, and before publishing. It consumes the available artifact content, coverage rollups, source map, declared scope, and artifact level from [execution-state.md](execution-state.md). It produces one recorded gate result, `learning_qa: pass` or `learning_qa: fail`, scoped to the declared artifact level.

Learning QA does not replace Integrity Check. Integrity Check establishes whether the source evidence and coverage can support the scope; Learning QA establishes whether the learner-facing artifact uses that support honestly and teachably.

## QA record and decision

For each check, record the artifact level, matching profile, affected unit or section, source locators or coverage evidence, result (`pass` or explicitly justified `not_applicable`), and smallest correction or next action. `learning_qa: pass` requires the matching artifact-specific profile/schema and every applicable check below to pass. A check may be `not_applicable` only when the declared artifact cannot make that learner-facing claim; the reason must be recorded. Any failure requires correction, a narrower declared scope, or an honest lower-level artifact; it blocks the exact completion name for the failed artifact.

The nine checks below are the full learner-facing check set. Apply that full set to a reconstructed learning artifact and to any artifact that claims learner-ready teaching. For a metadata index, source coverage map, or curriculum map, run the corresponding early-level profile/schema below plus every applicable learner-facing check, and record justified `not_applicable` results for the rest. Do not turn a pass for one artifact level into a pass for another: every exact completion name requires its own `learning_qa: pass`.

## Required learning checks

| Check | Pass condition |
|---|---|
| Objective traceability | Each stated outcome maps to one or more units, practice activities, and checks for understanding. No unit claims an outcome unsupported by its verified source coverage. |
| Prerequisite order | Prerequisites are explicit and appear before dependent concepts, examples, or practice. A missing prerequisite is taught, linked as required prior study, or narrows the outcome. |
| Source accuracy | Source-derived statements, names, numbers, code, formulas, quotations, and instructions agree with the source map and verified locators. Unverified coverage is not presented as fact. |
| Labeled synthesis | New explanations, analogies, examples, translations, and cross-source synthesis are visibly distinguished from source fact and instructor position. |
| Correct examples | Worked examples have correct reasoning and results, use valid inputs and assumptions, and do not imply that an invented example came from the source. |
| Feedback guidance | Each meaningful practice or check tells the learner how to judge an answer, where to find the expected result or rubric, and what to revisit after a weak result. |
| Compression integrity | Omitted, merged, or deferred material is recorded. Compression preserves required prerequisites, causal links, transfer examples, practice, limitations, and the stated outcome; otherwise the outcome or scope is narrowed. |
| Time-estimate assumptions | Expected time names the learner level, pace, included activities, and any excluded preparation, reading, watching, or practice. Do not present a guess as a universal completion time. |
| Visible limitations | Integrity gaps, uncertainty, access limits, source-version limits, translation uncertainty, and scope exclusions appear where they affect learning and in the final limitations or provenance notes. |

## Artifact-specific minimum schemas and QA profiles

Use the declared artifact level from [execution-state.md](execution-state.md). These are minimum content contracts and QA profiles, not substitutes for the ledger, source manifest, coverage accounting, or exact completion names in that reference. A profile passes only when its schema and applicable learner-facing checks pass.

### Metadata index (`metadata_index` profile)

Include canonical resource identity, creator or publisher when known, edition or version, access class and processing eligibility, canonical item order and expected item list, public metadata sources, declared scope, access date when relevant, and known metadata uncertainty. It must state that it does not establish acquired instructional content, verified coverage, or learner-ready teaching. Its QA may mark teaching-specific checks not applicable only with that boundary and a reason.

### Source coverage map (`source_coverage_map` profile)

Include the declared scope and expected-item total; item-level source locators; access class and processing eligibility; speech, visual, practice, and attachment coverage; acquired, processed, verified, and reconstructed coverage; integrity status; gaps and blocking impact; source-version or translation notes; and the coverage rollups. It must not claim a learner-ready sequence merely because items are mapped.

### Curriculum map (`curriculum_map` profile)

Include learner and measurable outcome, explicit prerequisites, dependency-aware unit order, unit objectives, planned concepts and practice, source-locator mapping, expected time assumptions, and the limits of planned versus reconstructed content. It must not claim every unit has learner-ready explanations or verified final teaching unless that is separately supported.

### Companion

Include the original resource to use, learner and purpose, access and experience boundary, expected time assumptions for the paced reading/viewing/listening path, prompts or activities, feedback or self-check guidance, source/provenance notes, visible limitations, and next steps that return the learner to the original. It must not present itself as a substitute for an irreducible or unverified original experience. A companion has no independent completion name beyond the artifact levels defined in `execution-state.md`.

### Reconstructed course (`reconstructed_learning_artifact` profile)

Include learner and outcome, prerequisites, expected time assumptions, dependency-ordered units, learner-appropriate explanations, correctly labeled source material and synthesis, valid examples, practice, checks with feedback guidance, precise provenance, coverage and integrity limitations, compression or omission notes, and next steps. It may use `reconstructed learning artifact complete` only when every formal completion condition in `execution-state.md` and every applicable Learning QA check passes.

## Failure handling

When QA fails, name the failed check, affected outcome and unit, evidence or locator, learner impact, and smallest correction. Re-run the affected QA checks after correction. Do not resolve a failure by deleting the record, weakening the label, hiding a limitation, or calling a lower artifact level a completed course.
