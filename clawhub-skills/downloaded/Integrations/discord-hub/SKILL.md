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
  commands, messages, and oper。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

- OpenClaw skill for Discord Bot API workflows, covering interactions,
  commands, messages, and oper
- 触发关键词: discord, workflows, openclaw, covering, hub, skill

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

### Q1: 如何开始使用Discord？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Discord有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
