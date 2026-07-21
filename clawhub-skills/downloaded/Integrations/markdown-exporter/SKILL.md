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
  CSV, JSON, JSONL, XML files。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
# Markdown Exporter
---
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

> 详细内容已移至 `references/detail.md` - ### md_to_csv - Convert Markdown tables to CSV

> 详细内容已移至 `references/detail.md` - ### md_to_docx - Convert Markdown to DOCX
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

> 详细内容已移至 `references/detail.md` - ### md_to_json - Convert Markdown Tables to JSON

> 详细内容已移至 `references/detail.md` - ### md_to_latex - Convert Markdown Tables to LaTeX
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

To help you test the various tools, below are common Markdown input examples that represent the content of input files:

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

````markdown
title: Markdown Exporter
author: Bowen Liang
## Welcome Slide
Welcome to our Markdown Exporter!

::: notes
Remember to greet the audience warmly.
:::

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

## Code Block
Here's a Python code block:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```

## 示例
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

- All scripts only support file paths as input
- For scripts that generate multiple files (e.g., multiple tables, multiple code blocks), the output filename will be automatically numbered
- Use the `--strip-wrapper` option to remove code block wrappers (```) from the input Markdown

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
Markdown Exporter is available as a PyPI package, which provides a seamless command-line interface for all its functionality.

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

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Markdown Exporter？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Markdown Exporter有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
