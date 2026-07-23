---
slug: "notion-api-skill"
name: "notion-api-skill"
version: "1.0.11"
displayName: "Notion"
summary: "Notion API托管OAuth集成,查数据库/搜页面/读工作区"
license: "Proprietary"
description: |-
  Notion API integration with managed OAuth。Query databases, search pages,
  and read workspace cont。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策.
tags:
  - Integrations
  - Productivity
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Notion

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

- Notion API integration with managed OAuth
- Query databases, search pages,
  and read workspace cont
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 数据处理 | 数据源与处理规则 | 清洗结果与统计摘要 |
| Notion API | 目标数据与配置参数 | 处理结果与执行状态 |
| 查数据库 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

> 详细内容已移至 `references/detail.md`

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | notion-api-skill处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "skill_result": "skill_result_value",
      "skill_metadata": "skill_metadata_value",
      "skill_status": "skill_status_value"
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

中间产物模板参考: `assets/notion-api-skill_template`

## 错误处理
| Status | Meaning |
|:-----:|:-----:|
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
> **处理方式**: 参考上表中的错误场景说明,按照对应建议进行处理和恢复.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### CLI
```bash
maton notion search 'roadmap'
# ...
maton notion page view 0123456789abcdef0123456789abcdef
# ...
maton notion data-source query <dataSourceId> --filter '{"property":"Status","select":{"equals":"Active"}}'
# ...
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
# ...
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

## 已知限制

- 需要API Key，无Key环境无法使用
