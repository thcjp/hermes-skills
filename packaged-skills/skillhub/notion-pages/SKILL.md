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

## 核心能力

- Search pages and databases, update content, and manage Notion workspace
  data from chat
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Use、需要生成营销文案、写作内容、标题优化、内容创作时使用、不适用于纯技术文、档撰写、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
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

### 命令参数说明

1. `--strict-json`: 命令参数,用于指定操作选项
2. `--params`: 命令参数,用于指定操作选项
3. `-platform`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
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

## 已知限制

- 
- 
- 
