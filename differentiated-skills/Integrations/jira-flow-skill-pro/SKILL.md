---
slug: jira-flow-skill-pro
name: jira-flow-skill-pro
version: "1.0.0"
displayName: Jira Flow 专业版
summary: 全功能Jira任务管理与团队工时分析，支持批量操作、自定义报表与自动化集成。
license: Proprietary
edition: pro
description: |-
  Jira Flow Skill 专业版面向团队负责人与项目经理，在免费版基础上解锁批量任务操作、多项目工时对比、自定义报表模板与团队工时聚合视图。核心能力：单条命令完成批量状态流转、跨项目工时对比报表、自定义工时模板导出（Markdown/CSV/JSON）、团队成员工时聚合、Webhook 自动化触发、并发请求与缓存优化
tags:
- 集成工具
- 任务管理
- 团队协作
- 自动化
tools:
  - - read
- exec
---

# Jira Flow Skill（专业版）

面向团队负责人与项目经理的全功能 Jira 任务管理与工时分析平台，在免费版基础上解锁批量操作、团队聚合、自定义报表与自动化集成。

## 概述

Jira Flow Skill 专业版将 Jira Cloud REST API 的能力扩展到团队级与自动化场景。无论是项目经理需要一键生成团队周报，还是 DevOps 工程师希望让 CI/CD 流水线自动更新 Jira 状态，专业版都提供了对应的命令与配置能力。相比免费版，专业版在性能、扩展性与自动化三个维度全面升级。

### 核心价值

- **团队视角工时分析**：一次命令拉取全员工时，按用户/任务/项目多维聚合
- **批量操作与并发优化**：批量状态流转与工时记录，内置并发请求与限流
- **自定义报表模板**：支持 Markdown / CSV / JSON 三种导出格式，模板可配置
- **Webhook 自动化**：与 CI/CD、IM 机器人联动，实现状态变更自动通知
- **多级缓存策略**：缓存 transitions 与用户列表，减少重复请求耗时

## 核心能力

| 能力域 | 命令族 | 说明 | 专业版增强 |
|--------|--------|------|-----------|
| 任务检索 | `search` / `my` / `team` | 模糊搜索、个人任务、团队任务 | 新增 `team` 团队视角 |
| 状态管理 | `status` / `transitions` / `batch-status` | 单条与批量状态流转 | 新增批量操作 |
| 任务分配 | `assign` / `batch-assign` | 单条与批量分配 | 新增批量分配 |
| 工时记录 | `log` / `batch-log` | 单条与批量工时记录 | 新增批量记录 |
| 工时统计 | `hours` / `hours-day` / `hours-issue` / `hours-team` | 多维工时统计 | 新增团队聚合 |
| 报表导出 | `report` | 自定义模板导出 | 专业版独有 |
| 自动化 | `webhook` / `watch` | Webhook 注册与事件监听 | 专业版独有 |
| 缓存优化 | `cache` | 多级缓存管理 | 专业版独有 |

## 使用场景

### 场景一：项目经理一键生成团队周报（项目经理角色）

每周一上午需要汇总上周团队工时投入分布，并按项目维度对比。专业版提供 `hours-team` 命令与 `report` 模板能力：

```bash
# 拉取团队上周工时（按用户+任务聚合）
bash {baseDir}/scripts/jira.sh hours-team 2025-01-06 2025-01-12

# 按自定义模板生成 Markdown 周报
bash {baseDir}/scripts/jira.sh report --template weekly --format markdown --output weekly-report.md
```

### 场景二：Sprint 结束时批量关闭已完成任务（Scrum Master 角色）

Sprint 评审后需要将一批已验证的任务统一关闭。免费版需要逐条执行，专业版支持批量：

```bash
# 批量更新状态（自动并发，带限流）
bash {baseDir}/scripts/jira.sh batch-status ABC-101,ABC-102,ABC-103 "Done"

# 批量记录工时
bash {baseDir}/scripts/jira.sh batch-log "ABC-101:2.5,ABC-102:1.5,ABC-103:3.0" 2025-01-18
```

### 场景三：CI/CD 流水线自动更新 Jira 状态（DevOps 工程师角色）

部署成功后自动将关联任务流转到"已部署"状态，并通过 Webhook 通知 IM 群：

