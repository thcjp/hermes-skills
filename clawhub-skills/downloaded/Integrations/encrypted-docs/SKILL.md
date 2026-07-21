---
slug: encrypted-docs
name: encrypted-docs
version: "1.0.0"
displayName: Encrypted Docs
  This is a multiplayer alternative to gog and Google Docs that lets people (via CLI)
  and agents create, search and sync encrypted markdown docs. This service leverages
  https://ddocs.new which can be enabled locally or via your preferred cloud set-up
  to make docs accessible across any device or chatbot interface in complete privacy.
summary: End-to-end encrypted .md documents for agents & humans to collaborate. This
  is a multiplayer alte...
license: MIT
description: |-
  End-to-end encrypted 。md documents for agents & humans to collaborate。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。
tags:
- Integrations
- Security
tools:
  - - read
- exec
---

# End-to-end encrypted .md documents for agents & humans to collaborate. This is a multiplayer alternative to gog and Google Docs that lets people (via CLI) and agents create, search and sync encrypted markdown docs. This service leverages https://ddocs.new which can be enabled locally or via your preferred cloud set-up to make docs accessible across any device or chatbot interface in complete privacy.

> End-to-end encrypted .md documents for agents & humans to collaborate. This is a multiplayer alternative to gog and Google Docs that lets people (via CLI) and agents create, search and sync encrypted markdown docs. This service leverages <https://ddocs.new> which can be enabled locally or via your preferred cloud set-up to make docs accessible across any device or chatbot interface in complete privacy.

Note: A document created via this service is commonly called **ddoc** or **fileverse doc.** Each document has a unique randomly generated `ddocId`.

## Agents - Setup (Device)

There are different ways to connect to the Fileverse API. First, you need to get the `<SERVER_URL>` from the user.

### MCP

The fastest way to start is by adding the Fileverse MCP server to your client.

#### Claude Code

```bash
claude mcp add --transport http fileverse-api <SERVER_URL>
```

#### Cursor

Add this to your `~/.cursor/config/mcp.json`:

```json
{
  "mcpServers": {
    "fileverse-api": {
      "type": "streamable-http",
      "url": "<SERVER_URL>"
    }
  }
}
```

#### Windsurf

Add this to your MCP config:

```json
{
  "mcpServers": {
    "fileverse-api": {
      "type": "streamable-http",
      "url": "<SERVER_URL>"
    }
  }
}
```

Note: if for some reason MCP is not supported you can fallback to API and check the documentation on the guide.md for exact API Docs.

---

## Agents - Setup (Browser)

### MCP

#### ChatGPT

ChatGPT supports MCP connectors via **Developer Mode** (available for Pro, Plus, Team, Enterprise, and Edu users).

**Setup steps:**

1. Open ChatGPT > Settings > Apps > Advanced > toggle Developer Mode on
2. Go to Settings > Apps > click Create
3. Fill in:

   * Name: API Encrypted Docs
   * Server URL: `https://<your-server-url>/` (e.g. `https://abc123.ngrok.app/mcp`)
4. Check **"I trust this provider"**
5. Click **Create**

**Using in a chat:**

1. Start a new chat
2. Ask it to create a .md file and store it on Fileverse

#### Claude (Web)

1. Open Claude > Settings > Connector > Add Custom Connector
2. Fill in:

   * Name: API Encrypted Docs
   * Server URL: `https://<your-server-url>/` (e.g. `https://abc123.ngrok.app/`)
3. Click **Add**

---

## MCP Tools Reference

The Fileverse MCP server exposes **8 tools**. All tools return JSON responses.

### fileverse_list_documents

List documents stored in Fileverse. Returns an array of documents with their metadata and sync status.

**Parameters:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| limit | number | No | Maximum number of documents to return (default: 10) |
| skip | number | No | Number of documents to skip (for pagination) |

**Returns:**

```json
{
  "ddocs": [{ "ddocId": "...", "title": "...", "content": "...", "syncStatus": "synced", "link": "..." }],
  "total": 42,
  "hasNext": true
}
```

**Usage notes:**

* Use `skip` and `limit` to paginate through large document sets
* Check `hasNext` to determine if more documents are available
* Documents are returned with full metadata including `syncStatus` and `link`

---

### fileverse_get_document

Get a single document by its `ddocId`. Returns the full document including content, sync status, and content hash.

**Parameters:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| ddocId | string | Yes | The unique document identifier |

**Returns:**

```json
{
  "ddocId": "abc123",
  "title": "My Document",
  "content": "# Hello World\n\nThis is my document.",
  "syncStatus": "synced",
  "link": "https://ddocs.new/d/abc123#encryptionKey",
  "localVersion": 3,
  "onchainVersion": 3,
  "createdAt": "2025-01-01T00:00:00.000Z",
  "updatedAt": "2025-01-02T00:00:00.000Z"
}
```

**Usage notes:**

* The `link` field is only available when `syncStatus` is `"synced"`
* The link contains an encryption key fragment after `#` for end-to-end encryption

---

### fileverse_create_document

Create a new document and wait for syncing. Returns the document with its sync status and public link once synced.

**Parameters:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| title | string | Yes | Document title |
| content | string | Yes | Document content (plain text or markdown) |

**Returns:**

```json
{
  "ddocId": "newDoc123",
  "title": "My New Document",
  "content": "...",
  "syncStatus": "synced",
  "link": "https://ddocs.new/d/newDoc123#encryptionKey"
}
```

**Usage notes:**

* This tool **blocks** until the document is synced to decentralized storage networks (up to 60 seconds)
* Content supports full markdown syntax
* The returned `link` is a shareable, encrypted URL to view the document on ddocs.new
* If sync takes too long, the tool returns with `syncStatus: "pending"` - use `fileverse_get_sync_status` to poll later

