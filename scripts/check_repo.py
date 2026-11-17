#!/usr/bin/env python3
"""Checks this repository (not a study repository): skill frontmatter, manifests,
version consistency and relative Markdown links. Stdlib only, Python 3.11+.

Usage: python scripts/check_repo.py
"""

from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "studyforge"
problems: list[str] = []


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        problems.append(f"{path.relative_to(ROOT)}: no YAML frontmatter")
        return {}
    data: dict[str, str] = {}
    parent = ""
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        indented = line.startswith("  ")
        key, _, value = line.strip().partition(":")
        value = re.sub(r"\s+#.*$", "", value.strip()).strip('"')
        if not indented:
            parent = key if not value else ""
            data[key] = value
        elif parent:
            data[f"{parent}.{key}"] = value
    return data


def check_skill() -> str | None:
    meta = frontmatter(SKILL / "SKILL.md")
    name, description = meta.get("name", ""), meta.get("description", "")
    if name != SKILL.name:
        problems.append(f"SKILL.md: name '{name}' must match its folder '{SKILL.name}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        problems.append("SKILL.md: name must be lowercase letters, digits and hyphens, <= 64")
    if not description or len(description) > 1024:
        problems.append(f"SKILL.md: description must be 1-1024 characters ({len(description)})")
    if len(meta.get("compatibility", "")) > 500:
        problems.append("SKILL.md: compatibility must be <= 500 characters")
    return meta.get("metadata.version")


def check_versions(skill_version: str | None) -> None:
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    json.loads((ROOT / "release-please-config.json").read_text(encoding="utf-8"))
    json.loads((ROOT / ".release-please-manifest.json").read_text(encoding="utf-8"))
    template = tomllib.loads(
        (SKILL / "templates" / "repo" / "studyforge.toml").read_text(encoding="utf-8"))
    versions = {
        ".claude-plugin/plugin.json": plugin.get("version"),
        "skills/studyforge/SKILL.md (metadata.version)": skill_version,
        "templates/repo/studyforge.toml": template.get("studyforge"),
    }
    if len(set(versions.values())) != 1:
        listed = ", ".join(f"{k} = {v}" for k, v in versions.items())
        problems.append(f"versions differ: {listed}")


LINK = re.compile(r"\]\(([^)\s]+)\)")


def check_links() -> None:
    for md in ROOT.rglob("*.md"):
        relative = md.relative_to(ROOT).as_posix()
        if relative.startswith(("skills/studyforge/templates/", ".git/")) or "CHANGELOG" in relative:
            continue
        in_fence = False
        for number, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for target in LINK.findall(line):
                if target.startswith(("http://", "https://", "mailto:", "#", "<")):
                    continue
                if target.startswith("labs/"):  # example paths of a study repository
                    continue
                path = (md.parent / target.split("#")[0]).resolve()
                if not path.exists():
                    problems.append(f"{relative}:{number}: broken link {target}")


def check_bom() -> None:
    for file in ROOT.rglob("*"):
        if ".git" in file.parts or not file.is_file():
            continue
        if file.suffix in {".md", ".py", ".json", ".toml", ".yml", ".yaml"}:
            if file.read_bytes()[:3] == b"\xef\xbb\xbf":
                problems.append(f"{file.relative_to(ROOT)}: UTF-8 byte-order mark")


def main() -> int:
    check_versions(check_skill())
    check_links()
    check_bom()
    for message in problems:
        print(f"[fail] {message}")
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
