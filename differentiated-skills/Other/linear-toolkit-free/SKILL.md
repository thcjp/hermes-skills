---
slug: linear-toolkit-free
name: linear-toolkit-free
version: "1.0.0"
displayName: Linear 工具箱
summary: 面向个人的 Linear 任务查询与基础管理工具，含站会摘要。
license: Proprietary
edition: free
description: |-
  面向个人开发者的 Linear 任务查询与基础管理工具。

  核心能力:
  - 个人任务、待办、紧急事项查询
  - 任务创建、评论、状态与优先级管理
  - 每日站会摘要
  - Linear 与 Git 分支名联动

  适用场景:
  - 个人查看与更新 Linear 任务
  - 每日站会快速摘要
  - 从 Linear 任务生成 Git 分支名

  差异化: 免费版聚焦个人单团队任务管理，提供查询、更新与站会摘要，零成本接入。

  触发关键词: linear, 任务管理, 站会, 待办, issue, standup, branch
tags:
- Linear
- 任务管理
- 个人效率
- 其他工具
tools:
  - - read
- exec
---
# Linear 工具箱（免费版）

## 概述

本工具帮助个人开发者查询与管理 Linear 任务、项目与团队工作流。免费版覆盖个人任务查询、创建、评论、状态/优先级管理、每日站会摘要与 Git 分支名联动，适合个人单团队使用。

## 核心能力

| 能力 | 说明 | 免费版范围 |
|:-----|:-----|:-----------|
| 任务查询 | 我的任务、待办、紧急 | 个人 |
| 任务管理 | 创建、评论、状态、优先级 | 单团队 |
| 站会摘要 | 待办、阻塞、评审、已完成 | 每日 |
| Git 联动 | 从任务生成分支名 | 单仓库 |

## 使用场景

### 场景一：每日站会

```bash
export LINEAR_API_KEY="your-key"
export LINEAR_DEFAULT_TEAM="TEAM"

# 站会摘要：待办、阻塞、评审中、近期完成
{baseDir}/scripts/linear.sh standup
```

### 场景二：快速建任务

```bash
# 从聊天直接建任务
{baseDir}/scripts/linear.sh create TEAM "修复登录超时" "用户 5 分钟后被登出"
```

### 场景三：Git 分支联动

```bash
# 取任务对应分支名
BRANCH=$({baseDir}/scripts/linear.sh branch TEAM-212)

cd /path/to/repo
git checkout main && git pull origin main
git worktree add .worktrees/team-212 -b "$BRANCH" origin/main
cd .worktrees/team-212
git push -u origin "$BRANCH"
```

## 不适用场景

以下场景Linear 工具箱不适合处理：

- 实际人员绩效评估
- 财务预算审批
- 合同法务审核


## 触发条件

需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于非本工具能力范围的需求。


## 快速开始

1. 设置 `LINEAR_API_KEY` 与 `LINEAR_DEFAULT_TEAM`。
2. 用 `teams` 发现团队 key。
3. 查询与更新任务。
4. 站会前跑 `standup`。

```bash
{baseDir}/scripts/linear.sh teams              # 列团队
{baseDir}/scripts/linear.sh my-issues          # 我的任务
{baseDir}/scripts/linear.sh urgent             # 紧急/高优
```

## 示例

优先级对照：

| 级别 | 值 | 用途 |
|:-----|:---|:-----|
| urgent | 1 | 生产事故、阻塞 |
| high | 2 | 本周、重要 |
| medium | 3 | 本迭代 |
| low | 4 | 锦上添花 |
| none | 0 | 待办池 |

## 最佳实践

- **分支名走 Linear**：用 `branch` 命令生成分支名，PR 合并自动推进状态。
- **main 保持干净**：改动只在 worktree，避免误推 main。
- **站会前跑摘要**：`standup` 一条命令出全貌，省去手工翻。
- **优先级要准**：生产事故才 urgent，别滥用高优。
- **状态及时更新**：开始做就转 progress，评审转 review，便于团队看板。

## 常见问题

**Q1：API Key 从哪拿？**
A：Linear 设置 → API → 生成 Personal API Key。

**Q2：为什么分支名重要？**
A：Linear 按分支名追踪 PR，PR 创建自动转「评审中」，合并自动转「完成」。

**Q3：免费版支持多团队吗？**
A：支持查询多团队，但默认聚焦单团队。跨团队看板与批量操作为专业版能力。

**Q4：能改任务指派人？**
A：能。`assign TEAM-123 用户名`。

**Q5：站会摘要包含什么？**
A：你的待办、团队阻塞项、评审中、近期完成。

## 进阶用法

### 常用查询命令

```bash
{baseDir}/scripts/linear.sh my-issues              # 我的任务
{baseDir}/scripts/linear.sh urgent                 # 紧急/高优
{baseDir}/scripts/linear.sh backlog TEAM           # 团队待办池
{baseDir}/scripts/linear.sh search "登录"          # 关键词搜索
{baseDir}/scripts/linear.sh issue TEAM-123         # 查看详情
{baseDir}/scripts/linear.sh comments TEAM-123      # 查看评论
```

### 任务更新操作

```bash
# 更新状态
{baseDir}/scripts/linear.sh update TEAM-123 --status "In Progress"

# 设置优先级
{baseDir}/scripts/linear.sh update TEAM-123 --priority urgent

# 指派
{baseDir}/scripts/linear.sh assign TEAM-123 用户名

# 添加评论
{baseDir}/scripts/linear.sh comment TEAM-123 "已复现，预计今日修复"
```

### 站会摘要详解

```text
═══ 今日站会摘要 ═══
我的待办（5）:
  TEAM-101 修复登录超时 [进行中]
  TEAM-105 优化首页加载 [待办]
  ...

团队阻塞项（2）:
  TEAM-108 等待设计稿（@设计师）
  TEAM-112 依赖后端接口（@后端）

评审中（3）:
  TEAM-100 PR #234 待评审

近期完成（4）:
  TEAM-095 登录页重构 ✓
  ...
══════════════════════
```

## Git 分支工作流

```text
完整工作流:
  1. linear.sh branch TEAM-212 → 得到分支名
  2. git worktree add .worktrees/team-212 -b 分支名
  3. 开发提交
  4. 推送创建 PR
  5. Linear 自动转「评审中」
  6. PR 合并 → Linear 自动转「完成」
```

## 任务管理习惯

- **开始即更新**：动手做就转「进行中」，团队看板才准。
- **评审及时转**：提 PR 即转「评审中」，评审人可见。
- **阻塞要标注**：卡住标注阻塞原因与依赖人。
- **优先级定期校**：每周校一次优先级，urgent 别滥用。
- **评论留上下文**：关键决策写评论，便于回溯。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 可访问 api.linear.app

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| curl | 命令行工具 | 必需 | 系统包管理器 |
| jq | JSON 处理 | 推荐 | 系统包管理器 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- `LINEAR_API_KEY`：Linear Personal API Key，从设置获取
- `LINEAR_DEFAULT_TEAM`：默认团队 key，可省略每次传团队
- 密钥建议存环境变量或权限 0600 的配置文件

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 调用 Linear GraphQL API 管理任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
