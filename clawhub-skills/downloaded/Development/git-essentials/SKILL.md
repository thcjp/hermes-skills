---
slug: git-essentials
name: git-essentials
version: "1.0.0"
displayName: Git Essentials
summary: "版本控制/分支/协作的Git必备命令与工作流"
  collaboration.
license: MIT
description: |-
  Essential Git commands and workflows for version control, branching,
  and collaboration。核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全...
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Git Essentials

Essential Git commands for version control and collaboration.

## Initial Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

git init

git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git custom-name
```

## Basic Workflow

### Staging and committing

```bash
git status

git add file.txt
git add .
git add -A  # All changes including deletions

git commit -m "Commit message"

git commit -am "Message"

git commit --amend -m "New message"
git commit --amend --no-edit  # Keep message
```

### Viewing changes

```bash
git diff

git diff --staged

git diff file.txt

git diff commit1 commit2
```

## Branching & Merging

### Branch management

```bash
git branch
git branch -a  # Include remote branches

git branch feature-name

git checkout feature-name
git switch feature-name  # Modern alternative

git checkout -b feature-name
git switch -c feature-name

git branch -d branch-name
git branch -D branch-name  # Force delete

git branch -m old-name new-name
```

### Merging

```bash
git merge feature-name

git merge --no-ff feature-name

git merge --abort

git diff --name-only --diff-filter=U
```

## Remote Operations

### Managing remotes

```bash
git remote -v

git remote add origin https://github.com/user/repo.git

git remote set-url origin https://github.com/user/new-repo.git

git remote remove origin
```

### Syncing with remote

```bash
git fetch origin

git pull

git pull --rebase

git push

git push -u origin branch-name

git push --force-with-lease
```

## History & Logs

### Viewing history

```bash
git log

git log --oneline

git log --graph --oneline --all

git log -5

git log --author="Name"

git log --since="2 weeks ago"
git log --until="2024-01-01"

git log -- file.txt
```

### Searching history

```bash
git log --grep="bug fix"

git log -S "function_name"

git blame file.txt

git bisect start
git bisect bad
git bisect good commit-hash
```

## Undoing Changes

### Working directory

```bash
git restore file.txt
git checkout -- file.txt  # Old way

git restore .
```

### Staging area

```bash
git restore --staged file.txt
git reset HEAD file.txt  # Old way

git reset
```

### Commits

```bash
git reset --soft HEAD~1

git reset --hard HEAD~1

git revert commit-hash

git reset --hard commit-hash
```

## Stashing

```bash
git stash

git stash save "Work in progress"

git stash list

git stash apply

git stash pop

git stash apply stash@{2}

git stash drop stash@{0}

git stash clear
```

## Rebasing

```bash
git rebase main

git rebase -i HEAD~3

git rebase --continue

git rebase --skip

git rebase --abort
```

## Tags

```bash
git tag

git tag v1.0.0

git tag -a v1.0.0 -m "Version 1.0.0"

git tag v1.0.0 commit-hash

git push origin v1.0.0

git push --tags

git tag -d v1.0.0
git push origin --delete v1.0.0
```

## Advanced Operations

### Cherry-pick

```bash
git cherry-pick commit-hash

git cherry-pick -n commit-hash
```

### Submodules

```bash
git submodule add https://github.com/user/repo.git path/

git submodule init

git submodule update

git clone --recursive https://github.com/user/repo.git
```

### Clean

```bash
git clean -n

git clean -f

git clean -fd

git clean -fdx
```

## Common Workflows

**Feature branch workflow:**

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
git checkout main
git pull
git branch -d feature/new-feature
```

**Hotfix workflow:**

```bash
git checkout main
git pull
git checkout -b hotfix/critical-bug
git commit -am "Fix critical bug"
git push -u origin hotfix/critical-bug
git checkout main && git pull
```

**Syncing fork:**

```bash
git remote add upstream https://github.com/original/repo.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## Useful Aliases

Add to `~/.gitconfig`:

```ini
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    unstage = reset HEAD --
    last = log -1 HEAD
    visual = log --graph --oneline --all
    amend = commit --amend --no-edit
```

## Tips

* Commit often, perfect later (interactive rebase)
* Write meaningful commit messages
* Use `.gitignore` for files to exclude
* Never force push to shared branches
* Pull before starting work
* Use feature branches, not main
* Rebase feature branches before merging
* Use `--force-with-lease` instead of `--force`

## Common Issues

**Undo accidental commit:**

```bash
git reset --soft HEAD~1
```

**Recover deleted branch:**

```bash
git reflog
git checkout -b branch-name <commit-hash>
```

**Fix wrong commit message:**

```bash
git commit --amend -m "Correct message"
```

**Resolve merge conflicts:**

```bash
git add resolved-files
git commit  # Or git merge --continue
```

## Documentation

Official docs: <https://git-scm.com/doc>
Pro Git book: <https://git-scm.com/book>
Visual Git guide: <https://marklodato.github.io/visual-git-guide/>

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

- Essential Git commands and workflows for version control, branching,
  and collaboration
- 触发关键词: workflows, version, essentials, git, commands, essential, control

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

### Q1: 如何开始使用Git Essentials？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Git Essentials有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
