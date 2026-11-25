# Quality

The agent owns the quality of every lab. These rules are what "done" means. Most of them come from mistakes made while building real labs.

## The bar

1. **Job level.** The lab covers what a real project and an interview expect, not only the mechanism. When the topic depends on it, the lab includes how things run outside development mode (packaged artifact, container), typical mistakes, and what a team would do.
2. **At least one explicit trap**: a situation where the intuitive answer fails (precedence, build time vs run time, defaults, ordering…). The learner discovers it, and the README explains it afterwards.
3. **Predict before running.** Experiments ask the learner to write down a prediction first.
4. **Verified claims only.** Every command, output, error message, default value and trap quoted in the README was produced by running it on the pinned versions. Nothing comes from memory, and nothing comes only from a guide's example.
5. **Explained, not only exercised.** Every new concept is introduced with the problem it solves and an example before a task needs it (see [didactics](didactics.md#explaining)).
6. **Direct and short.** 1–2 h. Optional material goes into the "Stretch goal" section.
7. **Lean.** Every section has content of its own, and each idea is said once (see [writing](writing.md)). A section added to fill the template, or a paragraph that repeats another one, costs the learner attention for nothing.

## Definition of done

**Every lab**
- [ ] The README follows the template of its type, and every required section anchor is present, with the reference titles ([writing](writing.md)).
- [ ] Read as a learner at this point of the path: every new concept is introduced (problem, idea, example, name) before a task needs it, and every term of art and acronym is glossed the first time ([didactics](didactics.md#explaining)).
- [ ] Nothing before a prediction answers it: not Concepts, not the scenario's tables, not the dissection, not the starter.
- [ ] Every optional section has content of its own, no idea is explained twice, and long sections show their parts with `###` ([writing](writing.md#say-each-thing-once)).
- [ ] Every number and name in the README and in the starter's comments matches the files (test counts, how many tests come written, which settings each `pyproject` or build file has).
- [ ] Every command and quoted output in the README was run, in the learner's shells from `studyforge.toml`.
- [ ] Every claim was checked against [sources](sources.md), and every link opens.
- [ ] Diagrams render on GitHub ([visuals](visuals.md)).
- [ ] Proofread for form: capitalization (headings, lists, tables, diagram labels), proper nouns, accents and punctuation in the content language ([didactics](didactics.md#tone)).
- [ ] No byte-order mark, no build output, no `.env`, no secret. Wrapper scripts (`mvnw`, `gradlew`) are executable in git.
- [ ] `python tools/verify.py --lab <ID>` passes.
- [ ] `SYLLABUS.md` says `🟨 built`, and its "Notes for the next labs" are updated.
- [ ] One commit: `feat(lab-<ID>): …`.

**Challenge, in addition**
- [ ] `solution/` is green, and `starter/` is red exactly on the target tests (guards may be green).
- [ ] **Progressive check:** apply the solution of task 1 only (clean build), and its tests turn green while later tasks stay red. Repeat for each task. A task that only appears once an earlier one is solved is fine, as long as you saw it fail.
- [ ] **Targeted mutations:** for each trap and each key test, break the solution on purpose in a scratch copy and confirm the named test turns red. Restore the solution, and prove the restoration by running it green again.

**Exploration, in addition**
- [ ] The guide was run from top to bottom, in order, from a clean state. Files the guide edits are restored afterwards (`git diff` is empty).
- [ ] The cleanup section removes everything the guide created, and only that.

**Project, in addition** (see [projects](projects.md))
- [ ] `reference/` is green, `acceptance/` is green against it, and the packaged artifact was run against real dependencies.
- [ ] Every row of the "break it yourself" table in `REVIEW.md` was run, and its failure is quoted from the output (extracted, not paraphrased).

## How to verify without fooling yourself

- **Experiment in a scratch copy, never in the repository.** Copy, change one thing, use a clean build, run, read the log, restore, and prove the restoration.
- **A test that passes for the wrong reason is a bug.** Examples: negative tests that pass when the happy path is broken, two nulls compared as equal, a route that does not exist answering 404. Assert that the thing exists before asserting what it says.
- **"0 tests ran" is a failure, not a success.** A mutation that does not compile, or a starter that cannot build, produces no reports. Every experiment script prints how many tests ran.
- **A mutation that stays green is a finding.** Either the code is not needed (remove it from the solution and the task) or the tests cannot see it (say so in the README, and show the effect another way). Explain it; never ignore it.
- **First guesses about traps are often wrong.** Before building a task or a warning around a setting, remove the setting and see whether anything fails. It may already be the default.
- **Read real defaults from the artifact.** Use the library's configuration model, its signatures or its source, not a guide's example: guides lag behind versions.
- **Packaged and development modes differ.** Anything about error bodies, exposure, configuration or startup gets checked on the packaged artifact.
- **Flaky domains need repetition.** Run concurrency, timing and security tests 5 times before trusting them. Use small, fixed resources (pool sizes, threads) and wide time margins.
- **Shared state needs an explicit reset** between tests (caches, breakers, counters, fakes). When a trap breaks shared state for good, order the test classes by task and say so.
- **Wait for readiness**, such as a port or a log line, before the first call. A silent first call is a startup race, not a bug.
- **Plan the verification budget** when the infrastructure is slow. Dry-run one mutation first and read its log. Run long batteries in the background.
- **A comfortable test environment hides bugs.** An experiment script that set `PYTHONIOENCODING=utf-8` for every child process let a "no UTF-8 output" mutation pass; without it, the acceptance test caught it. Run experiments in the environment learners have, not one that is friendlier.
- **A test that compares against the same constant as the code protects nothing.** If `EXIT_ERROR = 2` changes to `1`, a test that asserts `== EXIT_ERROR` changes with it. When a value is part of the contract, write it literally in the test.
- **Your own tests fall into the traps you teach.** Data that does not separate two behaviors lets a mutant survive (ties in alphabetical order, a largest debtor who is also the first name). The mutation list catches it.

## Being a good guest on the machine

- Ask before heavy experiments (native builds, clusters, many containers) and before any automation that leaves the machine (CI workflows, pushes, publishing).
- Name what you create (containers, images, namespaces, branches) after the lab, and remove only those. Never stop processes or containers by pattern.
- Use realistic but obviously fake secrets. Secret scanners react to real-looking tokens.

## Platform notes worth knowing

- **Encodings:** never write a UTF-8 byte-order mark. Some Windows shells add one when writing files or piping text to programs.
- **Executable bits:** wrapper scripts committed from Windows may lose mode `100755`. Check with `git ls-files -s`.
- **PowerShell:** quote `-Dkey=value` arguments, use `curl.exe` (not the `curl` alias), and remember that variables are case-insensitive.
- **Long files with quotes:** write them with a file-writing tool. Multi-line shell heredocs fail silently and run nothing.

Lessons specific to a study repository go into its `docs/lessons.md`. Lessons that would help every study path should go upstream to StudyForge (see the `feedback` workflow).
