---
slug: "git-cli"
name: "git-cli"
version: 1.0.2
displayName: "Git cli"
summary: "用Git CLI检查/暂存/提交/分支/同步代码变更"
license: "Proprietary"
description: |-
  Helper for using the Git CLI to inspect, stage, commit, branch, and
  synchronize code changes。Use。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求.
tags:
  - Development
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Git cli

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

- Git 仓库检查：查看状态、差异、日志、分支、远程仓库、暂存区内容
- 代码暂存与提交：智能选择文件、生成规范化提交信息（Conventional Commits）
- 分支管理：创建、切换、合并、变基（rebase）、删除、重命名分支
- 远程同步：拉取（pull）、推送（push）、获取（fetch）、解决冲突
- 变更审查：差异对比、暂存审查、提交历史分析、 blame 追溯
- 工作流支持：Git Flow、GitHub Flow、Trunk-Based Development
- 冲突解决：三方合并、cherry-pick、rebase 冲突处理、冲突标记解析

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 代码检查 | 仓库路径 | 状态报告与变更摘要 |
| 提交管理 | 变更描述 | 规范化提交信息与暂存策略 |
| 分支操作 | 分支名与操作类型 | 分支创建/合并/删除结果 |
| 冲突解决 | 冲突文件列表 | 合并方案与解决后的代码 |
| 历史追溯 | 文件路径与行号 | 变更历史与责任人 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

### 流程详解：代码提交工作流

**步骤 1：检查变更状态**

```bash
# 查看工作区状态
git status

# 查看未暂存的变更
git diff

# 查看已暂存的变更
git diff --staged

# 查看简短状态
git status -s
# 输出示例:
#  M src/index.js        (已修改未暂存)
# M  src/utils.js        (已修改已暂存)
# ?? src/new-file.js     (未跟踪)
# A  src/feature.js      (新增已暂存)
# D  src/old-file.js     (删除已暂存)
```

**步骤 2：智能暂存**

```bash
# 暂存单个文件
git add src/index.js

# 暂存多个相关文件
git add src/components/ src/utils/helpers.js

# 交互式暂存（选择部分变更）
git add -p
# 对每个 hunk 选择: y(暂存) n(跳过) s(拆分) e(编辑) q(退出)

# 暂存特定文件的特定行
git add -p src/index.js

# 撤销暂存
git restore --staged src/index.js
```

**步骤 3：生成规范化提交信息**

遵循 Conventional Commits 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

| 类型 (type) | 说明 | 示例 |
|:------------|:-----|:-----|
| `feat` | 新功能 | `feat(auth): 添加 OAuth2 登录支持` |
| `fix` | 修复 Bug | `fix(api): 修复分页参数 off-by-one 错误` |
| `docs` | 文档变更 | `docs(readme): 更新安装说明` |
| `style` | 代码格式 | `style: 统一缩进为 2 空格` |
| `refactor` | 重构 | `refactor(utils): 提取公共验证函数` |
| `perf` | 性能优化 | `perf(render): 使用虚拟列表优化大列表渲染` |
| `test` | 测试相关 | `test(auth): 添加登录流程单元测试` |
| `chore` | 构建/工具 | `chore(deps): 升级 React 到 18.2` |
| `ci` | CI 配置 | `ci: 添加 GitHub Actions 自动部署` |
| `revert` | 回退提交 | `revert: feat(auth): 添加 OAuth2 登录支持` |

## 分支管理

### 分支策略

