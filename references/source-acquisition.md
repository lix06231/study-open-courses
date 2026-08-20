# Source Acquisition, Transcription, Integrity, and Provenance

Read this reference whenever a named or identifiable learning resource's real content must be assessed, acquired, reconstructed, compressed, or published. The resource does not need to have become the primary recommendation first.

The objective is to acquire enough lawful, trustworthy instructional material to support the claimed learning outcome and to show exactly where that material came from. When the user requests whole-resource integrity assessment or a formally complete artifact, the expected scope defaults to every canonical lesson, page, appendix, exercise, and companion item relevant to that resource. Narrow that scope only because of a real blocker, disclose the excluded range and learning impact, and obtain the user's acceptance before calling the result formally complete.

## Autonomous acquisition contract

The user does not need to supply transcripts, downloads, notes, or files before work can begin.

When the resource is identifiable:

1. resolve the exact edition, version, playlist, episode set, or document collection;
2. inspect the host agent for relevant browsing, document extraction, caption, media, OCR, and speech-to-text capabilities;
3. acquire the best lawful source available using the priority below;
4. verify coverage and transcription or extraction quality;
5. ask the user only when a real blocker remains.

Do not ask the user to download, copy, transcribe, or OCR material that the host can lawfully access and process within the user's authorization. Do not call missing user-provided material a blocker until the available acquisition paths have been checked.

This contract does not grant new permissions. Never bypass logins, payment, DRM, regional restrictions, technical access controls, platform terms, or copyright limits. Never ask the user to paste a password, session token, cookie, or other reusable credential. If the host supports user-controlled authentication, ask the user to sign in there and confirm when access is ready.

## Source Resolver

Resolve the actual content, not just its marketing page. Confirm when relevant:

- canonical title and creator;
- edition, release, version, or publication date;
- expected lesson, chapter, episode, or document count;
- canonical order and grouping;
- official page and actual content locations;
- languages and available translations;
- registration, payment, login, region, and access restrictions;
- exercises, slides, diagrams, datasets, code, or companion materials.

A catalog entry, landing page, syllabus, table of contents, search snippet, review, or creator announcement is metadata. It can establish identity or expected scope, but it cannot support a faithful full reconstruction by itself.

Prefer the newest version when the subject changes quickly. Prefer a stable, complete edition when freshness does not materially affect the learning outcome.

## Content Ingestion priority

Use the highest-quality lawful option that covers the needed material:

1. native source text or official transcript;
2. official captions or subtitles;
3. platform-provided captions or subtitles;
4. official notes, slides, exercises, code, or companion documents;
5. lawfully accessible audio or video processed with speech-to-text;
6. scans or images processed with OCR when no reliable text layer exists.

Do not transcribe media merely because it is possible when a complete official transcript is available. Prefer primary text over ASR output because it normally preserves names, terminology, equations, and structure more reliably.

Use supporting sources to repair terminology or context, not to silently replace missing primary instructional content.

## Media-only resources

When audio or video is the best available source:

1. check for official and platform captions first;
2. if captions are absent or unusable, inspect the host for lawful media access and speech-to-text capability;
3. when both are available and authorized, obtain or stream the media through the permitted mechanism and transcribe it;
4. keep segment, episode, or lesson boundaries in the transcript;
5. retain timestamps when the tool provides them and they help verification;
6. preserve speaker labels only when they are known or reliably inferred;
7. mark inaudible or low-confidence passages instead of inventing text.

If the host lacks a required capability, state which capability is missing and what exact input would unblock the work. Do not reduce a complete-course claim to metadata or an outline.

## Scanned and image-based text

When a PDF, slide deck, or image has no reliable text layer:

1. inspect for an alternate accessible or native-text edition;
2. use OCR when available and permitted;
3. verify that an alternate edition matches the required edition, order, and non-text content before substituting it;
4. OCR every page or slide required by the claimed learning outcome and record expected versus processed page coverage;
5. keep page or slide boundaries;
6. verify headings, lists, tables, formulas, names, and page order;
7. flag diagrams or layout-dependent meaning that OCR did not capture.

If only part of the required page range can be processed or checked, classify the gap through Integrity Check and narrow the learning outcome unless the unprocessed pages are demonstrably non-blocking.

