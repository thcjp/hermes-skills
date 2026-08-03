---

slug: pandoc-converter
name: pandoc-converter
version: "0.1.0"
displayName: "转换器"
summary: "用pandoc CLI在40+格式间转文档,Markdown/Word/PDF/HTML。Convert documents between 40+ formats using pandoc"
summary_zh: "用pandoc CLI在40+格式间转文档,Markdown/Word/PDF/HTML。Convert documents between 40+ formats using pandoc"
license: "MIT"
description: |-
  Convert documents between 40+ formats using pandoc CLI。Handles Markdown
  ↔ Word ↔ PDF ↔ HTML ↔ La。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - 文档
  - 工作流
  - pdf
  - format
  - 请参考
  - 目录中的
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"

---

```markdown
# Pandoc Converter

## 技能描述

Pandoc Converter 是一款强大的文档转换工具，利用 Pandoc CLI 在多种格式之间进行转换，包括 Markdown、Word、PDF、HTML、LaTeX、EPUB 等。它适用于需要文件处理、文档转换、格式互转和内容提取的场景。

## 技能概述

| 属性 | 描述 |
| --- | --- |
| 名称 | Pandoc Converter |
| 版本 | 0.1.0 |
| 显示名称 | 转换器 |
| 摘要 | 使用 Pandoc CLI 在 40+ 格式间转换文档，支持 Markdown、Word、PDF、HTML 等。 |
| 摘要（中文） | 使用 Pandoc CLI 在 40+ 格式间转换文档，支持 Markdown、Word、PDF、HTML 等。 |
| 许可证 | MIT |
| 描述 | Pandoc Converter 是一款基于 Pandoc CLI 的文档转换工具，支持多种格式转换，包括 Markdown、Word、PDF、HTML、LaTeX、EPUB 等。 |
| 标签 | 文档、工作流、PDF、格式、请参考、目录中的 |
| 工具 | read、exec、write |
| 主页 | [Pandoc Converter](https://pandoc.org/) |
| 分类 | 自动化 |

## 核心功能

### 40+ 格式支持

- **Markdown, Word, PDF, HTML, LaTeX, EPUB, RST, AsciiDoc, Org-mode, and more**: Pandoc Converter 支持超过 40 种文档格式，满足各种文档转换需求。

### 双工具集

- **Python for smart conversions + bash for validation/batch processing**: 结合 Python 和 bash，实现智能转换和批量处理。

### 专业模板

- **12 templates covering academic, business, and web use cases**: 提供涵盖学术、商务和网页用例的 12 个专业模板。

### 完善的文档

- **Format guides, troubleshooting, templates, and quick reference**: 提供格式指南、故障排除、模板和快速参考。

### 智能默认值

- **Optimized settings for each conversion path**: 为每种转换路径提供优化的设置。

### 元数据保留

- **Keep titles, authors, dates across formats**: 在不同格式之间保留标题、作者和日期。

### 错误恢复

- **Validation and helpful error messages**: 提供验证和有用的错误消息。

## 快速开始

1. **确认运行环境**：确保您的系统满足 Pandoc Converter 的依赖要求。
2. **调用技能**：在 AI Agent 对话中调用 Pandoc Converter，并提供必要的输入参数。
3. **检查输出**：检查转换后的文档，并根据需要进行后续处理。

## 适用场景

| 场景 | 输入 | 输出 |
| --- | --- | --- |
| 格式转换 | 源文件与目标格式 (MD/Word/PDF/HTML) | 转换后的目标格式文档 |
| 批量处理 | 多个源文件与统一输出格式 | 批量转换结果目录 |
| 模板应用 | 文档与模板类型 (学术/商务/网页) | 带目录与元数据的专业文档 |

**不适用于**：需要人工判断的复杂决策场景。

## 使用流程

### 使用 Python Helper（推荐）

```bash
python （请参考skill目录中的脚本文件） input.md output.pdf
# ...
python （请参考skill目录中的脚本文件） report.md report.pdf --template business --toc
# ...
python （请参考skill目录中的脚本文件） --batch *.md --format pdf --output-dir ./pdfs
```

### 使用 Bash 工具

```bash
（请参考skill目录中的脚本文件） input/*.md pdf output/
# ...
（请参考skill目录中的脚本文件） output/document.pdf
（请参考skill目录中的脚本文件） output/book.epub
```

### 直接使用 Pandoc

```bash
pandoc input.md -o output.pdf
# ...
pandoc input.md -o output.docx
# ...
pandoc input.docx -o output.md --extract-media=./media
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 否 | Pandoc Converter 处理的内容输入 |
| mode | string | 否 | 处理模式，可选：json/text/markdown |
| max_retries | integer | 否 | 单步最大重试次数，默认：2 |
| skip_steps | array | 否 | 跳过的步骤编号（用于断点续传），默认：[] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "openclaw_result": "openclaw_result_value",
      "openclaw_metadata": "openclaw_metadata_value",
      "openclaw_status": "openclaw_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

## 异常处理

### 常见问题

* **"pandoc: command not found"** → 安装 Pandoc（请参阅 INSTALL.md）
* **"pdflatex not found"** → 安装 LaTeX 发行版
* **Unicode broken in PDF** → 使用 `--pdf-engine=xelatex`
* **Images missing** → 检查路径并使用 `--resource-path`
* **EPUB validation fails** → 运行 epubcheck 以获取详细信息

请参阅 `references/troubleshooting.md` 以获取全面解决方案。

### 错误场景

| 错误场景 | 原因 | 处理方式 |
| --- | --- | --- |
| LLM 响应超时或无响应 | 网络延迟或模型负载过高 | 确认 Agent 平台 LLM 服务正常 |
| 输入内容格式不正确 | 用户输入不符合 skill 预期格式 | 对照使用流程章节检查输入格式；参考示例章节修正输入 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 对照依赖说明章节确认环境配置；检查命令权限设置 |

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux

### 依赖说明（补充）

| 依赖项 | 类型 | 是否必需 | 获取方式 |
| --- | --- | --- | --- |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- **分类**：MD+EXEC()
- **说明**：基于 Markdown 的 AI Skill

**API Key 配置方式**：

```bash
export API_KEY="your_api_key_here"
```

配置后需重启会话或开启新终端生效。API Key 应妥善保管，避免泄露到版本控制系统。

## 案例展示

### 示例 1：基础用法

```bash
### 使用 Python Helper（推荐）

# ...
```bash
python （请参考 skill 目录中的脚本文件） input.md output.pdf
# ...
python （请参考 skill 目录中的脚本文件） report.md report.pdf --template business --toc
# ...
python （请参考 skill 目录中的脚本文件） --batch *./pdfs
```

# ...
### 使用 Bash 工具

# ...
```bash
（请参考 skill 目录中的脚本文件） input/*.md pdf output/
# ...
（请参考 skill 目录中的脚本文件） output/document.pdf
（请参考 skill 目录中的脚本文件） output/book.epub
```

# ...
### 直接使用 Pandoc

# ...
```bash
pandoc input.md -o output.pdf

pandoc input.md -o output.docx

pandoc input.docx -o output.md --extract-media=./media
```

# ...

## 常见问题

### Q1：如何开始使用 Pandoc Converter？

A：1. 确认您的运行环境满足依赖说明中的要求。2. 在 AI Agent 对话中调用本技能，提供必要的输入参数。3. 检查输出结果，根据需要进行后续处理。

### Q2：遇到错误怎么办？

A：1. 查看错误信息，根据错误提示进行操作，例如安装缺失的软件包。2. 查阅 `references/troubleshooting.md` 以获取更详细的解决方案。

### Q3：Pandoc Converter 有什么限制？

A：1. 不支持加密文件。2. 对于大文件，处理速度可能较慢。3. 可能受限于运行环境的资源限制。

## 错误处理

| 错误场景（续） | 原因 | 处理方式 |
| --- | --- | --- |
| LLM 响应超时或无响应 | 网络延迟或模型负载过高 | 确认 Agent 平台 LLM 服务正常 |
| 输入内容格式不正确 | 用户输入不符合 skill 预期格式 | 检查输入是否符合 skill 使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 边界条件与限制

### 输入限制

- **文件大小限制**：Pandoc Converter 技能可能对输入文件的尺寸有限制，通常受限于运行环境和操作系统的文件大小限制。例如，某些操作系统可能限制单个文件的大小不超过 4GB。
- **格式支持限制**：虽然 Pandoc 支持多种格式，但某些特殊格式可能由于复杂度或依赖项的原因不被支持。
- **编码限制**：输入文件应使用 UTF-8 编码，否则可能会出现编码错误。

### 性能边界

- **处理速度**：对于包含大量内容的文件，如大型 PDF 或 Word 文档，转换过程可能需要较长时间。
- **并发处理**：由于资源限制，技能可能不支持同时处理大量或大尺寸的文件。

### 兼容性约束

- **操作系统兼容性**：技能可能在某些操作系统（如 Windows Server）上运行时遇到兼容性问题。
- **Pandoc 版本**：技能依赖于 Pandoc CLI，因此需要确保安装的 Pandoc 版本与技能兼容。

### 其他限制

- **加密文件**：技能不适用于加密文件，如加密的 PDF 或 Word 文档。
- **网络依赖**：如果使用远程模板或资源，网络连接的稳定性将影响技能的性能。

---