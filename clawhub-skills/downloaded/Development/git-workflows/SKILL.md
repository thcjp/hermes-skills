---
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
summary: "高级git操作rebase/bisect/worktree/reflog/子树/子模块"
---
# Git Workflows

Advanced git operations for real-world development. Covers interactive rebase, bisect, worktree, reflog recovery, subtrees, submodules, sparse checkout, conflict resolution, and monorepo patterns.

## When to Use

* Cleaning up commit history before merging (interactive rebase)
* Finding which commit introduced a bug (bisect)
* Working on multiple branches simultaneously (worktree)
* Recovering lost commits or undoing mistakes (reflog)
* Managing shared code across repos (subtree/submodule)
* Resolving complex merge conflicts
* Cherry-picking commits across branches or forks
* Working with large monorepos (sparse checkout)

## Interactive Rebase

### Squash, reorder, edit commits

```bash
git rebase -i HEAD~5

git rebase -i main
```

The editor opens with a pick list:

```text
pick a1b2c3d Add user model
pick e4f5g6h Fix typo in user model
pick i7j8k9l Add user controller
pick m0n1o2p Add user routes
pick q3r4s5t Fix import in controller
```

Commands available:

```text
pick   = use commit as-is
reword = use commit but edit the message
edit   = stop after this commit to amend it
squash = merge into previous commit (keep both messages)
fixup  = merge into previous commit (discard this message)
drop   = remove the commit entirely
```

### Common patterns

```bash
pick a1b2c3d Add user model
fixup e4f5g6h Fix typo in user model
pick i7j8k9l Add user controller
fixup q3r4s5t Fix import in controller
pick m0n1o2p Add user routes

pick i7j8k9l Add user controller
pick m0n1o2p Add user routes
pick a1b2c3d Add user model

git reset HEAD~
git add src/model.ts
git commit -m "Add user model"
git add src/controller.ts
git commit -m "Add user controller"
git rebase --continue
```

### Autosquash (commit messages that auto-arrange)

```bash
git commit --fixup=a1b2c3d -m "Fix typo"
git commit --squash=a1b2c3d -m "Additional changes"

git rebase -i --autosquash main
```

### Abort or continue

```bash
git rebase --abort      # Cancel and restore original state
git rebase --continue   # Continue after resolving conflicts or editing
git rebase --skip       # Skip the current commit and continue
```

## Bisect (Find the Bug)

### Binary search through commits

```bash
git bisect start

git bisect bad

git bisect good v1.2.0

git bisect good   # if this commit doesn't have the bug
git bisect bad    # if this commit has the bug


git bisect reset
```

### Automated bisect (with a test script)

```bash
git bisect start HEAD v1.2.0
git bisect run ./test-for-bug.sh

cat > /tmp/test-for-bug.sh << 'EOF'
#!/bin/bash
npm test -- --grep "login should redirect" 2>/dev/null
EOF
chmod +x /tmp/test-for-bug.sh
git bisect run /tmp/test-for-bug.sh
```

### Bisect with build failures

```bash
git bisect skip

git bisect skip v1.3.0..v1.3.5
```

## Worktree (Parallel Branches)

### Work on multiple branches simultaneously

```bash
git worktree add ../myproject-hotfix hotfix/urgent-fix

git worktree add ../myproject-feature -b feature/new-thing

git worktree list

git worktree remove ../myproject-hotfix

git worktree prune
```

### Use cases

```bash
git worktree add ../review-pr-123 origin/pr-123

git worktree add ../main-tests main
cd ../main-tests && npm test

git worktree add ../compare-old release/v1.0
git worktree add ../compare-new release/v2.0
```

## Reflog (Recovery)

### See everything git remembers

```bash
git reflog

git reflog show feature/my-branch

git reflog --date=relative
```

### Recover from mistakes

```bash
git reflog
git reset --hard ghi789

git reflog
git branch recovered-branch abc123

git reflog
git reset --hard HEAD@{2}   # Go back 2 reflog entries

git fsck --unreachable | grep commit
git stash list  # if it's still there
git log --walk-reflogs --all -- stash  # find dropped stash commits
```

## Cherry-Pick

### Copy specific commits to another branch

```bash
git cherry-pick abc123

git cherry-pick abc123 def456 ghi789

git cherry-pick abc123..ghi789

git cherry-pick --no-commit abc123

git remote add upstream https://github.com/other/repo.git
git fetch upstream
git cherry-pick upstream/main~3   # 3rd commit from upstream's main
```

### Handle conflicts during cherry-pick

```bash
git add resolved-file.ts
git cherry-pick --continue

git cherry-pick --abort
```

## Subtree and Submodule

### Subtree (simpler — copies code into your repo)

