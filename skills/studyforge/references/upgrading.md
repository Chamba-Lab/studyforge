# Upgrading a study repository

A study repository records the StudyForge version it follows in `studyforge.toml`. When the skill is newer, the [review](../workflows/review.md) workflow brings the repository up to date with the notes below. The changelog lists commits; these notes say what each version means for a repository that already has labs.

An upgrade applies these notes; it is not a full audit. Audit every lab only when the person asks for it, or when the repository was built with 0.x.

## Procedure

1. **Read the notes of every version** newer than the repository's, oldest first. Several versions are applied in one pull request, with one commit per version that changes files.
2. **Prepare the environment, then verify.**
   - Install the repository's pinned dependencies as its `SETUP.md` says, only after checking that the interpreter and tools that run are the environment's; never install into the person's global environment (the stack notes say how, for example [Python](../stacks/python.md)). A new block may have added libraries since the environment was created.
   - Copy `scripts/verify.py` to `tools/verify.py`, run `python tools/verify.py --strict`, and fix what it reports. A failure that disappears once the environment is right came from the environment, not the repository; if learners can hit it too, write it in `docs/lessons.md` and fix the guide that should have prevented it. Do not change the person's environment to get there (their profile files, packages in a shared environment): run with an override, and write in `docs/lessons.md` how the verification was run.
   - The verifier does not depend on the shell: run it once. Commands that the upgrade adds to or changes in a README are run in every shell from `studyforge.toml`.
3. **Sort each note** into one of four kinds:
   - **Mechanical:** a file to copy or add. Do it; if it is already there, check that it matches the note and move on.
   - **Repository files** (`docs/`, CI, `SETUP.md`): update them; no lab changes.
   - **For new labs only:** nothing to change now. The next `build` follows it.
   - **For built labs:** a rule that existing labs break. Audit every lab in scope for it, as in the review workflow.
4. **Patch or rebuild, per block.**
   - **Patch** by default: the rule changes wording or structure inside labs, and the syllabus stays the same. Keep each change minimal, because learners merge it (see [learners](learners.md)).
   - **Rebuild** when the rule changes what the block teaches: topics move between labs, labs split or merge, or most of a lab's README would change. A rebuild may renumber the block only while nobody depends on it (see [layout](layout.md#ids)); otherwise keep the IDs and insert with a letter.
