---
slug: powerpoint-pptx
name: powerpoint-pptx
version: "1.0.1"
displayName: Powerpoint / PPTX
summary: Create, inspect, and edit Microsoft PowerPoint presentations and PPTX decks
  with reliable layouts...
license: MIT-0
description: |-
  Create, inspect, and edit Microsoft PowerPoint presentations and PPTX
  decks with reliable layouts...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: edit, create, microsoft, inspect, powerpoint, pptx
tags:
- Productivity
tools:
- read
- exec
---

# Powerpoint / PPTX

## When to Use

Use when the main artifact is a Microsoft PowerPoint presentation or `.pptx` deck, especially when layouts, templates, placeholders, notes, comments, charts, extraction, editing, or final visual quality matter.

## Core Rules

### 1. Choose the workflow before touching the deck

* Reading text, editing an existing deck, rebuilding from a template, and creating from scratch are different jobs with different failure modes.
* For text extraction or inspection, read the deck before editing it.
* Text extraction plus thumbnail-style visual inspection is safer than editing from shape assumptions alone.
* For template-driven work, inventory the deck before replacing content.
* For deep edits, remember a `.pptx` file is OOXML with separate parts for slides, layouts, masters, media, notes, and comments.
* If a template exists, template fidelity beats generic slide-design instincts.
* Reusing or duplicating a good existing slide is often safer than rebuilding it and hoping the theme still matches.

### 2. Inventory the deck before replacing content

* Count the reusable layouts, real placeholders, notes, comments, media, and recurring typography or color patterns first.
* Placeholder indexes and layout indexes are not portable assumptions.
* Inspect the actual slide or template before targeting title, body, chart, or image shapes.
* Speaker notes, comments, and linked assets can live outside the visible slide surface.
* A missing or wrong placeholder target can silently land content in the wrong box or wrong layer.
* Master and layout settings can override local slide edits, so the visible problem is not always on the slide you are editing.

### 3. Match content to the actual placeholders

* Count the actual content pieces before choosing a layout.
* Pick layouts based on the real number of ideas, columns, images, or charts the slide needs.
* Do not force two ideas into a three-column slide or cram dense text under a chart.
* Category counts and data series lengths must match or charts will break in ugly ways.
* Explicit sizing beats wishful thinking: text boxes, images, and charts need real space, not "it should fit".
* Do not choose a layout with more placeholders than the content can meaningfully fill.
* Quote layouts are for real quotes, and image-led layouts are for slides that actually have images.
* For chart-, table-, or image-heavy slides, full-slide or two-column layouts are usually safer than stacking dense text above the visual.

### 4. Preserve the deck's visual language

* Theme, master, and layout files usually decide fonts, colors, and hierarchy more than any one slide does.
* Start from the deck's actual theme, fonts, spacing, and aspect ratio instead of improvising a new style.
* Reuse the deck's own alignment and spacing system instead of inventing a second visual language.
* Use common fonts for portability and strong contrast for readability.
* Preserve the template's visual logic first; originality matters less than not breaking the deck's existing language.
* Combining slides from multiple sources requires normalizing themes, masters, and alignment afterward.

### 5. Run content QA and visual QA separately

* Text overflow, bad alignment, clipped shapes, weak contrast, and placeholder leftovers are normal first-pass failures.
* Run both content QA and visual QA; missing text and broken layout are different failure classes.
* Render or inspect the actual deck output before delivery when layout matters.
* Search for leftover template junk, sample labels, and placeholder text before calling the deck finished.
* Check notes, comments, labels, legends, and chart/table semantics separately from the visual pass.
* A deck can pass text extraction and still fail on overlap, clipping, wrong theme inheritance, or broken notes.
* Thumbnail grids and rendered slides usually reveal layout bugs faster than code or text inspection.
* Assume the first render is wrong and do at least one fix-and-verify cycle before calling the deck finished.
* Re-check affected slides after each fix because one spacing change often creates another issue.

### 6. Keep decks portable and review-safe

* Template masters can override direct edits in surprising ways.
* Complex effects may degrade across PowerPoint, LibreOffice, and conversion pipelines, so keep important content robust without them.
* Image sizing, font substitution, and placeholder mismatch are common reasons a deck looks good in code and bad on screen.
* Notes, comments, linked media, and merged decks can stay broken even when the visible slide looks fine.

## Common Traps

* Placeholder text and sample charts often survive template reuse if not explicitly replaced.
* Directly editing one slide can fail if the real issue lives in the master or layout.
* Charts, icons, and text boxes need enough space; near-collisions are usually visible only after rendering.
* Layout indexes vary by template, so built-in assumptions from one deck often break in another.
* A missing placeholder or wrong shape target can silently put content in the wrong place.
* Counting the text ideas after choosing the layout usually leads to empty placeholders, weak hierarchy, or leftover template junk.
* Font substitution can move line breaks and wreck careful spacing.
* Speaker notes, comments, and linked media can stay broken even when the visible slide looks fine.
* A deck can pass text inspection and still fail visually because of overlap, contrast, or edge clipping.
* Editing from one slide alone can miss the real source of truth in the theme, master, or layout definitions.
* Choosing a quote, comparison, or multi-column layout without matching content usually makes the deck look templated rather than intentional.
* Combining or duplicating slides without checking masters and themes can create subtle inconsistency slide by slide.
* Aspect-ratio mismatches like `16:9` versus `4:3` can shift every placement decision even when each slide looks locally reasonable.

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `documents` — Document workflows that often feed presentation content.
* `design` — Visual direction and layout decisions.
* `brief` — Concise business messaging for slide narratives.

## Feedback

* If useful: `
* Stay updated: `

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
