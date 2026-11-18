# 🧪 Examples

## pytest-lab: the showcase

**[Chamba-Lab/pytest-lab](https://github.com/Chamba-Lab/pytest-lab)**, "Testing en Python con pytest", is a complete study path built with StudyForge through its own workflows (`syllabus` → `init` → `build`). It is a separate repository on purpose: it is used like any real study path, with forks, solution branches and feedback issues. Its `studyforge.toml` pins the framework version it follows, so upgrading it shows the `review` workflow at work.

Its [syllabus](https://github.com/Chamba-Lab/pytest-lab/blob/master/SYLLABUS.md) plans four blocks, one per level of the test pyramid plus suite quality, and block 1 (unit tests) is built:

| Lab | Type | What it shows |
|---|---|---|
| [1.1 · Qué es una prueba y sus tipos](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-unit-tests/01-what-is-a-test) | 💭 concept | A `CONCEPT.md` that starts from a problem and shows the three levels on one example, a diagram as an image with a solid background, and a self-assessment with hidden answers |
| [1.2 · Primeras pruebas con pytest](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-unit-tests/02-first-tests) | 🧩 challenge | A **testing lab turned around**: the learner writes the tests, and a *mutant hunt* validates them. Concepts introduced on a different function than the tasks, and four verified traps |
| [1.3 · Diseño de casos de prueba](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-unit-tests/03-test-case-design) | 🧩 challenge | **Concept before tool:** equivalence classes and boundary values first, then `parametrize`. Two boundary mutants that only the boundary task can kill |
| [1.4 · Organizar la suite](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-unit-tests/04-organize-suite) | 🧩 challenge | Fixtures, `scope` and `conftest.py`, with structure checks (`--fixtures`, `--collect-only`, `ast`) and verified traps such as `ScopeMismatch` and strict markers |
| [1.5 · Dobles de prueba](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-unit-tests/05-test-doubles) | 🧩 challenge | The five test doubles explained before they are used; seven mutants, injected dependencies, a fake clock and `create_autospec` |
| [1.6 · Cobertura](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-unit-tests/06-coverage) | 🔭 exploration | A finished `demo/`. Each experiment asks for a prediction first and quotes real output, including 100% **branch** coverage with a live bug |
| [1.P · Dividir la cuenta](https://github.com/Chamba-Lab/pytest-lab/tree/master/labs/01-unit-tests/project-split-bill) | 🏗️ project | A **testing project turned around**: the application is finished, the learner writes the suite, and `acceptance/` is a mutant hunt over the whole suite (12 package mutants). `REVIEW` shows which test kills each mutant |

Plus a [glossary](https://github.com/Chamba-Lab/pytest-lab/blob/master/GLOSSARY.md) of terms of art, each linked to the lab that owns it.

### What building it changed in StudyForge
- **The verifier** stopped comparing test counts between starter and solution (parametrized solutions legitimately run more cases) and now warns about JUnit *errors* instead.
- **The Python stack note** became *proven*. It now covers the native `[tool.pytest]` table, the mutant hunt (per lab and over a whole suite), and two Windows gotchas: a virtual environment silently off `PATH`, and the code page of a child process.
- **The gallery** confirmed that every visual format renders on GitHub, and found the LaTeX-braces and dark-mode rules.
- **StudyForge 1.1** came from its first review: rules for explaining (problem, idea, example, name), terms of art in English, a syllabus with a learner part and a build map, and planning the whole path before building one block. pytest-lab's block 1 was rebuilt with them.

Its [`docs/lessons.md`](https://github.com/Chamba-Lab/pytest-lab/blob/master/docs/lessons.md) records each lesson as it was learned.

The `checks` workflow of this repository clones pytest-lab and runs the **current** verifier on it: a framework change that breaks the showcase turns CI red before it is released.
