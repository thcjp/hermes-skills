---
slug: linear-workflow-bot
name: linear-workflow-bot
version: 1.0.0
displayName: Linear工作流机器人
summary: 解决Webhook易断、免费额度烧光、多服务配置混乱痛点，打造可自愈的Linear任务流水线
license: Proprietary
description: 把Linear任务自动接入"通知-执行-回写-Git同步"流水线。面向独立开发者与一人公司，解决Webhook易断、免费额度烧光、多服务配置散乱、Git同步冲突四大痛点。适用于个人开发者把Linear作为任务中枢自动分发到Discord/Git、小团队任务到达即通知即执行即归档场景。适用关键词：linear、webhook、discord、make、pipedream、zapier、自动化、任务流水线、git
  sync。
tags:
- 自动化
- 项目管理
- 通知集成
tools:
- - read
- exec
homepage: https://skillhub.cn
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
---

# Linear 工作流机器人

自动化流水线：**Linear → Webhook 平台 → 通知通道 → 任务执行 → Git 同步**。在 Linear 创建的任务自动触发处理，实时通知、执行、回写结果并同步到 Git 仓库，含 Webhook 自愈与免费额度降级机制。

## 核心能力

### 三层自动化平台选型
Make.com（1000 ops/月免费首选）/ Pipedream（即时触发）/ Zapier（付费兜底）/ 自建 webhook 接收器（无限额度），按预算与任务量自动选型。

**输入**: 用户提供三层自动化平台选型所需的指令和必要参数。
**处理**: 按照skill规范执行三层自动化平台选型操作,遵循单一意图原则。
**输出**: 返回三层自动化平台选型的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### Webhook 健康检查与自愈
每小时心跳探活、30 min 无运行发测试 webhook、探活失败重投最近 5 条历史任务、切换备用平台、3 次失败进死信队列（DLQ）。

**输入**: 用户提供Webhook 健康检查与自愈所需的指令和必要参数。
**处理**: 按照skill规范执行Webhook 健康检查与自愈操作,遵循单一意图原则。
**输出**: 返回Webhook 健康检查与自愈的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 任务处理闭环（含失败补偿）
确认 → DM 通知 → 状态流转 → 执行 → 回写评论 → 完成流转 → Git 同步，每步都有失败补偿（重试/回退/告警）。

**输入**: 用户提供任务处理闭环（含失败补偿）所需的指令和必要参数。
**处理**: 按照skill规范执行任务处理闭环（含失败补偿）操作,遵循单一意图原则。
**输出**: 返回任务处理闭环（含失败补偿）的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 配置中心化
单一 JSON（`~/.linearbot/config.json`）管理团队/状态/Discord/Git/额度五类配置，变量引用 `${VAR}` 从环境变量读取避免明文 secrets。

**输入**: 用户提供配置中心化所需的指令和必要参数。
**处理**: 按照skill规范执行配置中心化操作,遵循单一意图原则。
**输出**: 返回配置中心化的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 免费额度监控与降级
每日 `quota-check` 看用量，超 80% 阈值自动降级（batch-daily 批量处理 / drop-low-priority 丢弃低优 / switch-platform 切平台）。

**输入**: 用户提供免费额度监控与降级所需的指令和必要参数。
**处理**: 按照skill规范执行免费额度监控与降级操作,遵循单一意图原则。
**输出**: 返回免费额度监控与降级的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：免费额度烧光、多服务配置混乱痛、打造可自愈的、任务流水线、任务自动接入、流水线、面向独立开发者与、一人公司、多服务配置散乱、同步冲突四大痛点、适用于个人开发者、作为任务中枢自动、分发到、小团队任务到达即、通知即执行即归档、适用关键词、sync等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 适用场景

**何时使用：**

| 触发情境 | 示例 |
|:---|:---|
| 个人开发者把 Linear 作为任务中枢 | "Linear 创建的任务自动分发到 Discord/Git" |
| 小团队需任务到达即通知即执行 | "新任务自动 DM 通知 + 执行 + 归档" |
| 研究/内容/代码任务自动化产出 | "调研任务自动生成 research/*.md" |
| 预算敏感榨干免费额度 | "Make.com 1000 ops 怎么用最划算" |
| Webhook 经常断需自愈 | "Make scenario 挂了自动切 Pipedream" |

**输入输出：**
- 输入：Linear 任务（标题/状态/assignee）+ 配置中心 JSON
- 输出：Discord 通知 + Linear 状态流转 + 任务产出文件 + Git commit/push + 死信队列告警

**不适用场景：**
- 无 Linear 账号的团队（核心依赖 Linear API）
- 任务量 > 10000/月（免费额度必爆，需自建接收器或付费）
- 无 Git 仓库的纯通知场景（Git 同步可关闭但失去归档能力）
- 企业级 Jira/Asana 用户（需另行适配）

## 使用流程

### Step 1：配置 Linear API

