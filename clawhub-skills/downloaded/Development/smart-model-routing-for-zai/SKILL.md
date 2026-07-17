---
slug: smart-model-routing-for-zai
name: smart-model-routing-for-zai
version: "1.0.0"
displayName: Smart Model Routing for Z.AI
summary: This skill is a disclosed z.ai model-routing guide and does not install code,
  request credentials...
license: MIT
description: |-
  This skill is a disclosed z.ai model-routing guide and does not install
  code, request credentials...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: routing, model, z.ai, zai, disclosed, smart, skill
tags: '[''Development'']'
tools: '[read, exec]'
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
