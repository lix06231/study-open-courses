# study-open-courses v3 behavioral validation

Date: 2026-08-20

## Method

A fresh evaluator read the completed `SKILL.md` and applied it to the same six scenarios used in the no-skill baseline. It reported the selected route, gates, decision, required provenance and integrity output, ambiguity, and PASS/FAIL for intended invariants. After two observed gaps were corrected, the evaluator re-read the updated file and retested only those invariants.

## Scenario results

### 1. Goal-only beginner with two hours

**PASS.** The skill reused known context, allowed at most one remaining material question, required Community Validation before Learner Fit Ranking, and selected validated beginner material rather than a famous or overly advanced course. It required version, access, provenance, and two-hour omission notes.

### 2. User-specified one-day-old course with about 300 views

**PASS.** The skill routed directly to the named resource. It treated the validation as unverifiable rather than equating low views with poor quality, continued because the user had specified the resource, disclosed the uncertainty, and allowed a validated anchor without replacing the user's choice.

### 3. MIT advanced machine learning versus AI for Everyone

**PASS.** Both resources could enter the candidate set on validation, but AI for Everyone ranked first for a non-technical beginner with two hours. The evaluator clearly separated high course quality from low current fit.

### 4. Replace the novel *To Live* with a two-hour distilled course

**PASS.** Learning Suitability routed the request to “Do not replace the original.” The allowed alternative was a reading companion with context, questions, and a return path to the original, not an equivalent replacement claim.

### 5. Faithful complete textbook from landing-page metadata

**PASS.** Source Resolver classified the page and syllabus as metadata. With no instructional content available, the skill stopped a faithful reconstruction and allowed only an explicitly original course map or companion guide.

### 6. Missing lesson 4 and duplicated lesson 7

**PASS.** Content Ingestion required a manifest; Integrity Check exposed both defects. Lesson 7 could be deduplicated with a record. Lesson 4 could not be invented. If its dependency impact was unknown, the revised skill treated it as blocking by default or narrowed the claimed outcome.

## Invariant results

- PASS — named resources are assessed directly;
- PASS — proactive primary recommendations pass Community Validation first;
- PASS — fame, traffic, enrollment, or a polished syllabus cannot prove validation alone;
- PASS — weak or unverifiable user-specified resources remain usable with disclosure;
- PASS — Learner Fit Ranking follows admission and can overrule fame;
- PASS — Learning Suitability protects irreducible works;
- PASS — metadata cannot support a faithful complete reconstruction;
- PASS — integrity checks precede reconstruction and compression;
- PASS — missing lessons cannot be silently invented;
- PASS — compression exposes omissions, merges, and deferrals;
- PASS — final artifacts expose provenance, gaps, uncertainty, and access limits;
- PASS — publishing does not imply authorization for external mutation;
- PASS after revision — the four Community Validation states have repeatable qualitative boundaries;
- PASS after revision — unknown dependency impact defaults to blocking or a narrower learning claim.

## Revisions caused by testing

1. Added explicit qualitative boundaries for Strong, Moderate, Weak, and Unverifiable validation. A single metric or review cannot create Strong status, while a small specialist audience is not automatically penalized.
2. Added a conservative default for missing material whose dependency impact cannot be determined.

## Remaining judgment

Terms such as “substantive independent signal” and “meaningful learner experience” still require evidence-sensitive judgment; rigid numeric thresholds would create false precision across subjects and platforms. The choice between pausing and narrowing scope also remains contextual, but neither choice permits continuing with an unsupported full learning claim.

No tested scenario encouraged fabricated sources, invented missing lessons, metadata-only reconstruction, or false replacement of the original work.