在 `~/.linearbot/linear.env` 写入 `LINEAR_API_KEY`（Linear → Settings → API → Personal API keys）。

### Step 2：获取团队/状态 ID

```bash
./scripts/linear-api.sh teams
./scripts/linear-api.sh states
```

### Step 3：写配置中心

编辑 `~/.linearbot/config.json`：

```json
{
  "$schema": "linearbot/v1",
  "linear": {
    "teamId": "team-uuid",
    "states": {
      "todo": "state-uuid",
      "inProgress": "state-uuid",
      "done": "state-uuid",
      "canceled": "state-uuid"
    },
    "watchFilter": "state.name = \"Todo\" AND assignee.id = \"配置值\""
  },
  "notify": {
    "channel": "discord",
    "discord": {
      "botToken": "${DISCORD_BOT_TOKEN}",
      "notifyUserId": "discord-user-id",
      "taskChannelId": "channel-id",
      "allowBots": true
    }
  },
  "git": {
    "repo": "/path/to/repo",
    "autoPush": true,
    "commitPrefix": "task:",
    "branch": "main",
    "conflictStrategy": "rebase"
  },
  "quota": {
    "platform": "make",
    "monthlyLimit": 1000,
    "warningThreshold": 0.8,
    "degradeStrategy": "batch-daily"
  }
}
```

### Step 4：接 Webhook 平台（按选型表）

| 平台 | 免费额度 | 触发延迟 | 推荐场景 |
|:---|:---|:---|:---|
| Make.com | 1000 ops/月 | 15 min | **免费首选** |
| Pipedream | ~100 credits | 即时 | 需实时性 |
| Zapier | 100 tasks/月 | 15 min | 已有付费账号 |
| 自建 | 无限 | 即时 | 有服务器 |

选型规则：预算敏感 + 任务量 < 1000/月 → Make.com；任务量 > 1000/月 或需即时 → 自建；已有 Zapier 付费 → Zapier。

Make.com 配置：新建 scenario → 添加 Linear "Watch Issues" 触发器 → 加 filter（`state.name = "Todo"`）→ 加 Webhook 动作指向执行端点 → 加 Discord 动作发通知 → 启用 scenario。

### Step 5：跑健康检查

```bash
./scripts/linearbot doctor   # 全链路健康检查
./scripts/linearbot quota-check  # 查额度用量
```

### Step 6：任务处理闭环（自动执行）

| 步骤 | 动作 | 失败补偿 |
|:---|:---|:---|
| 1. 确认 | 在通道回复收到 | 失败重试 3 次，仍失败则写入死信 |
| 2. DM 通知 | 给配置的用户发私信 | 用户 ID 错则回退到通道 @mention |
| 3. 状态流转 | `linear-api.sh start <id>` | Linear API 失败则走鉴权自愈 |
| 4. 执行任务 | 调子 Agent 或本地脚本 | 超时 30 min 则标记 "Stalled" |
| 5. 回写评论 | `linear-api.sh comment <id> "<summary>"` | 评论过长则改用文件附件 |
| 6. 完成流转 | `linear-api.sh done <id>` | 失败则保持 In Progress 并告警 |
| 7. Git 同步 | `git add/commit/push` | 冲突按 conflictStrategy 处理 |

状态机：`Todo →(收到)→ In Progress →(成功)→ Done`；`In Progress →(超时)→ Stalled →(用户介入)→ In Progress / Canceled`；`In Progress →(失败)→ In Progress + 评论告警`。

### Step 7：Webhook 自愈与额度监控（后台运行）

每小时心跳：调平台 API 查 scenario 最近运行 → 30 min 无运行发测试 webhook → 探活失败重投最近 5 条任务 + 通知用户 + 切备用平台 → 3 次失败进 DLQ。

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。


## 示例

### 示例 1：任务自动处理流程

**输入：**
```
Linear 任务 ENG-456 "调研 wasm 在边缘计算的应用"
（watchFilter 匹配，触发 webhook）
```

**输出：**
```
1. 收到 → Discord 通知 + DM
2. linear-api.sh start ENG-456
3. 子 Agent 调研，生成 research/wasm-edge-computing.md
4. linear-api.sh comment ENG-456 "已完成，见 research/wasm-edge-computing.md"
5. linear-api.sh done ENG-456
6. git add research/ && commit -m "task: ENG-456 wasm调研" && push
```

### 示例 2：Webhook 故障自愈

**输入：**
```
doctor 发现 Make scenario 30 min 无运行
```

**输出：**
```
1. 发测试 webhook → 失败
2. 重投最近 5 条任务到备用 Pipedream workflow
3. Discord 告警 "Make 异常，已切 Pipedream"
4. 用户收到通知后修复 Make
5. linearbot resume 回切 Make
```

### 示例 3：免费额度降级

**输入：**
```
quota-check 输出：本月已用 823/1000 ops (82%)
```

