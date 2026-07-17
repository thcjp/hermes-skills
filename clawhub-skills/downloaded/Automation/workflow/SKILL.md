---
slug: workflow
name: workflow
version: "1.0.0"
displayName: Workflow
summary: Build automated pipelines with reusable components, data flow between nodes,
  and state management.
license: MIT
description: |-
  Build automated pipelines with reusable components, data flow between
  nodes, and state management.

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: build, automated, reusable, pipelines, workflow
tags:
- Automation
tools:
- read
- exec
---

# Workflow

## Architecture

Workflows live in `workflows/` with components and flows:

```text
workflows/
├── index.md                 # Inventory with tags
├── components/
│   ├── connections/         # Auth configs
│   ├── nodes/               # Reusable operations
│   └── triggers/            # Event sources
└── flows/{name}/
    ├── flow.md              # Definition
    ├── config.yaml          # Parameters
    ├── run.sh               # Executable
    ├── state/               # Persistent between runs
    └── logs/
```

## Quick Reference

| Topic | File |
| --- | --- |
| Directory layout, naming, formats | `structure.md` |
| Data passing between nodes | `data-flow.md` |
| Cursor, seen set, checkpoint | `state.md` |
| Retry, rollback, idempotency | `errors.md` |
| Connections, nodes, triggers | `components.md` |
| Create, test, update, archive | `lifecycle.md` |

## Requirements

* **jq** — JSON processing
* **yq** — YAML config parsing
* **curl** — HTTP requests
* **flock** — Lock files to prevent concurrent runs
* Secrets in macOS Keychain (`security find-generic-password`)

## Data Storage

* **Location:** `workflows/` in workspace root
* **State:** `flows/{name}/state/` — cursor.json, seen.json, checkpoint.json
* **Logs:** `flows/{name}/logs/` — JSONL per run
* **Data:** `flows/{name}/data/` — intermediate files between nodes

## Core Rules

### 1. Data Flow Pattern

Each node writes output to `data/{NN}-{name}.json`. Next node reads it.

```bash
curl ... > data/01-fetch.json
jq '...' data/01-fetch.json > data/02-filter.json
```

Breaking this pattern = nodes can't communicate.

### 2. Error Declaration

Every node in flow.md MUST declare:

* **On error:** retry(N) | fail | continue | alert
* **On empty:** skip | continue | fail

Undefined behavior = unpredictable workflow.

### 3. Lock Files

Prevent concurrent runs:

```bash
LOCKFILE="/tmp/workflow-${NAME}.lock"
exec 200>"$LOCKFILE"
flock -n 200 || exit 0
```

### 4. State Files

| File | Purpose |
| --- | --- |
| cursor.json | "Where did I leave off?" |
| seen.json | "What have I processed?" |
| checkpoint.json | "Multi-step recovery" |

### 5. Component Reuse

Before creating new connections/nodes/triggers:

```bash
ls workflows/components/connections/
ls workflows/components/nodes/
```

Use existing. Update "Workflows Using This" when adding.

---

**Related:** For LLM-driven multi-phase processes, see the `cycle` skill.

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
