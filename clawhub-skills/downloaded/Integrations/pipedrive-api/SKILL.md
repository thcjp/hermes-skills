---
slug: pipedrive-api
name: pipedrive-api
version: "1.0.4"
displayName: Pipedrive
summary: "Pipedrive API托管OAuth,管交易/联系人/机构/活动(社区下载版)"
  activities, a...
license: MIT-0
description: |-
  Pipedrive API integration with managed OAuth。Manage deals, persons,
  organizations, activities, a。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Integrations
- Productivity
tools:
  - - read
- exec
# Pipedrive
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

Access the Pipedrive API with managed OAuth authentication. Manage deals, persons, organizations, activities, pipelines, and more for sales CRM workflows.

## Quick Start
```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

## Base URL
```text
https://api.maton.ai/pipedrive/{native-api-path}
```

Maton proxies requests to `api.pipedrive.com` and automatically injects your OAuth token.

## Authentication
All requests require the Maton API key in the Authorization header:

```text
Authorization: Bearer $MATON_API_KEY
```

**Environment Variable:** Set your API key as `MATON_API_KEY`:

```bash
export MATON_API_KEY="[REDACTED]"
```

### Getting Your API Key
1. Sign in or create an account at [maton.ai](https://maton.ai)
2. Go to [maton.ai/settings](https://maton.ai/settings)
3. Copy your API key

## Connection Management
Manage your Pipedrive OAuth connections at `https://api.maton.ai`.

