#!/usr/bin/env python3
"""Capture files BEFORE reviewing; this command never grants a QA pass."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
try:
    from .source_gate import artifact_paths, digest, input_hashes, load, validate_sources
    from .seal_course_pack import write_atomic
except ImportError:
    from source_gate import artifact_paths, digest, input_hashes, load, validate_sources
    from seal_course_pack import write_atomic


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack_dir", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.pack_dir).resolve()
    manifest = load(root, "book-manifest.json")
    errors = validate_sources(root, manifest)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    qa_path = root / manifest.get("qa_record", "evidence/learning-qa.json")
    run_path = root / manifest.get("run_ledger", "run-ledger.json")
    # Resolve paths through the containment checker before any writes.
    qa = load(root, manifest.get("qa_record", "evidence/learning-qa.json"))
    run = load(root, manifest.get("run_ledger", "run-ledger.json"))
    files = artifact_paths(root, manifest)
    if any(not p.stat().st_size for p in files.values()):
        raise ValueError("cannot review an empty artifact")
    history = qa.setdefault("history", [])
    history.append({k: v for k, v in qa.items() if k != "history"})
    qa.update({
        "artifact_revision": run["artifact_revision"],
        "artifact_content_sha256": digest(files["canonical_markdown"]),
        "artifact_hashes": {k: digest(p) for k, p in files.items()},
        "review_input_hashes": input_hashes(root, manifest),
        "review_started_at": datetime.now(timezone.utc).isoformat(),
        "learning_qa": "stale", "checks": [], "format_checks": [], "failed_checks": [],
    })
    qa.pop("sealed_at", None)
    run.update({"learning_qa": "stale", "checkpoint_status": "review_pending", "completion_name": None})
    write_atomic(run_path, run)
    write_atomic(qa_path, qa)
    print("SNAPSHOT: review these exact files and record concrete check evidence; QA remains stale")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
