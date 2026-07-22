---
slug: "cron-setup-guide"
name: "cron-setup-guide"
version: "1.0.0"
displayName: "定时任务设置指南(专业版)"
summary: "Agent Gateway定时任务设置完全指南专业版，含Webhook投递、模型覆盖、话题投递、退避策略、高级配置项。"
license: "Proprietary"
edition: "pro"
description: |-
  定时任务设置指南专业版是在免费版基础上的全功能升级，为AI Agent提供完整的定时调度配置能力。专业版解锁Webhook投递、模型覆盖、思考强度配置、Telegram话题投递、退避策略调优、高级配置项等高级特性，实现企业级定时任务管理。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
  - 定时任务
  - 调度配置
  - Webhook
  - 企业自动化
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 定时任务设置指南(专业版)

## 核心能力

### 三种调度类型
> 详细内容已移至 `references/detail.md`

**输入**: 用户提供三种调度类型所需的指令和必要参数。
**处理**: 按照skill规范执行三种调度类型操作,遵循单一意图原则。
**输出**: 返回三种调度类型的执行结果,包含操作状态和输出数据。### 双会话模式
| 模式 | 用途 | payload类型 | 上下文继承 |
|------|------|-------------|------------|
| **main**（主会话） | 系统事件，融入正常心跳流程 | `systemEvent` | 继承主会话上下文 |
| **isolated**（独立会话） | 后台任务，不污染主会话历史 | `agentTurn` | 独立上下文 |

**决策原则**：
- 任务需要主会话上下文（如引用之前对话）→ `main`
- 任务是独立的后台操作（如数据汇总、定时报告）→ `isolated`
- 任务结果需要投递到外部频道或Webhook → 必须 `isolated`
- 任务是简单的提醒通知 → `main`（更轻量）
- 任务使用模型覆盖或高思考强度 → 建议 `isolated`（避免占用主会话资源）

**输入**: 用户提供双会话模式所需的指令和必要参数。
**处理**: 按照skill规范执行双会话模式操作,遵循单一意图原则。### 模型覆盖与思考强度（专业版）
| 参数 | 可选值 | 适用场景 |
|------|--------|----------|
| `--model` | `opus` / `sonnet` / `haiku` | 根据任务复杂度选择模型 |
| `--thinking` | `low` / `medium` / `high` | 控制推理深度 |

**模型选择矩阵**：

| 任务类型 | 推荐模型 | 推荐思考强度 | 理由 |
|----------|----------|-------------|------|
| 简单数据汇总 | `haiku` | `low` | 快速、低成本 |
| 邮件简报生成 | `sonnet` | `medium` | 平衡质量与成本 |
| 复杂分析报告 | `opus` | `high` | 最高质量输出 |
| 代码审查任务 | `opus` | `high` | 需要深度推理 |
| 日常健康检查 | `haiku` | `low` | 简单检查即可 |

### 退避策略调优（专业版）
> 详细内容已移至 `references/detail.md`

**输入**: 用户提供退避策略调优（专业版）所需的指令和必要参数。
**处理**: 按照skill规范执行退避策略调优（专业版）操作,遵循单一意图原则。
**输出**: 返回退避策略调优（专业版）的执行结果,包含操作状态和输出数据。### 作业管理命令
**输入**: 用户提供作业管理命令所需的指令和必要参数。
**处理**: 按照skill规范执行作业管理命令操作,遵循单一意图原则。
**输出**: 返回作业管理命令的执行结果,包含操作状态和输出数据。### Cron vs Heartbeat 决策矩阵
| 场景 | 推荐 | 理由 |
|------|------|------|
| 精确时间（如"每周一9点"） | **cron** | 支持精确时间触发 |
| 批量检查（邮箱+日历+天气） | **heartbeat** | 一次性触发多个检查 |
| 一次性提醒 | **cron** | 支持at类型 |
| 后台自动化（频繁/嘈杂） | **cron (isolated)** | 隔离上下文，不污染主会话 |
| 主会话上下文相关任务 | **heartbeat** | 融入正常心跳流程 |
| 跨时区任务 | **cron** | 支持显式时区设置 |
| 需要Webhook投递 | **cron** | 支持webhook投递模式 |
| 模型覆盖任务 | **cron** | 支持model参数 |
| 简单周期性检查 | **heartbeat** | 无需配置，自动执行 |
### main（主会话）