---

### fileverse_update_document

Update an existing document's title and/or content, then wait for the syncing with decentralized storage networks.

**Parameters:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| ddocId | string | Yes | The unique document identifier |
| title | string | No | New document title |
| content | string | No | New document content |

At least one of `title` or `content` must be provided.

**Returns:** Updated document object with sync status and link.

**Usage notes:**

* This tool **blocks** until the update is synced to the decentralized storage networks (up to 60 seconds)
* Only provided fields are updated; omitted fields remain unchanged
* Each update increments the `localVersion`

---

### fileverse_delete_document

Delete a document by its `ddocId`.

**Parameters:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| ddocId | string | Yes | The unique document identifier to delete |

**Returns:**

```json
{
  "message": "Document deleted successfully",
  "data": { "ddocId": "abc123", "..." }
}
```

**Usage notes:**

* Deletion is permanent
* The document's decentralized storage networks’ (including a public blockchain for content hash registry) record will also be updated

---

### fileverse_search_documents

Search documents by text query. Returns matching documents ranked by relevance.

**Parameters:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| query | string | Yes | Search query string |
| limit | number | No | Maximum number of results (default: 10) |
| skip | number | No | Number of results to skip |

**Returns:**

```json
{
  "nodes": [{ "ddocId": "...", "title": "...", "content": "...", "syncStatus": "..." }],
  "total": 5,
  "hasNext": false
}
```

**Usage notes:**

* Searches across document titles and content
* Results are ranked by relevance
* Use `skip` and `limit` for pagination

---

### fileverse_get_sync_status

Check the sync status of a document. Returns the current syncStatus and link if synced.

**Parameters:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| ddocId | string | Yes | The unique document identifier |

**Returns:**

```json
{
  "ddocId": "abc123",
  "syncStatus": "synced",
  "link": "https://ddocs.new/d/abc123#encryptionKey",
  "localVersion": 3,
  "onchainVersion": 3
}
```

**Usage notes:**

* `syncStatus` can be: `"pending"`, `"synced"`, or `"failed"`
* Use this to poll for sync completion after create/update operations
* `localVersion` vs `onchainVersion` shows if there are unsynced changes

---

### fileverse_retry_failed_events

Retry all failed decentralized storage networks sync events. Use this when documents are stuck in `"failed"` sync status.

**Parameters:** None

**Returns:**

```json
{
  "retried": 3
}
```

**Usage notes:**

* Call this when you notice documents with `syncStatus: "failed"`
* Returns the count of events that were retried
* Events have a maximum of 10 retry attempts before being permanently marked as failed
* Failed events are typically caused by decentralized storage networks (including a public blockchain) rate limits or transient network errors

---

## Document Sync Lifecycle

Understanding the sync lifecycle helps agents work effectively:

```plaintext
Create/Update → syncStatus: "pending" →  decentralized storage networks sync → syncStatus: "synced"
                                                        → syncStatus: "failed" (retry with fileverse_retry_failed_events)
```

1. **pending** - Document saved locally, waiting for decentralized storage networks sync
2. **synced** - Document is on-chain and has a shareable `link`
3. **failed** - Sync failed (rate limit, network error). Use `fileverse_retry_failed_events` to retry

The `create` and `update` tools automatically poll for up to 60 seconds. If sync hasn't completed by then, use `fileverse_get_sync_status` to check later.

---

## Constraints & Limits

| Constraint | Value |
| --- | --- |
| Max file upload size | 10 MB |
| Default page size | 10 documents |
| Sync polling timeout | 60 seconds |
| Sync poll interval | 3 seconds |
| Max event retries | 10 attempts |
| Worker concurrency | 5 concurrent events |

---

## Agents - Use

### Common Patterns

**Creating documents from local files:**

* "Upload this README to a ddoc"
* "Sync my notes.md to Fileverse"
* "Create a ddoc from this file"

**Generating new content:**

* "Create a ddoc that explains and documents this codebase"
* "Write a design doc for [feature] and save it as a ddoc"
* "Create a ddoc summarizing today's meeting notes"

**Managing existing documents:**

* "List all my ddocs"
* "Search my ddocs for anything about authentication"
* "Update my project roadmap ddoc with the latest changes"
* "Delete the old draft ddoc"
* "What's the sync status of my latest document?"

**Sharing:**

* “Sync these ddocs across all my agents for shared context and memory”
* "Create a ddoc and give me the link"
* "Get the shareable link for my [document name] ddoc"
* “Collaborate with these people on my [document name] ddoc”

### Best Practices for Agents

1. **Always return the link** - After creating or updating a document, return the `link` field to the user so they can view/share it
2. **Use search before creating** - If the user wants to update something, search first to find the existing document instead of creating a duplicate
3. **Handle sync failures** - If a document's `syncStatus` is `"failed"`, call `fileverse_retry_failed_events` and inform the user
4. **Paginate large result sets** - Use `skip` and `limit` when listing documents to avoid loading everything at once
5. **Use markdown** - Content supports full markdown. Format documents with proper headings, lists, code blocks, and tables
6. **Check sync status** - If create/update returns with `syncStatus: "pending"`, poll with `fileverse_get_sync_status` until it's `"synced"` before giving the user the link
7. **Create a skill** - It's recommended for LLMs to create a skill/shortcut for common Fileverse operations to make it easier for users to interact with the API (e.g., `/ddoc create`, `/ddoc list`)

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

- End-to-end encrypted
- md documents for agents & humans to collaborate
- This is a multiplayer alte
- 触发关键词: leverages, sync, set-up, (via, gog, https:, interface, accessible

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

### Q1: 如何开始使用Encrypted Docs？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Encrypted Docs有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
