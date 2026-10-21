#!/usr/bin/env python3
"""Fail-closed checks for retained instructional evidence, scope and provenance.

Hashes and excerpts establish consistency, not authenticity or teaching quality.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

ACCESS_PAIRS = {
    "free_access": "eligible",
    "public_excerpt": "eligible_limited",
    "official_free_edition": "eligible_as_separate_source",
}
CONTENT_KINDS = {"lecture_text", "transcript", "captions", "asr", "slides", "exercise", "code", "attachment"}
ACQUISITION_METHODS = {"native_text", "official_captions", "platform_captions", "asr", "ocr", "user_file"}
CHANNELS = {"primary", "visual", "practice", "attachment"}
CORE_CHECKS = {"objective_traceability", "source_accuracy", "labeled_synthesis", "compression_integrity", "visible_limitations"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_path(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or re.match(r"^[a-z]+://", relative, re.I):
        raise ValueError(f"a retained local path is required: {relative!r}")
    path = (root / relative).resolve()
    path.relative_to(root.resolve())
    if not path.is_file():
        raise ValueError(f"missing local evidence: {relative}")
    return path


def load(root: Path, relative: str) -> dict:
    obj = json.loads(local_path(root, relative).read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError(f"{relative}: expected a JSON object")
    return obj


def excerpt(root: Path, locator: str) -> str:
    """Use explicit inclusive line ranges; URLs and unchecked fragments never pass."""
    match = re.fullmatch(r"(.+)#L([1-9][0-9]*)(?:-L?([1-9][0-9]*))?", locator or "")
    if not match:
        raise ValueError(f"exact local #Lstart-Lend locator required: {locator!r}")
    path = local_path(root, match[1])
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    start, end = int(match[2]), int(match[3] or match[2])
    if end < start or end > len(lines):
        raise ValueError(f"line range is outside retained evidence: {locator}")
    value = "\n".join(lines[start - 1:end]).strip()
    if not value:
        raise ValueError(f"empty evidence range: {locator}")
    return value


def rows(root: Path, relative: str) -> list[dict]:
    with local_path(root, relative).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def text(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def line_bounds(locator: str) -> tuple[int, int]:
    match = re.fullmatch(r".+#L([1-9][0-9]*)(?:-L?([1-9][0-9]*))?", locator)
    if not match:
        raise ValueError("explicit local line bounds required")
    return int(match[1]), int(match[2] or match[1])


def caption_seconds(value: str) -> float:
    parts = value.replace(",", ".").split(":")
    return sum(float(part) * (60 ** index) for index, part in enumerate(reversed(parts)))


def unique(records: list[dict], key: str, label: str) -> dict:
    if not isinstance(records, list) or not records or any(not isinstance(r, dict) for r in records):
        raise ValueError(f"{label}: non-empty object list required")
    result = {r.get(key): r for r in records}
    if any(not text(k) for k in result) or len(result) != len(records):
        raise ValueError(f"{label}: duplicate or blank {key}")
    return result


def _validate(root: Path, manifest: dict, *, reconstruction: bool) -> None:
    if not re.fullmatch(r"[A-Za-z0-9_-][A-Za-z0-9_.-]*", manifest.get("output_basename", "course-book")):
        raise ValueError("output_basename must be a filename without path separators")
    run = load(root, manifest.get("run_ledger", "run-ledger.json"))
    sources = load(root, manifest.get("source_manifest", "evidence/source-manifest.json"))
    if sources.get("schema_version") != 1:
        raise ValueError("source-manifest: unsupported schema_version")
    resource = run.get("resource", {})
    if ACCESS_PAIRS.get(resource.get("access_class")) != resource.get("processing_eligibility") or resource.get("access_class") not in ACCESS_PAIRS:
        raise ValueError("source gate: access_class / processing_eligibility mismatch or forbidden access")
    if run.get("integrity_status") != "pass" or run.get("blockers") != []:
        raise ValueError("source gate: integrity must pass with no unresolved blockers")

    inventory = sources.get("inventory", {})
    index_path = local_path(root, inventory.get("local_path"))
    if inventory.get("sha256") != digest(index_path):
        raise ValueError("canonical inventory hash mismatch")
    excerpt(root, inventory.get("locator"))
    if not text(inventory.get("origin")):
        raise ValueError("canonical inventory needs its original URL or user-file identity")
    canonical = unique(inventory.get("items"), "item_id", "canonical inventory")
    for item in canonical.values():
        # Each denominator entry must appear in the retained canonical listing.
        entry = excerpt(root, item.get("inventory_locator"))
        if item.get("title", "") not in entry or not text(item.get("title")):
            raise ValueError(f"inventory title is absent from canonical listing: {item['item_id']}")
        if item.get("inventory_locator", "").split("#")[0] != inventory.get("local_path"):
            raise ValueError("inventory item locator must address the canonical listing")
        channels = item.get("required_channels")
        if not isinstance(channels, list) or "primary" not in channels or set(channels) - CHANNELS or len(channels) != len(set(channels)):
            raise ValueError("inventory required_channels must include primary and valid unique channels")
        if item.get("primary_kind") not in {"speech", "text"}:
            raise ValueError("inventory primary_kind must be speech or text")
        if item.get("primary_kind") == "speech":
            duration = item.get("duration_seconds")
            if isinstance(duration, bool) or not isinstance(duration, (int, float)) or duration <= 0:
                raise ValueError("speech inventory needs the original lesson duration_seconds")
            excerpt(root, item.get("duration_evidence_locator"))
        if not text(item.get("channel_basis")):
            raise ValueError("inventory channel_basis must explain visual/practice/attachment inspection")

    scope = sources.get("scope", {})
    included = scope.get("included_item_ids")
    exclusions = scope.get("exclusions")
    if not isinstance(included, list) or not included or any(not text(i) for i in included) or len(set(included)) != len(included):
        raise ValueError("scope included_item_ids must be non-empty and unique")
    if not isinstance(exclusions, list) or any(not isinstance(e, dict) for e in exclusions):
        raise ValueError("scope exclusions must be a list of records")
    excluded = [e.get("item_id") for e in exclusions]
    if len(excluded) != len(set(excluded)) or set(included) & set(excluded) or set(included) | set(excluded) != set(canonical):
        raise ValueError("scope must partition the entire canonical inventory; no silent denominator reduction")
    for exclusion in exclusions:
        if not text(exclusion.get("reason")):
            raise ValueError("scope exclusion requires learning impact and reason")
        excerpt(root, exclusion.get("authorization_locator"))
    if not text(scope.get("basis")):
        raise ValueError("scope basis must identify the user's requested scope")
    items = unique(run.get("expected_items"), "item_id", "expected_items")
    if set(items) != set(included):
        raise ValueError("expected_items must match locked included scope")
    expected_sequence = [item_id for item_id in canonical if item_id in included]
    for index, item_id in enumerate(expected_sequence, 1):
        if items[item_id].get("expected_order") != index or items[item_id].get("title") != canonical[item_id]["title"]:
            raise ValueError("expected items must preserve canonical titles and order")

    records = unique(sources.get("records"), "source_id", "source records")
    channels_by_unit = {item_id: set() for item_id in included}
    for record in records.values():
        unit = record.get("unit_id")
        if unit not in items or record.get("channel") not in CHANNELS:
            raise ValueError("source record has unknown unit_id or channel")
        if record.get("content_kind") not in CONTENT_KINDS:
            raise ValueError("metadata, summaries and AI text are not instructional source evidence")
        if ACCESS_PAIRS.get(record.get("access_class")) != record.get("processing_eligibility") or record.get("access_class") not in ACCESS_PAIRS:
            raise ValueError("source record has forbidden or mismatched access pair")
        for key in ("origin", "acquired_at", "acquisition_method", "coverage_basis"):
            if not text(record.get(key)):
                raise ValueError(f"source record needs {key}")
        if record.get("acquisition_method") not in ACQUISITION_METHODS:
            raise ValueError("AI generation/recollection/secondary summaries are not acquisition methods")
        path = local_path(root, record.get("local_path"))
        if path.suffix.lower() not in {".txt", ".md", ".vtt", ".srt", ".csv", ".py", ".js", ".json", ".html"}:
            raise ValueError("retain extracted teaching text alongside media/PDF/images")
        if record.get("sha256") != digest(path):
            raise ValueError(f"source hash mismatch: {record['source_id']}")
        if path.is_relative_to((root / "chapters").resolve()) or path.is_relative_to((root / manifest.get("output_dir", "dist")).resolve()):
            raise ValueError("generated chapters/outputs cannot be their own source evidence")
        value = excerpt(root, record.get("locator"))
        if record.get("locator", "").split("#")[0] != record.get("local_path") or value != record.get("content_evidence"):
            raise ValueError("content_evidence must equal the retained source excerpt")
        if record.get("content_kind") in {"asr", "slides"} or record.get("acquisition_method") == "ocr":
            raw = local_path(root, record.get("raw_path"))
            if record.get("raw_sha256") != digest(raw) or raw == path:
                raise ValueError("ASR/OCR/slides need distinct retained original media or page images and raw hash")
        verification = record.get("verification", {})
        if not text(verification.get("method")) or not verification.get("evidence_locators"):
            raise ValueError("source verification method and local evidence_locators are required")
        for locator in verification["evidence_locators"]:
            excerpt(root, locator)
        if record.get("channel") == "primary" and canonical[unit]["primary_kind"] == "speech" and record.get("content_kind") not in {"transcript", "captions", "asr"}:
            raise ValueError("notes/slides cannot silently replace a missing speech channel")
        if record.get("content_kind") in {"captions", "asr"}:
            caption_text = path.read_text(encoding="utf-8-sig")
            ranges = re.findall(r"(\d{1,2}:\d{2}(?::\d{2})?[.,]\d+)\s*-->\s*(\d{1,2}:\d{2}(?::\d{2})?[.,]\d+)", caption_text)
            if not ranges:
                raise ValueError("captions/ASR need retained timed segments, not a prose summary")
            intervals = [(caption_seconds(a), caption_seconds(b)) for a, b in ranges]
            if any(a < 0 or b <= a for a, b in intervals) or any(intervals[i][0] < intervals[i - 1][0] for i in range(1, len(intervals))):
                raise ValueError("caption timing is invalid or out of sequence")
            duration = canonical[unit].get("duration_seconds")
            if not isinstance(duration, (int, float)) or duration <= 0:
                raise ValueError("timed captions need canonical duration_seconds")
            tolerance = max(5, duration * .02)
            if intervals[0][0] > tolerance or abs(intervals[-1][1] - duration) > tolerance:
                raise ValueError("caption timing does not cover the canonical lesson boundaries")
            large_gaps = any(intervals[i][0] - intervals[i - 1][1] > max(30, duration * .05) for i in range(1, len(intervals)))
            if large_gaps:
                excerpt(root, verification.get("timing_gap_evidence_locator"))
        channels_by_unit[unit].add(record["channel"])

    for item_id, item in items.items():
        if not all(item.get(flag) is True for flag in ("acquired", "processed", "verified")):
            raise ValueError(f"source gate: {item_id} has not been acquired, processed and verified")
        if set(canonical[item_id]["required_channels"]) - channels_by_unit[item_id]:
            raise ValueError(f"source gate: missing required channel for {item_id}")

    evidence = rows(root, manifest.get("evidence_ledger", "evidence/evidence-ledger.csv"))
    evidence_by_unit = unique(evidence, "unit_id", "evidence ledger")
    if set(evidence_by_unit) != set(items):
        raise ValueError("evidence ledger must match expected items exactly")
    for unit, row in evidence_by_unit.items():
        selected = [r for r in records.values() if r["unit_id"] == unit and r["channel"] == "primary"]
        if row.get("source_locator") not in {r["locator"] for r in selected} or items[unit].get("source_locator") not in {r["locator"] for r in selected}:
            raise ValueError("source_locator does not resolve to retained primary instructional content")
        actual = excerpt(root, row["source_locator"])
        if row.get("content_evidence") != actual:
            raise ValueError("evidence ledger content_evidence differs from source text")
        path = local_path(root, row["source_locator"].split("#")[0])
        if row.get("evidence_size") != str(path.stat().st_size):
            raise ValueError("evidence_size must be the actual source byte count")
        for key in ("first_locator", "last_locator"):
            excerpt(root, row.get(key))
            if row[key].split("#")[0] != row["source_locator"].split("#")[0]:
                raise ValueError("first/last locators must address the same primary source")
        line_count = len(path.read_text(encoding="utf-8-sig").splitlines())
        if line_bounds(row["first_locator"])[0] != 1 or line_bounds(row["last_locator"])[1] != line_count:
            raise ValueError("first/last locators must cover actual retained file boundaries")

    if not reconstruction:
        return
    acquisition = load(root, "evidence/acquisition-gate.json")
    if acquisition.get("input_hashes") != acquisition_hashes(root, manifest):
        raise ValueError("acquisition gate is missing/stale; validate retained sources before drafting")
    chapter_paths = {c["path"] if isinstance(c, dict) else c for c in manifest.get("chapters", [])}
    source_map = load(root, manifest.get("source_map", "evidence/source-map.json"))
    if source_map.get("schema_version") != 1:
        raise ValueError("source-map: unsupported schema_version")
    citations = source_map.get("citations", [])
    if not isinstance(citations, list) or not citations:
        raise ValueError("source-map must contain claim-level citations")
    mapped_units, mapped_chapters, mapped_locators = set(), set(), set()
    mapped_teaching_lines = {}
    for citation in citations:
        record = records.get(citation.get("source_id"))
        if not record or citation.get("unit_id") != record["unit_id"]:
            raise ValueError("citation source_id/unit_id mismatch")
        if citation.get("claim_kind") not in {"course_teaching", "translation", "ai_explanation", "ai_supplement"}:
            raise ValueError("citation must distinguish source teaching from AI interpretation")
        locator = citation.get("source_locator", "")
        if locator.split("#")[0] != record["local_path"] or excerpt(root, locator) != citation.get("quote"):
            raise ValueError("citation quote does not match precise retained source range")
        target = citation.get("target_locator", "")
        chapter = target.split("#")[0]
        if chapter not in chapter_paths:
            raise ValueError("citation target is outside the ordered chapter master")
        target_text = excerpt(root, target)
        label = {"course_teaching": "[Course teaching]", "translation": "[Translation]", "ai_explanation": "[AI explanation]", "ai_supplement": "[AI supplement]"}[citation["claim_kind"]]
        if label not in target_text:
            raise ValueError("citation target must visibly carry its provenance label")
        mapped_units.add(record["unit_id"])
        mapped_chapters.add(chapter)
        mapped_locators.add(locator)
        if citation["claim_kind"] in {"course_teaching", "translation"}:
            start, end = line_bounds(target)
            mapped_teaching_lines.setdefault(chapter, set()).update(range(start, end + 1))
    if set(items) - mapped_units or chapter_paths - mapped_chapters:
        raise ValueError("every expected unit and output chapter needs precise source mapping")
    for chapter in chapter_paths:
        for number, line in enumerate(local_path(root, chapter).read_text(encoding="utf-8").splitlines(), 1):
            if ("[Course teaching]" in line or "[Translation]" in line) and number not in mapped_teaching_lines.get(chapter, set()):
                raise ValueError("every source-teaching/translation block needs its own source-map citation")
    concepts = rows(root, manifest.get("concept_coverage_ledger", "evidence/concept-coverage.csv"))
    unique(concepts, "concept_id", "concept coverage")
    concept_units = set()
    for row in concepts:
        locator = row.get("lecture_evidence", "")
        if locator not in mapped_locators:
            raise ValueError("concept lecture_evidence must match a checked source-map citation")
        source_units = {t.strip() for t in re.split(r"[,;|]", row.get("source_units", "")) if t.strip()}
        if not source_units or source_units - set(items):
            raise ValueError("concept references unknown source_units")
        if not any(c["source_locator"] == locator and c["unit_id"] in source_units for c in citations):
            raise ValueError("concept source_units do not match its cited evidence")
        concept_units.update(source_units)
        for field in ("explanation", "reasoning", "example", "boundaries", "quick_check", "application"):
            target = row.get(field, "")
            if target.split("#")[0] not in chapter_paths:
                raise ValueError(f"concept {field} must resolve to an actual output chapter range")
            excerpt(root, target)
    if set(items) - concept_units:
        raise ValueError("every expected unit needs concept coverage, not just a citation")
    for row in rows(root, manifest.get("visual_ledger", "evidence/visual-ledger.csv")):
        if row.get("source_unit") not in items:
            raise ValueError("visual ledger references unknown source unit")
        if row.get("action") in {"TEXT_ONLY", "AI_ILLUSTRATE"} and "visual" in canonical[row["source_unit"]]["required_channels"]:
            if "visual" not in channels_by_unit[row["source_unit"]]:
                raise ValueError("TEXT_ONLY/AI illustrations cannot discharge required visual acquisition")
        if row.get("action") in {"EXTRACT", "REBUILD_EXACT", "REDRAW_CONCEPT"}:
            visual_sources = [r for r in records.values() if r["unit_id"] == row["source_unit"] and r["channel"] == "visual"]
            if row.get("locator", "").split("#")[0] not in {r["local_path"] for r in visual_sources}:
                raise ValueError("source-based visual reconstruction needs retained visual channel evidence")
        excerpt(root, row.get("locator"))


def validate_sources(root: Path, manifest: dict, *, reconstruction: bool = True) -> list[str]:
    try:
        _validate(root, manifest, reconstruction=reconstruction)
        return []
    except (ValueError, TypeError, KeyError, AttributeError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"source gate: {exc}"]


def acquisition_hashes(root: Path, manifest: dict) -> dict[str, str]:
    return input_hashes(root, manifest, acquisition=True)


def input_hashes(root: Path, manifest: dict, *, acquisition: bool = False) -> dict[str, str]:
    """Bind scope, identity, evidence, chapters and build settings to the review."""
    paths = {
        manifest.get("source_manifest", "evidence/source-manifest.json"),
        manifest.get("evidence_ledger", "evidence/evidence-ledger.csv"),
    }
    if not acquisition:
        paths.update({manifest.get("source_map", "evidence/source-map.json"), manifest.get("concept_coverage_ledger", "evidence/concept-coverage.csv"), manifest.get("visual_ledger", "evidence/visual-ledger.csv"), "evidence/acquisition-gate.json"})
    sources = load(root, manifest.get("source_manifest", "evidence/source-manifest.json"))
    paths.add(sources["inventory"]["local_path"])
    for entry in sources["records"]:
        paths.add(entry["local_path"])
        if entry.get("raw_path"):
            paths.add(entry["raw_path"])
        paths.update(l.split("#")[0] for l in entry["verification"]["evidence_locators"])
    paths.update(e["authorization_locator"].split("#")[0] for e in sources["scope"]["exclusions"])
    if not acquisition:
        paths.update(c["path"] if isinstance(c, dict) else c for c in manifest["chapters"])
    result = {p: digest(local_path(root, p)) for p in sorted(paths)}
    run = load(root, manifest.get("run_ledger", "run-ledger.json"))
    # Mutable checkpoint/QA fields are intentionally excluded; meaning and scope are bound.
    semantic = {k: run.get(k) for k in ("run_id", "resource", "learner", "outcome", "declared_scope", "expected_items", "requested_artifact_level", "target_artifact_level", "delivery_contract", "artifact_revision")}
    if acquisition:
        semantic.pop("artifact_revision")
        semantic["expected_items"] = [{k: item.get(k) for k in ("item_id", "title", "expected_order", "source_locator", "acquired", "processed", "verified")} for item in run["expected_items"]]
    result["@run_context"] = hashlib.sha256(json.dumps(semantic, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    if not acquisition:
        result["@manifest"] = hashlib.sha256(json.dumps(manifest, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return result


def artifact_paths(root: Path, manifest: dict) -> dict[str, Path]:
    base = manifest.get("output_basename", "course-book")
    return {k: local_path(root, manifest.get(k, default)) for k, default in {
        "canonical_markdown": f"dist/{base}.md", "standalone_html": f"dist/{base}-standalone.html", "pdf": f"dist/{base}.pdf",
    }.items()}


def review_errors(root: Path, manifest: dict, qa: dict) -> list[str]:
    errors = []
    try:
        if qa.get("review_input_hashes") != input_hashes(root, manifest):
            errors.append("QA review input hashes are stale or missing; source/scope/chapter/build settings changed")
        for key, path in artifact_paths(root, manifest).items():
            if qa.get("artifact_hashes", {}).get(key) != digest(path):
                errors.append(f"QA artifact_hashes.{key} changed since review snapshot; review again before sealing")
        for group in ("checks", "format_checks"):
            entries = qa.get(group, [])
            if not isinstance(entries, list) or any(not isinstance(r, dict) for r in entries):
                raise ValueError(f"QA {group} must contain records")
            if len({r.get("check") for r in entries}) != len(entries):
                raise ValueError("QA contains duplicate check names")
            for row in entries:
                if row.get("result") == "not_applicable" and row.get("check") in CORE_CHECKS:
                    raise ValueError("core source/traceability/provenance checks cannot be not_applicable")
                excerpt(root, row.get("evidence"))
                path = local_path(root, row["evidence"].split("#")[0])
                if row.get("evidence_sha256") != digest(path):
                    raise ValueError("QA evidence needs matching evidence_sha256 for the actual review report")
    except (ValueError, TypeError, KeyError, AttributeError, OSError, UnicodeError) as exc:
        errors.append(f"review gate: {exc}")
    return errors
