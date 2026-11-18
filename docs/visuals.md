# 🎨 Visual gallery

Every visual format that StudyForge recommends ([references/visuals.md](../skills/studyforge/references/visuals.md)), rendered, with its source in the collapsible block below it. This page is also the **rendering test**: a format that does not render here on GitHub is removed from the recommendations.

## Mermaid

### `flowchart`: a flow or a decision
The request goes through validation before it reaches the database. Look for the early exit at 400.

```mermaid
flowchart LR
    A[Request] --> B{Valid?}
    B -- No --> C[400 + error contract]
    B -- Yes --> D[(Database)]
    D --> E[201 + Location]
```

<details><summary>Source</summary>

````text
```mermaid
flowchart LR
    A[Request] --> B{Valid?}
    B -- No --> C[400 + error contract]
    B -- Yes --> D[(Database)]
    D --> E[201 + Location]
```
````
</details>

### `sequenceDiagram`: interaction over time
The client gives up after the timeout, but the service keeps working: this is why retries need idempotency.

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Service
    participant P as Provider
    C->>S: POST /payments (key=abc)
    S->>P: charge
    Note over C,S: client timeout (2 s)
    P-->>S: charged
    C->>S: retry POST /payments (key=abc)
    S-->>C: 200 (Same payment, charged once)
```

### `stateDiagram-v2`: a lifecycle
The three statuses of a lab. Only learner feedback moves a lab to `done`.

```mermaid
stateDiagram-v2
    [*] --> pending
    pending --> built: build + verify
    built --> done: learner solved it, feedback applied
    done --> built: a rule changed, lab rebuilt
```

### `erDiagram`: a data model

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_LINE : contains
    PRODUCT ||--o{ ORDER_LINE : "appears in"
```

### `classDiagram`: types and their relations

```mermaid
classDiagram
    class PaymentGateway {
        <<interface>>
        +charge(amount, key) Receipt
    }
    PaymentGateway <|.. FakeProvider
    PaymentGateway <|.. RealProvider
```

### `gitGraph`: branches in a study repository
Learners keep their work in their own branch and merge `main` when labs change.

```mermaid
gitGraph
    commit id: "lab 1.1"
    branch solutions/ana
    commit id: "ana solves 1.1"
    checkout main
    commit id: "lab 1.2"
    checkout solutions/ana
    merge main
    commit id: "ana solves 1.2"
```

### `timeline`: how a technology evolved

```mermaid
timeline
    title Asynchronous Java
    2004 : Future
    2014 : CompletableFuture
    2017 : Reactive Streams (Flow API)
    2023 : Virtual threads (Java 21)
```

### `mindmap`: the map of a block

```mermaid
mindmap
  root((Block 1: Fundamentals))
    Dev mode
      Live reload
      Dev UI
    Configuration
      Profiles
      Precedence
    CDI
      Scopes
      Interceptors
```

### `xychart-beta`: measured numbers
Always next to the table with the same numbers (charts are not accessible on their own).

```mermaid
xychart-beta
    title "Latency p99 (ms) by pool size"
    x-axis [1, 2, 4, 8, 16]
    y-axis "ms" 0 --> 800
    bar [740, 410, 230, 180, 175]
```

| Pool size | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| p99 (ms) | 740 | 410 | 230 | 180 | 175 |

## Markdown

### `diff`: what changes between two states

```diff
 quarkus.http.port=8080
-quarkus.log.level=DEBUG
+quarkus.log.level=INFO
+%dev.quarkus.log.level=DEBUG
```

### Alerts

> [!NOTE]
> Context the learner should know.

> [!TIP]
> A shortcut.

> [!IMPORTANT]
> Something that must not be missed.

> [!WARNING]
> The trap of the task, without spoiling it.

### Collapsible answers

<details><summary>💡 Answer</summary>

Hidden until the learner opens it, which is right for hints, verified answers and self-assessment.
</details>

### Math

Write braces as `\lbrace` / `\rbrace`: Markdown eats the backslash of `\{`. Inline: the throughput is $\lambda = \frac{N}{T}$. As a block:

$$
\text{p99} = \min \lbrace x : P(X \le x) \ge 0.99 \rbrace
$$

### Keyboard keys and footnotes

Stop the dev mode with <kbd>Ctrl</kbd>+<kbd>C</kbd>.[^1]

[^1]: Footnotes keep references out of the main text.

### Terminal output

```text
[INFO] Tests run: 12, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

## Images

Excalidraw (`.excalidraw.svg`) and diagrams.net (`.drawio.svg`) files render on GitHub as images and stay editable in their editors. They need a solid background so they stay visible in dark mode. For a real image with a solid background, alt text and a `<title>`/`<desc>` for screen readers, see the test pyramid in the showcase: [pytest-lab, lab 1.1](https://github.com/Chamba-Lab/pytest-lab/blob/master/labs/01-unit-tests/01-what-is-a-test/CONCEPT.md#la-pirámide-de-pruebas).
