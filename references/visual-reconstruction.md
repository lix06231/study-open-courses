# Visual Reconstruction

Use this workflow whenever slides, video frames, boards, interfaces, charts, diagrams, objects, movement, spatial relationships, formulas, code, or other visuals carry teaching information.

## Visual inventory

Inspect the transcript for visual references such as `this chart`, `as shown`, `on the screen`, `this line`, `here`, `the blue box`, or equivalent. Cross-check slides/notes and sample frames instead of relying only on those phrases. Record every teaching-relevant visual in `evidence/visual-ledger.csv` with:

`visual_id,source_unit,locator,visual_type,teaching_role,action,rights_basis,asset_path,caption,status`

Allowed `action` values:

- `EXTRACT`: retain a necessary permitted source frame or source image.
- `REBUILD_EXACT`: recreate a precise chart, table, formula, board derivation, code listing, map, or interface annotation from verified source data.
- `REDRAW_CONCEPT`: create an original diagram that teaches the same underlying relationship without copying protected expression.
- `AI_ILLUSTRATE`: create a non-factual analogy or decorative teaching illustration.
- `TEXT_ONLY`: no image is needed because the visual adds no teaching information; explain why in `teaching_role` or `caption`.
- `BLOCKED`: the visual is necessary but cannot be legally or technically inspected or reconstructed.

Only `READY` rows count as resolved. A `BLOCKED` necessary visual prevents the pack from being called complete.

## Decision table

| Visual type | Preferred action | Accuracy rule |
|---|---|---|
| Concept relationship, process, taxonomy | `REDRAW_CONCEPT` | Preserve the relationships; use SVG, HTML/CSS, Mermaid, or another editable exact format. |
| Data chart, coordinate plot, precise table | `EXTRACT` or `REBUILD_EXACT` | Use the original data/labels. Never ask an image generator to invent the chart. |
| Formula, proof, code, derivation | `REBUILD_EXACT` | Re-typeset or reproduce in text/code and explain each important step. |
| Software/UI demonstration | `EXTRACT` with annotations, or `REBUILD_EXACT` when practical | Preserve labels, order, state, and controls. Use multiple frames when state changes matter. |
| Board work or handwriting | source key frame plus a clean `REBUILD_EXACT` version when permitted | Do not discard intermediate derivation steps. |
| Physical technique, movement, experiment | a permitted key-frame sequence or original schematic | Preserve timing, position, safety, and causal order. |
| Decorative photograph or analogy | `AI_ILLUSTRATE` or omit | Clearly treat it as an aid, never as documentary evidence. |
| Lecturer talking head with no teaching information | `TEXT_ONLY` | Omit by default. |

## Source priority

Prefer in order:

1. official course slide/figure with suitable reuse terms;
2. a necessary permitted video key frame;
3. exact reconstruction from verified data, formula, code, or interface state;
4. original conceptual redraw;
5. AI-generated analogy or decorative illustration.

Use AI image generation only for the fifth category. It must not carry exact numbers, text, formulae, UI state, historical evidence, scientific observations, or other facts that require precision.

## Rights and attribution

Record the source and reuse basis for every extracted source visual. Public viewing does not itself grant redistribution. For a private learner pack made from user-supplied or legitimately accessed material, minimize copied frames to what teaching requires. For a shareable/public pack, prefer original redraws and inspect the source license before retaining screenshots or figures.

Do not remove watermarks or attribution. Add a caption that distinguishes `source image/frame`, `exact reconstruction`, `conceptual redraw`, and `AI illustration`.

## Page integration

Every included visual needs:

- a figure number and descriptive caption;
- nearby explanation of what the learner should notice;
- accessible alt text;
- readable labels at phone and print size;
- a source locator or `AI-created` label;
- no essential meaning communicated by color alone.

Do not create a gallery detached from the teaching. Place each visual beside the concept, step, question, or worked example it supports.

## Static overflow check

Before delivery, verify every SVG fits its own `viewBox`/`rect` by a browser-side `getBBox()` pass rather than eyeballing. Details and the key `text-anchor` pitfall (a naive bbox-vs-rect comparison false-positives on `middle`/`end`-anchored labels) are in `references/build-and-pdf-pitfalls.md` §4.
