---
slug: openclaw-linear
name: openclaw-linear
version: "1.0.1"
displayName: Linear CLI
summary: "命令行管Linear issue/项目/团队/文档(社区下载版)"
  using the linear CLI. ...
license: MIT
description: |-
  Manage Linear issues, projects, teams, and documents from the command
  line using the linear CLI。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
---

# Linear CLI

A CLI to manage Linear issues from the command line, with git and jj integration.

## Prerequisites

The `linear` command must be available on PATH. To check:

```bash
linear --version
```

If not installed:

* **Homebrew**: `brew install schpet/tap/linear`
* **Deno**: `deno install -A --reload -f -g -n linear jsr:@schpet/linear-cli`
* **Binaries**: <https://github.com/schpet/linear-cli/releases/latest>

## Setup

1. Create an API key at <https://linear.app/settings/account/security>
2. Authenticate: `linear auth login`
3. Configure your project: `cd my-project-repo && linear config`

## Available Commands

```text
linear auth               # Manage Linear authentication
linear issue              # Manage Linear issues
linear team               # Manage Linear teams
linear project            # Manage Linear projects
linear project-update     # Manage project status updates
linear milestone          # Manage Linear project milestones
linear initiative         # Manage Linear initiatives
linear initiative-update  # Manage initiative status updates
linear label              # Manage Linear issue labels
linear document           # Manage Linear documents
linear config             # Interactively generate .linear.toml configuration
linear schema             # Print the GraphQL schema to stdout
linear api                # Make a raw GraphQL API request
```

## Common Workflows

### List and view issues

```bash
linear issue list

linear issue list -s started
linear issue list -s completed

linear issue list -A

linear issue view

linear issue view ABC-123
```

### Create and manage issues

```bash
linear issue create

linear issue create -t "Fix login bug" -d "Users can't log in with SSO" -s "In Progress" -a self --priority 1

linear issue update ABC-123 -s "Done" -t "Updated title"

linear issue comment add ABC-123 -b "This is fixed in the latest build"

linear issue delete ABC-123 -y
```

### Start working on an issue

```bash
linear issue start

linear issue start ABC-123

linear issue pr
```

### Projects and milestones

```bash
linear project list

linear project create -n "Q1 Launch" -t ENG -s started --target-date 2026-03-31

linear milestone list --project <projectId>
```

### Documents

```bash
linear document list

linear document create --title "Design Spec" --content-file ./spec.md --project <projectId>

linear document view <slug>
```

### Teams

```bash
linear team list

linear team members
```

## Discovering Options

Run `--help` on any command for flags and options:

```bash
linear --help
linear issue --help
linear issue list --help
linear issue create --help
```

## Using the Linear GraphQL API Directly

**Prefer the CLI for all supported operations.** The `api` command is a fallback for queries not covered by the CLI.

### Check the schema

```bash
linear schema -o "${TMPDIR:-/tmp}/linear-schema.graphql"
grep -i "cycle" "${TMPDIR:-/tmp}/linear-schema.graphql"
grep -A 30 "^type Issue " "${TMPDIR:-/tmp}/linear-schema.graphql"
```

### Make a GraphQL request

```bash
linear api '{ viewer { id name email } }'

linear api 'query($teamId: String!) { team(id: $teamId) { name } }' --variable teamId=abc123

linear api 'query($filter: IssueFilter!) { issues(filter: $filter) { nodes { title } } }' \
  --variables-json '{"filter": {"state": {"name": {"eq": "In Progress"}}}}'

linear api '{ issues(first: 5) { nodes { identifier title } } }' | jq '.data.issues.nodes[].title'
```

### Using curl directly

```bash
curl -s -X POST https://api.linear.app/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: $(linear auth token)" \
  -d '{"query": "{ viewer { id } }"}'
```

## Reference Documentation

For detailed subcommand documentation with all flags and options:

* [issue](/api/v1/skills/skill-platform-linear/file?path=references%2Fissue.md&ownerHandle=cipher-shad0w) - Manage Linear issues (list, create, update, start, view, comment, PR, delete)
* [team](/api/v1/skills/skill-platform-linear/file?path=references%2Fteam.md&ownerHandle=cipher-shad0w) - Manage Linear teams (list, create, delete, members, autolinks)
* [project](/api/v1/skills/skill-platform-linear/file?path=references%2Fproject.md&ownerHandle=cipher-shad0w) - Manage Linear projects (list, view, create)
* [document](/api/v1/skills/skill-platform-linear/file?path=references%2Fdocument.md&ownerHandle=cipher-shad0w) - Manage Linear documents (list, view, create, update, delete)
* [api](/api/v1/skills/skill-platform-linear/file?path=references%2Fapi.md&ownerHandle=cipher-shad0w) - Make raw GraphQL API requests

## Configuration

The CLI supports environment variables or a `.linear.toml` config file:

| Option | Env Var | TOML Key | Example |
| --- | --- | --- | --- |
| Team ID | `LINEAR_TEAM_ID` | `team_id` | `"ENG"` |
| Workspace | `LINEAR_WORKSPACE` | `workspace` | `"mycompany"` |
| Issue sort | `LINEAR_ISSUE_SORT` | `issue_sort` | `"priority"` or `"manual"` |
| VCS | `LINEAR_VCS` | `vcs` | `"git"` or `"jj"` |

Config file locations (checked in order):

1. `./linear.toml` or `./.linear.toml` (current directory)
2. `<repo-root>/linear.toml` or `<repo-root>/.linear.toml`
3. `<repo-root>/.config/linear.toml`
4. `~/.config/linear/linear.toml`

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

- Manage Linear issues, projects, teams, and documents from the command
  line using the linear CLI
- 触发关键词: teams, linear, manage, openclaw, issues, projects, cli

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Linear CLI？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Linear CLI有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
