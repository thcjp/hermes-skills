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
  a user-provided PPTX and show...

  核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: font, pdf, fix, narrow, powerpoint, pptx, repair, skill
tags:
- Knowledge
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
