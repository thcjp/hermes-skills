---
slug: github-api
name: github-api
version: "1.0.7"
displayName: GitHub
summary: This is a disclosed GitHub integration that uses Maton-managed OAuth/API
  access and includes appr...
license: MIT-0
description: |-
  This is a disclosed GitHub integration that uses Maton-managed OAuth/API
  access and includes appr。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags: '[''Integrations'', ''Development'']'
tools:
  - read
  - exec
# GitHub
---
# GitHub

## 核心能力

- This is a disclosed GitHub integration that uses Maton-managed OAuth/API
  access and includes appr
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

### 源能力映射
本skill覆盖源skill的以下能力点:

| 源能力点 | 支持状态 | 实现方式 |
|:---------|:---------|:---------|
| Commits | 支持 | 通过核心功能实现对应能力 |
| Milestones | 支持 | 通过核心功能实现对应能力 |
| Organizations | 支持 | 通过核心功能实现对应能力 |
| Branches | 支持 | 通过核心功能实现对应能力 |

**输入**: 用户提供源能力映射所需的指令和必要参数。
**处理**: 按照skill规范执行源能力映射操作,遵循单一意图原则。
**输出**: 返回源能力映射的执行结果,包含操作状态和输出数据。
### 领域术语
本skill涉及以下领域术语: `labels`, `urls`, `compare`, `sha`, `pagination`, `community`, `handling`, `resources`, `since`, `committer`, `until`, `comments`, `irreversible`, `repositories`, `rest`

**输入**: 用户提供领域术语所需的指令和必要参数。
**处理**: 按照skill规范执行领域术语操作,遵循单一意图原则。
**输出**: 返回领域术语的执行结果,包含操作状态和输出数据。

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

> 详细内容已移至 `references/detail.md`

### 命令参数说明

- `--jq`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
| --- | --- |
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
1. Ensure your URL path starts with `github`. For example:

* Correct: `https://api.maton.ai/github/user`
* Incorrect: `https://api.maton.ai/api.相关技术文档
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
maton github repo list --json

maton github repo list --json --jq '.[] | {name, full_name, private}'

maton github repo list --json --jq '.[] | select(.private == false) | .name'

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

### Q2: 遇到错误怎么办？
A: 

### Q3: GitHub有什么限制？
A: 

## 已知限制

- 需要API Key，无Key环境无法使用
