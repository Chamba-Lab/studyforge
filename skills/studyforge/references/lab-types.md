# Lab types

Choose the type per topic when designing the syllabus. Every lab has the same sections in its README regardless of type (see [writing](writing.md)). What changes is what sits next to the README and how the lab is verified.

| Type | Use it when | Next to the README | Verified by |
|---|---|---|---|
| 🧩 `challenge` | The behavior can be checked by tests | `starter/`, `solution/` | Tests: `solution` green, `starter` red on the target tests |
| 🔭 `exploration` | The topic is understood by observing a working system (infrastructure, tooling, performance, operations) | `demo/` | Every step run in order; "what you should see" quotes real output |
| 💭 `concept` | There is nothing to run yet (mindset, theory, comparisons) | `CONCEPT.md` | Self-assessment with hidden answers; every claim sourced |
| 🏗️ `project` | A block ends | `BRIEF.md`, `acceptance/`, `reference/`, `REVIEW.md` | See [projects](projects.md) |

## 🧩 Challenge

```
NN-<slug>/
├── README.md
├── CONCEPT.md     optional, when the theory is long
├── starter/       compiles and runs, has TODOs, the target tests fail
└── solution/      complete, every test green
```

- **Tests are the acceptance criteria.** Each task names the test class that validates it.
- **The starter hides the mechanism under study, not the app.** Replace only the code being taught with a `TODO`, and keep everything else working. A starter that cannot even build is not "red": its tests never run.
- **Each target test fails for the right reason.** A "404 for an unknown id" test passes on its own when the route does not exist yet. Make negative tests first prove that the valid case works.
- **Regression guards are welcome.** A test that is green from the start protects something the learner must not break, such as an earlier domain this lab builds on. Name it as a guard in the README.
- **Labs about testing are turned around.** The production code is finished and the learner writes tests. Two ways to validate them:
  - **Arrangement missing:** the assertions are written and the setup is missing (mocks, clock, fixtures). This fits labs about test tooling inside a larger framework.
  - **Mutant hunt (preferred when the learner writes whole tests):** a test runs the learner's test file in a subprocess, first against the real module (it must pass) and then against each mutant in `tests/mutants/<id>/` (it must fail). Stubs call `skip("TODO …")`, so each task turns its own mutants green. A "bug fixed" variant validates an expected failure (`xfail`). See the [Python stack note](../stacks/python.md) and pytest-lab labs 1.2–1.4.
- Build the solution first, then derive the starter from it, then check task by task that each step turns its tests green (see [quality](quality.md)).

## 🔭 Exploration

```
NN-<slug>/
├── README.md      the guide is the deliverable
├── CONCEPT.md     optional
└── demo/          a working project, scripts or manifests
```

- **The demo is finished.** The learner switches options on and off, breaks things on purpose, and watches what happens.
- **Every step is "🔮 predict first → run → compare".** Show the expected output and its explanation inside a `<details>` block after the commands. Visible right under the prediction, it would be the answer.
- **Run every command in the guide, in order, on a clean machine state.** Quote real numbers and messages. A guide step that edits a file must end by restoring it, or must say clearly that it leaves the file changed.
- **Name everything you create** (containers, images, namespaces) after the lab, and end with a 🧹 cleanup section that removes only those.
- When the demo has a build, `tools/verify.py` checks that it builds. The steps themselves are checked by running them.

## 💭 Concept

```
NN-<slug>/
├── README.md      objectives, why it matters, self-assessment
├── CONCEPT.md     the explanation
└── assets/        optional diagrams (Excalidraw works well here)
```

- **Use it for the mindset that later labs need**: analogies, mental models, comparisons, history ("callbacks → futures → streams").
- **Depth is mandatory.** Explain the internal mechanics, not just definitions. Every non-obvious claim links its source.
- **Self-assessment is the check.** Write 5 questions at interview level, each with its answer in a `<details>` block. Add a thought experiment where it helps ("what happens to thread X when…").
- Keep concept labs rare: most topics learn better with something to run.

## Common to every type

- **Duration is 1–2 h.** Split the lab if it grows.
- **Remove from generated projects whatever does not serve the topic**: Dockerfiles, sample READMEs, unused dependencies.
- **Every scenario in the README links its code and tests** with relative paths, so a learner can go from text to file in one click.
- **Commands are native to the stack** (`mvn test`, `npm test`, `docker compose up`). A `Makefile` or script may exist as a shortcut, never as the only way.
