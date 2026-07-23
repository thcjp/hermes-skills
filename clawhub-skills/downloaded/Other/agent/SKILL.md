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
  assistants that feel authenti。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

- Define agent identity, personality, voice, and boundaries to create
  assistants that feel authenti
- 触发关键词: personality, voice, define, agent, identity

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

### Q1: 如何开始使用Agent？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Agent有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
