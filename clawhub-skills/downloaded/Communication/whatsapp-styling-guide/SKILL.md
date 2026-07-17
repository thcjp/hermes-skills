---
slug: whatsapp-styling-guide
name: whatsapp-styling-guide
version: "1.0.0"
displayName: WhatsApp Styler
summary: Skill to ensure all messages sent to WhatsApp follow the platform's specific
  formatting syntax. I...
license: MIT
description: |-
  Skill to ensure all messages sent to WhatsApp follow the platform's
  specific formatting syntax. I...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: ensure, whatsapp, sent, styling, guide, styler, messages, skill'
tags:
- Communication
tools:
- read
- exec
---

# WhatsApp Styler

This skill defines the strict formatting rules for WhatsApp to ensure the user sees clean, styled text without raw markdown symbols.

## Core Syntax Rules

1. *Bold*: Use single asterisks around text: `*texto*`. NEVER use double asterisks `**`.
2. *Italic*: Use single underscores around text: `_texto_`.
3. ~~Strikethrough~~: Use tildes around text: `~texto~`.
4. `Monospace`: Use triple backticks: `texto` (good for code or technical IDs).
5. *Bullet Lists*: Use a single asterisk followed by a space: `* Item`.
6. *Numbered Lists*: Use standard numbers: `1. Item`.
7. *Quotes*: Use the angle bracket: `> texto`.

## Prohibited Patterns (Do NOT use)

* No headers (`#`, `##`, `###`). Use *BOLD CAPS* instead.
* No markdown tables. Use bullet lists for structured data.
* No horizontal rules (`---`). Use a line of underscores if needed `__________`.
* No nested bold/italic symbols if it risks showing raw characters.

## Goal

The goal is a "Human-to-Human" look. Technical but clean.

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
