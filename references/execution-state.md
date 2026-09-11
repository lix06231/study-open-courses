# Execution State, Coverage, and Completion

Read this reference whenever eligible real instructional content will be assessed, acquired, reconstructed, compressed, or published, and whenever any exact artifact-level completion name will be used. Apply the Free-Access Processing Gate in `SKILL.md` first. A `report_only` resource may have a public-metadata ledger and metadata-index completion, but never enters instructional-content acquisition or processing.

## Artifact levels

Keep the artifact level explicit. These are different deliverables, not stages that may be silently treated as the same result:

| Artifact level | What it establishes | What it does not establish | Learning QA profile required before its exact completion name |
|---|---|---|---|
| **metadata index** | Resource identity, version, canonical order, expected items, and public metadata. | That instructional content was acquired, verified, or reconstructed. | `metadata_index` profile and applicable learner-facing checks |
| **source coverage map** | The acquired source set, item-level coverage, provenance, integrity status, and gaps. | A learner-ready curriculum or reconstructed teaching. | `source_coverage_map` profile and applicable learner-facing checks |
| **curriculum map** | A learner outcome, prerequisites, dependency-aware sequence, and planned units mapped to sources. | That every planned unit has been reconstructed or verified as a final learning artifact. | `curriculum_map` profile and applicable learner-facing checks |
| **reconstructed learning artifact** | Learner-ready explanations, practice, checks for understanding, provenance, and visible limitations for the declared scope. | Completion beyond its declared scope or of any other artifact level. | `reconstructed_learning_artifact` profile and the full learner-facing check set |

Use only these exact completion names: `metadata index complete`, `source coverage map complete`, `curriculum map complete`, and `reconstructed learning artifact complete`. “Complete” modifies only the named artifact level; never turn one completion into a claim that a later or broader artifact is complete.

Each exact completion name is independently gated. Before using it, record `learning_qa: pass` for its matching profile in [learning-quality.md](learning-quality.md). The profile and applicable-check result are scoped to that artifact level; a pass at an early level never substitutes for QA at a later level. The full learner-facing check set is required when the artifact makes learner-ready teaching claims; early levels run their corresponding profile/schema and explicitly record any inherently non-applicable learner checks with a reason.

## Run ledger

Create or resume one run ledger for the declared resource, scope, and artifact level. Store it at a durable, user-visible project or task location recorded in the handoff; chat-only memory is not a ledger. Persist it atomically after every state mutation and checkpoint so a later run can continue from verified work rather than rediscovering or reprocessing it.

For a course pack, use the machine-readable `run-ledger.json` created by `scripts/init_course_pack.py`. Follow [run-ledger-schema.md](run-ledger-schema.md) for item and QA fields. Keep the required learning and format checks in `evidence/learning-qa.json`; `scripts/validate_course_pack.py` treats missing fields, mismatched revisions or hashes, optimistic rollups, unresolved items, or absent review evidence as completion failures. Each `expected_items` row must retain failed or deferred work rather than deleting it.

The run-level record must include:

- `run_id`, start and last-updated time;
- canonical resource identity, version or edition, source URLs or local identifiers, and `access_class` / `processing_eligibility`;
- learner, outcome, declared scope, `requested_artifact_level`, target artifact level, `delivery_contract`, any explicit user format override, and deadline if one exists;
- declared expected item list and canonical order;
- artifact status, integrity status, checkpoint status, and the exact completion name when one is justified;
- the five coverage totals and rollups below;
- discovery routes, evidence sources, rejected candidates, and why continued search was unlikely to change a Moderate fallback decision when applicable;
- for a Moderate fallback: `confirmation_status` (`pending`, `confirmed`, or `invalidated`), `confirmed_scope`, `confirmed_at` or `confirmation_evidence`, and the confirmed resource identity, edition, and source-set revision;
- `qa_profile`, aggregate `learning_qa`, per-check `qa_result`, `qa_evidence`, `failed_checks`, and the `artifact_revision` tested;
- scope changes, their reason, excluded items, learner impact, and learner acceptance when formal scope is narrowed.

For a request to create a course, `requested_artifact_level` is `reconstructed learning artifact` and the default `delivery_contract` is `three_primary_files`. Neither field may be reduced on resume or during implementation without an explicit user instruction. A blocker changes completion status, not the user's requested artifact.

Maintain one item record for every expected lesson, chapter, episode, page range, exercise, attachment, or other required component. Each item record must include `item_id`, title, expected order, source locator, `item_status`, `attempt_count`, `last_error`, `blocking_impact`, and `next_action`, plus the item's acquired, processed, verified, and reconstructed coverage. Keep failed or deferred items in the ledger; do not erase them to make a rollup appear complete.