执行main（主会话）操作,处理用户输入并返回结果。

**输入**: 用户提供main（主会话）所需的参数和指令。

**输出**: 返回main（主会话）的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`main（主会话）`相关配置参数进行设置
#
## 适用场景

### 场景一：企业级晨间简报（独立开发者角色）
> 详细内容已移至 `references/detail.md`

### 场景二：Webhook数据同步（运维工程师角色）
> 详细内容已移至 `references/detail.md`

### 场景三：周报分析（项目经理角色）
> 详细内容已移至 `references/detail.md`

### 场景四：工作日定时健康检查（运维工程师角色）
> 详细内容已移至 `references/detail.md`

### 场景五：多渠道投递（技术负责人角色）
**场景描述**：每月1号生成月度技术总结，同时投递到Telegram团队话题和Webhook归档系统。

**关键决策**：
- 拆分为两个作业：单作业单投递目标，便于独立管理
- 同时触发但独立执行：避免一个失败影响另一个
- 使用相同cron表达式：确保同步触发

## 使用流程

### 60秒上手（创建带模型覆盖的深度任务）
> 详细内容已移至 `references/detail.md`

### 120秒标准搭建（Webhook投递）
配置一个将结果POST到HTTP端点的定时任务：

```bash
skill-platform cron add \
  --name "数据同步" \
  --cron "0 */6 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "从上游系统拉取最新数据并同步至本地" \
  --webhook "https://api.example.com/hooks/sync" \
  --webhook-signing-secret "your-secret-key"
```

关键差异：
1. `--webhook`：投递到HTTP端点（替代 `--announce`）
2. `--webhook-signing-secret`：签名密钥，端点可验证请求来源

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

| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 任务不执行 | `cron.enabled: false` | 在config.json中启用cron | 高 |
| 任务不执行 | Gateway未持续运行 | 确保Gateway进程常驻 | 高 |
| 任务不执行 | 时区设置错误 | 检查 `--tz` 参数 | 高 |
| 任务反复延迟 | 连续失败触发退避 | 检查任务逻辑；调整退避参数 | 高 |
| Webhook投递失败 | URL不可达或超时 | 检查URL；调整 `webhookTimeout` | 高 |
| Webhook签名验证失败 | signingSecret不匹配 | 核对客户端与服务端密钥 | 高 |
| Telegram话题投递失败 | 话题ID格式错误 | 使用 `topic:详情见说明` 显式格式 | 中 |
| Telegram话题投递失败 | supergroup ID格式错误 | 确保以 `-100` 开头 | 中 |
| 模型覆盖无效 | 模型名称拼写错误 | 使用 `opus`/`sonnet`/`haiku` | 中 |
| 思考强度无效 | 参数值错误 | 使用 `low`/`medium`/`high` | 中 |
| 作业历史丢失 | runLog配置过小 | 调整 `maxBytes` 和 `keepLines` | 低 |
| 独立会话上下文丢失 | sessionRetention过短 | 调整 `sessionRetention` 时长 | 低 |
| 主会话被污染 | 错误使用main模式 | 改用 `isolated` 模式 | 中 |
| 作业列表混乱 | 未及时清理 | 使用 `cron cleanup` 清理 | 低 |
| 退避策略过于激进 | maxDelay过小 | 增大 `maxDelay` 至3600秒 | 中 |
| 退避策略过于保守 | baseDelay过大 | 减小 `baseDelay` 至30秒 | 中 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Agent Gateway**: 需启用cron调度器（`cron.enabled: true`）
- **Python**: 3.8+（用于Webhook签名验证脚本）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Agent Gateway | 运行时 | 必需 | Agent平台内置 |
| skill-platform CLI | 工具 | 必需 | Agent平台内置 |
| Telegram Bot | 投递通道 | 否 | 注册Telegram Bot获取 |
| Discord Bot | 投递通道 | 否 | 注册Discord Bot获取 |
| WhatsApp Business | 投递通道 | 否 | 注册WhatsApp Business API |
| Webhook端点 | 投递通道 | 否 | 自建或第三方服务 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 专业版使用 **GPT-4o** 模型路由，确保复杂调度场景的配置质量
- 支持模型覆盖（`opus`/`sonnet`/`haiku`），按任务复杂度灵活选择

