---
slug: github-api
name: github-api
version: "1.0.7"
displayName: GitHub
summary: This is a disclosed GitHub integration that uses Maton-managed OAuth/API
  access and includes appr...
license: MIT-0
description: |-
  This is a disclosed GitHub integration that uses Maton-managed OAuth/API
  access and includes appr。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags: '[''Integrations'', ''Development'']'
tools:
  - read
  - exec
# GitHub
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

Access the GitHub REST API with managed OAuth authentication. Manage repositories, issues, pull requests, commits, branches, users, and more.

## Quick Start
> 详细内容已移至 `references/detail.md`

## Base URL
```text
https://api.maton.ai/github/{native-api-path}
```

Maton proxies requests to `api.github.com` and automatically injects your OAuth token.

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
Manage your GitHub OAuth connections at `https://api.maton.ai`.

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
* Access is scoped to repositories, issues, pull requests, commits, branches, and users within the connected GitHub account.
* **All write operations require explicit user approval.** Before executing any create, update, or delete call:
  1. Confirm the exact target (owner/repo, issue number, branch name) with the user.
  2. Verify the correct connection ID when multiple connections exist.
  3. State whether the action is reversible or destructive.
* **Irreversible / high-risk operations** (require extra caution):
  + Deleting repositories, branches, or releases
  + Force-pushing or rewriting history
  + Merging pull requests (cannot be unmerged)
  + Removing collaborators or transferring ownership
* **Scope boundaries:**
  + Only operate on repositories the user explicitly names. Never enumerate or modify repositories outside the current task context.
  + Organization-level actions (creating repos, managing members) require the user to confirm the target organization.
  + Do not request or use OAuth scopes beyond what the current task requires.

## API Reference

### Users
> 详细内容已移至 `references/detail.md`

### Repository Contents
> 详细内容已移至 `references/detail.md`

### Branches
> 详细内容已移至 `references/detail.md`

### Commits
#### List Commits
```bash
GET /github/repos/{owner}/{repo}/commits?per_page=30
```

Query parameters: `sha` (branch name or commit SHA), `path` (file path), `author`, `committer`, `since`, `until`, `per_page`, `page`

#### Get Commit
```bash
GET /github/repos/{owner}/{repo}/commits/{ref}
```

#### Compare Two Commits
```bash
GET /github/repos/{owner}/{repo}/compare/{base}...{head}
```

### Issue Comments
> 详细内容已移至 `references/detail.md`

### Labels
> 详细内容已移至 `references/detail.md`

### Milestones
#### List Milestones
```bash
GET /github/repos/{owner}/{repo}/milestones?state=open&per_page=30
```

#### Create Milestone
```bash
POST /github/repos/{owner}/{repo}/milestones
Content-Type: application/json

{
  "title": "v1.0",
  "state": "open",
  "description": "First release",
  "due_on": "2026-03-01T00:00:00Z"
}
```

### Pull Request Reviews
> 详细内容已移至 `references/detail.md`

### Organizations
#### List User Organizations
```bash
GET /github/user/orgs?per_page=30
```

Note: Requires `read:org` scope.

#### Get Organization
```bash
GET /github/orgs/{org}
```

#### List Organization Members
```bash
GET /github/orgs/{org}/members?per_page=30
```

### Rate Limit
#### Get Rate Limit
```bash
GET /github/rate_limit
```

## Pagination
GitHub uses page-based pagination. The CLI automatically paginates with '--paginate'.

Example:

```bash
maton github repo list --paginate
```

## 示例
### CLI
```bash
maton github repo list --json

maton github repo list --json --jq '.[] | {name, full_name, private}'

maton github repo list --json --jq '.[] | select(.private == false) | .name'

maton github issue list --repo owner/repo --json --jq '.[].title'
```

### JavaScript
```javascript
const response = await fetch(
  'https://api.maton.ai/github/repos/owner/repo/issues?state=open&per_page=10',
  {
    headers: {
      'Authorization': `Bearer ${process.env.MATON_API_KEY}`
    }
  }
);
const issues = await response.json();
```

### Python
```python
import os
import requests

response = requests.get(
    'https://api.maton.ai/github/repos/owner/repo/issues',
    headers={'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}'},
    params={'state': 'open', 'per_page': 10}
)
issues = response.json()
```

## Notes
* Repository names are case-insensitive but the API preserves case
* Issue numbers and PR numbers share the same sequence per repository
* Content must be Base64 encoded when creating/updating files
* Rate limits: 5000 requests/hour for authenticated users, 30 searches/minute
* Search queries may timeout on very broad patterns
* Some endpoints require specific OAuth scopes (e.g., `read:org` for organization operations). If you receive a scope error, contact Maton support at [support@maton.ai](mailto:support@maton.ai) with the specific operations/APIs you need and your use-case
* IMPORTANT: When using curl commands, use `curl -g` when URLs contain brackets to disable glob parsing
* IMPORTANT: When piping curl output to `jq` or other commands, environment variables like `$MATON_API_KEY` may not expand correctly in some shell environments

## Error Handling
| Status | Meaning |
| --- | --- |
| 400 | Missing GitHub connection |
| 401 | Invalid or missing Maton API key |
| 403 | Forbidden - insufficient permissions or scope |
| 404 | Resource not found |
| 408 | Request timeout (common for complex searches) |
| 422 | Validation failed |
| 429 | Rate limited |
| 4xx/5xx | Passthrough error from GitHub API |

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
1. Ensure your URL path starts with `github`. For example:

* Correct: `https://api.maton.ai/github/user`
* Incorrect: `https://api.maton.ai/api.github.com/user`

## Resources
* [GitHub REST API Documentation](https://docs.github.com/en/rest)
* [Repositories API](https://docs.github.com/en/rest/repos/repos)
* [Issues API](https://docs.github.com/en/rest/issues/issues)
* [Pull Requests API](https://docs.github.com/en/rest/pulls/pulls)
* [Search API](https://docs.github.com/en/rest/search/search)
* [Rate Limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)
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
- This is a disclosed GitHub integration that uses Maton-managed OAuth/API
  access and includes appr
- 触发关键词: integration, api, disclosed, github

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题
### Q1: 如何开始使用GitHub？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: GitHub有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
