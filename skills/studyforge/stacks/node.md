# Node.js (npm)

> [!NOTE]
> Starting values, not yet proven by a StudyForge pilot. Confirm them with the test runner version the repository pins.

## `studyforge.toml`

```toml
[[stack]]
id = "node"
detect = "package.json"
command = "npm ci --no-audit --no-fund && npm test"
reports = "reports/junit.xml"
timeout = 600
```

The `npm test` script writes a JUnit XML report so that `verify.py` can count the tests. With Vitest:

```json
{ "scripts": { "test": "vitest run --reporter=default --reporter=junit --outputFile.junit=reports/junit.xml" } }
```

With the built-in Node test runner:

```json
{ "scripts": { "test": "node --test --test-reporter=spec --test-reporter-destination=stdout --test-reporter=junit --test-reporter-destination=reports/junit.xml" } }
```

## Scaffolding

- Each variant is a complete package with its own `package.json` and a committed `package-lock.json`, so `npm ci` installs exactly the pinned versions.
- **Strategy `shared-parent`:** a root `package.json` with `workspaces` holds the shared dev dependencies. Weigh the cost first: a learner cannot copy one lab out on its own.

## Making a starter

Export the function or module under study with a body that throws `new Error("TODO")`, or that returns a placeholder. Every other module still loads, so the test file imports cleanly and its assertions fail.

## Ignore rules

```gitignore
node_modules/
reports/
coverage/
dist/
.env
```

## Gotchas

- **Use `npm ci`, not `npm install`,** for verification. `npm install` may rewrite the lockfile.
- **Pin the Node version** in `SETUP.md` and `package.json` (`engines`). The minimum is what the dependencies require, not what someone happens to have installed.
