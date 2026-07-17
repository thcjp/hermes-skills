---
slug: clawdbot-jira-skill
name: clawdbot-jira-skill
version: "1.0.2"
displayName: Jira
summary: Manage Jira issues, transitions, and worklogs via the Jira Cloud REST API.
license: MIT
description: |-
  Manage Jira issues, transitions, and worklogs via the Jira Cloud REST
  API.

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: jira, worklogs, clawdbot, transitions, manage, issues, skill
tags:
- Integrations
- Productivity
tools:
- read
- exec
---

# Jira

Work with Jira issues and worklogs from Clawdbot (search, status, create, log work, worklog summaries).

## Setup

1. Get your API key: <https://id.atlassian.com/manage-profile/security/api-tokens>
2. Click "Create API Token"
3. Set environment variables:

   bash

   ```
   export JIRA_EMAIL="you@example.com"
   export JIRA_API_TOKEN="[REDACTED]"
   export JIRA_URL="https://your-domain.atlassian.net"
   # Optional project scope (comma-separated). Empty = search all.
   export JIRA_BOARD="ABC"
   ```

Requires `curl`, `jq`, `bc`, and `python3`.

## Quick Commands

All commands live in `{baseDir}/scripts/jira.sh`.

* `{baseDir}/scripts/jira.sh search "timeout" [max]` — fuzzy search by summary or key inside `JIRA_BOARD`
* `{baseDir}/scripts/jira.sh link ABC-123` — browser link for an issue
* `{baseDir}/scripts/jira.sh issue ABC-123` — quick issue details
* `{baseDir}/scripts/jira.sh status ABC-123 "In Progress"` — move an issue (validates available transitions)
* `{baseDir}/scripts/jira.sh transitions ABC-123` — list allowed transitions
* `{baseDir}/scripts/jira.sh assign ABC-123 "name or email"` — assign by user search
* `{baseDir}/scripts/jira.sh assign-me ABC-123` — assign to yourself
* `{baseDir}/scripts/jira.sh comment ABC-123 "text"` — add a comment
* `{baseDir}/scripts/jira.sh create "Title" ["Description"]` — create a Task in `JIRA_BOARD`
* `{baseDir}/scripts/jira.sh log ABC-123 2.5 [YYYY-MM-DD]` — log hours (defaults to today UTC)
* `{baseDir}/scripts/jira.sh my [max]` — open issues assigned to you
* `{baseDir}/scripts/jira.sh hours 2025-01-01 2025-01-07` — your logged hours by issue (JSON)
* `{baseDir}/scripts/jira.sh hours-day 2025-01-07 [name|email]` — logged hours for a day grouped by user/issue; optional filter (name/email; also resolves to accountId)
* `{baseDir}/scripts/jira.sh hours-issue ABC-123 [name|email]` — logged hours for an issue; optional filter (name/email; also resolves to accountId)

## Command Reference

* **Search issues**

  bash

  ```
  {baseDir}/scripts/jira.sh search "payment failure" [maxResults]
  ```
* **Issue link**

  bash

  ```
  {baseDir}/scripts/jira.sh link ABC-321
  ```
* **Issue details**

  bash

  ```
  {baseDir}/scripts/jira.sh issue ABC-321
  ```
* **Update status**

  bash

  ```
  {baseDir}/scripts/jira.sh status ABC-321 "Done"
  ```
* **List transitions**

  bash

  ```
  {baseDir}/scripts/jira.sh transitions ABC-321
  ```
* **Assign issue**

  bash

  ```
  {baseDir}/scripts/jira.sh assign ABC-321 "Jane Doe"
  ```
* **Assign to yourself**

  bash

  ```
  {baseDir}/scripts/jira.sh assign-me ABC-321
  ```
* **Add comment**

  bash

  ```
  {baseDir}/scripts/jira.sh comment ABC-321 "Deployed to staging"
  ```
* **Create issue**

  bash

  ```
  {baseDir}/scripts/jira.sh create "Fix auth timeout" "Users being logged out after 5m"
  ```
* **Log hours**

  bash

  ```
  {baseDir}/scripts/jira.sh log PB-321 1.5 2025-01-18
  ```
* **My open issues**

  bash

  ```
  {baseDir}/scripts/jira.sh my [maxResults]
  ```
* **Logged hours by issue (me)**

  bash

  ```
  {baseDir}/scripts/jira.sh hours 2025-01-01 2025-01-05
  ```
* **Logged hours for a day (everyone)**

  bash

  ```
  {baseDir}/scripts/jira.sh hours-day 2025-01-05
  ```
* **Logged hours for a day (user filter)**

  bash

  ```
  {baseDir}/scripts/jira.sh hours-day 2025-01-05 "jane"
  ```
* **Logged hours for an issue**

  bash

  ```
  {baseDir}/scripts/jira.sh hours-issue ABC-321 "jane"
  ```

## Notes

* Worklog commands use Jira's worklog/updated + worklog/list combo and may take a few seconds on large projects.
* `hours` filters by `JIRA_EMAIL`; `hours-day` returns all users with totals per issue and user.
* Outputs for hours commands are JSON for reuse in other tools.
* Status transitions are validated against the server-provided transition list before applying.

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
