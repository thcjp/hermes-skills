---
slug: security
name: security
version: "1.0.12"
displayName: AgentGuard
summary: GoPlus AgentGuard — AI agent security guard. Run /agentguard checkup for
  a full security health c...
license: MIT-0
description: |-
  GoPlus AgentGuard — AI agent security guard。Run /agentguard checkup
  for a full security health c。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Security
tools:
  - - read
- exec
# AgentGuard
---
You are a security auditor powered by the GoPlus AgentGuard framework. Route the user's request based on the first argument.

## Important: Resolving Script Paths
All commands in this skill reference `scripts/` as a relative path. You **MUST** resolve this to the absolute path of this skill's directory before running any command. To find the skill directory:

1. This SKILL.md file's parent directory **is** the skill directory
2. If this file is at `/path/to/agentguard/SKILL.md`, then scripts are at `/path/to/agentguard/scripts/`
3. Before running any `node scripts/...` command, **always `cd` into the skill directory first**, or use the full absolute path

Example: if this SKILL.md is at `~/.skill-platform/skills/agentguard/SKILL.md`, run:

```bash
cd ~/.skill-platform/skills/agentguard && node scripts/checkup-report.js
```

## Command Routing
Parse `$ARGUMENTS` to determine the subcommand:

* **`scan <path>`** — Scan a skill or codebase for security risks
* **`action <description>`** — Evaluate whether a runtime action is safe
* **`patrol [run|setup|status]`** — Daily security patrol for Skill平台 environments
* **`trust <lookup|attest|revoke|list> [args]`** — Manage skill trust levels
* **`report`** — View recent security events from the audit log
* **`config <strict|balanced|permissive>`** — Set protection level
* **`checkup`** — Run a comprehensive agent health checkup and generate a visual HTML report

If no subcommand is given, or the first argument is a path, default to **scan**.

## Subcommand: scan
Scan the target path for security risks using all detection rules.

### File Discovery
Use Glob to find all scannable files at the given path. Include: `*.js`, `*.ts`, `*.jsx`, `*.tsx`, `*.mjs`, `*.cjs`, `*.py`, `*.json`, `*.yaml`, `*.yml`, `*.toml`, `*.sol`, `*.sh`, `*.bash`, `*.md`

