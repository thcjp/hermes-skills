---
slug: schedule
name: schedule
version: "1.0.2"
displayName: Schedule
summary: Program recurring or one-time tasks. User defines what to do, skill handles
  when.
license: MIT
description: |-
  Program recurring or one-time tasks. User defines what to do, skill
  handles when.

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: program, schedule, tasks, recurring, time
tags:
- Automation
tools:
- read
- exec
---

# Schedule

## Data Storage

```text
~/schedule/
├── jobs.json           # Job definitions
├── preferences.json    # Timezone, preferred times
└── history/            # Execution logs
    └── YYYY-MM.jsonl
```

Create on first use: `mkdir -p ~/schedule/history`

## Scope

This skill:

* ✅ Stores scheduled job definitions in ~/schedule/
* ✅ Triggers jobs at specified times
* ✅ Learns timezone and time preferences from user

**Execution model:**

* User explicitly defines WHAT the job does
* User grants any permissions needed for the job
* Skill only handles WHEN, not WHAT

This skill does NOT:

* ❌ Assume access to any external service
* ❌ Modify system crontab or launchd
* ❌ Execute jobs without user-defined instructions

## Quick Reference

| Topic | File |
| --- | --- |
| Cron expression syntax | `patterns.md` |
| Common mistakes | `traps.md` |
| Job format | `jobs.md` |

## Core Rules

### 1. User Defines Everything

When user requests a scheduled task:

1. **WHAT**: User specifies the action (may require other skills/permissions)
2. **WHEN**: This skill handles timing
3. **HOW**: User grants any needed access explicitly

Example flow:

```text
User: "Every morning, summarize my emails"
Agent: "I'll schedule this for 8am. This will need email access —
        do you want me to use the mail skill for this?"
User: "Yes"
→ Job stored with explicit reference to mail skill
```

### 2. Simple Requests

| Request | Action |
| --- | --- |
| "Remind me to X at Y" | Store job, confirm |
| "Every morning do X" | Ask time, store job |
| "Cancel X" | Remove from jobs.json |

### 3. Confirmation Format

```text
✅ [what user requested]
📅 [when] ([timezone])
🔧 [permissions/skills needed, if any]
🆔 [id]
```

### 4. Job Persistence

In ~/schedule/jobs.json:

```json
{
  "daily_review": {
    "cron": "0 9 * * 1-5",
    "task": "User-defined task description",
    "requires": ["mail"],
    "created": "2024-03-15",
    "timezone": "Europe/Madrid"
  }
}
```

The `requires` field explicitly lists any skills/access the job needs.

### 5. Execution

When scheduled time arrives:

* Agent executes the user-defined task
* Uses only permissions user explicitly granted
* Logs result to history/

### 6. Preferences

After first job, store in preferences.json:

* Timezone
* Preferred "morning" / "evening" times
* Default notification style

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
