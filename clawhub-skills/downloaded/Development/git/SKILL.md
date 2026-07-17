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
  recovery, team workflows, an...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: rebases, commits, git, conflict, merges, branches
tags:
- Development
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
