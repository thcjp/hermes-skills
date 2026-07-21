---
slug: notion-api-skill
name: notion-api-skill
version: "1.0.11"
displayName: Notion
summary: Notion API integration with managed OAuth. Query databases, search pages,
  and read workspace cont...
license: MIT-0
description: |-
  Notion API integration with managed OAuth。Query databases, search pages,
  and read workspace cont。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
- Productivity
tools:
  - - read
- exec
# Notion
---
# Notion

## 核心能力

- Notion API integration with managed OAuth
- Query databases, search pages,
  and read workspace cont
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

本skill还覆盖以下能力场景: Use、需要数据库操作、SQL、数据存储管理时使、不适用于数据库架、构设计决策、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

> 详细内容已移至 `references/detail.md`

### 命令参数说明

1. `-source`: 命令参数,用于指定操作选项
2. `--jq`: 命令参数,用于指定操作选项
3. `-Type`: 命令参数,用于指定操作选项
4. `--filter`: 命令参数,用于指定操作选项
5. `-Version`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-Version`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-Version`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Version`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-Version`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Version`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-Version`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Version`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Version`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项

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
| Status | Meaning |
| --- | --- |
| 400 | Missing Notion connection |
| 401 | Invalid or missing Maton API key |
| 429 | Rate limited (10 req/sec per account) |
| 4xx/5xx | Passthrough error from Notion API |

### 错误恢复步骤
**CLI:**

1. Check your auth state:

```bash
maton whoami
```

2. Verify the API key is valid by listing connections:

```bash
maton connection list
```

**Manual:**

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
1. Ensure your URL path starts with `notion`. For example:

* Correct: `https://api.maton.ai/notion/v1/search`
* Incorrect: `https://api.maton.ai/v1/search`
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

### CLI
```bash
maton notion search 'roadmap'

maton notion page view 0123456789abcdef0123456789abcdef

maton notion data-source query <dataSourceId> --filter '{"property":"Status","select":{"equals":"Active"}}'

maton notion search 'roadmap' --json --jq '.results | map(select(.object == "page"))'
```

### JavaScript
```javascript
const response = await fetch('https://api.maton.ai/notion/v1/search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.MATON_API_KEY}`,
    'Notion-Version': '2025-09-03'
  },
  body: JSON.stringify({ query: 'meeting' })
});
```

### Python
```python
import os
import requests

response = requests.post(
    'https://api.maton.ai/notion/v1/search',
    headers={
        'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}',
        'Notion-Version': '2025-09-03'
    },
    json={'query': 'meeting'}
)
```

## 常见问题

### Q1: 如何开始使用Notion？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Notion有什么限制？
A: 

## 已知限制

- 需要API Key，无Key环境无法使用
