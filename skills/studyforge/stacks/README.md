# Stack notes

A stack note tells the workflows how to build and verify labs for one toolchain. These notes are **starting values**: confirm them against the versions a study repository pins, and record what you learn in that repository's `docs/lessons.md`. Lessons that hold for every repository come back here.

| Stack | Note | `detect` | Typical lab types |
|---|---|---|---|
| Java with Maven | [maven](maven.md) | `pom.xml` | challenge, exploration, project |
| Node.js (npm) | [node](node.md) | `package.json` | challenge, exploration, project |
| Python (pytest) ✅ proven | [python](python.md) | `pyproject.toml` | challenge, exploration, project |
| Jupyter notebooks | [notebook](notebook.md) | `*.ipynb` | challenge, exploration (data, ML) |
| Containers (Docker / Podman) | [containers](containers.md) | `compose.yaml` | exploration |

## What every note covers

1. **`[[stack]]` values** for `studyforge.toml`: `detect`, `command` (and `command_windows` if it differs), `reports`, `timeout`.
2. **Scaffolding**: how to start a lab variant, usually by copying the build files of the latest lab.
3. **Making a starter**: it builds and runs, and its target tests fail.
4. **Ignore rules** for `.gitignore`.
5. **Gotchas** worth knowing before the first lab.

A repository can declare several `[[stack]]` tables (for example, Maven labs plus a containers exploration). `verify.py` uses the first one whose `detect` pattern matches inside each variant folder, so list the most specific stack first.

A stack that is not listed here works too. Write its `[[stack]]` values in `studyforge.toml` and its notes in the repository's `AGENTS.md`, and consider contributing the note back.
