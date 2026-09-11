# Course Discovery and Recommendation

Use this reference when the learner has not chosen a course, asks for recommendations, wants a learning path, or is unsure which course in a large catalog fits them.

## Contents

- Search current primary sources
- Apply hard eligibility gates before scoring
- Build the candidate set
- Judge fit, not prestige
- Recommend decisively
- Move from recommendation to learning

Do not use this workflow merely because a course URL or name is present. If the learner has already chosen that course and asks to process or learn it, skip recommendation discovery and process it directly. If they ask whether that chosen course is suitable, evaluate it first and search alternatives only if comparison is requested or the learner opts into alternatives after a material mismatch is explained.

## Search newest editions first

When internet search is available, search current official university, instructor, and open-course pages and explicitly look for the **newest substantive edition/version** of each serious course. Course catalogs change, so verify the actual course page rather than relying on remembered availability or an old roundup.

Resolve freshness before comparing delivery convenience:

1. Identify candidate editions from newest to oldest using course/instructor/institution evidence.
2. Distinguish the course edition/release date from the webpage, playlist, or reupload date. A 2026 upload of a 2023 lecture is still 2023 teaching.
3. For each edition in newest-first order, verify identity, completeness, free access, provenance, and inspectable core teaching.
4. Select the newest edition that passes the hard gates. Fall back to an older edition only when the newer one is incomplete, inaccessible under the learner's constraints, untrustworthy in provenance, lacks usable teaching evidence, or the learner explicitly requests the older edition.
5. Record why an older edition was chosen when a newer one was found.

Do not prefer an older version merely because it has cleaner subtitles, a familiar URL, higher view counts, or easier tooling. When a new edition is a supplement rather than a replacement, preserve that distinction instead of treating it as a full newer course.

Search across multiple credible providers when useful instead of treating one catalog as the universe. Prefer primary course sources for syllabus, prerequisites, materials, dates, access, and licensing. Use third-party reviews or discussions only as secondary evidence about teaching experience, never as the sole basis for availability or course facts.

If current search is unavailable, say that availability could not be verified and avoid presenting remembered course details as current facts.

For Chinese-speaking learners or a China-oriented workflow, add **Bilibili** to the routine course-source and **version** check. Search both the original course/instructor name and common Chinese names, including plausible current-year/version terms when useful. Use it to discover newer accessible editions as well as alternate deliveries, and to cross-check whether a course that is inconvenient on an overseas platform has a legitimate public delivery elsewhere. Still use official course/instructor sources where possible to establish identity, syllabus, actual teaching date/version, and provenance.

Do not assume a Bilibili upload is authorized because it is public or complete. Prefer instructor, university, publisher, or authorized-channel uploads. When a third-party upload has unclear provenance or an explicit no-authorization/repost warning, do not treat it as rights-cleared for download or redistribution; keep searching for a legitimate source or tell the learner what could not be verified.

## Apply hard eligibility gates before scoring

For default recommendations, **free, actually accessible, and complete enough to learn are eligibility requirements, not low-weight preferences**. Classify each serious candidate before scoring it:

### Access state

- **Free / no login:** the core teaching content can be consumed without payment or authentication.
- **Free / login required:** no payment is required for the core content, but authentication is needed to reach it. Keep the candidate eligible, label the login requirement prominently, and prefer an equally good no-login source when available.
- **Paid / subscription:** payment is required to consume the core teaching content. Exclude by default unless the learner explicitly allows paid courses or already has access.
- **Unknown:** the landing page or search result does not prove what happens after enrollment/login. Do not call it free until verified.

Treat phrases such as `enroll for free`, `free trial`, `audit available`, a zero-price registration button, or a publicly visible course outline as **insufficient evidence** that the complete learning content is free. Check the actual lecture/content access path when possible.

### Completeness state

- **Complete:** the accessible source covers the coherent course sequence closely enough to learn the stated course, with the core lectures/teaching material present.
- **Partial:** only some weeks, clips, samples, or units are accessible.
- **Metadata only:** only a syllabus, description, lecture titles, snippets, or catalog metadata is visible.

