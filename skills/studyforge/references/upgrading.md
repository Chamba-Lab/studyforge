# Upgrading a study repository

A study repository records the StudyForge version it follows in `studyforge.toml`. When the skill is newer, the [review](../workflows/review.md) workflow brings the repository up to date with the notes below. The changelog lists commits; these notes say what each version means for a repository that already has labs.

An upgrade applies these notes; it is not a full audit. Audit every lab only when the person asks for it, or when the repository was built with 0.x.

## Procedure

1. **Read the notes of every version** newer than the repository's, oldest first. Several versions are applied in one pull request, with one commit per version that changes files.
2. **Prepare the environment, then verify.**
   - Install the repository's pinned dependencies as its `SETUP.md` says, only after checking that the interpreter and tools that run are the environment's; never install into the person's global environment (the stack notes say how, for example [Python](../stacks/python.md)). A new block may have added libraries since the environment was created.
   - Copy `scripts/verify.py` to `tools/verify.py`, run `python tools/verify.py --strict`, and fix what it reports. A failure that disappears once the environment is right came from the environment, not the repository; if learners can hit it too, write it in `docs/lessons.md` and fix the guide that should have prevented it.
   - The verifier does not depend on the shell: run it once. Commands that the upgrade adds to or changes in a README are run in every shell from `studyforge.toml`.
3. **Sort each note** into one of three kinds:
   - **Mechanical:** a file to copy or add. Do it; if it is already there, check that it matches the note and move on.
   - **Repository files** (`docs/`, CI, `SETUP.md`): update them; no lab changes.
   - **For new labs only:** nothing to change now. The next `build` follows it.
   - **For built labs:** a rule that existing labs break. Audit every lab in scope for it, as in the review workflow.
4. **Patch or rebuild, per block.**
   - **Patch** by default: the rule changes wording or structure inside labs, and the syllabus stays the same. Keep each change minimal, because learners merge it (see [learners](learners.md)).
   - **Rebuild** when the rule changes what the block teaches: topics move between labs, labs split or merge, or most of a lab's README would change. A rebuild may renumber the block only while nobody depends on it (see [layout](layout.md#ids)); otherwise keep the IDs and insert with a letter.
