---
slug: solo-research-free
name: solo-research-free
version: "1.0.0"
displayName: 独立研究工具免费版
summary: 免费版研究工具，支持WebFetch内容获取与基础搜索策略。
license: MIT
description: |-
  独立研究工具免费版，提供基础的多策略搜索能力。
  支持WebFetch内容获取与基础搜索回退策略。
  适用于个人研究与技术调研场景。
tools:
  - read
  - exec
---

# 独立研究工具（免费版）

提供基础WebFetch内容获取与搜索策略的研究工具。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **网络访问**: 需要互联网连接进行搜索与内容获取

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| WebFetch | 工具 | 必需 | Agent内置工具 |
| 网络访问 | 网络 | 必需 | 用于搜索与内容获取 |

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，需要exec与WebFetch工具进行搜索与内容获取）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行基础研究任务

## 核心能力

### WebFetch
获取指定URL的网页内容并进行结构化提取：

- **内容获取**：获取网页全文内容
- **结构化提取**：从网页中提取关键信息
- **重试机制**：网络失败时自动重试
- **内容清洗**：去除广告、导航等无关内容

**输入**: 用户提供WebFetch所需的指令和必要参数。
**处理**: 按照skill规范执行WebFetch操作,遵循单一意图原则。
**输出**: 返回WebFetch的执行结果,包含操作状态和输出数据。### Blocked Content Fallback

当内容被阻止或无法访问时的回退策略：

- **替代来源**：寻找相同内容的替代URL
- **摘要回退**：从搜索结果摘要中提取关键信息
- **用户提示**：当回退策略失败时，提示用户提供内容

### 基础研究方法论

基础研究流程：

- **并发查询**：同时发起多个搜索查询
- **来源验证**：验证来源的权威性与时效性
- **结果综合**：综合研究发现并输出结论

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 明确研究问题与目标
3. Agent使用WebFetch获取相关网页内容
4. 如遇内容阻止，使用回退策略
5. 综合研究发现，输出结论

## 示例

### 示例1：技术调研

```
用户: 帮我调研一下Zustand这个React状态管理库

Agent: 研究完成

## Key Findings
1. Zustand - 轻量级React状态管理库
2. API简洁，学习成本低
3. 支持TypeScript
4. 无需Provider包裹

## 来源
- github.com/pmndrs/zustand (WebFetch获取)
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| WebFetch获取失败 | 网页不可访问 | 使用Blocked Content Fallback；尝试替代URL |
| 搜索结果为空 | 关键词过于具体 | 扩大搜索范围；使用同义词 |
| 来源不可靠 | 信息来源缺乏权威性 | 标记来源可靠性；寻找替代来源 |

## 常见问题

### Q1: 免费版与付费版有什么区别？
A: 免费版提供WebFetch内容获取与基础回退策略。付费版额外提供GitHub Library Discovery、MCP web_search、Product Hunt Research、交叉验证与结构化结果输出等高级功能。

### Q2: 如何处理被阻止的内容？
A: 使用回退策略：寻找替代URL、从搜索摘要提取关键信息、提示用户提供内容。

### Q3: 支持哪些搜索方式？
A: 免费版主要通过WebFetch直接获取指定URL的内容，支持基础的内容回退策略。

## 已知限制

- 不支持GitHub Library Discovery功能
- 不支持MCP web_search网络搜索
- 不支持Product Hunt产品调研
- 不支持交叉验证与结构化结果输出
