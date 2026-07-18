---
slug: local-rag-tool-free
name: local-rag-tool-free
version: "1.0.0"
displayName: 本地文件检索（免费版）
summary: 本地文件RAG检索增强生成工具，支持文档索引、语义搜索与上下文注入。
license: MIT
edition: free
description: |-
  本地文件检索 - （免费版）

  核心能力: 本地RAG, 文档检索, 语义搜索, 知识库, RAG, retrieval augmented, 向量搜索, 上下文注入

  适用场景: 个人用户日常使用，核心功能覆盖基础需求

  差异化: 精简版，适合个人用户快速上手，提供核心功能与基础用法

  触发关键词: 本地RAG, 文档检索, 语义搜索, 知识库, RAG, retrieval augmented, 向量搜索, 上下文注入
tags:
- RAG
- 本地检索
- 语义搜索
- 知识库
tools:
- read
- exec
---

# 本地文件检索（免费版）

## 概述

本地文件检索是针对RAG检索领域的专业化AI辅助工具。免费版面向个人用户，提供核心功能与基础用法，适合快速上手和日常使用。

本工具经过深度优化，增强元数据和触发关键词，完全适配SkillHub平台规范。

## 核心能力

文档索引、语义搜索、上下文注入、分块策略、向量存储、检索增强生成

### 免费版核心功能

- 基础功能完整覆盖
- 简洁易用的操作接口
- 标准格式输入输出
- 快速上手，零配置即可使用
- 适合个人日常使用场景

## 使用场景

### 场景1：本地文档问答

对本地文档建立索引后进行语义检索和问答。**示例指令**：`

`搜索本地文档中关于部署的内容

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景2：代码库检索

对代码文件建立索引，支持代码语义搜索。**示例指令**：`

`搜索项目中的认证逻辑代码

**操作流程**：
1. 识别用户需求类型
2. 加载对应处理模块
3. 执行操作并返回结果

### 场景3：知识库构建

将多个文档构建为可检索的本地知识库。**示例指令**：`

`构建本地知识库

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
# 本地RAG基础检索
import os
from pathlib import Path

def build_index(docs_dir):
    index = {}
    for md_file in Path(docs_dir).rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        words = set(content.lower().split())
        for word in words:
            if word not in index:
                index[word] = []
            index[word].append(str(md_file))
    return index

def search(index, query):
    results = []
    for word in query.lower().split():
        if word in index:
            results.extend(index[word])
    return list(set(results))

idx = build_index("./docs")
results = search(idx, "部署 配置")
print(f"找到 {len(results)} 个相关文档")
```

### 执行结果

执行上述代码后，将根据输入参数返回结构化结果。免费版支持单次操作，适合处理单个文件或任务。

## 配置示例

```yaml
rag:
  index_dir: "./rag_index"
  chunk_size: 500
  search_mode: keyword
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
| numpy | Python库 | 可选 | pip install numpy |
| rank-bm25 | Python库 | 可选 | pip install rank-bm25 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
- **版本**: 免费版（v1.0.0 免费版，核心功能）