5. **Review each block whose labs changed with fresh eyes** ([build](../workflows/build.md#review-a-block-with-fresh-eyes)). The author of a change is the worst reader of it. A change only to dependencies, CI or the repository's own files needs no review.
6. **Record.**
   - Set `studyforge` in `studyforge.toml` to the new version.
   - Write what the upgrade found in `docs/lessons.md`, and any rebuild and its reason in `docs/decisions.md`.
   - Commit with `chore: upgrade to StudyForge <version>`.
7. **Merge only after that version is released.** A repository must never declare a version that does not exist yet. Released versions are listed at [StudyForge releases](https://github.com/Chamba-Lab/studyforge/releases), with tags `studyforge-vX.Y.Z`. If you cannot check it, say so to the person instead of assuming.

## Notes by version

### 1.5.0

- **For built labs and repository files:** none. The rules for explaining moved from [writing](writing.md) to a new [didactics](didactics.md) reference; links into `writing.md#explaining` and `writing.md#tone` now point there.
- **For new labs only:** [didactics](didactics.md) adds two sets of rules. *One idea at a time*: one idea per unit, lead with the point, show instead of listing. *Questions that make the learner think*: predictions and self-assessment ask for retrieval or reasoning, one idea per question, wrong options are real mistakes, and answers explain why. A later review may apply them to built labs when the person asks for it.
- **For new paths and syllabus refinements:** the [syllabus workflow](../workflows/syllabus.md) asks at most three questions and shows the rest as assumptions, with the path's size in labs and hours. Built labs need nothing.
- **For new paths and syllabus refinements:** before the plan is shown, the workflow checks block 1's prerequisites in one message and handles the gaps: a block `00` of 1–3 express labs without a project, another path first, or a gap written in `SYLLABUS.md` ([syllabus](syllabus.md#prerequisites)). An existing path may add a block `00` in a refinement; its IDs (`0.1`…) do not change anyone else's.

- **Repository files:** add the *Talking with the learner* section of the [AGENTS.md template](../templates/repo/AGENTS.md) to the repository's `AGENTS.md`, after *Working agreement*, with the next-step line in the language the learner chats in. In *Working agreement*, the terms-of-art rule now points to `references/didactics.md`. The learner's agent reads these rules even without the skill: answers come first and short, one question at a time, a hint before the solution, and every reply ends with the next step ([didactics](didactics.md#in-the-conversation), [learners](learners.md#helping-during-a-lab)).

### 1.4.2

- **For built labs and repository files:** none.
- When an agent verifies or upgrades a repository, it checks `sys.prefix` (or the stack's equivalent) before installing anything, and never installs into the person's global environment ([Python](../stacks/python.md)).

### 1.4.1

- **Repository files:** the dependency checklist now has gates (vulnerabilities, license, runs on the learner's environment) and signals that need judgment ([dependencies](dependencies.md#choosing-a-library)). In `docs/decisions.md`, replace a 1.4.0 per-library table with only the exceptions that need a reason. Re-run the gates rather than copying the 1.4.0 results. A weak copyleft library installed unmodified is fine and closes a license decision 1.4.0 left pending; record it.
- The procedure above now prepares the environment before verifying, keeps an upgrade to the version notes, and asks for a fresh-eyes review only when labs changed. pytest-lab's upgrade from 1.2.0 to 1.4.0, run by an agent without prior context, found these gaps.

### 1.4.0

- **For built labs:** check every library the repository pins against the new checklist in [dependencies](dependencies.md#choosing-a-library), and record the result in `docs/decisions.md` as the checklist says.
- **Mechanical:** add the ecosystem's audit tool to CI (for Python, `pip-audit` on every file that pins versions), on every change and weekly.
- For new labs: the `syllabus` self-review asks for the checklist before a library enters the plan.

### 1.3.0

- **For built labs:** none.
- `review` reads these notes instead of the changelog, and decides between patching and rebuilding with the procedure above.
- A block nobody depends on yet may be rebuilt with new IDs; record why in `docs/decisions.md`.

### 1.2.0

- **Mechanical:** copy `verify.py`. It no longer requires 💼 in challenges and explorations, nor ✔️ in explorations.
- **For built labs** ([writing](writing.md)):
  - Remove optional sections that only repeat other sections: 💼 that summarizes Concepts, ✔️ that repeats the 👀 blocks, a retrospective with generic questions.
  - One `###` per concept in 🧠 and per part of a long 🧭 Scenario; bold only for one-line notes.
  - Say each thing once: one command block when PowerShell and Bash are identical, the location check only in the first lab, and the dissection as a reference card.
  - Concepts never answer a prediction. Check Concepts, scenario tables, the dissection and the starter's imports.
  - Gloss every acronym the first time, and word the verified-answers versions line the same in every lab.
  - Each project's `BRIEF.md` lists what it needs that no lab taught ([projects](projects.md#briefmd)).
- A fresh-eyes review now closes every block. Run one for each built block after applying these notes.

### 1.1.0

- **Mechanical:** add `GLOSSARY.md` at the root from the template.
- **For built labs:**
  - Concepts go problem → idea → example → name, with the idea before the tool ([didactics](didactics.md#explaining)). Concepts written as bare definitions are rewritten.
  - Terms of art and the method's names stay in English; other section titles come from the reference table ([writing](writing.md#section-anchors)).
- **`SYLLABUS.md`:** split it into the learner's table and the build map, plan every block of the path, and keep each block on one focus ([syllabus](syllabus.md)). If a built block mixes levels, this is a rebuild, not a patch.

### 1.0.1

- **For built labs:** capitalize diagram labels as prose ([writing](writing.md#tone)), and proofread every lab once only for form ([didactics](didactics.md#tone)).

### 1.0.0

- First stable version. A repository built with 0.x is reviewed whole, lab by lab, against the current rules.
