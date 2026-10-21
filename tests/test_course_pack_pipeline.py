from __future__ import annotations

import csv
import contextlib
import base64
import io
import json
import hashlib
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
ACQUIRE = SKILL_DIR / "scripts/validate_source_evidence.py"
CAPTURE = SKILL_DIR / "scripts/capture_qa_snapshot.py"
TEST_TMP = SKILL_DIR / "tests/.tmp"
TEST_TMP.mkdir(exist_ok=True)
sys.path.insert(0, str(SKILL_DIR))

from scripts import build_course_book, init_course_pack, seal_course_pack, validate_course_pack
from scripts import capture_qa_snapshot, validate_source_evidence


def run(script: str, *args: str) -> SimpleNamespace:
    modules = {
        str(INIT): init_course_pack,
        str(BUILD): build_course_book,
        str(VALIDATE): validate_course_pack,
        str(SEAL): seal_course_pack,
        str(ACQUIRE): validate_source_evidence,
        str(CAPTURE): capture_qa_snapshot,
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
            "> [Course teaching] To compare two costs, subtract the old cost from the new cost.\n\n"
            "## Method\n\nReasoning, example, boundary, check, and transfer practice.\n\n"
            "<details>\n<summary>Answer</summary>\nThe worked answer explains why.\n</details>\n",
            encoding="utf-8",
        )
        (pack / "source.txt").write_text(
            "To compare two costs, subtract the old cost from the new cost.\n"
            "For an old cost of 10 and a new cost of 14, the change is 14 - 10 = 4.\n"
            "Keep the units and the comparison period the same; otherwise the subtraction is misleading.\n",
            encoding="utf-8",
        )
        (pack / "sources/inventory.txt").write_text("Synthetic test resource, text edition.\nMethod: one text lesson, no visual or companion files.\n", encoding="utf-8")
        (pack / "sources/verification.md").write_text("Test fixture: read all three retained lines; example arithmetic gives 4; no speech/visual/practice/attachment channels in this text-only fixture.\n", encoding="utf-8")
        primary_quote = (pack / "source.txt").read_text(encoding="utf-8").splitlines()[0]
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
            writer.writerow(["u1", "Method", "10m", "lecture_text", "source.txt#L1", primary_quote, "source.txt#L1", "source.txt#L3", str((pack / "source.txt").stat().st_size), "none needed", "chapters/01-course-book.md#L3", "READY"])
        with (pack / "evidence/concept-coverage.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow([
                "concept_id", "chapter", "concept", "source_units", "lecture_evidence",
                "explanation", "reasoning", "example", "boundaries", "visual",
                "quick_check", "application", "status",
            ])
            writer.writerow(["c1", "01", "Method", "u1", "source.txt#L1", *["chapters/01-course-book.md#L5-L10"] * 4, "NOT_NEEDED: verbal", "chapters/01-course-book.md#L5-L10", "chapters/01-course-book.md#L5-L10", "READY"])
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

        source_manifest = {
            "schema_version": 1,
            "inventory": {
                "origin": "user-file: synthetic fixture", "local_path": "sources/inventory.txt",
                "sha256": hashlib.sha256((pack / "sources/inventory.txt").read_bytes()).hexdigest(),
                "locator": "sources/inventory.txt#L1-L2",
                "items": [{"item_id": "u1", "title": "Method", "inventory_locator": "sources/inventory.txt#L2", "required_channels": ["primary"], "primary_kind": "text", "channel_basis": "Synthetic text source has no required visual, practice or attachment channel."}],
            },
            "scope": {"basis": "user requested the entire synthetic test resource", "included_item_ids": ["u1"], "exclusions": []},
            "records": [{
                "source_id": "s1", "unit_id": "u1", "channel": "primary", "content_kind": "lecture_text",
                "origin": "user-file: test source.txt", "acquired_at": "2026-10-05T00:00:00Z",
                "acquisition_method": "native_text", "coverage_basis": "all three teaching lines retained",
                "access_class": "free_access", "processing_eligibility": "eligible",
                "local_path": "source.txt", "sha256": hashlib.sha256((pack / "source.txt").read_bytes()).hexdigest(),
                "locator": "source.txt#L1", "content_evidence": primary_quote,
                "verification": {"method": "synthetic fixture consistency check", "evidence_locators": ["sources/verification.md#L1"]},
            }],
        }
        (pack / "evidence/source-manifest.json").write_text(json.dumps(source_manifest, indent=2), encoding="utf-8")
        (pack / "evidence/source-map.json").write_text(json.dumps({
            "schema_version": 1,
            "citations": [{"unit_id": "u1", "source_id": "s1", "claim_kind": "course_teaching", "source_locator": "source.txt#L1", "quote": primary_quote, "target_locator": "chapters/01-course-book.md#L3"}],
        }), encoding="utf-8")
        acquired = run(str(ACQUIRE), str(pack))
        self.assertEqual(acquired.returncode, 0, acquired.stdout + acquired.stderr)

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
        captured = run(str(CAPTURE), str(pack))
        self.assertEqual(captured.returncode, 0, captured.stdout + captured.stderr)
        review_path = pack / "evidence/review.md"
        review_path.write_text("Synthetic QA fixture: chapter L3 compared with source L1. Format assertions are fixture claims for testing state consistency, not actual visual acceptance.\n", encoding="utf-8")
        qa_path = pack / "evidence/learning-qa.json"
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
        evidence = {"evidence": "evidence/review.md#L1", "evidence_sha256": hashlib.sha256(review_path.read_bytes()).hexdigest()}
        qa.update({"learning_qa": "pass", "failed_checks": [],
                   "checks": [{"check": name, "result": "pass", **evidence} for name in learning_checks],
                   "format_checks": [{"check": name, "result": "pass", **evidence} for name in format_checks]})
        qa_path.write_text(json.dumps(qa, indent=2), encoding="utf-8")
        ledger = json.loads(run_ledger_path.read_text(encoding="utf-8"))
        ledger.update({"learning_qa": "pass", "completion_name": "reconstructed learning artifact complete"})
        run_ledger_path.write_text(json.dumps(ledger, indent=2), encoding="utf-8")
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

    def edit_json(self, pack: Path, name: str, change) -> None:
        path = pack / name
        value = json.loads(path.read_text(encoding="utf-8"))
        change(value)
        path.write_text(json.dumps(value, indent=2), encoding="utf-8")

    def assert_gate_rejects(self, pack: Path, phrase: str) -> None:
        result = run(str(ACQUIRE), str(pack))
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(phrase, result.stdout)

    def test_build_blocks_missing_content_before_writing_outputs(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=False)
        result = run(str(BUILD), str(pack / "book-manifest.json"), "--html-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((pack / "dist/course-book.md").exists())

    def test_url_only_evidence_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["records"][0].update(local_path="https://example.test/lesson"))
        self.assert_gate_rejects(pack, "retained local path")

    def test_metadata_is_not_instructional_evidence(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["records"][0].update(content_kind="syllabus"))
        self.assert_gate_rejects(pack, "not instructional source evidence")

    def test_ai_generation_is_not_acquisition(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["records"][0].update(acquisition_method="ai_generation"))
        self.assert_gate_rejects(pack, "not acquisition methods")

    def test_source_change_invalidates_gate_and_completion(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        (pack / "source.txt").write_text("Replaced source.", encoding="utf-8")
        self.assert_gate_rejects(pack, "source hash mismatch")
        self.assertNotEqual(run(str(VALIDATE), str(pack)).returncode, 0)
        self.assertNotEqual(run(str(SEAL), str(pack)).returncode, 0)

    def test_out_of_range_fragment_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["records"][0].update(locator="source.txt#L999"))
        self.assert_gate_rejects(pack, "outside retained evidence")

    def test_fabricated_quote_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["records"][0].update(content_evidence="The instructor supposedly said this."))
        self.assert_gate_rejects(pack, "must equal the retained source excerpt")

    def test_fake_evidence_size_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        path = pack / "evidence/evidence-ledger.csv"
        with path.open(encoding="utf-8", newline="") as handle:
            data = list(csv.reader(handle))
        data[1][8] = "100000 words"
        with path.open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle).writerows(data)
        self.assert_gate_rejects(pack, "actual source byte count")

    def test_missing_visual_channel_cannot_be_text_only(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["inventory"]["items"][0].update(required_channels=["primary", "visual"]))
        self.assert_gate_rejects(pack, "missing required channel")

    def test_missing_practice_channel_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["inventory"]["items"][0].update(required_channels=["primary", "practice"]))
        self.assert_gate_rejects(pack, "missing required channel")

    def test_text_notes_cannot_replace_lecture_speech(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["inventory"]["items"][0].update(primary_kind="speech", duration_seconds=600, duration_evidence_locator="sources/inventory.txt#L2"))
        self.assert_gate_rejects(pack, "missing speech channel")

    def test_source_access_pair_cannot_hide_paid_content(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["records"][0].update(access_class="paid_or_entitlement_gated", processing_eligibility="eligible"))
        self.assert_gate_rejects(pack, "forbidden or mismatched access pair")

    def test_whole_resource_denominator_cannot_silently_shrink(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        def add_item(obj):
            item = dict(obj["inventory"]["items"][0], item_id="u2")
            obj["inventory"]["items"].append(item)
        self.edit_json(pack, "evidence/source-manifest.json", add_item)
        self.assert_gate_rejects(pack, "no silent denominator reduction")

    def test_scope_exclusion_requires_user_instruction_evidence(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        def exclude(obj):
            obj["inventory"]["items"].append(dict(obj["inventory"]["items"][0], item_id="u2"))
            obj["scope"]["exclusions"].append({"item_id": "u2", "reason": "too much work"})
        self.edit_json(pack, "evidence/source-manifest.json", exclude)
        self.assert_gate_rejects(pack, "exact local")

    def test_generated_chapter_cannot_serve_as_own_source(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        chapter = pack / "chapters/01-course-book.md"
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["records"][0].update(local_path="chapters/01-course-book.md", sha256=hashlib.sha256(chapter.read_bytes()).hexdigest()))
        self.assert_gate_rejects(pack, "cannot be their own source")

    def test_scope_change_after_acquisition_requires_new_gate(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "run-ledger.json", lambda obj: obj.update(declared_scope="a different scope"))
        result = run(str(BUILD), str(pack / "book-manifest.json"), "--html-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("acquisition gate is missing/stale", result.stderr)

    def test_core_source_qa_cannot_be_not_applicable(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/learning-qa.json", lambda obj: obj["checks"][2].update(result="not_applicable", reason="not enough time"))
        result = run(str(SEAL), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot be not_applicable", result.stdout)

    def test_seal_cannot_retroactively_approve_changed_html(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        qa_path = pack / "evidence/learning-qa.json"
        before = qa_path.read_bytes()
        html = pack / "dist/course-book-standalone.html"
        html.write_text(html.read_text(encoding="utf-8") + "<!-- edited -->", encoding="utf-8")
        result = run(str(SEAL), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("changed since review snapshot", result.stdout)
        self.assertEqual(qa_path.read_bytes(), before)

    def test_duplicate_qa_checks_are_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/learning-qa.json", lambda obj: obj["checks"].append(dict(obj["checks"][0])))
        result = run(str(SEAL), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate check names", result.stdout)

    def test_review_report_mutation_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        (pack / "evidence/review.md").write_text("Changed QA report.", encoding="utf-8")
        result = run(str(VALIDATE), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("evidence_sha256", result.stdout)

    def test_citation_cannot_invent_source_quote(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-map.json", lambda obj: obj["citations"][0].update(quote="An invented teacher claim."))
        result = run(str(BUILD), str(pack / "book-manifest.json"), "--html-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("citation quote does not match", result.stderr)

    def test_unmapped_chapter_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        (pack / "chapters/02-invented.md").write_text("# Invented lesson\n", encoding="utf-8")
        self.edit_json(pack, "book-manifest.json", lambda obj: obj["chapters"].append({"path": "chapters/02-invented.md"}))
        result = run(str(BUILD), str(pack / "book-manifest.json"), "--html-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("every expected unit and output chapter", result.stderr)

    def test_rebuild_marks_previous_qa_stale(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        result = run(str(BUILD), str(pack / "book-manifest.json"), "--html-only")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads((pack / "evidence/learning-qa.json").read_text())["learning_qa"], "stale")
        self.assertNotEqual(run(str(SEAL), str(pack)).returncode, 0)

    def test_capture_resets_checks_and_preserves_history(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        result = run(str(CAPTURE), str(pack))
        self.assertEqual(result.returncode, 0, result.stdout)
        qa = json.loads((pack / "evidence/learning-qa.json").read_text())
        self.assertEqual(qa["learning_qa"], "stale")
        self.assertEqual(qa["checks"], [])
        self.assertEqual(qa["history"][-1]["learning_qa"], "pass")

    def test_no_pdf_flag_cannot_authorize_formal_completion(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        (pack / "dist/course-book.pdf").unlink()
        self.assertNotEqual(run(str(VALIDATE), str(pack), "--allow-no-pdf").returncode, 0)

    def test_unavailable_pdf_parser_blocks_formal_completion(self) -> None:
        import builtins
        pack = self.make_pack(self.fresh_root(), complete=True)
        original = builtins.__import__
        def without_pdf(name, *args, **kwargs):
            if name in {"pymupdf", "pypdf"}:
                raise ImportError("simulated unavailable parser")
            return original(name, *args, **kwargs)
        with patch("builtins.__import__", side_effect=without_pdf):
            result = run(str(VALIDATE), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("required PDF checks are unverified", result.stdout)

    def test_caption_summary_without_timed_segments_is_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/source-manifest.json", lambda obj: obj["records"][0].update(content_kind="captions"))
        self.assert_gate_rejects(pack, "need retained timed segments")

    def test_truncated_captions_are_rejected(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        source = pack / "source.txt"
        source.write_text("00:00:00.000 --> 00:00:10.000\nOnly the opening was acquired.\n", encoding="utf-8")
        def caption(obj):
            obj["inventory"]["items"][0].update(primary_kind="speech", duration_seconds=600, duration_evidence_locator="sources/inventory.txt#L2")
            obj["records"][0].update(content_kind="captions", sha256=hashlib.sha256(source.read_bytes()).hexdigest(), content_evidence=source.read_text().splitlines()[0])
        self.edit_json(pack, "evidence/source-manifest.json", caption)
        self.assert_gate_rejects(pack, "does not cover the canonical lesson boundaries")

    def test_second_teacher_claim_needs_its_own_citation(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        chapter = pack / "chapters/01-course-book.md"
        chapter.write_text(chapter.read_text(encoding="utf-8") + "\n> [Course teaching] An additional instructor claim with no citation.\n", encoding="utf-8")
        result = run(str(BUILD), str(pack / "book-manifest.json"), "--html-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("needs its own source-map citation", result.stderr)

    def test_seal_rejects_missing_required_qa_checks(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "evidence/learning-qa.json", lambda obj: obj.update(checks=[], format_checks=[]))
        result = run(str(SEAL), str(pack))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("checks missing", result.stdout)

    def test_output_basename_cannot_escape_pack(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        self.edit_json(pack, "book-manifest.json", lambda obj: obj.update(output_basename="../../outside"))
        result = run(str(BUILD), str(pack / "book-manifest.json"), "--html-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("without path separators", result.stderr)
        self.assertFalse((pack.parent / "outside.md").exists())

    def test_user_selected_subset_can_pass_with_retained_instruction(self) -> None:
        pack = self.make_pack(self.fresh_root(), complete=True)
        (pack / "evidence/scope-instruction.md").write_text("Synthetic user instruction for this test: process only the first lesson, leave the second for later.\n", encoding="utf-8")
        def authorized_subset(obj):
            obj["inventory"]["items"].append(dict(obj["inventory"]["items"][0], item_id="u2"))
            obj["scope"]["exclusions"].append({"item_id": "u2", "reason": "The user explicitly requested lesson 1 only; lesson 2 is outside the requested learning outcome.", "authorization_locator": "evidence/scope-instruction.md#L1"})
        self.edit_json(pack, "evidence/source-manifest.json", authorized_subset)
        acquired = run(str(ACQUIRE), str(pack))
        self.assertEqual(acquired.returncode, 0, acquired.stdout)
        result = run(str(BUILD), str(pack / "book-manifest.json"), "--html-only")
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
