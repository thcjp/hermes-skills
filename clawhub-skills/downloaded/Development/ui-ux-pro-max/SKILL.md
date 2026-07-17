---
slug: ui-ux-pro-max
name: ui-ux-pro-max
version: "0.1.0"
displayName: UI/UX Pro Max
summary: This skill provides UI/UX guidance and an optional local design-system file
  generator, with no ev...
license: MIT
description: |-
  This skill provides UI/UX guidance and an optional local design-system
  file generator, with no ev...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: provides, optional, guidance, skill
tags:
- Development
tools:
- read
- exec
---

# UI/UX Pro Max

Follow these steps to deliver high-quality UI/UX output with minimal back-and-forth.

## 1) Triage

Ask only what you must to avoid wrong work:

* Target platform: web / iOS / Android / desktop
* Stack (if code changes): React/Next/Vue/Svelte, CSS/Tailwind, component library
* Goal and constraints: conversion, speed, brand vibe, accessibility level (WCAG AA?)
* What you have: screenshot, Figma, repo, URL, user journey

If the user says "全部都要" (design + UX + code + design system), treat it as four deliverables and ship in that order.

## 2) Produce Deliverables (pick what fits)

Always be concrete: name components, states, spacing, typography, and interactions.

* **UI concept + layout**: Provide a clear visual direction, grid, typography, color system, key screens/sections.
* **UX flow**: Map the user journey, critical paths, error/empty/loading states, edge cases.
* **Design system**: Tokens (color/typography/spacing/radius/shadow), component rules, accessibility notes.
* **Implementation plan**: Exact file-level edits, component breakdown, and acceptance criteria.

## 3) Use Bundled Assets

This skill bundles data you can cite for inspiration/standards.

* **Design intelligence data**: Read from `skills/ui-ux-pro-max/assets/data/` when you need palettes, patterns, or UI/UX heuristics.
* **Upstream reference**: If you need more phrasing/examples, consult `skills/ui-ux-pro-max/references/upstream-skill-content.md`.

## 4) Optional Script (Design System Generator)

If you need to quickly generate tokens and page-specific overrides, use the bundled script:

```bash
python3 skills/ui-ux-pro-max/scripts/design_system.py --help
```

Prefer running it when the user wants a structured token output (ASCII-friendly).

## Output Standards

* Default to ASCII-only tokens/variables unless the project already uses Unicode.
* Include: spacing scale, type scale, 2-3 font pair options, color tokens, component states.
* Always cover: empty/loading/error, keyboard navigation, focus states, contrast.

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
