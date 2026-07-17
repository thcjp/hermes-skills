---
slug: clawhub-jira-pat-skill
name: clawhub-jira-pat-skill
version: "0.0.1"
displayName: Clawhub Jira Pat Skill
summary: Manage Jira issues on self-hosted or enterprise Jira instances using Personal
  Access Tokens in SS...
license: MIT
description: |-
  Manage Jira issues on self-hosted or enterprise Jira instances using
  Personal Access Tokens in SS...

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: jira, clawhub, self, issues, manage, hosted, pat, skill
tags:
- Productivity
tools:
- read
- exec
---

# SkillHub Jira Pat Skill

Manage Jira issues on self-hosted/enterprise Jira instances using Personal Access Tokens (PAT). This skill is designed for environments where Basic Auth doesn't work due to SSO/SAML authentication.

## When to Use This Skill

Use this skill when working with:

* Self-hosted Jira instances (e.g., Red Hat, enterprise deployments)
* Jira instances with SSO/SAML authentication
* Environments where `jira-cli` or Basic Auth fails

**Note:** For Atlassian Cloud with email + API token auth, use the `clawdbot-jira-skill` instead.

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
  "$JIRA_URL/rest/api/2/search?jql=project%3DPROJ%20AND%20status%3DOpen" | jq
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

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
