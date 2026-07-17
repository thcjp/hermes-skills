---
slug: jira
name: jira
version: "1.3.3"
displayName: JIRA
summary: Use when the user mentions Jira issues (e.g., \
license: MIT
description: |-
  Use when the user mentions Jira issues (e.g., \

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: mentions, jira, issues
tags: '[''Productivity'']'
tools: '[read, exec]'
---

# JIRA

Natural language interaction with Jira. Supports multiple backends.

## Backend Detection

**Run this check first** to determine which backend to use:

```text
1. Check if jira CLI is available:
   → Run: which jira
   → If found: USE CLI BACKEND

2. If no CLI, check for Atlassian MCP:
   → Look for mcp__atlassian__* tools
   → If available: USE MCP BACKEND

3. If neither available:
   → GUIDE USER TO SETUP
```

| Backend | When to Use | Reference |
| --- | --- | --- |
| **CLI** | `jira` command available | `references/commands.md` |
| **MCP** | Atlassian MCP tools available | `references/mcp.md` |
| **None** | Neither available | Guide to install CLI |

---

## Quick Reference (CLI)

> Skip this section if using MCP backend.

| Intent | Command |
| --- | --- |
| View issue | `jira issue view ISSUE-KEY` |
| List my issues | `jira issue list -a$(jira me)` |
| My in-progress | `jira issue list -a$(jira me) -s"In Progress"` |
| Create issue | `jira issue create -tType -s"Summary" -b"Description"` |
| Move/transition | `jira issue move ISSUE-KEY "State"` |
| Assign to me | `jira issue assign ISSUE-KEY $(jira me)` |
| Unassign | `jira issue assign ISSUE-KEY x` |
| Add comment | `jira issue comment add ISSUE-KEY -b"Comment text"` |
| Open in browser | `jira open ISSUE-KEY` |
| Current sprint | `jira sprint list --state active` |
| Who am I | `jira me` |

---

## Quick Reference (MCP)

> Skip this section if using CLI backend.

| Intent | MCP Tool |
| --- | --- |
| Search issues | `mcp__atlassian__searchJiraIssuesUsingJql` |
| View issue | `mcp__atlassian__getJiraIssue` |
| Create issue | `mcp__atlassian__createJiraIssue` |
| Update issue | `mcp__atlassian__editJiraIssue` |
| Get transitions | `mcp__atlassian__getTransitionsForJiraIssue` |
| Transition | `mcp__atlassian__transitionJiraIssue` |
| Add comment | `mcp__atlassian__addCommentToJiraIssue` |
| User lookup | `mcp__atlassian__lookupJiraAccountId` |
| List projects | `mcp__atlassian__getVisibleJiraProjects` |

See `references/mcp.md` for full MCP patterns.

---

## Triggers

* "create a jira ticket"
* "show me PROJ-123"
* "list my tickets"
* "move ticket to done"
* "what's in the current sprint"

---

## Issue Key Detection

Issue keys follow the pattern: `[A-Z]+-[0-9]+` (e.g., PROJ-123, ABC-1).

When a user mentions an issue key in conversation:

* **CLI:** `jira issue view KEY` or `jira open KEY`
* **MCP:** `mcp__atlassian__jira_get_issue` with the key

---

## Workflow

**Creating tickets:**

1. Research context if user references code/tickets/PRs
2. Draft ticket content
3. Review with user
4. Create using appropriate backend

**Updating tickets:**

1. Fetch issue details first
2. Check status (careful with in-progress tickets)
3. Show current vs proposed changes
4. Get approval before updating
5. Add comment explaining changes

---

## Before Any Operation

Ask yourself:

1. **What's the current state?** — Always fetch the issue first. Don't assume status, assignee, or fields are what user thinks they are.
2. **Who else is affected?** — Check watchers, linked issues, parent epics. A "simple edit" might notify 10 people.
3. **Is this reversible?** — Transitions may have one-way gates. Some workflows require intermediate states. Description edits have no undo.
4. **Do I have the right identifiers?** — Issue keys, transition IDs, account IDs. Display names don't work for assignment (MCP).

---

## NEVER

* **NEVER transition without fetching current status** — Workflows may require intermediate states. "To Do" → "Done" might fail silently if "In Progress" is required first.
* **NEVER assign using display name (MCP)** — Only account IDs work. Always call `lookupJiraAccountId` first, or assignment silently fails.
* **NEVER edit description without showing original** — Jira has no undo. User must see what they're replacing.
* **NEVER use `--no-input` without all required fields (CLI)** — Fails silently with cryptic errors. Check project's required fields first.
* **NEVER assume transition names are universal** — "Done", "Closed", "Complete" vary by project. Always get available transitions first.
* **NEVER bulk-modify without explicit approval** — Each ticket change notifies watchers. 10 edits = 10 notification storms.

---

## Safety

* Always show the command/tool call before running it
* Always get approval before modifying tickets
* Preserve original information when editing
* Verify updates after applying
* Always surface authentication issues clearly so the user can resolve them

---

## No Backend Available

If neither CLI nor MCP is available, guide the user:

```text
To use Jira, you need one of:

1. **jira CLI** (recommended):
   https://github.com/ankitpokhrel/jira-cli

   Install: brew install ankitpokhrel/jira-cli/jira-cli
   Setup:   jira init

2. **Atlassian MCP**:
   Configure in your MCP settings with Atlassian credentials.
```

---

## Deep Dive

**LOAD reference when:**

* Creating issues with complex fields or multi-line content
* Building JQL queries beyond simple filters
* Troubleshooting errors or authentication issues
* Working with transitions, linking, or sprints

**Do NOT load reference for:**

* Simple view/list operations (Quick Reference above is sufficient)
* Basic status checks (`jira issue view KEY`)
* Opening issues in browser

| Task | Load Reference? |
| --- | --- |
| View single issue | No |
| List my tickets | No |
| Create with description | **Yes** — CLI needs `/tmp` pattern |
| Transition issue | **Yes** — need transition ID workflow |
| JQL search | **Yes** — for complex queries |
| Link issues | **Yes** — MCP limitation, need script |

References:

* CLI patterns: `references/commands.md`
* MCP patterns: `references/mcp.md`

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
