---
slug: pandoc-convert-openclaw
name: pandoc-convert-openclaw
version: "0.1.0"
displayName: Pandoc Convert
summary: "用pandoc CLI在40+格式间转文档,Markdown/Word/PDF/HTML(社区下载版)"
  ↔ Word ↔ PDF ↔ HTML ↔ La...
license: MIT
description: |-
  Convert documents between 40+ formats using pandoc CLI。Handles Markdown
  ↔ Word ↔ PDF ↔ HTML ↔ La。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Knowledge
tools:
  - - read
- exec
---

# Pandoc Convert

**Universal document converter combining unified Python tools with modular bash utilities.**

The **pandoc-convert** skill provides intelligent workflows for converting documents between 40+ formats using pandoc. This integrated version combines:

* **Unified Python converter** (convert.py) - Single powerful tool for most conversions
* **Modular bash utilities** (batch_convert.sh, validate.sh) - Specialized workflows
* **Comprehensive templates** - Both LaTeX academic and modern CSS styles
* **Professional documentation** - Complete guides, troubleshooting, and references

## 核心能力

* **40+ Format Support**: Markdown, Word, PDF, HTML, LaTeX, EPUB, RST, AsciiDoc, Org-mode, and more
* **Dual Toolset**: Python for smart conversions + bash for validation/batch processing
* **Professional Templates**: 12 templates covering academic, business, and web use cases
* **Comprehensive Documentation**: Format guides, troubleshooting, templates, and quick reference
* **Smart Defaults**: Optimized settings for each conversion path
* **Metadata Preservation**: Keep titles, authors, dates across formats
* **Error Recovery**: Validation and helpful error messages

## 🔧 Prerequisites

### Required

* **pandoc** (v2.19+ recommended)
* **Python 3.8+** (for convert.py helper)

### Optional (for extended formats)

* **LaTeX** (TeX Live, MiKTeX) - Required for PDF output
* **wkhtmltopdf** - Alternative HTML to PDF converter
* **librsvg** - SVG support
* **epubcheck** - EPUB validation

See `INSTALL.md` for detailed installation instructions per platform.

## 使用流程

### Using Python Helper (Recommended)

```bash
python scripts/convert.py input.md output.pdf

python scripts/convert.py report.md report.pdf --template business --toc

python scripts/convert.py --batch *.md --format pdf --output-dir ./pdfs
```

### Using Bash Utilities

```bash
./scripts/batch_convert.sh input/*.md pdf output/

./scripts/validate.sh output/document.pdf
./scripts/validate.sh output/book.epub
```

### Direct Pandoc

```bash
pandoc input.md -o output.pdf

pandoc input.md -o output.docx

pandoc input.docx -o output.md --extract-media=./media
```

## 🎯 Common Workflows

See `references/conversion-guides.md` for detailed step-by-step guides:

* Markdown → Professional PDF (business reports, academic papers)
* Word → Markdown (version control friendly)
* Markdown → EPUB (eBooks with validation)
* Multi-file → Single PDF (book compilation)
* Markdown → HTML5 (standalone with CSS)

## 🎨 Templates

### LaTeX Templates (Academic/Professional)

* `academic-paper.tex` - Manuscript style
* `business-letter.tex` - Professional correspondence
* `technical-report.tex` - Technical documentation
* `resume.tex` - CV/resume formatting
* `professional.tex` - General-purpose professional
* `report-template.tex` - Report structure

### CSS Templates (Web/Modern)

* `github.css` - GitHub markdown style
* `blog-style.css` - Clean blog format
* `epub-style.css` - eBook styling
* `presentation.html` - HTML presentations
* `ebook.css` - Enhanced eBook layout

### Reference Documents

* `reference-styles.docx` - Word style reference

All templates in `templates/` directory.

## 🔧 Tool Reference

### convert.py (Python)

Unified conversion tool with smart defaults:

```bash
python scripts/convert.py [OPTIONS] INPUT OUTPUT

Options:
  --format FORMAT       Force output format
  --template TEMPLATE   Use named template
  --toc                 Include table of contents
  --number-sections     Number headings
  --title TITLE         Document title
  --author AUTHOR       Document author
  --batch               Batch mode
  --validate            Validate output
  --verbose             Detailed output
```