Default recommendations should be **Complete**. Verify a playlist against the official or credible course structure when possible; do not infer completeness merely from a title containing `full course` or `全集`.

### Freshness state

Classify the selected edition as **latest verified**, **latest eligible**, **older fallback**, or **version unknown**. Freshness is a selection order, not an excuse to weaken the access/completeness/evidence requirements.

- **Latest verified:** newest substantive edition found and it passes all gates.
- **Latest eligible:** a newer edition exists but cannot satisfy the learner's stated access/rights/completeness constraints; this is the newest one that can.
- **Older fallback:** use only with an explicit reason, such as the learner requesting it or a newer edition lacking core teaching evidence.
- **Version unknown:** do not silently imply currency; surface the uncertainty and keep searching when it matters.

How much course age matters is domain-specific. Still search newest-first in every subject, but judge the learning risk of age by the subject: a newer software, regulation, clinical-guidance, current-data, or fast-moving technology course may materially supersede an older one, while a strong older calculus, classical mechanics, history, literature, art, or foundational theory course may remain pedagogically sound. This affects warnings and fallback judgment, not the obligation to check whether a newer edition exists.

If no candidate passes both gates, say that no verified free complete course was found. Ask before broadening the search to paid courses; do not quietly recommend a paywalled course because it has higher prestige.

## Build the candidate set

For each serious candidate, collect enough evidence to answer:

- What does the course actually teach?
- What learner level and prerequisites does it assume?
- Is it a coherent full course or only a collection of clips/materials?
- Are lectures, transcript/captions, notes/slides, assignments, solutions, projects, or readings available?
- How much work is likely required?
- What language and accessibility friction exists?
- How current is the course, and does freshness matter for this subject?
- Can the learner legally access and use the materials for the intended private-study workflow?
- What is the verified access state: free/no-login, free/login-required, paid/subscription, or unknown?
- What is the verified completeness state: complete, partial, or metadata-only?
- Can the agent reach actual lecture-level content needed for later summarization, rather than only the course outline?
- What verifiable **course-specific** evidence suggests recognition, trust, or influence: long-running editions, substantial learner adoption, use in other curricula, course awards, sustained instructor/institution support, respected public evaluations, or another meaningful signal?

Discard courses whose prerequisites clearly exceed the learner unless they are being considered as a later target in a learning path.

Before scoring, create a compact candidate fit card:

| Field | Required judgment |
|---|---|
| Capability coverage | Which primary and supporting capabilities from the learner-fit brief are taught, and what source proves it |
| Missing capability | What important learner need is absent or only weakly covered |
| Starting-point fit | Which demonstrated learner evidence supports the difficulty judgment |
| Prerequisite gap | Blocking, repairable inside the plan, already demonstrated, or unknown |
| Workload fit | Credible workload compared with the learner's actual duration and focused hours |
| Constraint fit | Access, login, cost, language, device, format, and other hard constraints |
| Teaching-evidence readiness | Whether actual content can later support a source-grounded pack |
| Main tradeoff | The most important reason to choose or reject it for this learner |

Do not award high fit from a course title, institution name, or generic description. If the source does not prove a field, mark it unknown. If an unknown could reverse the recommendation, investigate it or lower confidence rather than inventing certainty.

## Judge fit, not prestige

Use these dimensions as a reasoning rubric rather than fake precision:

| Dimension | Default weight | High-fit signal |
|---|---:|---|
| Goal match | 25 | Directly builds the knowledge or capability the learner wants |
| Level/prerequisite fit | 20 | Challenging but realistically learnable now |
| Teaching/course coherence | 15 | Clear sequence and a complete course rather than disconnected resources |
| Material completeness | 15 | Strong combination of lectures, text/notes, exercises or supporting resources |
| Course recognition/influence | 10 | Verifiable course-level evidence of sustained use, adoption, reputation, or impact |
| Accessibility/language fit | 5 | The learner can access it and AI can reasonably bridge language friction |
| Freshness relevance | 5 | Newest eligible edition checked; age risk appropriate to the subject |
| Time/format fit | 5 | Fits the learner's weekly time and preferred way of learning |

