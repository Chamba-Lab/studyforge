#!/usr/bin/env python3
"""StudyForge verifier: checks a study repository and runs its labs.

Usage (from anywhere inside the study repository):
  python tools/verify.py                 structure + run every lab
  python tools/verify.py --structure     structure only, nothing is run
  python tools/verify.py --lab 1.2       one lab, by ID (1.2, 1.2b, 1.P) or by path
  python tools/verify.py --list          list the labs that were found

What "passes" means:
  challenge    solution/ exits 0 and starter/ exits non-zero (red on its tests)
  exploration  demo/ builds when a stack matches it; the guide itself is run by hand
  concept      structure only
  project      reference/ exits 0; acceptance/ is run as the project README says

Needs Python 3.11+ and nothing else. Exit code: 0 = all good, 1 = problems found,
2 = cannot run (wrong Python, no studyforge.toml).
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

if sys.version_info < (3, 11):
    print("verify.py needs Python 3.11 or newer (it reads TOML with tomllib).")
    sys.exit(2)

import tomllib  # noqa: E402  (after the version check on purpose)
import xml.etree.ElementTree as ET  # noqa: E402

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

SLUG = r"[a-z0-9]+(?:-[a-z0-9]+){0,3}"
BLOCK_RE = re.compile(rf"^(\d{{2}})-({SLUG})$")
LAB_RE = re.compile(rf"^(\d{{2}})([b-z]?)-({SLUG})$")
PROJECT_RE = re.compile(rf"^project-({SLUG})$")

VS16 = "️"  # emoji variation selector, ignored when comparing anchors
TYPE_EMOJI = {"challenge": "🧩", "exploration": "🔭", "concept": "💭", "project": "🏗"}
ANCHOR_ORDER = ["🎯", "💡", "📍", "🧠", "📚", "🧭", "✅", "🧪", "🛣", "🔍", "👀",
                "💼", "🧹", "🚀", "🆘", "✔", "🎤", "🔁"]
REQUIRED_ANCHORS = {  # sections every lab of the type needs; the rest appear only when they add something
    "challenge": ["🎯", "💡", "📍", "🧠", "📚", "🧭", "✅", "✔", "🎤"],
    "exploration": ["🎯", "💡", "📍", "🧠", "📚", "🧭", "🧪", "🎤"],
    "concept": ["🎯", "💡", "🧠", "📚", "🎤"],
    "project": ["🎯", "📍", "🛣"],
}
ROOT_FILES = ["studyforge.toml", "AGENTS.md", "CLAUDE.md", "README.md", "SETUP.md",
              "SYLLABUS.md", "docs/decisions.md", "docs/lessons.md"]
SKIP_DIRS = {".git", "target", "build", "dist", "out", "node_modules", ".venv", "venv",
             "__pycache__", ".idea", ".vscode", ".gradle", ".mvn", ".pytest_cache",
             ".ipynb_checkpoints", ".next", ".turbo", "coverage"}
TEXT_EXT = {".md", ".java", ".kt", ".kts", ".xml", ".json", ".py", ".js", ".mjs", ".cjs",
            ".ts", ".tsx", ".jsx", ".toml", ".yml", ".yaml", ".properties", ".sql", ".sh",
            ".gradle", ".txt", ".html", ".css", ".ipynb", ".go", ".rs", ".cs", ".proto",
            ".tape", ".env.example", ".cfg", ".ini"}
WRAPPERS = {"mvnw", "gradlew"}
LEFTOVER = "<!-- studyforge:"


@dataclass
class Lab:
    id: str
    kind: str
    path: Path
    problems: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    results: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------- setup

def find_root(start: Path) -> Path | None:
    for folder in [start, *start.parents]:
        if (folder / "studyforge.toml").is_file():
            return folder
    return None


def load_config(root: Path, problems: list[str], warnings: list[str]) -> dict:
    try:
        config = tomllib.loads((root / "studyforge.toml").read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as error:
        problems.append(f"studyforge.toml is not valid TOML: {error}")
        return {}
    version = config.get("studyforge")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        problems.append('studyforge.toml: "studyforge" must be the framework version, like "0.1.0"')
    if not config.get("language", {}).get("content"):
        problems.append("studyforge.toml: [language] content is missing")
    os_name = config.get("learner", {}).get("os")
    if os_name not in {"windows", "macos", "linux"}:
        warnings.append("studyforge.toml: [learner] os should be windows, macos or linux")
    strategy = config.get("dependencies", {}).get("strategy")
    if strategy not in {"shared-parent", "independent", "per-block"}:
        warnings.append("studyforge.toml: [dependencies] strategy should be "
                        "shared-parent, independent or per-block")
    stacks = config.get("stack", [])
    if not stacks:
        warnings.append("studyforge.toml: no [[stack]] tables, so no lab can be run")
    for index, stack in enumerate(stacks, 1):
        for key in ("id", "detect", "command"):
            if not stack.get(key):
                problems.append(f"studyforge.toml: [[stack]] #{index} needs '{key}'")
    return config


# ------------------------------------------------------------------- discovery

def discover(root: Path, problems: list[str]) -> list[Lab]:
    labs_dir = root / "labs"
    if not labs_dir.is_dir():
        return []
    labs: list[Lab] = []
    seen_blocks: dict[str, str] = {}
    for block in sorted(p for p in labs_dir.iterdir() if p.is_dir()):
        match = BLOCK_RE.match(block.name)
        if not match:
            problems.append(f"labs/{block.name}: a block folder must be NN-<slug> "
                            "(two digits, kebab-case, ASCII, at most four words)")
            continue
        number = match.group(1)
        if number in seen_blocks:
            problems.append(f"labs/{block.name}: block number {number} is also used by "
                            f"labs/{seen_blocks[number]}")
        seen_blocks[number] = block.name
        block_id = str(int(number))
        seen_labs: dict[str, str] = {}
        projects = 0
        for item in sorted(p for p in block.iterdir() if p.is_dir()):
            if item.name == "assets":
                continue
            lab_match = LAB_RE.match(item.name)
            project_match = PROJECT_RE.match(item.name)
            if lab_match:
                key = lab_match.group(1) + lab_match.group(2)
                if key in seen_labs:
                    problems.append(f"{rel(root, item)}: lab number {key} is also used by "
                                    f"{seen_labs[key]}")
                seen_labs[key] = item.name
                lab_id = f"{block_id}.{int(lab_match.group(1))}{lab_match.group(2)}"
                labs.append(Lab(lab_id, detect_kind(item), item))
            elif project_match:
                projects += 1
                labs.append(Lab(f"{block_id}.P", "project", item))
            else:
                problems.append(f"{rel(root, item)}: a lab folder must be NN-<slug>, "
                                "NNx-<slug> or project-<slug>")
        if projects > 1:
            problems.append(f"labs/{block.name}: one project per block (found {projects})")
    return labs


def detect_kind(path: Path) -> str:
    if (path / "starter").is_dir() or (path / "solution").is_dir():
        return "challenge"
    if (path / "demo").is_dir():
        return "exploration"
    return "concept"


# ------------------------------------------------------------------- structure

def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def anchors_of(readme: Path) -> tuple[str | None, list[str]]:
    title, anchors = None, []
    for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# ") and title is None:
            parts = line[2:].split()
            title = parts[0].replace(VS16, "") if parts else ""
        elif line.startswith("## "):
            parts = line[3:].split()
            if parts:
                anchors.append(parts[0].replace(VS16, ""))
    return title, anchors


def check_structure(root: Path, lab: Lab) -> None:
    where = rel(root, lab.path)
    required_files = {
        "challenge": ["README.md"],
        "exploration": ["README.md"],
        "concept": ["README.md", "CONCEPT.md"],
        "project": ["README.md", "BRIEF.md", "REVIEW.md"],
    }[lab.kind]
    for name in required_files:
        if not (lab.path / name).is_file():
            lab.problems.append(f"{where}: missing {name}")
    if lab.kind == "challenge":
        for variant in ("starter", "solution"):
            if not (lab.path / variant).is_dir():
                lab.problems.append(f"{where}: a challenge needs {variant}/")
    if lab.kind == "project":
        if not (lab.path / "reference").is_dir():
            lab.problems.append(f"{where}: a project needs reference/")
        if not (lab.path / "acceptance").is_dir():
            lab.warnings.append(f"{where}: no acceptance/ (BRIEF.md must say why)")

    readme = lab.path / "README.md"
    if readme.is_file():
        title, anchors = anchors_of(readme)
        expected = TYPE_EMOJI[lab.kind]
        if title != expected:
            lab.warnings.append(f"{where}/README.md: the title should start with {expected}")
        for anchor in REQUIRED_ANCHORS[lab.kind]:
            if anchor not in anchors:
                lab.problems.append(f"{where}/README.md: missing the section anchored "
                                    f"'## {anchor} …'")
        positions = [ANCHOR_ORDER.index(a) for a in anchors if a in ANCHOR_ORDER]
        if positions != sorted(positions):
            lab.warnings.append(f"{where}/README.md: sections are not in the standard order "
                                "(see references/writing.md)")

    for doc in ("README.md", "CONCEPT.md", "BRIEF.md", "REVIEW.md"):
        file = lab.path / doc
        if file.is_file() and LEFTOVER in file.read_text(encoding="utf-8", errors="replace"):
            lab.warnings.append(f"{where}/{doc}: template instructions are still there "
                                f"({LEFTOVER} … -->)")

    check_files(root, lab.path, lab.problems)


def walk(folder: Path):
    for current, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            yield Path(current) / name


def check_files(root: Path, folder: Path, problems: list[str]) -> None:
    for file in walk(folder):
        name = file.name
        if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
            problems.append(f"{rel(root, file)}: environment files are never committed")
        suffix = ".env.example" if name == ".env.example" else file.suffix.lower()
        if suffix in TEXT_EXT:
            with file.open("rb") as handle:
                if handle.read(3) == b"\xef\xbb\xbf":
                    problems.append(f"{rel(root, file)}: starts with a UTF-8 byte-order mark")
        if name in WRAPPERS:
            mode = git_mode(root, file)
            if mode and mode != "100755":
                problems.append(f"{rel(root, file)}: not executable in git (mode {mode}); "
                                f"run: git update-index --chmod=+x {rel(root, file)}")


def git_mode(root: Path, file: Path) -> str | None:
    try:
        out = subprocess.run(["git", "ls-files", "-s", "--", rel(root, file)], cwd=root,
                             capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.split()[0] if out.returncode == 0 and out.stdout.strip() else None


def check_root(root: Path, problems: list[str], warnings: list[str], labs: list[Lab]) -> None:
    for name in ROOT_FILES:
        if not (root / name).is_file():
            problems.append(f"missing {name}")
    claude = root / "CLAUDE.md"
    if claude.is_file() and "@AGENTS.md" not in claude.read_text(encoding="utf-8"):
        warnings.append("CLAUDE.md should only import AGENTS.md (@AGENTS.md)")
    for name in ("AGENTS.md", "SYLLABUS.md", "SETUP.md", "README.md"):
        file = root / name
        if file.is_file() and LEFTOVER in file.read_text(encoding="utf-8", errors="replace"):
            warnings.append(f"{name}: template instructions are still there ({LEFTOVER} … -->)")
    syllabus = root / "SYLLABUS.md"
    if syllabus.is_file():
        text = syllabus.read_text(encoding="utf-8", errors="replace")
        for lab in labs:
            pattern = rf"(?<![\w.]){re.escape(lab.id)}(?![\w.])"
            if not re.search(pattern, text):
                warnings.append(f"SYLLABUS.md does not mention {lab.id} ({rel(root, lab.path)})")
    for folder in ("docs", "tools"):
        if (root / folder).is_dir():
            check_files(root, root / folder, problems)
    for name in ROOT_FILES:
        file = root / name
        if file.is_file():
            with file.open("rb") as handle:
                if handle.read(3) == b"\xef\xbb\xbf":
                    problems.append(f"{name}: starts with a UTF-8 byte-order mark")


# ------------------------------------------------------------------------- run

def stack_for(variant: Path, stacks: list[dict]) -> dict | None:
    for stack in stacks:
        detect = stack.get("detect")
        if detect and any(variant.glob(detect)):
            return stack
    return None


def junit_totals(variant: Path, pattern: str, since: float) -> tuple[int, int, int] | None:
    """(tests, assertion failures, errors) from the JUnit XML reports written by this run."""
    tests = failures = errors = 0
    found = False
    for report in variant.glob(pattern):
        if report.stat().st_mtime < since:
            continue
        try:
            tree = ET.parse(report)
        except ET.ParseError:
            continue
        found = True
        for suite in tree.getroot().iter("testsuite"):
            tests += int(suite.get("tests", 0))
            failures += int(suite.get("failures", 0))
            errors += int(suite.get("errors", 0))
    return (tests, failures, errors) if found else None


def run_variant(root: Path, lab: Lab, name: str, stacks: list[dict], logs: Path,
                expect_green: bool) -> None:
    variant = lab.path / name
    where = f"{rel(root, lab.path)}/{name}"
    stack = stack_for(variant, stacks)
    if stack is None:
        lab.problems.append(f"{where}: no [[stack]] in studyforge.toml matches it "
                            "(check 'detect')")
        return
    command = stack.get("command_windows") if os.name == "nt" else None
    command = command or stack["command"]
    log = logs / f"{lab.id}-{name}.log"
    started = time.time() - 1
    try:
        with log.open("w", encoding="utf-8", errors="replace") as out:
            done = subprocess.run(command, shell=True, cwd=variant, stdout=out,
                                  stderr=subprocess.STDOUT, timeout=stack.get("timeout", 900))
        code = done.returncode
    except subprocess.TimeoutExpired:
        lab.problems.append(f"{where}: timed out after {stack.get('timeout', 900)} s "
                            f"(log: {log})")
        return
    totals = junit_totals(variant, stack["reports"], started) if stack.get("reports") else None
    counted = f" ({totals[0]} tests, {totals[1] + totals[2]} failing)" if totals else ""
    if expect_green:
        if code != 0:
            lab.problems.append(f"{where}: expected green, exit code {code}{counted} (log: {log})")
        elif stack.get("reports") and (totals is None or totals[0] == 0):
            lab.problems.append(f"{where}: exit code 0 but 0 tests ran (log: {log})")
        else:
            lab.results.append(f"{name} green{counted}")
    else:
        if code == 0:
            lab.problems.append(f"{where}: expected red (failing target tests), but it passed"
                                f"{counted} (log: {log})")
        elif stack.get("reports") and (totals is None or totals[0] == 0):
            lab.problems.append(f"{where}: red, but 0 tests ran: it probably does not build, "
                                f"so its tests never run (log: {log})")
        elif totals and totals[1] + totals[2] == 0:
            lab.problems.append(f"{where}: exit code {code} with no failing test: a build or "
                                f"setup error, not a red test (log: {log})")
        else:
            lab.results.append(f"{name} red{counted}")
            if totals and totals[2]:
                lab.warnings.append(
                    f"{where}: {totals[2]} error(s), not assertion failures. A module that does "
                    "not import or a test that cannot be set up is red for the wrong reason, "
                    f"unless the lab means it (log: {log})")


def run_lab(root: Path, lab: Lab, stacks: list[dict], logs: Path) -> None:
    if lab.kind == "challenge":
        if (lab.path / "solution").is_dir():
            run_variant(root, lab, "solution", stacks, logs, expect_green=True)
        if (lab.path / "starter").is_dir():
            run_variant(root, lab, "starter", stacks, logs, expect_green=False)
    elif lab.kind == "exploration":
        if stack_for(lab.path / "demo", stacks):
            run_variant(root, lab, "demo", stacks, logs, expect_green=True)
        else:
            lab.results.append("demo has no build; run the guide by hand")
    elif lab.kind == "project":
        if (lab.path / "reference").is_dir():
            run_variant(root, lab, "reference", stacks, logs, expect_green=True)
        if (lab.path / "acceptance").is_dir():
            lab.results.append("acceptance: run it against reference/ as the README says")
    else:
        lab.results.append("concept: structure only")


# ------------------------------------------------------------------------ main

def select(labs: list[Lab], wanted: str, root: Path) -> list[Lab]:
    wanted_path = (Path.cwd() / wanted).resolve()
    chosen = [lab for lab in labs
              if lab.id.lower() == wanted.lower() or lab.path.resolve() == wanted_path]
    if not chosen:
        known = ", ".join(lab.id for lab in labs) or "none"
        print(f"No lab matches '{wanted}'. Labs found: {known}")
        sys.exit(1)
    return chosen


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a StudyForge study repository.")
    parser.add_argument("--structure", action="store_true", help="check structure only")
    parser.add_argument("--lab", help="one lab: an ID (1.2, 1.2b, 1.P) or a path")
    parser.add_argument("--list", action="store_true", help="list the labs found")
    parser.add_argument("--strict", action="store_true", help="treat warnings as problems")
    args = parser.parse_args()

    root = find_root(Path.cwd())
    if root is None:
        root = find_root(Path(__file__).resolve().parent)
    if root is None:
        print("No studyforge.toml found here or in any parent folder.")
        return 2

    problems: list[str] = []
    warnings: list[str] = []
    config = load_config(root, problems, warnings)
    labs = discover(root, problems)

    if args.list:
        for lab in labs:
            print(f"{lab.id:<6} {lab.kind:<12} {rel(root, lab.path)}")
        return 0

    check_root(root, problems, warnings, labs)
    selected = select(labs, args.lab, root) if args.lab else labs
    logs = Path(tempfile.mkdtemp(prefix="studyforge-verify-"))

    print(f"StudyForge verify · {root.name} · {len(selected)} lab(s)"
          f"{' · structure only' if args.structure else ''}")
    for lab in selected:
        check_structure(root, lab)
        if not args.structure:
            print(f"  running {lab.id} …", flush=True)
            run_lab(root, lab, config.get("stack", []), logs)

    print()
    for message in problems:
        print(f"[fail] {message}")
    for message in warnings:
        print(f"[warn] {message}")
    for lab in selected:
        status = "fail" if lab.problems else ("warn" if lab.warnings else "ok")
        detail = " · ".join(lab.results)
        print(f"[{status}] {lab.id:<6} {lab.kind:<12} {rel(root, lab.path)}"
              f"{'  ' + detail if detail else ''}")
        for message in lab.problems:
            print(f"         [fail] {message}")
        for message in lab.warnings:
            print(f"         [warn] {message}")

    failures = len(problems) + sum(len(lab.problems) for lab in selected)
    warns = len(warnings) + sum(len(lab.warnings) for lab in selected)
    print(f"\n{failures} problem(s), {warns} warning(s). Logs: {logs}")
    if failures or (args.strict and warns):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
