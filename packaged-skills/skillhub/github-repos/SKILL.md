---
slug: "github-repos"
name: "github-repos"
version: "1.0.5"
displayName: "GitHub"
summary: "Work with GitHub repositories, issues, pull requests, commits, branches,"
license: "Proprietary"
description: |-
  Work with GitHub repositories, issues, pull requests, commits, branches,
  releases, and workflows 。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
  - Integrations
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# GitHub

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Work with GitHub repositories, issues, pull requests, commits, branches, | 支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Work with GitHub repositories, issues, pull requests, commits, branches,
  releases, and workflows
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

```bash
clawlink_call_tool --tool "github_list_repositories_for_the_authenticated_user" --params '{}'

clawlink_call_tool --tool "github_get_a_repository" --params '{"owner": "owner", "repo": "repo-name"}'

clawlink_call_tool --tool "github_list_issues_for_a_repository" --params '{"owner": "owner", "repo": "repo-name", "state": "open"}'
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
| Tool not found | The tool name does not exist in the current catalog. Verify with `clawlink_list_tools --integration github`. |
| Missing connection | GitHub is not connected. Direct the user to <https://claw-link.dev/dashboard?add=github>. |
| `404 Not Found` | Repository, issue, or PR does not exist. Verify owner, repo, and number. |
| `403 Forbidden` | Rate limit exceeded or insufficient permissions. |
| `422 Unprocessable` | Invalid request body or missing required fields. Verify tool schema. |
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

1. Ensure the integration slug is exactly `github`.
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

### List open issues in a repository

```bash
clawlink_call_tool --tool "github_list_issues_for_a_repository" \
  --params '{
    "owner": "owner",
    "repo": "repo-name",
    "state": "open",
    "sort": "created",
    "direction": "desc"
  }'
```

### Create a new issue

```bash
clawlink_call_tool --tool "github_create_an_issue" \
  --params '{
    "owner": "owner",
    "repo": "repo-name",
    "title": "Bug: Login fails on mobile",
    "body": "Steps to reproduce: 1. Go to login 2. Enter credentials 3. Error shown",
    "labels": ["bug", "high-priority"]
  }'
```

### Add labels to an issue

```bash
clawlink_call_tool --tool "github_add_labels_to_an_issue" \
  --params '{
    "owner": "owner",
    "repo": "repo-name",
    "issue_number": 123,
    "labels": ["needs-review", "bug"]
  }'
```

### Create a pull request

```bash
clawlink_call_tool --tool "github_create_a_pull_request" \
  --params '{
    "owner": "owner",
    "repo": "repo-name",
    "title": "Fix login bug",
    "head": "fix/login-bug",
    "base": "main",
    "body": "Fixes #123 - Login fails on mobile devices"
  }'
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
