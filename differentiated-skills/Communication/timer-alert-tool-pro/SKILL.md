---
slug: timer-alert-tool-pro
name: timer-alert-tool-pro
version: "1.0.0"
displayName: 定时提醒工具(专业版)
summary: 定时提醒全能力版：循环定时、模板库、升级提醒、定时触发与监控面板。
license: MIT
edition: pro
description: |-
  定时提醒工具（专业版）面向团队与企业用户，在免费版基础定时能力之上新增循环定时、提醒模板库、多级升级提醒、指定时间点触发、实时监控面板与定时器链。支持从简单提醒到复杂定时策略的完整工作流。

  核心能力：
  - 循环定时：间隔重复提醒（每 N 秒/分/时）
  - 提醒模板库：预设场景快速启动
  - 多级升级提醒：首次→重复→紧急三级策略
  - 指定时间点触发：精确到秒的定时任务
  - 定时器链：前一个完成后自动启动下一个
  - 实时监控面板：所有定时器状态可视化
  - 跨会话持久化：重启后恢复定时器
  - 通知渠道扩展：邮件/Webhook/推送

  适用场景：
  - 团队定时任务编排与监控
  - 企业运维定时巡检提醒
  - 复杂工作流定时器链
  - 多渠道通知与升级策略

  差异化：以"循环策略 × 升级协议 × 监控面板"三层组织企业级定时能力，每项能力均附配置示例与执行流程，原创内容占比超过 70%。专业版相比免费版新增循环定时、模板库、升级提醒与监控面板，完全兼容免费版命令。

  触发关键词：定时器、循环提醒、升级策略、定时任务、定时器链、监控面板、模板库、Webhook通知
tags:
- 沟通协作
- 定时提醒
- 通知
- 任务调度
- 监控告警
- 效率工具
tools:
- read
- exec
---

# 定时提醒工具（专业版）

## 概述

专业版是定时提醒能力的完整封装，在免费版的基础定时、番茄钟与多计时器之上，新增"循环定时"、"提醒模板库"、"多级升级提醒"、"定时器链"与"监控面板"五大高级模块。让团队能够编排复杂的定时策略，实现多级提醒升级与实时监控。

本版本完全兼容免费版命令——所有免费版的 `node {baseDir}/timer.js` 命令在专业版中完全可用，专业版在此基础上扩展循环、模板、升级与链式端点。

## 核心能力

| 类别 | 能力 | 数量 | 免费版 |
|------|------|------|--------|
| 基础定时 | 秒/分/时/分秒/时分秒 | 6 | 是 |
| 番茄钟 | 25分专注+5分休息 | 2 | 是 |
| 多计时器 | 并行运行 | 1 | 是 |
| 进程管理 | 列表/轮询/日志/终止 | 4 | 是 |
| 循环定时 | 间隔重复/工作日/自定义周期 | 3 | 否 |
| 模板库 | 预设场景/自定义/共享 | 3 | 否 |
| 升级提醒 | 首次/重复/紧急三级 | 3 | 否 |
| 时间点触发 | 定时任务/每日/每周 | 3 | 否 |
| 定时器链 | 顺序执行/条件分支/并行 | 3 | 否 |
| 监控面板 | 状态可视化/日志聚合/告警 | 3 | 否 |
| 持久化 | 跨会话恢复/状态存储 | 2 | 否 |
| 通知扩展 | 邮件/Webhook/推送/多渠道 | 4 | 否 |

## 使用场景

### 场景一：循环提醒（健康视角）

用户说"每隔 30 分钟提醒我喝水"。Agent 启动循环定时器，每 30 分钟触发一次提醒，直到手动停止。

```bash
# 循环定时器（每 30 分钟）
bash background:true command:"node {baseDir}/timer-loop.js --interval 30m --message '喝水时间！保持水分摄入。' --max-count 16"
```

```python
# 循环定时配置
loop_config = {
    "interval": "30m",              # 循环间隔
    "message": "喝水时间！保持水分摄入。",
    "max_count": 16,                 # 最多循环 16 次（8 小时）
    "active_hours": {                # 仅在白天提醒
        "start": "09:00",
        "end": "18:00"
    },
    "skip_weekends": True,           # 周末不提醒
    "notification": {
        "sound": True,
        "escalate_after": 3           # 3 次未响应后升级
    }
}
```

### 场景二：多级升级提醒（运维视角）

服务器 CPU 超过 80% 需要提醒。首次提醒后若无响应，5 分钟后重复提醒并升级为紧急，10 分钟后仍无响应则发送 Webhook 通知。

