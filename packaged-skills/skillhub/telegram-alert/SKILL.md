---
slug: "telegram-alert"
name: "telegram-alert"
version: 1.0.1
displayName: "Telegram告警专业版"
summary: "多通道交易告警系统，支持多群组、复杂触发、富媒体消息与团队协作。。面向专业交易团队的多通道告警通知系统。支持Telegram多群组推送、 复合触发条件、富媒体消息（图表/图片）、定时播报与团"
license: "Proprietary"
edition: "pro"
description: |-
  面向专业交易团队的多通道告警通知系统。支持Telegram多群组推送、
  复合触发条件、富媒体消息（图表/图片）、定时播报与团队协作功能。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发.
tags:
  - Finance
  - 告警通知
  - 企业级
  - 团队协作
  - Telegram
  - 社交
  - 通信
  - 请参考
  - 目录中的
  - 脚本文件
  - python3
  - telegram
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Communication"
---
# Telegram告警专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |
| 消息频控与智能排队 | 不支持 | 支持 |

## 核心能力

### PRO版功能增强对比
| 功能 | 免费版 | PRO版 |
|:-----|:-----|:-----|
| 目标群组 | 单一 | 多群组同步 |
| 触发条件 | 单一条件 | 复合(AND/OR) |
| 消息格式 | 基础Markdown | 富媒体+按钮 |
| 通知通道 | 仅Telegram | +钉钉/企微/邮件 |
| 定时播报 | 基础定时 | 工作流自动化 |
| 告警去重 | 不支持 | 智能去重 |
| 优先级 | 不支持 | 3级优先级 |
| 历史分析 | 基础记录 | 统计与分析 |

**输出**: 返回PRO版功能增强对比的处理结果,包含执行状态码、结果数据和执行日志.
### 复合触发条件
```yaml
# PRO版支持复合逻辑
triggers:
  - name: "BTC突破+成交量放大"
    conditions:
      - ticker: BTC-USD
        metric: price
        operator: "above"
        value: 65000
      - ticker: BTC-USD
        metric: volume
        operator: "above"
        value: 1000000000
    logic: "AND"                    # AND 或 OR
# ...
  - name: "跌至支撑位或破前低"
    conditions:
      - ticker: AAPL
        metric: price
        operator: "below"
        value: 170
      - ticker: AAPL
        metric: price
        operator: "below"
        value: 165
    logic: "OR"
```

**处理**: 解析复合触发条件的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回复合触发条件的处理结果,包含执行状态码、结果数据和执行日志.
### 目标群组

针对目标群组,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供目标群组相关的配置参数、输入数据和处理选项.
**输出**: 返回目标群组的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`目标群组`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：多群组信号分发

用户输入："把买入信号同时发到3个Telegram群"

```bash
# 多群组推送
python3 （请参考skill目录中的脚本文件） broadcast \
  --message "买入信号: AAPL 突破阻力位180" \
  --chat-ids "@group1,@group2,@group3" \
  --priority high \
  --include-chart
# ...
# 输出：各群组发送状态
# [OK] @group1 - 发送成功
# [OK] @group2 - 发送成功
# [FAIL] @group3 - 发送失败（重试中）
```

### 场景二：复合触发告警

用户输入："BTC突破65000且成交量超过10亿时提醒"

```bash
# 设置复合触发
python3 （请参考skill目录中的脚本文件） add \
  --name "BTC突破+量能" \
  --conditions "price:BTC-USD:above:65000,volume:BTC-USD:above:1000000000" \
  --logic AND \
  --channels "telegram,dingtalk" \
  --priority high
# ...
# 启动监控
python3 （请参考skill目录中的脚本文件） monitor --multi-channel
```

### 场景三：定时市场播报

用户输入："每天9点和15点发市场概况，带图表"

```bash
# 设置定时播报
python3 （请参考skill目录中的脚本文件） add \
  --name "每日市场播报" \
  --times "09:00,15:00" \
  --message-type "market_summary" \
  --include-chart \
  --include-watchlist \
  --channels "telegram,dingtalk" \
  --chat-ids "@trading_team"
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt
# ...
# 配置多通道
cp config_pro_template.yaml config_pro.yaml
# 填入各通道的凭证
```

### 常用命令