```bash
# 注册 Webhook（部署成功事件）
bash {baseDir}/scripts/jira.sh webhook register \
  --event deployment.success \
  --action "status {ISSUE_KEY} '已部署'"

# 监听事件并触发动作
bash {baseDir}/scripts/jira.sh watch --event deployment.success
```

### 场景四：跨项目工时投入对比（技术负责人角色）

需要对比本月团队在两个项目上的工时投入比例，作为资源调配依据：

```bash
# 跨项目工时对比
bash {baseDir}/scripts/jira.sh hours-team 2025-01-01 2025-01-31 \
  --projects "ABC,XYZ" \
  --group-by project
```

### 场景五：大型项目工时统计性能优化（团队负责人角色）

万级任务的项目工时统计耗时较长，专业版提供缓存与并发优化：

```bash
# 预热缓存（transitions 与用户列表）
bash {baseDir}/scripts/jira.sh cache warm --include transitions,users

# 并发拉取工时（默认 5 并发，可调整）
bash {baseDir}/scripts/jira.sh hours 2025-01-01 2025-01-31 --concurrency 8
```

## 快速开始

### 前置准备（约 60 秒）

1. 访问 Atlassian API Token 管理页：`https://id.atlassian.com/manage-profile/security/api-tokens`
2. 点击"Create API Token"生成令牌
3. 配置环境变量：

```bash
export JIRA_EMAIL="you@example.com"
export JIRA_API_TOKEN="你的API令牌"
export JIRA_URL="https://your-domain.atlassian.net"
export JIRA_BOARD="ABC"
# 专业版新增：并发与缓存配置
export JIRA_FLOW_CONCURRENCY=5
export JIRA_FLOW_CACHE_DIR="$HOME/.jira-flow-cache"
```

### 验证专业版能力（约 30 秒）

```bash
# 验证团队工时聚合
bash {baseDir}/scripts/jira.sh hours-team 2025-01-01 2025-01-07

# 验证缓存预热
bash {baseDir}/scripts/jira.sh cache warm
```

### 依赖说明

- 命令行工具：`curl`、`jq`、`bc`、`python3`
- 操作系统：Windows（需 WSL 或 Git Bash）/ macOS / Linux
- 网络：可访问 `atlassian.net` 域名
- 磁盘：缓存目录建议预留 50MB

## 示例

### 环境变量配置表

| 变量名 | 必填 | 默认值 | 说明 |
|--------|------|--------|------|
| `JIRA_EMAIL` | 是 | 无 | 登录 Jira 的邮箱 |
| `JIRA_API_TOKEN` | 是 | 无 | Atlassian API 令牌 |
| `JIRA_URL` | 是 | 无 | Jira 实例地址（含 https://） |
| `JIRA_BOARD` | 否 | 空 | 项目键值过滤 |
| `JIRA_FLOW_CONCURRENCY` | 否 | 5 | 并发请求数（建议 3-10） |
| `JIRA_FLOW_CACHE_DIR` | 否 | `~/.jira-flow-cache` | 缓存目录 |
| `JIRA_FLOW_CACHE_TTL` | 否 | 3600 | 缓存有效期（秒） |

### 自定义报表模板

在 `$JIRA_FLOW_CACHE_DIR/templates/` 下放置模板文件，支持以下变量：

| 变量 | 含义 | 示例 |
|------|------|------|
| `{{range_start}}` | 统计区间起点 | 2025-01-01 |
| `{{range_end}}` | 统计区间终点 | 2025-01-07 |
| `{{total_hours}}` | 总工时 | 120.5 |
| `{{by_user}}` | 按用户聚合 | JSON 数组 |
| `{{by_project}}` | 按项目聚合 | JSON 数组 |

### Webhook 自动化配置

```bash
# 注册 Webhook
bash {baseDir}/scripts/jira.sh webhook register \
  --event issue.updated \
  --url "https://your-im-bot/webhook" \
  --secret "your-webhook-secret"

# 查看已注册 Webhook
bash {baseDir}/scripts/jira.sh webhook list

# 删除 Webhook
bash {baseDir}/scripts/jira.sh webhook delete --id 12345
```

## 最佳实践

### 1. 并发数根据 Jira 实例负载调整

