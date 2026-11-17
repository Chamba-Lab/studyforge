# Visuals

A visual earns its place when it shows something prose would take a paragraph to say. Prefer formats that are **text**: they can be versioned, reviewed in a diff, and written and fixed by any agent. The [visual gallery](https://github.com/Chamba-Lab/studyforge/blob/master/docs/visuals.md) shows each format below rendered, next to its source.

## Which tool, when

| You want to show… | Use | Renders natively on GitHub |
|---|---|:-:|
| A flow, a pipeline, a decision | Mermaid `flowchart` | ✅ |
| Interaction between components over time | Mermaid `sequenceDiagram` | ✅ |
| A lifecycle or state machine | Mermaid `stateDiagram-v2` | ✅ |
| A data model | Mermaid `erDiagram` / `classDiagram` | ✅ |
| Branches and merges (git topics) | Mermaid `gitGraph` | ✅ |
| How a technology evolved | Mermaid `timeline` | ✅ |
| A map of a block or of a concept | Mermaid `mindmap` | ✅ |
| Measured numbers (benchmarks, latencies) | Mermaid `xychart-beta` (with the table next to it) | ✅ |
| A comparison | Markdown table | ✅ |
| What changes between two states | A `diff` code block | ✅ |
| A formula (data, ML, complexity) | LaTeX: `$...$` inline, `$$...$$` as a block | ✅ |
| Terminal output ("what you should see") | A fenced code block | ✅ |
| Notes, tips, traps | Alerts: `> [!NOTE]`, `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]` | ✅ |
| Hints, answers, long detours | `<details><summary>…</summary>` | ✅ |
| Keyboard shortcuts | `<kbd>Ctrl</kbd>+<kbd>C</kbd>` | ✅ |
| An analogy or a whiteboard sketch (concept labs) | Excalidraw, saved as `.excalidraw.svg` (stays editable) | ✅ as an image |
| An architecture Mermaid cannot lay out well | diagrams.net, saved as `.drawio.svg` (stays editable) | ✅ as an image |
| A user interface (consoles, dashboards) | A screenshot in `assets/` | ✅ |
| A terminal session for a landing page | A GIF recorded from a VHS script (`.tape`) | ✅ as an image |

Do not use formats that GitHub does not render (PlantUML, D2, ASCII art for anything but terminal output). They need a build step and fail silently for readers.

## Rules

- **Use Mermaid by default.** Use images only when Mermaid falls short.
- **One diagram per idea, at most ~15 nodes.** If it does not fit, it is two ideas.
- **A diagram never replaces the text.** One sentence before it says what to look at. Images carry alt text. This keeps guides accessible and readable from a terminal or by an agent.
- **Use classic diagram types first.** GitHub does not always ship the newest Mermaid. Check a newer type in the gallery before relying on it, and look at the GitHub preview before marking a lab `built`.
- **Images have a solid background.** A transparent PNG or SVG with dark strokes disappears in GitHub's dark theme.
- **Images live in the lab's `assets/`**, compressed, with descriptive names (`assets/event-loop.excalidraw.svg`).
- **Do not color-code meaning alone.** Pair color with a label or a shape.

## How readers see the diagrams

Lab READMEs include a short "How to read these guides" note (from the repository template). This is what it says:

| Where you read | Mermaid | Excalidraw / diagrams.net files |
|---|---|---|
| GitHub, GitLab | Native | Shown as images |
| VS Code | Built into recent versions of the Markdown preview. On older versions, install *Markdown Preview Mermaid Support*, and remove it once your version has it built in, because the two can conflict | Shown as images; to edit, install the *Excalidraw* or *Draw.io Integration* extensions |
| JetBrains IDEs | Enable Mermaid in the Markdown settings | Shown as images |
| Obsidian | Native | Shown as images |

Check this table against current editor releases when you write the template's note, and keep it short there: one line per editor.
