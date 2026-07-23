---
slug: "notion-pages"
name: "notion-pages"
version: "0.1.1"
displayName: "Notion"
summary: "搜页面数据库/更新内容/管Notion工作区数据"
license: "Proprietary"
description: |-
  Search pages and databases, update content, and manage Notion workspace
  data from chat。Use this。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Productivity
  - Automation
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
---
# Notion

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Search pages and databases, update content, and manage Notion workspace | 支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Search pages and databases, update content, and manage Notion workspace
  data from chat
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

```bash
clawlink_call_tool --tool "notion_list_databases" --params '{}'

clawlink_call_tool --tool "notion_search" --params '{"query": "project notes"}'

clawlink_call_tool --tool "notion_get_page" --params '{"page_id": "PAGE_ID"}'
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| mode | string | 否 | 处理模式, 可选: json/text/markdown, 默认: 默认值 |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/（根据实际场景填充）`

## 错误处理
| Status / Error | Meaning |
| --- | --- |
| Tool not found | The tool name does not exist in the current catalog. Verify with `clawlink_list_tools --integration notion`. |
| Missing connection | Notion is not connected. Direct the user to <https://claw-link.dev/dashboard?add=notion>. |
| `object_not_found` | Page or database does not exist. Check the ID or search for the resource first. |
| `validation_error` | Invalid parameter or missing required field. Review the tool schema with `clawlink_describe_tool`. |
| `conflict_error` | Resource was modified concurrently. Retry or re-fetch the latest state. |
| Write rejected | User did not confirm a write action. Always confirm before executing writes. |

### 错误恢复步骤
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
> **处理方式**: 参考上表中的错误场景说明,按照对应建议进行处理和恢复。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

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

## 常见问题

### Q1: 如何开始使用Notion？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Notion有什么限制？
A: 

