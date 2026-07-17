---
slug: monitor
name: monitor
version: "1.0.2"
displayName: Monitor
summary: Create monitors for anything. User defines what to check, skill handles scheduling
  and alerts.
license: MIT
description: |-
  Create monitors for anything. User defines what to check, skill handles
  scheduling and alerts.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: anything, create, monitor, defines, monitors
tags:
- Other
tools:
- read
- exec
---

# Monitor

## Data Storage

```text
~/monitor/
├── monitors.json       # Monitor definitions
├── config.json         # Alert preferences
└── logs/               # Check results
    └── {name}/YYYY-MM.jsonl
```

Create on first use: `mkdir -p ~/monitor/logs`

## Scope

This skill:

* ✅ Stores monitor definitions in ~/monitor/
* ✅ Runs checks at specified intervals
* ✅ Alerts user on status changes

**Execution model:**

* User explicitly defines WHAT to monitor
* User grants any permissions/tools needed
* Skill only handles WHEN and ALERTING

This skill does NOT:

* ❌ Assume access to any service or endpoint
* ❌ Run checks without user-defined instructions
* ❌ Store credentials (user provides via environment or other skills)

## Requirements

**Required:**

* `curl` — for HTTP checks

**Optional (for alerts):**

* `PUSHOVER_TOKEN` / `PUSHOVER_USER` — for push notifications
* Webhook URL — user provides their own endpoint

**Used if available:**

* `openssl` — for SSL certificate checks
* `pgrep` — for process checks
* `df` — for disk space checks
* `nc` — for port checks

## Quick Reference

| Topic | File |
| --- | --- |
| Monitor type examples | `templates.md` |
| Alert configuration | `alerts.md` |
| Analysis patterns | `insights.md` |

## Core Rules

### 1. User Defines Everything

When user requests a monitor:

1. **WHAT**: User specifies what to check
2. **HOW**: User provides method or grants tool access
3. **WHEN**: This skill handles interval
4. **ALERT**: This skill handles notifications

Example flow:

```text
User: "Monitor my API at api.example.com every 5 minutes"
Agent: "I'll check HTTP status. Alert you on failures?"
User: "Yes, and check SSL cert too"
→ Monitor stored with user-defined checks
```

### 2. Monitor Definition

In ~/monitor/monitors.json:

```json
{
  "api_prod": {
    "description": "User's API health",
    "checks": [
      {"type": "http", "target": "https://api.example.com/health"},
      {"type": "ssl", "target": "api.example.com"}
    ],
    "interval": "5m",
    "alert_on": "change",
    "requires": [],
    "created": "2024-03-15"
  }
}
```

### 3. Common Check Types

User can request any of these (or others):

| Type | What it checks | Tool used |
| --- | --- | --- |
| http | URL status + latency | curl |
| ssl | Certificate expiry | openssl |
| process | Process running | pgrep |
| disk | Free space | df |
| port | Port open | nc |
| custom | User-defined command | user specifies |

### 4. Confirmation Format

```text
✅ Monitor: [description]
🔍 Checks: [what will be checked]
⏱️ Interval: [how often]
🔔 Alert: [when to notify]
🔧 Requires: [tools/access needed]
```

### 5. Alert on Change

* Alert when status changes (ok→fail, fail→ok)
* Include failure count
* Recovery message when back to OK
* Never spam repeated same-status

### 6. Permissions

The `requires` field lists what user granted:

* Empty = basic checks only (curl, df, pgrep)
* `["ssh:server1"]` = user granted SSH access
* `["docker"]` = user granted Docker access

Agent asks before assuming any access.

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
