# Default Self-Contained Study Sprint

Use this structure when the user asks to study, process, summarize, or learn from a course without specifying a narrower format. The default product is a complete batch for the learner's current study window—normally one week—not merely notes about one lecture or a source-defined chapter.

## Contents

- Evidence gate before generation
- Scope and completeness
- Sprint plan and unit card
- Learning outcomes, prerequisites, and main teaching text
- Visual/math/code reconstruction and terminology
- Temporal calibration and provenance separation
- Tutor notes, practice, checkpoints, and review
- Sprint-end synthesis
- Sources, provenance, and quality bar

## Evidence gate before generation

Do not begin the full study pack until the teaching content for the planned units is actually inspectable. Use a syllabus/module list to map coverage, but use **lecture-level content evidence** to summarize what was taught: actual lecture text, transcript/captions, permitted ASR, direct audio/video understanding, or an equivalent detailed instructor-authored teaching source.

A course landing page, outline, module titles, search snippets, or a few public samples cannot support claims about what the instructor explained in inaccessible videos. If only those are available, either resolve a legitimate source containing the actual lectures, ask the learner to complete a required free login, process a legitimately obtained file supplied by the learner, or stop and label the limitation. Do not fill the gap from general model knowledge and present it as a course summary.

Before synthesis, maintain a small **evidence ledger** for every unit in the planned scope: unit identity, source URL/file, access state, content evidence obtained, visual/supporting material, and ready/blocked status. Do not call the pack complete while a planned unit is blocked or was never inspected. If access fails partway through a course, name the affected units and resolve access rather than silently shrinking the pack.

When the learner explicitly asks to summarize the course videos or lectures, inspect the spoken teaching itself through captions/transcript, permitted ASR, or direct media understanding for every covered video. Even detailed lecture notes are supporting evidence in that mode, not a substitute for the requested video content. Outline-only notes never satisfy this requirement.

## Scope and completeness

Size the sprint from the learner outward:

1. Determine the target study window, normally one week unless the learner specifies another deadline or period.
2. Determine usable study hours and intensity from the learner profile. Distinguish steady weekly learning from a concentrated sprint.
3. Estimate real learning time for each candidate course span, including reading/explanation, examples, exercises or projects, prerequisite repair, and review—not only lecture/video runtime.
4. Before selecting a partial span, estimate the **entire remaining course** in real learning time. If it fits within the current study window, select the whole remaining course as required core and generate all of it in this task. Separate chapter files may improve navigation, but they are not separate weekly generation rounds.
5. If the entire remaining course is just over the required capacity but fits within the normal pre-generated stretch range (roughly up to 120%), still generate the whole remaining course. Keep only the within-budget portion in the required schedule and mark the excess **optional stretch / prepared material**.
6. If the whole remaining course does not fit, select the largest coherent consecutive span that reasonably uses the available study time.
7. Map that span back onto the official course structure. It may contain part of one chapter, one complete chapter, or multiple chapters.
8. Before finalizing a cutoff inside a chapter, inspect the remaining children of that chapter. If only the final one or two consecutive subunits/sections would remain, generate them as well so the learner receives the complete chapter. Mark the portion beyond the time budget as **prepared overflow / closure material**, not required core work.

If hours are unknown, infer a capacity from the learner's stated intensity, course difficulty, published workload, and remaining course length and state the assumption. Treat words such as concentrated, crash, intensive, library week, exam prep, or equivalent as evidence against a light default workload.

Do not use media duration as the sole whole-course-fit test. Incorporate known readings, assignments, practice, prerequisite repair, and review, using credible published workload guidance when available. If those components are not known, state a conservative assumption. If the learner explicitly requested only selected chapters, lectures, or topics, honor that narrower scope instead of expanding to the full course.

When the whole-course completion override fires, treat the deliverable as one **whole-course sprint**. Use the learner's spare capacity for cumulative review, a capstone/project, prerequisite repair, or simply finishing early; do not create artificial later weeks to pad the plan.

Prefer natural concept boundaries near the time target. Split a long chapter only when necessary, using names such as `chapter-03a-neural-networks-foundations.md`. Avoid leaving a tiny tail: when only the last one or two coherent subunits would be stranded, finish generating the whole chapter even if that pushes prepared material beyond the normal weekly target or stretch allowance. Keep the excess available for later instead of deleting or compressing it. Never reduce scope silently just to make generation easier.

When files are available, maintain:

- a course index listing all official or inferred units and completion status;
- a sprint/week index stating time assumptions, target outcomes, covered units, and total estimated study time;
- one or more separate learning-unit files for every chapter/part covered by that sprint.

When the learner asks for one week of material, all files listed for that week are part of the requested deliverable. Generate them in the same task when possible rather than stopping after the first chapter.

## 1. Sprint plan

Start with:

