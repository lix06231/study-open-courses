#!/usr/bin/env python3
"""Seal reviewed course artifacts to the current QA and artifact revision."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def pack_path(root: Path, relative: str | Path) -> Path:
    path = (root / relative).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"path escapes the course pack: {relative}") from exc
    return path


def write_atomic(path: Path, value: dict) -> None:
    temporary = path.with_name(f"{path.name}.tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack_dir", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.pack_dir).resolve()
    manifest = load_object(root / "book-manifest.json")
    run_path = pack_path(root, manifest.get("run_ledger", "run-ledger.json"))
    qa_path = pack_path(root, manifest.get("qa_record", "evidence/learning-qa.json"))
    run = load_object(run_path)
    qa = load_object(qa_path)

    if run.get("learning_qa") != "pass" or qa.get("learning_qa") != "pass":
        raise ValueError("record Learning QA pass in both records before sealing")
    if run.get("artifact_revision") != qa.get("artifact_revision"):
        raise ValueError("artifact_revision differs between run ledger and QA record")
    if qa.get("failed_checks") != []:
        raise ValueError("failed_checks must be empty before sealing")

    basename = manifest.get("output_basename", "course-book")
    files = {
        "canonical_markdown": pack_path(root, manifest.get("canonical_markdown", f"dist/{basename}.md")),
        "standalone_html": pack_path(root, manifest.get("standalone_html", f"dist/{basename}-standalone.html")),
        "pdf": pack_path(root, manifest.get("pdf", f"dist/{basename}.pdf")),
    }
    missing = [str(path) for path in files.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"cannot seal missing artifact(s): {missing}")

    content_hash = digest(files["canonical_markdown"])
    if manifest.get("build_content_sha256") != content_hash:
        raise ValueError("canonical Markdown changed after the last build; rebuild and re-run QA")
    run["artifact_content_sha256"] = content_hash
    qa["artifact_content_sha256"] = content_hash
    qa["artifact_hashes"] = {name: digest(path) for name, path in files.items()}
    timestamp = datetime.now(timezone.utc).isoformat()
    run["last_updated_at"] = timestamp
    run["checkpoint_status"] = "sealed"
    qa["sealed_at"] = timestamp
    write_atomic(run_path, run)
    write_atomic(qa_path, qa)
    print(f"SEALED: {run.get('artifact_revision')} ({content_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
