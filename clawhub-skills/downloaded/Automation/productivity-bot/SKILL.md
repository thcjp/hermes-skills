---
slug: productivity-bot
name: productivity-bot
version: "1.0.0"
displayName: Productivity Bot
summary: Automation bot for productivity tasks including data processing, scheduled
  notifications, and wor...
license: MIT-0
description: |-
  Automation bot for productivity tasks including data processing, scheduled
  notifications, and wor...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: productivity, including, automation, tasks, data, bot
tags:
- Automation
- Integrations
tools:
- read
- exec
---

# Productivity Bot

Automation bot for everyday productivity tasks.

## Features

### 1. Data Automation

* Auto-process CSV/Excel files
* Data transformation pipelines
* Report generation

### 2. Scheduled Tasks

* Daily reminders
* Periodic data syncs
  -定时报告

### 3. Notifications

* Email alerts
* Slack/Discord messages
* Custom webhooks

## Usage

```python
from productivity_bot import Scheduler, DataProcessor

scheduler = Scheduler()
scheduler.every day.at("9:00").do(send_report)

processor = DataProcessor()
processor.clean("dirty_data.csv").export("clean_data.csv")
```

## Requirements

* Python 3.8+
* Various API keys

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
