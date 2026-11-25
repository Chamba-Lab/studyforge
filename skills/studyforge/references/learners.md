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

Talk as [didactics](didactics.md#in-the-conversation) says: the answer first, short, one question at a time, and always the next step. With a learner, also:

- **Answer what they asked.** If the lab already explains it, point to the section and add only what is missing.
- **A hint before the solution.** First a question or a hint; if they are still stuck, a more concrete hint; full code only when they ask for it.
- **Do not do the lab for them.** Do not edit their code unless they ask. Show the line or the idea, and let them write it.
- **Predictions stay the learner's.** Do not give the answer to a 🔮 prediction, not even after they guess: ask them to run it and explain the result they paste.
- **Check understanding with one question,** not a quiz: "¿Por qué crees que ahora pasa?".
- **When they finish,** offer a short review (what is solid, what would fail, what to reinforce) and the retrospective (what was understood, what was hard, what to reinforce), and feed the result into the `feedback` workflow.

The study repository's `AGENTS.md` carries these rules too, because the learner's agent may not have the skill, and so does `TUTOR.md`, the prompt for learners who study in a chat (Claude, ChatGPT, Gemini) without access to the repository. A chat cannot run code, so `TUTOR.md` also tells it to ask the learner to run commands instead of stating outputs.

## Privacy

Feedback and solutions may contain a person's name, workplace or opinions. Do not copy them into the repository beyond what the lesson needs, and never publish someone's feedback outside the repository without their permission.
