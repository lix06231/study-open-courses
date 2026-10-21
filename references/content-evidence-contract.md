# Retained Content Evidence Contract (v4.2)

Read before drafting reconstructed teaching. This is the executable formal-pack schema shared by acquisition, build, snapshot, seal and final validation. Early evaluation may inspect representative content without claiming full coverage; the formal builder requires the complete declared scope.

## Acquire first, write second

1. Save a lawful canonical syllabus/playlist/document listing under `sources/` as the inventory, preserving origin, edition, titles, order and required channels. Metadata defines the denominator; it does not teach the course.
2. Obtain actual permitted text/transcripts/captions and independently required visuals, exercises, code and attachments. Retain originals; store extraction/ASR separately with page/time boundaries. Internal evidence retention is not permission to redistribute it.
3. Record source origin, acquisition method/date, exact local content, hash, coverage basis and concrete verification notes. Notes/slides alone cannot replace missing speech. Captions/ASR need timed segments checked against original duration and any large gaps. ASR/OCR/slides need distinct retained original media/PDF/page images and their hashes.
4. Determine channel requirements through actual lesson/material inspection. `channel_basis` names inspected material or visual references; do not declare `primary` alone because other channels were difficult to acquire. `TEXT_ONLY`/AI illustration describe output choices and never discharge original visual acquisition.
5. Run `validate_source_evidence.py <pack-dir>` before instructional drafting. Success saves `evidence/acquisition-gate.json`. The builder compares that snapshot with current sources, expected items, identity and scope. Changes require acquisition/re-verification and a fresh gate.

Never author fake transcripts, relabel landing pages as lecture text, use secondhand summaries as primary teaching, or write reports about verification actions not performed. A missing transcript is a gap to resolve, not an invitation to teach from model memory. Do not change the named resource or artifact request to avoid the gate.

## `source-manifest.json`

Required top-level keys: `schema_version: 1`, `inventory`, `scope`, `records`.

`inventory` contains `origin` (canonical URL or supplied-file identity), `local_path`, `sha256`, `locator` (retained listing and exact local range), and `items`. Each item has `item_id`, `title`, `inventory_locator`, `required_channels`, `primary_kind`, `channel_basis`. Titles must occur in their own inventory ranges. Preserve separate attachment items when the original course organizes them that way.

`required_channels` includes `primary` plus required `visual`, `practice`, `attachment`. `primary_kind` is `speech` for spoken lessons or `text` for native written teaching. Speech items also need numeric `duration_seconds` and a retained `duration_evidence_locator`.

`scope` contains `basis`, `included_item_ids`, `exclusions`. Included plus excluded IDs partition the whole canonical inventory. Each exclusion contains `item_id`, reason and learning impact, and a local `authorization_locator` retaining the actual user's scope instruction/acceptance. When the original request already selects a week/chapter/excerpt, retain that instruction; do not ask again. A whole-course request cannot become a subset through Agent judgment or deletion of blocked items. Keep unresolved items until legitimate scope change. Never present an Agent's paraphrase as user consent.

Each `records` entry has these fields:

| Field | Required evidence |
|---|---|
| `source_id`, `unit_id`, `channel` | Unique source identity, declared unit, and one required channel |
| `content_kind` | `lecture_text`, `transcript`, `captions`, `asr`, `slides`, `exercise`, `code`, `attachment` |
| `origin`, `acquired_at` | Actual original URL/file identity and acquisition time |
| `acquisition_method` | `native_text`, `official_captions`, `platform_captions`, `asr`, `ocr`, `user_file` |
| `coverage_basis` | Evidence that retained material covers the original unit, including boundaries and omissions |
| `access_class`, `processing_eligibility` | Matching permitted pair from the free-access gate |
| `local_path`, `sha256` | Retained instructional text/inspection record and actual whole-file SHA-256 |
| `locator`, `content_evidence` | Exact retained line range and its exact text, preserving internal newlines |
| `verification.method` | Actual comparison method |
| `verification.evidence_locators` | Local report ranges containing concrete source checks and results |

For ASR/OCR/slides also provide `raw_path`, `raw_sha256`: distinct original media/PDF/page-image evidence. For large caption gaps provide `verification.timing_gap_evidence_locator`, describing original silence/visual activity or a repair; unresolved gaps block integrity.

Formal locators use retained UTF-8 text ranges `relative/path#Lstart-Lend` (inclusive; `#L12` for one line). Preserve original timestamp/page/slide identifiers in that text and review notes. URLs establish origin, not acquisition. PDF/images/media need extracted text or inspection records alongside originals; extracted text does not prove a diagram was understood.

`evidence-ledger.csv` matches expected IDs exactly, one row per item. `source_locator` resolves to retained primary content; `content_evidence` equals that range; `evidence_size` is the whole primary file's actual byte count; `first_locator` and `last_locator` reach its actual boundaries. Size is a consistency check, not a quality threshold or proof of full original coverage. Coverage notes, canonical duration and actual source review must show the file is not truncated.

## Claim-level source map

`evidence/source-map.json` has `schema_version: 1` and `citations`. Each citation contains:

```json
{
  "unit_id": "lesson-01",
  "source_id": "lesson-01-transcript",
  "claim_kind": "course_teaching",
  "source_locator": "sources/lesson-01.txt#L12-L16",
  "quote": "Exact retained text from those lines.",
  "target_locator": "chapters/01-basics.md#L20-L26"
}
```

This illustrates fields, not ready-to-pass evidence. Use actual retained files, text and actions. `claim_kind` uses `course_teaching`, `translation`, `ai_explanation`, `ai_supplement`, with matching visible `[Course teaching]`, `[Translation]`, `[AI explanation]`, `[AI supplement]` labels in target ranges.

Every expected unit and output chapter needs mapping. Every source-teaching/translation block needs its own citation. Split distinct claims instead of attaching a generic reference to an entire chapter. AI additions support acquired teaching; they cannot replace missing lessons. Exact source quotations stay in internal evidence; published quotations must remain within the rights boundary.

Each concept's `lecture_evidence` matches a checked citation for its `source_units`. Explanation, reasoning, example, boundaries, quick-check and application fields point to actual local chapter ranges. Source-based visual reconstruction maps to retained visual-channel evidence.

## Review and limits

Preserve a source-comparison report stating the verified teaching points, original examples and reasoning, indispensable diagrams/demonstrations, practice/attachments, omissions, and uncertainties for every unit. Compare claims and worked results with original text/media; inspect high-risk terms and actual visual teaching. Generic repeated QA prose is insufficient even when a script accepts its syntax.

Checks reject missing evidence, declared metadata/AI sources, broken references, changed inputs, absent channels and stale QA. They cannot prove origin authenticity, that a listing includes every live lesson, semantic agreement between captions and audio, or teaching quality. An Agent controlling all files could manufacture a coherent fake bundle. Retain actual acquisition outputs and originals; inspect content. Do not describe script success as a content-level or independent audit. If independent review is separately authorized, give the reviewer originals and rendered artifacts, not merely the author's summary/PASS.

## Existing packs

No grandfathered completion: v4.1 packs need a retained canonical inventory, real content records, source map, acquisition snapshot and fresh pre-review snapshot before v4.2 sealing. Migrate from existing originals, never from old generated chapters. If originals are missing, reacquire lawfully or report the missing-source blocker. Preserve prior QA and failed checks in history.
