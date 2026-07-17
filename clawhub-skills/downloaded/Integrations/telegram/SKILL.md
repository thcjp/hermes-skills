---
slug: telegram
name: telegram
version: "1.0.1"
displayName: Telegram
summary: OpenClaw skill for designing Telegram Bot API workflows and command-driven
  conversations using di...
license: MIT
description: |-
  OpenClaw skill for designing Telegram Bot API workflows and command-driven
  conversations using di...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: workflows, designing, telegram, openclaw, skill
tags:
- Integrations
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