When page images can be inspected, visually compare every high-risk page—tables, formulas, diagrams, dense layouts, low-confidence OCR, and boundary pages—against the extracted text, plus a representative sample of ordinary text pages. Record which pages were processed, which were visually verified, the verification method or sample, and which pages remain unverified. Processing coverage is not verification coverage.

Text extraction is ingestion, not reconstruction. Do not smooth over recognition errors until the source record preserves what was uncertain.

## Source manifest

Maintain one row or record per expected item:

| Field | Meaning |
|---|---|
| `item_id` | Stable lesson, chapter, episode, or document identifier. |
| `title` | Source title, preserving canonical wording when known. |
| `type` | Text, transcript, caption, audio, video, scan, slide, exercise, code, or other relevant type. |
| `source` | Canonical URL or local identifier. |
| `version_date` | Edition, version, release date, or `unknown`. |
| `expected_order` | Canonical position in the resource. |
| `expected_coverage` | What the item should contain. |
| `acquired_coverage` | What was actually obtained. |
| `method` | Native text, captions, ASR, OCR, or another acquisition method. |
| `source_locator` | Lesson, chapter, timestamp, file-page index, printed page number, slide number, or range needed to locate the material precisely. |
| `processed_coverage` | Pages, slides, segments, or time ranges processed by extraction, ASR, or OCR. |
| `verified_coverage` | Pages, slides, segments, or time ranges checked against the original, including the method or sampling note. |
| `quality_notes` | Gaps, confidence concerns, access limits, or substitutions. |

Keep acquisition notes outside the reconstructed lesson text.

## Integrity Check

Run this gate before Learning Reconstruction. Verify:

- expected items versus acquired items;
- canonical sequence and lesson boundaries;
- missing, truncated, or duplicated material;
- alternate versions and conflicts;
- transcript timing, language, speaker boundaries, and discontinuities;
- ASR errors in names, technical terms, numbers, formulas, and code;
- OCR errors in headings, tables, lists, formulas, and page order;
- processed coverage versus visually or otherwise verified coverage;
- exercises, examples, diagrams, files, and attachments that plain text omits;
- prerequisite gaps that affect later units.

Use primary titles, slides, glossaries, official documentation, or repeated context to correct high-impact ASR/OCR terms. Keep uncertain corrections labeled.

Classify every material gap:

- **Blocking:** prevents a defensible lesson sequence or claimed outcome. Pause, acquire a better source, or narrow the scope.
- **Non-blocking:** the supported learning outcome still holds. Continue only if the gap is disclosed in the final artifact.

Never silently invent a missing lesson. When dependency impact cannot be determined, treat the gap as blocking or narrow the outcome to material that does not depend on it.

## Evidence and provenance

Maintain a source map throughout the work:

- source title, creator, URL or local identifier;
- edition, version, publication date, and access date when relevant;
- acquired components, acquisition method, and known gaps;
- final unit or section mapped back to precise source locators such as lesson IDs, timestamps, or page/slide ranges;
- source-derived claims separated from explanation, synthesis, or new examples;
- uncertainty, conflicts, corrections, and substitutions.

For PDFs or slide decks, retain both file-page indices and printed page numbers when they differ. When an alternate edition is used, record the page or section alignment to the named edition rather than assuming identical pagination.

Use primary sources for course facts and current rules when possible. Community evidence supports validation and learner experience; it is not a substitute for instructional content.

## Copyright and redistribution

Acquisition permission is not redistribution permission. Use only content the user and host can lawfully access for the requested learning task.

Do not deliver a raw or near-complete copyrighted transcript, subtitle file, OCR dump, or reconstructed substitute when redistribution rights are absent or unclear. If the user requests redistribution and claims the necessary rights, ask for a clear confirmation of that authority when it is not already established; do not attempt to make a legal determination from weak evidence. Use the acquired content internally as needed to create original explanations, limited quotations where permitted, exercises, provenance notes, and a learning structure. When the original experience is essential, produce an assisted-learning companion instead of a substitute.

## Completion and blocker report

Proceed to reconstruction only when the manifest and integrity result support the stated learning outcome.

If blocked, report:

1. the exact resource and component affected;
2. what was attempted;
3. the access, permission, source, or capability blocker;
4. why it is blocking rather than merely inconvenient;
5. the smallest user action or narrower deliverable that would unblock progress.
