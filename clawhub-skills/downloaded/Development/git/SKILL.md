---
slug: git
name: git
version: "1.0.8"
displayName: Git
summary: Git commits, branches, rebases, merges, conflict resolution, history recovery,
  team workflows, an...
license: MIT-0
description: |-
  Git commits, branches, rebases, merges, conflict resolution, history
  recovery, team workflows, an。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- Development
tools:
  - - read
- exec
---

# Git

## When to Use

Use when the task involves Git repositories, branches, commits, merges, rebases, pull requests, conflict resolution, history inspection, or recovery. This skill is stateless and should be applied by default whenever Git work is part of the job.

## Quick Reference

| Topic | File |
| --- | --- |
| Essential commands | `commands.md` |
| Advanced operations | `advanced.md` |
| Branch strategies | `branching.md` |
| Conflict resolution | `conflicts.md` |
| History and recovery | `history.md` |
| Team workflows | `collaboration.md` |

## Core Rules

1. **Never force push to shared branches** — Use `--force-with-lease` on feature branches only
2. **Commit early, commit often** — Small commits are easier to review, revert, and bisect
3. **Write meaningful commit messages** — First line under 72 chars, imperative mood
4. **Pull before push** — Always `git pull --rebase` before pushing to avoid merge commits
5. **Clean up before merging** — Use `git rebase -i` to squash fixup commits

## Team Workflows

**Feature Branch Flow:**

1. `git checkout -b feature/name` from main
2. Make commits, push regularly
3. Open PR, get review
4. Squash and merge to main
5. Delete feature branch

**Hotfix Flow:**

1. `git checkout -b hotfix/issue` from main
2. Fix, test, commit
3. Merge to main AND develop (if exists)
4. Tag the release

**Daily Sync:**

```bash
git fetch --all --prune
git rebase origin/main  # or merge if team prefers
```

## Commit Messages

* Use conventional commit format: `type(scope): description`
* Keep first line under 72 characters
* Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Push Safety

* Use `git push --force-with-lease` instead of `--force` — prevents overwriting others' work
* If push rejected, run `git pull --rebase` before retrying
* Never force push to main/master branch

## Conflict Resolution

* After editing conflicted files, verify no markers remain: `grep -r "<<<\|>>>\|===" .`
* Test that code builds before completing merge
* If merge becomes complex, abort with `git merge --abort` and try `git rebase` instead

## Branch Hygiene

* Delete merged branches locally: `git branch -d branch-name`
* Clean remote tracking: `git fetch --prune`
* Before creating PR, rebase feature branch onto latest main
* Use `git rebase -i` to squash messy commits before pushing

## Safety Checklist

Before destructive operations (`reset --hard`, `rebase`, `force push`):

* Is this a shared branch? → Don't rewrite history
* Do I have uncommitted changes? → Stash or commit first
* Am I on the right branch? → `git branch` to verify
* Is remote up to date? → `git fetch` first

## Common Traps

* **git user.email wrong** — Verify with `git config user.email` before important commits
* **Empty directories** — Git doesn't track them, add `.gitkeep`
* **Submodules** — Always clone with `--recurse-submodules`
* **Detached HEAD** — Use `git switch -` to return to previous branch
* **Push rejected** — Usually needs `git pull --rebase` first
* **stash pop on conflict** — Stash disappears. Use `stash apply` instead
* **Large files** — Use Git LFS for files >50MB, never commit secrets
* **Case sensitivity** — Mac/Windows ignore case, Linux doesn't — causes CI failures

## Recovery Commands

* Undo last commit keeping changes: `git reset --soft HEAD~1`
* Discard unstaged changes: `git restore filename`
* Find lost commits: `git reflog` (keeps ~90 days of history)
* Recover deleted branch: `git checkout -b branch-name <sha-from-reflog>`
* Use `git add -p` for partial staging when commit mixes multiple changes

## Debugging with Bisect

Find the commit that introduced a bug:

```bash
git bisect start
git bisect bad                    # current commit is broken
git bisect good v1.0.0            # this version worked
git bisect good                   # or git bisect bad
git bisect reset                  # return to original branch
```

## Quick Summary

```bash
git status -sb                    # short status with branch
git log --oneline -5              # last 5 commits
git shortlog -sn                  # contributors by commit count
git diff --stat HEAD~5            # changes summary last 5 commits
git branch -vv                    # branches with tracking info
git stash list                    # pending stashes
```

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `gitlab` — GitLab CI/CD and merge requests
* `docker` — Containerization workflows
* `code` — Code quality and best practices

## Feedback

* If useful: `
* Stay updated: `

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

- Git commits, branches, rebases, merges, conflict resolution, history
  recovery, team workflows, an
- 触发关键词: rebases, commits, git, conflict, merges, branches

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

### Q1: 如何开始使用Git？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Git有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
