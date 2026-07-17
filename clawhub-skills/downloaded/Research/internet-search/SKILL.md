---
slug: internet-search
name: internet-search
version: "0.3.4"
displayName: Internet Search
summary: How to use the internet_search tool effectively — category routing, query
  formulation, and multi-...
license: MIT
description: |-
  How to use the internet_search tool effectively — category routing,
  query formulation, and multi-...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: internet, effectively, search, category
tags:
- Research
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
