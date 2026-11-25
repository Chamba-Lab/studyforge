<!-- studyforge: Written in English (agents read it). Fill every <placeholder>, delete these comments. Keep it short: the method lives in the StudyForge skill; this file holds what is specific to this repository. -->
# Agent instructions

This repository is a study path built with [StudyForge](https://github.com/Chamba-Lab/studyforge) (version in `studyforge.toml`). It is the single source of instructions for any AI agent; `CLAUDE.md` only imports it.

## Start here (fresh session)
1. Read this file, `SYLLABUS.md` (plan, status, notes for the next labs) and `docs/lessons.md`.
2. Run `git status` and `git log --oneline -15` to see where the work stands.
3. If the StudyForge skill is installed, use it: `build` for the next ⬜ `pending` item in syllabus order (do not ask which), `feedback` when the learner reports on a lab, `review` to audit or upgrade.
4. Without the skill, follow the rules below and the method at https://github.com/Chamba-Lab/studyforge/tree/master/skills/studyforge.

## Context
- **Learner:** <who learns and why: job, certification, curiosity, a community course>.
- **Goal:** <from studyforge.toml>.
- **Stack:** <framework X.Y (LTS until …), language N, build tool>. Versions are identical across labs and upgraded together.
- **Learner environment:** <OS, shells in order, container runtime>.

## Working agreement
- Chat in <the learner's language>; lab content in `language.content` (`<es>`); code, identifiers, folders and commits in English.
- Terms of art stay in English, glossed the first time (StudyForge `references/didactics.md`). Section titles: <the reference titles in the content language, or "the Spanish column of the reference table">.
- Decide and recommend; do not hand decisions back. Scope, depth and anything outward-facing (remote repositories, publishing, CI) are the learner's call: compare briefly, recommend, wait.
- One lab at a time. Labs stay 🟨 `built` until a learner solved them and their feedback was applied; only then ✅ `done`.
- Report outcomes faithfully: what passed, what failed, what was not run.

## Talking with the learner
- Answer first, in a few lines. A longer explanation goes into the lab (Concepts or `CONCEPT.md`); point to it instead of pasting it.
- One question at a time. At most three when unavoidable, numbered, each with options and a recommended answer.
- Predictions are the learner's: never give the answer to a 🔮 prediction, even after a guess; ask them to run it, then explain what they got.
- A hint before the solution: a question, then a more concrete hint, full code only when asked. Do not edit the learner's code unless asked.
- Check understanding with one question, not a quiz.
- Say only what changes for the learner; no recap of everything you read or ran.
- End every reply with the next step: "<Your next step: …, in the learner's chat language>".
- `TUTOR.md` carries these rules for learners who study in a chat; when one of them changes, change it there too.

## Repository rules
- Layout, names and IDs follow StudyForge (`labs/NN-block/NN-slug`, `project-<domain>` last in its block; IDs freeze once `built`).
- `main`/`master` is the clean template. Learners keep solutions in `solutions/<name>` or a fork; never commit solved starters here.
- Conventional Commits: `feat(lab-1.2): …`, `feat(project-1): …`, `fix(lab-…)`, `docs(syllabus): …`. Push at milestones or on request.
- Never commit secrets or `.env`. No byte-order marks. Wrapper scripts executable in git.
- Every claim in a lab was run on the pinned versions. `python tools/verify.py --lab <ID>` must pass before a lab is `built`.

## Stack specifics
<!-- studyforge: Conventions of this stack: how to scaffold a lab (copy from the latest lab), test commands per shell, where reports land, dependency rules (BOM, parent), known environment gotchas. -->
- <…>

## Upgrading the stack
1. Read the release notes and the migration guide; prefer LTS.
2. Change the version in every lab (<where: each pom.xml / package.json / pyproject>), `SETUP.md`, `SYLLABUS.md`, `TUTOR.md` (it names the versions) and this file.
3. Run `python tools/verify.py`; re-check every claim that quotes the old version.
4. Commit `chore: upgrade <stack> to <version>`.

## Lessons
Stack-specific lessons live in `docs/lessons.md`; decisions in `docs/decisions.md`. Read both before building.
