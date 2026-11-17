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
3. **Draft blocks and topics.** For each row, fill in: topic, kind, type, what is practiced, owns / builds on, starts from, and a 1–2 h size. End every block with a project. Apply the design rules in [syllabus](../references/syllabus.md).
4. **Choose the dependency strategy** and the stack verification commands (see [stacks](../stacks/README.md)).
5. **Self-review the draft before showing it:**
   - [ ] The core path stands alone.
   - [ ] Every row fits 1–2 h, and no row needs "and" three times.
   - [ ] Every concept has exactly one owner.
   - [ ] Prerequisites come before they are used.
   - [ ] Extras sit right after the topic they extend.
   - [ ] Every block has 3–7 labs and a project with a one-line idea of its domain.
   - [ ] The lab types fit (not everything is a challenge, and concept labs are rare).
   - [ ] Versions are pinned and current.
6. **Present it.** Show the blocks as a short table, the key decisions with your recommendation, and the open questions. Iterate until the person agrees.
7. **Write it.** In an existing repository, update `SYLLABUS.md` (renumbering only items that are still `pending`), update `docs/decisions.md` when a decision changed, and commit with `docs(syllabus): …`. With no repository yet, hand the draft to [init](init.md).

## Done when

The person has agreed to the syllabus. Every row has all its columns filled. The dependency strategy and the verification commands are chosen.
