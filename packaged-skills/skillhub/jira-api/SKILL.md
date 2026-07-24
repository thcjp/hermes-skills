---
slug: "jira-api"
name: "jira-api"
version: 1.0.9
displayName: "Jira"
summary: "Jira API托管OAuth集成,JQL搜索/建改issue/管看板。Jira API integration with managed OAuth。Search issues with"
license: "Proprietary"
description: |-
  Jira API integration with managed OAuth。Search issues with JQL, create
  and update issues, manage。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - Integrations
  - Productivity
  - API
  - 接口
  - 开发工具
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Development"
---
# Jira

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

- Jira API integration with managed OAuth
- Search issues with JQL, create
  and update issues, manage
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 搜索检索 | 关键词与过滤条件 | 匹配结果与相关性排序 |
| Jira API托管 | 目标数据与配置参数 | 处理结果与执行状态 |
| JQL搜索 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

> 详细内容已移至 `references/detail.md`

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | jira-api处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "api_result": "api_result_value",
      "api_metadata": "api_metadata_value",
      "api_status": "api_status_value"
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

中间产物模板参考: `assets/jira-api_template`

## 错误处理
| Status | Meaning |
|:-----:|:-----:|
| 400 | Missing Jira connection or invalid JQL |
| 401 | Invalid or missing Maton API key |
| 429 | Rate limited (10 req/sec per account) |
| 4xx/5xx | Passthrough error from Jira API |

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
1. Ensure your URL path starts with `jira`. For example:

* Correct: `https://api.maton.ai/jira/ex/jira/{cloudId}/rest/api/3/project`
* Incorrect: `https://api.maton.ai/ex/jira/{cloudId}/rest/api/3/project`
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
maton jira cloud list
# ...
maton jira issue search 'project = PROJ AND status = "In Progress"' --cloud-id abc-123
# ...
maton jira issue search 'project = PROJ' --cloud-id abc-123 \
  --json --jq '.issues | map(select(.fields.status.name == "In Progress"))'
# ...
maton jira issue create --cloud-id abc-123 --project PROJ --summary 'Fix login'
```

### JavaScript
```javascript
// Get cloud ID first
const resources = await fetch(
  'https://api.maton.ai/jira/oauth/token/accessible-resources',
  { headers: { 'Authorization': `Bearer ${process.env.MATON_API_KEY}` } }
).then(r => r.json());
// ...
const cloudId = resources[0].id;
// ...
// Search issues
const issues = await fetch(
  `https://api.maton.ai/jira/ex/jira/${cloudId}/rest/api/3/search/jql?jql=project=KEY`,
  { headers: { 'Authorization': `Bearer ${process.env.MATON_API_KEY}` } }
).then(r => r.json());
```

### Python

## 常见问题

### Q1: 如何开始使用Jira？
A: 

## 已知限制

- 需要API Key，无Key环境无法使用
