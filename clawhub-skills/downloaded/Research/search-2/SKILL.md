---
slug: search-2
name: search-2
version: "0.1.0"
displayName: Search
summary: Search the web using Tavily's LLM-optimized search API. Returns relevant
  results with content sni...
license: MIT
description: |-
  Search the web using Tavily's LLM-optimized search API. Returns relevant
  results with content sni...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: tavily, optimized, search, using'
tags:
- Research
tools:
- read
- exec
---

# Search

Search the web and get relevant results optimized for LLM consumption.

## Prerequisites

**Tavily API Key Required** - Get your key at <https://tavily.com>

Add to `~/.claude/settings.json`:

```json
{
  "env": {
    "TAVILY_API_KEY": "tvly-your-api-key-here"
  }
}
```

## Quick Start

### Using the Script

```bash
./scripts/search.sh '<json>'
```

**Examples:**

```bash
./scripts/search.sh '{"query": "python async patterns"}'

./scripts/search.sh '{"query": "React hooks tutorial", "max_results": 10}'

./scripts/search.sh '{"query": "AI news", "topic": "news", "time_range": "week", "max_results": 10}'

./scripts/search.sh '{"query": "machine learning", "include_domains": ["arxiv.org", "github.com"], "search_depth": "advanced"}'
```

### Basic Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "latest developments in quantum computing",
    "max_results": 5
  }'
```

### Advanced Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "machine learning best practices",
    "max_results": 10,
    "search_depth": "advanced",
    "include_domains": ["arxiv.org", "github.com"],
    "chunks_per_source": 3
  }'
```

## API Reference

### Endpoint

```text
POST https://api.tavily.com/search
```

### Headers

| Header | Value |
| --- | --- |
| `Authorization` | `Bearer <TAVILY_API_KEY>` |
| `Content-Type` | `application/json` |

### Request Body

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `query` | string | Required | Search query (keep under 400 chars) |
| `max_results` | integer | 5 | Maximum results (0-20) |
| `search_depth` | string | `"basic"` | `ultra-fast`, `fast`, `basic`, `advanced` |
| `topic` | string | `"general"` | `general`, `news`, `finance` |
| `chunks_per_source` | integer | 3 | Chunks per source (advanced/fast only) |
| `time_range` | string | null | `day`, `week`, `month`, `year` |
| `include_domains` | array | [] | Domains to include (max 300) |
| `exclude_domains` | array | [] | Domains to exclude (max 150) |
| `include_answer` | boolean | false | Include AI-generated answer |
| `include_raw_content` | boolean | false | Include full page content |
| `include_images` | boolean | false | Include image results |

### Response Format

```json
{
  "query": "latest developments in quantum computing",
  "results": [
    {
      "title": "Page Title",
      "url": "https://example.com/page",
      "content": "Extracted text snippet...",
      "score": 0.85
    }
  ],
  "response_time": 1.2
}
```

## Search Depth

| Depth | Latency | Relevance | Content Type |
| --- | --- | --- | --- |
| `ultra-fast` | Lowest | Lower | NLP summary |
| `fast` | Low | Good | Chunks |
| `basic` | Medium | High | NLP summary |
| `advanced` | Higher | Highest | Chunks |

**When to use each:**

* `ultra-fast`: Real-time chat, autocomplete
* `fast`: Need chunks but latency matters
* `basic`: General-purpose, balanced
* `advanced`: Precision matters (default recommendation)

## Examples

### News Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "AI news today",
    "topic": "news",
    "time_range": "day",
    "max_results": 10
  }'
```

### Domain-Filtered Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "Python async best practices",
    "include_domains": ["docs.python.org", "realpython.com", "github.com"],
    "search_depth": "advanced"
  }'
```

### Search with Full Content

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "React hooks tutorial",
    "max_results": 3,
    "include_raw_content": true
  }'
```

### Finance Search

```bash
curl --request POST \
  --url https://api.tavily.com/search \
  --header "Authorization: Bearer $TAVILY_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "AAPL earnings Q4 2024",
    "topic": "finance",
    "max_results": 10
  }'
```

## Tips

* **Keep queries under 400 characters** - Think search query, not prompt
* **Break complex queries into sub-queries** - Better results than one massive query
* **Use `include_domains`** to focus on trusted sources
* **Use `time_range`** for recent information
* **Filter by `score`** (0-1) to get highest relevance results

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