| 策略 | 主分支 | 特征分支 | 发布分支 | 适用团队 |
|:-----|:-------|:---------|:---------|:---------|
| Git Flow | main + develop | feature/* | release/* hotfix/* | 大型团队、版本发布 |
| GitHub Flow | main | feature/* | 无 | 小型团队、持续部署 |
| Trunk-Based | main | 短命特性分支 | 无 | 高频发布、DevOps |

### 常用分支操作

```bash
# 查看所有分支
git branch -a              # 包括远程分支
git branch -vv             # 显示跟踪关系和最新提交

# 创建并切换分支
git checkout -b feature/user-auth
# 或使用新语法
git switch -c feature/user-auth

# 从特定提交创建分支
git switch -c hotfix/fix-login a1b2c3d

# 合并分支（保留合并记录）
git merge feature/user-auth --no-ff

# 变基（线性历史）
git rebase main

# 交互式变基（压缩、重排、修改提交）
git rebase -i HEAD~5
# pick a1b2c3d feat: 添加登录页面
# squash d4e5f6g feat: 添加登录表单验证
# reword h7i8j9k fix: 修复表单校验问题

# 删除已合并的分支
git branch -d feature/user-auth

# 强制删除未合并的分支
git branch -D feature/abandoned
```

## 冲突解决

### 合并冲突处理

```bash
# 当 git merge 报告冲突时
git merge feature/branch
# CONFLICT (content): Merge conflict in src/index.js

# 查看冲突文件
git diff --name-only --diff-filter=U

# 冲突标记格式
# <<<<<<< HEAD
# 当前分支的代码
# =======
# 传入分支的代码
# >>>>>>> feature/branch

# 解决冲突后
git add src/index.js
git commit  # 完成合并

# 放弃合并
git merge --abort
```

### Rebase 冲突处理

```bash
git rebase main
# CONFLICT (content): Merge conflict in src/index.js

# 解决冲突
git add src/index.js
git rebase --continue

# 跳过当前提交
git rebase --skip

# 放弃 rebase
git rebase --abort
```

### Cherry-pick 操作

```bash
# 将特定提交应用到当前分支
git cherry-pick a1b2c3d

# 多个提交
git cherry-pick a1b2c3d d4e5f6g

# 不自动提交，仅应用变更
git cherry-pick --no-commit a1b2c3d
```

## 远程仓库同步

```bash
# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add upstream https://github.com/org/repo.git

# 拉取并合并（pull = fetch + merge）
git pull origin main

# 仅获取不合并
git fetch origin
git fetch --all --prune  # 获取所有远程并清理已删除的分支

# 推送
git push origin feature/branch
git push -u origin feature/branch  # 设置上游跟踪
git push --force-with-lease origin main  # 安全强制推送（推荐）
# 注意：避免使用 git push --force，它会覆盖远程历史

# 推送标签
git push origin --tags
git push origin v1.0.0
```

## 历史追溯与审查

```bash
# 查看提交历史
git log --oneline --graph --all
git log --author="张三" --since="2024-01-01" --until="2024-06-30"

# 查看文件的变更历史
git log --follow src/index.js

# 查看某一行代码的最后修改
git blame -L 42,50 src/index.js

# 搜索提交信息
git log --grep="fix.*login" --oneline

# 查看某次提交的详细变更
git show a1b2c3d

# 比较两个分支的差异
git diff main..feature/branch --stat
```

## 最佳实践

### 提交规范

1. **原子提交**：每个提交只做一件事，便于回滚和审查
2. **提交信息**：使用 Conventional Commits 规范，动词开头，清晰描述变更
3. **暂存策略**：使用 `git add -p` 选择性暂存，避免提交调试代码
4. **频率**：小步提交，每天多次提交优于一次大提交

### 分支管理

1. **命名规范**：`feature/`、`fix/`、`hotfix/`、`refactor/` 前缀
2. **生命周期**：特性分支存活不超过 3 天，及时合并或删除
3. **保护主分支**：禁止直接 push 到 main，通过 PR/MR 合并
4. **定期同步**：每天从主分支 rebase 或 merge，减少最终冲突

### 安全注意事项

1. **避免提交敏感信息**：使用 `.gitignore` 排除配置文件，使用 `git-secrets` 预防
2. **清理历史中的密钥**：`git filter-repo --replace-text passwords.txt`
3. **签名提交**：`git commit -S` 使用 GPG 签名验证身份
4. **不要 force push 到共享分支**：会覆盖他人的提交

## 常用 Git 配置

```bash
# 用户信息
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# 默认分支名
git config --global init.defaultBranch main

# 行尾处理
git config --global core.autocrlf input   # macOS/Linux
git config --global core.autocrlf true    # Windows

# 别名
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"

# Pull 默认使用 rebase
git config --global pull.rebase true
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| action | string | 是 | 操作类型: `inspect`/`stage`/`commit`/`branch`/`merge`/`sync` |
| repo_path | string | 否 | Git 仓库路径，默认当前目录 |
| content | string | 否 | git-cli处理的内容输入，可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "action": "commit",
    "repository": "my-project",
    "branch": "feature/user-auth",
    "staged_files": ["src/auth/login.js", "src/auth/oauth.js"],
    "commit": {
      "hash": "a1b2c3d",
      "message": "feat(auth): 添加 OAuth2 登录支持",
      "author": "开发者 <dev@example.com>",
      "timestamp": "2024-07-24T10:30:00+08:00"
    },
    "metadata": {
      "template_used": "git-cli-helper",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 常见问题

### Q1: 如何开始使用Git cli？
A: 在 Git 仓库目录中直接描述你的需求即可。例如"帮我查看当前变更并提交"，系统会先执行 `git status` 和 `git diff` 查看变更，然后智能选择相关文件进行暂存，自动生成符合 Conventional Commits 规范的提交信息。你也可以指定具体操作，如"创建分支 feature/payment 并切换过去"或"将 main 分支的最近 3 个提交变基到当前分支"。

### Q2: 合并冲突如何处理？
A: 当遇到合并冲突时，系统会列出所有冲突文件，展示冲突标记内容（`<<<<<<<`/`=======`/`>>>>>>>`），分析两边的变更意图，给出合并建议。你确认后系统会修改文件解决冲突，执行 `git add` 暂存已解决的文件，然后完成合并提交。如果需要放弃合并，可执行 `git merge --abort` 回到合并前状态。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

