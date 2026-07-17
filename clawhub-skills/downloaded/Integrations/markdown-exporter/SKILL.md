---
slug: markdown-exporter
name: markdown-exporter
version: "3.6.10"
displayName: Markdown Exporter
summary: Convert Markdown text to DOCX, PPTX, XLSX, PDF, PNG, HTML, IPYNB, MD, CSV,
  JSON, JSONL, XML files...
license: Apache-2.0
description: |-
  Convert Markdown text to DOCX, PPTX, XLSX, PDF, PNG, HTML, IPYNB, MD,
  CSV, JSON, JSONL, XML files...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: text, convert, docx, exporter, markdown, pptx
tags:
- Integrations
tools:
- read
- exec
---

# Markdown Exporter

Markdown Exporter is an Agent Skill that transforms your Markdown text into a wide variety of professional format files.

This [SKILL.md](https://github.com/bowenliang123/markdown-exporter/blob/main/SKILL.md) for Agent Skills, the cli tool and [Python package `markdown-exporter`](https://pypi.org/project/md-exporter/) are maintained in the GitHub repository [bowenliang123/markdown-exporter](https://github.com/bowenliang123/markdown-exporter) by [bowenliang123](https://github.com/bowenliang123).

### Tools and Supported Formats

| Tool | Input (File path of Markdown text or styles) | Output (File path of exported file) |
|------|-------|--------|
| `md_to_docx` | 📝 Markdown text | 📄 Word document (.docx) |
| `md_to_html` | 📝 Markdown text | 🌐 HTML file (.html) |
| `md_to_html_text` | 📝 Markdown text | 🌐 HTML text string |
| `md_to_pdf` | 📝 Markdown text | 📑 PDF file (.pdf) |
| `md_to_md` | 📝 Markdown text | 📝 Markdown file (.md) |
| `md_to_ipynb` | 📝 Markdown text | 📓 Jupyter Notebook (.ipynb) |
| `md_to_pptx` | 📝 Markdown slides in [Pandoc style](https://pandoc.org/MANUAL.html#slide-shows) | 🎯 PowerPoint (.pptx) |
| `md_to_xlsx` | 📋 [Markdown tables](https://www.markdownguide.org/extended-syntax/#tables) | 📊 Excel spreadsheet (.xlsx) |
| `md_to_csv` | 📋 [Markdown tables](https://www.markdownguide.org/extended-syntax/#tables) | 📋 CSV file (.csv) |
| `md_to_json` | 📋 [Markdown tables](https://www.markdownguide.org/extended-syntax/#tables) | 📦 JSON/JSONL file (.json) |
| `md_to_xml` | 📋 [Markdown tables](https://www.markdownguide.org/extended-syntax/#tables) | 🏷️ XML file (.xml) |
| `md_to_latex` | 📋 [Markdown tables](https://www.markdownguide.org/extended-syntax/#tables) | 📝 LaTeX file (.tex) |
| `md_to_codeblock` | 💻 [Code blocks in Markdown](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks) | 📁 Code files by language (.py, .js, .sh, etc.) |


## 📦 Usage

### Overview
Markdown Exporter is available as a PyPI package, which provides a seamless command-line interface for all its functionality.

### Installation

```bash
pip install md-exporter

uv tool install md-exporter

npx * 安装此Skill请参考SkillHub平台指南
```

Check `markdown-exporter` command and usages:
```
markdown-exporter -h

markdown-exporter <subcommand> -h
```

### Basic Usage
Use the `markdown-exporter` command to access all the tools:

```bash
markdown-exporter <subcommand> <args> [options]
```

### Important Notes
- All commands only support file paths as input
- The package handles all dependency management automatically
- You can run the command from anywhere in your system, no need to navigate to the project directory


## 🔧 Scripts

### md_to_csv - Convert Markdown tables to CSV

Converts Markdown tables to CSV format file.

**Usage:**
```bash
markdown-exporter md_to_csv <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path containing tables
- `output` - Output CSV file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_csv /path/input.md /path/output.csv
   ```
   This converts all tables in the input Markdown file to CSV format.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_csv /path/input.md /path/output.csv --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_pdf - Convert Markdown to PDF

Converts Markdown text to PDF format with support for Chinese, Japanese, and other languages.

**Usage:**
```bash
markdown-exporter md_to_pdf <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output PDF file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_pdf /path/input.md /path/output.pdf
   ```
   This converts the entire Markdown file to a PDF document.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_pdf /path/input.md /path/output.pdf --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_docx - Convert Markdown to DOCX

Converts Markdown text to DOCX format file.

**Usage:**
```bash
markdown-exporter md_to_docx <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output DOCX file path

**Options:**
- `--template` - Path to DOCX template file (optional)
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_docx /path/input.md /path/output.docx
   ```
   This converts the entire Markdown file to a DOCX document.

2. **With custom template**:
   ```bash
   markdown-exporter md_to_docx /path/input.md /path/output.docx --template /path/template.docx
   ```
   This uses a custom DOCX template for styling.

3. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_docx /path/input.md /path/output.docx --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_xlsx - Convert Markdown tables to XLSX

Converts Markdown tables to XLSX format with multiple sheets support.

**Usage:**
```bash
markdown-exporter md_to_xlsx <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path containing tables
- `output` - Output XLSX file path

**Options:**
- `--force-text` - Convert cell values to text type (default: True)
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_xlsx /path/input.md /path/output.xlsx
   ```
   This converts all tables in the input Markdown file to an XLSX workbook, with each table on a separate sheet.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_xlsx /path/input.md /path/output.xlsx --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

3. **With force-text disabled**:
   ```bash
   markdown-exporter md_to_xlsx /path/input.md /path/output.xlsx --force-text False
   ```
   This allows Excel to automatically determine cell types.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_pptx - Convert Markdown to PPTX

Converts Markdown text to PPTX format file.

**Usage:**
```bash
markdown-exporter md_to_pptx <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output PPTX file path

**Options:**
- `--template` - Path to PPTX template file (optional)

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_pptx /path/input.md /path/output.pptx
   ```
   This converts the Markdown file to a PowerPoint presentation.

2. **With custom template**:
   ```bash
   markdown-exporter md_to_pptx /path/input.md /path/output.pptx --template /path/template.pptx
   ```
   This uses a custom PowerPoint template for styling.

**Sample Markdown Input:**
Use the "Slides (for PPTX)" example from the [Sample Markdown Inputs - Slides (for PPTX)](#slides-for-pptx) section below.

---

### md_to_codeblock - Extract Codeblocks to Files

Extracts code blocks from Markdown and saves them as individual files.

**Usage:**
```bash
markdown-exporter md_to_codeblock <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path containing code blocks
- `output` - Output directory path or ZIP file path

**Options:**
- `--compress` - Compress all code blocks into a ZIP file

**Examples:**

1. **Extract to directory**:
   ```bash
   markdown-exporter md_to_codeblock /path/input.md /path/output_dir
   ```
   This extracts all code blocks to individual files in the specified directory.

2. **Extract to ZIP file**:
   ```bash
   markdown-exporter md_to_codeblock /path/input.md /path/output.zip --compress
   ```
   This extracts all code blocks and compresses them into a ZIP file.

**Sample Markdown Input:**
Use the "Code Blocks" example from the [Sample Markdown Inputs - Code Blocks](#code-blocks) section below.

---

### md_to_json - Convert Markdown Tables to JSON

Converts Markdown tables to JSON or JSONL format file.

**Usage:**
```bash
markdown-exporter md_to_json <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path containing tables
- `output` - Output JSON file path

**Options:**
- `--style` - JSON output style: `jsonl` (default) or `json_array`
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion (JSONL format)**:
   ```bash
   markdown-exporter md_to_json /path/input.md /path/output.json
   ```
   This converts tables to JSON Lines format (one JSON object per line).

2. **Convert to JSON array**:
   ```bash
   markdown-exporter md_to_json /path/input.md /path/output.json --style json_array
   ```
   This converts tables to a single JSON array of objects.

3. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_json /path/input.md /path/output.json --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_xml - Convert Markdown to XML

Converts Markdown text to XML format file.

**Usage:**
```bash
markdown-exporter md_to_xml <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output XML file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_xml /path/input.md /path/output.xml
   ```
   This converts the entire Markdown file to an XML document.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_xml /path/input.md /path/output.xml --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_latex - Convert Markdown Tables to LaTeX

Converts Markdown tables to LaTeX format file.

**Usage:**
```bash
markdown-exporter md_to_latex <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path containing tables
- `output` - Output LaTeX file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_latex /path/input.md /path/output.tex
   ```
   This converts all tables in the input Markdown file to LaTeX format.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_latex /path/input.md /path/output.tex --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_html - Convert Markdown to HTML

Converts Markdown text to HTML format file.

**Usage:**
```bash
markdown-exporter md_to_html <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output HTML file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_html /path/input.md /path/output.html
   ```
   This converts the entire Markdown file to an HTML document.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_html /path/input.md /path/output.html --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_html_text - Convert Markdown to HTML Text

Converts Markdown text to HTML and outputs to stdout.

**Usage:**
```bash
markdown-exporter md_to_html_text <input>
```

**Arguments:**
- `input` - Input Markdown file path

**Example:**
```bash
markdown-exporter md_to_html_text /path/input.md
```

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_md - Convert Markdown to MD File

Saves Markdown text to a .md file.

**Usage:**
```bash
markdown-exporter md_to_md <input> <output>
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output MD file path

**Example:**
```bash
markdown-exporter md_to_md /path/input.md /path/output.md
```

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

---

### md_to_ipynb - Convert Markdown to IPYNB

Converts Markdown text to Jupyter Notebook (.ipynb) format file.

**Usage:**
```bash
markdown-exporter md_to_ipynb <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output IPYNB file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_ipynb /path/input.md /path/output.ipynb
   ```
   This converts the Markdown file to a Jupyter Notebook format.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_ipynb /path/input.md /path/output.ipynb --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Code Blocks" example from the [Sample Markdown Inputs - Code Blocks](#code-blocks) section below.


### Sample Markdown Inputs

To help you test the various tools, below are common Markdown input examples that represent the content of input files:

#### Basic Text and Tables
```markdown

This is a test markdown file for testing various export tools.

## Table Test

| Name | Description | Price |
|------|-------------|-------|
| Item 1 | First item | $10 |
| Item 2 | Second item | $20 |
| Item 3 | Third item | $30 |

## Text Test

This is a paragraph with **bold** and *italic* text.

- List item 1
- List item 2
- List item 3

> This is a blockquote.
```

#### Code Blocks
````markdown

## Code Block Test

```python
print("Hello, World!")
def add(a, b):
    return a + b

result = add(5, 3)
print(f"Result: {result}")
```

```bash
echo "Hello from Bash"
ls -la
```

```javascript
// JavaScript example
console.log("Hello from JavaScript");
function multiply(a, b) {
    return a * b;
}
`

#### Slides (for PPTX)
````markdown
---
title: Markdown Exporter
author: Bowen Liang
---

## Welcome Slide

Welcome to our Markdown Exporter!

::: notes
Remember to greet the audience warmly.
:::

---

## Title and Content

- This is a basic slide with bullet points
- It uses the "Title and Content" layout
- Perfect for simple content presentation

## Two Column Layout

::::: columns
::: column
Left column content:
- Point 1
- Point 2
:::
::: column
Right column content:
- Point A
- Point B
:::
:::::

## Comparison Layout

::::: columns
::: column
Text followed by an image:

![Test Image](https://example.com/image.jpg)
:::
::: column
- This triggers the "Comparison" layout
- Useful for side-by-side comparisons
:::
:::::

## Content with Caption

Here's some explanatory text about the image below.

![Test Image](https://example.com/image.jpg "fig:Test Image")

---

## Code Block

Here's a Python code block:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```

## Table Example

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | More     |
| Row 2    | Info     | Stuff    |

## Incremental List

::: incremental
- This point appears first
- Then this one
- And finally this one
:::

## {background-image="https://example.com/image.jpg"}

::: notes
This is a slide with a background image and speaker notes only.
The "Blank" layout will be used.
:::


## Thank You

Thank you for viewing this kitchen sink presentation!

::: notes
Remember to thank the audience and invite questions.
:::
````


## 📝 Notes

- All scripts only support file paths as input
- For scripts that generate multiple files (e.g., multiple tables, multiple code blocks), the output filename will be automatically numbered
- Use the `--strip-wrapper` option to remove code block wrappers (```) from the input Markdown

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
