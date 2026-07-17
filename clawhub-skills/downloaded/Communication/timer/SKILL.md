---
slug: timer
name: timer
version: "1.0.0"
displayName: timer
summary: Set timers and alarms. When a background timer completes, you receive a System
  notification - res...
license: MIT
description: |-
  Set timers and alarms. When a background timer completes, you receive
  a System notification - res...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: timers, timer, alarms, background
tags:
- Communication
tools:
- read
- exec
---

# timer

Set timers that run in the background. When they complete, you will receive a system notification and MUST respond with the reminder to notify the user.

## Quick Start

```bash
bash background:true command:"node {baseDir}/timer.js 5m"

bash background:true command:"node {baseDir}/timer.js 10m 'Check the oven'"

bash background:true command:"node {baseDir}/timer.js 30s"

bash background:true command:"node {baseDir}/timer.js 1h"
```

## Time Formats

| Format | Description | Example |
| --- | --- | --- |
| `Ns` | N seconds | `30s`, `90s` |
| `Nm` | N minutes | `5m`, `15m` |
| `Nh` | N hours | `1h`, `2h` |
| `N` | N minutes (default) | `5` = 5 minutes |
| `MM:SS` | Minutes and seconds | `5:30` |
| `HH:MM:SS` | Hours, minutes, seconds | `1:30:00` |

## ⚠️ CRITICAL: Timer Completion Notification

When a timer completes, you receive a `System:` message like:

```text
System: [2026-01-24 21:27:13] Exec completed (swift-me, code 0) :: ⏰ Timer complete! Check the pasta!
```

### ❌ WRONG - Do NOT respond like this:

```text
HEARTBEAT_OK

🎉 Your timer is complete! Check the pasta!
```

This response will be **filtered and NOT delivered** to the user!

### ✅ CORRECT - Respond like this:

```text
⏰ Timer Alert! Your timer is complete: Check the pasta!
```

Start directly with the notification message. Do NOT include HEARTBEAT_OK.

**Why?** Responses starting with `HEARTBEAT_OK` followed by less than 300 characters are automatically suppressed and never reach the user. Your timer notification will be lost!

## Examples

### Cooking Timer

```bash
bash background:true command:"node {baseDir}/timer.js 12m 'Pasta is ready!'"
```

When complete, respond: "⏰ Your 12-minute timer is up! Pasta is ready!"

### Quick Reminder

```bash
bash background:true command:"node {baseDir}/timer.js 2m 'Take a break'"
```

### Pomodoro Session

```bash
bash background:true command:"node {baseDir}/timer.js 25m 'Pomodoro done - time for a break!'"
bash background:true command:"node {baseDir}/timer.js 5m 'Break over - back to work!'"
```

### Multiple Timers

```bash
bash background:true command:"node {baseDir}/timer.js 5m 'Tea is ready'"
bash background:true command:"node {baseDir}/timer.js 10m 'Eggs are done'"
bash background:true command:"node {baseDir}/timer.js 30m 'Meeting starts soon'"
```

## Managing Timers

```bash
process action:list

process action:poll sessionId:XXX

process action:log sessionId:XXX

process action:kill sessionId:XXX
```

## Notes

* Timers run as background processes with unique sessionIds
* Completed timers exit with code 0
* Cancelled timers (via kill) exit with code 130
* Sound notification plays on macOS when timer completes (if `afplay` available)
* Progress is logged every second (short timers) or every 10 seconds (long timers)

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
