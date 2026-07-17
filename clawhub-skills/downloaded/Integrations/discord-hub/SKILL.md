---
slug: discord-hub
name: discord-hub
version: "1.1.0"
displayName: Discord
summary: OpenClaw skill for Discord Bot API workflows, covering interactions, commands,
  messages, and oper...
license: MIT
description: |-
  OpenClaw skill for Discord Bot API workflows, covering interactions,
  commands, messages, and oper...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: discord, workflows, openclaw, covering, hub, skill
tags:
- Integrations
tools:
- read
- exec
---

# Discord

## Purpose

Provide a production-oriented guide for building Discord bot workflows via the REST API and Interactions, focusing on professional command UX, safe operations, and direct HTTPS usage (no SDKs).

## Best fit

* You want command-first bot behavior and clear interaction flows.
* You prefer direct HTTP requests without a library dependency.
* You need a structured map of Discord API surfaces.

## Not a fit

* You need a full SDK or gateway client implementation.
* You plan to stream large media uploads directly.

## Quick orientation

* Read `references/discord-api-overview.md` for base URL, versioning, and object map.
* Read `references/discord-auth-and-tokens.md` for token types and security boundaries.
* Read `references/discord-interactions.md` for interaction lifecycle and response patterns.
* Read `references/discord-app-commands.md` for slash, user, and message commands.
* Read `references/discord-messages-components.md` for messages, embeds, and components.
* Read `references/discord-gateway-webhooks.md` for gateway vs webhook tradeoffs.
* Read `references/discord-rate-limits.md` for throttling and header-based handling.
* Read `references/discord-request-templates.md` for HTTP payload templates.
* Read `references/discord-feature-map.md` for the full surface checklist.

## Required inputs

* Bot token and application ID.
* Interaction endpoint public key (if using interaction webhooks).
* Command list and UX tone.
* Allowed intents and event scope.

## Expected output

* A clear bot workflow plan, command design, and operational checklist.

## Operational notes

* Prefer interactions and slash commands over prefix parsing.
* Always validate incoming interaction signatures.
* Keep payloads small and respond quickly to interactions.

## Security notes

* Never log tokens or secrets.
* Use least-privilege permissions and scopes.

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
