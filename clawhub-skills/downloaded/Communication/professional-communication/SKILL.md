---
slug: professional-communication
name: professional-communication
version: "0.1.0"
displayName: Professional Communi
summary: "专业写作助手,纯markdown模板无代码执行"
  code execution or hidde...
license: MIT
description: |-
  This is a professional writing helper made of markdown templates, with
  no code execution or hidde。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Professional Communication

Write clear, effective professional messages that get read and acted upon.

## Installation

### Skill平台 / Moltbot / Clawbot

```bash
npx SkillHub@latest install professional-communication
```

## WHAT This Skill Does

Routes you to ready-to-use templates and translation guides for professional technical communication.

## WHEN To Use

* Drafting emails (status updates, requests, escalations, introductions)
* Writing Slack/Teams messages
* Preparing meeting agendas or summaries
* Translating technical concepts for non-technical audiences
* Any written communication to teammates, managers, or stakeholders

## Core Principle

**Key message first. Scannable format. Clear action requested.**

Every professional message answers: What do you need to know? Why does it matter? What action (if any) is needed?

## Quick Reference: Message Structure

```text
Subject: [Topic]: [Specific Purpose]

[1-2 sentences: key point or request upfront]

**Context:** (if needed)
- Bullet points, not paragraphs

**Action Needed:**
- Specific request with timeline
```

## Route to References

| Task | Load This Reference |
| --- | --- |
| Writing any email | **MANDATORY**: Load [`references/email-templates.md`](/api/v1/skills/professional-communication/file?path=references%2Femail-templates.md&ownerHandle=wpank) |
| Explaining technical concepts to non-technical people | **MANDATORY**: Load [`references/jargon-simplification.md`](/api/v1/skills/professional-communication/file?path=references%2Fjargon-simplification.md&ownerHandle=wpank) |
| Running or preparing for meetings | **MANDATORY**: Load [`references/meeting-structures.md`](/api/v1/skills/professional-communication/file?path=references%2Fmeeting-structures.md&ownerHandle=wpank) |
| Async/remote team communication | Load [`references/remote-async-communication.md`](/api/v1/skills/professional-communication/file?path=references%2Fremote-async-communication.md&ownerHandle=wpank) |

## The Four Rules

1. **Subject lines tell the story** - "Project X: Decision Needed by Friday" beats "Question"
2. **Bullets over paragraphs** - Nobody reads walls of text
3. **Specific asks** - "Please review by Thursday" beats "Let me know"
4. **Match the channel** - Chat for quick/informal, Email for records/formal

## NEVER

* Send a message without a clear purpose in the first sentence
* Use "Just checking in" without context (include what you're checking on)
* Write paragraphs when bullets would work
* Bury the ask at the bottom
* Use jargon with non-technical audiences
* Send walls of text in chat (use threads)
* Reply-all unnecessarily
* Use passive voice when active is clearer ("We decided" not "It was decided")

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

- This is a professional writing helper made of markdown templates, with
  no code execution or hidde
- 触发关键词: professional, writing, communication, helper

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

### Q1: 如何开始使用Professional Communi？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Professional Communi有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
