---
slug: "git-essentials"
name: "git-essentials"
version: "1.1.0"
displayName: "Git核心操作"
summary: "涵盖Git版本控制核心命令与工作流,包括分支、合并、变基、标签与冲突处理"
license: "Proprietary"
description: |-
  涵盖Git版本控制核心命令与工作流,包括初始配置、基础工作流、分支管理、合并、远程操作、历史查询、撤销变更、暂存、变基、标签、高级操作(cherry-pick、子模块、clean)与常见工作流模式。提供冲突解决、分支恢复与安全强制推送等错误处理策略。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 研发工具
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Git核心操作

涵盖Git版本控制核心命令与工作流,支持分支管理、合并、变基、标签与协作场景。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| **常见工作流模式**: 特性分支工作流、热修复工作流、Fork同步工作流 | 支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 初始配置

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

git init

git clone https://git.example.com/user/repo.git
git clone https://git.example.com/user/repo.git custom-name
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

- **初始配置与仓库初始化**: 通过 `git config --global` 设置用户信息,使用 `git init` 初始化仓库,`git clone` 克隆远程仓库
- **基础工作流(暂存与提交)**: 使用 `git add` 暂存变更,`git commit -m` 提交,`git commit --amend` 修改提交,`git diff` 查看变更
- **分支管理与切换**: 通过 `git branch` 创建/删除/重命名分支,`git switch -c` 创建并切换,`git branch -D` 强制删除
- **合并与冲突处理**: 使用 `git merge --no-ff` 保留合并记录,`git merge --abort` 取消合并,`git diff --name-only --diff-filter=U` 查看冲突文件
- **远程仓库操作**: 通过 `git remote add` 添加远程,`git fetch` 获取,`git pull --rebase` 变基拉取,`git push -u` 推送并设置上游
- **历史查询与搜索**: 使用 `git log --graph --oneline --all` 可视化历史,`git log -S` 搜索代码变更,`git blame` 追溯行级修改,`git bisect` 二分定位Bug
- **撤销与恢复**: 通过 `git restore` 恢复工作区,`git reset --soft HEAD~1` 撤销提交保留变更,`git revert` 安全回退,`git reflog` 恢复误删分支
- **暂存(stash)管理**: 使用 `git stash save` 暂存工作区,`git stash apply stash@{2}` 应用指定暂存,`git stash clear` 清空所有暂存
- **交互式变基**: 通过 `git rebase -i HEAD~3` 压缩/重排/编辑最近3个提交,`git rebase --continue` 继续变基,`git rebase --abort` 取消
- **标签管理**: 使用 `git tag -a v1.0.0 -m` 创建附注标签,`git push origin v1.0.0` 推送标签,`git tag -d` 删除标签
- **高级操作(cherry-pick/子模块/clean)**: 通过 `git cherry-pick` 选择性应用提交,`git submodule add` 添加子模块,`git clean -fdx` 清理未跟踪文件
- **常见工作流模式**: 特性分支工作流、热修复工作流、Fork同步工作流
### 初始配置与仓库初始化

执行初始配置与仓库初始化操作,处理用户输入并返回结果。

**输入**: 用户提供初始配置与仓库初始化所需的参数和指令。

**输出**: 返回初始配置与仓库初始化的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`初始配置与仓库初始化`相关配置参数进行设置
### 基础工作流(暂存与提交)

执行基础工作流(暂存与提交)操作,处理用户输入并返回结果。

**输入**: 用户提供基础工作流(暂存与提交)所需的参数和指令。

**输出**: 返回基础工作流(暂存与提交)的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`基础工作流(暂存与提交)`相关配置参数进行设置
### 分支管理与切换

执行分支管理与切换操作,处理用户输入并返回结果。

**输入**: 用户提供分支管理与切换所需的参数和指令。

**输出**: 返回分支管理与切换的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`分支管理与切换`相关配置参数进行设置
#
## 基础工作流

### 暂存与提交

```bash
git status

git add file.txt
git add .
git add -A  # 包含删除的所有变更

git commit -m "Commit message"

git commit -am "Message"  # 跳过暂存直接提交已跟踪文件

git commit --amend -m "New message"
git commit --amend --no-edit  # 保留原提交信息
```

### 查看变更

```bash
git diff

git diff --staged

git diff file.txt

git diff commit1 commit2
```

## 分支与合并

### 分支管理

```bash
git branch
git branch -a  # 包含远程分支

git branch feature-name

git checkout feature-name
git switch feature-name  # 现代替代方式

git checkout -b feature-name
git switch -c feature-name

git branch -d branch-name
git branch -D branch-name  # 强制删除

git branch -m old-name new-name
```

### 合并

```bash
git merge feature-name

git merge --no-ff feature-name  # 保留合并提交

git merge --abort  # 取消合并

git diff --name-only --diff-filter=U  # 列出冲突文件
```

## 远程操作

### 管理远程仓库

