# Layout, names and IDs

## A study repository

```
<topic>-lab/
├── AGENTS.md              rules for any agent (single source)
├── CLAUDE.md              only "@AGENTS.md"
├── README.md              landing page for learners
├── SETUP.md               tools, versions, checks
├── SYLLABUS.md            plan and status
├── GLOSSARY.md            optional: terms of art, each linked to its owner lab
├── studyforge.toml        configuration (see below)
├── docs/
│   ├── decisions.md
│   └── lessons.md
├── tools/
│   └── verify.py          copied from the skill by init
├── .github/ISSUE_TEMPLATE/lab-feedback.yml
└── labs/
    ├── 01-fundamentals/
    │   ├── 01-dev-mode/
    │   ├── 02-configuration/
    │   ├── 02b-config-sources/     inserted later, nothing renumbered
    │   ├── 03-cdi/
    │   └── project-task-board/     always last in its block
    └── 02-rest/
        └── …
```

## Naming rules

1. **Each level uses two digits with a leading zero** (`01`…`99`). This makes alphabetical order match the syllabus order on GitHub, in editors and in file explorers.
2. **A block is a folder: `NN-<slug>`.** Labs go inside it as `NN-<slug>` or `NNx-<slug>` (where `x` is a letter `b`–`z`).
3. **The project is named `project-<domain>`.** Letters sort after digits, so the project lands at the end of its block without a number. There is one project per block, and a final capstone gets its own block.
4. **Slugs** are kebab-case, English, ASCII only, at most four words, and contain no version numbers: `02-configuration`, not `02-config-quarkus-3-40`. Titles inside the README are written in the content language.
5. **Fixed names inside a lab:**
   - Challenge: `README.md`, `starter/`, `solution/`.
   - Exploration: `README.md`, `demo/`.
   - Concept: `README.md`, `CONCEPT.md`.
   - Any type may add `assets/`.
   - Project: `README.md`, `BRIEF.md`, `acceptance/`, `reference/`, `REVIEW.md`.
   - `CONCEPT.md` is optional in every type except `concept`.

## IDs

- **The short ID is `<block>.<lab>`**: `1.2`, `1.2b`, and `1.P` for the project. Use it in conversation, in the syllabus and in commits.
- **IDs freeze when a lab becomes `built`.** Learners keep their solutions in branches and forks, and a rename makes their merges painful.
  - Exception: a block nobody depends on yet (no feedback issues, no known forks or solution branches, no lab `done`) may be rebuilt with new IDs. Record why in `docs/decisions.md`.
  - Before `built`: renumber freely, then search the repository for old references (`grep -rn "lab 1\.4"`).
  - After `built`: insert with a letter (`02b`, `02c`). The letter only says *where* the lab goes; its kind (deep-dive, alternative…) lives in the syllabus.
  - Retired labs leave a gap, and their ID is never reused.
- **Unique artifact names per lab variant**, such as `<repo>-1-2-starter`. This way two labs open in the same IDE or build cache never collide.

## `studyforge.toml`

```toml
# StudyForge configuration. Read by the workflows and by tools/verify.py.
studyforge = "0.1.0"            # framework version this repository follows

[path]
title = "Kafka, from zero to job-ready"
goal = "Use Kafka in a backend job: produce, consume, test and operate"

[language]
content = "es"                  # guides, concepts, READMEs (BCP 47: es, en, pt-BR…)
                                # code, identifiers, folders and commits: always English

[learner]
os = "windows"                  # windows | macos | linux
shells = ["powershell", "bash"] # order in which guides show commands
containers = "docker"           # docker | podman | none

[dependencies]
strategy = "independent"        # shared-parent | independent | per-block

[[stack]]                       # one table per toolchain used by the labs
id = "maven"
detect = "pom.xml"              # file that identifies a variant of this stack
command = "mvn -q -B clean verify"
command_windows = "mvn -q -B clean verify"          # optional override
reports = "**/target/surefire-reports/TEST-*.xml"   # optional JUnit XML, to count tests
timeout = 900                   # seconds
```

`tools/verify.py` goes through each variant (`starter/`, `solution/`, `demo/`, `reference/`) and runs the command of the first stack whose `detect` file exists there. Stack notes in [stacks/](../stacks/README.md) give working values.

## Commits and branches

- **Conventional Commits in English.** Lab scopes: `feat(lab-1.2): …`, `feat(project-1): …`, `fix(lab-2.3): …`, `docs(syllabus): …`, `chore(tools): …`.
- **One commit per lab, made when the lab is built and verified.** Push at milestones, such as a lab that meets the definition of done or a finished block, or when the author asks.
- **`master`/`main` is the clean template.** Learners keep their work in their own branch (`solutions/<name>`) or fork. Agents never commit solved starters to the main branch (see [learners](learners.md)).
- **Nothing secret is ever committed**, including `.env` files and real tokens. A throw-away test key is labeled as such.
