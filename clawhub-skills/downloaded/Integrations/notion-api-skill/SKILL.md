---
slug: notion-api-skill
name: notion-api-skill
version: "1.0.11"
displayName: Notion
summary: "Notion API托管OAuth,查数据库/搜页面/读工作区"
  and read workspace cont...
license: MIT-0
description: |-
  Notion API integration with managed OAuth。Query databases, search pages,
  and read workspace cont。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
- Productivity
tools:
  - - read
- exec
# Notion
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

Access the Notion API with managed OAuth authentication. Query databases, search pages, and read workspace content. All write operations (creating, updating, or deleting pages, blocks, and databases) require explicit user confirmation specifying the target resource and connection before execution.

## Quick Start
> 详细内容已移至 `references/detail.md`

## Base URL
```text
https://api.maton.ai/notion/{native-api-path}
```

Maton proxies requests to `api.notion.com` and automatically injects your OAuth token. Write operations (POST, PATCH, DELETE) must only be executed after the user confirms the target page/database ID and intended connection.

## Required Headers
All Notion API requests require the version header:

```text
Notion-Version: 2025-09-03
```

## Installation
**NPM:**

```bash
npm install -g @maton/cli
```

**Homebrew:**

```bash
brew install maton-ai/cli/maton
```

## Authentication
> 详细内容已移至 `references/detail.md`

## Connection Management
Manage your Notion OAuth connections at `https://api.maton.ai`.

### List Connections
> 详细内容已移至 `references/detail.md`

### Create Connection
> 详细内容已移至 `references/detail.md`

### Get Connection
> 详细内容已移至 `references/detail.md`

### Delete Connection
> 详细内容已移至 `references/detail.md`

### Specifying Connection
> 详细内容已移至 `references/detail.md`

## Key Concept: Databases vs Data Sources
> 详细内容已移至 `references/detail.md`

## Security & Permissions
* Access is scoped to pages, databases, blocks, users, and search within the connected Notion account.
* **All write operations require explicit user approval.** Before executing any create, update, or delete call:
  1. Confirm the exact target (page ID, database ID, block ID) with the user.
  2. Verify the correct connection ID when multiple connections exist.
  3. State whether the action is reversible or destructive.
* **Irreversible / high-risk operations** (require extra caution):
  + Deleting pages or blocks (archived, not permanently deleted, but may disrupt workflows)
  + Bulk updates across multiple pages or databases
  + Modifying shared workspace pages visible to other team members
* **Scope boundaries:**
  + Only operate on pages and databases the user explicitly names or identifies. Never enumerate or modify resources outside the current task context.
  + Use the least-privileged Notion connection available for the task.
  + Do not perform bulk or batch operations without explicit user approval for each batch.

## API Reference

### Search
> 详细内容已移至 `references/detail.md`

### Databases
> 详细内容已移至 `references/detail.md`

### Users
> 详细内容已移至 `references/detail.md`

## Filter Operators
* `equals`, `does_not_equal`
* `contains`, `does_not_contain`
* `starts_with`, `ends_with`
* `is_empty`, `is_not_empty`
* `greater_than`, `less_than`

## Block Types
* `paragraph`, `heading_1`, `heading_2`, `heading_3`
* `bulleted_list_item`, `numbered_list_item`
* `to_do`, `code`, `quote`, `divider`

## Pagination
Notion uses cursor-based pagination. The CLI automatically paginates with '--paginate'.

Example:

```bash
maton notion data-source query <dataSourceId> --paginate
```

## 示例
### CLI
```bash
maton notion search 'roadmap'

maton notion page view 0123456789abcdef0123456789abcdef

maton notion data-source query <dataSourceId> --filter '{"property":"Status","select":{"equals":"Active"}}'

maton notion search 'roadmap' --json --jq '.results | map(select(.object == "page"))'
```

### JavaScript
```javascript
const response = await fetch('https://api.maton.ai/notion/v1/search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.MATON_API_KEY}`,
    'Notion-Version': '2025-09-03'
  },
  body: JSON.stringify({ query: 'meeting' })
});
```

### Python
```python
import os
import requests

response = requests.post(
    'https://api.maton.ai/notion/v1/search',
    headers={
        'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}',
        'Notion-Version': '2025-09-03'
    },
    json={'query': 'meeting'}
)
```

## Notes
* All IDs are UUIDs (with or without hyphens)
* Use `GET /databases/{id}` to get the `data_sources` array containing data source IDs
* Creating databases requires `POST /databases` endpoint
* Delete blocks returns the block with `archived: true`
* IMPORTANT: When using curl commands, use `curl -g` when URLs contain brackets (`fields[]`, `sort[]`, `records[]`) to disable glob parsing
* IMPORTANT: When piping curl output to `jq` or other commands, environment variables like `$MATON_API_KEY` may not expand correctly in some shell environments. You may get "Invalid API key" errors when piping.

## Error Handling
| Status | Meaning |
| --- | --- |
| 400 | Missing Notion connection |
| 401 | Invalid or missing Maton API key |
| 429 | Rate limited (10 req/sec per account) |
| 4xx/5xx | Passthrough error from Notion API |

### 错误处理
**CLI:**

1. Check your auth state:

```bash
maton whoami
```

2. Verify the API key is valid by listing connections:

```bash
maton connection list
```

**Manual:**

1. Check that the `MATON_API_KEY` environment variable is set:

```bash
echo $MATON_API_KEY
```

2. Verify the API key is valid by listing connections:

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

### Troubleshooting: Invalid App Name
1. Ensure your URL path starts with `notion`. For example:

* Correct: `https://api.maton.ai/notion/v1/search`
* Incorrect: `https://api.maton.ai/v1/search`

## Resources
* [Notion API Introduction](https://developers.notion.com/reference/intro)
* [Search](https://developers.notion.com/reference/post-search.md)
* [Query Database](https://developers.notion.com/reference/post-database-query.md)
* [Get Page](https://developers.notion.com/reference/retrieve-a-page.md)
* [Create Page](https://developers.notion.com/reference/post-page.md)
* [Update Page](https://developers.notion.com/reference/patch-page.md)
* [Append Block Children](https://developers.notion.com/reference/patch-block-children.md)
* [Filter Reference](https://developers.notion.com/reference/post-database-query-filter.md)
* [LLM Reference](https://developers.notion.com/llms.txt)
* [Maton CLI Manual](https://cli.maton.ai/manual)
* [Maton Community](https://discord.com/invite/dBfFAcefs2)
* [Maton Support](mailto:support@maton.ai)

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
- Notion API integration with managed OAuth
- Query databases, search pages,
  and read workspace cont
- 触发关键词: api, notion, managed, integration, oauth, skill

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题
### Q1: 如何开始使用Notion？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Notion有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
