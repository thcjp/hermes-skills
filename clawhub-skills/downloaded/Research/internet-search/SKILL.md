---
slug: internet-search
name: internet-search
version: "0.3.4"
displayName: Internet Search
summary: "高效使用internet_search工具:类别路由、查询构建、多轮搜索策略,提升搜索效率"
  formulation, and multi-...
license: MIT
description: |-
  How to use the internet_search tool effectively — category routing,
  query formulation, and multi-。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---


# Internet Search

Queries a self-hosted SearXNG instance aggregating multiple search engines.

## Category Routing

Always set `category` based on the nature of the query.

| Category | When to use | Engines |
| --- | --- | --- |
| `general` | Default. Facts, how-tos, products, people, broad web. | Brave, Bing, DDG, Startpage, Qwant, Wikipedia… |
| `news` | Recent events, breaking news, anything time-sensitive. | Bing News, DDG News |
| `academic` | Research papers, studies, medical literature, preprints. | arXiv, Google Scholar, PubMed |
| `social` | Opinions, community recommendations, "what do people think about X". | Reddit |

## Query Formulation

Write queries as a search engine expects — keywords, not full sentences:

```text
"what is the fastest async runtime for rust"

"rust async runtime benchmarks 2025"
```

* **news**: include a time anchor — `"OpenAI o3 release 2025"` not just `"OpenAI o3"`
* **academic**: use field terminology — `"transformer attention efficiency survey"`
* **social**: phrase as community search — `"reddit best mechanical keyboard 2025"`

## SearXNG Search Syntax (in `query`)

SearXNG supports lightweight query modifiers you can embed directly into the `query` string:

| Syntax | Meaning | Examples |
| --- | --- | --- |
| `!<engine>` / `!<category>` | Select engine(s) and/or a category. Chainable and inclusive; abbreviations are accepted. | `!wp paris`, `!wikipedia paris`, `!map paris`, `!map !ddg !wp paris` |
| `:<lang>` | Language filter | `:fr !wp Wau Holland` |

## Count

* `count=5` (default) — sufficient for most tasks
* `count=10` — comparing many options, checking consensus
* `count=3` — quick fact checks

## Multi-Search Strategy

Fire multiple focused searches rather than one broad one:

```text
internet_search("best way to deploy Node.js")

internet_search("Node.js Docker deployment best practices 2025")
internet_search("Node.js PM2 vs Docker production", category="social")
internet_search("Node.js zero-downtime deployment strategies")
```

Combine `general` + `social` for factual + sentiment coverage:

```text
internet_search("Bun runtime performance vs Node.js benchmarks")
internet_search("Bun runtime production experience", category="social")
```

## When NOT to Use

* Things you already know with high confidence
* Stable API docs or well-known syntax — use training knowledge
* Repeating a search that already answered the question

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| `general` for a research paper | Use `category="academic"` |
| Searching "what happened today" | Use `category="news"` with a specific topic |
| One broad search for a multi-part question | Break into 2–3 focused searches |
| Repeating a failed search verbatim | Rephrase with different keywords |
| `count=20` for a simple fact | Default `count=5` is almost always enough |

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

- How to use the internet_search tool effectively — category routing,
  query formulation, and multi-
- 触发关键词: internet, effectively, search, category

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

### Q1: 如何开始使用Internet Search？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Internet Search有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
