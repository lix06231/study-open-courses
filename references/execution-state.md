# Execution State, Coverage, and Completion

Read this reference whenever an eligible resource's real instructional content will be acquired, reconstructed, compressed, or published. Apply the Free-Access Processing Gate in `SKILL.md` first: a `report_only` resource never enters this workflow.

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

Create or resume one run ledger for the declared resource, scope, and artifact level. Keep it with the working record so a later run can continue from verified work rather than rediscovering or reprocessing it.

The run-level record must include:

- `run_id`, start and last-updated time;
- canonical resource identity, version or edition, source URLs or local identifiers, and `access_class` / `processing_eligibility`;
- learner, outcome, declared scope, target artifact level, and deadline if one exists;
- declared expected item list and canonical order;
- artifact status, integrity status, checkpoint status, and the exact completion name when one is justified;
- the five coverage totals and rollups below;
- discovery routes, evidence sources, rejected candidates, and why continued search was unlikely to change a Moderate fallback decision when applicable;
- scope changes, their reason, excluded items, learner impact, and learner acceptance when formal scope is narrowed.

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

Resume first. Before starting a new run or retrying work, read the current ledger, verify the resource identity and scope, preserve completed item records, and continue from the earliest incomplete, failed, or stale checkpoint. Do not reacquire, reprocess, or re-verify an item solely because a run restarted unless its version, evidence, or quality note requires it.

Process independent items in batches when useful, but isolate failures. Record the failed item's error, attempt count, blocking impact, and next action; continue independent non-blocking items. Do not let a successful batch erase a failed item, and do not label a batch or whole artifact complete merely because other items succeeded.

Record a checkpoint after each of these boundaries:

1. **acquisition:** source set, acquisition rollup, failed items, and next actions;
2. **integrity:** integrity result, verified rollup, blocking classification, and scope decision;
3. **reconstruction:** reconstructed rollup, provisional status if applicable, dependencies, and revision work;
4. **publishing:** requested formats, format-level verification, remaining blockers, and exact artifact-level completion name if justified.

## Provisional work and deadline scope

An incomplete batch may support a **provisional reconstruction** only for the evidence currently available. Label it `provisional`, identify missing or unresolved dependencies, state how they may change the result, and retain it as revisable. Provisional work is never a formal completion claim.

When a deadline requires a smaller deliverable, freeze the scope explicitly before continuing: state the included items, excluded items, expected total, outcome change, unresolved dependencies, and next action after the deadline. A deadline never overrides the paid-resource gate, integrity requirements, or formal-completion rules.

## Formal completion gate

Before using an exact completion name, confirm all of the following for that named artifact level:

1. its declared scope and item rows are current;
2. no item with `blocking_impact: blocking` remains;
3. no required item has an unresolved status, error, dependency, or next action;
4. all five coverage totals and `X/Y` rollups match the declared scope and the level's claim;
5. global integrity passes before finalization;
6. `learning_qa: pass` is recorded for the matching artifact-level profile, with the full learner-facing check set when applicable and explicit reasons for any early-level non-applicable checks; and
7. required checkpoints, including publishing verification when publishing is claimed, are recorded.

If any condition fails, report the precise checkpoint, item, coverage mismatch, or narrower artifact that is honestly available. Do not use an unqualified “complete.”