### List Connections
```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections?app=pipedrive&status=ACTIVE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

### Create Connection
```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'app': 'pipedrive'}).encode()
req = urllib.request.Request('https://api.maton.ai/connections', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

### Get Connection
```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections/{connection_id}')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

**Response:**

```json
{
  "connection": {
    "connection_id": "{connection_id}",
    "status": "ACTIVE",
    "creation_time": "2025-12-08T07:20:53.488460Z",
    "last_updated_time": "2026-01-31T20:03:32.593153Z",
    "url": "https://connect.maton.ai/?session_token=...",
    "app": "pipedrive",
    "metadata": {}
  }
}
```

Open the returned `url` in a browser to complete OAuth authorization.

### Delete Connection
```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections/{connection_id}', method='DELETE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

### Specifying Connection
If you have multiple Pipedrive connections, specify which one to use with the `Maton-Connection` header:

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Maton-Connection', '{connection_id}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

If you have multiple connections, always include this header to ensure requests go to the intended account.

## Security & Permissions
* Access is scoped to deals, persons, organizations, activities, and pipelines within the connected Pipedrive account.
* **All write operations require explicit user approval.** Before executing any create, update, or delete call, confirm the target resource and intended effect with the user.

## API Reference

> 详细内容已移至 `references/detail.md` - ### Deals

> 详细内容已移至 `references/detail.md` - ### Persons (Contacts)
### Organizations
#### List Organizations
```bash
GET /pipedrive/api/v1/organizations
```

#### Get Organization
```bash
GET /pipedrive/api/v1/organizations/{id}
```

#### Create Organization
```bash
POST /pipedrive/api/v1/organizations
Content-Type: application/json

{
  "name": "Acme Corporation",
  "address": "123 Main St, City, Country",
  "visible_to": 3
}
```

#### Update Organization
```bash
PUT /pipedrive/api/v1/organizations/{id}
Content-Type: application/json

{
  "name": "Acme Corp International"
}
```

#### Delete Organization
```bash
DELETE /pipedrive/api/v1/organizations/{id}
```

### Activities
#### List Activities
```bash
GET /pipedrive/api/v1/activities
```

Query parameters:

* `type` - Activity type (e.g., `call`, `meeting`, `task`, `email`)
* `done` - Filter by completion (0 or 1)
* `user_id` - Filter by user
* `start_date` - Filter by start date
* `end_date` - Filter by end date

#### Get Activity
```bash
GET /pipedrive/api/v1/activities/{id}
```

#### Create Activity
```bash
POST /pipedrive/api/v1/activities
Content-Type: application/json

{
  "subject": "Follow-up call",
  "type": "call",
  "due_date": "2025-03-15",
  "due_time": "14:00",
  "duration": "00:30",
  "deal_id": 789,
  "person_id": 123,
  "note": "Discuss contract terms"
}
```

#### Update Activity
```bash
PUT /pipedrive/api/v1/activities/{id}
Content-Type: application/json

{
  "done": 1,
  "note": "Completed - customer agreed to terms"
}
```

#### Delete Activity
```bash
DELETE /pipedrive/api/v1/activities/{id}
```

### Pipelines
#### List Pipelines
```bash
GET /pipedrive/api/v1/pipelines
```

#### Get Pipeline
```bash
GET /pipedrive/api/v1/pipelines/{id}
```

### Stages
#### List Stages
```bash
GET /pipedrive/api/v1/stages
```

Query parameters:

* `pipeline_id` - Filter by pipeline

#### Get Stage
```bash
GET /pipedrive/api/v1/stages/{id}
```

### Notes
#### List Notes
```bash
GET /pipedrive/api/v1/notes
```

Query parameters:

* `deal_id` - Filter by deal
* `person_id` - Filter by person
* `org_id` - Filter by organization

#### Create Note
```bash
POST /pipedrive/api/v1/notes
Content-Type: application/json

{
  "content": "Meeting notes: Discussed pricing and timeline",
  "deal_id": 789,
  "pinned_to_deal_flag": 1
}
```

### Users
#### List Users
```bash
GET /pipedrive/api/v1/users
```

#### Get Current User
```bash
GET /pipedrive/api/v1/users/me
```

## 示例
### JavaScript

> 详细代码示例已移至 `references/detail.md`

### Python

> 详细代码示例已移至 `references/detail.md`

## Notes
* IDs are integers
* Email and phone fields accept arrays for multiple values
* `visible_to` values: 1 (owner only), 3 (entire company), 5 (owner's visibility group), 7 (entire company and visibility group)
* Deal status: `open`, `won`, `lost`, `deleted`
* Use `start` and `limit` for pagination
* Custom fields are supported via their API key (e.g., `abc123_custom_field`)
* IMPORTANT: When using curl commands, use `curl -g` when URLs contain brackets (`fields[]`, `sort[]`, `records[]`) to disable glob parsing
* IMPORTANT: When piping curl output to `jq` or other commands, environment variables like `$MATON_API_KEY` may not expand correctly in some shell environments. You may get "Invalid API key" errors when piping.

## Error Handling
| Status | Meaning |
| --- | --- |
| 400 | Missing Pipedrive connection |
| 401 | Invalid or missing Maton API key |
| 404 | Resource not found |
| 429 | Rate limited (10 req/sec per account) |
| 4xx/5xx | Passthrough error from Pipedrive API |

### 错误处理
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
1. Ensure your URL path starts with `pipedrive`. For example:

* Correct: `https://api.maton.ai/pipedrive/api/v1/deals`
* Incorrect: `https://api.maton.ai/api/v1/deals`

## Resources
* [Pipedrive API Overview](https://developers.pipedrive.com/docs/api/v1)
* [Deals](https://developers.pipedrive.com/docs/api/v1/Deals)
* [Persons](https://developers.pipedrive.com/docs/api/v1/Persons)
* [Organizations](https://developers.pipedrive.com/docs/api/v1/Organizations)
* [Activities](https://developers.pipedrive.com/docs/api/v1/Activities)
* [Pipelines](https://developers.pipedrive.com/docs/api/v1/Pipelines)
* [Stages](https://developers.pipedrive.com/docs/api/v1/Stages)
* [Notes](https://developers.pipedrive.com/docs/api/v1/Notes)
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
- Pipedrive API integration with managed OAuth
- Manage deals, persons,
  organizations, activities, a
- 触发关键词: api, managed, integration, oauth, pipedrive

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题
### Q1: 如何开始使用Pipedrive？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Pipedrive有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
