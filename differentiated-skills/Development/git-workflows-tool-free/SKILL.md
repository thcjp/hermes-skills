---
slug: git-workflows-tool-free
name: git-workflows-tool-free
version: "1.0.0"
displayName: Git高级操作免费版
summary: Git 进阶操作助手，涵盖交互式变基、二分查找、工作树与引用日志恢复。
license: MIT
edition: free
description: |-
  面向进阶开发者的 Git 高级操作工具，覆盖 add/commit/push 之外的核心进阶场景。

  核心能力:
  - 交互式变基（rebase）整理提交历史
  - 二分查找（bisect）定位引入缺陷的提交
  - 工作树（worktree）并行多分支开发
  - 引用日志（reflog）恢复丢失的提交

  适用场景:
  - 合并前清理提交历史
  - 定位回归缺陷的引入提交
  - 同时处理多个分支任务
  - 误操作后的提交恢复

  差异化: 免费版聚焦开发者日常高频的进阶操作，提供交互式变基与二分查找的完整指引，开箱即用。

  触发关键词: 交互式变基, rebase, 二分查找, bisect, 工作树, worktree, 引用日志, reflog, 提交恢复, 樱桃挑选
tags:
- 开发工具
- 版本控制
- Git进阶
tools:
- read
- exec
---

# Git 高级操作助手（免费版）

## 概述

本工具为进阶开发者提供超越基础 add/commit/push 的 Git 操作指引，涵盖交互式变基、二分查找、工作树、引用日志恢复、樱桃挑选等核心场景。通过自然语言指令驱动，帮助开发者清理提交历史、定位缺陷来源、并行处理多分支任务，并在误操作后快速恢复。免费版聚焦个人开发者最常用的高频进阶操作，提供完整的命令模板与示例。

## 核心能力

| 能力模块 | 描述 | 典型用法 |
| --- | --- | --- |
| 交互式变基 | 整理、合并、重排、编辑提交 | `帮我合并最近 5 个提交` |
| 二分查找 | 定位引入缺陷的提交 | `用 bisect 找到引入 bug 的提交` |
| 工作树 | 并行处理多个分支 | `创建工作树处理紧急修复` |
| 引用日志恢复 | 恢复丢失的提交和分支 | `恢复误删的提交` |
| 樱桃挑选 | 跨分支复制特定提交 | `把这个提交挑选到 main 分支` |

## 使用场景

### 场景一：合并前清理提交历史

功能分支包含多个琐碎提交，合并前需要整理成清晰的提交序列。

```text
用户：我的功能分支有 5 个琐碎提交，合并前想整理一下

助手：使用交互式变基

1. 启动变基
   git rebase -i HEAD~5

2. 编辑器中会显示提交列表
   pick a1b2c3d 添加用户模型
   pick e4f5g6h 修复模型拼写错误
   pick i7j8k9l 添加用户控制器
   pick m0n1o2p 添加用户路由
   pick q3r4s5t 修复控制器导入

3. 修改操作指令（合并修复提交）
   pick a1b2c3d 添加用户模型
   fixup e4f5g6h 修复模型拼写错误
   pick i7j8k9l 添加用户控制器
   fixup q3r4s5t 修复控制器导入
   pick m0n1o2p 添加用户路由

4. 保存退出后自动完成变基

5. 如需放弃变基
   git rebase --abort

6. 如遇冲突解决后继续
   git add .
   git rebase --continue
```

### 场景二：定位引入缺陷的提交

线上发现一个回归缺陷，需要快速找到是哪个提交引入的。

```text
用户：登录功能在某个提交后坏了，帮我用 bisect 找出来

助手：
1. 启动二分查找
   git bisect start

2. 标记当前版本为坏
   git bisect bad

3. 标记已知正常的版本
   git bisect good v1.2.0

4. Git 会自动切换到中间提交，测试后标记
   git bisect good   # 这个提交正常
   git bisect bad    # 这个提交有问题

5. 重复直到定位到具体提交

6. 完成后重置
   git bisect reset
```

### 场景三：同时处理多个分支任务

正在开发功能时收到紧急修复任务，不想丢失当前工作。

```bash
# 创建工作树处理紧急修复
git worktree add ../project-hotfix hotfix/urgent-fix

# 创建新分支的工作树
git worktree add ../project-feature -b feature/new-thing

# 查看所有工作树
git worktree list

# 在工作树中完成工作后移除
cd ../project-hotfix
# 完成修复并推送
cd ../project
git worktree remove ../project-hotfix

# 清理无效的工作树引用
git worktree prune
```

## 快速开始

### 交互式变基命令速查

