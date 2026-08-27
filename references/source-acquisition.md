# Source Acquisition, Multimodal Verification, Integrity, and Provenance

Read this reference whenever a named or identifiable learning resource's real content must be assessed, acquired, reconstructed, compressed, translated, or published. Read `SKILL.md` and `references/execution-state.md` first. This reference is host-neutral: inspect the capabilities actually available in the current host, and name an unavailable capability rather than assuming a particular browser, downloader, media model, OCR engine, or speech service exists. The resource does not need to have become the primary recommendation first.

The objective is to acquire a lawful, trustworthy **complete source set** sufficient for the claimed learning outcome, then show exactly which speech, visual, and companion material supports it. When the user requests whole-resource integrity assessment or a formally complete artifact, the expected scope defaults to every canonical lesson, page, appendix, exercise, visual teaching element, and companion item relevant to that resource. Narrow that scope only because of a real blocker, disclose the excluded range and learning impact, and obtain the user's acceptance before calling the result formally complete.

## Access classification and non-overridable paid boundary

Classify each identified resource and each distinct source edition before any instructional-content access. The classification from `SKILL.md` controls all work here.

| `access_class` | `processing_eligibility` | Acquisition handling in this reference |
|---|---|---|
| `free_access` | `eligible` | Acquire and process the real instructional content only within platform, copyright, and authorization rules. A free account login is allowed only when it confers no paid entitlement. |
| `paid_or_entitlement_gated` | `report_only` | Record public metadata only. Do not open gated lessons, use paid login state, download, capture, record, transcribe, ASR, OCR, extract, translate, compress, or reconstruct gated instructional content. Continue looking for free-access alternatives. |
| `public_excerpt` | `eligible_limited` | Treat the public portion as a limited source. Process only its actual public items and ranges; do not infer the paid remainder, combine it into a paid-course reconstruction, or call it complete for that paid resource. |
| `official_free_edition` | `eligible_as_separate_source` | Treat it as a separate resource with its own version, expected scope, manifest, integrity result, validation, and provenance. Do not assume it matches a paid edition. |
| `unknown` | `blocked_pending_classification` | Do not ingest instructional content. Resolve access status through public metadata or continue discovery. |

`report_only` is a Skill rule, not an estimate of legal rights. Purchase, subscription, institutional access, a trial, a logged-in browser, explicit user authorization, personal-use intent, lack of DRM, a deadline, or technical feasibility never change paid or entitlement-gated content to `eligible`. A paid resource may be named only as a clearly separate manual-study option based on public metadata, with payment disclosed and no implication that gated lessons were inspected.

## Autonomous acquisition contract

The user does not need to supply transcripts, downloads, notes, or files before work can begin. Autonomous acquisition of a resource's full declared scope begins **only after** the Free-Access Processing Gate records `processing_eligibility: eligible`. For `eligible_limited`, acquire only the declared public excerpt scope. For `eligible_as_separate_source`, first resolve the free edition as a separate resource, then acquire only that edition's declared scope. Neither case authorizes access to a paid remainder. `report_only` and `blocked_pending_classification` never enter content acquisition.

When the resource is identifiable:

1. resolve the exact edition, version, playlist, episode set, or document collection;
2. identify canonical expected items, order, languages, and required speech, visual, exercise, code, data, and attachment channels;
3. inspect the host for relevant browsing, document extraction, caption, media, frame or slide inspection, OCR, speech-to-text, translation, and file-access capabilities;
4. acquire the complete permitted source set described below, not merely one convenient text stream;
5. verify coverage, transcription, visual interpretation, translation, and extraction quality;
6. ask the user only when a real blocker remains.

Do not ask the user to download, copy, transcribe, or OCR material that the host can lawfully access and process. Do not call missing user-provided material a blocker until the permitted acquisition paths have been checked.

This contract does not grant new permissions. Never bypass logins, payment, DRM, regional restrictions, technical access controls, platform terms, copyright limits, or the paid-resource boundary. Never ask the user to paste a password, session token, cookie, or other reusable credential. If a **free-access** source needs a user-controlled free login and the host supports it, ask the user to sign in there and confirm when access is ready.

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

## Complete source set

Build a source set around the expected teaching channels. The best source for spoken words does not replace other channels:

