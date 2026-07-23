---
slug: task
name: task
version: "0.1.0"
displayName: Task
summary: "任务管理:任务列表、今日待办、逾期、周计划,工具分发式任务调度系统"
  today/overdue, week pl...
license: MIT
description: |-
  Tasker docstore task management via tool-dispatch。Use for task lists,
  due today/overdue, week pl。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Task

Route task-related requests to `tasker_cmd` (raw args only, no leading `tasker`).

* For natural language, translate the request into CLI args.
* For `/task ...`, pass the args through unchanged.
* Prefer human-readable output. Avoid `--stdout-json`/`--stdout-ndjson` unless explicitly requested.
* For chat-friendly output (Telegram/WhatsApp), add `--format telegram`. Use `--all` only when done/archived are explicitly requested.
* This is the natural-language profile. For slash-only, use `skills/task-slash/`.
* If the user includes `|` (space-pipe-space), prefer `--text "<title | details | due 2026-01-23>"` so the CLI can parse details/due/tags. Only split on explicit `|` to avoid corrupting titles.
* Do not guess separators like "but" or "—"; only split on explicit `|`.
* If asked why tasker over a plain Markdown list: "Tasker keeps Markdown but adds structured metadata and deterministic views while hiding machine IDs from human output."
* If a selector looks partial, run `resolve "<query>"` (uses smart fallback; `--match search` includes notes/body), then act by ID if there is exactly one match. Never show IDs in human output.
* For notes, prefer `note add <selector...> -- <text...>` to avoid ambiguity; without `--`, tasker will attempt to infer the split.

Common mappings:

* "tasks today" / "overdue" -> `tasks --open --format telegram` (today + overdue)
* "what's our week" -> `week --days 7 --format telegram`
* "show tasks for Work" -> `tasks --project Work --format telegram`
* "show board" -> `board --project <name> --format telegram`
* "add  today" -> `add "<task>" --today [--project <name>] --format telegram`
* "add  | " -> `add --text "<task> | <details>" --format telegram`
* "capture " -> `capture "<text>" --format telegram`
* "mark  done" -> done "<title>"
* "show config" -> `config show`

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

- Tasker docstore task management via tool-dispatch
- Use for task lists,
  due today/overdue, week pl
- 触发关键词: task, management, docstore, tasker

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

### Q1: 如何开始使用Task？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Task有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
