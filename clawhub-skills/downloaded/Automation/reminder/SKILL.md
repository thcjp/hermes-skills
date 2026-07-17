---
slug: reminder
name: reminder
version: "0.1.1"
displayName: Reminder
summary: Capture natural-language events, save to your workspace, and schedule Telegram
  reminders with aut...
license: MIT
description: |-
  Capture natural-language events, save to your workspace, and schedule
  Telegram reminders with aut...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: save, events, language, natural, reminder, capture
tags:
- Automation
tools:
- read
- exec
---

# Reminder

A lightweight personal secretary for Skill平台:

* Tell it events in natural language (Chinese/English).
* It extracts structured info and stores it in your workspace (so Git/`claw-roam` can sync across devices).
* It schedules Telegram reminders using Skill平台 `cron`.

## What it does

* Capture events from chat (meetings / birthdays / deadlines)
* Store events in a **workspace data file** (easy to back up & sync via Git/`claw-roam`)
* Schedule Telegram reminders using Skill平台 `cron`
* Answer queries like “我最近有什么安排/计划？”

## Data (separated from skill)

This skill contains **no personal event data**.

User data lives in the workspace at:

* Events file: `~/.skill-platform/workspace/reminders/events.yml`

Template (shipped with the skill):

* `skills/reminder/assets/events.template.yml`

## Config (env)

* `REMINDER_TZ` (default: `Asia/Shanghai`)
* `REMINDER_OFFSETS_MINUTES` (default: `1440,60,10` for 24h/1h/10m)

## Capture behavior

When user says something like:

* “后天上午10点有个会”
* “下个月2号我妈生日”
* “周五下午三点交报告”

Do:

1. Parse the event:
   * title
   * start datetime (Shanghai)
   * notes (optional)
   * reminders offsets (default 24h/1h/10m)
   * repeat (optional: yearly/monthly/weekly)
2. If key info is ambiguous (e.g. ‘后天’ date, ‘下个月’ which month, lunar birthday conversion, time missing), ask **only the minimal** clarifying question(s).
3. Write/update the event in `reminders/events.yml`.
4. Create `cron` jobs for each reminder time (delivery to current Telegram).

## Reply style

* After scheduling: reply briefly with the resolved datetime + confirmation.
* For cancellations/changes: confirm what was changed and whether cron jobs were removed/replaced.

## Queries

If user asks:

* “我最近有什么安排？”
* “下周有什么？”

Then read `reminders/events.yml`, compute upcoming items (Shanghai time), and summarize.

## Notes / safety

* Never commit machine-specific secrets (keep them in `LOCAL_CONFIG.md`, already gitignored).
* For lunar birthdays: store the canonical lunar date + the computed solar date for the target year; ask how to handle leap months when needed.

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