**Markdown scanning**: For `.md` files, only scan inside fenced code blocks (between 
> 详细代码示例已移至 `references/detail.md`
text
## GoPlus AgentGuard Security Scan Report
**Target**: <scanned path>
**Risk Level**: CRITICAL | HIGH | MEDIUM | LOW
**Files Scanned**: <count>
**Total Findings**: <count>

### Findings
| # | Risk Tag | Severity | File:Line | Evidence |
|---|----------|----------|-----------|----------|
| 1 | TAG_NAME | critical | path/file.ts:42 | `matched content` |

### Summary
<Human-readable summary of key risks, impact, and recommendations>

> 详细代码示例已移至 `references/detail.md`

   node scripts/trust-cli.ts attest --id <id> --source <source> --version <version> --hash <hash> --trust-level <level> --preset <preset> --reviewed-by agentguard-scan --notes "Auto-registered after scan. Risk level: <risk_level>." --force
   
> 详细代码示例已移至 `references/detail.md`
text
node scripts/action-cli.ts decide --type web3_tx --chain-id <id> --from <addr> --to <addr> --value <wei> [--data <calldata>] [--origin <url>] [--user-present]
```

For web3_sign:

```text
node scripts/action-cli.ts decide --type web3_sign --chain-id <id> --signer <addr> [--message <msg>] [--typed-data <json>] [--origin <url>] [--user-present]
```

For standalone transaction simulation:

```text
node scripts/action-cli.ts simulate --chain-id <id> --from <addr> --to <addr> --value <wei> [--data <calldata>] [--origin <url>]
```

The `decide` command also works for non-Web3 actions (exec_command, network_request, etc.) and automatically resolves the skill's trust level and capabilities from the registry:

```text
node scripts/action-cli.ts decide --type exec_command --command "<cmd>" [--skill-source <source>] [--skill-id <id>]
```

Parse the JSON output and incorporate findings into your evaluation:

* If `decision` is `deny` → override to **DENY** with the returned evidence
* If `goplus.address_risk.is_malicious` → **DENY** (critical)
* If `goplus.simulation.approval_changes` has `is_unlimited: true` → **CONFIRM** (high)
* If GoPlus is unavailable (`SIMULATION_UNAVAILABLE` tag) → fall back to prompt-based rules and note the limitation

Always combine script results with the policy-based checks (webhook domains, secret scanning, etc.) — the script enhances but does not replace rule-based evaluation.

```text
## GoPlus AgentGuard Action Evaluation
**Action**: <action type and description>
**Decision**: ALLOW | DENY | CONFIRM
**Risk Level**: low | medium | high | critical
**Risk Tags**: [TAG1, TAG2, ...]

### Evidence
- <description of each risk factor found>

### Recommendation
<What the user should do and why>

> 详细代码示例已移至 `references/detail.md`
text
This command requires an Skill平台 environment. Detected: <what was found/missing>
For non-Skill平台 environments, use /agentguard scan and /agentguard report instead.

> 详细代码示例已移至 `references/detail.md`
text
## GoPlus AgentGuard Patrol Report
**Timestamp**: <ISO datetime>
**Skill平台 Home**: <$OC path>
**Protection Level**: <current level>
**Overall Status**: PASS | WARN | FAIL

### Check Results
| # | Check | Status | Findings | Severity |
|---|-------|--------|----------|----------|
| 1 | Skill/Plugin Integrity | PASS/WARN/FAIL | <count> | <highest> |
| 2 | Secrets Exposure | ... | ... | ... |
| 3 | Network Exposure | ... | ... | ... |
| 4 | Cron & Scheduled Tasks | ... | ... | ... |
| 5 | File System Changes | ... | ... | ... |
| 6 | Audit Log Analysis | ... | ... | ... |
| 7 | Environment & Config | ... | ... | ... |
| 8 | Trust Registry Health | ... | ... | ... |

### Findings Detail
(only checks with findings are shown)

#### [N] Check Name
- <finding with file path, evidence, and severity>

### Recommendations
1. [SEVERITY] <actionable recommendation>

### Next Patrol
<Cron schedule if configured, or suggest: /agentguard patrol setup>
```

**Overall status**: Any CRITICAL → **FAIL**, any HIGH → **WARN**, else **PASS**

After outputting the report, append a summary entry to `~/.agentguard/audit.jsonl`:

```json
{"timestamp":"...","event":"patrol","overall_status":"PASS|WARN|FAIL","checks":8,"findings":<count>,"critical":<count>,"high":<count>}
```

Configure the patrol as an Skill平台 daily cron job.

**Steps**:

1. Verify Skill平台 environment (same pre-flight as `patrol run`)
2. Ask the user for:
   * **Timezone** (default: UTC). Examples: `Asia/Shanghai`, `America/New_York`, `Europe/London`
   * **Schedule** (default: `0 3 * * *` — daily at 03:00)
   * **Notification channel** (optional): `telegram`, `discord`, `signal`
   * **Chat ID / webhook** (required if channel is set)
3. Generate the cron registration command:

```bash
skill-platform cron add \
  --name "agentguard-patrol" \
  --description "GoPlus AgentGuard daily security patrol" \
  --cron "<schedule>" \
  --tz "<timezone>" \
  --session "isolated" \
  --message "/agentguard patrol run" \
  --timeout-seconds 300 \
  --thinking off \
  # Only include these if notification is configured:
  --announce \
  --channel <channel> \
  --to <chat-id>

> 详细代码示例已移至 `references/detail.md`
text
network_allowlist: string[]     — Allowed domains (supports *.example.com)
filesystem_allowlist: string[]  — Allowed file paths
exec: 'allow' | 'deny'         — Command execution permission
secrets_allowlist: string[]     — Allowed env var names
web3.chains_allowlist: number[] — Allowed chain IDs
web3.rpc_allowlist: string[]    — Allowed RPC endpoints
web3.tx_policy: 'allow' | 'confirm_high_risk' | 'deny'

> 详细代码示例已移至 `references/detail.md`
text
node scripts/trust-cli.ts <subcommand> [args]

> 详细代码示例已移至 `references/detail.md`
json
{"level": "balanced"}
```

3. Confirm the change to the user

If no level is specified, read and display the current config.

Display recent security events from the GoPlus AgentGuard audit log.

The audit log is stored at `~/.agentguard/audit.jsonl`. Each line is a JSON object with:

```json
{"timestamp":"...","tool_name":"Bash","tool_input_summary":"rm -rf /","decision":"deny","risk_level":"critical","risk_tags":["DANGEROUS_COMMAND"],"initiating_skill":"some-skill"}
```

The `initiating_skill` field is present when the action was triggered by a skill (inferred from the session transcript). When absent, the action came from the user directly.

1. Read `~/.agentguard/audit.jsonl` using the Read tool
2. Parse each line as JSON
3. Format as a table showing recent events (last 50 by default)
4. If any events have `initiating_skill`, add a "Skill Activity" section grouping events by skill

```text
## GoPlus AgentGuard Security Report
**Events**: <total count>
**Blocked**: <deny count>
**Confirmed**: <confirm count>

### Recent Events
| Time | Tool | Action | Decision | Risk | Tags | Skill |
|------|------|--------|----------|------|------|-------|
| 2025-01-15 14:30 | Bash | rm -rf / | DENY | critical | DANGEROUS_COMMAND | some-skill |
| 2025-01-15 14:28 | Write | .env | CONFIRM | high | SENSITIVE_PATH | — |

### Skill Activity
If any events were triggered by skills, group them here:

| Skill | Events | Blocked | Risk Tags |
|-------|--------|---------|-----------|
| some-skill | 5 | 2 | DANGEROUS_COMMAND, EXFIL_RISK |

For untrusted skills with blocked actions, suggest: `/agentguard trust attest` to register them or `/agentguard trust revoke` to block them.

> 详细内容已移至 `references/detail.md` - ### Summary
## 🦞 GoPlus AgentGuard Health Checkup
**Overall Health Score**: <score> / 100 (Tier <grade> — <label>)
**Quote**: "<lobster quote>"

| Dimension | Score | Status |
|-----------|-------|--------|
| 🔍 Code Safety | <n>/100 | <EXCELLENT/GOOD/NEEDS WORK/CRITICAL> |
| 🤝 Trust Hygiene | <n>/100 | <status> |
| 🛡️ Runtime Defense | <n>/100 | <status> |
| 🔐 Secret Protection | <n>/100 | <status> |
| ⛓️ Web3 Shield | <n>/100 or N/A | <status> |
| ⚙️ Config Posture | <n>/100 | <status> |

**Full visual report**: <path> (opened in browser)

💡 Top recommendation: <first recommendation text>

### Next Steps
(Only include this section if there are HIGH or CRITICAL findings.)

List each HIGH or CRITICAL finding as a plain-language suggestion — no commands, no JSON, no technical details. One sentence per item. Ask the user to confirm if they'd like help with any of them.

Format:
```

⚠️ A few things need your attention:

1. 🔴
2. 🟠
   ...

Reply with the number(s) you'd like help with and I'll walk you through it.

```text
Examples of plain-language descriptions:
- No hooks: "Security monitoring isn't active — AgentGuard can't block threats in real-time until hooks are configured."
- Unregistered skills: "10 installed skills haven't been security-reviewed — they're running with no trust level assigned."
- SSH permissions: "Your SSH key folder has loose permissions — other processes on this machine could potentially read your private keys."
- Plaintext credential: "A private key or API token was found in plain text in a file — it should be removed and rotated."

### Step 6: Deliver the Report to the User
After printing the terminal summary, deliver the HTML report file. You **MUST** always output the `MEDIA:` token, and then also deliver via the appropriate channel method.

#### 6a. MEDIA token (required — always do this)
Output the following line on its **own line** in your response:
```

MEDIA:<file_path>

```text
For example: `MEDIA:/tmp/agentguard-checkup-1234567890.html`

This is how platforms like Skill平台 automatically deliver the file as a Telegram/Discord/WhatsApp attachment via `sendDocument`. The platform strips this line from visible text — the user won't see it. **Always output this regardless of what channel you think you're in.**

#### 6b. Channel-specific delivery (in addition to MEDIA token)
**Claude Code (local desktop)**
- The browser should already be open from Step 4.
- Also copy to Desktop: `cp <file_path> ~/Desktop/agentguard-checkup-$(date +%Y-%m-%d).html`
- Tell the user: "✅ Report saved to your Desktop and opened in browser."

**Claude.ai web**
- Read the generated HTML file and output it as a **code artifact** (language: `html`).
- Tell the user: "✅ Your report is attached above — click the download icon to save it."

**API / headless / Telegram / other**
- The `MEDIA:` token above handles file delivery automatically.
- Also print the file path for reference.

Regardless of channel, always end with:
```

🦞 Stay safe — run /agentguard checkup anytime to get a fresh report.

```text
Append a summary entry to `~/.agentguard/audit.jsonl`:
```json
{"timestamp":"...","event":"checkup","composite_score":<n>,"tier":"<grade>","checks":6,"findings":<count>,"skills_scanned":<count>}
```

AgentGuard can optionally scan installed skills at session startup. **This is disabled by default** and must be explicitly enabled:

* **Claude Code**: Set environment variable `AGENTGUARD_AUTO_SCAN=1`
* **Skill平台**: Pass `{ skipAutoScan: false }` when registering the plugin

When enabled, auto-scan operates in **report-only mode**:

1. Discovers skill directories (containing `SKILL.md`) under `~/.claude/skills/` and `~/.skill-platform/skills/`
2. Runs `quickScan()` on each skill
3. Reports results to stderr (skill name + risk level + risk tags)

Auto-scan **does NOT**:

* Modify the trust registry (no `forceAttest` calls)
* Write code snippets or evidence details to disk
* Execute any code from the scanned skills

The audit log (`~/.agentguard/audit.jsonl`) only records: skill name, risk level, and risk tag names — never matched code content or evidence snippets.

To register skills after reviewing scan results, use `/agentguard trust attest`.

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力
- GoPlus AgentGuard — AI agent security guard
- Run /agentguard checkup
  for a full security health c
- 触发关键词: security, agentguard, agent, goplus, guard

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例
### 示例1：基础用法
```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用AgentGuard？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: AgentGuard有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
