---
slug: smart-model-switching
name: smart-model-switching
version: "1.0.0"
displayName: Smart Model Switching
summary: This skill is a model-routing guide that helps choose between Claude models
  and shows no evidence...
license: MIT
description: |-
  This skill is a model-routing guide that helps choose between Claude
  models and shows no evidence...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: routing, model, guide, smart, switching, skill
tags:
- Development
tools:
- read
- exec
---

# Smart Model Switching

**Three-tier Claude routing: Haiku → Sonnet → Opus**

Start with the cheapest model. Escalate only when needed. Save 50-90% on API costs.

## The Golden Rule

> If a human would need more than 30 seconds of focused thinking, escalate from Haiku to Sonnet.
> If the task involves architecture, complex tradeoffs, or deep reasoning, escalate to Opus.

## Cost Reality

| Model | Input | Output | Relative Cost |
| --- | --- | --- | --- |
| Haiku | $0.25/M | $1.25/M | 1x (baseline) |
| Sonnet | $3.00/M | $15.00/M | 12x |
| Opus | $15.00/M | $75.00/M | 60x |

**Bottom line:** Wrong model selection wastes money OR time. Haiku for simple, Sonnet for standard, Opus for complex.

---

## 💚 HAIKU — Default for Simple Tasks

**Stay on Haiku for:**

* Factual Q&A — "what is X", "who is Y", "when did Z"
* Quick lookups — definitions, unit conversions, short translations
* Status checks — calendar, file reads, session monitoring
* Heartbeats — periodic checks, HEARTBEAT_OK responses
* Memory & reminders — "remember this", "remind me to..."
* Casual conversation — greetings, small talk, acknowledgments
* Simple file ops — read, list, basic writes
* One-liner tasks — anything answerable in 1-2 sentences

### NEVER do these on Haiku

* ❌ Write code longer than 10 lines
* ❌ Create comparison tables
* ❌ Write more than 3 paragraphs
* ❌ Do multi-step analysis
* ❌ Write reports or proposals

---

## 💛 SONNET — Standard Work (The Workhorse)

**Escalate to Sonnet for:**

### Code & Technical

* Code generation — write functions, build features, scripts
* Code review — PR reviews, quality checks
* Debugging — standard bug investigation
* Documentation — README, comments, user guides

### Analysis & Planning

* Analysis & evaluation — compare options, assess trade-offs
* Planning — project plans, roadmaps, task breakdowns
* Research synthesis — combining multiple sources
* Multi-step reasoning — "first... then... finally"

### Writing & Content

* Long-form writing — reports, proposals, articles (>3 paragraphs)
* Creative writing — blog posts, descriptions, copy
* Summarization — long documents, transcripts
* Structured output — tables, outlines, formatted docs

---

## ❤️ OPUS — Complex Reasoning Only

**Escalate to Opus for:**

### Architecture & Design

* System architecture decisions
* Major codebase refactoring
* Design pattern selection with tradeoffs
* Database schema design

### Deep Analysis

* Complex debugging (multi-file, race conditions)
* Security reviews
* Performance optimization strategy
* Root cause analysis of subtle bugs

### Strategic & Creative

* Strategic planning — business decisions, roadmaps
* Nuanced judgment — ethics, ambiguity, competing values
* Deep research — comprehensive multi-source analysis

---

## 🔄 Implementation

### For Subagents

```javascript
// Routine monitoring
sessions_spawn(task="Check backup status", model="haiku")

// Standard code work
sessions_spawn(task="Build the REST API endpoint", model="sonnet")

// Architecture decisions
sessions_spawn(task="Design the database schema for multi-tenancy", model="opus")
```

### For Cron Jobs

```json
{
"payload": {
"kind": "agentTurn",
"model": "haiku"
}
}
```
Always use Haiku for cron unless the task genuinely needs reasoning.

---

## 📊 Quick Decision Tree

```
Is it a greeting, lookup, status check, or 1-2 sentence answer?
YES → HAIKU
NO ↓

Is it code, analysis, planning, writing, or multi-step?
YES → SONNET
NO ↓

Is it architecture, deep reasoning, or critical decision?
YES → OPUS
NO → Default to SONNET, escalate if struggling
```

---

## 📋 Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│ SMART MODEL SWITCHING │
│ Haiku → Sonnet → Opus │
├─────────────────────────────────────────────────────────────┤
│ 💚 HAIKU (cheapest) │
│ • Greetings, status checks, quick lookups │
│ • Factual Q&A, definitions, reminders │
│ • Simple file ops, 1-2 sentence answers │
├─────────────────────────────────────────────────────────────┤
│ 💛 SONNET (standard) │
│ • Code > 10 lines, debugging │
│ • Analysis, comparisons, planning │
│ • Reports, proposals, long writing │
├─────────────────────────────────────────────────────────────┤
│ ❤️ OPUS (complex) │
│ • Architecture decisions │
│ • Complex debugging, multi-file refactoring │
│ • Strategic planning, deep research │
├─────────────────────────────────────────────────────────────┤
│ 💡 RULE: If a human needs > 30 sec thinking → escalate │
│ 💰 COST: Haiku 1x → Sonnet 12x → Opus 60x │
└─────────────────────────────────────────────────────────────┘
```

---

*Built for Claude-only setups with Haiku, Sonnet, and Opus.*
*Inspired by save-money skill, extended with three-tier progression.*

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
