#!/usr/bin/env python3
"""Create the deterministic textbook-mode course-pack skeleton."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


LEDGERS = {
    "evidence-ledger.csv": [
        "unit_id", "title", "official_duration", "source_type", "source_locator",
        "content_evidence", "first_locator", "last_locator", "evidence_size",
        "visual_support", "summary_location", "status",
    ],
    "concept-coverage.csv": [
        "concept_id", "chapter", "concept", "source_units", "lecture_evidence",
        "explanation", "reasoning", "example", "boundaries", "visual",
        "quick_check", "application", "status",
    ],
    "visual-ledger.csv": [
        "visual_id", "source_unit", "locator", "visual_type", "teaching_role",
        "action", "rights_basis", "asset_path", "caption", "status",
    ],
}


def write_new(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir")
    parser.add_argument("--title", required=True)
    parser.add_argument("--language", default="zh-CN")
    args = parser.parse_args()
    root = Path(args.output_dir).resolve()
    for name in ("chapters", "evidence", "assets", "sources", "dist"):
        (root / name).mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    manifest = {
        "title": args.title,
        "subtitle": "AI-enhanced course book",
        "language": args.language,
        "author": "",
        "source_note": "",
        "source_runtime_minutes": 0,
        "estimated_reading_minutes": 0,
        "estimated_practice_minutes": 0,
        "estimated_project_minutes": 0,
        "estimated_review_minutes": 0,
        "estimated_total_study_minutes": 0,
        "evidence_ledger": "evidence/evidence-ledger.csv",
        "concept_coverage_ledger": "evidence/concept-coverage.csv",
        "visual_ledger": "evidence/visual-ledger.csv",
        "run_ledger": "run-ledger.json",
        "qa_record": "evidence/learning-qa.json",
        "chapters": [{"path": "chapters/01-course-book.md", "title": "Course Book"}],
        "output_dir": "dist",
        "output_basename": "course-book",
        "canonical_markdown": "dist/course-book.md",
        "standalone_html": "dist/course-book-standalone.html",
        "pdf": "dist/course-book.pdf",
    }
    manifest_path = root / "book-manifest.json"
    if not manifest_path.exists():
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_new(
        root / "chapters/01-course-book.md",
        f"# {args.title}\n\n> [Course teaching] Replace this scaffold only after the evidence gate is READY.\n",
    )
    for filename, fields in LEDGERS.items():
        path = root / "evidence" / filename
        if not path.exists():
            with path.open("w", encoding="utf-8", newline="") as handle:
                csv.writer(handle).writerow(fields)
    run_ledger = {
        "schema_version": 1,
        "run_id": str(uuid4()),
        "started_at": now,
        "last_updated_at": now,
        "resource": {
            "identity": "",
            "edition": "",
            "source_set_revision": "source-v1",
            "source_urls": [],
            "access_class": "unknown",
            "processing_eligibility": "blocked_pending_classification",
        },
        "learner": "",
        "outcome": "",
        "declared_scope": "",
        "requested_artifact_level": "reconstructed learning artifact",
        "target_artifact_level": "reconstructed learning artifact",
        "delivery_contract": "three_primary_files",
        "explicit_format_override": None,
        "expected_items": [],
        "coverage": {
            "expected": 0,
            "acquired": 0,
            "processed": 0,
            "verified": 0,
            "reconstructed": 0,
        },
        "artifact_status": "not_started",
        "integrity_status": "not_checked",
        "checkpoint_status": "initialized",
        "completion_name": None,
        "artifact_revision": "artifact-v1",
        "artifact_content_sha256": "",
        "qa_profile": "reconstructed_learning_artifact",
        "learning_qa": "not_run",
        "blockers": [],
    }
    write_new(root / "run-ledger.json", json.dumps(run_ledger, ensure_ascii=False, indent=2) + "\n")
    qa_record = {
        "schema_version": 1,
        "qa_profile": "reconstructed_learning_artifact",
        "artifact_revision": "artifact-v1",
        "artifact_content_sha256": "",
        "artifact_hashes": {},
        "learning_qa": "not_run",
        "checks": [],
        "failed_checks": [],
        "format_checks": [],
    }
    write_new(root / "evidence/learning-qa.json", json.dumps(qa_record, ensure_ascii=False, indent=2) + "\n")
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
