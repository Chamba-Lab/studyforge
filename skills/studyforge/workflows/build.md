# Workflow: build

Build the next lab or project in the syllabus, verify it and commit it.

Read first: the study repository's `AGENTS.md`, `SYLLABUS.md` and `docs/lessons.md`. Then read [lab-types](../references/lab-types.md) or [projects](../references/projects.md), and [quality](../references/quality.md), [writing](../references/writing.md) and [visuals](../references/visuals.md).

## Choose what to build

Take the **first `⬜ pending` row in syllabus order**, unless the person names another one. Do not ask which one: the syllabus order is the plan. Build one item at a time.

Run `git status` and `git log --oneline -15` to see where the work stands. Before starting, finish or discard any half-built lab.

## Build a lab

1. **Design it.** Write down, for yourself:
   - the learning objectives (3–6);
   - the new concepts, and for each one the problem it solves, a minimal example and the term of art (see [writing](../references/writing.md#explaining));
   - the bridge from the previous lab;
   - the trap or traps;
   - the starting point;
   - the tasks or experiments, and the test or observation that proves each one.

   Check ownership: what this lab owns, and what it only references. Read the "Notes for the next labs" in the syllabus.
2. **Research** the exact APIs and settings, following [sources](../references/sources.md). Look up anything you would otherwise write from memory.
3. **Explore in a scratch copy.** Build the smallest version, run it, and break it on purpose. Confirm or discard each planned trap by running it (first guesses are often wrong). Measure what you will quote.
4. **Build it by type.**
   - **Challenge:**
     1. Write `solution/` first.
     2. Write the tests, which are the acceptance criteria.
     3. Derive `starter/` by replacing only the mechanism under study with `TODO`s. The starter still builds and runs.
     4. Verify it progressively, task by task, with targeted mutations.
   - **Exploration:** write `demo/` finished. Write the guide while running every step in order, from a clean state, and record the real output.
   - **Concept:** write `CONCEPT.md` and the self-assessment. Source every non-obvious claim, and draw a diagram where it helps.
5. **Write the README** from [templates/lab/](../templates/lab/), in the content language. Include only verified claims, keep the anchors and their order, and show commands in the learner's shells. Then go through it line by line and ask "which run showed this?".
6. **Verify.**
   - Run `python tools/verify.py --lab <ID>`.
   - Run the type's checks from the definition of done in [quality](../references/quality.md).
   - Check that the diagrams render.
   - **Read the lab as a learner** at the level the syllabus sets for this point. Can you follow it without guessing? Is every new concept introduced with its problem and an example before a task needs it, or taught in an earlier lab? Is every term of art and acronym glossed the first time? Does anything the learner reads before a prediction give its answer away?
   - **Read it once more as an editor**, only for form: does every optional section add something of its own, is any idea explained twice, does a long section show its parts with `###`, and do the counts and names in the README and the starter's comments match the files?
7. **Update the memory.**
   - In `SYLLABUS.md`: set the status to `🟨 built`, add the link to the README, and update the build map and the "Notes for the next labs".
   - In `GLOSSARY.md`, when the repository has one: add the terms of art this lab owns.
   - In `docs/lessons.md`: add anything worth keeping.
   - In `docs/decisions.md`: add any decision someone could undo without knowing why.
8. **Commit** with `feat(lab-<ID>): <what the lab teaches>`. Push only at milestones or when asked.
9. **Report briefly:**
   - what the lab teaches;
   - what was verified (tests, mutations, runs);
   - what is pending, if anything.

   If it closed a block, run the block review below before the block reminder (see [syllabus](../references/syllabus.md)).

## Review a block with fresh eyes

When the project of a block is `built`, and before you tell the learner the block is ready, have the whole block read by a reviewer who did not build it. The author no longer sees what they wrote, and every defect this review finds would otherwise reach the learner.

- **If your agent offers subagents,** start one without your context. Otherwise, ask the person whether a fresh session or another person can do it. As a last resort, do it yourself in a separate pass, with only the files open, reading the labs in order.
- **The reviewer gets:** the repository path, who the learner is (from `AGENTS.md`), and this brief. It reads the block in order (syllabus, every lab, the project) as the learner, may run commands only in a scratch copy, edits nothing, and reports findings ranked by impact on the learner:
  - **Defects:** a claim, count or name that does not match the files; a concept or acronym used before it is taught; an answer given away before its prediction (Concepts, tables, dissection, starter); something the project needs that no lab taught.
  - **Readability:** sections that add nothing of their own, ideas explained twice, boilerplate repeated across labs, walls of text without `###` parts, commands duplicated per shell when they are identical.
  - **What works**, briefly, so it is kept.
- **Act on it** like on learner feedback: fix the defects in every lab that has them, re-run the verifier, and send rules that would have prevented a finding to the `feedback` workflow's upstream step.

## Build a project

1. **Name the one question of the domain**, then write `BRIEF.md`: context, contract, acceptance criteria and non-functional requirements (each with the lab that taught it), plus the constraints and freedoms, and what is out of scope.
2. **Write `acceptance/`** as black-box tests against the contract. If the interface is not stable enough for that, write the reason in `BRIEF.md`.
3. **Build `reference/`.** Make every test green, then run `acceptance/` against it, then run the packaged artifact against real dependencies.
4. **Write the mutation list while you design the tests.** Ask yourself: "what would I break to prove this test matters?". Run each mutation in a scratch copy with a script that prints the number of tests that ran and the real failure.
5. **Write `REVIEW.md`** from the results: the reading order, the decisions with the lab that taught each one, the traps, the "break it yourself" table with failures quoted from the output, what is deliberately missing, and questions to challenge the design.
6. **Write the README** (what it is, how to run it, the two ways to use it), verify it, update the memory, and commit with `feat(project-<block>): …`, as for a lab.
