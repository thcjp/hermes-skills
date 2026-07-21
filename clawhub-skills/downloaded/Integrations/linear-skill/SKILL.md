---
slug: linear-skill
name: linear-skill
version: "1.0.0"
displayName: Linear
summary: Manage Linear projects, issues, and tasks via the bundled Node CLI and the
  official Linear API. U...
license: MIT
description: |-
  Manage Linear projects, issues, and tasks via the bundled Node CLI and
  the official Linear API。U。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
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

## 示例

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

- Manage Linear projects, issues, and tasks via the bundled Node CLI and
  the official Linear API
- 触发关键词: linear, tasks, manage, issues, projects, skill

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Linear？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Linear有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
