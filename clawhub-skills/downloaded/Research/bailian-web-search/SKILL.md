---
slug: bailian-web-search
name: bailian-web-search
version: "1.0.4"
displayName: Bailian Web Search
summary: "通过百炼(阿里ModelStudio)API进行AI优化网络搜索,返回多源精简结果"
  concise web se...
license: MIT
description: |-
  AI-optimized web search via Bailian(Alibaba ModelStdio) API。Returns
  multisourced, concise web se。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Bailian Web Search

AI-optimized web search using Bailian WebSearch(Enable_search) API. Designed for AI agents - returns clean, relevant content.

## Search

```bash
{baseDir}/scripts/mcp-websearch.sh "query"
{baseDir}/scripts/mcp-websearch.sh  "query"  10
```

## Options

* `<count>`: Number of results (default: 5, max: 20)
* `<query>`: User Query for Websearch

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

- AI-optimized web search via Bailian(Alibaba ModelStdio) API
- Returns
  multisourced, concise web se
- 触发关键词: web, bailian, alibaba, optimized, modelstdio, search

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Bailian Web Search？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Bailian Web Search有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 性能取决于底层模型能力