## Coverage accounting

Keep these five counts separate for the same declared scope:

| Count | Meaning |
|---|---|
| `expected` | Canonical items or coverage units required by the declared scope. |
| `acquired` | Expected coverage actually obtained from permitted sources. |
| `processed` | Acquired coverage processed by extraction, ASR, OCR, inspection, or another required method. |
| `verified` | Processed coverage checked against the original or an appropriate verification method. |
| `reconstructed` | Verified coverage represented in the learner-ready artifact. |

Report the rollups as `acquired: X/Y`, `processed: X/Y`, `verified: X/Y`, and `reconstructed: X/Y`, where `Y` is the same declared `expected` total. Also record `expected: Y/Y`. Do not substitute one count for another: acquired is not processed, processed is not verified, and verified is not reconstructed.

The item rows and rollups must agree. A changed denominator requires an explicit scope change with its reason and impact; it is not a way to hide missing work.

## Resume, batches, and checkpoints

Resume first. Before starting a new run or retrying work, read the durable ledger, verify the resource identity, edition, source set, scope, and artifact revision, preserve completed item records, and continue from the earliest incomplete, failed, or stale checkpoint. For a Moderate fallback, stop before acquisition unless its persisted confirmation is `confirmed` and matches all of those values; any resource, edition, source-set, or scope change makes it `invalidated` and requires fresh confirmation. Do not reacquire, reprocess, or re-verify an item solely because a run restarted unless its version, evidence, or quality note requires it.

Any mutation to artifact content, declared scope, source coverage, source-set revision, or edition makes an earlier Learning QA pass stale. Set the aggregate result to `stale`, retain its prior evidence and failed-check history, increment or replace `artifact_revision`, persist the mutation, and re-run the matching QA profile before completion or publishing.

Process independent items in batches when useful, but isolate failures. Record the failed item's error, attempt count, blocking impact, and next action; continue independent non-blocking items. Do not let a successful batch erase a failed item, and do not label a batch or whole artifact complete merely because other items succeeded.

Record a checkpoint after each of these boundaries:

1. **acquisition:** source set, acquisition rollup, failed items, and next actions;
2. **integrity:** integrity result, verified rollup, blocking classification, and scope decision;
3. **reconstruction:** reconstructed rollup, provisional status if applicable, dependencies, and revision work;
4. **Learning QA:** profile, artifact revision, aggregate result, per-check results and evidence, failed checks, corrections, and invalidation reason when stale;
5. **publishing:** requested formats, format-level verification, remaining blockers, and exact artifact-level completion name if justified.

## Provisional work and deadline scope

An incomplete batch may support a **provisional reconstruction** only for the evidence currently available. Label it `provisional`, identify missing or unresolved dependencies, state how they may change the result, and retain it as revisable. Provisional work is never a formal completion claim.

When a deadline requires a smaller deliverable, freeze the scope explicitly before continuing: state the included items, excluded items, expected total, outcome change, unresolved dependencies, and next action after the deadline. A deadline never overrides the paid-resource gate, integrity requirements, or formal-completion rules.

## Formal completion gate

Before using any exact completion name, the declared artifact level and scope must be explicit; provenance must support every claim at that level; its matching QA profile must record a current `learning_qa: pass` for the current `artifact_revision`; and no blocker relevant to that level may remain. Then apply the level-specific gate:

- **metadata index:** canonical identity/order, edition/version, access classification, public metadata sources, expected-item basis, uncertainty, and scope are recorded. Instructional-content integrity, acquired/verified coverage, explanations, practice, and publishing formats are not required. This is the only completion level available to a `report_only` resource.
- **source coverage map:** expected items and required channels for the declared eligible scope are itemized; acquired, processed, and verified rollups reconcile; unresolved coverage or provenance gaps affecting the map are blocking. Reconstruction, exercises, learner explanations, and three-format publishing are not required.
- **curriculum map:** learner/outcome, prerequisites, dependency order, planned concepts/practice, time assumptions, source mapping, and plan-versus-built limitations pass. Final teaching explanations, completed exercises, full source reconstruction, and three-format publishing are not required.
- **reconstructed learning artifact:** global integrity for the declared scope passes; all required coverage rollups, including reconstructed coverage, reconcile; no required item is unresolved; the full learner-facing QA profile passes; and publishing verification passes for every requested or default formal format.

If any condition fails, report the precise checkpoint, item, coverage mismatch, or narrower artifact that is honestly available. Do not use an unqualified “complete.”