```bash
git rebase -i HEAD~5          # 变基最近 5 个提交
git rebase -i main            # 变基到 main 分支
git rebase --abort            # 取消变基
git rebase --continue         # 解决冲突后继续
git rebase --skip             # 跳过当前提交
```

变基操作指令：

| 指令 | 作用 | 说明 |
| --- | --- | --- |
| pick | 保留提交 | 使用提交原样 |
| reword | 修改信息 | 保留提交但修改提交信息 |
| edit | 暂停编辑 | 停在此提交进行修改 |
| squash | 合并保留信息 | 合并到上一个提交，保留两条信息 |
| fixup | 合并丢弃信息 | 合并到上一个提交，丢弃提交信息 |
| drop | 删除提交 | 完全移除该提交 |

### 自动变基（autosquash）

```bash
# 创建修复提交（自动标记目标）
git commit --fixup=a1b2c3d
git commit --squash=a1b2c3d

# 自动整理
git rebase -i --autosquash main
```

### 二分查找自动化

```bash
# 手动二分
git bisect start
git bisect bad
git bisect good v1.2.0

# 自动化二分（带测试脚本）
git bisect start HEAD v1.2.0
git bisect run ./test-for-bug.sh

# 测试脚本示例
cat > /tmp/test-for-bug.sh << 'EOF'
#!/bin/bash
npm test -- --grep "login should redirect" 2>/dev/null
EOF
chmod +x /tmp/test-for-bug.sh
git bisect run /tmp/test-for-bug.sh

# 跳过无法构建的提交
git bisect skip
```

## 配置示例

### 引用日志恢复操作

```bash
# 查看所有操作记录
git reflog
git reflog show feature/my-branch
git reflog --date=relative

# 恢复到指定状态
git reset --hard HEAD@{2}      # 回到 2 步之前的状态
git reset --hard ghi789        # 回到指定提交

# 恢复误删的分支
git branch recovered-branch abc123

# 查找丢失的提交
git fsck --unreachable | grep commit

# 查找丢弃的暂存
git stash list
git log --walk-reflogs --all -- stash
```

### 樱桃挑选操作

```bash
# 挑选单个提交
git cherry-pick abc123

# 挑选多个提交
git cherry-pick abc123 def456 ghi789

# 挑选提交范围
git cherry-pick abc123..ghi789

# 不自动提交
git cherry-pick --no-commit abc123

# 冲突处理
git add resolved-file.ts
git cherry-pick --continue
git cherry-pick --abort
```

## 最佳实践

1. **变基仅限本地分支**：永远不要变基已推送到共享分支的提交

2. **引用日志是安全网**：误操作后 90 天内提交均可恢复
   ```bash
   git reflog
   ```

3. **工作树比多克隆更高效**：工作树共享 .git 存储，节省磁盘空间

4. **自动化二分更可靠**：`git bisect run` 配合测试脚本消除人为错误

5. **使用 fixup 提交**：开发时用 `--fixup` 标记，合并前统一整理
   ```bash
   git commit --fixup=目标提交
   git rebase -i --autosquash main
   ```

6. **樱桃挑选后测试**：跨分支复制提交后务必运行测试

## 常见问题

### Q1：变基时冲突太多怎么办？

```bash
# 放弃变基
git rebase --abort

# 或逐个解决
git status
# 编辑冲突文件
git add .
git rebase --continue

# 跳过无法解决的提交
git rebase --skip
```

### Q2：bisect 时遇到构建失败的提交？

```bash
git bisect skip                    # 跳过当前提交
git bisect skip v1.3.0..v1.3.5    # 跳过指定范围
```

### Q3：如何查看某个文件的历史变更？

```bash
# 追踪文件重命名的历史
git log --follow --oneline -- src/auth.ts

# 查看文件每行最后修改者
git blame src/auth.ts
git blame -L 50,70 src/auth.ts    # 指定行范围

# 查找字符串被添加/删除的提交
git log -S "function oldName" --oneline
git log -G "TODO.*hack" --oneline
```

### Q4：工作树无法删除怎么办？

```bash
# 强制删除
git worktree remove --force ../project-hotfix

# 清理无效引用
git worktree prune
```

### Q5：如何恢复 reset --hard 丢失的提交？

```bash
git reflog                        # 找到丢失的提交哈希
git reset --hard abc123           # 恢复到该提交
```

### Q6：樱桃挑选冲突如何处理？

```bash
# 查看冲突文件
git status

# 解决冲突后
git add .
git cherry-pick --continue

# 放弃樱桃挑选
git cherry-pick --abort
```

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Git 版本**: 建议 2.20 及以上

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Git | 命令行工具 | 必需 | 系统包管理器安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- 自动化二分查找需要可执行的测试脚本

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 执行 Git 高级操作，所有功能依赖命令行执行能力
