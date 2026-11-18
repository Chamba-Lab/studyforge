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
| 🔍 | Command dissection | Command dissection | optional | optional | | |
| 👀 | What you should see | Qué deberías ver | optional | optional | | |
| 💼 | In real projects | En proyectos reales | required | required | optional | |
| 🧹 | Cleanup | Limpieza | when it creates resources | when it creates resources | | |
| 🚀 | Stretch goal | Reto extra | optional | optional | optional | |
| 🆘 | Hints | Pistas | optional | optional | | |
| ✔️ | Verified answers | Respuestas verificadas | required | required | | |
| 🎤 | Self-assessment | Autoevaluación | required | required | required | |
| 🔁 | Retrospective | Retrospectiva | optional | optional | optional | optional |

The Spanish column is the reference translation. For another content language, translate the same way and write the titles once in the study repository's `AGENTS.md`, so every lab uses the same ones.

The title line is `# <type emoji> <ID> · <Title>`, for example `# 🧩 1.2 · Configuration and profiles`. A metadata table follows it: ⏱️ duration, 🧪 type, 🏷️ kind, and the pinned stack versions.

## Commands

- **Commands always go in fenced code blocks, never inline.** The learner copies them and runs them by hand.
- **Show each command in the learner's shells**, in the order of `learner.shells` (for example, PowerShell first, then Bash). Label each block in the line before it.
- **"Where to run commands"** goes near the top. It names the folder (for example `starter/`) and includes the check (`Get-Location` / `pwd`). If a step needs another folder, the step says so.
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
- **🧠 Concepts is not a dictionary.** Each item follows the order above, in a short paragraph or a small code block, not a one-line definition. When a lab introduces more than three or four concepts, or one needs a diagram or mechanics, move the explanation to `CONCEPT.md` and keep a short summary with a link in the README.
- **Concept first, tool second.** Say what the idea is in terms independent of the tool, then show how the tool expresses it: "una prueba parametrizada es una misma prueba que corre con varios datos" before `@pytest.mark.parametrize`. The learner should be able to take the idea to another tool.
- **A worked example before the task.** Before asking the learner to do something new, show it done once, complete and on a different case. The task then asks for the same skill on new data, not for guessing the syntax.
- **Analogies only when they map.** Use one when it maps the mechanism, not just the mood, and say where it stops working: "como una alarma de humo… pero, a diferencia de la alarma, una prueba solo detecta lo que le pediste revisar".
- **Bridge to the previous lab.** Open "Why it matters" or "Concepts" with one sentence that connects to what the learner already did: "En el lab 1.2 escribiste una prueba por caso; aquí…".
- **Keep the jargon level even.** Titles, objectives and the syllabus use words the learner knows at that point. A term not yet taught gets a gloss or waits for its lab.
- **Glossary.** When a study path accumulates terms of art (as a rule of thumb, from about ten), add a `GLOSSARY.md` at the repository root from [the template](../templates/repo/GLOSSARY.md). Group it by block. Each entry is the term as the trade writes it, one line in the content language, and a link to the lab that owns it. It is an index, not a second explanation: the owner lab keeps the explanation.

## Teaching devices

- **🔮 Predict first.** Mark prediction steps as `🔮 **Predict first:** …`. The answer lives in "Verified answers" (challenges) or in a `<details><summary>👀 …</summary>` right after the commands (explorations).
- **Nothing near a prediction may give its answer away.** That includes a `[!WARNING]` that explains the trap ("`match` is a regular expression"), expected output left visible, a hint in the same step ("…and read the failure"), a docstring or comment in the demo ("they pass together and fail apart"), and a starter `TODO` that names the solution ("…with `pytest.approx`"). A warning may say *that* a trap exists, never *what* it is. Check this from a learner's point of view before marking a lab `built`. A fresh reviewer who did not build the lab finds these faster than the author.
- **Tasks:** each task is numbered and has a one-line goal, checkbox steps, and the test that validates it (`**Validated by:** \`ConfigTest\``).
- **Alerts:** use `> [!NOTE]` for context, `> [!TIP]` for shortcuts, `> [!IMPORTANT]` for what must not be missed, and `> [!WARNING]` for the lab's traps (without spoiling them).
- **Spoilers** (hints, verified answers, self-assessment answers) go inside `<details><summary>…</summary>`. Order hints from vague to concrete.
- **🔍 Command dissection.** For each new command, flag, operator or annotation, add a short table of what each part does and its default. Use it whenever the lab introduces new syntax.
- **`diff` blocks** show what changes between two states (configuration, starter → solution) better than two full listings.
- **Links to code:** every scenario links its implementation and tests with relative paths.
- **💼 In real projects:** professional judgment, security, operations, typical team mistakes, and how this is configured outside development mode.
- **🎤 Self-assessment:** 5 interview-level questions, to answer without looking at the code. In concept labs the answers go in `<details>` blocks.
- **🔁 Retrospective:** what did I understand, what was hard, what should I reinforce. It feeds the `feedback` workflow.

## Tone

- **Concise and concrete.** Use one idea per paragraph, and a table when you are comparing.
- **Use emoji as signposts, not decoration**: the section anchors and an occasional marker (🔮, ⚠️). Never add emoji inside code or commands.
- Use tables for comparisons, Mermaid for flows, and a single diagram per idea (see [visuals](visuals.md)).
- **Write diagram labels as prose.** Node and edge labels start with a capital letter in the content language (`Your tests`, `Tus pruebas`, `Yes` / `No`, `Sí` / `No`). Code identifiers, commands and workflow names keep their exact spelling (`settle`, `weight_kg > 2?`, `build`), and the line after them is capitalized (`build<br/>Next lab`).
- **Proofread before you commit.** Read the text once only for form: capital letters in headings, list items, table cells and diagram labels; proper nouns as their owners write them (Git, GitHub, Python, PowerShell); accents and punctuation of the content language. Form mistakes cost the learner's trust as much as wrong facts.
- No filler, no hype, no promises. If something is uncertain, say what was measured and where.
