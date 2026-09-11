# Learner Modeling and Micro-Diagnostics

Use this reference for course discovery, course suitability evaluation, or a personalized study pack when the agent does not already have reliable evidence about the learner. Do not turn it into a long intake form. Gather only information that can change course choice, scope, teaching depth, practice, or delivery.

## Contents

- Build an evidence-aware learner card
- Convert vague goals into target capabilities
- Use a micro-diagnostic when self-report is insufficient
- Set profile confidence and choose the next action

## Build the learner card

Before ranking courses, create a compact internal learner card. Show the learner only the assumptions or gaps that matter to the decision.

| Field | Required interpretation |
|---|---|
| Action outcome | A concrete thing the learner wants to understand, produce, perform, pass, or decide |
| Use context | Work, school, exam, project, creative practice, hobby, or another real setting |
| Current evidence | What the learner has studied, built, explained, solved, or performed—not only a label such as `beginner` |
| Prerequisites | Subject knowledge, math, language, tools, physical technique, or other dependencies |
| Study capacity | Duration/deadline, realistic focused hours, and steady versus concentrated learning |
| Constraints | Free/paid, login, language, geography/network, device, accessibility, certificate, or source restrictions |
| Learning mode | Video, reading, projects, drills, discussion, mixed mode, or unknown |

For every field, mark its evidence status:

- **Confirmed:** directly stated or demonstrated by the learner.
- **Inferred:** supported by conversation or work samples; state consequential assumptions.
- **Unknown:** not established. Do not silently invent it.

Do not ask for demographic or personal information that does not affect learning fit. Reuse relevant conversation, memory, or course-workspace evidence and let the newest learner statement override older information.

## Ask only decision-changing questions

Use at most three short questions in the first round. Prioritize:

1. the action outcome and real use context;
2. current evidence or a small work sample;
3. duration and realistic focused hours.

Ask a second round only when a missing constraint can plausibly change the recommended course. If the learner asks the agent to decide, make a reasonable provisional assumption and label it instead of blocking.

When selectable choices would help, useful planning presets are light (3-5 focused hours/week), regular (6-10), intensive (12-20), and short sprint (20+). Always allow a different schedule, and ask duration/deadline separately when it is not implied.

Avoid broad questions such as `What is your level?` when a concrete prompt is possible. Prefer `What is the hardest thing you can currently do without help?` or `Show a recent attempt.`

## Convert the goal into a capability map

Do not search directly from a vague wish such as `learn AI`, `improve expression`, or `study economics`. Translate it into:

`desired real-world result -> required capabilities -> prerequisite capabilities -> observable success evidence`

Create a short map with:

- **Primary capabilities:** necessary for the learner's stated result now.
- **Supporting capabilities:** helpful but not the main bottleneck.
- **Out of scope:** adjacent abilities that sound relevant but do not serve the current result.
- **Success evidence:** a task, explanation, performance, project, test result, or decision that would show improvement.

Example: `speak better on short-form video` may require rapid structure, concise explanation, spontaneous recovery, audience adaptation, and camera delivery. Traditional recitation, debate, or broadcast diction may be supporting or out of scope depending on the learner's actual sample.

Do not confuse a subject label with a capability map. Use the map to form search queries and to judge course coverage later.

## Decide whether a micro-diagnostic is needed

Use a micro-diagnostic when all are true:

- course level or teaching approach materially depends on current ability;
- current evidence is absent, contradictory, or only a vague self-rating;
- a diagnostic can be completed in roughly 3-10 minutes without specialized setup.

Skip it when the learner has supplied a reliable recent artifact, a verified prerequisite result, or a concrete demonstrated history sufficient for the decision. Also skip it when the learner explicitly wants a general overview and personalization would not materially change the output.

Do not let diagnostics become an exam before learning starts. Use the smallest authentic task that reveals the likely bottleneck.

Match the diagnostic modality to the intended performance. Do not use polished writing to infer spontaneous speaking, multiple-choice recall to infer practical execution, or a tutorial-following task to infer independent creation. If the intended modality is still unknown, clarify it before requesting a sample.

| Course type | Useful diagnostic |
|---|---|
| Speaking, writing, language | A 60-120 second response, short writing sample, rewrite, or comprehension task in the intended use context |
| Math, coding, science | Two or three progressive problems or one small authentic task that tests prerequisites and transfer |
| Knowledge/humanities | Explain a foundational idea, interpret a short source, or compare two claims in the learner's own words |
| Creative/practical skill | A recent artifact, portfolio sample, process description, or minimum performance task |
| Tool/workflow course | Complete one representative operation and explain where assistance was needed |

Assess only dimensions relevant to course fit. Separate observations from interpretations. For example: `states the conclusion after 70 seconds` is an observation; `likely needs rapid structure practice` is an interpretation.

Never diagnose disability, illness, intelligence, or personality from a learning sample.

If the learner declines a diagnostic, proceed with a provisional assumption and trial mode when safe; do not present the inferred level as established fact.

## Set profile confidence

Use three operational levels rather than fake numerical precision:

- **High confidence:** action outcome, use context, demonstrated starting point, constraints, and study capacity are sufficiently established.
- **Medium confidence:** the goal and capacity are clear, but level, preference, or one important constraint remains inferred.
- **Low confidence:** the goal is broad, current ability is unknown, or major constraints could reverse the recommendation.

Then choose the next action:

| Confidence | Default action |
|---|---|
| High | Recommend/select the course and build the requested study scope |
| Medium | Make a provisional recommendation and begin with a 60-90 minute trial unit or first bounded module; state what it will test |
| Low | Run a micro-diagnostic or clarify the single highest-impact gap before committing to a long course pack |

An explicit learner request to process a named course still takes priority. In that case, do not block source processing merely because the profile is incomplete; gather only what is needed to size and adapt the requested material, and label provisional teaching assumptions.

## Learner-fit brief

Before course ranking or substantial study-pack generation, be able to state internally:

1. the learner's desired action outcome;
2. the primary capabilities and success evidence;
3. demonstrated starting point and prerequisite risks;
4. study capacity and hard constraints;
5. confirmed versus inferred facts;
6. profile confidence and whether trial mode is needed.

If these cannot be stated, do not claim that a recommendation is personalized.
