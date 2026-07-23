---
slug: task-planner
name: task-planner
version: "3.0.5"
displayName: Task Planner
summary: Manage tasks, set priorities, and track deadlines locally. Supports bilingual
  (EN/CN) documentati...
license: MIT-0
description: |-
  Manage tasks, set priorities, and track deadlines locally。Supports
  bilingual (EN/CN) documentati。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Task Planner

Your professional local task manager. All data stays on your machine.

## 使用流程

Just ask your AI assistant: / 直接告诉 AI 助手：

* "Add a high priority task: Finish report by Friday" (添加高优先级任务：周五前完成报告)
* "Show all tasks due today" (显示今日待办任务)
* "Mark task #1 as completed" (标记任务1为已完成)

## 适用场景

* **Daily Workflow**: Organizing your immediate to-do list and staying productive.
* **Deadline Tracking**: Keeping an eye on upcoming project milestones and due dates.
* **Privacy First**: When you need a task manager that doesn't upload your data to the cloud.

## 依赖说明

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

## 核心能力

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

## 示例

### 示例1：基础用法

```
Just ask your AI assistant: / 直接告诉 AI 助手：

* "Add a high priority task: Finish report by Friday" (添加高优先级任务：周五前完成报告)
* "Show all tasks due today" (显示今日待办任务)
* "Mark task #1 as completed" (标记任务1为已完成)
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Task Planner？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Task Planner有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 本地运行，不支持多设备同步
