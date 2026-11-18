# Writing labs

Lab READMEs are learning material. They must be easy to scan, pleasant to follow and honest.

## Language

- **Lab content** (READMEs, `CONCEPT.md`, `BRIEF.md`, `REVIEW.md`) is written in `language.content` from `studyforge.toml`.
- **Code, identifiers, test names, comments in code, folder names and commit messages** are always in English.
- **Keys** (`pending`, `core`, `challenge`…) stay in English, followed by their emoji.
- **Terms of art stay in English** when that is how the trade uses them (test suite, fixture, mock, stub, Arrange-Act-Assert, pull request, deployment). The first time a lab uses one, give it a short gloss in the content language: "un *fixture* (la preparación que una prueba necesita)". From then on, use the English term. A learner who only knows a literal translation cannot search the docs or follow a team conversation. Translate the term only when the content language has an established equivalent that practitioners use ("prueba unitaria" is used; "accesorio" for fixture is not).
- **StudyForge's own vocabulary stays in English**: the keys, the lab types and the names of its teaching devices (*Command dissection*, *Predict first*). They are the method's names, the same in every study path.
- **Every other heading is translated** with the table in [Section anchors](#section-anchors), not improvised. A literal translation that sounds odd ("Disección de comandos") is a sign the term belongs to the method and stays in English.
- Use plain, neutral language, without local slang. Use short sentences and active voice. Explain the *why* before the *how*.

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
| ✔️ | Verified answers | Respuestas verificadas | required | when it adds | | |
| 🎤 | Self-assessment | Autoevaluación | required | required | required | |
| 🔁 | Retrospective | Retrospectiva | when it adds | when it adds | when it adds | when it adds |

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

Each idea has one home in the lab. Concepts explain it, the task uses it, the hint points at it, and the verified answer shows what happened. If a second section needs it, it refers back in a few words; it does not explain it again. Watch for these repeats:
- 💼 restating Concepts. It only adds what the lab did not say: team practice, production, security, tools beyond the lab.
- 🔍 explaining again what the Concepts examples already showed. It is a reference card: one line per item, with options and defaults.
- A note repeated right under a table that already says it.
- Boilerplate copied into every lab (the same diagram, the same paragraph): say it once in the first lab or in the repository README, and link to it.

## Commands

- **Commands always go in fenced code blocks, never inline.** The learner copies them and runs them by hand.
- **Show each command for the learner's shells**, in the order of `learner.shells`. When the command is the same in every shell (`python -m pytest`, `mvn test`), write **one** block labeled with all of them ("PowerShell o Bash:"). Write one block per shell only when the command differs, such as environment variables or paths. Label each block in the line before it.
- **Running the same command again** needs no new block: "Corre otra vez el comando del experimento 2".
- **"Where to run commands"** goes near the top and names the folder (for example `starter/`). The check of where you are (`Get-Location` / `pwd`) appears in the first lab that uses a terminal; later labs only name the folder. If a step needs another folder, the step says so.
- **Expected output gets its own block** when it matters. Quote real output, trimmed to the key lines.
- **Inline code is only for identifiers, file names and short values.**

## Explaining

The teaching devices below make the learner practice. This section makes sure they understood what to practice first. A lab that only lists definitions and then asks for a task is a test, not a lesson.

- **Introduce before you use.** Every new concept arrives in this order:
  1. **The problem**, starting from something the learner already knows: "comparar `0.1 + 0.2` con `0.3` da `False`; ¿por qué?".
  2. **The idea** in one or two plain sentences.
  3. **A minimal example** that shows it working, on a case different from the task's.
  4. **The name**: the term of art, glossed the first time.

  A concept that appears in a task, a command or a hint without this introduction (here or in its owner lab) is an orphan concept, and a defect.
- **🧠 Concepts is not a dictionary.** Each concept follows the order above, under its own `###` heading, in a short paragraph and a small code block, not a one-line definition. Up to about five concepts stay in the README. A concept that needs a diagram or its internal mechanics, or a lab with more than five, moves the explanation to `CONCEPT.md` and keeps a short summary with a link in the README.
- **Concepts say what something does, not what goes wrong without it.** When a 🔮 prediction asks what happens if the learner forgets a setting, misuses a tool or picks the wrong data, the Concepts section must not answer it: it presents the tool and how to use it, and the consequence of misusing it stays for the verified answer. The learner reads Concepts first, so a trap explained there is spoiled.
- **Concept first, tool second.** Say what the idea is in terms independent of the tool, then show how the tool expresses it: "una prueba parametrizada es una misma prueba que corre con varios datos" before `@pytest.mark.parametrize`. The learner should be able to take the idea to another tool.
- **A worked example before the task.** Before asking the learner to do something new, show it done once, complete and on a different case. The task then asks for the same skill on new data, not for guessing the syntax.
- **Analogies only when they map.** Use one when it maps the mechanism, not just the mood, and say where it stops working: "como una alarma de humo… pero, a diferencia de la alarma, una prueba solo detecta lo que le pediste revisar".
- **Bridge to the previous lab.** Open "Why it matters" or "Concepts" with one sentence that connects to what the learner already did: "En el lab 1.2 escribiste una prueba por caso; aquí…".
- **Keep the jargon level even.** Titles, objectives and the syllabus use words the learner knows at that point. A term not yet taught gets a gloss or waits for its lab. Acronyms count as terms: the first "CI" or "API" a learner meets gets its gloss.
- **Only what the lab uses.** A concept the lab's tasks do not need belongs to the lab that uses it. A short "you will use this in…" mention is fine; a full explanation is not.
- **Glossary.** When a study path accumulates terms of art (as a rule of thumb, from about ten), add a `GLOSSARY.md` at the repository root from [the template](../templates/repo/GLOSSARY.md). Group it by block. Each entry is the term as the trade writes it, one line in the content language, and a link to the lab that owns it. It is an index, not a second explanation: the owner lab keeps the explanation.

## Teaching devices

- **🔮 Predict first.** Mark prediction steps as `🔮 **Predict first:** …`. The answer lives in "Verified answers" (challenges) or in a `<details><summary>👀 …</summary>` right after the commands (explorations).
- **Nothing the learner reads before a prediction may give its answer away.** That includes the 🧠 Concepts section and its examples, the scenario's tables (a mutant described as "calls a method that does not exist" answers "what if the mock has no spec?"), the command dissection, a `[!WARNING]` that explains the trap ("`match` is a regular expression"), expected output left visible, a hint in the same step ("…and read the failure"), a docstring or comment in the demo ("they pass together and fail apart"), and a starter that names or imports the solution (a `TODO` that says "…with `pytest.approx`", an unused `import re`). A warning may say *that* a trap exists, never *what* it is. Check this from a learner's point of view before marking a lab `built`. A fresh reviewer who did not build the lab finds these faster than the author.
- **Tasks:** each task is numbered and has a one-line goal, checkbox steps, and the test that validates it (`**Validated by:** \`ConfigTest\``).
- **Alerts:** use `> [!NOTE]` for context, `> [!TIP]` for shortcuts, `> [!IMPORTANT]` for what must not be missed, and `> [!WARNING]` for the lab's traps (without spoiling them).
- **Spoilers** (hints, verified answers, self-assessment answers) go inside `<details><summary>…</summary>`. Order hints from vague to concrete.
- **🔍 Command dissection.** A reference card for the new commands, flags, operators or annotations the lab uses: one line each, with what it does and its default. It does not repeat the explanation in Concepts, and it does not show the value a task asks for. Leave it out when the lab introduces no new syntax.
- **`diff` blocks** show what changes between two states (configuration, starter → solution) better than two full listings.
- **Links to code:** every scenario links its implementation and tests with relative paths.
- **💼 In real projects:** professional judgment, security, operations, typical team mistakes, and how this is configured outside development mode. Only what the lab did not already say; leave the section out when there is nothing new.
- **✔️ Verified answers** answer every prediction with the real output. They open with one line naming the versions they were run on, worded the same in every lab of the repository.
- **🎤 Self-assessment:** 5 interview-level questions, to answer without looking at the code. In concept labs the answers go in `<details>` blocks.
- **🔁 Retrospective:** what did I understand, what was hard, what should I reinforce. It feeds the `feedback` workflow.

## Tone

- **Concise and concrete.** Use one idea per paragraph, and a table when you are comparing.
- **Use emoji as signposts, not decoration**: the section anchors and an occasional marker (🔮, ⚠️). Never add emoji inside code or commands.
- Use tables for comparisons, Mermaid for flows, and a single diagram per idea (see [visuals](visuals.md)).
- **Write diagram labels as prose.** Node and edge labels start with a capital letter in the content language (`Your tests`, `Tus pruebas`, `Yes` / `No`, `Sí` / `No`). Code identifiers, commands and workflow names keep their exact spelling (`settle`, `weight_kg > 2?`, `build`), and the line after them is capitalized (`build<br/>Next lab`).
- **Proofread before you commit.** Read the text once only for form: capital letters in headings, list items, table cells and diagram labels; proper nouns as their owners write them (Git, GitHub, Python, PowerShell); accents and punctuation of the content language. Form mistakes cost the learner's trust as much as wrong facts.
- No filler, no hype, no promises. If something is uncertain, say what was measured and where.
