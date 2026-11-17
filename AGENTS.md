# Agent instructions (StudyForge repository)

This repository is the StudyForge framework: an Agent Skill, plus a Claude Code plugin wrapper around it, for building hands-on study paths. Any person or agent changing it reads this file first. `CLAUDE.md` only imports it.

## Map

| Path | What it is |
|---|---|
| `skills/studyforge/` | **The product.** One self-contained Agent Skill: `SKILL.md` (router), `workflows/`, `references/` (the method), `templates/`, `stacks/`, `scripts/verify.py` |
| `.claude-plugin/` | Plugin manifest and marketplace for Claude Code (the plugin root is the repository root) |
| `docs/decisions.md` | Why the framework is the way it is; read it before undoing anything |
| `docs/visuals.md` | Gallery of every recommended visual, rendered; also the proof that GitHub renders them |
| `examples/` | The showcase study path (arrives before 1.0.0) |
| `scripts/check_repo.py`, `tests/` | Repository checks and tests of the verifier; CI runs both |

## Rules

- **English** for everything in the framework (it is read by agents and people worldwide). `README.es.md` mirrors `README.md` for Spanish speakers; update both in the same commit.
- **The skill folder is self-contained.** Everything it needs lives under `skills/studyforge/`, with relative links, so copying that one folder installs it anywhere. Nothing there may depend on files outside it (links to the GitHub repository are fine).
- **Write workflows tool-agnostic.** Say what to do ("run the tests", "use a scratch copy"), not which tool of which agent to call. Optional extras are phrased "if your agent offers…".
- **One source of truth.** The method lives in `references/`; the READMEs summarize and link, they do not duplicate rules.
- **Keys are an interface.** Status, topic kind and lab type keys, section anchors, folder names and `studyforge.toml` fields are read by workflows and `verify.py`. Changing one is a breaking change (major version) and needs migration notes.
- **The verifier stays stdlib-only Python 3.11+.** Every change to it gets a test in `tests/test_verify.py`.
- **Starting values are labeled.** Stack notes not yet proven by a pilot say so; prove them before removing the label.

## Versions and releases

- [Semantic Versioning](https://semver.org). MAJOR: breaks existing study repositories (keys, layout, required files). MINOR: additive (a workflow, a stack, a rule). PATCH: wording, templates, fixes. While in `0.x`, breaking changes bump the minor version.
- **Never edit version numbers by hand.** release-please bumps `.claude-plugin/plugin.json`, the `metadata.version` line of `SKILL.md` and the `studyforge.toml` template (lines marked `x-release-please-version`), writes `CHANGELOG.md` and tags the release when its pull request is merged.
- [Conventional Commits](https://www.conventionalcommits.org) in English, imperative: `feat:`, `fix:`, `docs:`, `chore:`, `ci:`, `test:`, `refactor:`. A breaking change says `feat!:` or has a `BREAKING CHANGE:` footer.
- For now changes go straight to `master` (single maintainer); the release pull request opened by release-please is the review point before each version. No AI attribution lines in commits or pull requests.

## Before pushing

```bash
python scripts/check_repo.py
python -m pytest tests -q
```

Both must pass. A change to a workflow or a reference is read once more as an agent would read it: is every step actionable without guessing?

## Lessons from study repositories

Lessons proposed upstream from study repositories (issues with the "Lesson or improvement" template) land in `references/quality.md`, a template, a workflow or a stack note, whichever a builder would read at the moment the lesson matters.
