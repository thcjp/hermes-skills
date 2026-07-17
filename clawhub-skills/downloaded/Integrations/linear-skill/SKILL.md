---
slug: linear-skill
name: linear
version: "1.0.0"
displayName: Linear
summary: Manage Linear projects, issues, and tasks via the bundled Node CLI and the
  official Linear API. U...
license: MIT
description: |-
  Manage Linear projects, issues, and tasks via the bundled Node CLI and
  the official Linear API. U...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: linear, tasks, manage, issues, projects, skill
tags:
- Integrations
tools:
- read
- exec
---

# Linear Workflow Management

Manage Linear issues and projects through the bundled CLI at `{baseDir}/scripts/linear-cli.js`.

## Scope and Runtime Model

- This skill runs `node {baseDir}/scripts/linear-cli.js ...`.
- The CLI uses the official `@linear/sdk`.
- Authentication is `LINEAR_API_KEY` from the local environment.
- Expected API destination is Linear GraphQL (`https://api.linear.app/graphql`) through the official SDK.

## Prerequisites

1. Node.js and npm are installed.
2. Install script dependencies once:
   - `cd {baseDir}/scripts && npm install`
3. Set your API key:
   - `export LINEAR_API_KEY="[REDACTED]"`

If dependencies or `LINEAR_API_KEY` are missing, stop and complete setup before issue/project operations.

## Authentication and Credentials

- Required credential: `LINEAR_API_KEY`.
- Get it from `https://linear.app/settings/api`.
- Use least-privilege access and a dedicated token for automation.

## Required Workflow

1. Clarify intent and scope:
   - Team/project, labels, cycle, assignee, due date, priority.
2. Read current state first:
   - List/get issues, projects, statuses, labels, users, cycles.
3. Apply mutations second:
   - Create/update issues, comments, projects, milestones, labels.
4. Summarize exactly what changed:
   - Mention IDs, states, assignees, blockers, and follow-up actions.

## Command Coverage

- Teams and projects:
  `teams`, `projects`, `createProject`
- Issues:
  `issues`, `issue`, `createIssue`, `updateIssue`
- Comments:
  `createComment`
- States and labels:
  `states`, `labels`
- User:
  `user`

## Quick Examples

```bash
node {baseDir}/scripts/linear-cli.js teams
node {baseDir}/scripts/linear-cli.js projects
node {baseDir}/scripts/linear-cli.js issues
node {baseDir}/scripts/linear-cli.js issue ENG-123
node {baseDir}/scripts/linear-cli.js createIssue "Title" "Description" "team-id" '{"priority":2}'
node {baseDir}/scripts/linear-cli.js updateIssue "issue-id" '{"stateId":"state-id"}'
```

## Practical Workflows

- Triage urgent bugs:
  list high-priority open issues, assign owners, move state to `In Progress`, add triage comments.
- Sprint planning:
  review cycle scope, create missing issues, set priorities and estimates, align assignees.
- Release prep:
  verify blockers, update project status, create milestone tasks, add rollout comments.
- Documentation cleanup:
  find stale docs/issues, open follow-up tasks, link related records.

## Safety and Operational Rules

- Never invent IDs; fetch and confirm before updates.
- Prefer narrow updates over broad bulk edits.
- For bulk edits, explain grouping logic before applying changes.
- Do not include secrets in issue comments or descriptions.
- Do not send data to endpoints outside Linear API scope for this skill.

## References

- `references/API.md` for priority values and workflow patterns.

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
