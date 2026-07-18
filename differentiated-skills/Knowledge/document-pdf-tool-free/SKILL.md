---
slug: document-pdf-tool-free
name: document-pdf-tool-free
version: "1.0.0"
displayName: PDF文档工具（免费版）
summary: 综合PDF处理工具包：文本表格提取、PDF创建、合并拆分、水印、加密、OCR识别。
license: MIT
edition: free
description: |-
  PDF文档工具 - （免费版）

  核心能力: PDF处理, 文本提取, 表格提取, PDF合并, PDF拆分, OCR识别, 水印, 加密

  适用场景: 个人用户日常使用，核心功能覆盖基础需求

  差异化: 精简版，适合个人用户快速上手，提供核心功能与基础用法

  触发关键词: PDF处理, 文本提取, 表格提取, PDF合并, PDF拆分, OCR识别, 水印, 加密
tags:
- PDF处理
- 文本提取
- 表格提取
- OCR
- 文档工具
tools:
- read
- exec
---

# PDF文档工具（免费版）

## 概述

PDF文档工具是针对PDF处理领域的专业化AI辅助工具。免费版面向个人用户，提供核心功能与基础用法，适合快速上手和日常使用。

本工具经过深度优化，增强元数据和触发关键词，完全适配SkillHub平台规范。

## 核心能力

文本提取、表格提取、PDF创建、合并拆分、页面旋转、元数据提取、水印添加、密码保护、OCR识别

### 免费版核心功能

- 基础功能完整覆盖
- 简洁易用的操作接口
- 标准格式输入输出
- 快速上手，零配置即可使用
- 适合个人日常使用场景

## 使用场景

### 场景1：PDF文本提取

使用pdfplumber或pdftotext提取PDF中的文本内容。**示例指令**：`

`提取这个PDF的文本

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景2：PDF表格提取

从PDF中提取表格数据并导出为Excel格式。**示例指令**：`

`提取PDF中的表格

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景3：PDF合并与拆分

将多个PDF合并为一个，或按页码拆分为多个文件。**示例指令**：`

`合并这三个PDF文件

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果


## 快速开始

### 环境准备

```bash
# 确保Python环境可用
python3 --version

# 安装基础依赖（如需要）
pip install requests
```

### 基础用法

```python
# PDF基础操作
from pypdf import PdfReader, PdfWriter

# 提取文本
reader = PdfReader("document.pdf")
text = "".join(page.extract_text() for page in reader.pages)
print(f"共 {len(reader.pages)} 页")

# 合并PDF
writer = PdfWriter()
for pdf_file in ["a.pdf", "b.pdf"]:
    for page in PdfReader(pdf_file).pages:
        writer.add_page(page)
with open("merged.pdf", "wb") as f:
    writer.write(f)
```

### 执行结果

执行上述代码后，将根据输入参数返回结构化结果。免费版支持单次操作，适合处理单个文件或任务。

## 配置示例

```yaml
pdf:
  default_library: pypdf
  text_extraction: pdfplumber
  output_format: txt
```

### 配置说明

| 配置项 | 说明 | 默认值 |
|:-------|:-----|:-------|
| 基础路径 | 工作目录 | `./` |
| 输出格式 | 结果输出格式 | `json` |

## 最佳实践

### 基础使用建议

1. **明确需求**：在使用前明确需要处理的内容和期望结果
2. **检查输入**：确保输入文件格式正确、内容完整
3. **保存结果**：处理完成后及时保存输出结果
4. **定期清理**：定期清理临时文件
5. **错误处理**：遇到错误时检查输入参数

### 性能优化

```python
# 免费版：单文件优化
# 确保输入文件不超过建议大小
# 处理完成后释放资源
```

## 常见问题

### Q1: 处理速度较慢怎么办？

A: 免费版为单线程处理，对于大文件建议分批处理或升级到专业版获得并行处理能力。

### Q2: 支持的文件格式有哪些？

A: 支持标准格式输入输出，常见格式包括JSON、YAML、Markdown等。

### Q3: 如何获取API Key？

A: 本Skill基于Markdown指令，无需额外API Key。如需外部服务API，请参考对应服务的注册流程。

### Q4: 免费版有使用限制吗？

A: 免费版支持单次操作，适合个人日常使用。如需批量处理或高级功能，建议升级到专业版。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+


### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| pypdf | Python库 | 必需 | pip install pypdf |
| pdfplumber | Python库 | 推荐 | pip install pdfplumber |
| reportlab | Python库 | 可选 | pip install reportlab |
| pytesseract | Python库 | 可选 | pip install pytesseract |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
- **版本**: 免费版（v1.0.0 免费版，核心功能）
