---
slug: doc
name: doc
version: "1.0.0"
displayName: Doc
summary: Use when the task involves reading, creating, or editing `.docx` documents,
  especially when forma...
license: MIT
description: |-
  Use when the task involves reading, creating, or editing `.docx` documents,
  especially when forma...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: task, creating, reading, involves, doc
tags:
- Other
tools:
- read
- exec
---

# Doc

## When to use

* Read or review DOCX content where layout matters (tables, diagrams, pagination).
* Create or edit DOCX files with professional formatting.
* Validate visual layout before delivery.

## Workflow

1. Prefer visual review (layout, tables, diagrams).
   * If `soffice` and `pdftoppm` are available, convert DOCX -> PDF -> PNGs.
   * Or use `scripts/render_docx.py` (requires `pdf2image` and Poppler).
   * If these tools are missing, install them or ask the user to review rendered pages locally.
2. Use `python-docx` for edits and structured creation (headings, styles, tables, lists).
3. After each meaningful change, re-render and inspect the pages.
4. If visual review is not possible, extract text with `python-docx` as a fallback and call out layout risk.
5. Keep intermediate outputs organized and clean up after final approval.

## Temp and output conventions

* Use `tmp/docs/` for intermediate files; delete when done.
* Write final artifacts under `output/doc/` when working in this repo.
* Keep filenames stable and descriptive.

## Dependencies (install if missing)

Prefer `uv` for dependency management.

Python packages:

```text
uv pip install python-docx pdf2image
```

If `uv` is unavailable:

```text
python3 -m pip install python-docx pdf2image
```

System tools (for rendering):

```text
brew install libreoffice poppler

sudo apt-get install -y libreoffice poppler-utils
```

If installation isn't possible in this environment, tell the user which dependency is missing and how to install it locally.

## Environment

No required environment variables.

## Rendering commands

DOCX -> PDF:

```text
soffice -env:UserInstallation=file:///tmp/lo_profile_$$ --headless --convert-to pdf --outdir $OUTDIR $INPUT_DOCX
```

PDF -> PNGs:

```text
pdftoppm -png $OUTDIR/$BASENAME.pdf $OUTDIR/$BASENAME
```

Bundled helper:

```text
python3 scripts/render_docx.py /path/to/file.docx --output_dir /tmp/docx_pages
```

## Quality expectations

* Deliver a client-ready document: consistent typography, spacing, margins, and clear hierarchy.
* Avoid formatting defects: clipped/overlapping text, broken tables, unreadable characters, or default-template styling.
* Charts, tables, and visuals must be legible in rendered pages with correct alignment.
* Use ASCII hyphens only. Avoid U+2011 (non-breaking hyphen) and other Unicode dashes.
* Citations and references must be human-readable; never leave tool tokens or placeholder strings.

## Final checks

* Re-render and inspect every page at 100% zoom before final delivery.
* Fix any spacing, alignment, or pagination issues and repeat the render loop.
* Confirm there are no leftovers (temp files, duplicate renders) unless the user asks to keep them.

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
