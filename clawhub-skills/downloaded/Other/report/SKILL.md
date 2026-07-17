---
slug: report
name: report
version: "1.0.3"
displayName: Report
summary: Configure custom recurring reports. User defines data sources, skill handles
  scheduling and forma...
license: MIT
description: |-
  Configure custom recurring reports. User defines data sources, skill
  handles scheduling and forma...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: custom, report, configure, recurring, reports
tags:
- Other
tools:
- read
- exec
---

# Report

## Data Storage

```text
~/report/
├── memory.md               # Index + preferences
├── {name}/
│   ├── config.md           # Report configuration
│   ├── data.jsonl          # Historical data
│   └── generated/          # Past reports
```

Create on first use: `mkdir -p ~/report`

## Scope

This skill:

* ✅ Stores report configurations in ~/report/
* ✅ Generates reports on schedule
* ✅ Delivers via channels user configures

**User-driven model:**

* User defines WHAT data to include
* User grants access to any needed sources
* User provides API keys if external data needed
* Skill handles SCHEDULING and FORMATTING

This skill does NOT:

* ❌ Access APIs without user-provided credentials
* ❌ Pull data from sources user hasn't specified
* ❌ Store credentials (user provides via environment)

## Environment Variables

**No fixed requirements.** User provides API keys as needed:

```bash
export STRIPE_API_KEY="[REDACTED]"

export GITHUB_TOKEN="[REDACTED]"
```

Config references env var name, never the value.

## Delivery Security

External delivery (Telegram/webhook/email) sends report content off-device.

* User explicitly configures each channel
* User responsible for trusting destination
* `file` delivery stays local (~/report/{name}/generated/)

## Quick Reference

| Task | File |
| --- | --- |
| Configuration schema | `schema.md` |
| Output formats | `formats.md` |
| Delivery options | `delivery.md` |

## Core Rules

### 1. User Defines Data Sources

When creating a report:

1. User specifies what data to track
2. If external API needed, user provides credentials
3. Credentials stored as env var references, not values

Example:

```text
User: "Weekly report on my Stripe revenue"
Agent: "I'll need Stripe API access. Please set
        STRIPE_API_KEY in your environment."
User: "Done"
→ Config stored with "source": {"type": "api", "env": "STRIPE_API_KEY"}
```

### 2. Report Configuration

In ~/report/{name}/config.md:

```yaml
name: weekly-revenue
schedule: "0 9 * * 1"  # Monday 9am
sources:
  - type: api
    env: STRIPE_API_KEY  # User provides
format: chat
delivery: telegram
```

### 3. Scheduling

| Frequency | Cron | Example |
| --- | --- | --- |
| Daily | `0 9 * * *` | 9am daily |
| Weekly | `0 9 * * 1` | Monday 9am |
| Monthly | `0 9 1 * *` | 1st of month |
| On-demand | - | When user asks |

### 4. Delivery Channels

User configures in config.md:

* `chat` — Reply in conversation
* `telegram` — Send to Telegram (user provides chat ID)
* `file` — Save to ~/report/{name}/generated/
* `email` — Send via user's configured mail

### 5. Managing Reports

```text
"List my reports" → Read ~/report/memory.md
"Pause X report" → Update config
"Run X now" → Generate on-demand
```

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
