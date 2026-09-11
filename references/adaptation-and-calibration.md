# Adaptive Teaching and Calibration

Use this reference when turning a chosen course into learner-specific materials or when profile confidence is not high. Personalization must alter the learning design, not merely insert the learner's job, hobby, or name into examples.

## Contents

- Create an adaptation plan
- Change teaching by demonstrated level and outcome
- Use trial mode under uncertainty
- Calibrate from learning evidence

## Create an adaptation plan

Before drafting a substantial pack, decide how the learner profile changes at least the relevant parts of the design:

| Design lever | Possible change |
|---|---|
| Selection | Choose a different course, prerequisite bridge, or mixed path |
| Scope | Include prerequisite repair, skip mastered basics, or narrow to target capabilities |
| Sequence | Reorder optional material around dependencies and the learner's bottleneck without misrepresenting official course order |
| Explanation depth | Add intuition and scaffolding, or preserve advanced terminology and compress basics |
| Practice | Use retrieval, worked problems, projects, performance drills, critique, or transfer tasks suited to the outcome |
| Feedback | Add checkpoints that reveal the next decision rather than generic reflection prompts |
| Format | Adjust language support, chunk size, transcript use, visual aids, files, or accessibility |

Record a compact rationale for consequential changes. A course pack is not meaningfully personalized if the only change is replacing a generic example with the learner's occupation.

## Adapt by demonstrated level

Use demonstrated evidence rather than self-rating alone.

### Early-stage learner

- Repair blocking prerequisites inside the unit when feasible.
- Introduce one new abstraction at a time.
- Lead with intuition and concrete examples before formal detail.
- Include worked examples and frequent low-stakes checks.
- Reduce optional breadth before reducing the explanation needed for core understanding.

### Developing learner

- Compress already-demonstrated basics.
- Emphasize comparison, transfer, error diagnosis, and independent practice.
- Connect concepts to the learner's authentic use context.
- Make assistance gradually less explicit across exercises.

### Advanced learner

- Preserve original terminology, nuance, assumptions, disputes, and source distinctions.
- Emphasize synthesis, critique, edge cases, open questions, and realistic projects.
- Avoid padding with elementary definitions unless a specific prerequisite gap appears.

Do not assign one global level when capabilities are uneven. A learner may be advanced in subject judgment but new to programming, or fluent in written expression but weak in spontaneous speaking. Adapt per capability.

## Adapt by desired outcome

| Outcome | Default evidence of learning |
|---|---|
| Understand/explain | Retrieval, concept maps, explain-in-own-words, compare/contrast |
| Perform a skill | Repeated authentic performance, feedback, correction, and decreasing support |
| Build/create | A staged project with artifacts and explicit quality criteria |
| Pass an exam | Coverage map, representative questions, timed retrieval, error log |
| Make decisions at work | Cases, tradeoffs, source evaluation, decision memo or operating checklist |
| Explore for interest | Coherent narrative, optional depth branches, lighter compulsory drills |

Make at least one core assessment resemble the learner's intended real-world use. Do not use quizzes as the only evidence for a performance or project goal.

## Use trial mode when confidence is medium or low

A trial unit is not a teaser. Make it a coherent 60-90 minute learning experience that tests assumptions while providing real value.

Include:

- one representative concept or subskill;
- the proposed explanation style and practice format;
- one authentic transfer task;
- a short checkpoint that can distinguish `too easy`, `productive`, and `too hard`;
- the exact assumptions the trial is testing.

If the user explicitly requests a large deliverable immediately, proceed with a clearly labeled provisional first sprint rather than refusing. Keep the first boundary revisable and avoid generating a long multi-week pack from low-confidence assumptions.

## Calibrate from evidence

After a trial or sprint, collect the smallest useful feedback:

- actual completion time versus estimate;
- performance or correctness on the checkpoint;
- where the learner needed help or lost interest;
- whether the format was usable;
- whether the learner transferred the idea to a new task.

Update the learner card with demonstrated evidence. Then decide whether to:

- continue unchanged;
- add prerequisite repair;
- increase or reduce depth;
- change practice mode;
- adjust future study capacity;
- switch course or supplement a missing capability.

Do not interpret `I liked it` as mastery or `it was hard` as failure. Prefer observable performance and actual time. Keep original expectations and new evidence separate so later agents can understand why the plan changed.

## Deliver durable study packs

When file creation is available and the learner asks for a durable course pack, do not deliver only Markdown unless they explicitly request it.

- For a formal reconstructed course, follow the three-primary-file contract in `SKILL.md` and `references/publishing-spec.md`: one complete Markdown, one single-file self-contained HTML, and one complete PDF.
- Provide an editable document such as DOCX for ordinary app use only when the learner requests it.
- When several files belong together, provide a ZIP containing the shareable versions and source Markdown only as an optional extra; it never replaces the three primary files.
- Keep filenames and internal headings consistent across formats.
- Include only learning-relevant profile information. For a pack intended to be shared, omit private context that is not necessary to use the material and use neutral learner descriptions where possible.

If the environment cannot create these formats, provide the best available artifact and state the limitation plainly.
