---
slug: queue-task
name: queue-task
version: "0.1.0"
displayName: Queue Task
summary: "task-father目录的可恢复幂等批处理队列任务助手(社区下载版)"
  task folders.
license: MIT
description: |-
  Durable queue-task helper for resumable, idempotent batch jobs in task-father
  task folders。核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关...
tags:
- Automation
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Queue Task

Use this skill for durable long-running queue jobs with resumable batches.

Layout (task-father only):

* `<WORKSPACE_DIR>/<TASKS_DIR>/<slug>/...`

State files:

* `queue.jsonl`
* `progress.json`
* `done.jsonl`
* `failed.jsonl`
* `lock.json`

## Prerequisites

* `python3 --version`
* `skill-platform status`
* `skill-platform cron --help`

## Configuration (portable)

Skill-local config:

* Example: `config.env.example`
* Real machine config: `config.env`

Keys:

* `WORKSPACE_DIR`
* `TASKS_DIR`
* `BATCH_SIZE`
* `LOCK_STALE_MINUTES`
* `CRON_EXPR`
* `CRON_TZ`
* `DELIVERY_MODE`
* `AGENT_ID`

## Initialization / Installation / Onboarding

### Preferred (chat-first)

Provide:

1. task slug
2. batch size
3. lock stale minutes
4. schedule and timezone

Then initialize:

* `python3 scripts/queue_task.py init <slug>`

Smoke test:

* `python3 scripts/queue_task.py status <slug>`

### Optional (terminal)

* `cp config.env.example config.env`
* Edit `config.env`
* Run init/status commands above.

## Commands

* Init files:
  + `python3 scripts/queue_task.py init <slug>`
* Status:
  + `python3 scripts/queue_task.py status <slug>`
* Clear stale lock:
  + `python3 scripts/queue_task.py clear-stale-lock <slug>`
* Print worker template:
  + `python3 scripts/queue_task.py print-supervisor-template`

## Usage notes

* Prefer append-only JSONL logs.
* Process small batches.
* Update `progress.json` after each item.
* Keep idempotency keys task-defined.
* Use lock file to avoid concurrent runs.

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

- Durable queue-task helper for resumable, idempotent batch jobs in task-father
  task folders
- 触发关键词: resumable, task, helper, queue, durable

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

### Q1: 如何开始使用Queue Task？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Queue Task有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
