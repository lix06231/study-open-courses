# Textbook Mode

Use textbook mode by default when a learner asks to study, learn, process, or summarize a course and does not explicitly request a brief recap. The objective is not to reproduce the lecturer's expression. It is to reconstruct the course as an original, self-contained teaching artifact grounded in the course evidence, so a learner with little time for video can still gain most of the course's usable knowledge.

## Product boundary

Call the result an AI-enhanced course book, learning module, or textbook-style study pack. Do not call it an official textbook, transcript, reproduction, or guaranteed replacement for the course.

The original course may remain valuable for lecturer presence, performance, live demonstrations, or verification. It must not be a routine prerequisite for understanding an ordinary concept in the generated artifact.

## Teaching-unit pattern

For every major concept, argument, method, procedure, or skill, include the elements that materially apply:

1. **Problem and purpose:** what question this section solves and why the learner needs it.
2. **Course teaching:** the instructor's claim, method, or explanation, traced to lecture-level evidence.
3. **Reasoning or procedure:** the intermediate logic, derivation, causal chain, decision steps, or performance sequence. Never collapse a multi-step explanation into a slogan.
4. **Important source example:** preserve or independently restate examples and demonstrations needed for comprehension.
5. **Independent explanation:** add intuition, prerequisite repair, analogy, or another route to understanding, labeled `AI explanation`.
6. **Boundary and misconception:** state when the idea does not apply, what it does not prove, and what learners commonly confuse.
7. **Visual:** embed or reconstruct any figure, interface, diagram, formula, board work, movement, object, or comparison that carries teaching value.
8. **Immediate check:** ask one brief question that exposes whether the learner understood this section.
9. **Application or transfer:** require the learner to use the idea in a new example, decision, calculation, performance, critique, or project.
10. **Evidence locator:** cite the source unit plus timestamp, page, slide, section, or file locator when available.

Do not force all ten items into repetitive headings. Write connected teaching prose, but make the coverage auditable.

## Concept coverage ledger

Create `evidence/concept-coverage.csv` before final synthesis. Use one row per major teachable concept and these columns:

`concept_id,chapter,concept,source_units,lecture_evidence,explanation,reasoning,example,boundaries,visual,quick_check,application,status`

Use file/section anchors in the coverage fields, not only `yes`. Use `NOT_NEEDED: reason` only when an element genuinely does not apply. Set `status` to `READY` only when:

- the concept is grounded in actual teaching content;
- necessary reasoning or procedural steps are preserved;
- at least one useful example is present;
- limitations or likely confusion are handled;
- the visual decision is resolved;
- an immediate check and an application/transfer task exist.

If any major concept is not READY, the whole artifact is not complete. Do not hide the gap by removing the concept from the ledger.

## Depth and compression

Do not target a fixed word count. Increase detail only when it increases comprehension, transfer, or source coverage. Avoid transcript-like repetition, generic motivation, and duplicated summaries.

Use these as compression alarms, not automatic padding targets:

- for a nontechnical concept course, estimated main-text reading time below roughly half the source video runtime deserves review;
- a multi-step source explanation represented only by a bullet or one sentence deserves review;
- a source demonstration, counterexample, comparison, or visual omitted from the teaching artifact deserves review;
- a claimed study time much longer than the text, activities, and project actually support deserves correction.

Estimate reading time from the final teaching text, not the transcript. Estimate practice time from the actual questions, calculations, exercises, projects, and review. Video rewatching may be optional but must not be used to inflate the artifact's core learning time.

## Practice density

Provide at least one immediate check and one application/transfer task for every major learning objective. Substantial chapters should also include:

- one error-detection or misconception task;
- one synthesis task connecting multiple concepts;
- worked answers that explain the reasoning;
- cumulative retrieval from earlier chapters.

Do not let quizzes exist only in a promised directory. Ensure every file named in the course index or manifest exists.

## Provenance labels

Keep these layers distinguishable without making the page visually noisy:

- `Course teaching`: grounded summary of what the instructor taught.
- `AI explanation`: a clearer or alternate explanation of the same idea.
- `AI supplement`: useful knowledge beyond the source course.
- `Current-context update`: verified later information that prevents a stale course claim from misleading the learner.
- `Uncertain`: unresolved transcription, visual, numerical, or source conflict.

Do not label general model knowledge as course teaching. Do not strengthen possibility into certainty, exposure into job loss, correlation into causation, or a bounded example into a universal claim.

## Completion rule

Textbook mode fails completion if any of these are true:

- only a syllabus, outline, title list, or landing page supported the teaching prose;
- a normal concept requires `watch the original video`, `see the original image`, or equivalent to be understood;
- a planned chapter, quiz, visual, or exercise file is missing;
- Markdown is the only reading deliverable when HTML/PDF creation is available;
- concept coverage rows are missing or not READY;
- generated study-time claims disagree across the manifest, plan, and final artifact.
