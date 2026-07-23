---
slug: memory-scan
name: memory-scan
version: "1.0.0"
displayName: Memory Scan
summary: Scans OpenClaw agent memory files and workspace configs for malicious content,
  credential leaks, ...
license: MIT
description: |-
  Scans OpenClaw agent memory files and workspace configs for malicious
  content, credential leaks, 。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Agents
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Memory Scan

**Security scanner for Skill平台 agent memory files**

Scans MEMORY.md, daily logs (memory/*.md), and workspace configuration files for malicious content, prompt injection, credential leakage, and dangerous instructions that could compromise user security.

## Purpose

Detect security threats embedded in agent memory:

* Malicious instructions to bypass guardrails
* Prompt injection patterns in stored memories
* Credential/secret leakage
* Data exfiltration commands
* Behavioral manipulation
* Security policy violations

## Usage

### On-Demand Scan

Scan all memory files:

```bash
python3 skills/memory-scan/scripts/memory-scan.py
```

Allow remote LLM analysis (redacted content only):

```bash
python3 skills/memory-scan/scripts/memory-scan.py --allow-remote
```

Scan specific file:

```bash
python3 skills/memory-scan/scripts/memory-scan.py --file memory/2026-02-01.md
```

Quiet mode (for automation):

```bash
python3 skills/memory-scan/scripts/memory-scan.py --quiet
```

JSON output:

```bash
python3 skills/memory-scan/scripts/memory-scan.py --json
```

### Scheduled Monitoring

#### Cron Job (Daily Security Audit)

Already included in safe-install daily audit - runs 2pm PT daily.

To add standalone cron:

```bash
bash skills/memory-scan/scripts/schedule-scan.sh
```

Requires:

* `OPENCLAW_ALERT_CHANNEL` (configured in Skill平台)
* `OPENCLAW_ALERT_TO` (optional, for channels that require a recipient)

Creates cron job: daily at 3pm PT, sends alert only if threats found.

#### Heartbeat Integration

Add to HEARTBEAT.md:

```markdown
## Weekly Memory Scan

Every Sunday, run memory scan:
python3 skills/memory-scan/scripts/memory-scan.py --quiet
```

## Security Levels

* **SAFE** - No threats detected
* **LOW** - Minor concerns, proceed with awareness
* **MEDIUM** - Potential threat, review recommended
* **HIGH** - Likely threat, immediate review required
* **CRITICAL** - Active threat detected, quarantine recommended

## What It Scans

1. **MEMORY.md** - Long-term memory
2. **memory/*.md** - Daily logs (last 30 days by default)
3. **Workspace config files**:
   * AGENTS.md, SOUL.md, USER.md, TOOLS.md
   * HEARTBEAT.md, GUARDRAILS.md, IDENTITY.md
   * BOOTSTRAP.md (if exists)
   * STOCKS_MEMORIES.md (if exists)

## Detection Categories

1. **Malicious Instructions** - Commands to harm user/data
2. **Prompt Injection** - Embedded manipulation patterns
3. **Credential Leakage** - API keys, passwords, tokens
4. **Data Exfiltration** - Instructions to leak data
5. **Guardrail Bypass** - Attempts to override security
6. **Behavioral Manipulation** - Unauthorized personality changes
7. **Privilege Escalation** - Attempts to gain unauthorized access

## Alert Workflow

On MEDIUM/HIGH/CRITICAL detection:

1. Stop processing
2. Send alert via configured Skill平台 channel with:
   * Severity level
   * File location (file:line)
   * Threat description
   * Recommended action
3. Optional: Quarantine threat (backup + redact)

## LLM Provider

Auto-detects provider from Skill平台 config:

* Prefers OpenAI (gpt-4o-mini) if OPENAI_API_KEY set
* Falls back to Anthropic (claude-sonnet-4-5) if available
* Uses gateway model config

**Remote LLM scanning is disabled by default**. Use `--allow-remote` to enable
redacted LLM analysis.

## Quarantine

To quarantine a detected threat:

```bash
python3 skills/memory-scan/scripts/quarantine.py memory/2026-02-01.md 42
```

Creates:

* Backup: `.memory-scan/quarantine/memory_2026-02-01_line42.backup`
* Redacts line 42 with: `[QUARANTINED BY MEMORY-SCAN: <timestamp>]`

## Files

* `scripts/memory-scan.py` - Main scanner (local patterns + optional LLM with `--allow-remote`)
* `scripts/schedule-scan.sh` - Create cron job for daily scans
* `scripts/quarantine.py` - Quarantine detected threats
* `docs/detection-prompt.md` - LLM detection prompt template

## Integration with Other Skills

* **safe-install**: Daily audit already includes memory-scan
* **input-guard**: Complementary (input-guard = external, memory-scan = internal)
* **molthreats**: Can report memory-based threats to community feed

## Example

```bash
$ python3 skills/memory-scan/scripts/memory-scan.py

🧠 Memory Security Scan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Scanning memory files...

✓ MEMORY.md - SAFE
✓ memory/2026-02-01.md - SAFE
⚠ memory/2026-01-30.md - MEDIUM (line 42)
  → Potential credential leakage: API key pattern detected

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall: MEDIUM
Action: Review memory/2026-01-30.md:42
```

## Agent Workflow

When user requests memory scan:

1. Run: `python3 skills/memory-scan/scripts/memory-scan.py`
2. If MEDIUM+: Send alert immediately via configured channel
3. Summarize findings
4. Ask if user wants to quarantine threats

## Notes

* Scans last 30 days of daily logs by default (configurable with --days)
* Uses same LLM approach as input-guard for consistency
* Does NOT auto-quarantine - always asks first
* Safe to run frequently (minimal API cost with efficient chunking)

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

- Scans OpenClaw agent memory files and workspace configs for malicious
  content, credential leaks,
- 触发关键词: files, memory, scan, openclaw, scans, agent

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

## 错误处理
- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Memory Scan？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Memory Scan有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 案例展示

```json
{
  "input": "示例输入",
  "output": "处理结果"
}
```

## 输出格式

处理结果以结构化格式返回, 包含状态码、消息和数据字段。
