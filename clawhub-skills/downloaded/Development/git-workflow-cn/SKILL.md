---
slug: git-workflow-cn
name: git-workflow-cn
version: "1.1.0"
displayName: Git Workflow Cn
summary: Git 工作流助手 - 分支管理、冲突解决、提交规范。适合：开发者、团队协作。
license: MIT-0
description: |-
  Git 工作流助手 - 分支管理、冲突解决、提交规范。适合：开发者、团队协作。

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 冲突解决, 提交规范, 适合, 分支管理, workflow, git, 工作流助手
tags:
- Development
- Automation
tools:
- read
- exec
---

# Git Workflow Cn

Git 分支管理、冲突解决、提交规范，提升团队协作效率。

## 核心功能

| 功能 | 描述 |
| --- | --- |
| 分支管理 | 创建、切换、合并分支 |
| 冲突解决 | 识别和解决冲突 |
| 提交规范 | Conventional Commits |
| 常见问题 | 撤销、回滚、恢复 |

## 使用方法

### 分支操作

```text
创建并切换到新分支 feature/login
```

### 冲突解决

```text
帮我解决 Git 合并冲突
```

### 提交建议

```text
为这些改动生成符合规范的提交信息
```

## 常用命令速查

### 基础操作

```bash
git init                           # 初始化仓库
git clone URL                      # 克隆仓库

git config --global user.name "Your Name"
git config --global user.email "email@example.com"

git status                         # 查看状态
git log --oneline                  # 简洁日志
git log --graph --oneline --all    # 图形化日志
git diff                           # 查看改动
git show COMMIT_ID                 # 查看提交详情
```

### 分支管理

```bash
git branch                         # 本地分支
git branch -a                      # 所有分支
git branch -r                      # 远程分支

git branch feature/login           # 创建分支
git checkout -b feature/login      # 创建并切换
git switch -c feature/login        # 新语法

git checkout feature/login         # 切换分支
git switch feature/login           # 新语法

git merge feature/login            # 合并分支
git merge --no-ff feature/login    # 禁用快进

git branch -d feature/login        # 安全删除
git branch -D feature/login        # 强制删除
git push origin --delete feature/login  # 删除远程分支
```

### 远程操作

```bash
git remote -v                      # 查看远程仓库
git remote add origin URL          # 添加远程
git remote set-url origin URL      # 修改远程地址

git fetch origin                   # 获取更新
git pull origin main               # 拉取并合并
git push origin main               # 推送
git push -u origin feature/login   # 推送并设置上游

git remote prune origin            # 清理无效引用
git fetch --all --prune            # 获取并清理
```

### 暂存操作

```bash
git stash                          # 暂存当前修改
git stash save "message"           # 带消息暂存
git stash list                     # 查看暂存列表
git stash pop                      # 恢复并删除
git stash apply                    # 恢复但不删除
git stash drop stash@{0}           # 删除指定暂存
git stash clear                    # 清空暂存
```

## 提交规范

### Conventional Commits

```text
<type>(<scope>): <subject>

<body>

<footer>
```

### Type 类型

| Type | 描述 | 示例 |
| --- | --- | --- |
| feat | 新功能 | feat(auth): 添加登录功能 |
| fix | 修复 bug | fix(api): 修复接口超时 |
| docs | 文档更新 | docs(readme): 更新安装说明 |
| style | 代码格式 | style: 格式化代码 |
| refactor | 重构 | refactor(utils): 优化工具函数 |
| perf | 性能优化 | perf(list): 优化列表渲染 |
| test | 测试 | test(auth): 添加登录测试 |
| chore | 构建/工具 | chore: 更新依赖 |
| ci | CI 配置 | ci: 添加 GitHub Actions |
| revert | 回滚 | revert: 回滚登录功能 |

### 提交示例

```bash
git commit -m "feat(user): 添加用户注册功能"

git commit -m "fix(payment): 修复支付金额计算错误"

git commit -m "docs(api): 更新接口文档"

git commit -m "refactor(auth): 重构认证逻辑

- 提取公共方法
- 优化错误处理
- 添加单元测试"

git commit -m "feat(api)!: 修改 API 响应格式

BREAKING CHANGE: 响应格式从 {code, data} 改为 {status, result}"
```

## 工作流模式

### Git Flow

```bash
git flow init

git flow feature start login
git flow feature finish login

git flow release start v1.0.0
git flow release finish v1.0.0

git flow hotfix start fix-login-bug
git flow hotfix finish fix-login-bug
```

### GitHub Flow

```bash
git checkout -b feature/login main

git add .
git commit -m "feat: 添加登录功能"
git push origin feature/login

git checkout main
git pull origin main
git merge feature/login
git push origin main
```

### GitLab Flow

```bash

git checkout -b feature/login main
git push origin feature/login

git checkout main
git merge feature/login

git checkout staging
git merge main
git push origin staging

git checkout production
git merge staging
git push origin production
```

## 冲突解决

### 识别冲突

```bash
git status

<<<<<<< HEAD
当前分支内容
=======
合并分支内容
>>>>>>> feature/login
```

### 解决冲突

```bash
git add .
git commit
```

### 冲突工具

```bash
git mergetool

git config --global merge.tool code
git config --global mergetool.code.cmd 'code --wait $MERGED'

git diff HEAD                     # 与 HEAD 比较
git diff --ours                   # 使用当前版本
git diff --theirs                 # 使用合并版本
```

## 常见问题解决

### 撤销操作

```bash
git checkout -- file.txt
git restore file.txt              # 新语法

git reset HEAD file.txt
git restore --staged file.txt     # 新语法

git reset --soft HEAD~1

git reset --hard HEAD~1

git commit --amend -m "新信息"
```

### 回滚代码

```bash
git revert COMMIT_ID

git revert COMMIT_ID1..COMMIT_ID2

git revert --no-commit COMMIT_ID
```

### 恢复删除

```bash
git checkout COMMIT_ID -- file.txt

git reflog                        # 查找提交
git reset --hard COMMIT_ID        # 恢复

git reflog                        # 找到分支最后的提交
git checkout -b branch_name COMMIT_ID
```

### 清理仓库

```bash
git clean -n                      # 预览
git clean -f                      # 删除文件
git clean -fd                     # 删除文件和目录

git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/file' \
  --prune-empty --tag-name-filter cat -- --all

bfg --delete-folders folder_name
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

## 别名配置

```bash

[alias]
  co = checkout
  br = branch
  ci = commit
  st = status
  unstage = reset HEAD --
  last = log -1 HEAD
  visual = log --graph --oneline --all
  amend = commit --amend --no-edit
  undo = reset --soft HEAD~1
  wip = !git add -A && git commit -m 'WIP'
```

## 注意事项

* 提交前先拉取最新代码
* 功能分支及时合并
* 避免直接提交到 main
* 重要操作先备份

---

创建：2026-03-12
版本：1.0

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
