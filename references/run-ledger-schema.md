# Run Ledger and QA Record

Use these records for every course pack. Initialize them with `scripts/init_course_pack.py`; do not invent a parallel checklist.

## State transitions

Use these checkpoint states in order when they apply:

`initialized → acquired → integrity_checked → reconstructed → qa_passed → published → sealed`

A failed item remains in `expected_items` with its error and next action. A scope change updates the declared item list and reason before totals are recalculated. Any change to the source set, edition, scope, chapter Markdown, or generated deliverables increments `artifact_revision` and changes both Learning QA states to `stale` until reviewed again.

## Expected item record

Create one row for every lesson, chapter, episode, required attachment, exercise set, or other component included in the declared denominator:

```json
{
  "item_id": "lesson-01",
  "title": "Lesson title",
  "expected_order": 1,
  "source_locator": "sources/lesson-01.vtt#00:00-12:30",
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

`source_locator` must be an `http://` or `https://` URL, or a real file path relative to the pack with an optional `#timestamp`, `#page`, `#slide`, or section suffix. A descriptive phrase that cannot be opened is not a locator.

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

Each row records `check`, `result`, and concrete `evidence`. Use `not_applicable` only with a `reason`. Evidence names the reviewed unit, locator, page, viewport, or comparison; “checked”, “looks good”, and duplicated boilerplate are not sufficient evidence.

`pdf_visual_review` covers at least the title page, a dense lesson page, a table/list page when present, and the source-notes page. `html_offline_desktop_mobile_print` records the tested viewport sizes, offline state, internal navigation, and print preview. Content judgment remains the Agent's responsibility; scripts only reconcile the recorded claim with files and state.

## Final sealing sequence

After correcting QA failures:

1. record `learning_qa: pass` in both JSON records for the current `artifact_revision`;
2. build all three deliverables;
3. visually inspect HTML and PDF, compare format parity, and record evidence;
4. run `scripts/seal_course_pack.py <pack-dir>` to bind QA to the exact file hashes;
5. run `scripts/validate_course_pack.py <pack-dir>`;
6. use `reconstructed learning artifact complete` only when validation exits successfully.

Rebuild after sealing only when necessary. A rebuild changes file hashes and requires the affected format checks, sealing, and validation again.
