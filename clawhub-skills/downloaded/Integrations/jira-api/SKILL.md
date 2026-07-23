---
slug: jira-api
name: jira-api
version: "1.0.8"
displayName: Jira
summary: "Jira API托管OAuth,JQL搜索/建改issue/管看板"
  update issues, manage...
license: MIT-0
description: |-
  Jira API integration with managed OAuth。Search issues with JQL, create
  and update issues, manage。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Integrations
- Productivity
tools:
  - - read
- exec
# Jira
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

Access the Jira Cloud API with managed OAuth authentication. Search issues with JQL, create and manage issues, and automate workflows.

## Quick Start
> 详细内容已移至 `references/detail.md`

## Base URL
```text
https://api.maton.ai/jira/{native-api-path}
```

Maton proxies requests to `api.atlassian.com` and automatically injects your OAuth token.

## Getting Cloud ID
> 详细内容已移至 `references/detail.md`

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
Manage your Jira OAuth connections at `https://api.maton.ai`.

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
* Access is scoped to issues, projects, boards, sprints, and users within the connected Jira account.
* **All write operations require explicit user approval.** Before executing any create, update, or delete call, confirm the target resource and intended effect with the user.

## API Reference

### Projects
> 详细内容已移至 `references/detail.md`

### Transitions
> 详细内容已移至 `references/detail.md`

### Comments
> 详细内容已移至 `references/detail.md`

### Users
> 详细内容已移至 `references/detail.md`

### Metadata
> 详细内容已移至 `references/detail.md`

## 示例
### CLI
```bash
maton jira cloud list

maton jira issue search 'project = PROJ AND status = "In Progress"' --cloud-id abc-123

maton jira issue search 'project = PROJ' --cloud-id abc-123 \
  --json --jq '.issues | map(select(.fields.status.name == "In Progress"))'

maton jira issue create --cloud-id abc-123 --project PROJ --summary 'Fix login'
```

### JavaScript
```javascript
// Get cloud ID first
const resources = await fetch(
  'https://api.maton.ai/jira/oauth/token/accessible-resources',
  { headers: { 'Authorization': `Bearer ${process.env.MATON_API_KEY}` } }
).then(r => r.json());

const cloudId = resources[0].id;

// Search issues
const issues = await fetch(
  `https://api.maton.ai/jira/ex/jira/${cloudId}/rest/api/3/search/jql?jql=project=KEY`,
  { headers: { 'Authorization': `Bearer ${process.env.MATON_API_KEY}` } }
).then(r => r.json());
```

### Python

## Notes
* Always fetch cloud ID first using `/oauth/token/accessible-resources`
* JQL queries must be bounded (e.g., `project=KEY`)
* Use URL encoding for JQL query parameters
* Update, Delete, Transition return HTTP 204 on success
* Agile API requires additional OAuth scopes. If you receive a scope error, contact Maton support at [support@maton.ai](mailto:support@maton.ai) with the specific operations/APIs you need and your use-case
* IMPORTANT: When using curl commands, use `curl -g` when URLs contain brackets (`fields[]`, `sort[]`, `records[]`) to disable glob parsing
* IMPORTANT: When piping curl output to `jq` or other commands, environment variables like `$MATON_API_KEY` may not expand correctly in some shell environments. You may get "Invalid API key" errors when piping.

## Error Handling
| Status | Meaning |
| --- | --- |
| 400 | Missing Jira connection or invalid JQL |
| 401 | Invalid or missing Maton API key |
| 429 | Rate limited (10 req/sec per account) |
| 4xx/5xx | Passthrough error from Jira API |

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
1. Ensure your URL path starts with `jira`. For example:

* Correct: `https://api.maton.ai/jira/ex/jira/{cloudId}/rest/api/3/project`
* Incorrect: `https://api.maton.ai/ex/jira/{cloudId}/rest/api/3/project`

## Resources
* [Jira API Introduction](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
* [Search Issues (JQL)](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get)
* [Get Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-get)
* [Create Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)
* [Transition Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-transitions-post)
* [JQL Reference](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/)
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
- Jira API integration with managed OAuth
- Search issues with JQL, create
  and update issues, manage
- 触发关键词: jira, api, managed, integration, oauth

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题
### Q1: 如何开始使用Jira？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Jira有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
