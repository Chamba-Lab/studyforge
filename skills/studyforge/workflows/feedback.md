# Workflow: feedback

Turn what a learner said about a lab into improvements: to that lab, to the earlier labs, to the labs not built yet, and, when the lesson is general, to StudyForge itself.

Read first: the study repository's `AGENTS.md`, `SYLLABUS.md`, `docs/lessons.md`, and [learners](../references/learners.md).

Feedback can arrive at any moment, from the conversation or from a "Lab feedback" issue. Building never waits for it.

## Steps

1. **Collect.** Note which lab the feedback is about, and what the learner said, tried, expected and got. When they share a solution, review it (see [learners](../references/learners.md)).
2. **Classify each point.**

| Kind | Example | Goes to |
|---|---|---|
| Defect in this lab | A step fails, a test passes for the wrong reason, a claim is wrong | Fix the lab |
| A pattern across labs | "Every README hides where to run the commands" | Fix every built lab that has it; adjust the template |
| Pacing or scope | Too long, too easy, too dense | `syllabus` workflow (split, merge, reorder) |
| A rule for this repository | "Always show the Podman command too" | `AGENTS.md` + `docs/decisions.md`, then `review` across labs |
| A lesson for any study path | "Wait for the port before the first request" | `docs/lessons.md`, and propose it upstream (step 5) |

3. **Apply it.**
   - Fix the lab with minimal changes, and look for the same issue in earlier labs.
   - Re-run `python tools/verify.py` on every lab you touch.
   - Write what the next labs must do differently into the syllabus "Notes for the next labs", and into `docs/lessons.md` as a rule under its topic.
4. **Close the loop.**
   - Once the learner has solved the lab and their feedback is applied, set it to `✅ done` in `SYLLABUS.md`.
   - Commit with `fix(lab-<ID>): apply learner feedback` (or `docs(syllabus): …`).
   - Answer the learner (or the issue): what changed, and where.
5. **Upstream general lessons.** A lesson that would help any study path belongs in StudyForge (`references/quality.md`, a template or a workflow). Draft the issue or pull request for `Chamba-Lab/studyforge` and show it to the person. Opening it is outward-facing, so wait for their approval.
6. **Retrospective.** Use the learner's answers to "what was hard / what should I reinforce" to tune the next lab: more practice, a better trap, or a smaller step.
