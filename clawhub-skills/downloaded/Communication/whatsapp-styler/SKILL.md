---
slug: whatsapp-styler
name: whatsapp-styler
version: "1.0.0"
displayName: WhatsApp Styler
summary: "确保发往WhatsApp的消息遵循平台特定格式语法"
  formatting syntax. I...
license: MIT
description: |-
  Skill to ensure all messages sent to WhatsApp follow the platform's
  specific formatting syntax。I。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

- Skill to ensure all messages sent to WhatsApp follow the platform's
  specific formatting syntax
- 触发关键词: ensure, whatsapp, sent, styler, messages, skill'

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

### Q1: 如何开始使用WhatsApp Styler？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: WhatsApp Styler有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **消息长度**: WhatsApp Styler技能能够处理的消息长度受限于WhatsApp平台的限制，通常为2,000字符。
- **格式复杂性**: 对于过于复杂的Markdown格式，技能可能无法正确解析或应用格式规则。

### 性能边界
- **并发处理**: WhatsApp Styler技能在处理大量并发请求时，性能可能会受到影响，建议在高峰时段适当限制并发量。
- **响应时间**: 在网络条件良好且系统负载较低的情况下，技能的响应时间通常在几毫秒到几十毫秒之间。

### 兼容性约束
- **平台兼容性**: WhatsApp Styler技能目前仅支持与支持SKILL.md格式的AI Agent集成，如Claude Code、Cursor、Codex、Gemini CLI等。
- **操作系统兼容性**: 技能的运行环境要求操作系统为Windows、macOS或Linux，且需满足依赖说明中的最低版本要求。

### 其他限制
- **外部API限制**: 如果技能中使用了外部API，将受到API提供商的限制，如调用频率限制、可用性保证等。
- **隐私和安全**: 技能处理的消息内容应遵守相关隐私和安全法规，不得包含敏感信息。
---