| Teaching channel | Required acquisition decision |
|---|---|
| Speech | Use native text, official transcript, official captions, platform captions, or permitted ASR in that order of preference. Preserve lesson and timestamp boundaries. |
| Visual teaching | Independently locate and inspect required slides, frames, whiteboards, code shown on screen, diagrams, charts, demonstrations, and layout-dependent material. |
| Practice and attachments | Independently collect permitted exercises, prompts, datasets, code repositories, handouts, reading lists, and other companion files required by the stated outcome. |
| Cross-channel mapping | Map the speech, visual, and attachment records to the same lesson or source locator; record absent channels and their impact rather than assuming text coverage is complete. |

For the speech channel, use the highest-quality permitted option that covers the needed spoken material:

1. native source text or official transcript;
2. official captions or subtitles;
3. platform-provided captions or subtitles;
4. official notes, slides, exercises, code, or companion documents, as a complementary channel rather than a replacement for missing speech or visual material;
5. lawfully accessible audio or video processed with speech-to-text;
6. scans or images processed with OCR when no reliable text layer exists.

Do not transcribe media merely because it is possible when a complete official transcript is available. Prefer primary text over ASR output because it normally preserves names, terminology, equations, and structure more reliably.

Use supporting sources to repair terminology or context, not to silently replace missing primary instructional content. An accessible transcript or caption set completes only the speech channel; it does not prove slides, visual demonstrations, exercises, code, or attachments were acquired.

## Speech and ASR processing

For permitted media, first check for native text, official transcripts, official captions, and platform captions. Use ASR only when a better complete speech source is unavailable and the media itself is eligible for processing. When audio or video is the best available speech source:

1. check for official and platform captions first;
2. if captions are absent or unusable, inspect the host for lawful media access and speech-to-text capability;
3. when both are available and the source is eligible, obtain or stream the media through the permitted mechanism and transcribe it;
4. keep segment, episode, or lesson boundaries in the transcript;
5. retain timestamps when the tool provides them and they help verification;
6. preserve speaker labels only when they are known or reliably inferred;
7. mark inaudible or low-confidence passages instead of inventing text.

Verify every ASR or caption-based lesson against the original permitted media or another authoritative source:

1. confirm the lesson boundary and inspect samples from its opening, middle, and ending;
2. inspect every low-confidence, inaudible, overlapping, abrupt, repeated, or discontinuous segment;
3. compare transcript duration and timestamp coverage with the source duration, and investigate unexplained gaps, overlaps, or extra material;
4. verify high-impact names, terminology, numbers, units, formulas, commands, URLs, code, and version identifiers against primary material, slides, code, or official documentation; and
5. record processed coverage separately from verified coverage, including the verification method and unresolved uncertainty.

Do not treat an ASR confidence score as verification. When a required speech segment cannot be verified, classify its learning impact in Integrity Check; do not silently repair it from guesswork. If the host lacks a required capability, state which capability is missing and what exact permitted input would unblock the work. Do not reduce a complete-course claim to metadata or an outline.

## Visual-channel processing

For every video, screen recording, slide presentation, scan, or image-based lesson, perform visual-reference detection to determine whether visual material carries teaching meaning. Look for spoken visual references (for example, “this diagram,” “as shown”), slide or scene changes, demonstrations, code execution, diagrams, tables, equations, on-screen instructions, and layout-dependent explanations. A video with no spoken visual reference may still contain essential visual teaching.

For each required visual element:

1. record the lesson and exact timestamp, frame range, page, slide, or file locator;
2. inspect the relevant frame, slide, diagram, code, table, demonstration, or image directly when the host can do so;
3. use OCR for text embedded in visual material when appropriate, but retain the original visual locator and do not treat OCR as a substitute for diagrams, layout, color, motion, or demonstration behavior;
4. map the visual evidence to its associated speech, exercise, or attachment record; and
5. record `visual_coverage` as expected, acquired, processed, and verified visual references or ranges, with any unresolved item and its impact.

Inspect all visual-only or visually decisive teaching, plus any visual item with low-confidence OCR, dense layout, tables, formulas, diagrams, code, boundary transitions, or an ASR reference to it. If a required visual explanation, demonstration, diagram, code state, or attachment cannot be inspected well enough to support the outcome, classify it as **Blocking** unless the declared scope is narrowed and the learner accepts the impact. Do not claim a text-only reconstruction covers teaching that remains visually unresolved.