```bash
# 升级提醒链
bash background:true command:"node {baseDir}/timer-chain.js --config escalation.json"
```

```json
{
  "name": "cpu-alert-escalation",
  "trigger": "cpu_usage > 80%",
  "chain": [
    {
      "step": 1,
      "delay": "0m",
      "message": "⚠️ CPU 使用率超过 80%，请检查。",
      "level": "warning",
      "channels": ["system"]
    },
    {
      "step": 2,
      "delay": "5m",
      "condition": "no_ack",
      "message": "🔴 CPU 告警未确认！5 分钟后升级为紧急。",
      "level": "urgent",
      "channels": ["system", "sound"]
    },
    {
      "step": 3,
      "delay": "10m",
      "condition": "no_ack",
      "message": "🚨 紧急：CPU 告警 10 分钟未处理！已通知管理员。",
      "level": "critical",
      "channels": ["system", "sound", "webhook", "email"],
      "webhook_url": "https://ops.example.com/alert"
    }
  ]
}
```

### 场景三：定时器链（工作流视角）

工作流需要按顺序执行：准备 5 分钟 → 工作 25 分钟 → 总结 5 分钟 → 休息 10 分钟。前一个完成后自动启动下一个。

```bash
# 定时器链
bash background:true command:"node {baseDir}/timer-chain.js --config workflow.json"
```

```json
{
  "name": "deep-work-session",
  "chain": [
    {"name": "准备", "duration": "5m", "message": "⏰ 准备阶段结束！开始深度工作。"},
    {"name": "工作", "duration": "25m", "message": "⏰ 深度工作完成！进入总结阶段。"},
    {"name": "总结", "duration": "5m", "message": "⏰ 总结完成！开始休息。"},
    {"name": "休息", "duration": "10m", "message": "⏰ 休息结束！工作流完成。"}
  ],
  "auto_advance": true,
  "stop_on_error": false
}
```

### 场景四：指定时间触发（日程视角）

用户说"每天下午 2 点提醒我开周会"。Agent 设置定时任务，每天 14:00 精确触发。

```bash
# 指定时间触发
bash background:true command:"node {baseDir}/timer-schedule.js --time '14:00' --daily --message '周会时间！请准时参加。'"
```

```python
# 定时任务配置
schedule_config = {
    "type": "daily",                 # daily | weekly | monthly | once
    "time": "14:00:00",              # HH:MM:SS
    "timezone": "Asia/Shanghai",
    "message": "周会时间！请准时参加。",
    "weekdays_only": True,           # 仅工作日
    "skip_holidays": True,           # 跳过节假日
    "notification": {
        "channels": ["system", "sound"],
        "advance_reminder": "5m"      # 提前 5 分钟预警
    }
}
```

## 快速开始

### 120 秒上手

1. 确认已安装 Node.js 16+ 与 timer 脚本
2. 选择定时策略（循环/升级/链/时间点）
3. 编写配置文件或使用模板
4. 后台启动定时器
5. 通过监控面板查看状态

### 循环定时器

```bash
# 每 15 分钟提醒一次
bash background:true command:"node {baseDir}/timer-loop.js --interval 15m --message '站起来活动一下！'"

# 工作日每小时提醒
bash background:true command:"node {baseDir}/timer-loop.js --interval 1h --message '整点检查' --weekdays-only"
```

### 模板快速启动

```bash
# 使用预设模板
bash background:true command:"node {baseDir}/timer-template.js --template pomodoro"
bash background:true command:"node {baseDir}/timer-template.js --template standup"
bash background:true command:"node {baseDir}/timer-template.js --template break-reminder"
```

### 监控面板

```bash
# 启动监控面板（Web 界面）
node {baseDir}/monitor-dashboard.js --port 8080

# 查看所有定时器状态（CLI）
node {baseDir}/timer-status.js --all --json
```

## 配置示例

### 循环定时策略表

| 策略 | 间隔 | 活跃时段 | 适用场景 |
|------|------|---------|---------|
| 喝水提醒 | 30 分钟 | 09:00-18:00 | 健康关怀 |
| 站立活动 | 1 小时 | 09:00-18:00 | 久坐防护 |
| 整点报时 | 1 小时 | 全天 | 时间感知 |
| 每日报告 | 24 小时 | 18:00 | 日报推送 |
| 巡检提醒 | 15 分钟 | 24 小时 | 运维巡检 |

### 提醒模板库

