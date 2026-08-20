# Multi-format publishing design

## Problem

The v3 skill defines the content of a final learning artifact but does not define file formats. A complete-course request can therefore comply with the skill while returning Markdown only.

## Approved behavior

- A formal, complete course defaults to three downloadable files: Markdown (`.md`), self-contained HTML (`.html`), and PDF (`.pdf`).
- Markdown is the canonical content master. HTML and PDF are derived from the same approved content and must not silently diverge.
- A quick preview, outline, recommendation, interim checkpoint, or explicit single-format request may use only the format appropriate to that request.
- If the environment cannot create or verify HTML or PDF, report the blocked format and the exact remaining work. Do not silently downgrade a requested complete-course delivery to Markdown only.
- External upload remains separately authorized; creating local downloadable files is part of preparing the learning artifact.

## Format requirements

### Markdown

Preserve heading hierarchy, links, source notes, exercises, tables, and omission notes. Use portable relative links for companion files when possible.

### HTML

Produce a self-contained reading edition with semantic headings, a navigable table of contents, readable responsive typography, print styles, accessible link text, and no required remote runtime dependency.

### PDF

Produce a stable offline/print edition. Use embedded or reliably available Chinese fonts, preserve headings and source links, avoid clipped text and broken tables, and prevent headings from being stranded at page bottoms when practical.

## Verification

- All three files exist and are non-empty.
- Titles, unit order, exercises, source/provenance notes, integrity gaps, and compression notes agree across formats.
- HTML opens as a complete document and its internal navigation works.
- PDF page count is non-zero; text is extractable; Chinese glyphs render; representative pages are visually inspected for clipping, blank pages, broken tables, and bad page breaks.
- Final response links all generated files using absolute local paths.

## Scope

This update changes the publishing contract and README only. It does not add a universal content-export system or promise that every recommendation/intermediate response produces three files.
