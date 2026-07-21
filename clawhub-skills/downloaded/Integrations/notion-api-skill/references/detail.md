# 详细参考 - notion-api-skill

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (bash)

```bash
PATCH /notion/v1/blocks/{blockId}/children
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "children": [
    {
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{"type": "text", "text": {"content": "New paragraph"}}]
      }
    }
  ]
}
```

## 代码示例 (bash)

```bash
POST /notion/v1/data_sources/{dataSourceId}/query
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "filter": {
    "property": "Status",
    "select": {"equals": "Active"}
  },
  "sorts": [
    {"property": "Created", "direction": "descending"}
  ],
  "page_size": 100
}
```

### Pages
#### Get Page
```bash
GET /notion/v1/pages/{pageId}
Notion-Version: 2025-09-03
```

Example:

```bash
maton notion page view <pageId>
```

#### Create Page
```bash
POST /notion/v1/pages
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "parent": {"page_id": "PARENT_PAGE_ID"},
  "properties": {
    "title": {"title": [{"text": {"content": "New Page"}}]}
  }
}
```

Example:

```bash
maton notion page create --parent-page PARENT_PAGE_ID --title 'New Page'
```

#### Create Page in Data Source
```bash
POST /notion/v1/pages
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "parent": {"data_source_id": "DATA_SOURCE_ID"},
  "properties": {
    "Name": {"title": [{"text": {"content": "New Page"}}]},
    "Status": {"select": {"name": "Active"}}
  }
}
```

Example:

```bash
maton notion page create --data-source DATA_SOURCE_ID --title 'New Page' \
  --properties '{"Status":{"select":{"name":"Active"}}}'
```

#### Update Page Properties
```bash
PATCH /notion/v1/pages/{pageId}
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "properties": {
    "Status": {"select": {"name": "Done"}}
  }
}
```

Example:

```bash
maton notion page update {pageId} --properties '{"Status":{"select":{"name":"Done"}}}'
```

#### Update Page Icon
```bash
PATCH /notion/v1/pages/{pageId}
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "icon": {"type": "emoji", "emoji": "🚀"}
}
```

Example:

```bash
maton notion page update {pageId} --icon 🚀
```

Or with an image URL:

```bash
maton notion page update {pageId} --icon https://example.com/icon.png
```

#### Archive Page
```bash
PATCH /notion/v1/pages/{pageId}
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "archived": true
}
```

Example:

```bash
maton notion page archive {pageId}
```



### Data Sources
#### Get Data Source
```bash
GET /notion/v1/data_sources/{dataSourceId}
Notion-Version: 2025-09-03
```

Example:

```bash
maton notion data-source view <dataSourceId>
```

#### Query Data Source
```bash
POST /notion/v1/data_sources/{dataSourceId}/query
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "filter": {
    "property": "Status",
    "select": {"equals": "Active"}
  },
  "sorts": [
    {"property": "Created", "direction": "descending"}
  ],
  "page_size": 100
}
```

Example:

```bash
maton notion data-source query <dataSourceId> \
  --filter '{"property":"Status","select":{"equals":"Active"}}' \
  --sorts '[{"property":"Created","direction":"descending"}]' \
  --page-size 100
```

#### Update Data Source
```bash
PATCH /notion/v1/data_sources/{dataSourceId}
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "title": [{"type": "text", "text": {"content": "Updated Title"}}],
  "properties": {
    "NewColumn": {"rich_text": {}}
  }
}
```

Example:

```bash
maton notion data-source update <dataSourceId> \
  --body '{"title":[{"type":"text","text":{"content":"Updated Title"}}],"properties":{"NewColumn":{"rich_text":{}}}}'
```



### Blocks
#### Get Block Children
```bash
GET /notion/v1/blocks/{blockId}/children
Notion-Version: 2025-09-03
```

Example:

```bash
maton notion block children <blockId>
```

