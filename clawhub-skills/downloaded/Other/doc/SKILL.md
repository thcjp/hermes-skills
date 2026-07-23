---
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
summary: "读写编辑DOCX,表格/图表/分页布局"
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

## 依赖说明

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

## 核心能力

- Use when the task involves reading, creating, or editing `
- docx` documents,
  especially when forma
- 触发关键词: task, creating, reading, involves, doc

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

### Q1: 如何开始使用Doc？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Doc有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