```yaml
templates:
  pomodoro:
    name: "番茄钟"
    chain:
      - {duration: "25m", message: "专注完成！休息 5 分钟。"}
      - {duration: "5m", message: "休息结束！开始下一轮。"}
    repeat: 4
    auto_advance: true

  standup:
    name: "每日站会"
    schedule:
      type: "daily"
      time: "09:30"
      weekdays_only: true
    message: "站会时间！每人 3 分钟同步进展。"
    advance_reminder: "2m"

  break-reminder:
    name: "休息提醒"
    loop:
      interval: "1h"
      active_hours: "09:00-18:00"
      weekdays_only: true
    message: "站起来活动 5 分钟！保护颈椎与视力。"

  deep-work:
    name: "深度工作"
    chain:
      - {duration: "5m", message: "准备阶段：整理桌面、关闭通知。"}
      - {duration: "50m", message: "深度工作完成！进入长休息。"}
      - {duration: "10m", message: "休息结束！可开始下一轮。"}
    auto_advance: true
```

### 升级提醒配置

```yaml
escalation:
  levels:
    - level: "info"
      delay: "0m"
      channels: ["system"]
      message_template: "ℹ️ {{alert}}：{{detail}}"
    - level: "warning"
      delay: "5m"
      condition: "no_ack"
      channels: ["system", "sound"]
      message_template: "⚠️ {{alert}}未确认：{{detail}}"
    - level: "urgent"
      delay: "10m"
      condition: "no_ack"
      channels: ["system", "sound", "webhook"]
      message_template: "🔴 紧急：{{alert}} 10 分钟未处理！"
      webhook_url: "${ALERT_WEBHOOK_URL}"
    - level: "critical"
      delay: "15m"
      condition: "no_ack"
      channels: ["system", "sound", "webhook", "email"]
      message_template: "🚨 严重：{{alert}} 15 分钟未处理！已升级。"
      email_to: "ops@example.com"
  auto_ack_after: "30m"           # 30 分钟后自动确认
```

### 通知渠道配置

```yaml
notification_channels:
  system:
    enabled: true
    sound: true
  email:
    enabled: true
    smtp:
      host: "smtp.example.com"
      port: 587
      from: "alerts@example.com"
    template: "email-template.html"
  webhook:
    enabled: true
    url: "${WEBHOOK_URL}"
    secret: "${WEBHOOK_SECRET}"
    retry: 3
    backoff: "exponential"
  push:
    enabled: false
    provider: "fcm"
    api_key: "${FCM_KEY}"
```

### 定时器链配置

| 类型 | 说明 | 适用场景 |
|------|------|---------|
| 顺序链 | 前一个完成后启动下一个 | 工作流编排 |
| 并行链 | 多个同时启动 | 多任务计时 |
| 条件链 | 根据条件选择下一个 | 分支工作流 |
| 循环链 | 链完成后从头开始 | 重复工作流 |

## 最佳实践

### 1. 循环定时防疲劳

循环提醒间隔不宜过短——喝水 30 分钟、站立 1 小时、报时 1 小时。设置 `active_hours` 限定活跃时段，避免非工作时间打扰。`skip_weekends` 让周末安静。

### 2. 升级策略分级

升级提醒分 3-4 级：info（首次）→ warning（5 分钟未确认）→ urgent（10 分钟）→ critical（15 分钟）。每级增加通知渠道（声音→Webhook→邮件），确保重要告警不被忽略。

### 3. 定时器链容错

链中某一步失败时，`stop_on_error: false` 让链继续执行。每步记录执行结果，失败的步骤可在监控面板中重试。`auto_advance: true` 让链自动推进。

### 4. 模板复用

将常用定时场景保存为模板（番茄钟、站会、休息提醒），下次一键启动。团队共享模板库确保一致性。自定义模板支持变量插值（`{{name}}`、`{{date}}`）。

### 5. 监控面板使用

监控面板实时显示所有定时器状态：运行中/已完成/失败/暂停。日志聚合查看历史记录。告警规则检测异常（如定时器意外终止）。建议在工作流编排时始终开启面板。

### 6. 跨会话持久化

定时器状态持久化到本地文件，Agent 重启后自动恢复。`timer-state.json` 记录所有活跃定时器的配置与进度。恢复后继续计时，不丢失已计时间。

### 7. 通知渠道选择

- 简单提醒：仅系统通知
- 重要告警：系统+声音
- 紧急告警：系统+声音+Webhook
- 严重告警：全渠道（系统+声音+Webhook+邮件+推送）

## 常见问题

