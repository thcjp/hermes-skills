---
slug: fonts
name: fonts
version: "1.0.0"
displayName: Fonts
summary: Choose and implement web typography avoiding common rendering, pairing, and
  hierarchy mistakes.
license: MIT
description: |-
  Choose and implement web typography avoiding common rendering, pairing,
  and hierarchy mistakes。核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和...
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---


# Fonts

## Display vs Text Fonts

* Display fonts (Abril Fatface, Bebas Neue, Lobster) are for headings 24px+ only—using them for body text destroys readability
* If a font looks decorative or has extreme thick/thin contrast, it's display—not for paragraphs
* Text fonts (Inter, Roboto, Georgia) are designed for 12-18px—use these for body copy

## Pairing Traps

* Two fonts too similar look like a mistake—if you can't tell them apart instantly, use one font
* Contrast in category works: serif heading + sans-serif body, or different weights of same family
* Two decorative fonts clash—never pair Lobster with Pacifico
* Safe pairs: same superfamily (Roboto + Roboto Slab) or proven combos (Playfair Display + Source Sans Pro)

## Weight and Rendering

* Thin weights (100-300) render poorly on Windows—avoid for body text, use 400+ for cross-platform
* Light fonts on dark backgrounds look thinner—bump weight up one level for dark mode
* Faux bold (browser-generated) looks wrong—only use weights the font actually includes
* Check font has italic—faux italic (slanted roman) is noticeably worse than true italic

## Line Height and Length

* Body text needs 1.4-1.6 line-height—1.0 or 1.2 makes paragraphs unreadable walls
* Headings need tighter line-height (1.1-1.3)—large text with 1.5 line-height has awkward gaps
* Line length 45-75 characters max—wider than 75 chars causes readers to lose their place
* Set `max-width` on text containers in ch units: `max-width: 65ch`

## All Caps

* ALL CAPS needs increased letter-spacing—without it, letters collide and look cramped
* `text-transform: uppercase` + `letter-spacing: 0.05em` minimum
* Never use all caps for more than a few words—extended caps text is significantly harder to read
* Small caps (`font-variant: small-caps`) only if font supports it—faux small caps look amateurish

## Widows and Orphans

* Single word alone on last line of paragraph looks broken—adjust text or container width
* `text-wrap: balance` (CSS) distributes lines more evenly in headings
* `text-wrap: pretty` for body text—prevents orphans in browsers that support it
* Manual fix: non-breaking space (`&nbsp;`) between last two words

## Loading and Performance

* `font-display: swap` prevents invisible text—without it, text is blank until font loads
* Subset fonts to characters you need—Latin-only saves 60%+ over full Unicode
* WOFF2 is the only format you need—universal support, best compression
* Preload critical fonts: `<link rel="preload" href="font.woff2" as="font" crossorigin>`

## System Font Stack

```css
font-family: system-ui, -apple-system, BlinkMacSystemFont,
  'Segoe UI', Roboto, sans-serif;
```

* Zero load time, native look per platform—use for UI-heavy apps
* `system-ui` is now widely supported—simpler than listing all fallbacks
* Always end with generic fallback (`sans-serif`, `serif`, `monospace`)

## Hierarchy Mistakes

* Using too many font sizes—stick to a type scale (1.25 or 1.333 ratio), not random sizes
* Headings not distinct enough from body—skip at least one scale step between h1 and body
* Overusing bold—if everything is emphasized, nothing is emphasized
* Color as only differentiator—size and weight should establish hierarchy before color

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

- Choose and implement web typography avoiding common rendering, pairing,
  and hierarchy mistakes
- 触发关键词: typography, fonts, common, implement, choose, avoiding

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

### Q1: 如何开始使用Fonts？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Fonts有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
