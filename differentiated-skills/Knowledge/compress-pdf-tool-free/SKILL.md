---
slug: compress-pdf-tool-free
name: compress-pdf-tool-free
version: "1.0.0"
displayName: PDF压缩工具（免费版）
summary: 通过API上传PDF文件进行压缩，支持图像质量与DPI参数调整，轮询返回下载链接。
license: MIT
edition: free
description: |-
  PDF压缩工具 - （免费版）

  核心能力: PDF压缩, 文件压缩, 减小体积, 压缩PDF, compress pdf, 批量压缩

  适用场景: 个人用户日常使用，核心功能覆盖基础需求

  差异化: 精简版，适合个人用户快速上手，提供核心功能与基础用法

  触发关键词: PDF压缩, 文件压缩, 减小体积, 压缩PDF, compress pdf, 批量压缩
tags:
- PDF处理
- 文件压缩
- 批量处理
tools:
- read
- exec
---

# PDF压缩工具（免费版）

## 概述

PDF压缩工具是针对PDF处理领域的专业化AI辅助工具。免费版面向个人用户，提供核心功能与基础用法，适合快速上手和日常使用。

本工具经过深度优化，增强元数据和触发关键词，完全适配SkillHub平台规范。

## 核心能力

PDF文件上传、压缩参数配置、任务轮询、下载链接生成、批量压缩

### 免费版核心功能

- 基础功能完整覆盖
- 简洁易用的操作接口
- 标准格式输入输出
- 快速上手，零配置即可使用
- 适合个人日常使用场景

## 使用场景

### 场景1：单文件压缩

上传PDF文件，设置图像质量和DPI，获取压缩后下载链接。**示例指令**：`

`压缩这个PDF文件

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景2：批量压缩

一次性处理多个PDF文件，统一压缩参数，生成压缩报告。**示例指令**：`

`批量压缩这10个PDF

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景3：压缩参数优化

根据文件类型推荐最佳压缩参数，平衡质量与体积。**示例指令**：`

`优化扫描文档的压缩参数

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
# PDF压缩基础调用
import requests

def compress_pdf(file_path, api_key, quality=75, dpi=144):
    url = "https://api.example.com/solutions/solutions/api/29"
    headers = {"Authorization": f"Bearer {api_key}"}
    files = {"file": open(file_path, "rb")}
    data = {"imageQuality": quality, "dpi": dpi}
    resp = requests.post(url, headers=headers, files=files, data=data)
    return resp.json()

result = compress_pdf("document.pdf", "YOUR_API_KEY")
print(f"任务ID: {result.get('job_id')}")
```

### 执行结果

执行上述代码后，将根据输入参数返回结构化结果。免费版支持单次操作，适合处理单个文件或任务。

## 配置示例

```yaml
compress:
  api_key: "YOUR_API_KEY"
  default_quality: 75
  default_dpi: 144
  poll_interval: 3
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

A: 需要压缩服务API Key，通过服务注册获取。如需外部服务API，请参考对应服务的注册流程。

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
| requests | Python库 | 必需 | pip install requests |

### API Key 配置
- 需要压缩服务API Key，通过服务注册获取

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
- **版本**: 免费版（v1.0.0 免费版，核心功能）
