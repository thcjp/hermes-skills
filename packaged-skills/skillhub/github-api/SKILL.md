---
slug: "github-api"
name: "github-api"
version: "1.0.7"
displayName: "GitHub"
summary: "经Maton托管OAuth/API接入GitHub,含适当权限范围"
license: "Proprietary"
description: |-
  This is a disclosed GitHub integration that uses Maton-managed OAuth/API
  access and includes appr。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - Integrations
  - Development
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# GitHub

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

- This is a disclosed GitHub integration that uses Maton-managed OAuth/API
  access and includes appr
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| Git操作 | 仓库路径与分支名 | 操作结果与变更记录 |
| 经Maton托管OA | 目标数据与配置参数 | 处理结果与执行状态 |
| API接入GitHu | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

> 详细内容已移至 `references/detail.md`

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | github-api处理的内容输入 |,  |
| content | string | 否 | github-api处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "api 相关配置参数",
    result: "api 相关配置参数",
    result: "api 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 错误处理
| Status | Meaning |
|:-----:|:-----:|
| 400 | Missing GitHub connection |
| 401 | Invalid or missing Maton API key |
| 403 | Forbidden - insufficient permissions or scope |
| 404 | Resource not found |
| 408 | Request timeout (common for complex searches) |
| 422 | Validation failed |
| 429 | Rate limited |
| 4xx/5xx | Passthrough error from GitHub API |

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
1. Ensure your URL path starts with `github`. For example:

* Correct: `https://api.maton.ai/github/user`
* Incorrect: `https://api.maton.ai/api.相关技术文档
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
maton github repo list --json
# ...
maton github repo list --json --jq '.[] | {name, full_name, private}'
# ...
maton github repo list --json --jq '.[] | select(.private == false) | .name'
# ...
maton github issue list --repo owner/repo --json --jq '.[].title'
```

### JavaScript
```javascript
const response = await fetch(
  'https://api.maton.ai/github/repos/owner/repo/issues?state=open&per_page=10',
  {
    headers: {
      'Authorization': `Bearer ${process.env.MATON_API_KEY}`
    }
  }
);
const issues = await response.json();
```

### Python
```python
import os
import requests
# ...
response = requests.get(
    'https://api.maton.ai/github/repos/owner/repo/issues',
    headers={'Authorization': f'Bearer {os.environ["MATON_API_KEY"]}'},
    params={'state': 'open', 'per_page': 10}
)
issues = response.json()
```

## 常见问题

### Q1: 如何开始使用GitHub？
A: 

## 已知限制

- 需要API Key，无Key环境无法使用
