# 详细参考 - solo-build

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (text)

```text
Track complete: {title} ({trackId})

  Phases: {N}/{N}
  Tasks:  {M}/{M}
  Tests:  All passing

  Phase checkpoints:
    Phase 1: abc1234
    Phase 2: def5678
    Phase 3: ghi9012

  Revert entire track: git revert abc1234..HEAD

Next:
  /build {next-track-id}  — continue with next track
  /plan "next feature"    — plan something new
```


## Pre-flight Checks
1. **Detect context** — find where plan files live:

   * Check `docs/plan/*/plan.md` — standard location
   * Use whichever exists.
   * **DO NOT** search for `conductor/` or any other directory — only `docs/plan/`.
2. Load workflow config from `docs/workflow.md` (if exists):

   * TDD strictness (strict / moderate / none)
   * Commit strategy (conventional commits format)
   * Verification checkpoint rules
   * **Integration Testing section** — if present, run the specified CLI commands after completing tasks that touch the listed paths
     If `docs/workflow.md` missing: use defaults (moderate TDD, conventional commits).
3. **Verify git hooks are installed:**

   Read the stack YAML (`templates/stacks/{stack}.yaml`) — the `pre_commit` field tells you which system and what it runs:

   * `husky + lint-staged` → JS/TS stacks (eslint + prettier + tsc)
   * `pre-commit` → Python stacks (ruff + ruff-format + ty)
   * `lefthook` → mobile stacks (swiftlint/detekt + formatter)

   Then verify the hook system is active:

   bash

   ```
   [ -f .husky/pre-commit ] && git config core.hooksPath | grep -q husky && echo "OK" || echo "NOT ACTIVE"
   [ -f .pre-commit-config.yaml ] && [ -f .git/hooks/pre-commit ] && echo "OK" || echo "NOT ACTIVE"
   [ -f lefthook.yml ] && lefthook version >/dev/null 2>&1 && echo "OK" || echo "NOT ACTIVE"
   ```

   **If not active — install before first commit:**

   * husky: `pnpm prepare` (or `npm run prepare`)
   * pre-commit: `uv run pre-commit install`
   * lefthook: `lefthook install`

   Don't use `--no-verify` on commits — if hooks fail, fix the issue and commit again.



---

### Python-Specific Quality Tools
When the project uses a Python stack (detected by `pyproject.toml` or stack YAML), run the full Astral toolchain:

1. **Ruff** — linting + formatting (always):

   bash

   ```
   uv run ruff check --fix .
   uv run ruff format .
   ```
2. **ty** — type-checking (if `ty` in dev dependencies or stack YAML):

   bash

   ```
   uv run ty check .
   ```

   ty is Astral's type-checker (extremely fast, replaces mypy/pyright). Fix type errors before committing.
3. **Hypothesis** — property-based testing (if `hypothesis` in dependencies):

   * Use `@given(st.from_type(MyModel))` to auto-generate Pydantic model inputs.
   * Use `@given(st.text(), st.integers())` for edge-case coverage on parsers/validators.
   * Hypothesis tests go in the same test files alongside regular pytest tests.
4. **Pre-commit** — run all hooks before committing:

   bash

   ```
   uv run pre-commit run --all-files
   ```

Run these checks after each task implementation, before `git commit`. If any fail, fix before proceeding.



---

### JS/TS-Specific Quality Tools
When the project uses a JS/TS stack (detected by `package.json` or stack YAML):

1. **ESLint** — linting (always):

   bash

   ```
   pnpm lint --fix
   ```
2. **Prettier** — formatting (always):

   bash

   ```
   pnpm format
   ```
3. **tsc --noEmit** — type-checking (strict mode):

   bash

   ```
   pnpm tsc --noEmit
   ```

   Fix type errors before committing. Strict mode should be on in tsconfig.json.
4. **Knip** — dead code detection (if in devDependencies, run periodically):

   bash

   ```
   pnpm knip
   ```

   Finds unused files, exports, and dependencies. Run after significant refactors.
