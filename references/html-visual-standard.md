# Default Course-Book HTML Visual Standard

Read this reference whenever producing the required single-file HTML edition of a formal reconstructed course.

The canonical visual reference is [course-book-standalone-reference.html](../assets/course-book-standalone-reference.html). Reuse its document architecture, CSS system, responsive behavior, interaction pattern, and print treatment. The reference course's words, facts, titles, source notes, exercises, and metadata are example content only and must be completely replaced with the current course.

## Required visual direction

The HTML should feel like a calm, professionally edited digital course book rather than a generic landing page, Markdown preview, documentation site, dashboard, or collection of separate lesson pages.

Preserve these design characteristics by default:

- warm off-white paper background, dark green-black body text, muted gray-green secondary text, restrained deep-green accent, and warm brown only for secondary provenance states;
- fixed left reading sidebar on desktop, containing the course title, chapter/section links, active-section state, and a chapter search field;
- one centered long-form reading column with generous whitespace and a maximum readable line length;
- a book-like cover with eyebrow, large Chinese serif title, subtitle, version/scope/date metadata, and a quiet bottom rule;
- front matter for edition/use notes and a print-style contents page before the lessons;
- clear chapter boundaries, chapter kickers, serif major headings, sans-serif body copy, disciplined heading hierarchy, and visible reading rhythm;
- distinct components for provenance/source notes, AI supplements/current-context updates, uncertainty warnings, code, tables, figures, exercises, checks, collapsible answers, and an answer appendix when applicable;
- dark code blocks, restrained borders, small radii, and no decorative gradients, glossy cards, excessive shadows, dashboard tiles, or marketing-page calls to action;
- mobile behavior that converts the sidebar into a toggleable drawer without losing navigation or search;
- print CSS for A4, hidden interactive navigation, chapter page breaks, repeated table headers, and avoidance of broken headings, figures, exercises, and source notes.

Default tokens should remain recognizably close to the reference unless the user explicitly requests another visual identity:

```css
--ink: #18201d;
--muted: #64706b;
--paper: #fbfaf6;
--panel: #f0eee6;
--line: #d9ddd6;
--accent: #146c5a;
--accent-soft: #dff1ea;
--warm: #9b5d27;
--sidebar: 18rem;
```

Use a Chinese serif stack for the cover and major section headings—`"Noto Serif CJK SC", "Songti SC", Georgia, serif`—and a readable sans-serif stack for body text—`Inter, "Noto Sans CJK SC", "Microsoft YaHei", system-ui, sans-serif`.

## Required document architecture

The one-file HTML edition must include, when applicable to the course:

1. mobile navigation toggle;
2. fixed/searchable table-of-contents sidebar;
3. book cover;
4. publication/edition metadata;
5. visible contents section;
6. all course chapters in the same HTML document;
7. exercises and learning checks near the relevant lesson;
8. answers or feedback guidance;
9. provenance, integrity limits, and uncertainty states;
10. embedded JavaScript for sidebar toggle, search, and active-section highlighting; and
11. embedded responsive and print CSS.

Do not split chapters into separate HTML pages. Do not link required CSS or JavaScript files. Do not require a framework, CDN, remote font, remote runtime, or asset folder. Small permitted visual assets must be embedded as data assets or inline SVG.

## Content-aware adaptation

Keep the visual grammar stable while adapting labels and components to the subject. A technical course may use more code and warning blocks; a media course may use figures and production checklists; a conceptual course may use more provenance and reflection components. Do not add empty components merely to imitate the reference.

The course title length, number of chapters, and content density may change. Preserve readability rather than forcing the reference's exact measurements when the new content requires a small adjustment. Any adjustment must still read as the same course-book family.

## Visual acceptance gate

Before completion, inspect the rendered HTML at desktop and mobile widths and in print preview or PDF rendering. The HTML fails visual acceptance when any of these occur:

- it resembles raw Markdown with minimal CSS;
- it is a generic landing page, dashboard, or card grid rather than a readable course book;
- the sidebar is missing, non-searchable, unusable, or covers content;
- chapters are split across multiple HTML files;
- the cover, edition metadata, contents, exercises/checks, or source/limitation treatment are missing when applicable;
- typography, line length, spacing, contrast, tables, code, or mobile layout materially reduce readability;
- required assets or interactions fail offline; or
- print output clips content, loses chapter structure, or displays navigation controls.

If visual acceptance fails, revise the HTML. Do not call the HTML edition complete merely because it opens in a browser or contains all text.
