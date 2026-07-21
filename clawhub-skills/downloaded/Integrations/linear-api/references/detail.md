# 详细参考 - linear-api

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import os
import requests

response = requests.post(
    'https://api.maton.ai/linear/graphql',
    headers={
        'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}',
        'Content-Type': 'application/json'
    },
    json={
        'query': '{ issues(first: 10) { nodes { id identifier title state { name } } } }'
    }
)
data = response.json()
```

### Issues
#### List Issues
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ issues(first: 10, filter: { team: { key: { eq: \"ABC\" } } }) { nodes { id identifier title state { name } priority createdAt } pageInfo { hasNextPage endCursor } } }"}
```

Example:

```bash
maton linear issue list -c ABC -L 10
```

#### Get Issue by ID or Identifier
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ issue(id: \"ABC-123\") { id identifier title description state { name } priority assignee { name } team { key name } createdAt updatedAt } }"}
```

Example:

```bash
maton linear issue view ABC-123
```

#### Filter Issues
Filter by state type:

```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ issues(first: 10, filter: { state: { type: { eq: \"started\" } } }) { nodes { id identifier title state { name type } } } }"}
```

Example:

```bash
maton linear issue list --state started -L 10
```

Filter by title:

```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ issues(first: 10, filter: { title: { containsIgnoreCase: \"bug\" } }) { nodes { id identifier title } } }"}
```

Example:

```bash
maton linear issue list --title bug -L 10
```

#### Search Issues
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ searchIssues(first: 10, term: \"shopify\") { nodes { id identifier title } } }"}
```

Example:

```bash
maton linear issue search shopify -L 10
```

#### Create Issue
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "mutation { issueCreate(input: { teamId: \"TEAM_ID\", title: \"New issue title\" }) { success issue { id identifier title state { name } } } }"}
```

Example:

```bash
maton linear issue create --team-id TEAM_ID -t 'New issue title'
```

#### Update Issue
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "mutation { issueUpdate(id: \"ABC-123\", input: { title: \"Updated title\", priority: 2 }) { success issue { id identifier title priority } } }"}
```

Example:

```bash
maton linear issue update ABC-123 -t 'Updated title' --priority 2
```




## Quick Start
**CLI:**

```bash
maton linear issue list -c ABC -L 10
```

```bash
maton api '/linear/graphql'
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'query': '{ viewer { id name email } }'}).encode()
req = urllib.request.Request('https://api.maton.ai/linear/graphql', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

## Authentication
**CLI:**

```bash
maton login                          # Opens browser for API key
maton login --interactive            # Skip browser, paste API key directly
maton whoami                         # Show current auth state
```

**Manual:**

1. Sign in or create an account at [maton.ai](https://maton.ai)
2. Go to [maton.ai/settings](https://maton.ai/settings)
3. Copy your API key
4. Set your API key as `MATON_API_KEY`:

```bash
export MATON_API_KEY="[REDACTED]"
```



---

### List Connections
**CLI:**

```bash
maton connection list linear --status ACTIVE
```

```bash
maton api -X GET /connections -f app=linear -f status=ACTIVE
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections?app=linear&status=ACTIVE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

### Create Connection
**CLI:**

```bash
maton connection create linear
```

```bash
maton api /connections -f app=linear
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'app': 'linear'}).encode()
req = urllib.request.Request('https://api.maton.ai/connections', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

### Get Connection
**CLI:**

```bash
maton connection view {connection_id}
```

```bash
maton api /connections/{connection_id}
```

**Python:**

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
    "creation_time": "2026-02-04T23:03:22.676001Z",
    "last_updated_time": "2026-02-04T23:03:51.239577Z",
    "url": "https://connect.maton.ai/?session_token=...",
    "app": "linear",
    "metadata": {}
  }
}
```

Open the returned `url` in a browser to complete OAuth authorization.



---

### Delete Connection
**CLI:**

```bash
maton connection delete {connection_id}
```

```bash
maton api -X DELETE /connections/{connection_id}
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections/{connection_id}', method='DELETE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

### Specifying Connection
If you have multiple Linear connections, specify which one to use:

**CLI:**

```bash
maton linear issue list -c ABC --connection {connection_id}
```

```bash
maton api /linear/graphql --connection {connection_id}
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'query': '{ viewer { id name } }'}).encode()
req = urllib.request.Request('https://api.maton.ai/linear/graphql', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
req.add_header('Maton-Connection', '{connection_id}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

If you have multiple connections, always specify the connection to ensure requests go to the intended account.



---

### Teams
#### List Teams
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ teams { nodes { id name key } } }"}
```

Example:

```bash
maton linear team list
```

#### Get Team
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ team(id: \"ABC\") { id name key issues { nodes { id identifier title } } } }"}
```

Example:

```bash
maton linear team view ABC
```

> 详细内容已移至 `references/detail.md` - ### Issues


---

### Comments
#### List Comments
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "{ issue(id: \"ABC-123\") { comments(first: 10) { nodes { id body createdAt user { name } } } } }"}
```

Example:

```bash
maton linear comment list --issue ABC-123 -L 10
```

#### Create Comment
```bash
POST /linear/graphql
Content-Type: application/json

{"query": "mutation { commentCreate(input: { issueId: \"ABC-123\", body: \"Looking into this\" }) { success comment { id body } } }"}
```

Example:

```bash
maton linear comment create --issue ABC-123 -b 'Looking into this'
```



---

## Error Handling
| Status | Meaning |
| --- | --- |
| 400 | Missing Linear connection or GraphQL validation error |
| 401 | Invalid or missing Maton API key |
| 403 | Insufficient OAuth scope for the operation |
| 429 | Rate limited |
| 4xx/5xx | Passthrough error from Linear API |

GraphQL errors are returned in the `errors` array:

```json
{
  "errors": [
    {
      "message": "Invalid scope: `write` required",
      "extensions": {
        "type": "forbidden",
        "code": "FORBIDDEN",
        "statusCode": 403
      }
    }
  ]
}
```



---