5. **Pre-commit** — husky + lint-staged runs ESLint + Prettier + tsc on staged files.



---

### 5.6. Visual Verification (if browser/simulator/emulator available)
After implementation, run a quick visual smoke test if tools are available:

**Web projects (Playwright MCP or browser tools):**
If you have Playwright MCP tools or browser tools available:

1. Start the dev server if not already running (check stack YAML for `dev_server.command`)
2. Navigate to the page affected by the current task
3. Check the browser console for errors (hydration mismatches, uncaught exceptions, 404s)
4. Take a screenshot to verify the visual output matches expectations
5. If the task affects responsive layout, resize to mobile viewport (375px) and check

**iOS projects (simulator):**
If instructed to use iOS Simulator in the pipeline prompt:

1. Build for simulator: `xcodebuild -scheme {Name} -sdk iphonesimulator build`
2. Install on booted simulator: `xcrun simctl install booted {app-path}`
3. Launch and take screenshot: `xcrun simctl io booted screenshot /tmp/sim-screenshot.png`
4. Check simulator logs: `xcrun simctl spawn booted log stream --style compact --timeout 10`

**Android projects (emulator):**
If instructed to use Android Emulator in the pipeline prompt:

1. Build debug APK: `./gradlew assembleDebug`
2. Install: `adb install -r app/build/outputs/apk/debug/app-debug.apk`
3. Take screenshot: `adb exec-out screencap -p > /tmp/emu-screenshot.png`
4. Check logcat: `adb logcat '*:E' --format=time -d 2>&1 | tail -20`

**Graceful degradation:** If browser/simulator/emulator tools are not available or fail — skip visual checks entirely. Visual testing is a bonus, never a blocker. Log that it was skipped and continue with the task.



---

### 6. Complete Task
**Commit** (following commit strategy):

```bash
git add {specific files changed}
git commit -m "<type>(<scope>): <description>"
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `perf`, `style`

**Capture SHA** after commit:

```bash
git rev-parse --short HEAD
```

**SHA annotation in plan.md.** After every task commit:

1. Mark task done: `[~]` → `[x]`
2. Append commit SHA inline: `- [x] Task X.Y: description <!-- sha:abc1234 -->`

Without a SHA, there's no traceability and no revert capability. If a task required multiple commits, record the last one.



---

### 7. Phase Completion Check
After each task, check if all tasks in current phase are `[x]`.

If phase complete:

1. **SHA audit** — scan all `[x]` tasks in this phase. If any are missing `<!-- sha:... -->`, capture their SHA now from git log and add it. Every `[x]` task MUST have a SHA.
2. Run verification steps listed under `### Verification` for the phase.
3. Run full test suite.
4. Run linter.
5. Mark verification checkboxes in plan.md: `- [ ]` → `- [x]`.
6. Commit plan.md progress: `git commit -m "chore(plan): complete phase {N}"`.
7. Capture checkpoint SHA and append to phase heading in plan.md:
   `## Phase N: Title <!-- checkpoint:abc1234 -->`.
8. Report results and continue:

```text
Phase {N} complete! <!-- checkpoint:abc1234 -->

  Tasks:  {M}/{M}
  Tests:  {pass/fail}
  Linter: {pass/fail}
  Verification:
    - [x] {check 1}
    - [x] {check 2}

  Revert this phase: git revert abc1234..HEAD
```

Proceed to the next phase automatically. No approval needed.



---

## Reverting Work
SHA comments in plan.md enable surgical reverts:

**Revert a single task:**

```bash
git revert abc1234
```

Then update plan.md: `[x]` → `[ ]` for that task.

**Revert an entire phase:**

```bash
git revert abc1234..def5678
```

Then update plan.md: all tasks in that phase `[x]` → `[ ]`.

**Never use `git reset --hard`** — always `git revert` to preserve history.



---
