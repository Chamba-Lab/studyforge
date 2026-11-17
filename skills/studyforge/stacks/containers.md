# Containers (Docker / Podman)

Infrastructure topics are usually 🔭 `exploration` labs. The demo is finished, and the learner runs, inspects, breaks and cleans it up.

## `studyforge.toml`

```toml
[[stack]]
id = "compose"
detect = "compose.yaml"
command = "docker compose config --quiet"
timeout = 120
```

The command only validates the Compose file. The guide itself is verified by running every step in order. A demo without a Compose file has no build, and `verify.py` says so.

## Lab shape

- Name the Compose file `compose.yaml`. Give the project a fixed name (`name: lab-1-3` at the top of `compose.yaml`), and give every container and image a name that says which lab owns it.
- Pin image tags (`postgres:17.2`, not `postgres:latest`). Mention when a tool exists only in some image variants.
- End every guide with **🧹 Cleanup** commands that remove only what the lab created (`docker compose down -v`, and `docker image rm` for the images the lab built).

## Learner environments

- Show Podman equivalents when `learner.containers = "podman"`: `podman compose` and the Podman Desktop notes. Test them; do not assume.
- State resource needs (RAM, CPU) up front for heavy labs (clusters, many containers), and ask the learner to switch off what they do not need afterwards.

## Gotchas

- **Never remove containers, images or volumes you did not create,** and never filter by pattern. Other projects on the same machine are not yours.
- **Wait for readiness** (a health check, a port, a log line) before the first request. A silent first call is a startup race.
- **On Windows, PowerShell 5.1 adds a byte-order mark to text piped to a program.** Copy files into the container (`docker cp`) and redirect them instead of piping.
