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
  file generator, with no ev。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Development
tools:
  - - read
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

- This skill provides UI/UX guidance and an optional local design-system
  file generator, with no ev
- 触发关键词: provides, optional, guidance, skill

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

### Q1: 如何开始使用UI/UX Pro Max？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: UI/UX Pro Max有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 本地运行，不支持多设备同步
