---
slug: git-cli
name: git-cli
version: "1.0.1"
displayName: Git cli
summary: Helper for using the Git CLI to inspect, stage, commit, branch, and synchronize
  code changes. Use...
license: MIT-0
description: |-
  Helper for using the Git CLI to inspect, stage, commit, branch, and
  synchronize code changes。Use。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Git cli

Use this skill when the user asks about **Git from the command line**: what changed, staging/committing, branching, push/pull, stashing, history, tags, merge/rebase, or cloning.

## Your Workflow

1. **Confirm context**: Ensure Git is on PATH and the user is in (or will run commands in) a repo. If unsure, suggest `git status` or run `scripts/is-repo.sh` from the skill directory.
2. **Safety first**: Prefer read-only commands (`git status`, `git diff`, `git log`). Do not suggest destructive commands (`git reset --hard`, `git clean -fdx`, `git push --force`) unless the user explicitly asks and understands the risk. For recovery, use `git reflog` to find a commit before suggesting reset/checkout.
3. **Give the right level of detail**:
   * **Quick answer**: Use the Quick Reference table below and reply with the exact command(s).
   * **Step-by-step or edge cases**: Point to or quote from [reference/](/api/v1/skills/git-cli/file?path=reference&ownerHandle=openlang-cn) (e.g. [reference/workflows.md](/api/v1/skills/git-cli/file?path=reference%2Fworkflows.md&ownerHandle=openlang-cn), [reference/troubleshooting.md](/api/v1/skills/git-cli/file?path=reference%2Ftroubleshooting.md&ownerHandle=openlang-cn)).
   * **Automation / repeatable checks**: Use or adapt scripts in [scripts/](/api/v1/skills/git-cli/file?path=scripts&ownerHandle=openlang-cn) and tell the user how to run them.
   * **Templates** (commit message, .gitignore): Use or copy from [assets/](/api/v1/skills/git-cli/file?path=assets&ownerHandle=openlang-cn).

## Quick Reference (use this first)

| Task | Command |
| --- | --- |
| State & diff | `git status` · `git diff` · `git diff --staged` · `git diff --stat` |
| Stage / unstage | `git add <path>` or `git add .` · `git restore --staged <path>` |
| Commit | `git commit -m "message"` |
| Branch | `git branch` · `git branch -a` · `git switch -c new` · `git switch existing` |
| Sync remote | `git fetch` · `git pull` · `git push -u origin <branch>` then `git push` |
| Stash | `git stash` · `git stash list` · `git stash apply` / `git stash pop` |
| History | `git log --oneline --decorate --graph -n 20` · `git blame <file>` |
| Clone / init | `git clone <url>` · `git init` · `git remote add origin <url>` |
| Remotes | `git remote -v` · `git remote show origin` · `git branch -vv` |
| Discard (destructive) | `git restore <file>` (working tree) · `git restore --staged <file>` (unstage) |
| Amend | `git commit --amend --no-edit` or `-m "message"` |
| Tags | `git tag` · `git tag v1.0` · `git push origin v1.0` or `--tags` |
| Merge / rebase | `git merge <branch>` · `git rebase <branch>` · conflict → fix → `git add` → `git commit` or `git rebase --continue` |

## Where to Look

| Need | Location |
| --- | --- |
| Full command list, options, examples | [reference/commands.md](/api/v1/skills/git-cli/file?path=reference%2Fcommands.md&ownerHandle=openlang-cn) |
| Step-by-step workflows (branch, release, conflict) | [reference/workflows.md](/api/v1/skills/git-cli/file?path=reference%2Fworkflows.md&ownerHandle=openlang-cn) |
| Errors, recovery, detached HEAD, .gitignore | [reference/troubleshooting.md](/api/v1/skills/git-cli/file?path=reference%2Ftroubleshooting.md&ownerHandle=openlang-cn) |
| Run checks (is repo, status summary, branch info) | [scripts/](/api/v1/skills/git-cli/file?path=scripts&ownerHandle=openlang-cn) — run from repo root |
| Commit message or .gitignore template | [assets/](/api/v1/skills/git-cli/file?path=assets&ownerHandle=openlang-cn) |

## Scripts (run from repository root)

* **scripts/is-repo.sh** — Exit 0 if current dir is a Git repo, else 1. Use to confirm context before suggesting commands.
* **scripts/status-summary.sh** — Short status + branch + last commit. Use when user asks "what’s my current state?"
* **scripts/branch-list.sh** — Local and remote branches with upstream. Use when user asks about branches or push target.

On Windows: run in Git Bash or WSL (e.g. `bash scripts/status-summary.sh`).

## Assets

* **assets/commit-msg-template.txt** — Template for conventional or structured commit messages; suggest when user asks for commit message format.
* **assets/gitignore-common.txt** — Common .gitignore patterns; suggest when user has many untracked files or asks for .gitignore examples.

When the user needs a diagram (e.g. branch/merge flow), describe it in text or point to reference; only create or reference images in assets/ if the user explicitly asks for a visual.

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

- Helper for using the Git CLI to inspect, stage, commit, branch, and
  synchronize code changes
- 触发关键词: stage, using, inspect, git, helper, commit, cli

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

### Q1: 如何开始使用Git cli？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Git cli有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
