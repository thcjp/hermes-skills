---
slug: work
name: work
version: "1.0.0"
displayName: Work
summary: "职场导航:专业沟通、会议准备、职场动态与可见度管理,提升职场软技能"
  dynamics, and visib...
license: MIT
description: |-
  Navigate office work with professional communication, meeting prep,
  workplace dynamics, and visib。Use when 用户需要Work相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Work

## Core Focus

Day-to-day effectiveness in corporate/office environments. Not career strategy (that's `career`), not personal productivity (that's `productivity`).

---

## Situation Detection

| Signal | Context | Load |
| --- | --- | --- |
| First 90 days, onboarding, new hire | New role adaptation | `situations/new-hire.md` |
| Credit-taking, undermining, politics | Workplace dynamics | `situations/politics.md` |
| Email drafts, meeting prep, status updates | Communication tasks | `situations/comms.md` |
| Visibility, recognition, being overlooked | Perception management | `situations/visibility.md` |
| Vague assignments, unclear priorities | Task clarity | `situations/clarity.md` |

---

## Professional Communication

**Email drafts:** Match tone to recipient and urgency. Executive summary first, details below.

**Meeting prep:**

1. Review context (previous threads, decisions)
2. Define your contribution (questions, updates, blockers)
3. Prepare one-liner if asked "any updates?"

**Status updates formula:**

```text
DONE: [completed items with impact]
IN PROGRESS: [current focus + ETA]
BLOCKED: [what needs input/decision]
```

**Difficult conversations:** See `scripts.md` for templates.

---

## Workplace Dynamics

**When someone takes credit:** Document contributions in writing before meetings. Follow up with "as I mentioned in my email about X..."

**When undermined publicly:** Don't react in the moment. Address privately first: "I noticed X happened. Can we talk about how we work together?"

**Building alliances:** Visibility comes from being useful to the right people. Find where your work overlaps with influential stakeholders.

**Reading the room:** Watch who speaks, who gets interrupted, who makes final calls. That's the real org chart.

---

## First 90 Days

**Week 1-4:** Listen more than contribute. Map relationships. Understand what "good" looks like here.

**Week 5-8:** Start delivering small wins. Ask for feedback explicitly.

**Week 9-12:** Own something end-to-end. Have the "how am I doing?" conversation.

Key questions for manager:

* "What does success look like in 90 days?"
* "Who should I build relationships with?"
* "What should I definitely avoid?"

---

## Work Profile

*Build over time. Confirm before storing.*

### Environment

### Key Relationships

### Culture Signals

### Challenges

---

*Empty = nothing learned yet. Every work question reveals more context.*

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

- Navigate office work with professional communication, meeting prep,
  workplace dynamics, and visib
- 触发关键词: professional, office, navigate, work

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

### Q1: 如何开始使用Work？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Work有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
