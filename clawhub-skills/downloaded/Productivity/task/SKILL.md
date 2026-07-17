---
slug: task
name: task
version: "0.1.0"
displayName: Task
summary: Tasker docstore task management via tool-dispatch. Use for task lists, due
  today/overdue, week pl...
license: MIT
description: |-
  Tasker docstore task management via tool-dispatch. Use for task lists,
  due today/overdue, week pl...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: task, management, docstore, tasker
tags:
- Productivity
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
