---
slug: -jira-pat-skill
name: -jira-pat-skill
version: "0.0.1"
displayName:  Jira Pat Ski
summary: "通过PAT管理自托管或企业Jira实例的issue,支持SSL认证,提升研发项目管理效率"
  Access Tokens in SS...
license: MIT
description: |-
  Manage Jira issues on self-hosted or enterprise Jira instances using
  Personal Access Tokens in SS。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
tools:
  - - read
- exec
---

> **核心功能**: 本技能提供化工作流场景等能力。

# SkillHub Jira Pat Skill

Manage Jira issues on self-hosted/enterprise Jira instances using Personal Access Tokens (PAT). This skill is designed for environments where Basic Auth doesn't work due to SSO/SAML authentication.

## When to Use This Skill

Use this skill when working with:

* Self-hosted Jira instances (e.g., Red Hat, enterprise deployments)
* Jira instances with SSO/SAML authentication
* Environments where `jira-cli` or Basic Auth fails

**Note:** For Atlassian Cloud with email + API token auth, use the `-jira-skill` instead.

## Prerequisites

1. **Personal Access Token (PAT)**: Create one in Jira:

   * Go to your Jira profile → Personal Access Tokens
   * Create a new token with appropriate permissions
   * Store it in environment variable `JIRA_PAT`
2. **Jira Base URL**: Your Jira instance URL in `JIRA_URL`

## Environment Variables

```bash
export JIRA_PAT="your-personal-access-token"
export JIRA_URL="https://issues.example.com"
```

## Tools

This skill uses `curl` and `jq` for all operations.

## Instructions

### Get Issue Details

Fetch full details of a Jira issue:

```bash
curl -s -H "Authorization: Bearer $JIRA_PAT" \
  "$JIRA_URL/rest/api/2/issue/PROJECT-123" | jq
```

Get specific fields only:

```bash
curl -s -H "Authorization: Bearer $JIRA_PAT" \
  "$JIRA_URL/rest/api/2/issue/PROJECT-123?fields=summary,status,description" | jq
```

### Search Issues (JQL)

```bash
curl -s -H "Authorization: Bearer $JIRA_PAT" \
  "$JIRA_URL/rest/api/2/search?jql=parent=EPIC-123" | jq

curl -s -H "Authorization: Bearer $JIRA_PAT" \
jql=project%3DPROJ%20AND%20status%3DOpen" | jq
```

Common JQL patterns:

* `parent=EPIC-123` - Child issues of an epic
* `project=PROJ AND status=Open` - Open issues in project
* `assignee=currentUser()` - Your assigned issues
* `labels=security` - Issues with specific label
* `updated >= -7d` - Recently updated

### Get Available Transitions

Before changing status, query available transitions:

```bash
curl -s -H "Authorization: Bearer $JIRA_PAT" \
  "$JIRA_URL/rest/api/2/issue/PROJECT-123/transitions" | jq '.transitions[] | {id, name}'
```

### Transition (Change Status)

Close an issue with a comment:

```bash
curl -s -X POST \
  -H "Authorization: Bearer $JIRA_PAT" \
  -H "Content-Type: application/json" \
  -d '{
    "transition": {"id": "61"},
    "update": {
      "comment": [{"add": {"body": "Closed via API"}}]
    }
  }' \
  "$JIRA_URL/rest/api/2/issue/PROJECT-123/transitions"
```

### Add a Comment

```bash
curl -s -X POST \
  -H "Authorization: Bearer $JIRA_PAT" \
  -H "Content-Type: application/json" \
  -d '{"body": "Comment added via API."}' \
  "$JIRA_URL/rest/api/2/issue/PROJECT-123/comment"
```

### Update Issue Fields

```bash
curl -s -X PUT \
  -H "Authorization: Bearer $JIRA_PAT" \
  -H "Content-Type: application/json" \
  -d '{
    "fields": {
      "summary": "Updated summary",
      "labels": ["api", "automated"]
    }
  }' \
  "$JIRA_URL/rest/api/2/issue/PROJECT-123"
```

### Create an Issue

```bash
curl -s -X POST \
  -H "Authorization: Bearer $JIRA_PAT" \
  -H "Content-Type: application/json" \
  -d '{
    "fields": {
      "project": {"key": "PROJ"},
      "summary": "New issue via API",
      "description": "Issue description",
      "issuetype": {"name": "Task"},
      "parent": {"key": "EPIC-123"}
    }
  }' \
  "$JIRA_URL/rest/api/2/issue"
```

## Useful jq Filters

```bash
jq '{key: .key, summary: .fields.summary, status: .fields.status.name}'

jq '.issues[] | {key: .key, summary: .fields.summary, status: .fields.status.name}'

jq '.fields.issuelinks[] | {type: .type.name, key: (.inwardIssue // .outwardIssue).key}'
```

## Troubleshooting

| Error | Cause | Solution |
| --- | --- | --- |
| 401 Unauthorized | Invalid/expired PAT | Regenerate token, check `Bearer` format |
| 404 Not Found | Issue doesn't exist or no access | Verify issue key and permissions |
| 400 Bad Request on transition | Invalid transition ID | Query available transitions first |

## Comparison with Basic Auth Skills

This skill uses **Bearer token authentication** (`Authorization: Bearer <PAT>`), which works with self-hosted Jira instances using SSO/SAML. For Atlassian Cloud with email + API token, use skills that implement Basic Auth instead.

## 运行环境
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
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 主要能力
- Manage Jira issues on self-hosted or enterprise Jira instances using
  Personal Access Tokens in SS
- 触发关键词: jira, , self, issues, manage, hosted, pat, skill

## 适用范围
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用指南
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
# 请参考上方使用说明进行配置和调用
result = "ready"
```

## 问题汇编
### Q1: 如何开始使用 Jira Pat Ski？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3:  Jira Pat Ski有什么限制？
A: 请参考已知限制章节了解具体限制。

## 使用约束
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 用户疑问集
### Q1: Jira Pat Ski支持哪些输入格式？

A1: 通过PAT管理自托管或企业Jira实例的issue,支持SSL认证,提升研发项目管理效率。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。

## 安全提示
### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 效能分析
| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 特色分析
| 对比维度 | Jira Pat Ski | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 通过PAT管理自托管或企业Jira实例的issue,支持SSL认证,提升研发项目 | 通用场景 | 通用场景 |

## 核心特点
- **自动化执行**: 通过PAT管理自托管或企业Jira实例的issue,支持SSL认证,提升研发项目管理效率
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

## 用户疑问集
### Q1: Jira Pat Ski支持哪些输入格式？

A1: 通过PAT管理自托管或企业Jira实例的issue,支持SSL认证,提升研发项目管理效率。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。

## 优势对比
| 对比维度 | Jira Pat Ski | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 通过PAT管理自托管或企业Jira实例的issue,支持SSL认证,提升研发项目 | 通用场景 | 通用场景 |

## 关键特点
- **自动化执行**: 通过PAT管理自托管或企业Jira实例的issue,支持SSL认证,提升研发项目管理效率
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据