```bash
git remote -v

git remote add origin https://git.example.com/user/repo.git

git remote set-url origin https://git.example.com/user/new-repo.git

git remote remove origin
```

### 与远程同步

```bash
git fetch origin

git pull

git pull --rebase  # 变基方式拉取

git push

git push -u origin branch-name  # 设置上游分支

git push --force-with-lease  # 安全强制推送
```

## 历史与日志

### 查看历史

```bash
git log

git log --oneline

git log --graph --oneline --all

git log -5  # 最近5条提交

git log --author="Name"

git log --since="2 weeks ago"
git log --until="2024-01-01"

git log -- file.txt
```

### 搜索历史

```bash
git log --grep="bug fix"

git log -S "function_name"  # 搜索包含特定字符串的提交

git blame file.txt

git bisect start
git bisect bad
git bisect good commit-hash
```

## 撤销变更

### 工作区

```bash
git restore file.txt
git checkout -- file.txt  # 旧方式

git restore .
```

### 暂存区

```bash
git restore --staged file.txt
git reset HEAD file.txt  # 旧方式

git reset
```

### 提交

```bash
git reset --soft HEAD~1  # 撤销提交,保留变更在暂存区

git reset --hard HEAD~1  # 撤销提交,丢弃变更

git revert commit-hash  # 创建反向提交

git reset --hard commit-hash  # 重置到指定提交
```

## 暂存(stash)

```bash
git stash

git stash save "Work in progress"

git stash list

git stash apply

git stash pop

git stash apply stash@{2}  # 应用指定暂存

git stash drop stash@{0}  # 删除指定暂存

git stash clear  # 清空所有暂存
```

## 变基(rebase)

```bash
git rebase main

git rebase -i HEAD~3  # 交互式变基最近3个提交

git rebase --continue

git rebase --skip

git rebase --abort
```

## 标签

```bash
git tag

git tag v1.0.0

git tag -a v1.0.0 -m "Version 1.0.0"  # 附注标签

git tag v1.0.0 commit-hash  # 为指定提交打标签

git push origin v1.0.0

git push --tags

git tag -d v1.0.0  # 删除本地标签
git push origin --delete v1.0.0  # 删除远程标签
```

## 高级操作

### Cherry-pick

```bash
git cherry-pick commit-hash

git cherry-pick -n commit-hash  # 不自动提交
```

### 子模块

```bash
git submodule add https://git.example.com/user/repo.git path/

git submodule init

git submodule update

git clone --recursive https://git.example.com/user/repo.git
```

### 清理未跟踪文件

```bash
git clean -n  # 预览

git clean -f  # 删除未跟踪文件

git clean -fd  # 包含目录

git clean -fdx  # 包含.gitignore忽略的文件
```

## 常见工作流

**特性分支工作流:**

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
git checkout main
git pull
git branch -d feature/new-feature
```

**热修复工作流:**

```bash
git checkout main
git pull
git checkout -b hotfix/critical-bug
git commit -am "Fix critical bug"
git push -u origin hotfix/critical-bug
git checkout main && git pull
```

**Fork同步工作流:**

```bash
git remote add upstream https://git.example.com/original/repo.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## 使用流程

1. 使用 `git config --global` 配置用户信息,`git init` 或 `git clone` 初始化仓库
2. 通过 `git add` 暂存变更,`git commit -m` 提交,`git status` 和 `git diff` 检查状态
3. 使用 `git switch -c` 创建特性分支,开发完成后 `git merge --no-ff` 合并
4. 通过 `git push -u` 推送到远程,`git pull --rebase` 同步上游变更
5. 使用 `git stash` 临时保存工作,`git rebase -i HEAD~3` 整理提交历史
6. 遇到冲突时用 `git diff --name-only --diff-filter=U` 定位,手动解决后 `git add` 标记
7. 使用 `git tag -a v1.0.0 -m` 标记发布版本,`git push --tags` 推送标签

#
## 示例

### 示例1:特性分支开发与合并

```bash
git switch -c feature/user-auth
git add src/auth.py
git commit -m "Add user authentication with JWT"
git push -u origin feature/user-auth
git switch main
git pull --rebase
git merge --no-ff feature/user-auth
git push
git branch -d feature/user-auth
```

### 示例2:交互式变基压缩提交

```bash
git rebase -i HEAD~3
# 在编辑器中将第2、3行改为 squash,保存退出
# 合并后编辑提交信息:
# "Add login endpoint with JWT validation"
git push --force-with-lease
```

### 示例3:二分定位Bug

```bash
git bisect start
git bisect bad HEAD
git bisect good v1.2.0
# Git自动切换到中间提交,测试后标记:
git bisect good  # 或 git bisect bad
# 重复直到定位到引入Bug的提交
git bisect reset
```

### 示例4:恢复误删分支

