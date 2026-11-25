# Workflow: syllabus

Design a study path, or refine an existing one. The output is an agreed `SYLLABUS.md`. If the study repository already exists, the file is written in place; if not, it is a draft that `init` will use.

Read first: [method](../references/method.md), [syllabus](../references/syllabus.md), [lab-types](../references/lab-types.md), [dependencies](../references/dependencies.md).

## Steps

1. **Understand the goal with three questions at most.** The person may be learning, and most planning details are yours to decide. Ask only what is still missing from their request, in one message, numbered, each with an example or options (see [didactics](../references/didactics.md#in-the-conversation)):
   1. **What do you want to learn?** For example: "Kafka", "testing en Python", "ciberseguridad ofensiva". A broad field ("ciberseguridad", "cloud") is not an answer yet: ask which part, with 3–4 options.
   2. **What for?** Your current job · getting a job or changing careers · a project of your own · teaching a group · curiosity.
   3. **What have you already done with something close to it?** For example: "uso Docker en el trabajo, pero nunca Kubernetes", or "nada todavía".

   Ask them in the person's language, translating the examples. When the answer to question 2 is teaching a group, question 3 asks what the group already knows; if levels are mixed, plan for the less experienced part, and mark as `deep-dive` or `elective` what the others may skip.

   A question is answered only when the request says it plainly: a specific topic, a purpose, and experience with the topic or something close to it ("uso Spring Boot y Docker" counts for Kafka). If the request answers all three, ask nothing: say in one line that you will research and come back with a plan, then go on.

   Do not ask the rest; decide it, and list it later as assumptions the person can correct:
   - **Level and goal:** from questions 2 and 3. Current job, getting a job and teaching a group aim at job-ready; a project of your own aims at what the project needs; curiosity at solid basics.
   - **Scope:** what is in and what is left out, with the depth, modern and alternative topics you propose from the research in step 2.
   - **Time:** sessions of 1–2 h; no deadline unless they mention one.
   - **Content language:** the language they write in.
   - **Environment:** when the person will study the path themselves and you can run commands, detect it: the operating system, the shells available, the container runtime, virtualization when the path needs it (WSL, virtual machines), and the versions already installed of the tools the path needs, including the build tool. When the path is for a group, or you cannot run commands, assume PowerShell and Bash, and Docker if a container runtime is needed.
   - **Pinned versions** come from step 2. When the goal is their current job, confirm the versions of the main tools and where they run: "I will use Kafka 4.1 and Spring Boot 4.0, self-hosted; tell me if your job uses other versions or a managed service."

   For a refinement, read `SYLLABUS.md`, `docs/decisions.md` and the feedback first, and ask only about the change.
2. **Research the current state** of the technology, following [sources](../references/sources.md):
   - stable or LTS versions and their support window;
   - what is current and what is legacy (so legacy is not taught as the default);
   - what has changed recently enough to deserve a 🆕 `modern` topic.
3. **Draft the whole path, then each block.**
   - Start block 1 at the subject itself. Knowledge from other subjects that the learner lacks (a programming language, the terminal) is a prerequisite for step 4, not a block of this path.
   - First the blocks, from the starting level to the goal, each with one focus the learner can name ("pruebas unitarias", then "pruebas de integración"). Do not squeeze the subject into one block because only one will be built first.
   - Then the rows of every block: topic, kind, type, what the learner will be able to do, and a 1–2 h size; and for the build map, what it owns, builds on and starts from. End every block with a project that uses only what the block taught.
   - Open each block with the ideas it needs, independent of the tool, then alternate idea and tool.
   - Apply the design rules in [syllabus](../references/syllabus.md).
4. **Check the prerequisites** the path needs on day one (see [syllabus](../references/syllabus.md#prerequisites)).
   1. **List them** from what block 1 starts from: the languages, tools and ideas a learner must already handle, such as using a terminal, reading Python, or how HTTP works. Leave out what the path itself teaches.
   2. **Ask only what you cannot tell** from the answers in step 1. If they said "nunca programé", programming is a gap; do not ask about it. When nothing is in doubt, skip this message.
   3. **Ask in one message.** Each prerequisite gets one concrete example and three answers: yes · somewhat · no. For example: "Bash: ¿sabrías decir qué hace `cat log.txt | grep error`?". Say that they may skip the question; a skipped prerequisite counts as "somewhat".
   4. **Act on the gaps:**
      - **None:** go on.
      - **Small** (all of it fits in about three labs): open the path with a block `00` of express fundamentals.
      - **Large** (more than three labs, or a whole language or discipline): recommend another path first, which StudyForge can also plan, and say so in the presentation. The person decides.
      - **The person goes ahead anyway:** keep the plan, and record in `SYLLABUS.md` which labs will be hard without the prerequisite and what to read first.
5. **Choose the dependency strategy** and the stack verification commands (see [stacks](../stacks/README.md)). These are your decisions; do not ask the person.
6. **Self-review the draft before showing it:**
   - [ ] Every block from the starting level to the goal is planned, and each has one focus.
   - [ ] Read as a learner at the starting level, every topic title and outcome makes sense: no API names, no term taught later, the same level of technicality across rows.
   - [ ] Each block introduces its concepts before its tools, and the learner runs something in its first or second lab.
   - [ ] The core path stands alone.
   - [ ] Every row fits 1–2 h, and no row needs "and" three times.
   - [ ] Every concept has exactly one owner.
   - [ ] Prerequisites come before they are used.
   - [ ] Extras sit right after the topic they extend.
   - [ ] Every block has 3–7 labs and a project with a one-line idea of its domain; a block `00` has 1–3 labs and no project.
   - [ ] Every prerequisite of block 1 is known, taught in block `00`, or named as a gap in the presentation.
   - [ ] The lab types fit (not everything is a challenge, and concept labs are rare).
   - [ ] Versions are pinned and current.
   - [ ] Every library the plan pins passes the checklist in [dependencies](../references/dependencies.md#choosing-a-library).
7. **Present it**, in this order:
   1. The blocks as a short table: block, focus, number of labs, and the project's idea.
   2. **The prerequisites**, when step 4 found gaps: what the block `00` covers, or which path to take first and why.
   3. **The size:** total labs and an estimate of the hours (labs × 1–2 h). When the path is long for the goal (more than about six blocks, or more than the deadline allows), offer a shorter first milestone, for example the first three blocks.
   4. **What I assumed:** level and goal, scope, time, content language and environment, one line each, so the person can correct any of them. Name versions only when the person will care (their current job); otherwise name the tools, and the versions go into `SYLLABUS.md` and `docs/decisions.md`.
   5. At most three open questions, each with your recommendation. Ask only what is the person's to decide: scope, depth, time, and how or where they will practice or publish.

   Keep technical decisions out of this message (dependency strategy, build tools, verification commands): they are yours, and they go into `docs/decisions.md`. Iterate until the person agrees.
8. **Write it.** In an existing repository, update `SYLLABUS.md` (renumbering only items that are still `pending`), update `docs/decisions.md` when a decision changed, and commit with `docs(syllabus): …`. With no repository yet, hand the draft to [init](init.md).

## Done when

The person has agreed to the syllabus. Every block of the path is planned, and every row has all its columns filled, in the block tables and in the build map. The dependency strategy and the verification commands are chosen.
