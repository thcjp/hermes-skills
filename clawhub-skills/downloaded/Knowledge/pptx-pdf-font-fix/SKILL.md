---
slug: pptx-pdf-font-fix
name: pptx-pdf-font-fix
version: "1.0.0"
displayName: PPTX PDF Font Fix
summary: This skill is a narrow PowerPoint repair utility that locally edits a user-provided
  PPTX and show...
license: MIT
description: |-
  This skill is a narrow PowerPoint repair utility that locally edits
  a user-provided PPTX and show。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
- exec
---

# PPTX PDF Font Fix

## Problem

PowerPoint's "Export to PDF" can fail to embed downloaded/custom fonts, substituting built-in defaults, even when:

* Fonts are properly installed and embeddable
* "Embed fonts in the file" is checked in PowerPoint options

## Workaround

Applying a tiny transparency (1%) to text with 0% transparency forces PowerPoint to correctly embed fonts in PDF output. This is visually imperceptible but changes how PowerPoint processes the font during export.

## Usage

```bash
python3 scripts/fix_font_transparency.py input.pptx [output.pptx] [--transparency 1]
```

### Options

* `output` -- Output PPTX path (default: `input_fixed.pptx`)
* `--transparency, -t` -- Transparency % to apply (default: 1)

## Behavior

* Only patches text runs that are fully opaque (0% transparency)
* Leaves text that already has any transparency untouched
* Safe to run multiple times
* Only modifies slide XML (`ppt/slides/slideN.xml`), not layouts/masters

## Workflow

1. Receive PPTX file from user
2. Run the fix script: `python3 scripts/fix_font_transparency.py input.pptx`
3. Return the patched PPTX to the user
4. User opens patched file in PowerPoint and exports to PDF -- fonts now embed correctly

## Note

PDF export must be done from PowerPoint desktop. Server-side converters (LibreOffice, Graph API) do not reproduce the same font embedding behavior.

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

- This skill is a narrow PowerPoint repair utility that locally edits
  a user-provided PPTX and show
- 触发关键词: font, pdf, fix, narrow, powerpoint, pptx, repair, skill

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

### Q1: 如何开始使用PPTX PDF Font Fix？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: PPTX PDF Font Fix有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 本地运行，不支持多设备同步