5. **Review each block whose labs changed with fresh eyes** ([build](../workflows/build.md#review-a-block-with-fresh-eyes)). The author of a change is the worst reader of it. A change only to dependencies, CI or the repository's own files needs no review.
6. **Record.**
   - In each version's commit, set `studyforge` in `studyforge.toml` to that version and write its lessons in `docs/lessons.md`, so every commit leaves a consistent repository.
   - Write what the upgrade found in `docs/lessons.md`, and any rebuild and its reason in `docs/decisions.md`.
   - Commit with `chore: upgrade to StudyForge <version>`.
7. **Merge only after that version is released.** A repository must never declare a version that does not exist yet. Released versions are listed at [StudyForge releases](https://github.com/Chamba-Lab/studyforge/releases), with tags `studyforge-vX.Y.Z`. Checking it is read-only and allowed (open that page, or `git ls-remote --tags https://github.com/Chamba-Lab/studyforge`); if you cannot, say so to the person instead of assuming.

## Notes by version

### 1.8.0

- **Mechanical:** copy `verify.py`. It now expects the verified answers last and warns about a lab that still has them before the self-assessment.
- **For built labs:** move the verified answers to the end of every challenge, and of every exploration that has them, so a learner reading in a terminal or a chat meets the questions before the answers. Cut the whole section, from its heading to the line before the next `## `, and paste it after the last section of the README (the 🔁 retrospective when there is one, otherwise the 🎤 self-assessment). Keep its heading text exactly as it is, so links to its anchor still work. The heading to move is the one starting with `## ✔️`, in Spanish `## ✔️ Respuestas verificadas`, in English `## ✔️ Verified answers`. In a challenge, also move the line that links to `solution/` from the end of the self-assessment to after the answers. The order of every other section does not change.

### 1.7.0

- **For new labs only:** nothing to change in the repository. A new reference, [multi-agent build](multi-agent-build.md), describes how to build a whole block with subagents (orchestrator, builder, validator, checker and learner), which model tier each role needs and the rules that keep the cost down.
- **Keep `docs/lessons.md` and the syllabus notes short.** Agents reread them every session. Rewrite `docs/lessons.md` grouped by topic, not by lab: one rule per bullet, in the imperative, with its reason; merge duplicates and delete lessons that moved into `AGENTS.md`, a tool or StudyForge. In `SYLLABUS.md`, delete the "Notes for the next labs" whose labs are built. In `docs/decisions.md`, replace superseded decisions instead of keeping both.

### 1.6.1

- **Repository files:** in *Upgrading the stack* of `AGENTS.md`, list `TUTOR.md` among the files to change, because it names the versions.
- The notes of 1.5.0 and 1.6.0 now quote the exact lines to add instead of pointing to the templates, and the procedure says that each version's commit records its own version and lessons. An upgrade from pytest-lab, run by an agent without prior context, found these gaps.

### 1.6.0

- **Repository files:**
  - Copy [TUTOR.md](../templates/repo/TUTOR.md) to the repository root and fill it in the content language: title, repository URL, goal, learner, stack and versions, the feedback form link (`<repository URL>/issues/new?template=lab-feedback.yml`) and the next-step line. Adapt *Role* and *Solutions* to how the path's labs work (for example, challenges where the learner writes the tests, or `demo/` folders).
  - In `README.md`, under *Start*, add a tip in the content language that links to `TUTOR.md` ("No coding agent? Study with Claude, ChatGPT or Gemini as your tutor").
  - In *Talking with the learner* of `AGENTS.md`, add these lines, in this order: after "One question at a time…", `- Predictions are the learner's: never give the answer to a 🔮 prediction, even after a guess; ask them to run it, then explain what they got.`; after "A hint before the solution…", `- Check understanding with one question, not a quiz.`; at the end, `` - `TUTOR.md` carries these rules for learners who study in a chat; when one of them changes, change it there too.``
  - Built labs need nothing.
- **For built labs, only in paths with a lab where the learner runs an attack** (naming an attack, such as SQL injection as the reason for query parameters, does not count): check every lab against [Teaching offensive techniques](quality.md#teaching-offensive-techniques). A lab that attacks a target it does not start, or has no line saying what makes it legal, is patched. If the path has no lab on authorization and scope, add one with a letter ID early in the path.

### 1.5.0

- **Repository files:** in `AGENTS.md`, add this section after *Working agreement*, writing the next-step line in the language the learner chats in. These are the rules the learner's agent reads even without the skill ([didactics](didactics.md#in-the-conversation), [learners](learners.md#helping-during-a-lab)):

  ```markdown
  ## Talking with the learner
  - Answer first, in a few lines. A longer explanation goes into the lab (Concepts or `CONCEPT.md`); point to it instead of pasting it.
  - One question at a time. At most three when unavoidable, numbered, each with options and a recommended answer.
  - A hint before the solution: a question, then a more concrete hint, full code only when asked. Do not edit the learner's code unless asked.
  - Say only what changes for the learner; no recap of everything you read or ran.
  - End every reply with the next step: "<Your next step: …>".
  ```

  In *Working agreement*, the terms-of-art rule now cites `references/didactics.md`; if the repository's rule cites nothing or `writing.md`, add or change the citation and keep its wording.
- **For built labs:** none. The rules for explaining moved from [writing](writing.md) to a new [didactics](didactics.md) reference; links into `writing.md#explaining` and `writing.md#tone` now point there.
- **For new labs only:** [didactics](didactics.md) adds two sets of rules. *One idea at a time*: one idea per unit, lead with the point, show instead of listing. *Questions that make the learner think*: predictions and self-assessment ask for retrieval or reasoning, one idea per question, wrong options are real mistakes, and answers explain why. A later review may apply them to built labs when the person asks for it.
- **For new paths and syllabus refinements:** the [syllabus workflow](../workflows/syllabus.md) asks at most three questions and shows the rest as assumptions, with the path's size in labs and hours. Before drafting, it checks the prerequisites of the whole path in one message and sizes each gap: a reminder with a link for "somewhat", a block `00` of 1–3 express labs without a project for small gaps, another path first for large ones ([syllabus](syllabus.md#prerequisites)). An existing path may add a block `00` in a refinement; its IDs (`0.1`…) do not change anyone else's.

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
