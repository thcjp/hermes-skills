---
slug: queue-task
name: queue-task
version: "0.1.0"
displayName: Queue Task
summary: Durable queue-task helper for resumable, idempotent batch jobs in task-father
  task folders.
license: MIT
description: |-
  Durable queue-task helper for resumable, idempotent batch jobs in task-father
  task folders.

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: resumable, task, helper, queue, durable
tags:
- Automation
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
