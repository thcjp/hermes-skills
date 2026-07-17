---
slug: local-file-rag-basic
name: local-file-rag-basic
version: "1.0.0"
displayName: local-file-rag-basic
summary: High-performance local File RAG suite (Basic Edition).
license: MIT
description: |-
  High-performance local File RAG suite (Basic Edition).

  核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: high, suite, local, performance, file, rag, local-file-rag-basic, basic
tags:
- Knowledge
tools:
- read
- exec
---

# local-file-rag-basic

## Description

This is the **Basic Edition** of the high-performance local RAG suite, providing efficient code and document retrieval within constraints.

* **Constraints**:
  + Only indexes files **under 20MB**.
  + Uses single-threaded (sequential) indexing for lower resource usage.
* **Support**: JS/TS, Python, C++, Go, Markdown, PDF, DOCX, XLSX, etc.

## Tools

### local_file_rag_search

Efficiently searches the local workspace.

**Parameters:**

* `query` (string, required): Search terms or function names.
* `targetFile` (string, optional): Specific file path to restrict the search.
* `rootDir` (string, optional): Root directory to scan.

**Output Protocol:**
Returns a structured result with Skeletons, Metadata, and Clustered Code Snippets.

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
