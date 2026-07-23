---
slug: "git-workflow-cn-paid"
name: "git-workflow-cn-paid"
version: "1.0.0"
displayName: "Git工作流专业版"
summary: "企业级 Git 工作流方案，支持 Git Flow、团队协作、冲突工具集成与批量分支管理。"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队协作与企业研发场景的 Git 工作流专业工具。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
  - 开发工具
  - 版本控制
  - Git
  - 企业协作
  - DevOps
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Git工作流专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力模块 | 支持 | 支持 |
| 专业版新增 | 不支持 | 支持 |
| 分支管理 | 不支持 | 支持 |
| 批量分支管理、保护分支策略 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
| --- | --- | --- |
| 分支管理 | 基础创建/切换/合并 | 批量分支管理、保护分支策略 |
| 工作流模型 | - | Git Flow / GitHub Flow / GitLab Flow |
| 冲突解决 | 手动解决 | rerere 自动记忆 + 三方对比工具 |
| 提交规范 | Conventional Commits | CHANGELOG 自动生成 + 语义化版本 |
| 发布管理 | - | 发布分支、版本标签、回滚策略 |
| 团队协作 | - | 代码审查流程、合并请求规范 |
### 能力模块

执行能力模块操作,处理用户输入并返回结果。

**输入**: 用户提供能力模块所需的参数和指令。

**输出**: 返回能力模块的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`能力模块`相关配置参数进行设置
### 分支管理

执行分支管理操作,处理用户输入并返回结果。

**输入**: 用户提供分支管理所需的参数和指令。

**输出**: 返回分支管理的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`分支管理`相关配置参数进行设置
### 工作流模型

执行工作流模型操作,处理用户输入并返回结果。

**输入**: 用户提供工作流模型所需的参数和指令。

**输出**: 返回工作流模型的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`工作流模型`相关配置参数进行设置
#
## 适用场景

### 场景一：Git Flow 发布流程管理

团队需要规划一个正式版本发布，包含功能开发、预发布验证、紧急修复全流程。

```text
用户：我们需要发布 v2.0.0 版本，包含多个功能分支，帮我规划 Git Flow 流程

助手：
1. 初始化 Git Flow
   git flow init

2. 功能分支开发（多个并行）
   git flow feature start user-auth
   git flow feature start payment-module
   # 开发完成后分别完成
   git flow feature finish user-auth
   git flow feature finish payment-module

3. 创建发布分支
   git flow release start v2.0.0
   # 在发布分支上仅允许修复缺陷和文档更新

4. 完成发布并打标签
   git flow release finish v2.0.0
   # 自动合并到 main 和 develop，并打版本标签

5. 推送所有分支和标签
   git push origin --all
   git push origin --tags

6. 紧急修复流程（如线上发现缺陷）
   git flow hotfix start fix-login-crash v2.0.0
   # 修复完成后
   git flow hotfix finish fix-login-crash
```

### 场景二：多环境部署分支策略

团队需要维护开发、预发、生产三个环境的代码同步。

```text
用户：我们有 dev/staging/prod 三个环境，怎么管理分支

助手：推荐 GitLab Flow 模式

1. 功能分支开发并合并到 main
   git checkout -b feature/payment main
   git push origin feature/payment
   # 通过合并请求合并到 main

2. main 合并到 staging 部署预发
   git checkout staging
   git merge main
   git push origin staging

3. staging 验证通过后合并到 production
   git checkout production
   git merge staging
   git push origin production

4. 紧急修复需要从 production 反向合并
   git checkout -b hotfix/urgent production
   # 修复后合并回 production 和 main
```

### 场景三：批量分支清理与冲突记忆

项目积累了大量过期分支，需要批量清理并启用冲突自动记忆。

```bash
# 启用 rerere 自动记忆冲突解决方案
git config --global rerere.enabled true

# 批量查看已合并分支
git branch --merged main | grep -v "^\*\|main\|develop"

# 批量删除已合并的本地分支
git branch --merged main | grep -v "^\*\|main\|develop" | xargs -n 1 git branch -d

# 批量清理远程过期分支
git remote prune origin
git fetch --all --prune

# 批量删除远程已合并分支（谨慎操作）
git branch -r --merged origin/main | grep -v "main\|develop" | sed 's/origin\///' | xargs -I{} git push origin :{}
```

## 使用流程

### Git Flow 初始化配置

```bash
# 依赖说明
brew install git-flow

# 安装 git-flow（Ubuntu/Debian）
apt-get install git-flow

# 初始化项目
git flow init

# 自定义分支名（交互式配置）
# main branch: main
# develop branch: develop
# feature/: feature/
# release/: release/
# hotfix/: hotfix/
```

