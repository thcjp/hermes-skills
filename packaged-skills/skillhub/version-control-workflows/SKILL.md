---
slug: "version-control-workflows"
name: "version-control-workflows"
version: "1.0.1"
displayName: "Git Workflows"
summary: "add/commit/push之外的高级git操作,rebase/bisect/worktree。Advanced git operations beyond add/commit/push"
license: "Proprietary"
description: |-
  Advanced git operations beyond add/commit/push. Use when rebasing, bisecting
  bugs, using worktree, reflog recovery, subtrees, submodules, sparse checkout,
  conflict resolution, and monorepo patterns.
tags:
  - Development
  - 工作流
  - 自动化
  - 效率
  - workflows
  - agent
  - git
tools:
  - read
  - write
  - exec
homepage: ""
category: "Automation"
---
# Git Workflows

## 核心能力

提供add/commit/push之外的高级Git操作指导,覆盖以下六大核心能力:

### 一、Rebase变基操作
- **交互式rebase**: `git rebase -i HEAD~N`合并/编辑/重排/删除历史提交,保持提交历史整洁
- **rebase冲突解决**: 处理rebase过程中的合并冲突,`git rebase --continue`/`--abort`/`--skip`操作指南
- **rebase与merge选择**: 团队协作中rebase(线性历史)vs merge(保留分支记录)的适用场景与最佳实践

### 二、Bisect二分查错
- **二分定位Bug**: `git bisect start`/`good`/`bad`通过二分法快速定位引入Bug的具体提交
- **自动二分**: `git bisect run <test_script>`自动执行测试脚本,无需手动标记每次提交
- **回归排查**: 利用bisect在大量历史提交中精确找到导致回归问题的commit

### 三、Worktree工作树
- **多分支并行**: `git worktree add`在不切换分支的情况下同时在多个分支上工作
- **隔离环境**: 为每个任务创建独立工作目录,避免频繁stash和分支切换的开销
- **工作树管理**: `git worktree list`/`remove`/`prune`管理工作树的创建、查看与清理

### 四、Reflog恢复
- **误操作恢复**: `git reflog`查看HEAD移动历史,恢复误删的提交、硬重置前的状态
- **分支恢复**: 通过reflog找到被删除分支的最后一个commit,`git branch <name> <commit>`恢复
- **操作溯源**: reflog记录所有HEAD变更,是Git操作的"后悔药"

### 五、Subtree与Submodule
- **Subtree子树**: `git subtree add/pull/push`管理外部仓库代码,保持单一仓库结构
- **Submodule子模块**: `git submodule add/update/sync`管理独立的子仓库,适合大型项目
- **选择策略**: Subtree(简单,适合小型依赖)vs Submodule(独立,适合大型组件)的对比与选择

### 六、高级冲突解决与Monorepo
- **复杂冲突处理**: `git mergetool`/`checkout --ours`/`--theirs`处理三方合并冲突
- **Sparse Checkout稀疏检出**: `git sparse-checkout`仅检出Monorepo中需要的子目录,提升大仓库性能
- **Monorepo模式**: 大型Monorepo仓库的分支策略、CI/CD集成与代码所有权管理
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 典型需求 | 涉及操作 |
|:-----|:-----|:-----|
| 提交历史整理 | 合并多个小提交为完整功能提交 | `git rebase -i`交互式变基 |
| Bug回归定位 | 在大量提交中找到引入Bug的commit | `git bisect`二分查错 |
| 多分支并行开发 | 同时在feature/hotfix分支工作不切换 | `git worktree add`工作树 |
| 误操作恢复 | 恢复误删分支或硬重置前的代码 | `git reflog`操作溯源 |
| 外部代码集成 | 引入其他仓库代码作为子模块或子树 | `git submodule`/`git subtree` |
| Monorepo管理 | 大型仓库仅检出所需子目录 | `git sparse-checkout`稀疏检出 |
| 复杂冲突解决 | 多方合并时处理代码冲突 | `git mergetool`/`checkout --ours` |

