# Integrator projects

Each block ends with a project. The project applies what the block taught to a **new, small domain**, end to end, with production-level configuration. It consolidates the block without carrying a growing application through every lab.

## Shape

```
project-<domain>/
├── README.md      what this is, how to run the reference, the two ways to use it
├── BRIEF.md       the assignment: domain, requirements, contract, acceptance criteria
├── acceptance/    black-box tests that run against ANY implementation (when feasible)
├── reference/     the reference implementation, all green
└── REVIEW.md      guided review of the reference
```

**The project is atomic.** It inherits no parent build and no code from the labs. It brings its own domain, configuration and dependencies, as a real service would. It follows the same versions as the labs (see [dependencies](dependencies.md)).

## Two ways to use it

1. **Build and compare.** Read `BRIEF.md`, implement it your way in your branch or fork, run `acceptance/` against your implementation, then read `REVIEW.md` and compare it with `reference/`.
2. **Review only.** Read `reference/` guided by `REVIEW.md`, run it, break it, and challenge its decisions.

The README states both paths and recommends one based on the learner's time.

## `BRIEF.md`

- **The one question of the domain.** Name it before writing code: "after this failure, can the customer's money have moved?", "can two appointments overlap?". That question drives the states, the errors, the tests and the metrics. A project without one is a list of features.
- **Context and domain**: actors, entities and rules, in plain language.
- **Contract**: endpoints, messages or the CLI, plus the error contract.
- **Acceptance criteria** as Given/When/Then, each mapped to `acceptance/` when possible.
- **Non-functional requirements** from the block, such as security, resilience, observability or packaging. Name the lab that taught each one.
- **Constraints and freedom**: what is fixed (contract, versions) and what is up to the learner (internal design).
- **Out of scope**: what is missing on purpose.

## `acceptance/`

- **Black box only.** It talks to the contract (HTTP, messages, CLI) and never to internal classes, so it judges any implementation.
- It is required when the project exposes a stable interface. Otherwise `BRIEF.md` says why it does not exist and how the learner can check their work by hand.
- It runs green against `reference/` before the project is `built`. The README says how to point it at another implementation (URL, port, command).
- **When the path teaches testing, the project is turned around too.** The deliverable is a test suite, so `reference/` holds the finished application and its reference suite, the learner writes theirs in a folder of the project (for example `your-suite/`), and `acceptance/` is a mutant hunt over a whole suite: it must pass against the real application and fail against each mutant copy of it. Otherwise a weak suite "passes" as long as the application works. See the project of pytest-lab, block 1.

## `reference/`

- **A finished, reasonable implementation**: a clean architecture that is not over-engineered, follows the stack's best practices, and keeps every test green.
- **Run the packaged artifact** (jar, image, binary) against real dependencies at least once before calling it done, and run the README tour word for word. Those runs find defects that the tests miss.

## `REVIEW.md`

- **Reading order**: which file first, and why.
- **Decisions and their reasons**, each linked to the lab that taught it.
- **Traps hit while building it.**
- **🔨 Break it yourself**: a table of single changes. Each row names the test that turns red and quotes the real failure. Every row was run in a scratch copy.
- **What is deliberately missing**, and **questions to challenge** the design.

## Community implementations

Keep **one maintained reference** in the repository. Implementations from the community are linked from the README (to their forks or branches), not copied in. Several divergent copies inside the repository go stale.
