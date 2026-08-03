---
slug: smart-model-switching
name: smart-model-switching
version: "1.0.0"
displayName: Smart Model Switchin
summary: "ai-assistant模型路由指南,助你在模型间选择"
  and shows no evidence...
license: MIT
description: |-
  This skill is a model-routing guide that helps choose between ai-assistant
  models and shows no evidence。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Smart Model Switching

**Three-tier ai-assistant routing: Haiku → Sonnet → Opus**

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

*Built for ai-assistant-only setups with Haiku, Sonnet, and Opus.*
*Inspired by save-money skill, extended with three-tier progression.*

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
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

- This skill is a model-routing guide that helps choose between ai-assistant
  models and shows no evidence
- 触发关键词: routing, model, guide, smart, switching, skill

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

### Q1: 如何开始使用Smart Model Switchin？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Smart Model Switchin有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 性能取决于底层模型能力
