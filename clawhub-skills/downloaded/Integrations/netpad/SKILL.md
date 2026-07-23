---
pricing_tier: L4
pricing_model: monthly
suggested_price: 99.9
---

# NetPad - Build forms, workflows and manage MongoDB data
Manage forms, submissions, users, and RBAC via CLI and REST API.

## Two Tools
| Tool | Install | Purpose |
| --- | --- | --- |
| `netpad` CLI | `npm i -g @netpad/cli` | RBAC, marketplace, packages |
| REST API | curl + API key | Forms, submissions, data |

## Authentication
```bash
export NETPAD_API_KEY="[REDACTED]"  # Production
export NETPAD_API_KEY="[REDACTED]"  # Test (can submit to drafts)
```

All requests use Bearer token:

```bash
curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/..."
```

---

## Quick Reference
| Task | Endpoint | Method |
| --- | --- | --- |
| List projects | `/projects` | GET |
| List forms | `/forms` | GET |
| Create form | `/forms` | POST |
| Get form | `/forms/{formId}` | GET |
| Update/publish form | `/forms/{formId}` | PATCH |
| Delete form | `/forms/{formId}` | DELETE |
| List submissions | `/forms/{formId}/submissions` | GET |
| Create submission | `/forms/{formId}/submissions` | POST |
| Get submission | `/forms/{formId}/submissions/{id}` | GET |
| Delete submission | `/forms/{formId}/submissions/{id}` | DELETE |

---

## Projects
Forms belong to projects. Get project ID before creating forms.

```bash
curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/projects" | jq '.data[] | {projectId, name}'
```

---

## Forms
### List Forms
```bash
curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms?status=published&pageSize=50"
```

### Create Form
```bash
curl -X POST -H "Authorization: Bearer $NETPAD_API_KEY" \
  -H "Content-Type: application/json" \
  "https://www.netpad.io/api/v1/forms" \
  -d '{
    "name": "Contact Form",
    "description": "Simple contact form",
    "projectId": "proj_xxx",
    "fields": [
      {"path": "name", "label": "Name", "type": "text", "required": true},
      {"path": "email", "label": "Email", "type": "email", "required": true},
      {"path": "phone", "label": "Phone", "type": "phone"},
      {"path": "message", "label": "Message", "type": "textarea"}
    ]
  }'
```

### Get Form Details
```bash
curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms/{formId}"
```

### Publish Form
```bash
curl -X PATCH -H "Authorization: Bearer $NETPAD_API_KEY" \
  -H "Content-Type: application/json" \
  "https://www.netpad.io/api/v1/forms/{formId}" \
  -d '{"status": "published"}'
```

### Update Form Fields
```bash
curl -X PATCH -H "Authorization: Bearer $NETPAD_API_KEY" \
  -H "Content-Type: application/json" \
  "https://www.netpad.io/api/v1/forms/{formId}" \
  -d '{
    "fields": [
      {"path": "name", "label": "Full Name", "type": "text", "required": true},
      {"path": "email", "label": "Email Address", "type": "email", "required": true},
      {"path": "company", "label": "Company", "type": "text"},
      {"path": "role", "label": "Role", "type": "select", "options": [
        {"value": "dev", "label": "Developer"},
        {"value": "pm", "label": "Product Manager"},
        {"value": "exec", "label": "Executive"}
      ]}
    ]
  }'
```

### Delete Form
```bash
curl -X DELETE -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms/{formId}"
```

---

## Submissions
### Submit Data
```bash
curl -X POST -H "Authorization: Bearer $NETPAD_API_KEY" \
  -H "Content-Type: application/json" \
  "https://www.netpad.io/api/v1/forms/{formId}/submissions" \
  -d '{
    "data": {
      "name": "John Doe",
      "email": "john@example.com",
      "message": "Hello from the API!"
    }
  }'
```

### List Submissions
```bash
curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms/{formId}/submissions?pageSize=50"

curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms/{formId}/submissions?startDate=2026-01-01T00:00:00Z"

curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms/{formId}/submissions?sortOrder=asc"
```

### Get Single Submission
```bash
curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms/{formId}/submissions/{submissionId}"
```

### Delete Submission
```bash
curl -X DELETE -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms/{formId}/submissions/{submissionId}"
```

---

## Field Types
| Type | Description | Validation |
| --- | --- | --- |
| `text` | Single line text | minLength, maxLength, pattern |
| `email` | Email address | Built-in validation |
| `phone` | Phone number | Built-in validation |
| `number` | Numeric input | min, max |
| `date` | Date picker | - |
| `select` | Dropdown | options: [{value, label}] |
| `checkbox` | Boolean | - |
| `textarea` | Multi-line text | minLength, maxLength |
| `file` | File upload | - |

### Field Schema
```json
{
  "path": "fieldName",
  "label": "Display Label",
  "type": "text",
  "required": true,
  "placeholder": "Hint text",
  "helpText": "Additional guidance",
  "options": [{"value": "a", "label": "Option A"}],
  "validation": {
    "minLength": 1,
    "maxLength": 500,
    "pattern": "^[A-Z].*",
    "min": 0,
    "max": 100
  }
}
```

