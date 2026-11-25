"""Tests for scripts/check_repo.py: GitHub heading anchors.

Run: python -m pytest tests -q
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_repo.py"
spec = importlib.util.spec_from_file_location("check_repo", SCRIPT)
check_repo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_repo)


def test_slugs_follow_github() -> None:
    assert check_repo.slug("Say each thing once") == "say-each-thing-once"
    assert check_repo.slug("Structure of `SYLLABUS.md`") == "structure-of-syllabusmd"
    assert check_repo.slug("🧠 Concepts") == "-concepts"
    assert check_repo.slug("Review a block with fresh eyes") == "review-a-block-with-fresh-eyes"
    assert check_repo.slug("Qué es") == "qué-es"


def test_anchors_ignore_fences_and_number_duplicates(tmp_path: Path) -> None:
    page = tmp_path / "page.md"
    page.write_text("# Title\n## Notes\n```\n## Not a heading\n```\n## Notes\n", encoding="utf-8")
    assert check_repo.anchors(page) == {"title", "notes", "notes-1"}
