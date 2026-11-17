<!-- studyforge: The assignment, in the content language. Precise enough to implement without reading the reference. Delete these comments. -->
# 📋 Brief · <Project: domain>

## The question of the domain
> <The one question everything else serves, e.g. "after this failure, can the customer's money have moved?">

## Context
<Who uses it, what problem it solves, in plain language.>

## Domain
| Entity | Rules |
|---|---|
| <Entity> | <Invariants, states, limits> |

```mermaid
stateDiagram-v2
    [*] --> <State>
    <State> --> <State>: <event>
```

## Contract
<Endpoints, messages or commands, with request and response examples.>

| Method | Path | Success | Errors |
|---|---|---|---|
| `POST` | `/<resource>` | `201` + `Location` | `400`, `409` |

**Error contract:** <one shape for every error, with an example.>

## Acceptance criteria
1. **Given** <state>, **when** <action>, **then** <observable result>. → `acceptance/<Test>`
2. <…>

## Non-functional requirements
| Requirement | Taught in |
|---|---|
| <Security: …> | <lab 1.3> |
| <Resilience: …> | <lab 1.4> |

## Fixed and free
- **Fixed:** <contract, versions, …>
- **Your choice:** <internal design, persistence layout, …>

## Out of scope
- <What is deliberately missing, and why.>
