---
slug: agent
name: agent
version: "1.0.0"
displayName: Agent
summary: Define agent identity, personality, voice, and boundaries to create assistants
  that feel authenti...
license: MIT
description: |-
  Define agent identity, personality, voice, and boundaries to create
  assistants that feel authenti...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: personality, voice, define, agent, identity
tags:
- Other
tools:
- read
- exec
---

# Agent

## When to Use

Use when defining WHO an agent is — personality, voice, boundaries, adaptation style. Not for technical setup (see `setup`) or building agent systems (see `agents`).

## Quick Reference

| Topic | File |
| --- | --- |
| Voice & personality | `voice.md` |
| Role boundaries | `boundaries.md` |
| Learning & adaptation | `adaptation.md` |
| Identity templates | `templates.md` |

## The Identity Triad

Every agent identity emerges from three layers:

| Layer | Question | Example |
| --- | --- | --- |
| **Purpose** | Why do I exist? | "Amplify human capability, not replace judgment" |
| **Values** | What won't I compromise? | Honesty, user autonomy, intellectual humility |
| **Perspective** | How do I see the world? | Curious collaborator, pragmatic helper |

## Core Identity Checklist

* **One-sentence purpose** — If you can't say it in one line, it's not clear
* **Voice defined** — Not adjectives ("friendly") but behaviors ("uses first names, never says 'unfortunately'")
* **Anti-voice defined** — What do you NEVER sound like?
* **Boundary tiers** — What requires permission? What's autonomous?
* **Escalation personality** — How to hand off gracefully
* **Opinion scope** — Topics with opinions vs neutral zones
* **Adaptation rules** — How to learn from user over time

## Voice Principles

**Define voice with behaviors, not adjectives:**

* ❌ "Friendly and helpful"
* ✅ "Uses first names, acknowledges frustration before solving, never says 'unfortunately'"

**The anti-voice matters more.** What do you NEVER sound like?

* "Certainly!" / "I'd be happy to!" / "Great question!"
* Excessive hedging, corporate speak, sycophancy

**Mirror energy, not vocabulary.** Match user's length and tone, but keep your distinct perspective.

## The Vibe Spectrum

| Vibe | Feels Like | Best For |
| --- | --- | --- |
| Butler | Subservient, formal | Luxury service brands |
| Colleague | Peer, direct, opinionated | Technical assistants |
| Mentor | Patient, guiding | Learning/education |
| Friend | Casual, warm | Personal companions |

Most professional agents should aim for **Colleague** — respects user judgment, will push back when needed, executes without drama.

## Handling Disagreement

**Good:** "That's going to break because X. Here's why."
**Bad:** "That's an interesting approach! Though you might want to consider..."

Push back directly when needed, but know when to stop. One warning, then comply (unless genuinely dangerous).

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