### API Key 配置
- Telegram投递需要Telegram Bot Token（存储在Agent Gateway配置中）
- Discord投递需要Discord Bot Token（存储在Agent Gateway配置中）
- WhatsApp投递需要WhatsApp Business API凭证
- Webhook签名密钥由用户自定义，存储在作业配置中
- 禁止在SKILL.md或脚本中硬编码Token

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent配置企业级定时任务


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 与CI/CD系统集成
```bash
skill-platform cron run <deploy-notify-job-id>

skill-platform cron add \
  --name "部署后验证" \
  --at "5m" \
  --session isolated \
  --message "验证最新部署的功能" \
  --webhook "https://ci.example.com/hooks/verify" \
  --webhook-signing-secret "ci-secret" \
  --delete-after-run
```

### 与监控系统集成
```bash
skill-platform cron add \
  --name "服务健康检查" \
  --cron "0 * * * *" \
  --session isolated \
  --message "检查服务健康状态" \
  --model "haiku" \
  --webhook "https://monitoring.example.com/hooks/alert" \
  --webhook-signing-secret "monitor-secret"
```

### 与团队协作平台集成
```bash
skill-platform cron add \
  --name "月度总结" \
  --cron "0 10 1 * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "生成月度工作总结" \
  --model "opus" \
  --thinking high \
  --announce \
  --channel telegram \
  --to "-1001234567890:topic:monthly"
```

### 与归档系统集成
```bash
skill-platform cron add \
  --name "周度归档" \
  --cron "0 18 * * 5" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message "归档本周工作记录至知识库" \
  --webhook "https://kb.example.com/hooks/archive" \
  --webhook-signing-secret "kb-secret" \
  --webhook-header "X-Archive-Type" "weekly"
```

### 从免费版升级至专业版
1. **无需迁移数据**：专业版完全兼容免费版的作业格式
2. **新增功能激活**：
   - 启用Webhook投递：编辑作业添加 `--webhook` 参数
   - 启用模型覆盖：编辑作业添加 `--model` 参数
   - 启用话题投递：编辑作业的 `--to` 参数为话题格式
3. **配置升级**：
   - 在 `~/.skill-platform/config.json` 中添加 `backoff` 配置
   - 添加 `delivery` 全局配置
4. **指令兼容**：免费版的所有命令在专业版中均可使用

### 版本更新历史
| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-07 | 初版发布，含完整投递模式、模型覆盖、退避策略 |

## 常见问题

### Q1：免费版与专业版有什么区别？
免费版提供三种调度类型、双会话模式、基础投递（announce/none）、作业管理命令。专业版解锁Webhook投递、模型覆盖、思考强度配置、Telegram话题投递、退避策略调优、高级配置项、Cron与Heartbeat对比决策、多角色场景指南、性能优化策略、多平台集成示例。此外提供完整FAQ（15问）与故障排查表（16项）。

### Q2：Webhook投递如何工作？
任务执行完成后，调度器将结果以JSON格式POST到指定的HTTP端点。请求包含 `X-Signature` 头（HMAC-SHA256签名），服务端可验证请求来源。支持自定义头、超时控制、bestEffort模式。Webhook模式仅适用于 `isolated` 会话任务。

### Q3：模型覆盖有什么用？
模型覆盖允许为特定任务指定不同的LLM模型，而非使用默认路由。简单任务（如健康检查）用 `haiku` 降低成本，复杂任务（如深度分析）用 `opus` 确保质量。配合 `thinking` 参数控制推理深度，实现成本与质量的平衡。

