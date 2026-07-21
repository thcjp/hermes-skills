---
slug: smart-model-routing-for-zai
name: smart-model-routing-for-zai
version: "1.0.0"
displayName: Smart Model Routing 
summary: This skill is a disclosed z.ai model-routing guide and does not install code,
  request credentials...
license: MIT
description: |-
  This skill is a disclosed z。ai model-routing guide and does not install
  code, request credentials。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags: '[''Development'']'
tools:
  - read
  - exec
---

# Smart Model Routing for Z.AI

**Three-tier z.ai (GLM) routing: Flash → Standard → Plus / 32B**

Start with the cheapest model. Escalate only when needed. Designed to minimize API cost without sacrificing correctness.

---

## The Golden Rule

> If a human would need more than 30 seconds of focused thinking, escalate from Flash to Standard.
> If the task involves architecture, complex tradeoffs, or deep reasoning, escalate to Plus / 32B.

---

## Model Reality (Relative)

| Tier | Example Models | Purpose |
| --- | --- | --- |
| Flash | GLM-4.5-Flash, GLM-4.7-Flash | Fastest & cheapest |
| Standard | GLM-4.6, GLM-4.7 | Strong reasoning & code |
| Plus / 32B | GLM-4-Plus, GLM-4-32B-128K | Heavy reasoning & architecture |

**Bottom line:** Wrong model selection wastes money OR time. Flash for simple, Standard for normal work, Plus/32B for complex decisions.

---

## 💚 FLASH — Default for Simple Tasks

**Stay on Flash for:**

* Factual Q&A — “what is X”, “who is Y”, “when did Z”
* Quick lookups — definitions, unit conversions, short translations
* Status checks — monitoring, file reads, session state
* Heartbeats — periodic checks, OK responses
* Memory & reminders
* Casual conversation — greetings, acknowledgments
* Simple file ops — read, list, basic writes
* One-liner tasks — anything answerable in 1–2 sentences
* Cron jobs (always Flash by default)

### NEVER do these on Flash

* ❌ Write code longer than 10 lines
* ❌ Create comparison tables
* ❌ Write more than 3 paragraphs
* ❌ Do multi-step analysis
* ❌ Write reports or proposals

---

## 💛 STANDARD — Core Workhorse

**Escalate to Standard for:**

### Code & Technical

* Code generation — functions, scripts, features
* Debugging — normal bug investigation
* Code review — PRs, refactors
* Documentation — README, comments, guides

### Analysis & Planning

* Comparisons and evaluations
* Planning — roadmaps, task breakdowns
* Research synthesis
* Multi-step reasoning

### Writing & Content

* Long-form writing (>3 paragraphs)
* Summaries of long documents
* Structured output — tables, outlines

**Most real user conversations belong here.**

---

## ❤️ PLUS / 32B — Complex Reasoning Only

**Escalate to Plus / 32B for:**

### Architecture & Design

* System and service architecture
* Database schema design
* Distributed or multi-tenant systems
* Major refactors across multiple files

### Deep Analysis

* Complex debugging (race conditions, subtle bugs)
* Security reviews
* Performance optimization strategy
* Root cause analysis

### Strategic & Judgment-Based Work

* Strategic planning
* Nuanced judgment and ambiguity
* Deep or multi-source research
* Critical production decisions

---

## 🔄 Implementation

### For Subagents

```javascript
// Routine monitoring
sessions_spawn(task="Check backup status", model="GLM-4.5-Flash")

// Standard code work
sessions_spawn(task="Build the REST API endpoint", model="GLM-4.7")

// Architecture decisions
sessions_spawn(task="Design the database schema for multi-tenancy", model="GLM-4-Plus")
For Cron Jobs
json
Copy code
{
  "payload": {
    "kind": "agentTurn",
    "model": "GLM-4.5-Flash"
  }
}
Always use Flash for cron unless the task genuinely needs reasoning.

📊 Quick Decision Tree
pgsql
Copy code
Is it a greeting, lookup, status check, or 1–2 sentence answer?
  YES → FLASH
  NO ↓

Is it code, analysis, planning, writing, or multi-step?
  YES → STANDARD
  NO ↓

Is it architecture, deep reasoning, or a critical decision?
  YES → PLUS / 32B
  NO → Default to STANDARD, escalate if struggling
📋 Quick Reference Card
less
Copy code
┌─────────────────────────────────────────────────────────────┐
│                  SMART MODEL SWITCHING                      │
│              Flash → Standard → Plus / 32B                  │
├─────────────────────────────────────────────────────────────┤
│  💚 FLASH (cheapest)                                        │
│  • Greetings, status checks, quick lookups                  │
│  • Factual Q&A, reminders                                   │
│  • Simple file ops, 1–2 sentence answers                    │
├─────────────────────────────────────────────────────────────┤
│  💛 STANDARD (workhorse)                                    │
│  • Code > 10 lines, debugging                               │
│  • Analysis, comparisons, planning                          │
│  • Reports, long writing                                    │
├─────────────────────────────────────────────────────────────┤
│  ❤️ PLUS / 32B (complex)                                    │
│  • Architecture decisions                                   │
│  • Complex debugging, multi-file refactoring                │
│  • Strategic planning, deep research                        │
├─────────────────────────────────────────────────────────────┤
│  💡 RULE: >30 sec human thinking → escalate                 │
│  💰 START CHEAP → SCALE ONLY WHEN NEEDED                    │
└─────────────────────────────────────────────────────────────┘
Built for z.ai (GLM) setups.
```

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

- This skill is a disclosed z
- ai model-routing guide and does not install
  code, request credentials
- 触发关键词: routing, model, z
- ai, zai, disclosed, smart, skill

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

### Q1: 如何开始使用Smart Model Routing？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Smart Model Routing有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 性能取决于底层模型能力
