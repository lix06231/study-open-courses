#!/usr/bin/env python3
"""Run the mandatory acquisition gate before drafting learner-facing teaching."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
try:
    from .source_gate import acquisition_hashes, load, validate_sources
except ImportError:
    from source_gate import acquisition_hashes, load, validate_sources


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack_dir", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.pack_dir).resolve()
    try:
        manifest = load(root, "book-manifest.json")
        errors = validate_sources(root, manifest, reconstruction=False)
        if not errors:
            snapshot = {"schema_version": 1, "validated_at": datetime.now(timezone.utc).isoformat(), "input_hashes": acquisition_hashes(root, manifest)}
            # Resolve an existing snapshot before replacing it; no escaping symlink.
            target = (root / "evidence/acquisition-gate.json").resolve()
            target.relative_to(root)
            target.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (ValueError, OSError) as exc:
        errors = [str(exc)]
    for error in errors:
        print(f"ERROR {error}")
    print("FAIL: source evidence unavailable" if errors else "PASS: retained acquisition evidence is structurally consistent; human content review still required")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