## Scanned and image-based text

When a PDF, slide deck, or image has no reliable text layer:

1. inspect for an alternate accessible or native-text edition;
2. use OCR only when the source is eligible and OCR is available;
3. verify that an alternate edition matches the required edition, order, visual material, and non-text content before substituting it;
4. OCR every page or slide required by the claimed learning outcome and record expected versus processed page and visual coverage;
5. keep page or slide boundaries;
6. verify headings, lists, tables, formulas, names, and page order;
7. flag diagrams or layout-dependent meaning that OCR did not capture.

If only part of the required page range can be processed or checked, classify the gap through Integrity Check and narrow the learning outcome unless the unprocessed pages are demonstrably non-blocking.

When page images can be inspected, visually compare every high-risk page—tables, formulas, diagrams, dense layouts, low-confidence OCR, and boundary pages—against the extracted text, plus a representative sample of ordinary text pages. Record which pages were processed, which were visually verified, the verification method or sample, and which pages remain unverified. Processing coverage is not verification coverage.

Text extraction is ingestion, not reconstruction. Do not smooth over recognition errors until the source record preserves what was uncertain.

## Translation verification

Translate only eligible instructional content. Record the source language, target language, translation method, and source locators for each translated item. Translation is an interpretation layer, not new evidence and not a replacement for the original source record.

Before using a translation in reconstruction:

1. identify the language of the source segment and confirm that translated duration, item boundaries, and coverage match the source;
2. maintain a bilingual glossary for important terms, names, abbreviations, product names, and domain-specific phrases, and apply it consistently;
3. verify names, numbers, units, formulas, code, commands, URLs, and quoted labels against the original rather than translating or normalizing them blindly;
4. retain the original wording beside or in the source map when a term, idiom, ambiguity, or technical expression is uncertain;
5. distinguish translated source material from the Agent's new teaching explanation, examples, or synthesis; and
6. record translation uncertainty, its affected locators, and its learning impact in the manifest, provenance map, and final artifact.

Do not hide a translation uncertainty by making prose smoother. If an unresolved translation changes a required concept or instruction, treat it as blocking or narrow the scope.

## Source manifest

Maintain one item record for every expected lesson, chapter, episode, page range, visual component, exercise, attachment, or other required component of an eligible declared scope. Keep `report_only` resources as public-metadata notes only; do not create or populate records from gated instructional content. The manifest and run ledger must agree.

| Field | Meaning |
|---|---|
| `item_id` | Stable lesson, chapter, episode, or document identifier. |
| `title` | Source title, preserving canonical wording when known. |
| `type` | Text, transcript, caption, audio, video, scan, slide, diagram, demonstration, exercise, code, attachment, or other relevant type. |
| `source` | Canonical URL or local identifier. |
| `version_date` | Edition, version, release date, or `unknown`. |
| `access_class` | Access classification from `SKILL.md`, retained with the item or its source set. |
| `processing_eligibility` | Gate result controlling whether and how the item may be processed. |
| `expected_order` | Canonical position in the resource. |
| `expected_coverage` | Speech, visual, practice, or attachment coverage the item should contain. |
| `acquired_coverage` | What was actually obtained. |
| `method` | Native text, captions, ASR, OCR, visual inspection, translation, or another permitted method. |
| `source_locator` | Lesson, chapter, timestamp, frame range, file-page index, printed page number, slide number, repository path, or range needed to locate the material precisely. |
| `processed_coverage` | Pages, slides, frames, segments, time ranges, or attachments processed by extraction, ASR, OCR, inspection, or translation. |
| `verified_coverage` | Pages, slides, segments, or time ranges checked against the original, including the method or sampling note. |
| `visual_coverage` | Expected, acquired, processed, and verified visual references or ranges, plus unresolved visual teaching. |
| `reconstructed_coverage` | Verified coverage represented in the learner-ready artifact; it never substitutes for acquired, processed, or verified coverage. |
| `item_status` | Current state such as pending, acquired, processed, verified, deferred, failed, blocked, or reconstructed. |
| `attempt_count` | Number of acquisition or processing attempts for the item. |
| `last_error` | Latest concrete failure, access limit, or `none` when no error occurred. |
| `blocking_impact` | `blocking`, `non-blocking`, or pending classification, with the affected outcome or dependency. |
| `next_action` | Smallest permitted next step, including retry, alternate source, visual inspection, scope decision, or no action. |
| `quality_notes` | Gaps, confidence concerns, translation uncertainty, access limits, substitutions, and provenance notes. |

