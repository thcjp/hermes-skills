---
slug: professional-communication
name: professional-communication
version: "0.1.0"
displayName: Professional Communication
summary: This is a professional writing helper made of markdown templates, with no
  code execution or hidde...
license: MIT
description: |-
  This is a professional writing helper made of markdown templates, with
  no code execution or hidde...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: professional, writing, communication, helper
tags:
- Communication
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
