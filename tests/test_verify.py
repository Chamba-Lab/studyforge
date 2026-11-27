"""Tests for skills/studyforge/scripts/verify.py against a small study repository.

Run: python -m pytest tests -q   (needs pytest; the labs inside the fixture use it too)
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

VERIFY = Path(__file__).resolve().parent.parent / "skills" / "studyforge" / "scripts" / "verify.py"

CONFIG = """studyforge = "0.1.0"
[language]
content = "es"
[learner]
os = "linux"
[dependencies]
strategy = "independent"
[[stack]]
id = "python"
detect = "pyproject.toml"
command = "{python} -m pytest -q -p no:cacheprovider --junitxml=.reports/junit.xml"
reports = ".reports/junit.xml"
timeout = 120
"""
CHALLENGE_README = "\n".join([
    "# 🧩 1.1 · Suma", "## 🎯 Objetivos", "## 💡 Por qué importa", "## 📍 Dónde",
    "## 🧠 Conceptos", "## 📚 Documentación", "## 🧭 Escenario", "## ✅ Tareas",
    "## 💼 En proyectos reales", "## 🎤 Autoevaluación", "## ✔️ Respuestas verificadas", ""])
PYPROJECT = '[project]\nname = "x"\nversion = "0"\n[tool.pytest.ini_options]\npythonpath = ["."]\n'
TESTS = "from calc import add\n\ndef test_add():\n    assert add(2, 3) == 5\n\ndef test_guard():\n    assert True\n"
LAB = "labs/01-basics/01-sum"


def write(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    python = sys.executable.replace("\\", "/")
    write(tmp_path, "studyforge.toml", CONFIG.format(python=f'"{python}"'.strip('"')))
    for name in ("AGENTS.md", "README.md", "SETUP.md", "docs/decisions.md", "docs/lessons.md"):
        write(tmp_path, name, "# x\n")
    write(tmp_path, "CLAUDE.md", "@AGENTS.md\n")
    write(tmp_path, "SYLLABUS.md", "| 1.1 | a |\n| 1.2 | b |\n")
    write(tmp_path, f"{LAB}/README.md", CHALLENGE_README)
    for variant, body in (("solution", "return a + b"), ("starter", "raise NotImplementedError('TODO')")):
        write(tmp_path, f"{LAB}/{variant}/pyproject.toml", PYPROJECT)
        write(tmp_path, f"{LAB}/{variant}/calc.py", f"def add(a, b):\n    {body}\n")
        write(tmp_path, f"{LAB}/{variant}/tests/test_calc.py", TESTS)
    write(tmp_path, "labs/01-basics/02-mindset/README.md",
          "# 💭 1.2 · M\n## 🎯 O\n## 💡 P\n## 🧠 C\n## 📚 D\n## 🎤 A\n")
    write(tmp_path, "labs/01-basics/02-mindset/CONCEPT.md", "# C\n")
    return tmp_path


def verify(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VERIFY), *args], cwd=root,
                          capture_output=True, text=True, encoding="utf-8")


def test_a_correct_repository_passes(repo: Path) -> None:
    result = verify(repo)
    assert result.returncode == 0, result.stdout
    assert "solution green (2 tests, 0 failing)" in result.stdout
    assert "starter red (2 tests, 1 failing)" in result.stdout


def test_a_starter_that_passes_is_a_problem(repo: Path) -> None:
    write(repo, f"{LAB}/starter/calc.py", "def add(a, b):\n    return a + b\n")
    result = verify(repo, "--lab", "1.1")
    assert result.returncode == 1
    assert "expected red" in result.stdout


def test_a_starter_that_does_not_import_is_flagged(repo: Path) -> None:
    write(repo, f"{LAB}/starter/calc.py", "def add(a, b:\n")
    result = verify(repo, "--lab", "1.1")
    assert "error(s), not assertion failures" in result.stdout


def test_a_starter_with_fewer_cases_than_the_solution_is_fine(repo: Path) -> None:
    # Parametrization labs: the solution legitimately has more test cases.
    extra = "\n\nimport pytest\n\n@pytest.mark.parametrize('n', [1, 2, 3])\ndef test_more(n):\n    assert add(n, 0) == n\n"
    (repo / f"{LAB}/solution/tests/test_calc.py").write_text(TESTS + extra, encoding="utf-8")
    result = verify(repo, "--lab", "1.1")
    assert result.returncode == 0, result.stdout
    assert "[warn]" not in result.stdout


def test_answers_before_self_assessment_warn(repo: Path) -> None:
    # Since 1.8 the verified answers come last, after self-assessment and the retrospective,
    # because a reader in a terminal or a chat sees no <details> fold.
    write(repo, f"{LAB}/README.md", CHALLENGE_README.replace(
        "## 🎤 Autoevaluación\n## ✔️ Respuestas verificadas\n",
        "## ✔️ Respuestas verificadas\n## 🎤 Autoevaluación\n"))
    result = verify(repo, "--structure")
    assert "sections are not in the standard order" in result.stdout


def test_sections_that_add_nothing_can_be_left_out(repo: Path) -> None:
    # "In real projects" is optional in a challenge, and an exploration keeps its answers
    # in the "What you should see" blocks, so neither section is forced.
    write(repo, f"{LAB}/README.md", CHALLENGE_README.replace("## 💼 En proyectos reales\n", ""))
    write(repo, "labs/01-basics/03-tour/README.md", "\n".join([
        "# 🔭 1.3 · T", "## 🎯 O", "## 💡 P", "## 📍 D", "## 🧠 C", "## 📚 D", "## 🧭 E",
        "## 🧪 X", "## 🎤 A", ""]))
    (repo / "labs/01-basics/03-tour/demo").mkdir(parents=True)
    write(repo, "SYLLABUS.md", "| 1.1 | a |\n| 1.2 | b |\n| 1.3 | c |\n")
    result = verify(repo, "--structure", "--strict")
    assert result.returncode == 0, result.stdout


def test_structure_problems_are_reported(repo: Path) -> None:
    write(repo, "labs/01-basics/02-mindset/README.md", "# 💭 1.2 · M\n## 🎯 O\n")
    (repo / "labs/01-basics/3-Bad_Name").mkdir()
    (repo / f"{LAB}/solution/bom.py").write_bytes(b"\xef\xbb\xbfx = 1\n")
    result = verify(repo, "--structure")
    assert result.returncode == 1
    assert "missing the section anchored '## 🎤" in result.stdout
    assert "a lab folder must be" in result.stdout
    assert "byte-order mark" in result.stdout


def test_a_block_00_of_fundamentals_needs_no_project(repo: Path) -> None:
    # Prerequisites: block 00 holds 1-3 express labs and, unlike other blocks, no project.
    write(repo, "labs/00-foundations/01-terminal/README.md",
          "# 💭 0.1 · T\n## 🎯 O\n## 💡 P\n## 🧠 C\n## 📚 D\n## 🎤 A\n")
    write(repo, "labs/00-foundations/01-terminal/CONCEPT.md", "# C\n")
    write(repo, "SYLLABUS.md", "| 0.1 | t |\n| 1.1 | a |\n| 1.2 | b |\n")
    result = verify(repo, "--structure", "--strict")
    assert result.returncode == 0, result.stdout
    assert "0.1    concept" in verify(repo, "--list").stdout


def test_list_shows_ids_and_types(repo: Path) -> None:
    result = verify(repo, "--list")
    assert "1.1    challenge" in result.stdout
    assert "1.2    concept" in result.stdout


def test_without_configuration_it_cannot_run(tmp_path: Path) -> None:
    copy = tmp_path / "verify.py"
    shutil.copy(VERIFY, copy)
    result = subprocess.run([sys.executable, str(copy)], cwd=tmp_path,
                            capture_output=True, text=True, encoding="utf-8")
    assert result.returncode == 2
