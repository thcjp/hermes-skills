# 详细参考 - jira-api

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import os
import requests

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}'}

resources = requests.get(
    'https://api.maton.ai/jira/oauth/token/accessible-resources',
    headers=headers
).json()

cloud_id = resources[0]['id']

issues = requests.get(
    f'https://api.maton.ai/jira/ex/jira/{cloud_id}/rest/api/3/search/jql',
    headers=headers,
    params={'jql': 'project=KEY', 'maxResults': 10}
).json()
```

### Issues
#### Search Issues (JQL)
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/search/jql?jql=project%3DPROJ%20order%20by%20created%20DESC&maxResults=20&fields=summary,status,assignee
```

Example:

```bash
maton jira issue search 'project = PROJ order by created DESC' --cloud-id abc-123 --limit 20 --fields summary,status,assignee
```

#### Get Issue
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/issue/{issueIdOrKey}
```

Example:

```bash
maton jira issue view PROJ-123 --cloud-id abc-123
```

#### Create Issue
```bash
POST /jira/ex/jira/{cloudId}/rest/api/3/issue
Content-Type: application/json

{
  "fields": {
    "project": {"key": "PROJ"},
    "summary": "Fix login",
    "issuetype": {"name": "Task"}
  }
}
```

Example:

```bash
maton jira issue create --cloud-id abc-123 --project PROJ --summary 'Fix login' --type Task
```

#### Update Issue
```bash
PUT /jira/ex/jira/{cloudId}/rest/api/3/issue/{issueIdOrKey}
Content-Type: application/json

{
  "fields": {
    "summary": "Updated summary"
  }
}
```

Example:

```bash
maton jira issue update PROJ-123 --cloud-id abc-123 --summary 'Updated summary'
```

#### Delete Issue
```bash
DELETE /jira/ex/jira/{cloudId}/rest/api/3/issue/{issueIdOrKey}
```

Example:

```bash
maton jira issue delete PROJ-123 --cloud-id abc-123
```

#### Assign Issue
```bash
PUT /jira/ex/jira/{cloudId}/rest/api/3/issue/{issueIdOrKey}/assignee
Content-Type: application/json

{
  "accountId": "712020:5aff718e-6fe0-4548-82f4-f44ec481e5e7"
}
```

Example:

```bash
maton jira issue update PROJ-123 --cloud-id abc-123 --assignee 712020:5aff718e-6fe0-4548-82f4-f44ec481e5e7
```




## Quick Start
**CLI:**

```bash
maton jira issue search 'project = PROJ AND status = "In Progress"' --cloud-id abc-123
```

```bash
maton api '/jira/ex/jira/{cloudId}/rest/api/3/search/jql?jql=project%3DKEY&maxResults=10'
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/jira/oauth/token/accessible-resources')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF

python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/jira/ex/jira/{cloudId}/rest/api/3/search/jql?jql=project%3DKEY&maxResults=10')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

## Getting Cloud ID
Jira Cloud requires a cloud ID. Get it first:

```bash
GET /jira/oauth/token/accessible-resources
```

Example:

```bash
maton jira cloud list
```

Response:

```json
[{
  "id": "62909843-b784-4c35-b770-e4e2a26f024b",
  "url": "https://yoursite.atlassian.net",
  "name": "yoursite"
}]
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
maton connection list jira --status ACTIVE
```

```bash
maton api -X GET /connections -f app=jira -f status=ACTIVE
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections?app=jira&status=ACTIVE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

### Create Connection
**CLI:**

```bash
maton connection create jira
```

```bash
maton api /connections -f app=jira
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'app': 'jira'}).encode()
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
    "creation_time": "2025-12-08T07:20:53.488460Z",
    "last_updated_time": "2026-01-31T20:03:32.593153Z",
    "url": "https://connect.maton.ai/?session_token=...",
    "app": "jira",
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
If you have multiple Jira connections, specify which one to use:

**CLI:**

```bash
maton jira project list --cloud-id abc-123 --connection {connection_id}
```

```bash
maton api /jira/ex/jira/{cloudId}/rest/api/3/project --connection {connection_id}
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/jira/ex/jira/{cloudId}/rest/api/3/project')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Maton-Connection', '{connection_id}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

If you have multiple connections, always specify the connection to ensure requests go to the intended account.



---

### Projects
#### List Projects
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/project
```

Example:

```bash
maton jira project list --cloud-id abc-123
```

#### Get Project
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/project/{projectKeyOrId}
```

Example:

```bash
maton jira project view PROJ --cloud-id abc-123
```

> 详细内容已移至 `references/detail.md` - ### Issues


---

### Transitions
#### Get Transitions
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/issue/{issueIdOrKey}/transitions
```

Example:

```bash
maton jira transition list PROJ-123 --cloud-id abc-123
```

#### Transition Issue (change status)
```bash
POST /jira/ex/jira/{cloudId}/rest/api/3/issue/{issueIdOrKey}/transitions
Content-Type: application/json

{
  "transition": {"id": "31"}
}
```

Example:

```bash
maton jira transition apply PROJ-123 --cloud-id abc-123 --id 31
```



---

### Comments
#### Get Comments
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/issue/{issueIdOrKey}/comment
```

Example:

```bash
maton jira comment list PROJ-123 --cloud-id abc-123
```

#### Add Comment
```bash
POST /jira/ex/jira/{cloudId}/rest/api/3/issue/{issueIdOrKey}/comment
Content-Type: application/json

{
  "body": {
    "type": "doc",
    "version": 1,
    "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Comment text"}]}]
  }
}
```

Example:

```bash
maton jira comment add PROJ-123 --cloud-id abc-123 --body 'Comment text'
```



---

### Users
#### Get Current User
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/myself
```

Example:

```bash
maton jira whoami --cloud-id abc-123
```

#### Search Users
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/user/search?query=john
```

Example:

```bash
maton jira user search john --cloud-id abc-123
```



---

### Metadata
#### List Issue Types
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/issuetype
```

Example:

```bash
maton jira issuetype list --cloud-id abc-123
```

#### List Priorities
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/priority
```

Example:

```bash
maton jira priority list --cloud-id abc-123
```

#### List Statuses
```bash
GET /jira/ex/jira/{cloudId}/rest/api/3/status
```

Example:

```bash
maton jira status list --cloud-id abc-123
```



---