#### Append Block Children
```bash
PATCH /notion/v1/blocks/{blockId}/children
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "children": [
    {
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{"type": "text", "text": {"content": "New paragraph"}}]
      }
    }
  ]
}
```

Example:

```bash
maton notion block append <blockId> \
  --children '[{"object":"block","type":"paragraph","paragraph":{"rich_text":[{"type":"text","text":{"content":"New paragraph"}}]}}]'
```

#### Delete Block
```bash
DELETE /notion/v1/blocks/{blockId}
Notion-Version: 2025-09-03
```

Example:

```bash
maton notion block delete <blockId>
```




## Quick Start
**CLI:**

```bash
maton notion search 'meeting notes'
```

```bash
maton api '/notion/v1/search'
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'query': 'meeting notes'}).encode()
req = urllib.request.Request('https://api.maton.ai/notion/v1/search', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
req.add_header('Notion-Version', '2025-09-03')
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
maton connection list notion --status ACTIVE
```

```bash
maton api -X GET /connections -f app=notion -f status=ACTIVE
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections?app=notion&status=ACTIVE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

### Create Connection
**CLI:**

```bash
maton connection create notion
```

```bash
maton api /connections -f app=notion
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'app': 'notion'}).encode()
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
    "app": "notion",
    "method": "OAUTH2",
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
If you have multiple Notion connections, specify which one to use:

**CLI:**

```bash
maton notion search 'meeting notes' --connection {connection_id}
```

```bash
maton api /notion/v1/search --connection {connection_id}
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'query': 'meeting notes'}).encode()
req = urllib.request.Request('https://api.maton.ai/notion/v1/search', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
req.add_header('Notion-Version', '2025-09-03')
req.add_header('Maton-Connection', '{connection_id}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

If you have multiple connections, always specify the connection to ensure requests go to the intended account.



---

## Key Concept: Databases vs Data Sources
In API version 2025-09-03, databases and data sources are separate:

| Concept | Use For |
| --- | --- |
| **Database** | Creating databases, getting data source IDs |
| **Data Source** | Querying, updating schema, updating properties |

Use `GET /databases/{id}` to get the `data_sources` array, then use `/data_sources/` endpoints:

```json
{
  "object": "database",
  "id": "abc123",
  "data_sources": [
    {"id": "def456", "name": "My Database"}
  ]
}
```



---

### Search
Search for pages:

```bash
POST /notion/v1/search
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "query": "meeting notes",
  "filter": {"property": "object", "value": "page"}
}
```

Example:

```bash
maton notion search 'meeting notes' --filter page
```

Search for data sources:

```bash
POST /notion/v1/search
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "filter": {"property": "object", "value": "data_source"}
}
```

Example:

```bash
maton notion search --filter data_source
```

> 详细内容已移至 `references/detail.md` - ### Data Sources


---

### Databases
#### Get Database
```bash
GET /notion/v1/databases/{databaseId}
Notion-Version: 2025-09-03
```

Example:

```bash
maton notion database view <databaseId>
```

#### Create Database
```bash
POST /notion/v1/databases
Content-Type: application/json
Notion-Version: 2025-09-03

{
  "parent": {"type": "page_id", "page_id": "PARENT_PAGE_ID"},
  "title": [{"type": "text", "text": {"content": "New Database"}}],
  "properties": {
    "Name": {"title": {}}
  }
}
```

Example:

```bash
maton notion database create --parent-page PARENT_PAGE_ID --title 'New Database'
```

In API version 2025-09-03, `POST /databases` only accepts the title property — any other entries in `properties` are silently dropped. To define a schema, follow up with `PATCH /data_sources/{dataSourceId}` (see [Update Data Source](#update-data-source)) using the `data_sources[0].id` returned by the create call.



---

### Users
#### List Users
```bash
GET /notion/v1/users
Notion-Version: 2025-09-03
```

Example:

```bash
maton notion user list
```

#### Get Current User
```bash
GET /notion/v1/users/me
Notion-Version: 2025-09-03
```

Example:

```bash
maton notion whoami
```



---
