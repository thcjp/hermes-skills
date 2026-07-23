---
slug: chat
name: chat
version: "1.1.0"
displayName: Chat
summary: "从用户反馈中学习通信偏好,自适应调整语气、格式与风格,提升沟通效率"
  and style.
license: MIT
description: |-
  Learns communication preferences from explicit feedback。Adapts tone,
  format, and style。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

- Learns communication preferences from explicit feedback
- Adapts tone,
  format, and style
- 触发关键词: chat, learns, preferences, explicit, communication

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

### Q1: 如何开始使用Chat？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Chat有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