Adjust weights when the goal demands it. For fast-moving AI tooling, software frameworks, regulation, or other rapidly changing fields, raise freshness. For calculus, classical mechanics, foundational algorithms, or other stable fundamentals, do not penalize an excellent older course merely for age.

Every score or comparative judgment must trace back to the learner-fit brief and candidate evidence. Use the following anchors:

- **Goal match:** high only when the course directly covers most primary capabilities, not merely the same broad subject.
- **Level/prerequisite fit:** high only when demonstrated learner evidence and verified course prerequisites align; self-label alone is weak evidence.
- **Time/format fit:** compare real workload and delivery format with the learner's actual constraints, not an ideal schedule.
- **Unknown evidence:** do not give full credit. State the uncertainty and decide whether it warrants more research, a trial unit, or a different candidate.

Treat recognition as a confidence signal, not a prestige contest. Prefer course-specific evidence over the fame of the institution or instructor. Do not equate a famous university, famous professor, high raw view count, or catalog placement with course quality. When two courses fit similarly, prefer the one with stronger verified recognition and a longer trustworthy teaching track record.

Apply the eligibility gates before this rubric. Do not let recognition, prestige, or an otherwise high score rescue a course whose core content is paid, incomplete, or unverified when the learner asked for free study. Among similarly fitting eligible courses, prefer free/no-login over free/login-required to reduce friction.

Do not invent social proof. If course-level recognition could not be verified, say so. A less famous course can still be the best recommendation when its fit, teaching, materials, accessibility, or freshness is materially better. For fast-moving AI/software topics, do not let historical influence override serious obsolescence.

## Recommend decisively

Usually return no more than three choices:

1. **Best next course:** the one the learner should start now.
2. **Alternative:** a meaningful different tradeoff, such as more practical, more theoretical, shorter, or gentler.
3. **Stretch/next-step course:** only when useful; explain what must be learned first.

For each choice give:

- the direct official link;
- **why it fits this learner**;
- **why this course is worth trusting**, with concrete recognition/influence evidence when verified;
- prerequisite risk and expected workload/format when evidence exists;
- material completeness and freshness;
- verified access state, including whether login is required;
- verified delivery/source used for the actual lectures, including a Bilibili link when that is the best legitimate China-friendly delivery;
- the most important tradeoff or limitation.

Also name the learner capability the course does **not** solve. When a small supplement can close the gap, propose the smallest supplement; when the missing capability is central, do not call the course the best fit.

Make the recommendation reason evidence-based rather than writing generic praise such as `famous university`, `classic course`, or `widely recognized` without support.

If one course is clearly best, say so. Do not force three recommendations just to fill a list.

If no single course fits, build the shortest prerequisite path instead of recommending a course the learner is not ready for. A path can combine courses from different institutions when that produces a better progression.

## Move from recommendation to learning

After recommending, make the next action concrete. Map the full course, then build the first self-contained study sprint sized to the learner's actual study window; do not cap the first batch at one official chapter if the learner has time for more. If the user explicitly asked the agent to choose for them, choose the best-fit option and proceed within the user's authorized scope rather than asking for redundant confirmation.

If learner-profile confidence is medium, make the recommendation provisional and use a coherent 60-90 minute trial unit or bounded first module to test level, pace, and teaching mode. If confidence is low, resolve the highest-impact uncertainty before producing a long pack.

Before beginning the study pack, verify that the agent can actually inspect the teaching content for the selected units. If the platform is free but login-gated, ask the learner to log in before continuing. If only the syllabus is accessible, do not silently switch to a syllabus-based synthetic course; resolve another legitimate delivery source, obtain captions/transcript/media through a permitted path, or state the blocker.

Persist only stable, useful learning-profile information when memory/files are available: subject goal, demonstrated level/prerequisites, time budget, language preference, learning-mode preference, and completed/current courses. Keep temporary search results separate from the learner profile.
