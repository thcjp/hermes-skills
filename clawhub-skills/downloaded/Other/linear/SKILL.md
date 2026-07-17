---
slug: linear
name: linear
version: "1.0.0"
displayName: Linear
summary: Query and manage Linear issues, projects, and team workflows.
license: MIT
description: |-
  Query and manage Linear issues, projects, and team workflows.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: query, linear, manage, issues, projects
tags:
- Other
tools:
- read
- exec
---

# Linear

Manage issues, check project status, and stay on top of your team's work.

## Setup

```bash
export LINEAR_API_KEY="[REDACTED]"
export LINEAR_DEFAULT_TEAM="TEAM"
```

Discover team keys:

```bash
{baseDir}/scripts/linear.sh teams
```

If `LINEAR_DEFAULT_TEAM` is set, you can omit the team key in `team` and call:

```bash
{baseDir}/scripts/linear.sh create "Title" ["Description"]
```

## Quick Commands

```bash
{baseDir}/scripts/linear.sh my-issues          # Your assigned issues
{baseDir}/scripts/linear.sh my-todos           # Just your Todo items
{baseDir}/scripts/linear.sh urgent             # Urgent/High priority across team

{baseDir}/scripts/linear.sh teams              # List available teams
{baseDir}/scripts/linear.sh team <TEAM_KEY>    # All issues for a team
{baseDir}/scripts/linear.sh project <name>     # Issues in a project
{baseDir}/scripts/linear.sh issue <TEAM-123>   # Get issue details
{baseDir}/scripts/linear.sh branch <TEAM-123>  # Get branch name for GitHub

{baseDir}/scripts/linear.sh create <TEAM_KEY> "Title" ["Description"]
{baseDir}/scripts/linear.sh comment <TEAM-123> "Comment text"
{baseDir}/scripts/linear.sh status <TEAM-123> <todo|progress|review|done|blocked>
{baseDir}/scripts/linear.sh assign <TEAM-123> <userName>
{baseDir}/scripts/linear.sh priority <TEAM-123> <urgent|high|medium|low|none>

{baseDir}/scripts/linear.sh standup            # Daily standup summary
{baseDir}/scripts/linear.sh projects           # All projects with progress
```

## Common Workflows

### Morning Standup

```bash
{baseDir}/scripts/linear.sh standup
```

Shows: your todos, blocked items across team, recently completed, what's in review.

### Quick Issue Creation (from chat)

```bash
{baseDir}/scripts/linear.sh create TEAM "Fix auth timeout bug" "Users getting logged out after 5 min"
```

### Triage Mode

```bash
{baseDir}/scripts/linear.sh urgent    # See what needs attention
```

## Git Workflow (Linear ↔ GitHub Integration)

**Always use Linear-derived branch names** to enable automatic issue status tracking.

### Getting the Branch Name

```bash
{baseDir}/scripts/linear.sh branch TEAM-212
```

### Creating a Worktree for an Issue

```bash
BRANCH=$({baseDir}/scripts/linear.sh branch TEAM-212)

cd /path/to/repo
git checkout main && git pull origin main

git worktree add .worktrees/team-212 -b "$BRANCH" origin/main
cd .worktrees/team-212

git push -u origin "$BRANCH"
```

**⚠️ Never modify files on main.** All changes happen in worktrees only.

### Why This Matters

* Linear's GitHub integration tracks PRs by branch name pattern
* When you create a PR from a Linear branch, the issue **automatically moves to "In Review"**
* When the PR merges, the issue **automatically moves to "Done"**
* Manual branch names break this automation
* Keeping main clean = no accidental pushes, easy worktree cleanup

### Quick Reference

```bash
ISSUE="TEAM-212"
BRANCH=$({baseDir}/scripts/linear.sh branch $ISSUE)

cd ~/workspace/your-repo
git checkout main && git pull origin main

git worktree add .worktrees/${ISSUE,,} -b "$BRANCH" origin/main
cd .worktrees/${ISSUE,,}

git add -A && git commit -m "fix: implement $ISSUE"
git push -u origin "$BRANCH"
gh pr create --title "$ISSUE: <title>" --body "Closes $ISSUE"
```

## Priority Levels

| Level | Value | Use for |
| --- | --- | --- |
| urgent | 1 | Production issues, blockers |
| high | 2 | This week, important |
| medium | 3 | This sprint/cycle |
| low | 4 | Nice to have |
| none | 0 | Backlog, someday |

## Teams (cached)

Team keys and IDs are discovered via the API and cached locally after the first lookup.
Use `linear.sh teams` to refresh and list available teams.

## Notes

* Uses GraphQL API (api.linear.app/graphql)
* Requires `LINEAR_API_KEY` env var
* Issue identifiers are like `TEAM-123`

## Attribution

Inspired by [schpet/linear-cli](https://github.com/schpet/linear-cli) by Peter Schilling (ISC License).
This is an independent bash implementation for Clawdbot integration.

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