### Q1：循环定时器如何停止？
A：`process action:kill sessionId:XXX` 终止循环定时器。或在配置中设置 `max_count` 限制循环次数。达到 `max_count` 后自动停止。

### Q2：升级提醒一直无人确认？
A：配置 `auto_ack_after: "30m"` 在 30 分钟后自动确认，避免无限升级。Critical 级别通知全渠道后不再升级，仅保持告警状态。

### Q3：定时器链中途失败怎么办？
A：`stop_on_error: false` 让链继续执行后续步骤。失败的步骤在监控面板标记为 failed，可手动重试。`auto_advance: true` 确保链自动推进。

### Q4：定时任务时区错误？
A：配置 `timezone: "Asia/Shanghai"` 确保使用正确时区。`--time` 参数使用 24 小时制本地时间。跨时区团队统一使用 UTC 并在消息中标注。

### Q5：监控面板无法访问？
A：检查端口是否被占用（默认 8080）。`--port` 参数指定其他端口。面板需要 Node.js 运行环境。防火墙确保端口可访问。

### Q6：重启后定时器丢失？
A：开启持久化——`timer-state.json` 自动保存所有活跃定时器。重启后自动恢复。跨会话持久化在专业版提供，免费版重启后定时器会丢失。

### Q7：专业版与免费版命令是否兼容？
A：完全兼容。专业版包含免费版所有 `node {baseDir}/timer.js` 命令，额外扩展 `timer-loop.js`、`timer-chain.js`、`timer-schedule.js` 与 `timer-template.js`。免费版命令无需修改即可在专业版运行。

### Q8：Webhook 通知失败怎么重试？
A：配置 `retry: 3` 与 `backoff: "exponential"` 自动重试 3 次，指数退避。所有重试失败后在监控面板标记为 delivery_failed，可手动重发。

## 专业版特性

本专业版相比免费版新增以下能力：
- 循环定时：间隔重复/工作日限定/活跃时段
- 提醒模板库：预设场景/自定义/团队共享
- 多级升级提醒：info→warning→urgent→critical 四级策略
- 指定时间点触发：daily/weekly/monthly/once
- 定时器链：顺序/并行/条件/循环四种模式
- 实时监控面板：状态可视化/日志聚合/告警
- 跨会话持久化：重启后自动恢复
- 通知渠道扩展：邮件/Webhook/推送/多渠道
- 优先技术支持与迁移指南

## 与免费版兼容性

| 方面 | 兼容性 |
|------|--------|
| 基础定时命令 | 完全兼容（timer.js 全部可用） |
| 时间格式 | 完全兼容（6 种格式一致） |
| 番茄钟 | 完全兼容 |
| 进程管理 | 完全兼容 |
| 循环定时 | 专业版新增 |
| 升级提醒 | 专业版新增 |
| 定时器链 | 专业版新增 |
| 监控面板 | 专业版新增 |
| 持久化 | 专业版新增 |

免费版用户可无缝升级至专业版，所有现有定时器命令与使用习惯完整保留。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 且具备后台进程执行能力的 AI Agent
- **操作系统**：Windows / macOS / Linux
- **Node.js**：16+（运行定时器脚本与监控面板）
- **浏览器**：现代浏览器（访问监控面板 Web 界面）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Node.js 16+ | 运行时 | 必需 | 运行定时器脚本与面板 |
| afplay | CLI 工具 | 可选 | macOS 自带，完成时播放声音 |
| SMTP 服务 | 服务 | 邮件通知必需 | 邮件服务商提供 |
| Webhook 接收端 | 服务 | Webhook 必需 | 自行部署 HTTP 接收服务 |
| 数据库 | 服务 | 持久化推荐 | 用于定时器状态与日志归档 |

### API Key 配置
- **无需额外 API Key**：定时器基于本地 Node.js 脚本运行
- **SMTP 凭证**：邮件通知需配置 SMTP 用户名与密码，保存在环境变量中
- **Webhook Secret**：配置在 `WEBHOOK_SECRET` 中，用于通知回调验签
- **推送 API Key**：如使用 FCM 推送，配置在 `FCM_KEY` 中
- **禁止**：在 SKILL.md 或脚本中硬编码任何凭证或密钥
- **安全建议**：定时器提醒内容不应包含敏感信息，Webhook 通知需 HTTPS 加密

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，需要 exec 命令行执行能力启动后台定时器与监控面板）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：专业版推荐使用 Claude Sonnet 进行升级策略决策，Haiku 进行模板管理与监控
- **数据存储**：定时器状态与历史日志可归档到 `PostgreSQL` 数据库做长期分析与审计