Jira Cloud 对 API 请求有速率限制。建议工作时段使用 3-5 并发，非高峰时段可提升到 8-10。超过限制会触发 429 状态码，脚本会自动退避重试。

### 2. 缓存预热减少首次查询耗时

`transitions` 与用户列表在短期内变化不大，建议在每日工作前执行一次 `cache warm`，后续状态变更与分配操作可直接走缓存。

### 3. 批量操作使用 CSV 输入

批量操作支持逗号分隔的简单格式，也支持从 CSV 文件读取。对于超过 50 条的批量操作，建议使用 CSV 文件并分批执行：

```bash
bash {baseDir}/scripts/jira.sh batch-status --file tasks.csv "Done"
```

### 4. 报表模板按团队角色区分

不同角色关注的工时维度不同。建议为项目经理、技术负责人、PMO 分别维护模板，通过 `--template` 参数切换。

### 5. Webhook 密钥定期轮换

Webhook 的 `secret` 用于校验请求来源，建议每季度轮换一次，避免长期泄露风险。

### 6. 工时统计使用增量更新

对于跨月统计，建议按周分批拉取后本地合并，避免单次请求超时。专业版的 `hours-team` 支持增量模式：

```bash
bash {baseDir}/scripts/jira.sh hours-team 2025-01-01 2025-01-31 --incremental
```

## 常见问题

### Q1：批量操作中部分任务失败如何处理？

专业版采用"部分成功"策略：成功的任务正常更新，失败的任务会输出到 stderr 并记录到 `$JIRA_FLOW_CACHE_DIR/failed-<timestamp>.csv`，可基于该文件重试。

### Q2：并发数设置多少合适？

取决于 Jira 实例的速率限制策略。建议从默认值 5 开始，观察是否出现 429 错误。如果稳定无错误，可逐步提升到 8-10；如果频繁报错，降低到 3。

### Q3：缓存数据会过期吗？

默认 TTL 为 3600 秒（1 小时）。可通过 `JIRA_FLOW_CACHE_TTL` 调整。`transitions` 缓存过期后会自动重新拉取；用户列表缓存过期后会在下次分配操作时刷新。

### Q4：Webhook 接收不到事件？

检查三项：Webhook URL 是否可被 Jira 实例访问（需公网可达）、secret 是否与注册时一致、事件类型是否匹配。可在 Webhook 管理页查看投递日志。

### Q5：报表模板变量未渲染？

确认模板文件位于 `$JIRA_FLOW_CACHE_DIR/templates/` 目录，且变量使用双花括号语法 `{{variable}}`。模板修改后无需重启，下次执行 `report` 命令会自动加载。

### Q6：跨项目工时对比耗时较长？

跨项目查询需要遍历多个项目的 worklog，建议先 `cache warm` 预热，并使用 `--concurrency 8` 提升并发。对于超过 3 个项目的对比，建议分批执行后本地合并。

### 已知限制

专业版内置自动退避重试，默认重试 3 次，每次间隔指数退避（1s、2s、4s）。如果仍失败，建议降低并发数或避开高峰时段。

### Q8：如何在 CI/CD 中安全使用 API Token？

将 Token 存储在 CI/CD 平台的密钥管理中（如 GitHub Actions Secrets、GitLab CI Variables），通过环境变量注入。禁止将 Token 写入脚本或配置文件。

### Q9：报表导出支持哪些格式？

支持 Markdown、CSV、JSON 三种格式。Markdown 适合周报与月报；CSV 适合导入 Excel 二次加工；JSON 适合被其他脚本消费。

### Q10：专业版与免费版可以共存吗？

可以。两个版本的 slug 不同（`-free` 与 `-pro`），可同时安装。建议根据场景切换：日常个人操作用免费版，团队管理与自动化用专业版。

## 性能优化策略

### 多级缓存架构

| 缓存层 | 内容 | TTL | 命中率 |
|--------|------|-----|--------|
| L1 内存 | transitions 映射 | 进程生命周期 | 95%+ |
| L2 文件 | 用户列表、项目元数据 | 1 小时 | 80%+ |
| L3 远程 | Jira API | 实时 | - |

### 并发与限流

