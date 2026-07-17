---
slug: mcporter
name: mcporter
version: "1.0.0"
displayName: Mcporter
summary: Use the mcporter CLI to list, configure, auth, and call MCP servers/tools.
license: MIT
description: |-
  Use the mcporter CLI to list, configure, auth, and call MCP servers/tools.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: call, mcporter, list, configure, auth
tags:
- Other
tools:
- read
- exec
---

# Mcporter

Use `mcporter` to work with MCP servers directly.

Quick start

* `mcporter list`
* `mcporter list <server> --schema`
* `mcporter call <server.tool> key=value`

Call tools

* Selector: `mcporter call linear.list_issues team=ENG limit:5`
* Function syntax: `mcporter call "linear.create_issue(title: \"Bug\")"`
* Full URL: `mcporter call https://api.example.com/mcp.fetch url:https://example.com`
* Stdio: `mcporter call --stdio "bun run ./server.ts" scrape url=https://example.com`
* JSON payload: `mcporter call <server.tool> --args '{"limit":5}'`

Auth + config

* OAuth: `mcporter auth <server | url> [--reset]`
* Config: `mcporter config list|get|add|remove|import|login|logout`

Daemon

* `mcporter daemon start|status|stop|restart`

Codegen

* CLI: `mcporter generate-cli --server <name>` or `--command <url>`
* Inspect: `mcporter inspect-cli <path> [--json]`
* TS: `mcporter emit-ts <server> --mode client|types`

Notes

* Config default: `./config/mcporter.json` (override with `--config`).
* Prefer `--output json` for machine-readable results.

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
