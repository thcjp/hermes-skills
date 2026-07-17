---
slug: work
name: work
version: "1.0.0"
displayName: Work
summary: Navigate office work with professional communication, meeting prep, workplace
  dynamics, and visib...
license: MIT
description: |-
  Navigate office work with professional communication, meeting prep,
  workplace dynamics, and visib...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: professional, office, navigate, work
tags:
- Productivity
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