### Q4：Telegram话题投递的格式是什么？
支持两种格式：(1) 显式格式 `-1001234567890:topic:123`（推荐）；(2) 简写格式 `-1001234567890:123`。supergroup ID必须以 `-100` 开头，话题ID为数字。推荐使用显式 `topic:` 标记，便于阅读与维护。

### Q5：退避策略如何配置？
默认退避序列为 30s → 1m → 5m → 15m → 60m，成功后重置。可通过 `retry` 配置自定义：`maxAttempts`（最大重试次数）、`backoff`（退避算法）、`baseDelay`（基础延迟）、`maxDelay`（最大延迟）。指数退避适合大多数场景，线性退避适合需要稳定间隔的场景。

### Q6：Cron和Heartbeat应该如何选择？
精确时间触发用cron，批量检查用heartbeat，一次性提醒用cron，后台自动化用cron(isolated)，主会话上下文任务用heartbeat，跨时区任务用cron，需要Webhook投递用cron，模型覆盖任务用cron。详见"Cron vs Heartbeat 决策矩阵"。

### Q7：主会话和独立会话有什么区别？
主会话（main）继承当前对话上下文，适合需要引用之前讨论的系统事件，payload类型为 `systemEvent`。独立会话（isolated）创建全新上下文，不污染主会话历史，适合后台任务，payload类型为 `agentTurn`。需要投递到外部频道或Webhook的任务必须使用独立会话。使用模型覆盖或高思考强度的任务建议使用独立会话，避免占用主会话资源。

### Q8：`--at` 参数支持哪些时间格式？
支持两种格式：(1) ISO 8601绝对时间，如 `2026-07-20T10:00:00Z`；(2) 相对时间，如 `20m`（20分钟后）、`2h`（2小时后）、`1d`（1天后）。相对时间从作业创建时刻开始计算。

### Q9：cron表达式的5个字段分别是什么？
标准5字段格式：`分 时 日 月 周`。例如 `0 7 * * *` 表示每天7点0分。字段取值范围：分(0-59)、时(0-23)、日(1-31)、月(1-12)、周(0-6，0为周日)。`*` 表示任意值，`-` 表示范围（如 `1-5`），`,` 表示列表（如 `1,3,5`），`/` 表示步进（如 `*/6` 表示每6单位）。

### Q10：为什么建议显式指定时区？
不指定时区时默认使用UTC，可能导致任务在非预期时间触发。例如期望"每天早上7点"但实际在UTC 7点（即北京时间15点）触发。显式指定 `--tz "Asia/Shanghai"` 可确保任务按本地时间执行。时区使用IANA格式（如 `Asia/Shanghai`、`America/New_York`）。

### Q11：如何查看作业的运行历史？
使用 `skill-platform cron runs --id <job-id> --limit 10` 查看指定作业的最近10次运行记录。使用 `--include-failures` 参数查看失败详情。运行历史存储在 `~/.skill-platform/cron/runs/<jobId>.jsonl`，包含每次执行的开始时间、结束时间、状态、输出等信息。

### Q12：作业日志过大怎么办？
通过 `~/.skill-platform/config.json` 中的 `runLog.maxBytes` 控制单作业日志最大大小（默认2MB），`runLog.keepLines` 控制保留行数（默认2000）。根据作业输出量调整这两个参数。日志过大时，较早的记录会被自动截断。

### Q13：如何暂停和恢复作业？
使用 `skill-platform cron pause <job-id>` 暂停作业，暂停后作业不再被调度执行。使用 `skill-platform cron resume <job-id>` 恢复作业。暂停状态不会影响作业的配置，仅暂停调度。

### Q14：如何批量清理已完成作业？
使用 `skill-platform cron cleanup --status done --older-than 7d` 清理7天前已完成（status=done）的作业。可根据需要调整 `--status` 和 `--older-than` 参数。建议定期清理，避免作业列表膨胀。

### Q15：多个任务可以同时触发吗？
可以。多个任务使用相同的cron表达式会同时触发。调度器会并行执行这些任务（各自在独立的isolated会话中）。但建议错峰调度，避免负载集中。对于有依赖关系的任务，应拆分为多个作业并通过Webhook串联。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

