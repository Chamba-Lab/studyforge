# Workflow: init

Create the study repository from an agreed syllabus.

Read first: [layout](../references/layout.md), [method](../references/method.md), and the notes of the chosen stacks in [stacks/](../stacks/README.md).

## Steps

1. **Check the preconditions.**
   - There is an agreed syllabus. If not, run [syllabus](syllabus.md) first.
   - The target folder is new or empty. If it already has content, stop. Explain that this version cannot adopt an existing repository, and offer a new folder next to it.
2. **Copy the templates** from [templates/repo/](../templates/repo/) and fill in every `<placeholder>`:
   - `studyforge.toml`: keep the version the template carries (it is this skill's version). Fill in the title, goal, content language, learner environment, dependency strategy and one `[[stack]]` per toolchain.
   - `AGENTS.md`: the repository's context, stack and pinned versions, its conventions, and the upgrade checklist. Write it in English, because it is read by agents.
   - `CLAUDE.md`: only `@AGENTS.md`.
   - `SYLLABUS.md`: the agreed syllabus, with the legend translated to the content language.
   - `SETUP.md`: tools, exact versions, and one command to check each, in the learner's shells.
   - `README.md`: the landing page for learners, in the content language. It covers what the path is, how to start, how to keep solutions (branch or fork), and how to read the guides.
   - `docs/decisions.md`: the dependency strategy, the pinned versions and the reason for each, and anything someone could undo without knowing why.
   - `docs/lessons.md`: an empty structure.
   - `.github/ISSUE_TEMPLATE/lab-feedback.yml`: written in the content language.
   - `GLOSSARY.md` is not copied yet. `build` adds it when the path accumulates terms of art (see [writing](../references/writing.md#explaining)).
3. **Copy the verifier.** Copy [scripts/verify.py](../scripts/verify.py) to `tools/verify.py`, unchanged.
4. **Add the stack's ignore rules** to `.gitignore` (build output, IDE files, `.env`), following the stack notes.
5. **Do not create lab folders yet.** `build` creates each one when its time comes.
6. **Check the result.**
   - Run `python tools/verify.py --structure`. With no labs yet, it checks the configuration and the files.
   - Read the README as a new learner would.
7. **Make the first commit** with the message `chore: start the study path with StudyForge <version>`.
8. **Ask before anything outward-facing.** Creating a remote repository, choosing public or private, or pushing is the person's decision. Recommend an option, then wait.

## Done when

The repository has every file from the layout, no `<placeholder>` is left, `verify.py --structure` passes, and the first commit exists.
