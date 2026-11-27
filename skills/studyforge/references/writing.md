# Writing labs

Lab READMEs are learning material. They must be easy to scan, pleasant to follow and honest. This file says how lab material is written. How to explain anything to a learner, in a lab or in the conversation, lives in [didactics](didactics.md), and every rule there applies here.

## Language

- **Lab content** (READMEs, `CONCEPT.md`, `BRIEF.md`, `REVIEW.md`) is written in `language.content` from `studyforge.toml`.
- **Code, identifiers, test names, comments in code, folder names and commit messages** are always in English.
- **Keys** (`pending`, `core`, `challenge`…) stay in English, followed by their emoji.
- **Terms of art stay in English**, glossed the first time ([didactics](didactics.md#terms-of-art)).
- **StudyForge's own vocabulary stays in English**: the keys, the lab types and the names of its teaching devices (*Command dissection*, *Predict first*). They are the method's names, the same in every study path.
- **Every other heading is translated** with the table in [Section anchors](#section-anchors), not improvised. A literal translation that sounds odd ("Disección de comandos") is a sign the term belongs to the method and stays in English.

## Section anchors

Each section heading starts with a fixed emoji, followed by a title in the content language: `## 🎯 Objetivos`, `## 🎯 Objectives`. The emoji is the **anchor**. It keeps the same order in every lab, and `tools/verify.py` uses it to check structure in any language. Keep the order below.

| Anchor | Section | Spanish title | challenge | exploration | concept | project README |
|---|---|---|:-:|:-:|:-:|:-:|
| 🎯 | Objectives (learning objectives, 3–6) | Objetivos | required | required | required | required |
| 💡 | Why it matters (the real problem, 2–3 lines) | Por qué importa | required | required | required | |
| 📍 | Where to run commands | Dónde correr los comandos | required | required | | required |
| 🧠 | Concepts (each one introduced; see [Explaining](#explaining)) | Conceptos | required | required | required | |
| 📚 | Documentation (official links, exact pages) | Documentación | required | required | required | |
| 🧭 | Scenario (what is there, what to achieve) | Escenario | required | required | | |
| ✅ | Tasks | Tareas | required | | | |
| 🧪 | Experiments | Experimentos | | required | | |
| 🛣️ | Two ways to use this project | Dos formas de usar este proyecto | | | | required |
| 🔍 | Command dissection | Command dissection | when it adds | when it adds | | |
| 👀 | What you should see | Qué deberías ver | when it adds | when it adds | | |
| 💼 | In real projects | En proyectos reales | when it adds | when it adds | when it adds | |
| 🧹 | Cleanup | Limpieza | when it creates resources | when it creates resources | | |
| 🚀 | Stretch goal | Reto extra | when it adds | when it adds | when it adds | |
| 🆘 | Hints | Pistas | when it adds | when it adds | | |
| 🎤 | Self-assessment | Autoevaluación | required | required | required | |
| 🔁 | Retrospective | Retrospectiva | when it adds | when it adds | when it adds | when it adds |
| ✔️ | Verified answers | Respuestas verificadas | required | when it adds | | |

**Answers come last.** A `<details>` fold hides them only on GitHub; a learner reading in a terminal or a chat, and an agent, read the file top to bottom. With ✔️ last, the self-assessment and the retrospective are met before any answer (since 1.8.0; earlier labs had ✔️ before 🎤).

The Spanish column is the reference translation. For another content language, translate the same way and write the titles once in the study repository's `AGENTS.md`, so every lab uses the same ones.

The title line is `# <type emoji> <ID> · <Title>`, for example `# 🧩 1.2 · Configuration and profiles`. A metadata table follows it: ⏱️ duration, 🧪 type, 🏷️ kind, and the pinned stack versions.

**"When it adds" means: only if the section has content of its own.** A section that restates what another section said, or that exists because the template has it, is noise: leave it out. Examples: a concept lab with no commands has no command dissection; an exploration whose 👀 blocks already answer every prediction needs no ✔️; a lab with nothing to say about teams or production has no 💼. The order of the sections that remain does not change.

## Structure inside a section

A long section reads as a flat wall unless its parts are visible. Inside a section, use `###` headings for its parts, and keep bold lead-ins for one-line notes.

- **🧠 Concepts:** one `### <Name> (*term of art*)` per concept, for example `### Parametrizar (*parametrize*)`. The heading shows the learner how many ideas the lab has, and GitHub lists it in the file outline.
- **🧭 Scenario:** when it has more than one part, `###` for each, for example "the code" and "how your work is checked" (mutants, structure checks).
- **✅ Tasks** and **🧪 Experiments** already use `### Task N · <Title>` and `### Experiment N · <Title>`.
- `####` rarely: a part that needs a fourth level is too long for the README, so move it to `CONCEPT.md` or split it into more `###` parts. On GitHub a `####` looks almost like bold body text, so it adds little hierarchy. A section under about 15 lines needs no `###`. `tools/verify.py` reads only `## <emoji>` lines, so `###` headings are free.

## Say each thing once

Each idea has one home ([didactics](didactics.md#say-each-thing-once)). In a lab, Concepts explain it, the task uses it, the hint points at it, and the verified answer shows what happened. Watch for these repeats:
- 💼 restating Concepts. It only adds what the lab did not say: team practice, production, security, tools beyond the lab.
- 🔍 explaining again what the Concepts examples already showed. It is a reference card: one line per item, with options and defaults.
- A note repeated right under a table that already says it.
- Boilerplate copied into every lab (the same diagram, the same paragraph): say it once in the first lab or in the repository README, and link to it.

## Commands

- **Commands always go in fenced code blocks, never inline.** The learner copies them and runs them by hand.
- **Show each command for the learner's shells**, in the order of `learner.shells`. When the command is the same in every shell (`python -m pytest`, `mvn test`), write **one** block labeled with all of them ("PowerShell o Bash:"). Write one block per shell only when the command differs, such as environment variables or paths. Label each block in the line before it.
- **Running the same command again** needs no new block: "Corre otra vez el comando del experimento 2".
- **"Where to run commands"** goes near the top and names the folder (for example `starter/`). The check of where you are (`Get-Location` / `pwd`) appears in the first lab that uses a terminal; later labs only name the folder. If a step needs another folder, the step says so.
- **Expected output gets its own block** when it matters. Quote real output, trimmed to the key lines. A data table printed in a README matches the seed or fixture row for row; regenerate it from the data, never by hand.
- **File sizes:** show `ls -l <file>`, which runs in PowerShell and Bash, and name the size column in each (`Length` in PowerShell, the fifth column in Bash).
- **Inline code is only for identifiers, file names and short values.**

## Explaining

Every concept follows [didactics](didactics.md#explaining): problem, idea, example, name; concept before tool; a worked example before the task. In a lab README that takes this shape:

- **🧠 Concepts is not a dictionary.** Each concept follows that order, under its own `###` heading, in a short paragraph and a small code block, not a one-line definition. Up to about five concepts stay in the README. A concept that needs a diagram or its internal mechanics, or a lab with more than five, moves the explanation to `CONCEPT.md` and keeps a short summary with a link in the README.
- **Concepts say what something does, not what goes wrong without it.** When a 🔮 prediction asks what happens if the learner forgets a setting, misuses a tool or picks the wrong data, the Concepts section must not answer it: it presents the tool and how to use it, and the consequence of misusing it stays for the verified answer. The learner reads Concepts first, so a trap explained there is spoiled.
- **Glossary.** When a study path accumulates terms of art (as a rule of thumb, from about ten), add a `GLOSSARY.md` at the repository root from [the template](../templates/repo/GLOSSARY.md). Group it by block. Each entry is the term as the trade writes it, one line in the content language, and a link to the lab that owns it. It is an index, not a second explanation: the owner lab keeps the explanation.

## Teaching devices

- **🔮 Predict first.** Mark prediction steps as `🔮 **Predict first:** …`. The answer lives in "Verified answers" (challenges) or in a `<details><summary>👀 …</summary>` right after the commands (explorations). Put the 🔮 step before the command that produces the answer: even the command's startup banner can give it away.
- **A prediction must be reachable.** Its code gets past every check that runs before the one it asks about (a harness that compares columns before rows stops at "columns differ"). Keep the trap in the one expression the prediction asks about; split the task when the prediction would contain another step's solution. When the prediction's code stays in the task file, the next step says "replace it", and the harness explains the error a second statement causes.
- **The step after a prediction does not answer it.** It says "compare what you see with your prediction", then gives a goal ("leave in the file a query that…"), never the fix or where to look ("read the failure", "fix it with parentheses").
- **Nothing the learner reads before a prediction may give its answer away.** That includes the 🎯 objectives, the 🧠 Concepts section and its examples, the captions and contents of the scenario's tables (a mutant described as "calls a method that does not exist" answers "what if the mock has no spec?"), the command dissection, a `[!WARNING]` that explains the trap ("`match` is a regular expression"), expected output left visible, a hint in the same step ("…and read the failure"), a docstring or comment in the demo ("they pass together and fail apart"), and a starter that names or imports the solution (a `TODO` that says "…with `pytest.approx`", an unused `import re`). A warning may say *that* a trap exists, never *what* it is. Check this from a learner's point of view before marking a lab `built`. A fresh reviewer who did not build the lab finds these faster than the author.
- **Tasks:** each task is numbered and has a one-line goal, checkbox steps, and the test that validates it (`**Validated by:** \`ConfigTest\``).
- **Alerts:** use `> [!NOTE]` for context, `> [!TIP]` for shortcuts, `> [!IMPORTANT]` for what must not be missed, and `> [!WARNING]` for the lab's traps (without spoiling them).
- **Spoilers** (hints, verified answers, self-assessment answers) go inside `<details><summary>…</summary>`. Order hints from vague to concrete.
- **🔍 Command dissection.** A reference card for the new commands, flags, operators or annotations the lab uses: one line each, with what it does and its default. It does not repeat the explanation in Concepts, and it does not show the value a task asks for. Leave it out when the lab introduces no new syntax. A flag that appears only here is not taught: a later lab that relies on it introduces it again in a task.
- **`diff` blocks** show what changes between two states (configuration, starter → solution) better than two full listings.
- **Links to code:** every scenario links its implementation and tests with relative paths.
- **💼 In real projects:** professional judgment, security, operations, typical team mistakes, and how this is configured outside development mode. Only what the lab did not already say; leave the section out when there is nothing new.
- **✔️ Verified answers** answer every prediction with the real output. They open with one line naming the versions they were run on, worded the same in every lab of the repository. An exploration without ✔️ puts that line first in its first 👀 block.
- **🎤 Self-assessment:** 5 interview-level questions, to answer without looking at the code, written as [questions that make the learner think](didactics.md#questions-that-make-the-learner-think). In concept labs the answers go in `<details>` blocks.
- **🔁 Retrospective:** what did I understand, what was hard, what should I reinforce. It feeds the `feedback` workflow.

## Tone

The tone rules in [didactics](didactics.md#tone) apply. Lab material adds these:

- **Use emoji as signposts, not decoration**: the section anchors and an occasional marker (🔮, ⚠️). Never add emoji inside code or commands.
- Use tables for comparisons, Mermaid for flows, and a single diagram per idea (see [visuals](visuals.md)).
- **Write diagram labels as prose.** Node and edge labels start with a capital letter in the content language (`Your tests`, `Tus pruebas`, `Yes` / `No`, `Sí` / `No`). Code identifiers, commands and workflow names keep their exact spelling (`settle`, `weight_kg > 2?`, `build`), and the line after them is capitalized (`build<br/>Next lab`).
