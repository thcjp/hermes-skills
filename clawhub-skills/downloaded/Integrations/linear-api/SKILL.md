---
slug: linear-api
name: linear-api
version: "1.0.6"
displayName: Linear
summary: This skill is a disclosed Linear integration that uses Maton authentication
  to read and manage Li...
license: MIT-0
description: |-
  This skill is a disclosed Linear integration that uses Maton authentication
  to read and manage Li。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags: '[''Integrations'']'
tools:
  - read
  - exec
# Linear
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

Access the Linear API with managed OAuth authentication. Query and manage issues, projects, teams, cycles, labels, and comments using GraphQL.

## Quick Start
> 详细内容已移至 `references/detail.md`

## Base URL
```text
https://api.maton.ai/linear/graphql
```

All requests use POST to the GraphQL endpoint. Maton proxies requests to `api.linear.app` and automatically injects your OAuth token.

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
Manage your Linear OAuth connections at `https://api.maton.ai`.

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

## Security & Permissions
* Access is scoped to issues, projects, teams, cycles, and comments within the connected Linear account.
* **All write operations require explicit user approval.** Before executing any create, update, or delete call, confirm the target resource and intended effect with the user.

## API Reference
Linear uses a GraphQL API. All operations are sent as POST requests with a JSON body containing the `query` field.

### Viewer (Current User)
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ viewer { id name email } }"}
```

Example:

```bash
maton linear whoami
```

### Organization
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ organization { id name urlKey } }"}
```

Example:

```bash
maton linear org view
```

### Teams
> 详细内容已移至 `references/detail.md`

### Projects
#### List Projects
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ projects(first: 10) { nodes { id name state createdAt } } }"}
```

Example:

```bash
maton linear project list
```

### Cycles
#### List Cycles
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ cycles(first: 10) { nodes { id name number startsAt endsAt } } }"}
```

Example:

```bash
maton linear cycle list
```

### Labels
#### List Labels
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ issueLabels(first: 20) { nodes { id name color } } }"}
```

Example:

```bash
maton linear label list
```

### Workflow States
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ workflowStates(first: 20) { nodes { id name type team { key } } } }"}
```

Example:

```bash
maton linear state list
```

### Users
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ users(first: 20) { nodes { id name email active } } }"}
```

Example:

```bash
maton linear user list
```

### Comments
> 详细内容已移至 `references/detail.md`

## Pagination
Linear uses Relay-style cursor-based pagination. The CLI automatically paginates with '--paginate'.

Example:

```bash
maton linear issue list -c ABC --paginate
```

## 示例
### CLI
```bash
maton linear issue list -c ABC -L 10

maton linear issue view ABC-123

maton linear issue create --team-id TEAM_ID -t 'Fix login'

maton linear comment create --issue ABC-123 -b 'Looking into this'
```

### JavaScript
```javascript
const response = await fetch('https://api.maton.ai/linear/graphql', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${process.env.MATON_API_KEY}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    query: `{ issues(first: 10) { nodes { id identifier title state { name } } } }`
  })
});
const data = await response.json();
```

### Python

## Notes
* Linear uses GraphQL exclusively (no REST API)
* Issue identifiers like `ABC-123` can be used in place of UUIDs for the `id` parameter
* Priority values: 0 = No priority, 1 = Urgent, 2 = High, 3 = Medium, 4 = Low
* Workflow state types: `backlog`, `unstarted`, `started`, `completed`, `canceled`
* The GraphQL schema is introspectable at `https://api.linear.app/graphql`
* Use `searchIssues(term: "...")` for full-text search across issues
* Some mutations (delete, create labels/projects) may require additional OAuth scopes. If you receive a scope error, contact Maton support at [support@maton.ai](mailto:support@maton.ai) with the specific operations/APIs you need and your use-case

## Error Handling
> 详细内容已移至 `references/detail.md`

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
1. Ensure your URL path starts with `linear`. For example:

* Correct: `https://api.maton.ai/linear/graphql`
* Incorrect: `https://api.maton.ai/graphql`

## Resources
* [Linear API Overview](https://linear.app/developers)
* [Linear GraphQL Getting Started](https://linear.app/developers/graphql)
* [Linear GraphQL Schema (Apollo Studio)](https://studio.apollographql.com/public/Linear-API/schema/reference?variant=current)
* [Linear API and Webhooks](https://linear.app/docs/api-and-webhooks)
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
- This skill is a disclosed Linear integration that uses Maton authentication
  to read and manage Li
- 触发关键词: api, linear, disclosed, integration, skill

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题
### Q1: 如何开始使用Linear？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Linear有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
