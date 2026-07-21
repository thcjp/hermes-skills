---
slug: ui
name: ui
version: "1.0.0"
displayName: UI
summary: Design clear, consistent, and visually polished user interfaces.
license: MIT
description: |-
  Design clear, consistent, and visually polished user interfaces。核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Creative
tools:
  - - read
- exec
---

# UI

## Visual Hierarchy

* One focal point per screen—eye knows where to go first
* Size, color, weight establish importance—primary action most prominent
* Group related elements—proximity implies relationship
* White space is not wasted space—breathing room aids scanning

## Typography

* Maximum 2-3 font families—more creates visual noise
* Clear size scale: title > heading > body > caption—distinct steps, not gradual
* Line height 1.4-1.6 for body text—too tight or loose hurts readability
* Line length 45-75 characters—prevents eye fatigue
* Left-align body text—centered only for short headings

## Color Usage

* Primary color for primary actions—one dominant brand color
* Semantic colors consistent: red=error, green=success, yellow=warning
* Don't rely on color alone—add icons, text, patterns for accessibility
* Neutral palette for most UI—color for emphasis, not everywhere
* Test color blindness scenarios—8% of men affected

## Spacing System

* Use consistent scale: 4px, 8px, 16px, 24px, 32px, 48px
* Apply same spacing for same relationships—all card padding equal
* More space around groups than within—visual grouping through proximity
* Generous padding on touch targets—44px minimum for mobile

## Alignment

* Grid system for consistency—8px or 4px base grid
* Align to invisible lines—elements share edges, not scattered
* Left edge strongest for LTR—anchor content predictably
* Optical alignment when needed—visual center differs from mathematical

## Component States

* Default, hover, active, focus, disabled—all states designed
* Focus state visible and clear—keyboard users need this
* Disabled looks disabled—reduced opacity, no pointer cursor
* Loading state replaces content—not just overlay
* Error state in context—red border, inline message

## Icons

* Consistent style throughout—don't mix outlined and filled
* Recognizable at small sizes—simple shapes work better
* Labels when meaning ambiguous—icon + text clearer than icon alone
* Touch target larger than visual icon—44px tap area, 24px icon

## Imagery

* Consistent aspect ratios—don't stretch or skew
* Fallback for failed loads—placeholder, not broken image
* Alt text for content images—decorative images alt=""
* Compress appropriately—quality vs file size balance

## Responsive Design

* Design for smallest screen first—enhance for larger
* Breakpoints based on content—not arbitrary device widths
* Touch targets larger on touch screens—hover states only on desktop
* Consider landscape orientation—especially for tablets

## Dark Mode

* Not just color inversion—redesign depth and emphasis
* Reduce contrast slightly—pure white on black strains eyes
* Shadows don't work same—use lighter surfaces for elevation
* Test all states—errors, success, charts, images
* Respect system preference—but allow override

## Motion and Animation

* Duration 150-300ms for transitions—fast but perceptible
* Ease-out for entering—starts fast, settles in
* Ease-in for exiting—accelerates out of view
* Consistent timing across similar interactions
* Purpose: guide attention, show relationships, provide feedback

## Design Tokens

* Define tokens for colors, spacing, typography—single source of truth
* Semantic naming: `color-error` not `color-red`
* Enables theming and dark mode—swap token values
* Scales with product—change once, update everywhere

## Common Mistakes

* Too many font sizes—stick to the scale
* Inconsistent spacing—creates unpolished feel
* Low contrast text—4.5:1 minimum for accessibility
* Buttons that don't look clickable—affordance matters
* Different styles for same component—cards should match cards

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

- Design clear, consistent, and visually polished user interfaces
- 触发关键词: polished, clear, design, visually, consistent

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

### Q1: 如何开始使用UI？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: UI有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
