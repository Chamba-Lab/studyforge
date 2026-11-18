# Decisions

Short record of the decisions that shape StudyForge, and why. Only decisions someone could undo without knowing the reason. When one changes, update its entry in the same commit.

## Origin

- **StudyForge distills the MeloStudy labs** (2025–2026): three generations of study repositories.
  - Ad hoc labs (redis, java-concurrency).
  - A spec-kit process with a constitution, per-lab `spec/plan/tasks`, eight workflows and five statuses (containers, mongodb, reactive, kafka).
  - A lean and rigorous `AGENTS.md` + `SYLLABUS.md` + template + verifier (quarkus).

  The third generation is the base. From the second, it brings back learning objectives, `CONCEPT.md`, command dissection, cleanup sections and links from READMEs to code.
- **No per-lab `spec.md` / `plan.md` / `tasks.md`.** They were over-engineering for the need. A lab's design lives in its syllabus row and its README. The separate `architect`, `auditor` and `master-*` workflows became one `build` that designs, builds and self-audits. `governor` (propagating rule changes) lives on inside `review` and `feedback`.

## Format and portability

- **One Agent Skill, not several.** Skills are copied folder by folder, and five skills that share templates break when only one is copied. A single folder with `SKILL.md` routing to `workflows/` installs anywhere in one step.
- **Open standard first, Claude Code plugin as a wrapper.** The skill follows the Agent Skills format, read by 30+ agents (Codex, Gemini CLI, Copilot, Cursor…). `.claude-plugin/` only packages it for Claude Code's plugin manager. Install routes: the plugin, `npx skills add`, or a manual copy.
- **`AGENTS.md` is canonical in every study repository**, and `CLAUDE.md` only imports it. A study repository carries its own rules, so an agent without the skill can keep working from the repository alone.
- **Rigor lives in scripts, not only in prose.** Instructions travel between agents, but discipline does not. `verify.py` makes "solution green, starter red for the right reason" mechanical.

## Language and keys

- **The framework is written in English; lab content uses a configurable language; code is always English.** Early-career learners read the generated labs, not the framework internals, so the content language is what reaches them. `README.es.md` serves the Spanish-speaking community.
- **Keys stay in English in every language, with an emoji.** Status (`pending`, `built`, `done`), topic kind, lab type and section anchors are read by workflows and `verify.py`. A key that changed per language would need every workflow to understand every language. Only legends are translated.
- **Section anchors are emoji.** They are language-neutral, so `verify.py` checks README structure in Spanish, English or any other language without translations.
- **Terms of art and the method's own names stay in English; other headings are translated from a reference table** (1.1). The first review of pytest-lab found literal translations that read oddly ("Disección de comandos") and terms a learner could not search for. Learners meet the English terms at work and in the docs. Writing every heading in English would be the other extreme: it would make beginners' material harder to read.

## Teaching

- **Explaining has rules, not only practicing** (1.1). Up to 1.0 the writing rules covered predicting, traps and verification, and only one line covered explaining. The first review of pytest-lab, by a reader who knows testing, found labs that listed definitions and then asked for tasks. Every concept now goes problem → idea → example → name, and the idea comes before the tool.
- **The syllabus has a learner part and a build map** (1.1). In the same review, the "Owns / builds on" and "Starts from" columns, written for the agent, made the syllabus hard to read, and so did outcomes listed as API names. Nothing parses those columns mechanically, so moving them is not a breaking change.
- **Plan the whole path, build one block at a time** (1.1). pytest-lab planned one block and squeezed unit, acceptance, coverage and flakiness into it. A full plan shows the learner where the path goes and keeps each block on one focus.
- **Sections appear only when they add something** (1.2). Up to 1.1, "In real projects" was required in every challenge and exploration, and "Verified answers" in every exploration. The fresh-eyes review of pytest-lab found those sections filled with summaries of Concepts or with the same answers the 👀 blocks already gave. The verifier now requires only the sections every lab of the type needs. Relaxing a required section does not break existing study repositories.
- **Concepts get `###` headings; each idea is said once; identical commands get one block** (1.2). The same review found flat walls of text with bold lead-ins, one idea explained in four sections, and about 120 lines of PowerShell and Bash blocks with the same command.
- **Concepts do not explain what goes wrong** when a prediction asks that (1.2). "Explain before practicing" (1.1) pushed explanations up to the Concepts section, and five labs ended up answering their own predictions there.
- **A fresh-eyes review closes every block** (1.2). It was optional ("if your agent offers subagents") and was skipped while pytest-lab's block 1 was rewritten twice. Its first run found what the author's own reading had missed.
- **One owner per topic means one lab teaches it, not that only one lab uses it.** The rule keeps a single explanation to maintain and keeps each lab's time for what is new. The glossary is an index that points to owners, so it does not become a second explanation.
- **Three statuses, not five.** Statuses track the author's lifecycle. `done` needs a learner, which is what proves a lab works. Each learner's progress lives in their branch or fork.

