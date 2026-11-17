# Java with Maven

## `studyforge.toml`

```toml
[[stack]]
id = "maven"
detect = "pom.xml"
command = "mvn -q -B clean verify"
reports = "**/target/*-reports/TEST-*.xml"   # surefire and failsafe, every module
timeout = 900
```

- `clean` matters. Copied files keep their old modification time, and an incremental compile can run against stale classes.
- If the labs ship the Maven wrapper, you may use it instead: `./mvnw -q -B clean verify`, with `command_windows = "mvnw.cmd -q -B clean verify"`. The system `mvn` avoids wrapper problems with `JAVA_HOME` in some shells.
- Integration tests (`*IT.java`) run with Failsafe during `verify`. They do not run when the module's unit tests fail, so a red starter may report fewer tests than its solution.

## Scaffolding

- Copy `pom.xml`, `mvnw`, `mvnw.cmd`, `.mvn/` and `.gitignore` from the latest lab's variant, then change the `artifactId` to something unique per lab and variant (`<repo>-1-2-starter`). No network is needed.
- **Strategy `shared-parent`:** each lab declares `<parent>` and no versions. **Strategy `independent`:** each variant imports the platform BOM and keeps the same version as every other lab.
- Remove whatever the generator added that does not serve the topic: Dockerfiles, sample READMEs, extra dependencies.

## Making a starter

- Replace the code under study with a `TODO` method body or a placeholder field, so the starter compiles **and the application starts**.
- If the application cannot even start (for example, a dependency injection error at build time), JUnit fails while loading the test class, the module reports zero tests, and `verify.py` flags it. Design the starter so the app boots and the tests fail.

## Ignore rules

```gitignore
target/
*.class
.idea/
*.iml
.vscode/
.env
```

## Gotchas

- **The wrapper's executable bit.** Files committed from Windows may lose mode `100755`. Run `git update-index --chmod=+x <lab>/<variant>/mvnw`. `verify.py` checks this.
- **Read real signatures from the jar,** not from memory. Run `mvn dependency:build-classpath` to find the jar, then `javap -cp <jar> <fully.qualified.Class>`. Use `javap -v` to see annotation defaults. Many frameworks ship their configuration model inside the jar, for example `META-INF/quarkus-config-doc/quarkus-config-model.json`.
- **System properties for the test JVM** go in Surefire's `systemPropertyVariables`, not in `-DargLine`.
- **Plugin configuration in a shared parent** (for example `<argLine>@{argLine}</argLine>`) can break modules that do not need it. A parent manages versions, and modules keep their own plugin configuration.
- **PowerShell** needs `-D` arguments in quotes: `mvn "-Dtest=ConfigTest" test`.
