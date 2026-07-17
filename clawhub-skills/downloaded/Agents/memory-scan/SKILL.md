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
  content, credential leaks, ...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: files, memory, scan, openclaw, scans, agent
tags:
- Agents
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
