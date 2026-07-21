---
slug: pdf-toolkit-free
name: pdf-toolkit-free
version: "1.0.0"
displayName: PDF工具包（免费版）
summary: 综合PDF处理工具集：创建、编辑、转换、合并、拆分、压缩、加密一站式解决。
license: Proprietary
edition: free
description: |-
  PDF工具包 - （免费版）

  核心能力: PDF处理, PDF创建, PDF合并, PDF拆分, PDF压缩, PDF加密, 水印, OCR, 表格提取

  适用场景: 个人用户日常使用，核心功能覆盖基础需求

  差异化: 精简版，适合个人用户快速上手，提供核心功能与基础用法

  触发关键词: PDF处理, PDF创建, PDF合并, PDF拆分, PDF压缩, PDF加密, 水印, OCR, 表格提取
tags:
- PDF处理
- PDF工具
- 文档处理
- OCR
tools:
  - - read
- exec
---

# PDF工具包（免费版）

## 概述

PDF工具包是针对PDF处理领域的专业化AI辅助工具。免费版面向个人用户，提供核心功能与基础用法，适合快速上手和日常使用。

本工具经过深度优化，增强元数据和触发关键词，完全适配SkillHub平台规范。

## 核心能力

PDF创建、PDF编辑、格式转换、合并拆分、压缩优化、加密解密、OCR识别、表单填写

### 核心能力

- 基础功能完整覆盖
- 简洁易用的操作接口
- 标准格式输入输出
- 快速上手，零配置即可使用
- 适合个人日常使用场景

## 使用场景

### 场景1：综合PDF处理

对PDF进行多种操作组合处理。**示例指令**：`

`处理这个PDF：提取文本并加水印

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景2：PDF转换

将PDF转换为Word、Excel等格式。**示例指令**：`

`把PDF转为Word

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景3：PDF安全

对PDF进行加密、添加水印等安全操作。**示例指令**：`

`加密这个PDF并加水印

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果


## 快速开始

### 环境准备

```bash
# 确保Python环境可用
python3 --version

# 依赖说明
pip install requests
```

### 基础用法

```python
# PDF工具包基础
from pypdf import PdfReader, PdfWriter

# 提取文本
reader = PdfReader("input.pdf")
text = reader.pages[0].extract_text()
print(text[:200])

# 加密PDF
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)
writer.encrypt("password123")
with open("encrypted.pdf", "wb") as f:
    writer.write(f)
print("PDF已加密")
```

### 执行结果

执行上述代码后，将根据输入参数返回结构化结果。免费版支持单次操作，适合处理单个文件或任务。

## 示例

```yaml
pdf_toolkit:
  default_library: pypdf
  operations: [read, create, merge, encrypt]
  output_format: pdf
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

### 已知限制

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

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
- **版本**: 免费版（v1.0.0 免费版，核心功能）

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |
