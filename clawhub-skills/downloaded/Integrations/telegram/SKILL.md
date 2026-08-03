---
slug: telegram
name: telegram
version: "1.0.1"
displayName: Telegram
summary: "设计Telegram Bot API工作流与命令驱动对话(社区下载版)"
  conversations using di...
license: MIT
description: |-
  OpenClaw skill for designing Telegram Bot API workflows and command-driven
  conversations using di。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Telegram

## Purpose

Provide a clean, production-oriented guide for building Telegram bot workflows via the Bot API, focusing on command UX, update handling, and safe operations using plain HTTPS.

## Best fit

* You want a command-first bot that behaves professionally.
* You need a reliable update flow (webhook or polling).
* You prefer direct HTTP calls instead of libraries.

## Not a fit

* You require a full SDK or framework integration.
* You need complex media uploads and streaming in-process.

## Quick orientation

* Read `references/telegram-bot-api.md` for endpoints, update types, and request patterns.
* Read `references/telegram-commands-playbook.md` for command UX and messaging style.
* Read `references/telegram-update-routing.md` for update normalization and routing rules.
* Read `references/telegram-request-templates.md` for HTTP payload templates.
* Keep this SKILL.md short and use references for details.

## Required inputs

* Bot token and base API URL.
* Update strategy: webhook or long polling.
* Command list and conversation tone.
* Allowed update types and rate-limit posture.

## Expected output

* A clear command design, update flow plan, and operational checklist.

## Operational notes

* Prefer strict command routing: `/start`, `/help`, `/settings`, `/status`.
* Always validate incoming update payloads and chat context.
* Handle 429s with backoff and avoid message bursts.

## Security notes

* Never log tokens.
* Use webhooks with a secret token header when possible.

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

- OpenClaw skill for designing Telegram Bot API workflows and command-driven
  conversations using di
- 触发关键词: workflows, designing, telegram, openclaw, skill

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

### Q1: 如何开始使用Telegram？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Telegram有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用

---
## 边界条件与限制

### 输入限制
- **Bot Token**: 必须是有效的Telegram Bot API Token，否则技能无法正常工作。
- **命令列表**: 命令数量不应超过Telegram API的限制，通常为100个命令。
- **更新类型**: 支持的更新类型有限，如消息、回调查询等，不支持所有类型的更新。

### 性能边界
- **并发处理**: 单个技能实例可能无法处理大量并发更新，需要考虑扩展或使用多个技能实例。
- **响应时间**: 应对更新响应时间不应超过Telegram API的要求，通常为5秒。

### 兼容性约束
- **API版本**: 必须使用与技能版本兼容的Telegram Bot API版本。
- **操作系统**: 支持Windows、macOS和Linux操作系统，但不保证在其他操作系统上的兼容性。
- **网络环境**: 需要稳定的网络连接，否则可能导致技能无法正常工作。

### 其他限制
- **消息长度**: 单条消息的长度不应超过4096个字符。
- **文件大小**: 支持上传的文件大小有限制，通常为50MB。
- **频率限制**: 请求频率受到Telegram API的限制，如超过限制可能导致技能被限制或封禁。
---

