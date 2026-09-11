from __future__ import annotations

import csv
import contextlib
import base64
import io
import json
import shutil
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from uuid import uuid4

from reportlab.pdfgen import canvas


SKILL_DIR = Path(__file__).resolve().parents[1]
INIT = SKILL_DIR / "scripts/init_course_pack.py"
BUILD = SKILL_DIR / "scripts/build_course_book.py"
VALIDATE = SKILL_DIR / "scripts/validate_course_pack.py"
SEAL = SKILL_DIR / "scripts/seal_course_pack.py"
TEST_TMP = SKILL_DIR / "tests/.tmp"
TEST_TMP.mkdir(exist_ok=True)
sys.path.insert(0, str(SKILL_DIR))

from scripts import build_course_book, init_course_pack, seal_course_pack, validate_course_pack


def run(script: str, *args: str) -> SimpleNamespace:
    modules = {
        str(INIT): init_course_pack,
        str(BUILD): build_course_book,
        str(VALIDATE): validate_course_pack,
        str(SEAL): seal_course_pack,
    }
    stdout = io.StringIO()
    stderr = io.StringIO()
    with patch.object(sys, "argv", [script, *args]), contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        try:
            returncode = modules[script].main()
        except SystemExit as exc:
            returncode = int(exc.code or 0)
    return SimpleNamespace(returncode=returncode, stdout=stdout.getvalue(), stderr=stderr.getvalue())


