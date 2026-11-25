# The syllabus

`SYLLABUS.md` is the plan and the state of a study path. The `syllabus` workflow writes it. The `build`, `review` and `feedback` workflows update it.

## Keys

Keys are always written in English, with their emoji, in every language. A study repository in another language translates **only the legend** at the top of `SYLLABUS.md`. Workflows read the keys, so a key that changes per language would break them.

**Status**

| Key | Meaning |
|---|---|
| ⬜ `pending` | Planned and not built yet |
| 🟨 `built` | Built and verified, waiting for a learner to solve it and give feedback |
| ✅ `done` | A learner solved it and their feedback was applied |

Never mark a lab `done` yourself: only learner feedback does that. When a lab is retired, keep its row with a note and do not reuse its ID.

**Topic kind**

| Key | Meaning |
|---|---|
| 🎯 `core` | The path; skipping it leaves a gap |
| 🔬 `deep-dive` | The same topic, deeper |
| 🔀 `alternative` | The same goal with another technology or approach (RabbitMQ instead of Kafka) |
| ➕ `elective` | Valuable but skippable when time is short |

The **🆕 `modern`** tag can go on any kind. It marks a topic that brings the path up to date, such as a newer API or a new platform feature.

**Lab type**: 🧩 `challenge` · 🔭 `exploration` · 💭 `concept` · 🏗️ `project`. See [lab-types](lab-types.md) and [projects](projects.md).

## Structure of `SYLLABUS.md`

The syllabus has two readers: the **learner**, who decides whether the path is for them and where they are, and the **author's agent**, who needs ownership and starting points to build. The top of the file is for the learner; the build map at the end is for the agent. A learner should understand the whole top part at their starting level.

1. **Header**: goal, audience and starting level, the stack with **pinned versions**, session length, and the legend (translated if the content is not in English).
2. **The path at a glance**: every block in one short table (block, what you will be able to do at the end, status), so the learner sees where the path goes before the details.
3. **One section per block** with a one-line focus, written as what the learner will be able to do, and this table:

| ID | Topic | Kind | Type | You will be able to | Status |
|---|---|---|---|---|---|
| [1.1](labs/01-fundamentals/01-dev-mode/README.md) | Dev mode | 🎯 core | 🧩 challenge | Change code and see it live without restarting; run the packaged app | 🟨 built |
| 1.P | Project: task board | 🎯 core | 🏗️ project | Build a small service from scratch with everything in block 1 | ⬜ pending |

4. **Design rules**: the method's rules that this path stresses, plus any of its own. Example: "labs 08–10 start from the REST contract of lab 05".
5. **Build map** (for the author): one table for every lab, with what it owns, what it builds on and where it starts from.

| ID | Owns | Builds on | Starts from |
|---|---|---|---|
| 1.1 | Dev mode, live reload | — | Generated project |
| 1.P | — | 1.1–1.4 | From scratch |

6. **Notes for the next labs**: what the next lab should reuse, avoid or set up. Write it at the end of every lab so a fresh session can continue.

### Writing the rows

- **Topics name the concept or the tool**, at the same level of technicality across rows: "Tipos de prueba", "Primeras pruebas con pytest", "Dobles de prueba". A question or a hook ("¿qué probar y por qué?") belongs inside the lab, not in its title.
- **"You will be able to" is an outcome in the learner's words**, not a list of APIs: "comparar decimales sin falsos fallos", not "`approx`". A term of art may appear when the learner will meet it in that lab, but not one taught later. API names belong in the lab's objectives and in the build map.
- **Each block has one focus** that a learner can name in a few words ("pruebas unitarias"). A block that mixes levels (unit, integration and end-to-end at once) is two or three blocks.

## Designing a syllabus

- **Ask little, assume the rest.** The person answers at most three questions (what, what for, what they have done); level, time, language, environment and versions are assumptions they can correct when the plan is shown. The [syllabus workflow](../workflows/syllabus.md) says how.

  Propose defaults instead of asking open questions.
- **Research current versions** before naming them. Prefer LTS or stable releases, write down the support window, and follow [sources](sources.md).
- **Plan the whole path; build one block at a time.** The syllabus lays out every block from the starting level to the goal, each with its rows and project as ⬜ `pending`. Only then does `build` start on block 1. A path of one block hides where the learner is going and tempts you to squeeze the whole subject into it.
- **Concepts first, then the tool, alternating.** A block opens with the ideas it needs in terms independent of the tool (often a `concept` lab, or the first part of the first lab), then teaches how the tool expresses them. Later labs alternate: a new idea, then its tool. Do not front-load all the theory: the learner should run something in the first or second lab of every block.
- **Order by prerequisites.** A lab only uses what an earlier lab owns or what `SETUP.md` installs.
- **The core path must stand alone.** Someone who skips every deep-dive, alternative and elective still gets a coherent path.
- **Place extras after the core topic they extend.** They take the next free number, or a letter suffix when IDs are frozen (see [layout](layout.md)).
- **Blocks have 3–7 labs and one project.** A final capstone is its own block. The only exception is block `00`.

## Prerequisites

A path starts where the learner is, not where block 1 assumes they are. The [syllabus workflow](../workflows/syllabus.md) checks what block 1 needs before the plan is shown.

- **Block `00` covers small gaps:** express fundamentals in 1–3 labs, with IDs `0.1`, `0.2`… It teaches only what block 1 uses, owns those topics like any lab, and has no project, because block 1's project already uses them. A learner who has the prerequisites skips it.
- **A large gap is another path.** When the missing knowledge needs more than three labs, or is a whole language or discipline (Python before security, the terminal before Git workflows), a block `00` would squeeze it. Recommend that path first.
- **A gap the person accepts is written down.** The notes of `SYLLABUS.md` say which labs will be hard without it and what to read first.
- **One owner per topic.** If two rows teach the same thing, merge them or point one to the other. Owning means *teaching*; any later lab may *use* the topic with a link to its owner (see principle 5 in [method](method.md)).
- **Size every lab at 1–2 h.** A row that needs "and" three times is two labs.
- **Pick the starting point per lab**: a generated project, a minimal app, an earlier lab, or from scratch. Write it in "Starts from" in the build map (see principle 3 in [method](method.md)).
- **Pick the lab type per topic.** Use a `challenge` when the behavior can be checked by tests, an `exploration` for operational topics that are understood by observing them (infrastructure, tooling, performance), and a `concept` when there is nothing to run yet (mindset, theory, a comparison).
- **Decide the dependency strategy** with the syllabus and record it (see [dependencies](dependencies.md)).
- **Read it as the learner.** Before presenting the draft, read the top part as someone at the starting level. Every title and outcome should make sense to them without the labs at hand.
- **Present the draft with a recommendation**, iterate, and only then write the file.

## Keeping it alive

- A syllabus written before StudyForge 1.1 has one table per block with the columns "What is practiced", "Owns / builds on" and "Starts from". `review` offers to move it to the current structure; nothing reads those columns mechanically, so the old layout keeps working.
- Update the status in the same commit that builds or finishes a lab.
- Feedback that changes the plan (split, merge, reorder, add) goes through the `syllabus` workflow again. Renumber only items that are still `pending` (see [layout](layout.md)).
- When a block is finished, tell the learner in one short message: what the block contains, what was verified, and an invitation to give feedback. It is a reminder, never a gate.