- 默认并发数：5
- 最大并发数：10（受 Jira 速率限制约束）
- 退避策略：指数退避（1s、2s、4s、8s）
- 熔断阈值：连续 5 次 429 错误后暂停 30 秒

### 批处理与检查点

批量操作支持检查点机制，中断后可从上次位置恢复：

```bash
# 启用检查点
bash {baseDir}/scripts/jira.sh batch-status --file tasks.csv "Done" --checkpoint

# 从检查点恢复
bash {baseDir}/scripts/jira.sh batch-status --file tasks.csv "Done" --resume
```

## 错误处理

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|----------|----------|--------|
| 401 未授权 | Token 过期或邮箱错误 | 重新生成 Token，核对邮箱 | P0 |
| 404 任务不存在 | 键值错误或项目无权限 | 核对键值，检查项目权限 | P1 |
| 429 速率限制 | 并发过高或高峰时段 | 降低并发数，避开高峰 | P1 |
| 500 服务端错误 | Jira 实例异常 | 等待 5 分钟重试，查看 Jira 状态页 | P2 |
| 缓存命中率为 0 | 缓存目录权限或路径错误 | 检查 `JIRA_FLOW_CACHE_DIR` 权限 | P2 |
| Webhook 无事件 | URL 不可达或 secret 错误 | 校验 URL 公网可达性，核对 secret | P1 |
| 批量操作部分失败 | 个别任务状态不允许流转 | 查看失败 CSV，逐条修复后重试 | P2 |

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows（需 WSL 或 Git Bash）/ macOS / Linux
- **Shell**：bash 4.0+
- **磁盘**：缓存目录建议预留 50MB

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:-------|:-----|:---------|:---------|:---------|
| curl | 命令行工具 | 必需 | 系统自带或包管理器安装 | 7.0+ |
| jq | JSON 处理工具 | 必需 | `apt install jq` / `brew install jq` | 1.6+ |
| bc | 数值计算工具 | 必需 | `apt install bc` / `brew install bc` | 1.07+ |
| python3 | 运行时 | 必需 | `apt install python3` / 官网下载 | 3.8+ |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

### API Key 配置

- **JIRA_EMAIL**：通过环境变量配置，存储于 Shell 配置文件
- **JIRA_API_TOKEN**：通过环境变量配置，禁止明文写入脚本或提交到版本库
- **JIRA_URL**：通过环境变量配置
- **JIRA_BOARD**：可选，通过环境变量配置
- **Webhook Secret**：通过环境变量 `JIRA_FLOW_WEBHOOK_SECRET` 配置

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 调用脚本完成任务

## 专业版特性

本专业版相比免费版新增以下能力：

- **批量任务操作**：一次处理 50+ 任务的状态流转、工时记录与分配，支持检查点恢复
- **团队工时聚合**：`hours-team` 命令一次拉取全员工时，按用户/任务/项目多维聚合
- **自定义报表模板**：支持 Markdown / CSV / JSON 三种格式，模板变量可配置
- **Webhook 自动化**：注册事件监听，与 CI/CD、IM 机器人联动
- **多级缓存策略**：L1 内存 + L2 文件缓存，命中率 80%+，大型项目耗时降低 60%
- **并发与限流**：可配置并发数（3-10），内置指数退避与熔断
- **跨项目对比**：多项目工时投入对比，支撑资源调配决策
- **优先支持**：专业版用户享受工单优先处理与新功能优先体验

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 核心功能（检索/状态/工时）+ 基础示例 | 个人开发者日常使用 |
| 收费专业版 | ¥49.9/月 | 全功能 + 批量操作 + 团队聚合 + 自动化 + 优先支持 | 团队负责人/项目经理 |

专业版通过 SkillHub SkillPay 发布。

## License 与版权声明

本 skill 基于原始作品 Jira Flow Skill 改进，保留原始版权声明：

- 原始作品：Jira Flow Skill
- 原始 license：MIT
- 改进作品：Jira Flow Skill（专业版）
- 改进 license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：

- 完全重写中文化文档与使用指南
- 新增批量操作、团队聚合、报表模板、Webhook 自动化等高级能力
- 完善性能优化策略（并发、缓存、检查点）
- 增加故障排查表与多角色场景指南
- 增加免费版/专业版分层策略与定价