```bash
git subtree add --prefix=lib/shared https://github.com/org/shared-lib.git main --squash

git subtree pull --prefix=lib/shared https://github.com/org/shared-lib.git main --squash

git subtree push --prefix=lib/shared https://github.com/org/shared-lib.git main

git subtree split --prefix=lib/shared -b shared-lib-standalone
```

### Submodule (pointer to another repo at a specific commit)

```bash
git submodule add https://github.com/org/shared-lib.git lib/shared

git clone --recurse-submodules https://github.com/org/main-repo.git

git submodule update --init --recursive

git submodule update --remote

git rm lib/shared
rm -rf .git/modules/lib/shared
```

### When to use which

```text
Subtree: Simpler, no special commands for cloners, code lives in your repo.
         Use when: shared library, vendor code, infrequent upstream changes.

Submodule: Pointer to exact commit, smaller repo, clear separation.
           Use when: large dependency, independent release cycle, many contributors.
```

## Sparse Checkout (Monorepo)

### Check out only the directories you need

```bash
git sparse-checkout init --cone

git sparse-checkout set packages/my-app packages/shared-lib

git sparse-checkout add packages/another-lib

git sparse-checkout list

git sparse-checkout disable
```

### Clone with sparse checkout (large monorepos)

```bash
git clone --filter=blob:none --sparse https://github.com/org/monorepo.git
cd monorepo
git sparse-checkout set packages/my-service

git clone --no-checkout https://github.com/org/monorepo.git
cd monorepo
git sparse-checkout set packages/my-service
git checkout main
```

## Conflict Resolution

### Understand the conflict markers

```text
<<<<<<< HEAD (or "ours")
Your changes on the current branch
=======
Their changes from the incoming branch
>>>>>>> feature-branch (or "theirs")
```

### Resolution strategies

```bash
git checkout --ours path/to/file.ts
git add path/to/file.ts

git checkout --theirs path/to/file.ts
git add path/to/file.ts

git checkout --ours .
git add .

git mergetool

git diff --cc path/to/file.ts

git show :1:path/to/file.ts   # base (common ancestor)
git show :2:path/to/file.ts   # ours
git show :3:path/to/file.ts   # theirs
```

### Rebase conflict workflow

```bash
git add fixed-file.ts
git rebase --continue

git rebase --skip
```

### Rerere (reuse recorded resolutions)

```bash
git config --global rerere.enabled true


ls .git/rr-cache/

git rerere forget path/to/file.ts
```

## Stash Patterns

```bash
git stash push -m "WIP: refactoring auth flow"

git stash push -m "partial stash" -- src/auth.ts src/login.ts

git stash push -u -m "with untracked"

git stash list

git stash apply

git stash pop

git stash apply stash@{2}

git stash show -p stash@{0}

git stash branch new-feature stash@{0}

git stash drop stash@{1}

git stash clear
```

## Blame and Log Archaeology

```bash
git blame src/auth.ts

git blame -L 50,70 src/auth.ts

git blame -w src/auth.ts

git log -S "function oldName" --oneline

git log -G "TODO.*hack" --oneline

git log --follow --oneline -- src/new-name.ts

git blame -M src/auth.ts

git log --stat --oneline -20

git log --oneline -- src/auth.ts

git show abc123
```

## Tags and Releases

```bash
git tag -a v1.2.0 -m "Release 1.2.0: Added auth module"

git tag v1.2.0

git tag -a v1.1.0 abc123 -m "Retroactive tag for release 1.1.0"

git tag -l
git tag -l "v1.*"

git push origin v1.2.0      # Single tag
git push origin --tags       # All tags

git tag -d v1.2.0            # Local
git push origin --delete v1.2.0  # Remote
```

## Tips

* `git rebase -i` is the single most useful advanced git command. Learn it first.
* Never rebase commits that have been pushed to a shared branch. Rebase your local/feature work only.
* `git reflog` is your safety net. If you lose commits, they're almost always recoverable within 90 days.
* `git bisect run` with an automated test is faster than manual binary search and eliminates human error.
* Worktrees are cheaper than multiple clones — they share `.git` storage.
* Prefer `git subtree` over `git submodule` unless you have a specific reason. Subtrees are simpler for collaborators.
* Enable `rerere` globally. It remembers conflict resolutions so you never solve the same conflict twice.
* `git stash push -m "description"` is much better than bare `git stash`. You'll thank yourself when you have 5 stashes.
* `git log -S "string"` (pickaxe) is the fastest way to find when a function or variable was added or removed.

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

- Advanced git operations beyond add/commit/push
- Use when rebasing, bisecting
  bugs, using worktree
- 触发关键词: workflows, operations, git, push, advanced, commit, beyond

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

### Q1: 如何开始使用Git Workflows？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Git Workflows有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
