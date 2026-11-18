# Writing labs

Lab READMEs are learning material. They must be easy to scan, pleasant to follow and honest.

## Language

- **Lab content** (READMEs, `CONCEPT.md`, `BRIEF.md`, `REVIEW.md`) is written in `language.content` from `studyforge.toml`.
- **Code, identifiers, test names, comments in code, folder names and commit messages** are always in English.
- **Keys** (`pending`, `core`, `challenge`…) stay in English, followed by their emoji.
- Use plain, neutral language, without local slang. Use short sentences and active voice. Explain the *why* before the *how*.

## Section anchors

Each section heading starts with a fixed emoji, followed by a title in the content language: `## 🎯 Objetivos`, `## 🎯 Objectives`. The emoji is the **anchor**. It keeps the same order in every lab, and `tools/verify.py` uses it to check structure in any language. Keep the order below.

| Anchor | Section | challenge | exploration | concept | project README |
|---|---|:-:|:-:|:-:|:-:|
| 🎯 | Objectives (learning objectives, 3–6) | required | required | required | required |
| 💡 | Why it matters (the real problem, 2–3 lines) | required | required | required | |
| 📍 | Where to run commands | required | required | | required |
| 🧠 | Concepts (short list; link `CONCEPT.md` when long) | required | required | required | |
| 📚 | Documentation (official links, exact pages) | required | required | required | |
| 🧭 | Scenario (what is there, what to achieve) | required | required | | |
| ✅ | Tasks | required | | | |
| 🧪 | Experiments | | required | | |
| 🛣️ | Two ways to use this project | | | | required |
| 🔍 | Command dissection | optional | optional | | |
| 👀 | What you should see | optional | optional | | |
| 💼 | In real projects | required | required | optional | |
| 🧹 | Cleanup | when it creates resources | when it creates resources | | |
| 🚀 | Stretch goal | optional | optional | optional | |
| 🆘 | Hints | optional | optional | | |
| ✔️ | Verified answers | required | required | | |
| 🎤 | Self-assessment | required | required | required | |
| 🔁 | Retrospective | optional | optional | optional | optional |

The title line is `# <type emoji> <ID> · <Title>`, for example `# 🧩 1.2 · Configuration and profiles`. A metadata table follows it: ⏱️ duration, 🧪 type, 🏷️ kind, and the pinned stack versions.

## Commands

- **Commands always go in fenced code blocks, never inline.** The learner copies them and runs them by hand.
- **Show each command in the learner's shells**, in the order of `learner.shells` (for example, PowerShell first, then Bash). Label each block in the line before it.
- **"Where to run commands"** goes near the top. It names the folder (for example `starter/`) and includes the check (`Get-Location` / `pwd`). If a step needs another folder, the step says so.
- **Expected output gets its own block** when it matters. Quote real output, trimmed to the key lines.
- **Inline code is only for identifiers, file names and short values.**

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
