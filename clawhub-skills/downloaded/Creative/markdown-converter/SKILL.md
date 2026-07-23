---
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
---

# Markdown Converter

Convert files to Markdown using `uvx markitdown` — no installation required.

## Basic Usage

```bash
uvx markitdown input.pdf

uvx markitdown input.pdf -o output.md
uvx markitdown input.docx > output.md

cat input.pdf | uvx markitdown
```

## Supported Formats

* **Documents**: PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx, .xls)
* **Web/Data**: HTML, CSV, JSON, XML
* **Media**: Images (EXIF + OCR), Audio (EXIF + transcription)
* **Other**: ZIP (iterates contents), YouTube URLs, EPub

## Options

```bash
-o OUTPUT      # Output file
-x EXTENSION   # Hint file extension (for stdin)
-m MIME_TYPE   # Hint MIME type
-c CHARSET     # Hint charset (e.g., UTF-8)
-d             # Use Azure Document Intelligence
-e ENDPOINT    # Document Intelligence endpoint
--use-plugins  # Enable 3rd-party plugins
--list-plugins # Show installed plugins
```

## 示例

```bash
uvx markitdown report.docx -o report.md

uvx markitdown data.xlsx > data.md

uvx markitdown slides.pptx -o slides.md

cat document | uvx markitdown -x .pdf > output.md

uvx markitdown scan.pdf -d -e "https://your-resource.cognitiveservices.azure.com/"
```

## Notes

* Output preserves document structure: headings, tables, lists, links
* First run caches dependencies; subsequent runs are faster
* For complex PDFs with poor extraction, use `-d` with Azure Document Intelligence

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

- This is a straightforward Markdown conversion helper, with privacy caveats
  if users choose Azure
- 触发关键词: conversion, converter, straightforward, markdown, helper

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

### Q1: 如何开始使用Markdown Converter？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Markdown Converter有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 依赖云服务，需要网络连接
