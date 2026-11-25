# Didactics

How to explain anything to a learner: in a lab README, in `CONCEPT.md`, in a project brief, or in the conversation. These rules do not depend on the lab type or on the files of a study repository. How they take shape in lab material lives in [writing](writing.md).

## Explaining

The teaching devices make the learner practice. Explaining makes sure they understood what to practice first. Material that only lists definitions and then asks for a task is a test, not a lesson.

- **Introduce before you use.** Every new concept arrives in this order:
  1. **The problem**, starting from something the learner already knows: "comparar `0.1 + 0.2` con `0.3` da `False`; ¿por qué?".
  2. **The idea** in one or two plain sentences.
  3. **A minimal example** that shows it working, on a case different from the task's.
  4. **The name**: the term of art, glossed the first time.

  A concept that appears in a task, a command or a hint without this introduction (here or in its owner lab) is an orphan concept, and a defect.
- **Concept first, tool second.** Say what the idea is in terms independent of the tool, then show how the tool expresses it: "una prueba parametrizada es una misma prueba que corre con varios datos" before `@pytest.mark.parametrize`. The learner should be able to take the idea to another tool.
- **A worked example before the task.** Before asking the learner to do something new, show it done once, complete and on a different case. The task then asks for the same skill on new data, not for guessing the syntax.
- **Analogies only when they map.** Use one when it maps the mechanism, not just the mood, and say where it stops working: "como una alarma de humo… pero, a diferencia de la alarma, una prueba solo detecta lo que le pediste revisar".
- **Bridge to what came before.** Open with one sentence that connects to what the learner already did: "En el lab 1.2 escribiste una prueba por caso; aquí…".
- **Keep the jargon level even.** Titles, objectives and the syllabus use words the learner knows at that point. A term not yet taught gets a gloss or waits for its lab. Acronyms count as terms: the first "CI" or "API" a learner meets gets its gloss.
- **Only what is used now.** A concept the current tasks do not need belongs to the lab that uses it. A short "you will use this in…" mention is fine; a full explanation is not.

## Terms of art

- **Terms of art stay in English** when that is how the trade uses them (test suite, fixture, mock, stub, Arrange-Act-Assert, pull request, deployment). The first time a learner meets one, give it a short gloss in the content language: "un *fixture* (la preparación que una prueba necesita)". From then on, use the English term. A learner who only knows a literal translation cannot search the docs or follow a team conversation. Translate the term only when the content language has an established equivalent that practitioners use ("prueba unitaria" is used; "accesorio" for fixture is not).
- **Plain, neutral language**, without local slang. Use short sentences and active voice. Explain the *why* before the *how*.

## One idea at a time

- **One idea per unit.** A paragraph, a `###` part, a diagram or a message carries one idea. When a unit needs "and" to state its point, split it.
- **Lead with the point.** The first sentence of a unit says what the learner should take away; the rest supports it. A heading that states the point ("Una prueba parametrizada repite la misma prueba con varios datos") beats a heading that only names the topic, where the format allows it.
- **Show instead of listing.** Two or more things compared go in a table; a flow goes in a diagram (see [visuals](visuals.md)). A paragraph that walks through five options is a table waiting to happen.

## Say each thing once

Each idea has one home. Other places that need it refer back in a few words; they do not explain it again. Two explanations of one idea drift apart, and the learner cannot tell which one is right.

## Questions that make the learner think

Predictions, self-assessment questions and the questions an agent asks during a lab follow the same rules.

- **Ask for retrieval or reasoning, not recognition.** "¿Qué imprime este código y por qué?" makes the learner rebuild the idea; "¿Cuál de estas es la definición de *fixture*?" only checks they have seen it.
- **One idea per question.** A question that checks two things cannot tell which one the learner missed.
- **Wrong options are real mistakes.** In a multiple-choice question, every wrong option is a misconception a learner actually has, not filler that nobody would pick.
- **The answer explains why.** A hidden answer that only says "B" teaches nothing to the learner who picked C. Say why the right answer is right and why the tempting one is wrong.

## In the conversation

A reply in the chat is read once, on the spot, often by someone who is stuck. It follows every rule above, and these:

- **Lead with the answer.** The first line answers the question or says the result; the why comes after, if it is needed.
- **Short by default.** A few lines. When an explanation needs more, it belongs in a file (the lab's Concepts, a `CONCEPT.md`): point to it, or offer to write it there, instead of pasting it into the chat.
- **One question at a time.** When you need something from the person, ask one question. When several are unavoidable, ask at most three, numbered, each with examples or options and the answer you recommend.
- **Say only what changes for the person.** Not the list of everything you read or ran, and not a recap of what they just said.
- **End with the next step.** The last line says what the person does now, in one sentence: "Tu siguiente paso: corre las pruebas del lab 1.2 y dime qué falla." When nothing is pending on their side, say what you will do next.


- **Concise and concrete.** One idea per paragraph, and a table when you are comparing.
- **Proofread before you share.** Read the text once only for form: capital letters in headings, list items and table cells; proper nouns as their owners write them (Git, GitHub, Python, PowerShell); accents and punctuation of the content language. Form mistakes cost the learner's trust as much as wrong facts.
- **No filler, no hype, no promises.** If something is uncertain, say what was measured and where.
