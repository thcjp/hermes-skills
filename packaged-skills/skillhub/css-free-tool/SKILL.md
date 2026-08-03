---
name: css-free-tool
slug: css-free-tool
displayName: "CSS"
version: "1.0.1"
summary: "规避CSS常见陷阱:层叠上下文、布局怪癖,掌握现代CSS特性,提升页面渲染质量"
description: "规避CSS常见陷阱:层叠上下文、布局怪癖,掌握现代CSS特性,提升页面渲染质量。Avoid common CSS pitfalls — stacking context, layout quirks, and underused。触发关键词: avoid, css, stacking, common, pitfalls, context。"
license: "MIT"
tools:
  - read
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
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex /  CLI等)
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

- Avoid common CSS pitfalls — stacking context, layout quirks, and underused
  modern features
- 触发关键词: avoid, css, stacking, common, pitfalls, context

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

### Q1: 如何开始使用CSS？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: CSS有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **输入长度**: CSS技能接受的输入文本长度有限制，通常不超过1024个字符。超出此长度的输入可能会导致处理失败。
- **格式规范**: 输入必须符合Markdown格式，否则技能可能无法正确解析和执行。
- **内容相关性**: 输入内容必须与CSS相关，否则技能可能无法提供有用的反馈或处理结果。

### 性能边界
- **处理时间**: 对于复杂的CSS问题，技能的处理时间可能会增加，因为需要分析、生成和执行代码。
- **资源限制**: 技能运行在有限的资源上，因此对于资源密集型的操作（如处理大量数据）可能会有性能限制。

### 兼容性约束
- **浏览器支持**: 技能提供的信息和解决方案可能不适用于所有浏览器，尤其是针对较旧的浏览器版本。
- **CSS特性**: 技能可能无法处理某些尚未广泛支持的CSS特性或实验性功能。

### 代码执行限制
- **代码安全性**: 技能会限制执行的代码，以防止潜在的安全风险。
- **代码复杂性**: 技能可能无法处理过于复杂的CSS代码，尤其是那些涉及高级编程技巧的代码。

### 输出限制
- **输出格式**: 技能的输出将限制在Markdown格式内，可能无法直接生成其他格式（如HTML或CSS文件）。
- **输出长度**: 输出结果通常不超过1024个字符，以确保可读性和实用性。

---
