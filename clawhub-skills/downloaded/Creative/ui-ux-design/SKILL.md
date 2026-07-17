---
slug: ui-ux-design
name: ui-ux-design
version: "1.0.0"
displayName: UI/UX Design Guide
summary: Expert guidance on mobile-first UI/UX design, color systems, typography,
  accessibility (WCAG 2.2)...
license: MIT
description: |-
  Expert guidance on mobile-first UI/UX design, color systems, typography,
  accessibility (WCAG 2.2)...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: guidance, mobile, guide, design, expert
tags:
- Creative
tools:
- read
- exec
---

# UI/UX Design Guide

**Name:** ui-ux-design
**Description:** Modern UI/UX design principles, patterns, and best practices for web and mobile applications. Use when building user interfaces, designing layouts, choosing color palettes, implementing responsive design, ensuring accessibility (WCAG), or creating beautiful modern applications. Includes 2026 design trends, Tailwind CSS patterns, Shadcn/ui integration, micro-interactions, and mobile-first responsive design.

---

## When to Use This Skill

Activate this skill when:

* Building or designing web/mobile interfaces
* Choosing colors, typography, or layout systems
* Implementing responsive design (mobile-first)
* Ensuring accessibility compliance (WCAG 2.2)
* Setting up Shadcn/ui + Tailwind CSS projects
* Creating micro-interactions and animations
* Reviewing UI/UX decisions before coding

---

## Core Design Principles

### 1. Mobile-First Always

* Start with 320px width (smallest phone)
* Breakpoints: 576px (phone), 768px (tablet), 992px (laptop), 1200px (desktop)
* Single-column default, expand only when space allows

### 2. Visual Hierarchy

Guide user attention using:

* **Size:** Larger = more important
* **Color:** Bright/contrasting = attention
* **Whitespace:** More space = emphasis
* **Proximity:** Related items grouped together
* **Contrast:** Dark on light or light on dark (4.5:1 minimum for text)

### 3. Whitespace is Your Weapon

* Space elements in multiples of 8px (8, 16, 24, 32, 48, 64)
* Breathing room between sections: 48-64px minimum
* Padding inside cards: 24-32px

---

## Quick Reference

### Color System

Build a primary color scale (50-900):

* **Primary:** Brand color (CTAs, links, active states)
* **Neutrals:** Grays 50-900 (text, backgrounds, borders)
* **Semantic:** Success (green), Error (red), Warning (yellow/orange)

Tools: Huevy.app, Coolors.co, Adobe Color

### Typography Scale (8px baseline)

```text
text-xs:   12px / 16px line-height
text-sm:   14px / 20px
text-base: 16px / 24px (body default)
text-lg:   18px / 28px
text-xl:   20px / 28px
text-2xl:  24px / 32px
text-3xl:  30px / 36px (section headers)
text-4xl:  36px / 40px
text-5xl:  48px / 1 (hero titles)
```

**Font pairing:** 2 fonts max (sans-serif for UI, optional serif for headings)

### Layout Patterns

* **CSS Grid:** 2D layouts (page structure)
* **Flexbox:** 1D layouts (component internals)
* **Auto-fit grid:** `repeat(auto-fit, minmax(280px, 1fr))` (no media queries!)

### Micro-Interactions

* **Hover:** Scale 1.05x (buttons feel clickable)
* **Click:** Scale 0.95x (tactile feedback)
* **Duration:** 0.2-0.3s max (keep it subtle)
* **Animate only:** `transform` and `opacity` (GPU accelerated)

### Accessibility (WCAG 2.2)

* **Text contrast:** 4.5:1 minimum (normal text), 3:1 (large text)
* **UI components:** 3:1 contrast minimum
* **Keyboard navigation:** Tab order logical, focus states visible (3:1 contrast)
* **ARIA labels:** Always provide for buttons, images, interactive elements

---

## Shadcn/ui + Tailwind Stack

### Setup (Next.js)

```bash
npx create-next-app@latest project-name --typescript --tailwind --app
cd project-name
npx shadcn@latest init
```

Choose: Style (Default), Base color (Blue or custom), CSS variables (Yes)

### Adding Components

```bash
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add dialog
npx shadcn@latest add calendar
```

Components appear in `components/ui/` — you own the code, customize freely.

### Tailwind Best Practices

* Use design tokens (not arbitrary values): `p-4` not `p-[17px]`
* Responsive utilities: `w-full md:w-1/2 lg:w-1/3`
* Dark mode: `dark:bg-gray-900 dark:text-white`

---

## Pre-Build Checklist

Before writing code, confirm:

* Color palette defined (primary + neutrals + semantic colors)
* Typography scale chosen (6-8 sizes)
* Component library picked (Shadcn + Tailwind)
* Mobile breakpoints planned (576px, 768px, 992px)
* Accessibility contrast ratios checked (4.5:1 text, 3:1 UI)
* Micro-interaction list (hover, click, success states)
* Grid layout sketched (mobile → desktop progression)

---

## Inspiration Sources

**Study these products:**

* Linear (linear.app) — Best keyboard-first UI, subtle animations
* Stripe Dashboard — Clean data visualization, perfect spacing
* Vercel — Minimalist, fast, modern gradients
* Notion — Intuitive drag-and-drop, clear hierarchy

**Tools:**

* Figma (mockups before coding)
* WebAIM Contrast Checker (accessibility)
* Coolors/Huevy (color palettes)

---

## The 5 Laws of Beautiful UI

1. **Contrast creates hierarchy** (big vs small, dark vs light)
2. **Whitespace creates calm** (never fear empty space)
3. **Consistency builds trust** (same patterns repeated)
4. **Feedback confirms action** (animations, success messages)
5. **Accessibility includes everyone** (contrast, keyboard, screen readers)

---

## Full Reference

For comprehensive deep-dives (component patterns, animation examples, responsive grid techniques), see `UI_UX_MASTER_GUIDE.md` in this skill directory.

---

**Last Updated:** 2026-02-05

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
