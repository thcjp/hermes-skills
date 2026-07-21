---
slug: notion-pages
name: notion-pages
version: "0.1.1"
displayName: Notion
summary: Search pages and databases, update content, and manage Notion workspace data
  from chat. Use this ...
license: MIT-0
description: |-
  Search pages and databases, update content, and manage Notion workspace
  data from chat。Use this。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
- Automation
tools:
  - - read
- exec
---

# Notion

Access Notion via the Notion API with OAuth authentication. Search pages and databases, read and update content, manage sections, and coordinate workspace workflows.

This skill uses [ClawLink](https://claw-link.dev) for hosted connection flows and credentials so you do not need to configure Notion API access yourself.

### Setup in 3 Steps

| Step 1: Install | Step 2: Pair Account | Step 3: Connect Notion |
| --- | --- | --- |
|  |  | *App-specific connection GIF coming soon* |
| Run the install command in Skill平台 | Sign in and approve the device | Open the dashboard and connect Notion |

## How It Works

```text
┌─────────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Skill平台      │────▶│   ClawLink   │────▶│    Notion API    │
│   (User Chat)   │     │   (OAuth)    │     │ │
└─────────────────┘     └──────────────┘     └──────────────────┘
          │                       │                       │
          │  1. Install Plugin │                       │
          │  2. Pair Device      │                       │
          │  3. Connect Notion    │                       │
          │                      │  4. Secure Token      │
          │                      │  5. Proxy Requests │
          │                      │                       │
          ▼ ▼                       ▼
    ┌──────────┐           ┌──────────┐           ┌──────────┐
    │  SKILL   │           │ Dashboard│           │  Notion  │
    │  File    │           │ Auth     │           │ Workspace│
    └──────────┘           └──────────┘           └──────────┘
```

## Install

Install the verified ClawLink plugin from SkillHub. After the user confirms, complete the full setup so ClawLink tools are visible in the next Skill平台 chat.

```bash
skill-platform plugins install SkillHub:clawlink-plugin
skill-platform config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
skill-platform gateway restart
```

Then tell the user: "Skill平台 has been restarted. Send `/new` as a standalone message to start a fresh chat, then ask for Notion again."

## Quick Start

```bash
clawlink_call_tool --tool "notion_list_databases" --params '{}'

clawlink_call_tool --tool "notion_search" --params '{"query": "project notes"}'

clawlink_call_tool --tool "notion_get_page" --params '{"page_id": "PAGE_ID"}'
```

## Authentication

All Notion tool calls are authenticated automatically by ClawLink using the user's connected Notion account.

**No API key is required in chat.** ClawLink stores the OAuth token securely and injects it into every Notion API request on the user's behalf.

### Getting Connected

1. Install the ClawLink plugin (see Install above).
2. Pair the plugin with `clawlink_begin_pairing` if it is not configured yet.
3. Open <https://claw-link.dev/dashboard?add=notion> and connect Notion.
4. Call `clawlink_list_integrations` to verify the connection is active.

## Connection Management

### List Connections

```bash
clawlink_list_integrations
```

**Response:** Returns all connected integrations. Look for `notion` in the list.

### Verify Connection

```bash
clawlink_list_tools --integration notion
```

**Response:** Returns the live tool catalog for Notion.

### Reconnect

If Notion tools are missing or the connection shows an error:

1. Direct the user to <https://claw-link.dev/dashboard?add=notion>
2. After they confirm, call `clawlink_list_integrations` to verify
3. Then call `clawlink_list_tools --integration notion`

## Security& Permissions

* Access is scoped to pages, databases, and content within the connected Notion workspace.
* **All write operations require explicit user confirmation.** Before executing any create, update, or delete call, confirm the target resource and intended effect with the user.
* Destructive actions (delete page, remove database entry) must be confirmed.

## Discovery Workflow

1. Call `clawlink_list_integrations` to confirm Notion is connected.
2. Call `clawlink_list_tools --integration notion` to see the live catalog.
3. Treat the returned list as the source of truth. Do not guess or assume what tools exist.
4. If the user describes a capability but the exact tool is unclear, call `clawlink_search_tools` with a short query and integration `notion`.
5. If no Notion tools appear, direct the user to <https://claw-link.dev/dashboard?add=notion>.

## Execution Workflow

```text
┌─────────────────────────────────────────────────────────────┐
│  READ OPERATIONS (Safe)                                     │
│  list → get → search → describe → call                      │
│                                                             │
│  Example: Search pages → Read content → Show results        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  WRITE OPERATIONS (Require Confirmation)                     │
│  list → get → describe → preview → confirm → call           │
│                                                             │
│  Example: Describe tool → Preview changes → User approves   │
│           → Execute update                                  │
└─────────────────────────────────────────────────────────────┘
```

1. For unfamiliar tools, ambiguous requests, or any write action, call `clawlink_describe_tool` first.
2. Use the returned guidance, schema, `whenToUse`, `askBefore`, `safeDefaults`, `examples`, and `followups` to shape the call.
3. Prefer read, list, search, and get operations before writes when that reduces ambiguity.
4. For writes or anything marked as requiring confirmation, call `clawlink_preview_tool` first.
5. Execute with `clawlink_call_tool`. Pass confirmation only after the preview matches the user's intent.
6. If the tool call fails, report the real error. Do not invent results or restate the failure as a missing capability unless the live catalog supports that conclusion.

## 示例

### Search pages

```bash
clawlink_call_tool --tool "notion_search" \
  --params '{
    "query": "meeting notes",
    "filter": {
      "property": "object",
      "value": "page"
    }
  }'
```

### Query a database

```bash
clawlink_call_tool --tool "notion_query_database" \
  --params '{
    "database_id": "DATABASE_ID",
    "filter": {
      "property": "Status",
      "select": {
        "equals": "In Progress"
      }
    },
    "sorts": [
      {
        "property": "Last edited time",
        "direction": "descending"
      }
    ]
  }'
```

### Create a page

```bash
clawlink_call_tool --tool "notion_create_page" \
  --params '{
    "parent": {
      "database_id": "DATABASE_ID"
    },
    "properties": {
      "Name": {
        "title": [
          {
            "text": {
              "content": "New Project Page"
            }
          }
        ]
      }
    },
    "children": [
      {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
          "rich_text": [
            {
              "text": {
                "content": "Overview"
              }
            }
          ]
        }
      }
    ]
  }'
```

## Notes

* Notion API has rate limits. Use exponential backoff when encountering 429 errors.
* Page and database IDs are UUIDs (e.g., `abc123-def456-...`). Use the full ID, not the human-readable page URL slug.
* Block content updates require the full block structure in the request body.
* Archived pages can be retrieved but may require specific filter conditions.

## Error Handling

| Status / Error | Meaning |
| --- | --- |
| Tool not found | The tool name does not exist in the current catalog. Verify with `clawlink_list_tools --integration notion`. |
| Missing connection | Notion is not connected. Direct the user to <https://claw-link.dev/dashboard?add=notion>. |
| `object_not_found` | Page or database does not exist. Check the ID or search for the resource first. |
| `validation_error` | Invalid parameter or missing required field. Review the tool schema with `clawlink_describe_tool`. |
| `conflict_error` | Resource was modified concurrently. Retry or re-fetch the latest state. |
| Write rejected | User did not confirm a write action. Always confirm before executing writes. |

### 错误处理

1. Check that the ClawLink plugin is installed:

   bash

   ```
   skill-platform plugins list
   ```
2. If the plugin is installed but tools are missing, tell the user to send `/new` as a standalone message to reload the catalog.
3. If a fresh chat does not help, run:

   bash

   ```
   skill-platform config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
   skill-platform gateway restart
   ```
4. After restart, tell the user to send `/new` again and retry.

### Troubleshooting: Invalid Tool Call

1. Ensure the integration slug is exactly `notion`.
2. Use `clawlink_describe_tool` to verify parameter names and types before calling.
3. For write operations, always call `clawlink_preview_tool` first.

## Resources

* [Notion API Documentation](https://developers.notion.com/)
* [Notion Integration Guide](https://www.notion.so/help/guides)
* ClawLink: <https://claw-link.dev>
* ClawLink Docs: <https://docs.claw-link.dev/skill-platform>
* ClawLink Verification: <https://claw-link.dev/verify>

## Related Skills

* [Google Docs](https://SkillHub.ai/hith3sh/google-docs-documents) — For Google Workspace document operations
* [Notion](https://SkillHub.ai/hith3sh/notion-workspace) — For this skill's native documentation

---

**Powered by [ClawLink](https://claw-link.dev)** — an integration hub for Skill平台

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

- Search pages and databases, update content, and manage Notion workspace
  data from chat
- 触发关键词: pages, databases, content, notion, update, search

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题

### Q1: 如何开始使用Notion？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Notion有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