---

## Common Patterns
### Create and Publish Form
```bash
RESULT=$(curl -s -X POST -H "Authorization: Bearer $NETPAD_API_KEY" \
  -H "Content-Type: application/json" \
  "https://www.netpad.io/api/v1/forms" \
  -d '{"name":"Survey","projectId":"proj_xxx","fields":[...]}')
FORM_ID=$(echo $RESULT | jq -r '.data.id')

curl -X PATCH -H "Authorization: Bearer $NETPAD_API_KEY" \
  -H "Content-Type: application/json" \
  "https://www.netpad.io/api/v1/forms/$FORM_ID" \
  -d '{"status":"published"}'
```

### Export All Submissions
```bash
curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms/{formId}/submissions?pageSize=1000" \
  | jq '.data[].data'
```

### Bulk Submit
```bash
for row in $(cat data.json | jq -c '.[]'); do
  curl -s -X POST -H "Authorization: Bearer $NETPAD_API_KEY" \
    -H "Content-Type: application/json" \
    "https://www.netpad.io/api/v1/forms/{formId}/submissions" \
    -d "{\"data\":$row}"
done
```

### Search Forms
```bash
curl -H "Authorization: Bearer $NETPAD_API_KEY" \
  "https://www.netpad.io/api/v1/forms?search=contact&status=published"
```

---

## Helper Script
Use `scripts/netpad.sh` for common operations:

```bash
chmod +x scripts/netpad.sh

./scripts/netpad.sh projects list
./scripts/netpad.sh forms list published
./scripts/netpad.sh forms create "Contact Form" proj_xxx
./scripts/netpad.sh forms publish frm_xxx
./scripts/netpad.sh submissions list frm_xxx
./scripts/netpad.sh submissions create frm_xxx '{"name":"John","email":"john@example.com"}'
./scripts/netpad.sh submissions export frm_xxx > data.jsonl
./scripts/netpad.sh submissions count frm_xxx
```

---

## Rate Limits
| Limit | Value |
| --- | --- |
| Requests/hour | 1,000 |
| Requests/day | 10,000 |

Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

---

## Response Format
### Success
```json
{
  "success": true,
  "data": { ... },
  "pagination": {"total": 100, "page": 1, "pageSize": 20, "hasMore": true},
  "requestId": "uuid"
}
```

### Error
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Description",
    "details": {}
  },
  "requestId": "uuid"
}
```

---

## Environment Variables
```bash
export NETPAD_API_KEY="[REDACTED]"

export NETPAD_BASE_URL="https://staging.netpad.io/api/v1"
```

---

## NetPad CLI (@netpad/cli)
Install: `npm i -g @netpad/cli`

### Authentication
```bash
netpad login              # Opens browser
netpad whoami             # Check auth status
netpad logout             # Clear credentials
```

### Marketplace & Packages
```bash
netpad search "helpdesk"

netpad install @netpad/helpdesk-app

netpad list

netpad create-app my-app

netpad submit ./my-app
```

### RBAC - Users
```bash
netpad users list -o org_xxx

netpad users add user@example.com -o org_xxx --role member

netpad users update user@example.com -o org_xxx --role admin

netpad users remove user@example.com -o org_xxx
```

### RBAC - Groups
```bash
netpad groups list -o org_xxx

netpad groups create "Engineering" -o org_xxx

netpad groups add-member grp_xxx user@example.com -o org_xxx

netpad groups delete grp_xxx -o org_xxx
```

### RBAC - Roles
```bash
netpad roles list -o org_xxx

netpad roles create "Reviewer" -o org_xxx --base viewer --description "Can review submissions"

netpad roles get role_xxx -o org_xxx

netpad roles delete role_xxx -o org_xxx
```

### RBAC - Assignments
```bash
netpad assign user user@example.com role_xxx -o org_xxx

netpad assign group grp_xxx role_xxx -o org_xxx

netpad unassign user user@example.com role_xxx -o org_xxx
```

### RBAC - Permissions
```bash
netpad permissions list -o org_xxx

netpad permissions check user@example.com -o org_xxx
```

---

## References
* `references/api-endpoints.md` — Complete REST API endpoint docs
* `references/cli-commands.md` — Full CLI command reference

---

## Author
**Michael Lynn** — Principal Staff Developer Advocate at MongoDB

* 🌐 Website: [mlynn.org](https://mlynn.org)
* 🐙 GitHub: [@mrlynn](https://github.com/mrlynn)
* 💼 LinkedIn: [linkedin.com/in/mlynn](https://linkedin.com/in/mlynn)

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
- The skill appears to be a legitimate NetPad management tool, but it
  gives an agent powerful delet
- 触发关键词: legitimate, workflows, appears, build, mongodb, manage, data, forms,

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例
### 示例1：基础用法
```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Netpad？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Netpad有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
