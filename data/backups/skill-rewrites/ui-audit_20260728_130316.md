---
slug: ui-audit
name: ui-audit
version: "1.0.1"
displayName: UI Audit
summary: "AI驱动的自动化UI审计,基于UX原则评估界面,检查视觉层级与交互一致性,提升产品质量"
  for visual hie...
license: MIT
description: |-
  AI skill for automated UI audits。Evaluate interfaces against proven
  UX principles for visual hie。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# UI Audit

Evaluate interfaces against proven UX principles. Based on [Making UX Decisions](https://uxdecisions.com) by Tommy Geoco.

## When to Use This Skill

* Making UI/UX design decisions under time pressure
* Evaluating design trade-offs with business context
* Choosing appropriate UI patterns for specific problems
* Reviewing designs for completeness and quality
* Structuring design thinking for new interfaces

## Core Philosophy

**Speed ≠ Recklessness.** Designing quickly is not automatically reckless. Recklessly designing quickly is reckless. The difference is intentionality.

## The 3 Pillars of Warp-Speed Decisioning

1. **Scaffolding** — Rules you use to automate recurring decisions
2. **Decisioning** — Process you use for making new decisions
3. **Crafting** — Checklists you use for executing decisions

## Quick Reference Structure

### Foundational Frameworks

* `references/00-core-framework.md` — 3 pillars, decisioning workflow, macro bets
* `references/01-anchors.md` — 7 foundational mindsets for design resilience
* `references/02-information-scaffold.md` — Psychology, economics, accessibility, defaults

### Checklists (Execution)

* `references/10-checklist-new-interfaces.md` — 6-step process for designing new interfaces
* `references/11-checklist-fidelity.md` — Component states, interactions, scalability, feedback
* `references/12-checklist-visual-style.md` — Spacing, color, elevation, typography, motion
* `references/13-checklist-innovation.md` — 5 levels of originality spectrum

### Patterns (Reusable Solutions)

* `references/20-patterns-chunking.md` — Cards, tabs, accordions, pagination, carousels
* `references/21-patterns-progressive-disclosure.md` — Tooltips, popovers, drawers, modals
* `references/22-patterns-cognitive-load.md` — Steppers, wizards, minimalist nav, simplified forms
* `references/23-patterns-visual-hierarchy.md` — Typography, color, whitespace, size, proximity
* `references/24-patterns-social-proof.md` — Testimonials, UGC, badges, social integration
* `references/25-patterns-feedback.md` — Progress bars, notifications, validation, contextual help
* `references/26-patterns-error-handling.md` — Form validation, undo/redo, dialogs, autosave
* `references/27-patterns-accessibility.md` — Keyboard nav, ARIA, alt text, contrast, zoom
* `references/28-patterns-personalization.md` — Dashboards, adaptive content, preferences, l10n
* `references/29-patterns-onboarding.md` — Tours, contextual tips, tutorials, checklists
* `references/30-patterns-information.md` — Breadcrumbs, sitemaps, tagging, faceted search
* `references/31-patterns-navigation.md` — Priority nav, off-canvas, sticky, bottom nav

## Usage Instructions

### For Design Decisions

1. Read `00-core-framework.md` for the decisioning workflow
2. Identify if this is a recurring decision (use scaffold) or new decision (use process)
3. Apply the 3-step weighing: institutional knowledge → user familiarity → research

### For New Interfaces

1. Follow the 6-step checklist in `10-checklist-new-interfaces.md`
2. Reference relevant pattern files for specific UI components
3. Use fidelity and visual style checklists to enhance quality

### For Pattern Selection

1. Identify the core problem (chunking, disclosure, cognitive load, etc.)
2. Load the relevant pattern reference
3. Evaluate benefits, use cases, psychological principles, and implementation guidelines

## Decision Workflow Summary

When facing a UI decision:

```text
1. WEIGH INFORMATION
   ├─ What does institutional knowledge say? (existing patterns, brand, tech constraints)
   ├─ What are users familiar with? (conventions, competitor patterns)
   └─ What does research say? (user testing, analytics, studies)

2. NARROW OPTIONS
   ├─ Eliminate what conflicts with constraints
   ├─ Prioritize what aligns with macro bets
   └─ Choose based on JTBD support

3. EXECUTE
   └─ Apply relevant checklist + patterns
```

## Macro Bet Categories

Companies win through one or more of:

| Bet | Description | Design Implication |
| --- | --- | --- |
| **Velocity** | Features to market faster | Reuse patterns, find metaphors in other markets |
| **Efficiency** | Manage waste better | Design systems, reduce WIP |
| **Accuracy** | Be right more often | Stronger research, instrumentation |
| **Innovation** | Discover untapped potential | Novel patterns, cross-domain inspiration |

Always align micro design bets with company macro bets.

## Key Principle: Good Design Decisions Are Relative

A design decision is "good" when it:

* Supports the product's jobs-to-be-done
* Aligns with company macro bets
* Respects constraints (time, tech, team)
* Balances user familiarity with differentiation needs

There is no universally correct UI solution—only contextually appropriate ones.

---

## Generating Audit Reports

When asked to audit a design, generate a comprehensive report. Always include these sections:

### Required Sections (always include)

1. **Visual Hierarchy** — Headings, CTAs, grouping, reading flow, type scale, color hierarchy, whitespace
2. **Visual Style** — Spacing consistency, color usage, elevation/depth, typography, motion/animation
3. **Accessibility** — Keyboard navigation, focus states, contrast ratios, screen reader support, touch targets

### Contextual Sections (include when relevant)

4. **Navigation** — For multi-page apps: wayfinding, breadcrumbs, menu structure, information architecture
5. **Usability** — For interactive flows: discoverability, feedback, error handling, cognitive load
6. **Onboarding** — For new user experiences: first-run, tutorials, progressive disclosure
7. **Social Proof** — For landing/marketing pages: testimonials, trust signals, social integration
8. **Forms** — For data entry: labels, validation, error messages, field types

### Audit Output Format

```json
{
  "title": "Design Name — Screen/Flow",
  "project": "Project Name",
  "date": "YYYY-MM-DD",
  "figma_url": "optional",
  "screenshot_url": "optional - URL to screenshot",

  "macro_bets": [
    { "category": "velocity|efficiency|accuracy|innovation", "description": "...", "alignment": "strong|moderate|weak" }
  ],

  "jtbd": [
    { "user": "User Type", "situation": "context without 'When'", "motivation": "goal without 'I want to'", "outcome": "benefit without 'so I can'" }
  ],

  "visual_hierarchy": {
    "title": "Visual Hierarchy",
    "checks": [
      { "label": "Check name", "status": "pass|warn|fail|na", "notes": "Details" }
    ]
  },
  "visual_style": { ... },
  "accessibility": { ... },

  "priority_fixes": [
    { "rank": 1, "title": "Fix title", "description": "What and why", "framework_reference": "XX-filename.md → Section Name" }
  ],

  "notes": "Optional overall observations"
}
```

### Checks Per Section (aim for 6-10 each)

**Visual Hierarchy**: heading distinction, primary action clarity, grouping/proximity, reading flow, type scale, color hierarchy, whitespace usage, visual weight balance

**Visual Style**: spacing consistency, color palette adherence, elevation/shadows, typography system, border/radius consistency, icon style, motion principles

**Accessibility**: keyboard operability, visible focus, color contrast (4.5:1), touch targets (44px), alt text, semantic markup, reduced motion support

**Navigation**: clear current location, predictable menu behavior, breadcrumb presence, search accessibility, mobile navigation pattern

**Usability**: feature discoverability, feedback on actions, error prevention, recovery options, cognitive load management, loading states

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

- AI skill for automated UI audits
- Evaluate interfaces against proven
  UX principles for visual hie
- 触发关键词: audits, evaluate, interfaces, automated, audit, skill

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

### Q1: 如何开始使用UI Audit？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: UI Audit有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