```bash
git reflog
# 输出: a1b2c3d HEAD@{5}: commit: feature work
git checkout -b recovered-feature a1b2c3d
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 合并冲突(CONFLICT) | 两个分支修改了同一文件的同一区域 | 使用 `git diff --name-only --diff-filter=U` 定位冲突文件,手动编辑解决后 `git add`,再 `git commit` |
| 误提交到错误分支 | 在main分支直接提交了特性代码 | `git reset --soft HEAD~1` 撤销提交保留变更,`git switch -c feature` 创建正确分支后重新提交 |
| 误删分支 | 执行了 `git branch -D` 删除了未合并的分支 | 使用 `git reflog` 找到分支最后一个提交的哈希,`git checkout -b branch-name <commit-hash>` 恢复 |
| 提交信息错误 | `git commit -m` 中输入了错误的描述 | `git commit --amend -m "Correct message"` 修改最近一次提交信息,若已推送需 `git push --force-with-lease` |
| 强制推送覆盖他人提交 | 使用 `git push --force` 而非 `--force-with-lease` | 永远使用 `git push --force-with-lease`,它会检查远程是否有新提交再决定是否推送 |
| 变基中断(rebase冲突) | `git rebase` 过程中遇到冲突 | 解决冲突后 `git add`,执行 `git rebase --continue`;若无法解决可 `git rebase --abort` 回到变基前状态 |
| 拉取产生大量合并提交 | 直接 `git pull` 产生merge commit | 改用 `git pull --rebase` 将本地提交变基到远程最新提交之上 |
| 暂存丢失 | `git stash drop` 误删了需要的暂存 | 使用 `git fsck --unreachable` 找到悬空提交,`git stash apply <commit-hash>` 恢复 |
| 子模块未初始化 | 克隆含子模块的仓库后未初始化 | 执行 `git submodule init && git submodule update`,或克隆时使用 `--recursive` |
| 大文件导致push失败 | 仓库中包含超大文件 | 使用 `git clean -fdx` 清理,添加 `.gitignore`,若已提交需 `git filter-branch` 或BFG清理历史 |

## 常见问题

### Q1: `git merge` 和 `git rebase` 有什么区别,应该用哪个?
A: `git merge` 保留完整的分支历史,产生合并提交;`git rebase` 将本地提交重新应用到目标分支顶部,历史更线性。本地未推送的提交用变基整理历史,已推送的公共分支用合并保留记录。变基会改写提交哈希,已推送的分支不要变基。

### Q2: `git reset --soft`、`--mixed`和`--hard`有什么区别?
A: `--soft` 仅撤销提交,变更保留在暂存区;`--mixed`(默认)撤销提交和暂存,变更保留在工作区;`--hard` 撤销提交、暂存和工作区所有变更,不可恢复。`--hard` 慎用,除非确定不需要这些变更。

### Q3: 如何安全地强制推送?
A: 永远使用 `git push --force-with-lease` 而非 `git push --force`。`--force-with-lease` 会在远程分支有新提交时拒绝推送,防止覆盖他人工作。仅当确认远程状态符合预期时才使用强制推送,且仅限于自己的特性分支。

### Q4: `git stash` 和 `git commit` 有什么使用场景区别?
A: `git stash` 用于临时保存工作区变更(如需切换分支处理紧急Bug但当前工作未完成),变更不进入提交历史。`git commit` 是正式记录变更。stash适合短期临时保存,commit适合长期持久化。`git stash pop` 会恢复并删除暂存,`git stash apply` 恢复但保留暂存。

### Q5: 交互式变基 `git rebase -i HEAD~3` 能做什么?
A: 可以对最近3个提交执行: `pick`(保留)、`squash`(合并到上一个)、`reword`(修改提交信息)、`edit`(暂停修改)、`drop`(删除)、`reorder`(重排顺序)。常用于在推送前整理提交历史,使日志更清晰。注意只能变基未推送的提交,已推送的变基会破坏他人基于旧提交的工作。

### Q6: `git cherry-pick` 什么时候使用?
A: 当需要将某个分支上的特定提交(而非整个分支)应用到另一个分支时使用。例如在hotfix分支修复了Bug,需要将这个修复应用到main分支但不合并整个hotfix分支。`git cherry-pick <commit-hash>` 会创建一个新提交,内容与原提交相同但哈希不同。

### Q7: 如何查找引入特定Bug的提交?
A: 使用 `git bisect` 二分查找。执行 `git bisect start`,标记当前坏提交 `git bisect bad HEAD`,标记最后一个好提交 `git bisect good v1.0.0`。Git会自动切换到中间提交,测试后用 `git bisect good` 或 `git bisect bad` 标记,重复直到定位到引入Bug的确切提交,最后 `git bisect reset` 退出。

## 已知限制

- `git rebase` 会改写提交历史,已推送的公共分支不应变基
- `git reset --hard` 不可逆地丢弃工作区变更,使用前需确认
- 子模块操作复杂,克隆时需 `--recursive`,更新需 `git submodule update`
- `git clean -fdx` 会删除 `.gitignore` 中忽略的文件,使用前需预览(`-n`)
- 大文件历史清理需要特殊工具,普通命令无法彻底移除
