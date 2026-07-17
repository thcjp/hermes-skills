---
slug: task-planner
name: task-planner
version: "3.0.5"
displayName: Task Planner
summary: Manage tasks, set priorities, and track deadlines locally. Supports bilingual
  (EN/CN) documentati...
license: MIT-0
description: |-
  Manage tasks, set priorities, and track deadlines locally. Supports
  bilingual (EN/CN) documentati...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: track, planner, priorities, tasks, deadlines, manage, task
tags:
- Productivity
tools:
- read
- exec
---

# Task Planner

Your professional local task manager. All data stays on your machine.

## Quick Start / 快速开始

Just ask your AI assistant: / 直接告诉 AI 助手：

* "Add a high priority task: Finish report by Friday" (添加高优先级任务：周五前完成报告)
* "Show all tasks due today" (显示今日待办任务)
* "Mark task #1 as completed" (标记任务1为已完成)

## When to Use / 使用场景

* **Daily Workflow**: Organizing your immediate to-do list and staying productive.
* **Deadline Tracking**: Keeping an eye on upcoming project milestones and due dates.
* **Privacy First**: When you need a task manager that doesn't upload your data to the cloud.

## Requirements / 要求

* bash 4+
* python3 (standard library)

## Safety & Privacy / 安全与隐私

* **Local Storage**: All data is stored in `~/.task-planner/tasks.json`.
* **No Cloud**: This tool does NOT make any network calls or cloud sync.
* **Minimalist**: Only standard Linux tools and Python 3 are required.

## Commands / 常用功能

### add

Add a new task with optional priority and due date.

```bash
bash scripts/script.sh add "Task description" --priority high --due 2026-12-31
```

### list

Display pending or all tasks.

```bash
bash scripts/script.sh list --status pending
```

### done

Complete a task by ID.

```bash
bash scripts/script.sh done 1
```

## Feedback

<https://bytesagain.com/feedback/>
Powered by BytesAgain | bytesagain.com

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
