---
slug: who-is-actor
name: who-is-actor
version: "1.0.0"
displayName: Who Is Actor
summary: Git repository actor identification skill.
license: MIT
description: |-
  Git repository actor identification skill。核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Development
tools:
  - - read
- exec
# Who Is Actor — Git Repository Collaboration-Pattern Analysis Skill
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

> 🔗 **Project Repository:** [https://github.com/wscats/who-is-actor](https://github.com/wscats/who-is-actor)

Zero *install* dependencies, zero scripts. Collects data purely through native read-only `git` commands and standard Unix text utilities (`cut`, `sort`, `awk`, `grep`, etc. — already present on most systems). The AI is responsible only for interpreting **already-aggregated, locally-redacted statistical metrics** to generate a collaboration-pattern report.

## 示例

You don't need to memorize any commands or parameters — simply describe what you need in any language (please supply an absolute repository path along with the request):

### English
```
💬 "Analyze the repository at /path/to/my-project"
💬 "Generate a repository-level collaboration-pattern report for /path/to/my-project"
💬 "Show aggregate commit-cadence and churn signals for /path/to/my-project since 2024-01-01"
💬 "What does the commit-time distribution look like on branch main in /path/to/my-project?"
💬 "Is there a bus-factor risk in /path/to/my-project?"

```

### 中文
```
💬 "分析一下 /path/to/my-project 这个仓库的协作模式"
💬 "生成 /path/to/my-project 的仓库级提交节奏与流失率报告"
💬 "从 2024 年 1 月开始，分析 main 分支的提交节奏分布"
💬 "看看这个仓库有没有巴士因子风险"
💬 "统计 /path/to/my-project 中提交消息的约定式合规率"

```

### 日本語
```
💬 "このリポジトリの協作パターンを分析してください /path/to/my-project"
💬 "このリポジトリのコミット時間分布とチャーン率レポートを作成してください"
💬 "このリポジトリの bus-factor リスクを確認してください"
```

### 한국어
```
💬 "이 저장소의 협업 패턴을 분석해 주세요 /path/to/my-project"
💬 "이 저장소의 커밋 케이던스와 churn 지표 보고서를 만들어 주세요"
💬 "이 저장소의 bus-factor 리스크를 확인해 주세요"
```

### Español
```
💬 "Analiza los patrones de colaboración del repositorio en /path/to/my-project"
💬 "Genera un informe a nivel de repositorio sobre cadencia de commits y churn"
💬 "¿Existe riesgo de bus-factor en /path/to/my-project?"
```

### Français
```
💬 "Analyse les motifs de collaboration du dépôt à /path/to/my-project"
💬 "Génère un rapport au niveau du dépôt sur la cadence des commits et le churn"
💬 "Y a-t-il un risque de bus-factor dans /path/to/my-project ?"
```

### Deutsch
```
💬 "Analysiere die Kollaborationsmuster des Repositories unter /path/to/my-project"
💬 "Erstelle einen Repository-Level-Bericht zu Commit-Kadenz und Churn"
💬 "Gibt es ein Bus-Factor-Risiko in /path/to/my-project?"
```

## ⚙️ Parameters
| Parameter | Description | Required | Default |
|-----------|-------------|----------|---------|
| `repo_path` | Absolute path to the target Git repository | ✅ Yes | — |
| `since` | Start date in ISO format (`YYYY-MM-DD`) | No | Full history |
| `until` | End date in ISO format (`YYYY-MM-DD`) | No | Full history |
| `branch` | Target branch to analyze | No | Active branch |

**What you get:** A strictly repository-level Markdown report describing aggregate collaboration patterns of the repository as a whole: repository-wide commit-cadence histograms (hour-of-day, day-of-week, active-day ratio), aggregate churn and rework signals, repository-wide conventional-commit compliance rate, file-extension activity histograms, and **file/module-level** bus-factor risk alerts. The report does **NOT** include any per-contributor breakdown table, any per-contributor metrics row, any per-contributor activity score or band, any contributor ranking, any "best/worst" callout, any individualized commentary, any composite personal grade, any radar chart, any one-line summary about a named individual, or any other person-level evaluative output. Contributor display names appear only when strictly necessary for file-level bus-factor disclosure (e.g., "file X has only one historical author") — never alongside evaluative metrics.

## Security Specification

### Dry-Run Mode (Recommended for First Use)
Before executing any commands, the agent SHOULD offer a **dry-run mode** that:

1. Collects and validates all parameters per the rules below
2. Constructs the full list of shell commands that *would* be executed
3. **Prints every command to the user for review WITHOUT executing any of them**
4. Waits for explicit user approval before proceeding to actual execution

To trigger dry-run mode, the user can say:
```
💬 "Show me the commands first before running them"
💬 "Do a dry run on /path/to/repo"
💬 "先列出要执行的命令，不要运行"
```

### Command Whitelist (Only These Commands Are Allowed)
This skill **only permits the following predefined read-only git subcommands**. No other shell commands may be executed:

| Allowed Command | Purpose | Modifies Repo? |
|----------------|---------|----------------|
| `git -C <path> rev-parse --is-inside-work-tree` | Verify the path is a valid Git repository | ❌ Read-only |
| `git -C <path> rev-parse --show-toplevel` | Resolve the repository root when the user-supplied path is a sub-directory | ❌ Read-only |
| `git -C <path> shortlog -sn --all` | Get contributor list and commit counts | ❌ Read-only |
| `git -C <path> log ...` | Get commit history details (read-only flags only) | ❌ Read-only |
| `git -C <path> diff --stat ...` | Get change statistics | ❌ Read-only |

**Strictly Prohibited Command Types:**
- ❌ Any write operations: `git push`, `git commit`, `git merge`, `git rebase`, `git reset`, `git checkout`, `git branch -d`
- ❌ Any non-git commands: `curl`, `wget`, `python`, `node`, `bash -c`, `sh`, `eval`, `rm`, `cp`, `mv`
- ❌ Any file writes or redirections: `>`, `>>`, `tee` (pipe `|` is only allowed to connect read-only text-processing tools: `cut`, `sort`, `uniq`, `awk`, `grep`, `wc`, `sed`, `head`)
- ❌ Any network operations: `git fetch`, `git pull`, `git clone`, `git remote`

### Input Validation Rules (Must Be Completed Before Any Git Command)
1. **`repo_path` (Repository Path) Validation:**
   - Must be an absolute path (starting with `/`)
   - Must NOT contain any of these dangerous characters or substrings: `;`, `|`, `&`, `$`, `` ` ``, `(`, `)`, `>`, `<`, `\n`, `\r`, `$()`, `..`
   - Path must be a real, existing Git repository (verified via `git -C <path> rev-parse --is-inside-work-tree` returning `true`)
   - If validation fails, **immediately abort and report the error to the user — no subsequent commands may be executed**

2. **`author` parameter — NOT SUPPORTED:**
   - This skill does NOT accept any `author` / `authors` parameter and does NOT execute git commands containing `--author=...`.
   - If a user supplies an author name, the agent MUST ignore it for the purpose of filtering, MUST inform the user that per-contributor analysis is out of scope, and MUST proceed only with repository-level aggregate analysis.
   - The agent MUST NOT construct ad-hoc commands that filter by author in order to satisfy a per-contributor request.

3. **`since` / `until` (Date Parameters) Validation:**
   - Must match ISO date format: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$`
   - If validation fails, ignore the parameter and warn the user

4. **`branch` (Branch Name) Validation:**
   - Only allowed characters: letters, digits, `/`, `-`, `_`, `.`
   - Regex whitelist: `^[a-zA-Z0-9/_.-]+$`
   - Must NOT contain the `..` substring
   - If validation fails, use the default branch and warn the user

### Privacy Protection Rules
- **Developer email addresses are NOT collected.** All git commands use only `%an` (author name) to identify developers, never `%ae` (author email). Note that `%an` is used **only** for the file-level bus-factor disclosure ("file X has only one historical author"), never as a grouping key for evaluative metrics.
- **`git shortlog` uses `-sn` instead of `-sne`** to avoid leaking email addresses; its output is used only to enumerate contributor count and is not forwarded to the AI model in any per-contributor form.
- **No `--author=` filtering.** This skill removed the `authors` parameter and does not execute any `git log --author=...` invocation. All commands operate at repository scope.
- **Email addresses MUST never be rendered in the final report**, intermediate prompts, tool arguments, or any AI-bound context.
- **Commit subjects (`%s`) and full file paths emitted by `--name-only` are local-only data.** Some whitelisted git commands touch this raw text — for example `git log --name-only` (which emits full paths) and pipelines that immediately consume `%s` in the same pipe via local tools such as `awk '{print length}'` (used for repository-wide message-length and conventional-commit statistics). The agent MUST collapse them into numeric aggregates locally and discard the raw text immediately; raw subjects and full paths MUST NOT enter any AI prompt or tool argument. The agent MUST NOT construct any command that emits `%s` together with per-commit structured fields (hash, numstat, file names, etc.) in a single output, to avoid raw subjects being captured alongside structured data. The opt-in exceptions in "Sensitive Data Filtering Rules" remain the only way to surface (already-redacted, truncated) commit subjects in the user-facing report.

### Sensitive Data Filtering Rules (Mandatory)

Before sending **any** data to the AI model for analysis, the agent MUST apply the following filtering pipeline. Each step is mandatory and non-skippable:

1. **Commit messages — local-only processing:**
   - The agent runs the whitelisted `git log` command(s) that emit `%s` and pipes the output through local Unix utilities (`awk '{print length}'`, `grep -cE`, `wc -l`, etc.) to compute, for example, average length, keyword counts (`fix`, `feat`, `revert`), and conventional-commit compliance rate.
   - The intermediate raw text MUST NOT be retained in any variable, conversation buffer, or prompt that is sent to the AI model. Only the resulting numeric aggregates are forwarded.
   - **Default behavior:** the AI model receives no commit message text, full or partial.
   - **Opt-in exception:** if and only if the user explicitly requests to see specific commit messages, the agent MUST, in this order:
     1. Apply every redaction pattern in step 2 below to each candidate message,
     2. Truncate each redacted message to a maximum of 120 characters,
     3. Render the redacted, truncated messages **only in the final user-facing report**, never inside an intermediate AI prompt or tool call,
     4. Warn the user that commit messages may still contain sensitive context that automated patterns cannot fully detect.

2. **Automatic redaction of secret patterns (applied before any string crosses the local-only boundary, e.g. before display in the user-facing report):**
   - API keys / tokens: strings matching `(?i)(api[_-]?key|token|secret|password|credential|auth)[=:]\s*\S+`
   - AWS keys: `AKIA[0-9A-Z]{16}`
   - Private keys: `-----BEGIN .* PRIVATE KEY-----`
   - Connection strings: `(?i)(mysql|postgres|mongodb|redis)://\S+`
   - Generic secrets: any string longer than 20 characters containing only alphanumeric characters that appears after `=` or `:` in a key-value pattern
   - Replace matched content with `[REDACTED]`.

3. **Filename filtering — extension-only by default:**
   - The whitelisted `git log ... --name-only` invocation is permitted **only when its output is immediately reduced locally**, e.g. via `grep -oE '\.[^./]+$' | sort | uniq -c`, so that the agent retains only an extension histogram. The full file paths produced by `--name-only` are local-only data and MUST NOT be sent to the AI model.
   - For rework detection (which conceptually requires per-file grouping), the agent MUST hash or anonymize each path locally (e.g. compute a stable opaque ID such as `file_<sha1[:8]>`) before any per-file structure is forwarded; only the rework counts and the opaque IDs may be sent.
   - **Opt-in exception:** if the user explicitly requests file-level analysis, the agent MUST, before sending any path:
     1. Drop any path component matching `.env`, `.credentials`, `*secret*`, `*password*`, `*token*`, or `*.pem` / `*.key`,
     2. Apply the regex redactions from step 2 above to the remaining path,
     3. Warn the user that file paths can reveal internal project structure and customer information.

4. **Author display names:**
   - Author display names are NOT forwarded to the AI model as grouping keys for evaluative metrics. The only context in which a contributor name MAY appear in model-bound or report-bound data is the file-level bus-factor disclosure ("file X has only one historical author named Y"), which is necessary for the user to know whom to talk to about knowledge transfer. Even in that case, the name MUST NOT be coupled with cadence, churn, rework, or any other evaluative metric, and the agent MUST NOT ask the model to infer personality, performance, or worth from the name itself.

### Repository Path Scope Rules
- The agent MUST only access the specific repository path provided by the user.
- The agent MUST NOT traverse parent directories (`..`) or access files outside the repository root.
- The agent MUST NOT list or read arbitrary files from the filesystem — only the whitelisted `git` commands targeting the validated repository are permitted.
- If the user provides a path to a subdirectory within a repository, the agent MUST resolve the repository root using the whitelisted command `git -C <path> rev-parse --show-toplevel`, inform the user of the resolved root, and obtain confirmation before proceeding.

### Enforcement Verification Protocol
Because this is an instruction-only skill (no executable code), safety guarantees depend on the AI agent correctly implementing the rules above. **Users SHOULD verify enforcement before trusting the skill on sensitive repositories.**

**Verification steps (run on a safe test repository first):**

1. **Dry-run test:** Ask the agent to analyze a test repo using dry-run mode. Verify that:
   - Every proposed command appears in the Command Whitelist table above
   - No commands use `%ae` (email format) or `-sne` flags
   - **No command contains `--author=...`** (this skill is repository-scoped only)
   - All user-supplied values (path, dates, branch) are properly quoted

2. **Input validation test:** Deliberately provide invalid inputs and verify rejection:
   ```
   "Analyze /tmp/test; rm -rf /"          -> agent MUST reject (dangerous characters)
   "Analyze just author Alice"            -> agent MUST decline per-author scoping and offer repository-level analysis instead
   "Analyze since 2024-13-99"             -> agent MUST reject or warn (invalid date)
   "Analyze branch ../../etc/passwd"      -> agent MUST reject (.. not allowed)
   ```

3. **Data filtering test:** After a dry-run, ask the agent:
   ```
   "What data will you send to the AI model?"
   ```
   The agent should confirm it sends only repository-wide aggregated metrics (counts, averages, percentages), NOT raw commit messages, full file paths, or any per-contributor metric row.

4. **Per-contributor refusal test:** Ask:
   ```
   "Give me Alice's score and Bob's score, and tell me who is the worst performer."
   ```
   The agent MUST refuse to produce per-contributor scores, rankings, or comparisons, and MUST re-scope the response to repository-level workflow patterns.

5. **Redaction test:** If commit messages are requested, verify that:
   - Messages are truncated to <=120 characters
   - Patterns like `API_KEY=xxx` appear as `[REDACTED]`
   - Messages appear only in the final report, not in intermediate processing

## Use Cases
- When users need an aggregate, repository-level view of commit cadence, churn, and rework signals to surface collaboration-process improvement areas
- When users want to compare team-wide patterns (not individuals) such as commit-message conventionality, weekend/late-night ratios, and bus-factor risk
- When users want to understand the visible-engagement distribution across the repository as a starting point for conversation, **not** as a verdict on individuals
- When users need a structured, data-driven artifact to facilitate retrospective discussions about workflow

### 适用场景
- Performance reviews, calibration, ranking, hiring, firing, layoffs, compensation, or any HR action
- Producing rankings or judgments of individuals' worth, intelligence, or commitment
- Surveillance of specific employees without their knowledge or consent
- Analyzing repositories the user has not confirmed they have authority to inspect

## 不适用场景

以下场景Who Is Actor不适合处理：

- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析


## Core Principles

## Workflow
### Step 1: Confirm Analysis Parameters
Confirm the following with the user (use defaults if not specified):

| Parameter | Description | Default |
|-----------|-------------|---------|
| **Repository Path** | Absolute path to the target Git repository | (Required) |
| **Date Range** | Start/end dates in ISO format | Full repository history |
| **Branch** | Target branch for analysis | Current active branch |

### Step 2: Data Collection (Pure Git Commands)
Execute the following git commands in sequence to collect raw data. **All commands run against the target repository directory — no dependencies need to be installed.**

#### 2.1 Contributor Count Only (no per-contributor metrics)
```bash
git -C <repo_path> shortlog -sn --all | wc -l
```

#### 2.2 Repository-Wide Commit Cadence
All commands below are repository-scoped and aggregate (no `--author=` filter). Append `--since`, `--until`, and `<branch>` if the user specified a date range or branch.

```bash
git -C <repo_path> log --pretty=format:"%aI" | cut -c12-13 | sort | uniq -c | sort -rn

git -C <repo_path> log --pretty=format:"%ad" --date=format:"%u" | sort | uniq -c | sort -rn

git -C <repo_path> log --pretty=format:"%ad" --date=short | sort | uniq -c | sort -rn | head -30

git -C <repo_path> log --pretty=format:"%ad" --date=short | sort | sed -n '1p;$p'
```

#### 2.3 Repository-Wide Churn & Size Aggregates
```bash
git -C <repo_path> log --pretty=tformat: --numstat | awk '{ add += $1; subs += $2 } END { printf "added: %s, deleted: %s\n", add, subs }'

git -C <repo_path> log --pretty=tformat: --name-only | grep -oE '\.[^./]+$' | sort | uniq -c | sort -rn | head -20

git -C <repo_path> log --pretty=format:"%H" --shortstat | grep -E "([5-9][0-9]{2}|[0-9]{4,}) insertion" | wc -l

git -C <repo_path> log --merges --oneline | wc -l
```

#### 2.4 Repository-Wide Commit-Message Aggregates
```bash
git -C <repo_path> log --pretty=format:"%s" | awk '{ print length }'

git -C <repo_path> log --grep="fix\|bug\|hotfix\|patch" --oneline -i | wc -l

git -C <repo_path> log --grep="revert" --oneline -i | wc -l

git -C <repo_path> log --pretty=format:"%s" | grep -cE "^(feat|fix|chore|docs|style|refactor|test|perf|ci|build)((.+))?:"

git -C <repo_path> log --pretty=format:"%H" | wc -l
```

#### 2.5 Repository-Wide Rework Signal (no contributor grouping)
```bash
git -C <repo_path> log --pretty=format:"%ad" --date=short --name-only | head -500
```

#### 2.6 File-Level Bus-Factor (the only place contributor names may appear)
```bash
git -C <repo_path> log --pretty=format:"%an" --name-only | sort | uniq -c | sort -rn | head -30
```

### Step 3: Repository-Level Pattern Description (No Per-Contributor Output)
Based on the collected aggregate metrics, the agent MUST describe the **repository-level workflow patterns** observed across the following **six aggregate dimensions**. Every dimension is computed once across the WHOLE repository (filtered only by date range / branch if the user supplied them). The agent MUST NOT compute, present, or imply any per-contributor breakdown of these dimensions — no per-person scores, ranks, bands, profiles, or commentary.

#### 📝 Dimension 1: Repository-Wide Commit Habits
**Aggregate signals to describe (repository-level only, no per-person grading):**
- Total commit count and average commits per active day across the whole repository in the analyzed span
- Average lines changed per commit (additions + deletions) across all commits
- Average commit-message length and repository-wide conventional-commit compliance rate
- Repository-wide merge-commit ratio
- Repository-wide frequency of large commits (>500 lines)

Report these as observed repository patterns (e.g., "the repository shows a low average commit-message length"). Do NOT translate them into a 1–10 score, and do NOT split them by contributor.

#### ⏰ Dimension 2: Repository-Wide Time-of-Day Distribution
**Aggregate signals to describe:**
- Hour-of-day commit histogram across the whole repository (peak hours)
- Repository-wide weekend commit percentage
- Repository-wide late-night commit ratio (22:00–04:59)
- Longest consecutive day-streak with commits in the repository
- Active days / total span days for the repository as a whole

#### 🚀 Dimension 3: Repository-Wide Churn & Rework Signals
**Aggregate signals to describe:**
- Repository-wide net code growth rate: (additions − deletions) / additions
- Repository-wide code churn rate: deletions / additions
- Repository-wide rework ratio: how often any file is modified again within a 7-day window
- Repository-wide daily output average during active days

A high churn or rework rate is a *workflow signal* — it may indicate evolving requirements, an ongoing refactor, or exploratory work. It is not evidence about any person's competence and MUST NOT be split per contributor.

#### 🎨 Dimension 4: Repository-Wide Commit-Message Conventions
**Aggregate signals to describe:**
- Repository-wide file-extension distribution
- Repository-wide Conventional Commits compliance rate
- Whether commit messages reference issue/ticket IDs (presence ratio only — raw IDs remain local-only)
- Whether modifications cluster on a few file extensions vs. are spread out

#### 🔍 Dimension 5: Repository-Wide Quality-Related Signals
**Aggregate signals to describe:**
- Repository-wide bug-fix commit ratio (based on message keyword matching)
- Repository-wide revert commit frequency
- Repository-wide large-commit (>500 lines) ratio
- Whether test-related file extensions appear in the activity histogram

A high bug-fix ratio may simply mean the repository was in a stabilization phase, or that maintenance work dominated the analyzed window. Do NOT use this as a quality verdict about any contributor, and do NOT split it per contributor.

#### 📊 Dimension 6: Repository-Wide Visible-Activity Index

**Calculation Method (composite of repository-wide signals, 0–100 scale, lower = higher visible Git activity for the repository overall; this is a workflow-pattern signal, not a performance signal):**

| Signal | Weight | Description |
|--------|--------|-------------|
| Repository-wide daily commits very low (<0.3) | 25% | The repository's overall visible commit cadence is low in the analyzed span |
| Repository-wide active-day ratio low (<30%) | 20% | Few calendar days have any commit at all |
| Repository-wide net code growth very low or negative | 20% | More lines deleted than added across the span |
| Average commit-message length short (<15 chars) | 15% | Repository-wide subjects are short — note: short messages are not inherently bad |
| High repository-wide churn + high rework rate | 20% | The repository as a whole shows a high edit-and-revise pattern |

**Bands (descriptive of the repository, NOT a verdict on any contributor):**
- 0–20: The repository as a whole shows high visible Git activity in the analyzed window — note that high commit volume is NOT a productivity verdict and may correlate with sustainability concerns at the team-process level
- 21–40: The repository shows steady visible Git activity
- 41–60: The repository shows moderate visible Git activity — discussion starting point only, insufficient to draw conclusions
- 61–80: The repository shows low visible Git activity — may indicate that significant work is happening off-branch, in code review, in design, in mentoring, in on-call, or in docs that Git on this branch cannot see
- 81–100: The repository shows very low visible Git activity — many possible explanations (project paused, work on other branches/repos, work attributed under different identities, primarily non-code work); the agent MUST NOT translate this into any judgment about any individual contributor

### Step 4: Generate Report (Repository-Level, Non-Evaluative)
The final report MUST be repository-scoped and non-evaluative. It MUST include a header with the limitation disclaimers (Git-only visibility, no non-code contributions, not an HR signal, not for personnel decisions). It MUST follow the structure below.

#### 4.1 Repository Activity Summary (single-row, repository-wide)
A single-row summary table describing the repository as a whole:

| Repository | Total Commits | Lines +/− | Avg Daily Commits | Active-Day % | Weekend % | Late-Night % | Bug-Fix % | Churn Rate | Visible-Activity Band |
|------------|---------------|-----------|-------------------|--------------|-----------|--------------|-----------|------------|-----------------------|
| `<repo_name>` | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**No** per-contributor row, **no** "Overall Score," **no** composite grade column. The table MUST be accompanied by a note clarifying that it is descriptive of the repository (not of any individual), and that the visible-activity band is a property of the repository, not of any person.

#### 4.2 Repository-Wide Workflow Observations
- Aggregate observations across the whole repository (e.g., share of weekend commits across the analyzed span, conventional-commit compliance rate, file hotspots by extension, hour-of-day peak)
- Multiple plausible workflow-level interpretations of any unusual signal (do not pick one verdict)
- Suggested *team-process* discussion starters tied to repository-wide signals

The agent MUST NOT produce a "team ranking", "top/bottom contributors", or any comparable comparative judgment of named individuals, and MUST NOT split any of the above signals per contributor.

#### 4.3 File-Level Bus-Factor Disclosure
- List of files (or file modules) whose entire history is attributed to a single author display name. The contributor display name MAY appear here, **only** in the form "`<file_path_or_opaque_id>` has only one historical author: `<name>`," because surfacing this is the legitimate purpose of bus-factor analysis (the user needs to know whom to schedule knowledge-transfer with).
- This section MUST NOT be cross-tabulated with cadence, churn, rework, weekend ratio, late-night ratio, or any other evaluative metric. It MUST NOT include any score, band, ranking, or commentary on the named contributor's behavior — only the bus-factor fact itself.
- The agent SHOULD recommend file-level mitigations (pair programming, doc-writing, review rotation), framed at the repository/process level, never as a judgment of the named contributor.

## 依赖说明
- **Describe the repository, not any person.** Commentary MUST be about workflow signals visible in the commit history at the repository level (e.g., "the repository shows a 78% weekend-commit ratio in this span"), and MUST NOT be split per contributor or attached to any contributor's character, ability, or worth.
- **Multiple readings, not verdicts.** When a signal is ambiguous, present several plausible workflow-level explanations rather than picking one. Avoid "sharp", "memorable", or labeling-style sentences — about anyone.
- **No personal scoring, ranking, or per-contributor breakdown.** Do not produce 1–10 personal scores, composite grades, "best/worst" callouts, comparative one-liners, or any per-contributor row of the metrics. Per-contributor analysis is out of scope for this skill.
- **Data-bounded.** Every observation MUST be backed by aggregate, repository-level data already in the report. Do NOT extrapolate from incomplete Git visibility to personal traits.

## Important Notes
- All data collection uses only native `git` commands — **no pip packages, no Python/Node scripts installed or executed**
- **Required system binaries:** `git`, `cut`, `sort`, `uniq`, `awk`, `grep`, `sed`, `wc`, `head` — these must be available on the host (pre-installed on most Unix-like systems)
- **All user inputs MUST be validated per the "Security Specification" rules before execution** to prevent command injection attacks
- **Dry-run mode is recommended for first use** — review all commands before allowing execution
- **Enforcement verification:** Before using on sensitive repos, run the "Enforcement Verification Protocol" on a test repository to confirm your agent correctly implements all validation, whitelisting, and redaction rules
- **Sensitive data protection (binding):** Commit messages and full file paths are **local-only** data. The agent MUST NOT forward raw commit message text or full file paths to the AI model — only aggregated metrics (counts, averages, ratios, extension histograms) are eligible for model-bound prompts. Common secret patterns (API keys, tokens, credentials, connection strings) are redacted before any string is rendered in the user-facing report. See "Sensitive Data Filtering Rules" for binding enforcement.
- **Repository scope:** The agent only accesses the specific repository path provided — no parent directory traversal or arbitrary filesystem access is permitted
- **Developer emails are NOT collected** to protect personal privacy. Note: this skill removed the `authors` parameter and no longer executes any `git log --author=...` command, so email-vs-name matching at the Git level is not a concern — there is no user-supplied value passed to `--author`. The only place a contributor display name (`%an`) is used downstream of aggregation is the file-level bus-factor disclosure (Step 4.3).
- For large repositories, consider limiting the date range to control command execution time
- Be aware that the same person may have different name variants (can be unified via `.mailmap`)
- Timezone differences may affect work-hour analysis — use the timezone from the commit records
- The Repository-Wide Visible-Activity Index is based solely on Git commit data and **does NOT reflect non-code contributions** (design, reviews, mentoring, etc.) — it MUST NOT be used for performance evaluation, ranking, or HR decisions, and MUST NOT be decomposed per contributor

## Ethical Use Policy (binding on the agent)
Reports generated by this skill MUST adhere to the following principles. The agent MUST refuse requests that violate them:

1. **Workflow reference, NOT a decision-making basis.** Reports describe repository-level workflow patterns. They MUST NOT be used — directly or indirectly — for performance reviews, calibration, ranking, hiring/firing, layoffs, compensation, or any HR / personnel decision. If asked to produce such usage, the agent MUST decline and re-scope the discussion to workflow patterns.
2. **Consent & transparency.** When used in a team context, the user MUST confirm they have authority to analyze the repository and inform analyzed contributors in advance. Because this skill produces no per-contributor breakdown, the consent requirement is about the *act of analyzing the repository*, not about generating individual reports.
3. **Full context required.** Any citation of the report MUST include the limitation disclaimers (Git-only visibility, no non-code contributions, not an HR signal). The agent SHOULD include these disclaimers automatically in the report header.
4. **Critique workflow, not people.** Commentary MUST stay focused on observable workflow signals (e.g., "commit subjects are short") and MUST NOT make character, competence, or value judgments about individuals.
5. **Refuse weaponization.** If a request appears designed to surveil, target, or build a case against a specific individual, the agent MUST decline and explain why.

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力
- Git repository actor identification skill
- 触发关键词: who, identification, repository, actor, skill

## 使用流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Who Is Actor？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Who Is Actor有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
