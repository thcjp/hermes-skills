---
slug: github-repos
name: github-repos
version: "1.0.5"
displayName: GitHub
summary: "管GitHub仓库/issue/PR/提交/分支/发布/工作流(社区下载版)"
  releases, and workflows ...
license: MIT-0
description: |-
  Work with GitHub repositories, issues, pull requests, commits, branches,
  releases, and workflows 。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# GitHub

Access GitHub via the GitHub API with OAuth authentication. Manage repositories, issues, pull requests, commits, branches, releases, and workflows.

This skill uses [ClawLink](https://claw-link.dev/?utm_source=SkillHub&utm_medium=referral&utm_content=github-repos) for hosted connection flows and credentials so you do not need to configure GitHub API access yourself.

### Setup in 3 Steps

| Step 1: Install | Step 2: Pair Account | Step 3: Connect GitHub |
| --- | --- | --- |
|  |  | *App-specific connection GIF coming soon* |
| Run the install command in Skill平台 | Sign in and approve the device | Open the dashboard and connect GitHub |

## How It Works

```text
┌─────────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Skill平台      │────▶│   ClawLink   │────▶│   GitHub API     │
│   (User Chat)   │     │   (OAuth)    │     │   (REST/GraphQL) │
└─────────────────┘     └──────────────┘     └──────────────────┘
         │                       │                       │
         │  1. Install Plugin    │                       │
         │  2. Pair Device       │                       │
         │  3. Connect GitHub    │                       │
         │                       │  4. Secure Token      │
         │                       │  5. Proxy Requests    │
         │                       │                       │
         ▼                       ▼                       ▼
   ┌──────────┐           ┌──────────┐           ┌──────────┐
   │  SKILL   │           │ Dashboard│           │ GitHub   │
   │  File    │           │ Auth     │           │ Repos    │
   └──────────┘           └──────────┘           └──────────┘
```

## Install

Install the verified ClawLink plugin from SkillHub. After the user confirms, complete the full setup so ClawLink tools are visible in the next Skill平台 chat.

```bash
skill-platform plugins install SkillHub:clawlink-plugin
skill-platform config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
skill-platform gateway restart
```

Then tell the user: "Skill平台 has been restarted. Send `/new` as a standalone message to start a fresh chat, then ask for GitHub again."

## Quick Start

```bash
clawlink_call_tool --tool "github_list_repositories_for_the_authenticated_user" --params '{}'

clawlink_call_tool --tool "github_get_a_repository" --params '{"owner": "owner", "repo": "repo-name"}'

clawlink_call_tool --tool "github_list_issues_for_a_repository" --params '{"owner": "owner", "repo": "repo-name", "state": "open"}'
```

## Authentication

All GitHub tool calls are authenticated automatically by ClawLink using the user's connected GitHub account.

**No API key is required in chat.** ClawLink stores the OAuth token securely and injects it into every GitHub API request on the user's behalf.

### Getting Connected

1. Install the ClawLink plugin (see Install above).
2. Pair the plugin with `clawlink_begin_pairing` if it is not configured yet.
3. Open <https://claw-link.dev/dashboard?add=github> and connect GitHub.
4. Call `clawlink_list_integrations` to verify the connection is active.

## Connection Management

### List Connections

```bash
clawlink_list_integrations
```

**Response:** Returns all connected integrations. Look for `github` in the list.

### Verify Connection

```bash
clawlink_list_tools --integration github
```

**Response:** Returns the live tool catalog for GitHub.

### Reconnect

If GitHub tools are missing or the connection shows an error:

1. Direct the user to <https://claw-link.dev/dashboard?add=github>
2. After they confirm, call `clawlink_list_integrations` to verify
3. Then call `clawlink_list_tools --integration github`

## Security & Permissions

* Access is scoped to repositories and resources accessible to the connected GitHub account.
* **All write operations require explicit user confirmation.** Before executing any create, update, or delete call, confirm the target resource and intended effect with the user.
* Destructive actions (deleting issues, closing PRs, removing collaborators) are marked as high-impact and must be confirmed.
* Workflow triggers and deployments affect external systems — always confirm before executing.

## Tool Reference

### Repositories

| Tool | Description | Mode |
| --- | --- | --- |
| `github_list_repositories_for_the_authenticated_user` | List all repos for the authenticated user | Read |
| `github_get_a_repository` | Get repository details | Read |
| `github_create_a_repository` | Create a new repository | Write |
| `github_update_a_repository` | Update repository settings | Write |
| `github_delete_a_repository` | Delete a repository | Write |
| `github_list_repository_collaborators` | List repo collaborators | Read |

### Issues

| Tool | Description | Mode |
| --- | --- | --- |
| `github_list_issues_for_a_repository` | List issues with filtering | Read |
| `github_get_an_issue` | Get issue details | Read |
| `github_create_an_issue` | Create a new issue | Write |
| `github_update_an_issue` | Update issue fields (labels, assignee, state) | Write |
| `github_add_labels_to_an_issue` | Add labels to an issue | Write |
| `github_add_assignees_to_an_issue` | Add assignees to an issue | Write |

### Pull Requests

| Tool | Description | Mode |
| --- | --- | --- |
| `github_list_pull_requests` | List PRs in a repository | Read |
| `github_get_a_pull_request` | Get PR details | Read |
| `github_create_a_pull_request` | Create a new PR | Write |
| `github_update_a_pull_request` | Update PR fields | Write |

### Commits & Branches

| Tool | Description | Mode |
| --- | --- | --- |
| `github_list_commits` | List commits in a repository | Read |
| `github_get_a_commit` | Get commit details | Read |
| `github_list_branches` | List branches in a repository | Read |
| `github_create_a_branch` | Create a new branch | Write |

### Workflows

| Tool | Description | Mode |
| --- | --- | --- |
| `github_list_repository_workflows` | List workflows in a repo | Read |
| `github_list_workflow_runs` | List workflow runs | Read |
| `github_get_a_workflow_run` | Get workflow run details | Read |
| `github_cancel_workflow_run` | Cancel an in-progress workflow run | Write |

### Releases

| Tool | Description | Mode |
| --- | --- | --- |
| `github_list_releases` | List releases in a repository | Read |
| `github_get_a_release` | Get release details | Read |
| `github_create_a_release` | Create a new release | Write |

## 示例

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

## Discovery Workflow

1. Call `clawlink_list_integrations` to confirm GitHub is connected.
2. Call `clawlink_list_tools --integration github` to see the live catalog.
3. Treat the returned list as the source of truth. Do not guess or assume what tools exist.
4. If the user describes a capability but the exact tool is unclear, call `clawlink_search_tools` with a short query and integration `github`.
5. If no GitHub tools appear, direct the user to <https://claw-link.dev/dashboard?add=github>.

## Execution Workflow

```text
┌─────────────────────────────────────────────────────────────┐
│  READ OPERATIONS (Safe)                                     │
│  list → get → search → describe → call                      │
│                                                             │
│  Example: List issues → Get issue → Show details            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  WRITE OPERATIONS (Require Confirmation)                    │
│  list → get → describe → preview → confirm → call           │
│                                                             │
│  Example: Describe tool → Preview issue → User approves     │
│           → Execute create                                   │
└─────────────────────────────────────────────────────────────┘
```

1. For unfamiliar tools, ambiguous requests, or any write action, call `clawlink_describe_tool` first.
2. Use the returned guidance, schema, `whenToUse`, `askBefore`, `safeDefaults`, `examples`, and `followups` to shape the call.
3. Prefer read, list, search, and get operations before writes when that reduces ambiguity.
4. For writes or anything marked as requiring confirmation, call `clawlink_preview_tool` first.
5. Execute with `clawlink_call_tool`. Pass confirmation only after the preview matches the user's intent.
6. If the tool call fails, report the real error. Do not invent results or restate the failure as a missing capability unless the live catalog supports that conclusion.

## Notes

* GitHub API rate limits apply. The number of calls depends on the connected account type (free, pro, or enterprise).
* Some tools require specific OAuth scopes. If a tool fails with insufficient scope, verify the connection has the right permissions.
* Repository names must use `owner/repo` format for owner and repo parameters.
* Issues and PRs use different numbering systems within the same repository.

## Error Handling

| Status / Error | Meaning |
| --- | --- |
| Tool not found | The tool name does not exist in the current catalog. Verify with `clawlink_list_tools --integration github`. |
| Missing connection | GitHub is not connected. Direct the user to <https://claw-link.dev/dashboard?add=github>. |
| `404 Not Found` | Repository, issue, or PR does not exist. Verify owner, repo, and number. |
| `403 Forbidden` | Rate limit exceeded or insufficient permissions. |
| `422 Unprocessable` | Invalid request body or missing required fields. Verify tool schema. |
| Write rejected | User did not confirm a write action. Always confirm before executing writes. |

### 错误处理

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

## Resources

* [GitHub REST API Documentation](https://docs.github.com/en/rest)
* [GitHub GraphQL API](https://docs.github.com/en/graphql)
* [GitHub Actions Documentation](https://docs.github.com/en/actions)
* [ClawLink](https://claw-link.dev/?utm_source=SkillHub&utm_medium=referral&utm_content=github-repos)
* [ClawLink Docs](https://docs.claw-link.dev/skill-platform)
* [ClawLink Verification](https://claw-link.dev/verify)

## Related Skills

* [GitLab Repos](https://SkillHub.ai/hith3sh/gitlab-repos) — For GitLab project management
* [GitHub Triage](https://SkillHub.ai/hith3sh/github-triage-workflow) — For GitHub issue triage workflows

---

**Powered by [ClawLink](https://claw-link.dev/?utm_source=SkillHub&utm_medium=referral&utm_content=github-repos)** — an integration hub for Skill平台

## 依赖说明

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
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Work with GitHub repositories, issues, pull requests, commits, branches,
  releases, and workflows
- 触发关键词: repositories, repos, github, issues

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题

### Q1: 如何开始使用GitHub？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: GitHub有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