Keep acquisition notes outside the reconstructed lesson text. Failed and deferred records remain in the ledger; never delete them to make coverage rollups appear complete.

## Integrity Check

Run this gate before Learning Reconstruction. Verify:

- access classification and processing eligibility for every source set;
- expected items versus acquired items across speech, visual, practice, and attachment channels;
- canonical sequence, lesson boundaries, and source-to-channel mapping;
- missing, truncated, duplicated, visually unresolved, or conflicting-version material;
- alternate versions and conflicts;
- transcript timing, language, speaker boundaries, discontinuities, and duration/coverage mismatches;
- ASR errors in names, technical terms, numbers, formulas, commands, and code;
- OCR errors in headings, tables, lists, formulas, code, page order, and visual layout;
- translation language, glossary consistency, high-impact terms, source-to-target coverage, and visible uncertainty;
- processed coverage versus visually or otherwise verified coverage;
- exercises, examples, diagrams, files, and attachments that plain text omits;
- prerequisite gaps that affect later units.

Use primary titles, slides, glossaries, official documentation, or repeated context to correct high-impact ASR, OCR, or translation terms. Keep uncertain corrections labeled and preserve the original locator.

Classify every material gap:

- **Blocking:** prevents a defensible lesson sequence or claimed outcome. Pause, acquire a better source, or narrow the scope.
- **Non-blocking:** the supported learning outcome still holds. Continue only if the gap is disclosed in the final artifact.

Never silently invent a missing lesson, visual explanation, exercise, attachment, or translation. When dependency impact cannot be determined, treat the gap as blocking or narrow the outcome to material that does not depend on it.

## Evidence and provenance

Maintain a source map throughout the work:

- source title, creator, URL or local identifier, access class, and processing eligibility;
- edition, version, publication date, and access date when relevant;
- acquired speech, visual, practice, and attachment components; methods; coverage; and known gaps;
- final unit or section mapped back to precise source locators such as lesson IDs, timestamps, frame ranges, page/slide ranges, or attachment locators;
- source and target language, glossary terms, translation method, and unresolved translation uncertainty;
- source-derived claims separated from translation, explanation, synthesis, or new examples;
- uncertainty, conflicts, corrections, and substitutions.

For PDFs or slide decks, retain both file-page indices and printed page numbers when they differ. When an alternate edition is used, record the page or section alignment to the named edition rather than assuming identical pagination.

Use primary sources for course facts and current rules when possible. Community evidence supports validation and learner experience; it is not a substitute for instructional content.

## Copyright and redistribution

Processing eligibility is not redistribution permission. Use only content that is eligible under `SKILL.md` and lawfully accessible for the requested learning task.

Do not deliver a raw or near-complete copyrighted transcript, subtitle file, OCR dump, translated transcript, or reconstructed substitute when redistribution rights are absent or unclear. If the user requests redistribution and claims the necessary rights, ask for a clear confirmation of that authority when it is not already established; do not attempt to make a legal determination from weak evidence. Use acquired eligible content internally as needed to create original explanations, limited quotations where permitted, exercises, provenance notes, and a learning structure. When the original experience is essential, produce an assisted-learning companion instead of a substitute. These rules never permit processing paid or entitlement-gated instructional content.

## Completion and blocker report

Proceed to reconstruction only when the manifest, ledger, and integrity result support the stated learning outcome. Follow `references/execution-state.md` for coverage rollups and formal completion names.

If blocked, report:

1. the exact resource and component affected;
2. its access class, processing eligibility, and what permitted work was attempted;
3. the access, permission, source, visual, translation, quality, or capability blocker;
4. why it is blocking rather than merely inconvenient;
5. the smallest permitted next action or narrower deliverable.

For `report_only`, the correct result is a paid-resource boundary report based on public metadata, an optional manual-study note with payment disclosed, and continued discovery of free-access alternatives—not a request for login, purchase, authorization, or a copy of the gated lesson.
