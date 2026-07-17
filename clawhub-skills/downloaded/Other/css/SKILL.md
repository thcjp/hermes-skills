---
slug: css
name: css
version: "1.0.1"
displayName: CSS
summary: Avoid common CSS pitfalls — stacking context, layout quirks, and underused
  modern features.
license: MIT
description: |-
  Avoid common CSS pitfalls — stacking context, layout quirks, and underused
  modern features.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: avoid, css, stacking, common, pitfalls, context
tags:
- Other
tools:
- read
- exec
---

# CSS

## When to Use

User needs CSS expertise — from layout challenges to production optimization. Agent handles stacking contexts, flexbox/grid patterns, responsive design, performance, and accessibility.

## Quick Reference

| Topic | File |
| --- | --- |
| Layout patterns | `layout.md` |
| Responsive techniques | `responsive.md` |
| Selectors and specificity | `selectors.md` |
| Performance optimization | `performance.md` |

## CSS Philosophy

* Layout should be robust—work with any content, not just demo content
* Use modern features—they have better browser support than you think
* Prefer intrinsic sizing—let content determine size when possible
* Test with extreme content—longest names, missing images, empty states

## Stacking Context Traps

* `z-index` only works with positioned elements—or flex/grid children
* `isolation: isolate` creates stacking context—contains z-index chaos without position
* `opacity < 1`, `transform`, `filter` create stacking context—unexpected z-index behavior
* New stacking context resets z-index hierarchy—child z-index:9999 won't escape parent

## Layout Traps

* Margin collapse only vertical, only block—flex/grid children don't collapse
* `overflow: hidden` on flex container can break—use `overflow: clip` if you don't need scroll

## Flexbox Traps

* `flex: 1` means `flex: 1 1 0%`—basis is 0, not auto
* `min-width: 0` on flex child for text truncation—default min-width is min-content
* `flex-basis` vs `width`: basis is before grow/shrink—width is after, basis preferred
* `gap` works in flex now—no more margin hacks for spacing

## Grid Traps

* `fr` units don't respect min-content alone—use `minmax(min-content, 1fr)`
* `auto-fit` vs `auto-fill`: fit collapses empty tracks, fill keeps them
* `grid-template-columns: 1fr 1fr` is not 50%—it's equal share of REMAINING space
* Implicit grid tracks can surprise you—items placed outside explicit grid still appear

## Responsive Philosophy

* Start mobile-first—`min-width` media queries, base styles for mobile
* Container queries: `@container (min-width: 400px)`—component-based responsive
* `container-type: inline-size` on parent required—for container queries to work
* Test on real devices—emulators miss touch targets and real performance

## Sizing Functions

* `clamp(min, preferred, max)` for fluid typography—`clamp(1rem, 2.5vw, 2rem)`
* `min()` and `max()`—`width: min(100%, 600px)` replaces media query
* `fit-content` sizes to content up to max—`width: fit-content` or `fit-content(300px)`

## Modern Selectors

* `:is()` for grouping—`:is(h1, h2, h3) + p` less repetition
* `:where()` same as `:is()` but zero specificity—easier to override
* `:has()` parent selector—`.card:has(img)` styles card containing image
* `:focus-visible` for keyboard focus only—no outline on mouse click

## Scroll Behavior

* `scroll-behavior: smooth` on html—native smooth scroll for anchors
* `overscroll-behavior: contain`—prevents scroll chaining to parent/body
* `scroll-snap-type` and `scroll-snap-align`—native carousel without JS
* `scrollbar-gutter: stable`—reserves scrollbar space, prevents layout shift

## Shorthand Traps

* `inset: 0` equals `top/right/bottom/left: 0`—less repetition
* `place-items` is `align-items` + `justify-items`—`place-items: center` centers both
* `margin-inline`, `margin-block` for logical properties—respects writing direction

## Performance Mindset

* `contain: layout` isolates repaints—use on independent components
* `content-visibility: auto` skips offscreen rendering—huge for long pages
* `will-change` sparingly—creates layers, uses memory
* Avoid layout thrash—batch reads and writes to DOM

## Accessibility Baseline

* `prefers-reduced-motion: reduce`—disable animations for vestibular disorders
* `prefers-color-scheme`—`@media (prefers-color-scheme: dark)` for dark mode
* `forced-colors: active`—adjust for Windows high contrast
* Focus indicators must be visible—don't rely on color alone

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
