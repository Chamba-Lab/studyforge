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
- **Security baseline**: stable, patched versions, with no known vulnerabilities in what you pin. Check before pinning.
- **A shared parent manages versions, not behavior.** For example, test-runner configuration that one kind of module needs can break another kind. Keep plugin configuration in the modules that need it.
- **Upgrading** follows a checklist in `AGENTS.md`:
  1. Read the release notes and the migration guide.
  2. Change every lab.
  3. Run `tools/verify.py`.
  4. Re-check every claim that quotes the old version.
