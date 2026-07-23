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
  Telegram reminders with aut。Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Automation
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

- Capture natural-language events, save to your workspace, and schedule
  Telegram reminders with aut
- 触发关键词: save, events, language, natural, reminder, capture

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

### Q1: 如何开始使用Reminder？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Reminder有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
