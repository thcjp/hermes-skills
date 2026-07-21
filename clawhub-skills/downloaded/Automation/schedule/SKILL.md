---
slug: schedule
name: schedule
version: "1.0.2"
displayName: Schedule
summary: Program recurring or one-time tasks. User defines what to do, skill handles
  when.
license: MIT
description: |-
  Program recurring or one-time tasks。User defines what to do, skill
  handles when。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Automation
tools:
  - - read
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

- Program recurring or one-time tasks
- User defines what to do, skill
  handles when
- 触发关键词: program, schedule, tasks, recurring, time

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

### Q1: 如何开始使用Schedule？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Schedule有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