- a compact learner-fit statement: desired action outcome, demonstrated starting point, profile confidence, and consequential assumptions;
- the primary capabilities this sprint serves and the observable evidence that will show progress;
- study window and assumed available hours;
- why this amount of course content fits that window;
- chapters/parts covered, distinguishing **required core**, **prepared overflow/closure**, and **optional stretch**;
- estimated hours for explanation/reading, practice, project work, and review;
- a suggested day-by-day sequence that leaves some flexibility for difficult topics;
- a clearly marked optional stretch unit, generated in advance, for a learner who moves faster than expected.

Do not pretend the estimate is precise. It is a planning forecast that should be adjusted after the learner's actual pace is known. Prefer roughly 80-90% core work plus buffer/review and enough optional stretch material to support roughly 100-120% of the estimated capacity, unless the course ends first.

## 2. Unit card

Include when known:

- course, chapter/module, and covered lecture titles;
- institution and instructor;
- original language;
- substantive course edition/release date when known, separate from upload date;
- source link/files;
- materials used: transcript, captions, slides, notes, readings, ASR;
- access state and any login requirement;
- evidence coverage: which covered units were grounded in actual lecture-level content versus supporting notes/slides;
- license/attribution note when relevant;
- estimated study time for this unit and its share of the sprint;
- what comes before and after this chapter.

## 3. Learning outcomes and map

State what the learner should understand or be able to do by the end. Then give a compact concept map showing the dependency order for the chapter. Explain why the chapter matters in the broader course.

## 4. Prerequisites

List only prerequisite concepts that are genuinely needed. Distinguish prerequisites stated or implied by the course from AI-suggested refreshers. Provide a short refresher for prerequisites likely to block this learner instead of merely telling them to go look them up.

## 5. Main teaching text

This is the largest section. Teach the chapter in clear, connected prose using the best course sources as evidence, while writing explanations independently rather than producing an exhaustive paraphrase of the transcript. Organize by concept dependency when that teaches better than transcript order.

For each major concept include as applicable:

- an intuitive first explanation;
- precise definition or rule when present;
- why the idea exists and what problem it solves;
- a step-by-step deeper explanation;
- equations, code, algorithms, diagrams, or procedures from the strongest source, with explanation of each important part;
- worked examples or reconstructed examples that make the idea usable;
- the instructor's important examples or demonstrations when they are essential to understanding, summarized or adapted within the applicable rights boundary;
- connections to earlier and later concepts;
- a short "check yourself" prompt after substantial sections;
- traceability: timestamp, page/slide, section, or source link when available.

Do not force the learner to reopen the source merely to understand an ordinary concept. If the source assumes background or explains something too tersely, fill the instructional gap with original **AI explanation**. Use **AI supplement** for useful knowledge that goes beyond the course's actual scope. These labels distinguish provenance; they should not make the prose fragmented.

## 6. Visual, mathematical, and code reconstruction

When meaning depends on slides, boards, diagrams, equations, demos, or code, reconstruct the necessary logic in the chapter. Describe diagrams textually when they cannot be embedded. Explain mathematical derivations step by step at the learner's level. For code, explain the role of important lines and include a runnable or simplified example when useful.

Never infer missing visual content from speech alone. When an essential diagram, board derivation, chart, demonstration, or on-screen workflow is available in the lecture video but not in text/slides, inspect the relevant frame(s) with vision/OCR and reconstruct the teaching logic. Treat a generated note such as `see the original video for this figure` as an unresolved item unless access/rights/tooling truly prevent inspection; if blocked, state the limitation explicitly.

## 7. Temporal calibration and provenance separation

Keep three kinds of content distinct whenever they are relevant:

1. **Course teaching:** what the instructor taught in this course edition.
2. **AI explanation/supplement:** learner-oriented explanation or useful context added by the tutor.
3. **Current-context update:** later external facts needed because the original claim may now be stale or materially misleading.

Do not overwrite an older course claim with a present-day claim and make it look as though the instructor said it. Preserve the original teaching in its historical/version context, then add a current update only when needed.

Determine time sensitivity from the subject rather than from a fixed AI-course template. Examples of moving content include software/API behavior, laws and regulations, medical or safety guidance, product capabilities, standards, prices, market/data statistics, and changing scientific consensus. Stable mathematics, established theory, historical source interpretation, classical techniques, or other durable content normally needs no current-update box.

When a current update is included, verify it with suitable current evidence and state the update date. Prefer a compact pattern such as `Course teaching -> What changed -> What to retain` only for concepts where that separation helps learning.

## 8. Terminology

For cross-language learning, provide a compact bilingual glossary. On first use of a technical term in the notes, retain its source-language form, for example: "梯度下降（gradient descent）".

Do not translate established technical terms into misleading literal language merely for fluency.

## 9. Common traps, confusions, and AI tutor notes

Flag:

- similar concepts that are easy to confuse;
- assumptions the instructor relies on;
- suspicious ASR segments;
- source conflicts;
- questions that require the next lecture or external reading.