class CoursePackPipelineTests(unittest.TestCase):
    def fresh_root(self) -> Path:
        root = TEST_TMP / uuid4().hex
        root.mkdir()
        self.addCleanup(shutil.rmtree, root, True)
        return root

    def make_pack(self, root: Path, *, complete: bool) -> Path:
        pack = root / "pack"
        result = run(str(INIT), str(pack), "--title", "Reliable Course")
        self.assertEqual(result.returncode, 0, result.stderr)
        if not complete:
            return pack

        chapter = pack / "chapters/01-course-book.md"
        chapter.write_text(
            "# Reliable Course\n\n"
            "> [Course teaching] A verified source teaches the method.\n\n"
            "## Method\n\nReasoning, example, boundary, check, and transfer practice.\n\n"
            "<details>\n<summary>Answer</summary>\nThe worked answer explains why.\n</details>\n",
            encoding="utf-8",
        )
        (pack / "source.txt").write_text("Verified source transcript.", encoding="utf-8")
        manifest_path = pack / "book-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest.update({
            "source_runtime_minutes": 10,
            "estimated_reading_minutes": 8,
            "estimated_practice_minutes": 4,
            "estimated_project_minutes": 2,
            "estimated_review_minutes": 1,
            "estimated_total_study_minutes": 15,
        })
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        with (pack / "evidence/evidence-ledger.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow([
                "unit_id", "title", "official_duration", "source_type", "source_locator",
                "content_evidence", "first_locator", "last_locator", "evidence_size",
                "visual_support", "summary_location", "status",
            ])
            writer.writerow(["u1", "Method", "10m", "official transcript", "source.txt#L1", "verified transcript", "00:00", "10:00", "1000 words", "none needed", "chapters/01-course-book.md#method", "READY"])
        with (pack / "evidence/concept-coverage.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow([
                "concept_id", "chapter", "concept", "source_units", "lecture_evidence",
                "explanation", "reasoning", "example", "boundaries", "visual",
                "quick_check", "application", "status",
            ])
            writer.writerow(["c1", "01", "Method", "u1", "source.txt#L1", "#method", "#method", "#method", "#method", "NOT_NEEDED: verbal", "#method", "#method", "READY"])
        with (pack / "evidence/visual-ledger.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow([
                "visual_id", "source_unit", "locator", "visual_type", "teaching_role",
                "action", "rights_basis", "asset_path", "caption", "status",
            ])
            writer.writerow(["v1", "u1", "source.txt#L1", "none", "not needed", "TEXT_ONLY", "NOT_NEEDED: no source visual", "NOT_NEEDED: text-only", "NOT_NEEDED: text-only", "READY"])

        run_ledger_path = pack / "run-ledger.json"
        ledger = json.loads(run_ledger_path.read_text(encoding="utf-8"))
        ledger.update({
            "resource": {
                "identity": "Example/Open course",
                "edition": "2026",
                "source_set_revision": "source-v1",
                "source_urls": ["https://example.test/course"],
                "access_class": "free_access",
                "processing_eligibility": "eligible",
            },
            "learner": "adult learner",
            "outcome": "apply the method",
            "declared_scope": "unit u1",
            "expected_items": [{
                "item_id": "u1", "title": "Method", "expected_order": 1,
                "source_locator": "source.txt#L1", "item_status": "READY",
                "attempt_count": 1, "last_error": "none", "blocking_impact": "none",
                "next_action": "none", "acquired": True, "processed": True,
                "verified": True, "reconstructed": True,
            }],
            "coverage": {"expected": 1, "acquired": 1, "processed": 1, "verified": 1, "reconstructed": 1},
            "artifact_status": "complete",
            "integrity_status": "pass",
            "checkpoint_status": "published",
            "completion_name": "reconstructed learning artifact complete",
            "learning_qa": "pass",
        })
        run_ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        learning_checks = [
            "objective_traceability", "prerequisite_order", "source_accuracy",
            "labeled_synthesis", "correct_examples", "feedback_guidance",
            "compression_integrity", "time_estimate_assumptions", "visible_limitations",
        ]
        format_checks = [
            "markdown_complete", "html_offline_desktop_mobile_print",
            "pdf_visual_review", "format_parity",
        ]
        qa = {
            "schema_version": 1,
            "qa_profile": "reconstructed_learning_artifact",
            "artifact_revision": "artifact-v1",
            "learning_qa": "pass",
            "checks": [{"check": name, "result": "pass", "evidence": "reviewed chapter #method"} for name in learning_checks],
            "failed_checks": [],
            "format_checks": [{"check": name, "result": "pass", "evidence": "reviewed generated artifact"} for name in format_checks],
        }
        (pack / "evidence/learning-qa.json").write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        build = run(str(BUILD), str(manifest_path), "--html-only")
        self.assertEqual(build.returncode, 0, build.stderr)
        pdf = canvas.Canvas(str(pack / "dist/course-book.pdf"))
        pdf.drawString(72, 720, "Reliable Course with extractable teaching text")
        pdf.save()
        sealed = run(str(SEAL), str(pack))
        self.assertEqual(sealed.returncode, 0, sealed.stderr)
        return pack

    @classmethod
    def tearDownClass(cls) -> None:
        try:
            TEST_TMP.rmdir()
        except OSError:
            pass

    def test_scaffold_cannot_claim_completion(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=False)
        result = run(str(VALIDATE), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("expected_items", result.stdout)
        self.assertIn("Learning QA", result.stdout)

    def test_complete_pack_passes(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        result = run(str(VALIDATE), str(pack))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_stale_qa_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        ledger_path = pack / "run-ledger.json"
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        ledger["artifact_revision"] = "artifact-v2"
        ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        result = run(str(VALIDATE), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("artifact_revision does not match", result.stdout)

    def test_remote_runtime_image_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        html_path = pack / "dist/course-book-standalone.html"
        html_path.write_text(html_path.read_text(encoding="utf-8").replace("</main>", '<img src="https://example.test/x.png"></main>'), encoding="utf-8")
        result = run(str(VALIDATE), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("non-inlined image resource", result.stdout)

    def test_post_qa_artifact_mutation_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        html_path = pack / "dist/course-book-standalone.html"
        html_path.write_text(html_path.read_text(encoding="utf-8") + "<!-- changed -->", encoding="utf-8")
        result = run(str(VALIDATE), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("artifact_hashes.standalone_html", result.stdout)

    def test_fake_source_locator_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        evidence_path = pack / "evidence/evidence-ledger.csv"
        with evidence_path.open(encoding="utf-8") as handle:
            rows = list(csv.reader(handle))
        rows[1][4] = "sources/missing.vtt#00:00"
        with evidence_path.open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle).writerows(rows)
        result = run(str(VALIDATE), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("source_locator does not resolve", result.stdout)

    def test_local_png_is_inlined_in_standalone_html(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        png = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=")
        (pack / "assets/dot.png").write_bytes(png)
        chapter = pack / "chapters/01-course-book.md"
        chapter.write_text(chapter.read_text(encoding="utf-8") + "\n![A teaching dot](../assets/dot.png)\n", encoding="utf-8")
        build = run(str(BUILD), str(pack / "book-manifest.json"), "--html-only")
        self.assertEqual(build.returncode, 0, build.stderr)
        standalone = (pack / "dist/course-book-standalone.html").read_text(encoding="utf-8")
        self.assertIn("data:image/png;base64,", standalone)
        self.assertNotIn("../assets/dot.png", standalone)

    def test_manifest_path_escape_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        manifest_path = pack / "book-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["canonical_markdown"] = "../../outside.md"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        result = run(str(VALIDATE), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("escapes the course pack", result.stdout)


if __name__ == "__main__":
    unittest.main()
