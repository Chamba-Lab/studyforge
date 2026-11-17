# Learners

A study path has two kinds of state: the **author's** (is this lab built, verified, validated?) and each **learner's** (how far am I?). Keep them apart.

## Where things live

| State | Lives in | Who changes it |
|---|---|---|
| Lab status (`pending` · `built` · `done`) | `SYLLABUS.md` on the main branch | The author's agent |
| A learner's solutions and progress | The learner's branch (`solutions/<name>`) or fork | The learner |
| Feedback | An issue (from `.github/ISSUE_TEMPLATE/lab-feedback.yml`) or the conversation | The learner |

- **The main branch is the clean template.** Agents never commit solved starters to it.
- **Personal study:** the learner keeps a `solutions/<name>` branch and merges the main branch into it when labs change.
- **Community course:** each learner forks the repository and works in the fork. Their progress is the checkboxes in their copy of each README.
- **`done` means validated:** at least one learner solved the lab and their feedback was applied. In a course, the first complete round of feedback is enough. Later feedback still improves the lab.

## When a built lab has to change

Keep the change minimal, because learners will merge it into their work. Say in the commit and in the reply that people who already solved the lab may get a merge conflict, and where. IDs never change after `built` (see [layout](layout.md)).

## Reviewing a learner's solution

Read the difference against the main branch, limited to the lab, for example `git diff main..solutions/<name> -- labs/01-fundamentals/02-configuration/starter`. Review it as a code review:
- what is solid;
- what would fail in production;
- what to reinforce.

Do not rewrite their code unless they ask you to.

## Helping during a lab

- Answer a question with a hint or a question first. Give full code only if they ask for it.
- Explain the why before the how.
- When they finish, offer a short review and a retrospective (what was understood, what was hard), and feed the result into the `feedback` workflow.

## Privacy

Feedback and solutions may contain a person's name, workplace or opinions. Do not copy them into the repository beyond what the lesson needs, and never publish someone's feedback outside the repository without their permission.
