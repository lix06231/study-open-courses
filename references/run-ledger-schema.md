# Run Ledger and QA Record

Use these records for every course pack. Initialize them with `scripts/init_course_pack.py`; do not invent a parallel checklist.

## State transitions

Use these checkpoint states in order when they apply:

`initialized → acquired → integrity_checked → acquisition_gate_passed → reconstructed → built_pending_review → review_pending → qa_passed → sealed → validated`

A failed item remains in `expected_items` with its error and next action. A scope change updates the declared item list and reason before totals are recalculated. Any change to the source set, edition, scope, chapter Markdown, or generated deliverables increments `artifact_revision` and changes both Learning QA states to `stale` until reviewed again.

## Expected item record

Create one row for every lesson, chapter, episode, required attachment, exercise set, or other component included in the declared denominator:

```json
{
  "item_id": "lesson-01",
  "title": "Lesson title",
  "expected_order": 1,
  "source_locator": "sources/lesson-01.vtt#L1-L240",
  "item_status": "READY",
  "attempt_count": 1,
  "last_error": "none",
  "blocking_impact": "none",
  "next_action": "none",
  "acquired": true,
  "processed": true,
  "verified": true,
  "reconstructed": true
}
```

For formal v4.2 packs `source_locator` addresses retained content with an exact local `#Lstart-Lend` range. URLs are source origins, not acquired-content evidence. Preserve time/page/slide identifiers in retained text and notes. Inventory, source records, scope, channels and claim map must satisfy [content-evidence-contract.md](content-evidence-contract.md).

The five coverage totals are derived from these rows. `expected` equals the row count; each other total equals the number of rows whose corresponding Boolean is `true`. Never type totals that disagree with the rows.

## Learning QA record

For a reconstructed learning artifact, `evidence/learning-qa.json` contains all nine learning checks:

- `objective_traceability`
- `prerequisite_order`
- `source_accuracy`
- `labeled_synthesis`
- `correct_examples`
- `feedback_guidance`
- `compression_integrity`
- `time_estimate_assumptions`
- `visible_limitations`

It also contains these four format checks:

- `markdown_complete`
- `html_offline_desktop_mobile_print`
- `pdf_visual_review`
- `format_parity`

Each row records `check`, `result`, `evidence` (exact local report range) and `evidence_sha256` (whole-report hash). Use `not_applicable` only with a reason for a truly inapplicable non-core check. Objective traceability, source accuracy, labeled synthesis, compression integrity and visible limitations always apply to formal courses. Duplicate checks are rejected. Evidence describes actual source comparisons/render inspection, not generic repeated assertions or planned future actions.

`pdf_visual_review` covers at least the title page, a dense lesson page, a table/list page when present, and the source-notes page. `html_offline_desktop_mobile_print` records the tested viewport sizes, offline state, internal navigation, and print preview. Content judgment remains the Agent's responsibility; scripts only reconcile the recorded claim with files and state.

## Final sealing sequence

After correcting QA failures:

1. obtain/verify complete declared sources; run `scripts/validate_source_evidence.py <pack-dir>` before drafting;
2. write source-backed chapters and claim map; finalize reconstruction flags and other semantic ledger fields, then build all three deliverables (old QA becomes stale);
3. run `scripts/capture_qa_snapshot.py <pack-dir>`; capture current input/output hashes and clear current checks while preserving history;
4. actually compare content with sources, inspect HTML/PDF and format parity; write local review reports and required checks with their report hashes;
5. record `learning_qa: pass` in both JSON records only if every applicable check passes; retain prior failures in `history`;
6. set the candidate ledger's `artifact_status: complete`, `completion_name: reconstructed learning artifact complete`, and empty resolved blockers; these are claims awaiting seal/validation, never proof by themselves;
7. run `scripts/seal_course_pack.py <pack-dir>`; it verifies existing review hashes, sources, scope and all required checks, and cannot retroactively hash unreviewed changes;
8. run `scripts/validate_course_pack.py <pack-dir>`; only success permits the formal user-facing completion name.

The snapshot stores `review_input_hashes`, `artifact_hashes`, `artifact_content_sha256`, `review_started_at`. Changes to sources, scope, semantic ledger fields, chapters or build settings invalidate it. Checkpoint/QA/completion fields may change during review. Never hand-edit snapshot hashes to preserve an old pass. QA history and source originals are internal records, not public course downloads.

Rebuild after sealing only when necessary. A rebuild changes file hashes and requires the affected format checks, sealing, and validation again.