## Layout

- **One folder per block, with two-digit numbers and a project last.** In the earlier repositories, projects ended up after every lab or in a separate folder, `000` was duplicated, and numbering had gaps. Block folders show the syllabus in any file explorer. `project-<domain>` sorts after the numbered labs because letters sort after digits.
- **IDs freeze at `built`, and insertions take a letter (`02b`).** Learners merge updates into their solution branches, and renames turn those merges into conflicts. quarkus-lab paid for renumbering with cross-reference searches.
- **A block nobody depends on may be rebuilt with new IDs** (1.3). pytest-lab renumbered its built block 1 when it was rebuilt for 1.1: there were no feedback issues, forks or labs in `done`, so no learner's merge could break. The freeze protects learners, and with no learners it only blocks a better block.
- **`studyforge.toml`, not YAML.** Python reads TOML with the standard library (`tomllib`), so the verifier needs no dependency.
- **The verifier is stdlib-only Python 3.11+.** `verify.ps1` only worked on Windows. Authors and agents need Python. Learners only need their stack's own test command.

## Integrator projects

- **One format: `BRIEF.md` + `acceptance/` + `reference/` + `REVIEW.md`.**
  - Learners can build and compare, or only review.
  - Black-box `acceptance/` tests make "your version meets the brief" objective.
  - The guided review keeps what made quarkus-lab's showcase projects valuable.
- **One maintained reference. Community implementations are linked, not copied.** Divergent copies inside the repository go stale.

## Visuals

- **Mermaid first. Images only when Mermaid falls short** (Excalidraw for concept labs, diagrams.net for complex architecture), and saved as editable SVG. Text formats can be diffed and are written by any agent. PlantUML and D2 are out because GitHub does not render them.
- **The gallery doubles as a rendering test.** A diagram type that does not render in `docs/visuals.md` on GitHub is removed from the recommendations.

## Releases and license

- **SemVer and Conventional Commits, released by release-please.**
  - It is maintained by Google, uses Apache-2.0, and runs only in CI, so its license does not touch ours.
  - It needs no Node or `package.json`, unlike release-it.
  - It releases through a pull request that a person merges, unlike semantic-release, which publishes on every merge.
  - The action is pinned to a commit SHA, with minimal permissions and only the built-in token.
- **Upgrade notes live in the skill, not only in the changelog** (1.3). Upgrading pytest-lab from 1.0 to 1.2 meant reading the skill's diff: the changelog lives outside the skill folder and lists commit titles, not what an existing lab must change. `references/upgrading.md` says, per version, what to copy, which rules built labs must meet, and when to rebuild instead of patching.
- **The upgrade procedure is tested by an agent without context** (1.4.1). The first run, pytest-lab from 1.2.0 to 1.4.0, worked, and its report of every point where it had to guess drove the fixes: prepare the environment before verifying, an upgrade applies the notes and is not a full audit, measurable maintenance and license rules. The author of a procedure cannot test it.
- **0.x until the showcase validates 1.0.0.** `adopt` and upgrade help come in 1.x, and `adopt` will be tested by migrating a real repository from the MeloStudy generations.
- **MIT for everything.** If Chamba Lab's mascot or brand ever appears here, a `NOTICE.md` will exclude them from the license, as in `Chamba-Lab/chambalab-skills`.
