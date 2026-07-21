# 详细参考 - pipedrive-api

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (javascript)

```javascript
const headers = {
  'Authorization': `Bearer ${process.env.MATON_API_KEY}`
};

// List open deals
const deals = await fetch(
  'https://api.maton.ai/pipedrive/api/v1/deals?status=open',
  { headers }
).then(r => r.json());

// Create a deal
await fetch(
  'https://api.maton.ai/pipedrive/api/v1/deals',
  {
    method: 'POST',
    headers: { ...headers, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      title: 'New Deal',
      value: 10000,
      currency: 'USD'
    })
  }
);
```

## 代码示例 (python)

```python
import os
import requests

headers = {'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}'}

deals = requests.get(
    'https://api.maton.ai/pipedrive/api/v1/deals',
    headers=headers,
    params={'status': 'open'}
).json()

response = requests.post(
    'https://api.maton.ai/pipedrive/api/v1/deals',
    headers=headers,
    json={
        'title': 'New Deal',
        'value': 10000,
        'currency': 'USD'
    }
)
```

### Deals
#### List Deals
```bash
GET /pipedrive/api/v1/deals
```

Query parameters:

* `status` - Filter by status: `open`, `won`, `lost`, `deleted`, `all_not_deleted`
* `filter_id` - Filter ID to use
* `stage_id` - Filter by stage
* `user_id` - Filter by user
* `start` - Pagination start (default 0)
* `limit` - Items per page (default 100)
* `sort` - Sort field and order (e.g., `add_time DESC`)

**Example:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/pipedrive/api/v1/deals?status=open&limit=50')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

#### Get Deal
```bash
GET /pipedrive/api/v1/deals/{id}
```

#### Create Deal
```bash
POST /pipedrive/api/v1/deals
Content-Type: application/json

{
  "title": "New Enterprise Deal",
  "value": 50000,
  "currency": "USD",
  "person_id": 123,
  "org_id": 456,
  "stage_id": 1,
  "expected_close_date": "2025-06-30"
}
```

#### Update Deal
```bash
PUT /pipedrive/api/v1/deals/{id}
Content-Type: application/json

{
  "title": "Updated Deal Title",
  "value": 75000,
  "status": "won"
}
```

#### Delete Deal
```bash
DELETE /pipedrive/api/v1/deals/{id}
```

#### Search Deals
```bash
GET /pipedrive/api/v1/deals/search?term=enterprise
```



### Persons (Contacts)
#### List Persons
```bash
GET /pipedrive/api/v1/persons
```

Query parameters:

* `filter_id` - Filter ID
* `start` - Pagination start
* `limit` - Items per page
* `sort` - Sort field and order

#### Get Person
```bash
GET /pipedrive/api/v1/persons/{id}
```

#### Create Person
```bash
POST /pipedrive/api/v1/persons
Content-Type: application/json

{
  "name": "John Doe",
  "email": ["john@example.com"],
  "phone": ["+1234567890"],
  "org_id": 456,
  "visible_to": 3
}
```

#### Update Person
```bash
PUT /pipedrive/api/v1/persons/{id}
Content-Type: application/json

{
  "name": "John Smith",
  "email": ["john.smith@example.com"]
}
```

#### Delete Person
```bash
DELETE /pipedrive/api/v1/persons/{id}
```

#### Search Persons
```bash
GET /pipedrive/api/v1/persons/search?term=john
```



