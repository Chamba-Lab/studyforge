# Jupyter notebooks

Notebooks fit data and machine learning topics, where text, code and charts belong together. GitHub renders `.ipynb` files natively.

> [!NOTE]
> Starting values, not yet proven by a StudyForge pilot.

## `studyforge.toml`

```toml
[[stack]]
id = "notebook"
detect = "*.ipynb"
command = "jupyter nbconvert --to notebook --execute --output-dir .executed *.ipynb"
timeout = 900
```

`nbconvert --execute` runs every cell in order. It exits with an error when a cell raises, which makes a notebook "red" or "green" with no extra tooling. There is no JUnit report, so `verify.py` relies on the exit code.

## Lab shape

- **Challenge:** `starter/` and `solution/` each hold the same notebook.
  - In the starter, the cells under study contain `# TODO` and `raise NotImplementedError`, and each task ends with an **assert cell** that checks the result (`assert df.shape == (1200, 8)`).
  - The solution notebook runs top to bottom.
- **Exploration:** a finished notebook in `demo/`. The README asks the learner to change parameters and predict the effect before re-running.
- Put dependencies in a `requirements.txt` or `pyproject.toml` next to the notebook, with pinned versions.
- Keep data small and versioned in `data/`, or downloaded by a first cell from a stable official URL that the README names.

## Ignore rules

```gitignore
.executed/
.ipynb_checkpoints/
.venv/
.env
```

## Gotchas

- **Clear outputs before committing the starter,** so the answers do not leak. The solution may keep its outputs when they teach something (charts).
- **Hidden state:** a notebook that only works when its cells run out of order is broken. `nbconvert --execute` runs them in order, which is exactly the check you want.
