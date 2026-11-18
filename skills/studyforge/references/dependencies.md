# Dependency strategy

Labs that use the same toolchain can share their build configuration or keep it apart. Decide this **with the syllabus**, record it in `docs/decisions.md`, and set `dependencies.strategy` in `studyforge.toml`.

| Strategy | What it is | Choose it when | Cost |
|---|---|---|---|
| `shared-parent` | Every lab inherits one parent build (a Maven parent POM, a root `package.json` with workspaces, a shared `pyproject`). Versions are declared once. | Every lab uses the same framework and nearly the same libraries (all labs on Spring WebFlux X.Y, say) | Each lab pulls dependencies it does not use; a lab cannot be copied out alone |
| `independent` | Each lab variant is a complete project with its own build. Versions are kept identical by rule and upgraded together. | Labs need different libraries; each lab should open and run alone; a platform BOM already manages versions | One version change touches every lab (scripted, all at once) |
| `per-block` | One parent per block, or a parent only for the blocks that share a stack | Some blocks share a stack and others do not | More rules to explain |

## Rules for every strategy

- **Projects never inherit.** They are atomic (see [projects](projects.md)), even under `shared-parent`.
- **One version of each library across the repository.** Upgrade all labs together, never one by one. The only exception is a lab whose topic *is* an older version (an upgrade lab), and the README says so.
- **Prefer the platform's own version management** (a BOM, a constraints file) over pinning each library. A library outside it needs an explicit version and a written justification in the lab README.
- **Security baseline**: stable, patched versions, with no known vulnerabilities in what you pin. Check before pinning, with the checklist below.
- **A shared parent manages versions, not behavior.** For example, test-runner configuration that one kind of module needs can break another kind. Keep plugin configuration in the modules that need it.
- **Upgrading** follows a checklist in `AGENTS.md`:
  1. Read the release notes and the migration guide.
  2. Change every lab.
  3. Run `tools/verify.py`.
  4. Re-check every claim that quotes the old version.

## Choosing a library

Every library a lab adds runs on the learner's machine, so pick it as you would for a production project. Check every library the repository pins, including the one the path teaches: only the language runtime and its standard library are exempt. Record the result in the study repository's `docs/decisions.md` as a dated section with one table row per library (version, the result of each item, and how it was checked):

- [ ] **No known vulnerabilities**, in the library and in what it pulls in. Run the ecosystem's audit tool on every file that pins versions (`pip-audit -r requirements.txt`, `npm audit`, the OWASP `dependency-check` plugin for Maven) and query [OSV](https://osv.dev).
- [ ] **Maintained:** a release in the last 12 months, a repository that is not archived, and an organization or at least two people committing in the last year.
- [ ] **Adopted:** among the most used of its alternatives (monthly downloads, dependents), so the learner meets it at work and can find answers. When a less used option wins, write why (for example, "the popular one does not run on Windows").
- [ ] **Compatible license** with the study repository. Permissive licenses (MIT, Apache-2.0, BSD, ISC) are fine. A weak copyleft license (LGPL, MPL) is fine for a library the learner installs unmodified and the repository never copies; write it down. A strong copyleft license (GPL, AGPL) needs the person's decision.
- [ ] **Runs on the learner's environment** from `studyforge.toml` (operating system, shells, containers), checked by running it, not by reading its docs.
- [ ] **Few dependencies of its own.** Each one is one more thing to audit and upgrade; prefer the standard library when it teaches the same thing.
- [ ] **Tools that change code or files** (mutation testing, formatters, code generators) are tried first in a scratch copy: check what they modify, and what is left behind if a run is cut halfway.

When a library already in built labs fails an item, present the options (replace it, or keep it and record why) and let the person decide.

Then keep checking: add the audit tool to the repository's CI, on every change and on a weekly schedule, so a new advisory shows up even when nobody touches the labs.