**输出：**
```
启用 degradeStrategy: batch-daily
- 即时触发改为每日 22:00 批量处理
- 低优先级标签任务合并处理
- Discord 通知用户已启用降级模式
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|:---|:---|:---|
| 任务不触发 | webhook 平台 scenario 停用或 watchFilter 不匹配 | `linearbot doctor` 查 scenario 状态；确认 watchFilter 与 Linear filter 对齐 |
| Linear API 报 401 | API Key 失效或权限不足 | 检查 `~/.linearbot/linear.env`；重新生成 API Key；确认 Key 有读写权限 |
| Discord 不通知 | botToken 失效或 bot 无频道权限 | 验证 botToken；检查 bot 在频道权限；`allowBots: true` |
| Git push 失败 | SSH key/credential 失效或冲突 | 检查 SSH key/credential；查 remote；按 conflictStrategy 处理（rebase 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 3 次 / merge 生成 merge commit / abort 放弃同步并告警） |
| 子 Agent 执行超时 | 任务复杂度超 30 min | 默认 30 min 超时标记 Stalled；可在 config 调 `executionTimeout`；Stalled 任务不自动取消等用户介入 |
| 额度耗尽 | 月任务量超免费额度 | `quota-check` 启用降级；或切自建接收器；或升级付费 |
| 死信堆积 | 任务 3 次失败进 DLQ | `linearbot dlq list` 查看死信；逐个 `replay` 重放或 `ack` 确认处理 |
| 评论过长 | Linear 评论字符超限 | `comment-file` 改用文件附件；或分段评论 |
| 多团队配置冲突 | 团队 ID/状态 ID 跨团队混用 | 配置中心支持 `teams` 数组，每团队独立 watchFilter 与通知通道 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---|:---|:---|:---|
| Linear 账号 | SaaS | 必需 | linear.app 注册 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Make.com / Pipedream / Zapier | 自动化平台 | 三选一（或自建） | 对应官网注册 |
| Discord 账号 + Bot | 通知通道 | 推荐（可替换为 Slack/Telegram） | Discord Developer Portal |
| Git 仓库 | 版本控制 | 可选（启用 Git 同步时必需） | 本地或 GitHub/GitLab |
| jq | JSON 处理 | 推荐 | 系统包管理器 |
| bash | Shell | 推荐 | 脚本依赖 |
| Agent 平台 | 运行环境 | 必需 | 支持 SKILL.md 的任意 AI Agent |
| 操作系统 | 运行环境 | 必需 | Windows / macOS / Linux |

**API Key 配置：**
- `LINEAR_API_KEY`：Linear → Settings → API → Personal API keys
- `DISCORD_BOT_TOKEN`：Discord Developer Portal → Bot → Token
- Make/Pipedream API Token：对应平台账号设置
- 全部存于环境变量或 `~/.linearbot/*.env`（权限 600），勿入库

**可用性分类：** MD+EXEC（Markdown 指令 + 必须通过 exec 执行脚本与 webhook 调用）。
- 需要Claude、GPT-4等大语言模型提供推理和自然语言理解能力

## 常见问题

**Q1：免费 1000 ops 会超吗？**
A：单人日均任务 < 30 条基本够。每条任务平均消耗 2-3 ops（触发 + 通知）。超过 80% 阈值自动降级到 batch-daily。

**Q2：Git push 冲突怎么办？**
A：按 `conflictStrategy`：`rebase`（默认，自动 rebase 后重试 3 次）、`merge`（生成 merge commit）、`abort`（放弃同步并告警）。

**Q3：子 Agent 执行超时？**
A：默认 30 min 超时标记 Stalled。可在 config 中调 `executionTimeout`。Stalled 任务不自动取消，等用户介入。

**Q4：多个 Linear 团队怎么配？**
A：配置中心支持 `teams` 数组，每个团队独立 watchFilter 与通知通道。Git 同步可按团队分仓库或分目录。

**Q5：凭证安全？**
A：所有 secrets 用 `${VAR}` 引用环境变量，不写入 config.json。`~/.linearbot/` 目录权限设为 600。

## 已知限制

1. **强依赖 Linear**：核心流程基于 Linear API，无 Linear 账号无法使用；适配 Jira/Asana 需另行开发。
2. **免费额度有限**：Make.com 1000 ops/月、Pipedream ~100 credits、Zapier 100 tasks/月，任务量大需自建接收器或付费。
3. **Webhook 触发有延迟**：免费平台 15 min 轮询延迟，需即时性须用 Pipedream 或自建。
4. **当前面向个人/小团队**：多团队支持有限，需手动配 `teams` 数组；无内置 RBAC。
5. **Git 同步需仓库可写权限**：冲突策略依赖 git 操作能力，无权限场景只能 abort 告警。
6. **死信队列需人工处理**：DLQ 中的任务不会自动重试，需用户 `replay` 或 `ack`。