Add learner-specific advice where useful: what deserves slow reading, what can be skimmed, a recommended mental model, and which prerequisite to revisit if a concept does not click.

Learner-specific advice must follow an explicit adaptation rationale. Personalization should change relevant scope, depth, sequence, practice, feedback, language support, or delivery—not only swap a generic example for the learner's profession or hobby.

## 10. Practice and worked solutions

Create enough practice to cover the chapter's main learning outcomes. Mix:

- recall;
- explain-in-your-own-words;
- application;
- comparison;
- derivation, debugging, calculation, or code when appropriate;
- at least one synthesis question for substantial chapters.
- transfer tasks that apply the concept to a new example or the learner's own context when appropriate;
- error-detection or critique prompts when misconceptions are likely;
- cumulative retrieval from earlier units when the sprint spans multiple units.

Provide answers or worked solutions after the questions or in a collapsible/separate section when the output medium supports it. Explain why an answer is correct rather than giving only the final result.

## 11. Unit checkpoint

End the teaching portion with a short mastery checklist: "you are ready to continue if you can...". Identify the two or three ideas most likely to cause trouble in the next chapter.

## 12. Five-minute unit review

Give the smallest useful revision view: key ideas, must-remember terms/formulas/code patterns, and connections to the broader course. This review is intentionally brief because it follows the full teaching chapter; it must not replace it. Treat compressed slogans and one-line takeaways as high-risk: check that they do not become more absolute, causal, certain, or general than the instructor's evidence supports.

## 13. Sprint-end synthesis

After the final unit in the sprint, include:

- a cumulative concept map linking this week's units;
- a mixed retrieval test across the whole sprint;
- a short list of concepts that deserve another pass;
- a next-step recommendation based on whether the learner mastered, struggled with, or finished the planned scope early.

If the learner finishes significantly faster or slower than estimated, update the next sprint's capacity instead of reusing the original estimate blindly.

When the learner profile was medium- or low-confidence, also record what the sprint demonstrated about level, prerequisite gaps, preferred format, and transfer. Use this evidence to confirm, revise, or replace the provisional course plan.

## 14. Sources and provenance

List the course materials actually used. Keep timestamps/pages/slide numbers when available. If outside material or AI knowledge materially expanded the chapter, distinguish it from course-derived claims. Note missing course materials that could affect completeness.

## Final consistency pass

When the pack contains multiple files, reconcile the chapter files, glossary, concept index, course index, sprint plan, quizzes, and short reviews before delivery. Check repeated definitions, terminology, dates, formulas, named frameworks, source mappings, and compressed takeaways against the strongest evidence ledger entry. Fix accidental contradictions; label legitimate differences in instructor usage or historical/current context rather than flattening them.

When file creation is available and the learner wants a durable course pack, do not deliver only Markdown by default. Provide an editable document, a reading-friendly PDF when appropriate, and a ZIP for a multi-file pack while preserving source Markdown.

## Quality bar

- Every unit in the sprint should be usable as the learner's primary study document for its assigned scope; the original course remains an optional source for instructor presentation, demonstrations, or verification rather than a routine prerequisite for understanding.
- Every major source topic assigned to the sprint must appear, or be explicitly listed as missing/excluded.
- Every unit presented as a summary of the instructor's teaching must have lecture-level content evidence. Metadata-only access cannot satisfy a full study-pack request.
- Preserve conceptual depth. Do not collapse multi-step reasoning into conclusions merely to save tokens.
- Prefer independent teaching prose, worked examples, and checks for understanding over exhaustive transcript paraphrase.
- Keep the structure subject-agnostic. Use equations and derivations where the subject requires them, visual demonstrations where those carry the teaching, primary texts where interpretation depends on wording, procedural drills where skill performance matters, and current-context updates only where facts genuinely move.
- Do not let a memorable one-line summary strengthen the source claim beyond its evidence.
- Multi-file artifacts must agree on shared definitions, terminology, factual claims, and source mappings unless a deliberate course-vs-current or source-vs-source distinction is explicitly explained.
- Size output by the learner's available study time rather than by the number of official chapters. Chapter boundaries organize knowledge; they do not cap the sprint.
- Never split the remaining course into multiple calendar batches when its estimated real learning workload fits the current study window. If it fits only by using the normal optional stretch allowance, generate it all but keep the over-budget portion explicitly optional.
- Do not leave only the final one or two coherent subunits of an otherwise covered chapter ungenerated. Complete that chapter and preserve any over-budget tail as prepared overflow.
- When the planned sprint spans multiple files, completing only the first file does not satisfy the request.
- Use open-license material according to its license. When reuse rights are unclear or restrictive, achieve self-contained learning through original exposition rather than substantial copying of protected expression.
- A personalized pack must trace its major design choices to learner evidence. Occupational name-swaps alone do not meet this bar.
- Do not call the output a transcript, reproduction, or official textbook. "Study sprint", "weekly course pack", "learning module", or "AI-enhanced course notes" are good defaults.
