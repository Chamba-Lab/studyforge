# Python (pytest)

Proven by the showcase [pytest-lab](https://github.com/Chamba-Lab/pytest-lab) (Python 3.12 and 3.15, pytest 9.2).

## `studyforge.toml`

```toml
[[stack]]
id = "python"
detect = "pyproject.toml"
command = "python -m pytest -q -p no:cacheprovider --junitxml=.reports/junit.xml"
reports = ".reports/junit.xml"
timeout = 300
```

- Use `python -m pytest`, not bare `pytest`. It runs the pytest of the active interpreter, with the current folder on the import path.
- `-p no:cacheprovider` keeps verification runs from leaving `.pytest_cache/` folders behind.
- With uv, set `command = "uv run pytest -q --junitxml=.reports/junit.xml"`. uv creates the environment from the lockfile.

## Scaffolding

- **Configuration:** each variant has a `pyproject.toml` with the native table **`[tool.pytest]`** (pytest 9+): `testpaths = ["tests"]` and `pythonpath = ["."]` (or `["src"]`). Values have real TOML types there. The older `[tool.pytest.ini_options]` is text-based, and the two tables cannot coexist.
- **Environment:** a single virtual environment at the repository root, with `requirements.txt` holding the pinned versions, suits labs that share the same libraries (strategy `shared-parent`). Use one environment per variant only when the labs really need different libraries. Projects declare their own dependencies either way.

## Making a starter

- **Code labs:** the function under study raises `NotImplementedError("TODO")`. The module still imports, so pytest collects every test and the target tests fail.
- **Testing labs** (the learner writes the tests): stubs call `pytest.skip("TODO …")`, and the learner's tests are validated by a *mutant hunt*. A test runs the learner's test file in a subprocess, first against the real module (it must pass) and then against each mutant (it must fail). A `conftest.py` puts the mutant first on `sys.path` when an environment variable names it. With `skip` instead of `fail`, each task turns its own mutants green, so the progressive check works. pytest-lab labs 1.2–1.4 are working examples.

## Ignore rules

```gitignore
.venv/
__pycache__/
.pytest_cache/
.reports/
.coverage
htmlcov/
*.egg-info/
.env
```

## Gotchas

- **Collection errors are errors, not failures.** When a test module fails to import, the JUnit report counts an *error*. `verify.py` warns about errors in a red starter, because "red" then means "broken", not "failing for the right reason".
- **Check which Python runs.** On a machine with Anaconda, activating a virtual environment from Git Bash can silently leave it off `PATH`: Anaconda's `cygpath` returns `/cygdrive/...` paths, which Git Bash does not understand. `python -c "import sys; print(sys.prefix)"` must show the environment. When verifying from an agent, put the environment's `Scripts/` (Windows) or `bin/` folder first on `PATH` yourself.
- **A child Python on Windows writes in the console code page.** A test that runs pytest or Python as a subprocess and reads its output must set `PYTHONIOENCODING=utf-8` for the child and decode with `errors="replace"`. pytest prints symbols such as `±` (from `approx`) that cp1252 cannot hold, and the decoding fails in a reader thread, which pytest reports as `PytestUnhandledThreadExceptionWarning`.
- **On Windows the launcher may be `py`, not `python`.** Set `command_windows` if the learner's machine needs it.
