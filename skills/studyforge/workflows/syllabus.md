# Workflow: syllabus

Design a study path, or refine an existing one. The output is an agreed `SYLLABUS.md`. If the study repository already exists, the file is written in place; if not, it is a draft that `init` will use.

Read first: [method](../references/method.md), [syllabus](../references/syllabus.md), [lab-types](../references/lab-types.md), [dependencies](../references/dependencies.md).

## Steps

1. **Understand the goal.** Ask only what changes the plan, and propose a default for each question:
   - **What for:** a job, a certification, a project, teaching others, or curiosity.
   - **Level:** what they already know, and where they want to end up (basics, job-ready, expert).
   - **Depth:** topics to go deep on and topics to skip. Do they want modern or alternative topics?
   - **Time:** session length (default: 1–2 h), sessions per week, and any deadline.
   - **Environment:** operating system, shells, container runtime, and versions they must use (for example, the one at their job).
   - **Language** of the lab content.

   For a refinement, read `SYLLABUS.md`, `docs/decisions.md` and the feedback first, and ask only about the change.
2. **Research the current state** of the technology, following [sources](../references/sources.md):
   - stable or LTS versions and their support window;
   - what is current and what is legacy (so legacy is not taught as the default);
   - what has changed recently enough to deserve a 🆕 `modern` topic.
3. **Draft the whole path, then each block.**
   - First the blocks, from the starting level to the goal, each with one focus the learner can name ("pruebas unitarias", then "pruebas de integración"). Do not squeeze the subject into one block because only one will be built first.
   - Then the rows of every block: topic, kind, type, what the learner will be able to do, and a 1–2 h size; and for the build map, what it owns, builds on and starts from. End every block with a project that uses only what the block taught.
   - Open each block with the ideas it needs, independent of the tool, then alternate idea and tool.
   - Apply the design rules in [syllabus](../references/syllabus.md).
4. **Choose the dependency strategy** and the stack verification commands (see [stacks](../stacks/README.md)).
5. **Self-review the draft before showing it:**
   - [ ] Every block from the starting level to the goal is planned, and each has one focus.
   - [ ] Read as a learner at the starting level, every topic title and outcome makes sense: no API names, no term taught later, the same level of technicality across rows.
   - [ ] Each block introduces its concepts before its tools, and the learner runs something in its first or second lab.
   - [ ] The core path stands alone.
   - [ ] Every row fits 1–2 h, and no row needs "and" three times.
   - [ ] Every concept has exactly one owner.
   - [ ] Prerequisites come before they are used.
   - [ ] Extras sit right after the topic they extend.
   - [ ] Every block has 3–7 labs and a project with a one-line idea of its domain.
   - [ ] The lab types fit (not everything is a challenge, and concept labs are rare).
   - [ ] Versions are pinned and current.
   - [ ] Every library outside the stack's platform passes the checklist in [dependencies](../references/dependencies.md#choosing-a-library).
6. **Present it.** Show the blocks as a short table, the key decisions with your recommendation, and the open questions. Iterate until the person agrees.
7. **Write it.** In an existing repository, update `SYLLABUS.md` (renumbering only items that are still `pending`), update `docs/decisions.md` when a decision changed, and commit with `docs(syllabus): …`. With no repository yet, hand the draft to [init](init.md).

## Done when

The person has agreed to the syllabus. Every block of the path is planned, and every row has all its columns filled, in the block tables and in the build map. The dependency strategy and the verification commands are chosen.
