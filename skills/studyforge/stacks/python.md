# Python (pytest)

## `studyforge.toml`

```toml
[[stack]]
id = "python"
detect = "pyproject.toml"
command = "python -m pytest -q --junitxml=.reports/junit.xml"
reports = ".reports/junit.xml"
timeout = 600
```

With uv, set `command = "uv run pytest -q --junitxml=.reports/junit.xml"`. uv creates the environment from the lockfile.

## Scaffolding

- Each variant has its own `pyproject.toml` (and `uv.lock` when using uv) and its own virtual environment. Do not share an environment across labs.
- Keep the import path simple: put a `src/` package next to `tests/`, and set `pythonpath = ["src"]` under `[tool.pytest.ini_options]`.

## Making a starter

The function under study raises `NotImplementedError("TODO")`. The module still imports, so pytest collects every test, and the target tests fail.

## Ignore rules

```gitignore
.venv/
__pycache__/
.pytest_cache/
.reports/
*.egg-info/
.env
```

## Gotchas

- **Collection errors look like zero tests.** If a test module fails to import, pytest reports an error rather than failing assertions. `verify.py` treats "red with no failing test" as a problem.
- **On Windows the launcher may be `py`, not `python`.** Set `command_windows` if the learner's machine needs it.
