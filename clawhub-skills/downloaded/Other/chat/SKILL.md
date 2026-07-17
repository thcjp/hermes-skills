---
slug: chat
name: chat
version: "1.1.0"
displayName: Chat
summary: Learns communication preferences from explicit feedback. Adapts tone, format,
  and style.
license: MIT
description: |-
  Learns communication preferences from explicit feedback. Adapts tone,
  format, and style.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: chat, learns, preferences, explicit, communication
tags:
- Other
tools:
- read
- exec
---

# Chat

## Data Storage

```text
~/chat/
├── memory.md       # Confirmed preferences (≤50 lines)
├── experiments.md  # Testing patterns (not yet confirmed)
└── rejected.md     # User said no, don't re-propose
```

Create on first use: `mkdir -p ~/chat`

## Scope

This skill:

* ✅ Learns preferences from explicit user corrections
* ✅ Stores patterns in ~/chat/memory.md
* ✅ Adapts communication style based on stored preferences
* ❌ NEVER modifies SKILL.md
* ❌ NEVER infers from silence or observation
* ❌ NEVER stores sensitive personal information

## Quick Reference

| Topic | File |
| --- | --- |
| Preference dimensions | `dimensions.md` |
| Confirmation criteria | `criteria.md` |

## Core Rules

### 1. Learn from Explicit Feedback Only

* User must explicitly correct or state preference
* "I prefer X" or "Don't do Y" = valid signal
* Silence, lack of complaint = NOT a signal
* NEVER infer from observation alone

### 2. Three-Strike Confirmation

| Stage | Location | Action |
| --- | --- | --- |
| Testing | experiments.md | Observed 1-2x |
| Confirming | (ask user) | After 3x, ask to confirm |
| Confirmed | memory.md | User approved |
| Rejected | rejected.md | User declined |

### 3. Compact Storage Format

One line per preference in memory.md:

```text
- Concise responses, no fluff
- Uses 🚀 for launches, ✅ for done
- Prefers bullets over paragraphs
- Technical jargon OK
- Hates "Great question!" openers
```

### 4. Conflict Resolution

* Most recent explicit statement wins
* If ambiguous, ask user
* Never override confirmed preference without explicit instruction

### 5. Transparency

* Cite source when applying preference: "Using bullets (from ~/chat/memory.md)"
* On request, show full memory.md contents
* "Forget X" removes from all files

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
