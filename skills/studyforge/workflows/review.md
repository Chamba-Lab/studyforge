# Workflow: review

Audit labs against the current standard and fix the gaps. Use it for one lab, a block or the whole repository. Also use it when a rule changes and the change has to reach every lab, or when the repository follows an older StudyForge version.

Read first: the study repository's `AGENTS.md`, `SYLLABUS.md`, `docs/decisions.md`, and [quality](../references/quality.md) and [writing](../references/writing.md).

## Steps

1. **Define the scope:** one lab (`<ID>`), a block, everything, or one rule applied everywhere.
2. **Check the framework version.**
   - If `studyforge` in `studyforge.toml` is older than this skill's version, list what changed in between, using the StudyForge changelog.
   - **MINOR and PATCH** changes are additive: offer them.
   - **MAJOR** changes come with migration notes: follow those.
   - Update `tools/verify.py` from the skill.
3. **Audit.** For each lab in scope:
   - Run `python tools/verify.py --lab <ID>` for the structure, the green solution and the red starter.
   - **Orphan concepts:** a command, operator, flag or annotation used in an exercise but not explained in the README or `CONCEPT.md`.
   - **Explanation:** concepts listed as bare definitions, with no problem or example before the task that needs them; a tool shown before the idea it expresses; terms of art or acronyms translated literally or used without a gloss; section titles that differ from the reference table in [writing](../references/writing.md#section-anchors).
   - **Spoilers before a prediction:** in Concepts, in the scenario's tables, in the dissection or in the starter.
   - **Noise:** optional sections with nothing of their own, ideas explained twice, boilerplate repeated across labs, long sections without `###` parts, identical commands duplicated per shell.
   - **Syllabus readability:** API names or terms taught later in topics and outcomes, uneven technicality across rows, blocks that mix levels, and a path that plans only the blocks already built.
   - **Unverified claims:** outputs, defaults or error messages with no run behind them, or written for an older version.
   - **Tests that pass for the wrong reason**, and starter tests that are not red.
   - **Missing teaching devices:** a trap, a "predict first" step, the self-assessment, the command dissection when there is new syntax, or cleanup when the lab creates resources.
   - **Broken or outdated** links, versions and diagrams.
   - **Ownership:** the lab re-teaches something another lab owns.
4. **Present the findings** ranked by impact on the learner, with a recommendation. Fix immediately whatever is clearly a defect. Wait for the person's decision on anything that changes scope or the syllabus.
5. **Fix with minimal changes.** Learners may have to merge them (see [learners](../references/learners.md)). After any change, re-run the solution (green) and the starter (red where expected), and re-check every claim the change touched.
6. **Record.**
   - Lessons go in `docs/lessons.md`, and rule changes in `AGENTS.md` and `docs/decisions.md`.
   - Set `studyforge` in `studyforge.toml` to the new version.
   - Commit with `fix(lab-<ID>): …` or `chore: upgrade to StudyForge <version>`.
7. **Report** what changed, what was verified, and which labs learners may need to re-merge.