### batch_convert.sh (Bash)

Batch processing with progress tracking:

```bash
./scripts/batch_convert.sh INPUT_DIR FORMAT OUTPUT_DIR [OPTIONS]

./scripts/batch_convert.sh ./docs/ pdf ./output/ --toc --number-sections
```

### validate.sh (Bash)

Post-conversion validation:

```bash
./scripts/validate.sh FILE

```

## 📊 Format Support

### Input Formats

**Markdown**: `markdown`, `gfm`, `markdown_mmd`
**Word**: `docx`, `odt`, `rtf`
**Web**: `html`, `html5`
**LaTeX**: `latex`, `tex`
**Plain Text**: `txt`, `rst`, `textile`, `asciidoc`
**Academic**: `jats`, `docbook`
**Presentation**: `pptx`
**eBooks**: `epub`
**Other**: `json`, `csv`, `org`, `mediawiki`, `man`

### Output Formats

All input formats plus: **PDF**, **EPUB**, **RevealJS**, **Beamer**

Complete format matrix: `references/format-matrix.md`

## 🗂️ Directory Structure

```text
pandoc-convert-integrated/
├── SKILL.md              # This file
├── INSTALL.md            # Detailed installation guide
├── README.md             # Quick start guide
├── scripts/
│   ├── convert.py        # Unified Python converter
│   ├── batch_convert.sh  # Bash batch processor
│   └── validate.sh       # Validation utility
├── templates/
│   ├── *.tex             # LaTeX templates (6)
│   ├── *.css             # CSS templates (3)
│   ├── *.html            # HTML templates (1)
│   └── *.docx            # Word reference (1)
└── references/
    ├── format-guide.md         # Format details
    ├── format-matrix.md        # Compatibility matrix
    ├── conversion-guides.md    # Step-by-step guides
    ├── format-support.md       # Supported features
    ├── quick-reference.md      # Cheat sheet
    ├── templates.md            # Template documentation
    └── troubleshooting.md      # Problem solving
```

## 错误处理

### Common Issues

* **"pandoc: command not found"** → Install pandoc (see INSTALL.md)
* **"pdflatex not found"** → Install LaTeX distribution
* **Unicode broken in PDF** → Use `--pdf-engine=xelatex`
* **Images missing** → Check paths and use `--resource-path`
* **EPUB validation fails** → Run epubcheck for details

See `references/troubleshooting.md` for comprehensive solutions.

## 📖 References

* `INSTALL.md` - Platform-specific installation
* `references/format-guide.md` - Format capabilities and limitations
* `references/conversion-guides.md` - Step-by-step workflows
* `references/quick-reference.md` - One-page cheat sheet
* `references/templates.md` - Template usage and customization
* `references/troubleshooting.md` - Extended problem solving

## 🎯 Best Practices

1. **Use YAML frontmatter** for metadata (title, author, date)
2. **Validate outputs** before sharing (especially EPUB/PDF)
3. **Version control source** (Markdown), not outputs
4. **Test templates first** before batch processing
5. **Back up before batch operations**

## 🚀 Performance

* Use `batch_convert.sh` for parallel processing of multiple files
* Cache templates in `~/.pandoc/templates/`
* Use incremental builds (only reconvert changed files)
* For very large docs (>10MB), increase memory limits

## 📜 License

This skill is part of Skill平台. Pandoc itself is GPL-licensed.

---

**Quick Start**: `python scripts/convert.py input.md output.pdf`
**Batch Convert**: `./scripts/batch_convert.sh *.md pdf ./output/`
**Validate**: `./scripts/validate.sh output.pdf`
**Help**: See `README.md` and `references/` directory

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
### Using Python Helper (Recommended)

```bash
python scripts/convert.py input.md output.pdf

python scripts/convert.py report.md report.pdf --template business --toc

python scripts/convert.py --batch *.md --format pdf --output-dir ./pdfs
```

### Using Bash Utilities

```bash
./scripts/batch_convert.sh input/*.md pdf output/

./scripts/validate.sh output/document.pdf
./scripts/validate.sh output/book.epub
```

### Direct Pandoc

```bash
pandoc input.md -o output.pdf

pandoc input.md -o output.
```

## 常见问题

### Q1: 如何开始使用Pandoc Convert？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Pandoc Convert有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