```bash
# 多群组广播
python3 （请参考skill目录中的脚本文件） broadcast --message "信号" --chat-ids "@g1,@g2,@g3"
# ...
# 复合告警
python3 （请参考skill目录中的脚本文件） add --conditions "price:AAPL:above:180,volume:AAPL:above:100M" --logic AND
# ...
# 定时播报
python3 （请参考skill目录中的脚本文件） add --times "09:00,15:00" --message-type market_summary
# ...
# 告警历史分析
python3 （请参考skill目录中的脚本文件） stats --period 30d
python3 （请参考skill目录中的脚本文件） export --format excel
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | telegram-alert处理的内容输入 |,  |
| content | string | 否 | telegram-alert处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "alert 相关配置参数",
    result: "alert 相关配置参数",
    result: "alert 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
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

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+
- **网络**: 需访问各通知通道API

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| python-telegram-bot | Python库 | 必需 | `pip install python-telegram-bot` |
| requests | Python库 | 必需 | `pip install requests` |
| matplotlib | Python库 | 可选 | `pip install matplotlib`（图表生成） |
| Jinja2 | Python库 | 可选 | `pip install jinja2`（消息模板） |
| psycopg2 | Python库 | 可选 | `pip install psycopg2-binary`（历史存储） |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|---:|:---|---:|---:|
| Telegram Bot | `TELEGRAM_BOT_TOKEN` | 必需 | Telegram消息推送 |
| 钉钉 | `DINGTALK_WEBHOOK` | 可选 | 钉钉消息推送 |
| 企业微信 | `WECOM_WEBHOOK` | 可选 | 企微消息推送 |
| 邮件 | `SMTP_HOST`等 | 可选 | 邮件通知 |

- 未配置的通道自动跳过，不影响已配置通道
- 所有凭证存储在本地配置文件

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 多通道告警通知系统，支持复合触发与富媒体消息
- **PRO版特性**: 多群组同步、复合触发、富媒体、多通道、告警去重、优先级管理
- **兼容性**: 完全兼容免费版命令与配置，支持一键迁移

## 案例展示

### PRO多通道配置

```yaml
pro_config:
  channels:
    telegram:
      bot_token: "${TELEGRAM_BOT_TOKEN}"
      groups:
        - chat_id: "@trading_signals"
          name: "交易信号群"
          priority: high
        - chat_id: "@risk_alerts"
          name: "风险告警群"
          priority: critical
        - chat_id: "@market_summary"
          name: "市场概况群"
          priority: normal
# ...
    dingtalk:
      webhook: "${DINGTALK_WEBHOOK}"
      secret: "${DINGTALK_SECRET}"
# ...
    wechat_work:
      webhook: "${WECOM_WEBHOOK}"
# ...
    email:
      smtp_host: "${SMTP_HOST}"
      smtp_port: 587
      username: "${EMAIL_USER}"
      password: "${EMAIL_PASS}"
# ...
  alerts:
    deduplication:
      enabled: true
      window: 300                # 去重窗口（秒）
    priority:
      levels: [critical, high, normal, low]
      routing:
        critical: ["telegram", "dingtalk", "email"]
        high: ["telegram", "dingtalk"]
        normal: ["telegram"]
        low: ["telegram"]
# ...
    triggers:
      max_conditions: 10         # 单告警最大条件数
      logic: ["AND", "OR"]
      custom_scripts: true       # 支持自定义脚本
# ...
  scheduling:
    timezone: "Asia/Shanghai"
    max_schedules: 50
    retry_failed: true
# ...
  history:
    storage: "postgresql"
    retention_days: 365
    analytics: true
```

## 常见问题

### Q1：支持哪些通知通道？

PRO版支持Telegram、钉钉、企业微信、飞书Webhook和邮件五种通道。可同时配置多个通道，告警按优先级自动路由.
### Q2：复合触发条件如何工作？

当所有条件（AND）或任一条件（OR）满足时触发告警。支持价格、成交量、技术指标等多种指标的组合。每个告警最多支持10个条件.
### Q3：告警去重如何工作？

PRO版在配置的去重窗口（默认5分钟）内，相同标的相同类型的告警只发送一次。避免因价格波动导致短时间内重复告警.
### Q4：富媒体消息支持哪些内容？

支持发送图表（自动生成价格走势图）、图片、交互按钮（如"查看详情"、"确认交易"）。图表数据实时获取并渲染.
### Q5：定时播报支持自定义内容吗？

支持。可通过自定义脚本生成播报内容，包括市场概况、持仓P&L、自选股变动等。支持Jinja2模板灵活定制消息格式.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