### 企业级 Git 配置

```bash
# 启用冲突自动记忆
git config --global rerere.enabled true

# 配置三方合并工具
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# 配置行尾换行符
git config --global core.autocrlf input

# 配置拉取策略为 rebase
git config --global pull.rebase true

# 配置推送默认行为
git config --global push.default current

# 启用部分克隆（大仓库优化）
git config --global feature.experimental true
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Git 版本**: 建议 2.25 及以上（需支持 rerere、sparse-checkout）
- **Node.js**: 18.0+（CHANGELOG 生成工具依赖）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Git | 命令行工具 | 必需 | 系统包管理器安装 |
| git-flow | 扩展工具 | 推荐 | `brew install git-flow` 或 `apt install git-flow` |
| conventional-changelog-cli | Node 工具 | 可选 | `npm install -g conventional-changelog-cli` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- Git 远程推送需要配置 SSH Key 或个人访问令牌
- 团队协作建议配置统一的 GPG 签名密钥

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 执行 Git 操作，专业版功能依赖 git-flow 扩展和命令行执行能力

## 案例展示

### 保护分支策略建议

| 分支 | 保护规则 | 合并方式 | 谁可推送 |
| --- | --- | --- | --- |
| main | 禁止直接推送 | 合并请求 + 审查 | 仅管理员 |
| develop | 禁止直接推送 | 合并请求 | 核心成员 |
| release/* | 禁止新功能 | 仅缺陷修复 | 发布负责人 |
| hotfix/* | 紧急通道 | 快速审查 | 值班人员 |
| feature/* | 自由推送 | 直接推送 | 分支创建者 |

### 版本标签规范

```bash
# 语义化版本标签
git tag -a v2.0.0 -m "Release 2.0.0: 用户认证与支付模块"

# 预发布版本标签
git tag -a v2.1.0-beta.1 -m "Beta 2.1.0: 新搜索功能预览"

# 补丁版本标签
git tag -a v2.0.1 -m "Patch: 修复登录崩溃问题"

# 查看所有标签
git tag -l
git tag -l "v2.*"

# 推送标签
git push origin v2.0.0        # 单个标签
git push origin --tags         # 所有标签

# 删除标签
git tag -d v2.0.0              # 本地
git push origin --delete v2.0.0  # 远程
```

### CHANGELOG 自动生成配置

```bash
# 安装 conventional-changelog
npm install -g conventional-changelog-cli

# 生成 CHANGELOG
conventional-changelog -p angular -i CHANGELOG.md -s

# 首次生成完整历史
conventional-changelog -p angular -i CHANGELOG.md -s -r 0
```

## 常见问题

### Q1：rerere 如何工作？

```bash
# 启用后，首次解决冲突时 Git 会记录解决方案
git config --global rerere.enabled true

# 再次遇到相同冲突时自动应用记忆的方案
git rerere diff     # 查看当前记忆的解决方案
git rerere forget path/to/file  # 忘记指定文件的方案
ls .git/rr-cache/   # 查看所有记忆的冲突
```

### Q2：如何处理 Git Flow 中 release 期间的新功能？

```bash
# 新功能应在 develop 分支继续开发
# release 分支仅接受缺陷修复
git checkout develop
git flow feature start new-feature
```

### Q3：hotfix 修复后如何同步到所有分支？

```bash
# Git Flow 会自动合并 hotfix 到 main 和 develop
git flow hotfix finish fix-urgent

# 如有多环境分支，需手动同步
git checkout staging
git merge main
git push origin staging
```

### Q4：如何回滚已发布的版本？

```bash
# 方案一：使用 revert（保留历史，推荐）
git revert v2.0.0..HEAD
git commit -m "revert: 回滚 v2.0.0 之后的所有改动"

# 方案二：使用 reset（重写历史，谨慎使用）
git checkout main
git reset --hard v1.9.0
git push --force-with-lease origin main
```

### Q5：如何批量重命名多个分支？

```bash
# 批量添加前缀
for branch in feature-a feature-b feature-c; do
  git branch -m "$branch" "legacy/$branch"
done
```

### Q6：合并请求出现大量冲突怎么处理？

```bash
# 1. 先同步目标分支
git fetch origin
git checkout feature/complex
git rebase origin/main

# 2. 逐个文件解决冲突
git status
# 编辑冲突文件...
git add .
git rebase --continue

# 3. 如冲突过多，考虑重置后重新开发
git rebase --abort
git checkout main
git pull
git checkout -b feature/complex-v2
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

