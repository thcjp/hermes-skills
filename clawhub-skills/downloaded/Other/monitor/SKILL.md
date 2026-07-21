---
slug: monitor
name: monitor
version: "1.0.2"
displayName: Monitor
summary: Create monitors for anything. User defines what to check, skill handles scheduling
  and alerts.
license: MIT
description: |-
  Create monitors for anything。User defines what to check, skill handles
  scheduling and alerts。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
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

- Create monitors for anything
- User defines what to check, skill handles
  scheduling and alerts
- 触发关键词: anything, create, monitor, defines, monitors

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

### Q1: 如何开始使用Monitor？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Monitor有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
