# 🧪 Examples

## pytest-lab: the showcase

**[Chamba-Lab/pytest-lab](https://github.com/Chamba-Lab/pytest-lab)**, "Testing en Python con pytest", is a complete study path built with StudyForge through its own workflows (`syllabus` → `init` → `build`). It is a separate repository on purpose: it is used like any real study path, with forks, solution branches and feedback issues. Its `studyforge.toml` pins the framework version it follows, so upgrading it shows the `review` workflow at work.

| Lab | Type | What it shows |
|---|---|---|
| [1.1 · ¿Qué probar y por qué?](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-fundamentals/01-why-test) | 💭 concept | `CONCEPT.md` with a diagram as an image with a solid background, verified claims, and a self-assessment with hidden answers |
| [1.2 · Primeras pruebas](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-fundamentals/02-first-tests) | 🧩 challenge | A **testing lab turned around**: the learner writes the tests, and a *mutant hunt* validates them. It has four verified traps |
| [1.3 · Parametrizar y organizar](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-fundamentals/03-parametrize) | 🧩 challenge 🆕 | A "bug fixed" variant that validates a strict `xfail`, structure checks with `--collect-only`, and pytest 9's native TOML configuration |
| [1.4 · Fixtures y dobles](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-fundamentals/04-fixtures-doubles) | 🧩 challenge | Seven mutants, injected dependencies, a fake clock and `create_autospec` |
| [1.5 · Cobertura e inestabilidad](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-fundamentals/05-coverage-flaky) | 🔭 exploration | A finished `demo/`. Each experiment asks for a prediction first and quotes real output, including 100% coverage with a live bug, plus a cleanup section |
| [1.P · Dividir la cuenta](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-fundamentals/project-split-bill) | 🏗️ project | `BRIEF` + black-box `acceptance/` (any implementation, any language) + `reference/` + a `REVIEW` with 13 mutations that were run and quoted |

### What building it changed in StudyForge
- **The verifier** stopped comparing test counts between starter and solution (parametrized solutions legitimately run more cases) and now warns about JUnit *errors* instead.
- **The Python stack note** became *proven*. It now covers the native `[tool.pytest]` table, the mutant hunt, and two Windows gotchas: a virtual environment silently off `PATH`, and the code page of a child process.
- **The gallery** confirmed that every visual format renders on GitHub, and found the LaTeX-braces and dark-mode rules.

Its [`docs/lessons.md`](https://github.com/Chamba-Lab/pytest-lab/blob/master/docs/lessons.md) records each lesson as it was learned.

The `checks` workflow of this repository clones pytest-lab and runs the **current** verifier on it: a framework change that breaks the showcase turns CI red before it is released.