**不适用场景**: 基础Git操作(add/commit/push/clone)、GitHub PR管理、CI/CD流水线配置

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | version-control-workflows处理的内容输入 |, 默认: 全部维度 |
| operation | string | 否 | Git高级操作类型, 可选: rebase/bisect/worktree/reflog/subtree, 默认: rebase |

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Git高级操作执行结果与指导说明",
    "execution_time": "0.3s",
    "metadata": {
      "version": "1.0",
      "processor": "version-control-workflows"
    }
  },
  "execution_log": ["解析输入参数", "识别Git操作类型", "执行Git命令", "格式化输出结果"],
  "error": null
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|:-----|:-----|:-----|
| success | boolean | 处理是否成功,`true`表示成功,`false`表示失败 |
| data.result | string | Git操作执行结果,包含命令输出、操作步骤指导与注意事项 |
| data.execution_time | string | 处理耗时 |
| data.metadata.processor | string | 处理器标识,固定为`version-control-workflows` |
| execution_log | array | 执行步骤日志 |
| error | string/null | 错误信息,如Git命令不存在、仓库未初始化等 |

## 示例代码

### 1. 交互式Rebase整理提交历史

将最近5个提交合并整理为整洁的提交历史:

```bash
# 启动交互式rebase,编辑最近5个提交
git rebase -i HEAD~5

# 编辑器中会显示:
# pick a1b2c3d 添加用户登录功能
# pick d4e5f6g 修复登录bug
# pick h7i8j9k 添加注册页面
# pick l0m1n2o 优化注册表单
# pick p3q4r5s 添加密码重置

# 将后4个改为squash(s)合并到第一个:
# pick a1b2c3d 添加用户登录功能
# s d4e5f6g 修复登录bug
# s h7i8j9k 添加注册页面
# s l0m1n2o 优化注册表单
# s p3q4r5s 添加密码重置

# 保存后编辑合并提交信息,完成rebase
git rebase --continue
```

### 2. Bisect二分定位Bug

```bash
# 标记当前版本为bad(有Bug)
git bisect start
git bisect bad HEAD

# 标记一个已知正常的旧版本为good
git bisect good v1.0.0

# Git自动切换到中间提交,测试后标记
git bisect good   # 或 git bisect bad

# 自动二分(配合测试脚本)
git bisect run npm test

# 定位完成后退出bisect
git bisect reset
```

### 3. Worktree多分支并行开发

```bash
# 为hotfix分支创建独立工作目录
git worktree add ../project-hotfix hotfix-branch

# 为新feature分支创建独立工作目录
git worktree add -b new-feature ../project-feature

# 查看所有工作树
git worktree list
# /main/project      abc1234 [main]
# /main/project-hotfix  def5678 [hotfix-branch]
# /main/project-feature ghi9012 [new-feature]

# 完成后清理工作树
git worktree remove ../project-hotfix
git worktree prune  # 清理已删除目录的残留记录
```

### 4. Reflog恢复误删分支

```bash
# 查看HEAD移动历史
git reflog
# a1b2c3d HEAD@{0}: commit: 修复bug
# d4e5f6g HEAD@{1}: reset: moving to HEAD~1
# h7i8j9k HEAD@{2}: checkout: moving from feature to main
# l0m1n2o HEAD@{3}: commit: 添加新功能  <-- 误删分支的最后一个提交

# 恢复误删的分支
git branch recovered-feature l0m1n2o
git checkout recovered-feature
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

## 常见问题

### Q1: 如何开始使用Git Workflows？
A: 在AI Agent对话中描述你的Git操作需求(如"整理提交历史"、"定位引入Bug的提交"、"恢复误删分支"),技能会根据需求提供对应的高级Git命令与操作步骤指导。建议先确认本地已安装Git并初始化仓库,再根据示例代码逐步执行。

### Q2: rebase和merge应该如何选择?
A: 个人feature分支合并到主分支时优先用rebase(保持线性历史,便于review);多人协作的公共分支用merge(保留合并记录,避免改写历史)。黄金法则:永远不要对已推送到远程的公共分支执行rebase。

### Q3: reflog能恢复多久前的操作?
A: reflog默认保留90天(可通过`gc.reflogExpire`配置)。超过有效期的reflog记录会在`git gc`时被清理,届时将无法恢复。建议发现误操作后尽快使用reflog恢复。

## 已知限制

- **依赖Git环境**: 需本地安装Git并初始化仓库,无Git环境无法使用
- **不替代基础操作**: 本技能专注于高级操作,基础add/commit/push请直接使用Git命令
- **无法操作远程仓库**: 不支持直接管理GitHub/GitLab的PR、Issue等远程平台功能
- **rebase风险提示**: 对已推送的公共分支执行rebase可能导致团队协作冲突,需谨慎操作
- **reflog时效性**: reflog记录有有效期(默认90天),过期记录无法恢复

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

