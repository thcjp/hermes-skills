---
slug: token-manager-tool-pro
name: token-manager-tool-pro
version: "1.0.0"
displayName: Token用量管理专业版
summary: 定时余额监控、跨会话分析、团队用量汇总与自动告警，适合团队与企业级LLM成本治理。
license: MIT
edition: pro
description: |-
  Token用量管理工具专业版，面向团队与企业的高阶LLM成本治理平台。

  核心能力:
  - 定时余额监控与自动告警（cron 调度）
  - 跨会话用量追踪与每日/每周报告
  - 多账号统一管理与团队用量汇总
  - 智能省钱建议与模型切换推荐
  - 工具集成注册与命令行直调

  适用场景:
  - 团队多人协作的LLM成本治理
  - 企业级API预算监控与告警
  - 跨项目的用量分析与优化决策

  差异化: 专业版在免费版核心能力之上扩展定时监控与跨会话分析，新增多账号管理、团队汇总、自动告警等企业级能力，并与免费版命令兼容。

  触发关键词: Token管理, 定时监控, 跨会话分析, 团队用量, 自动告警, 成本治理, 预算监控, 多账号管理
tags:
- Token管理
- 成本治理
- 团队监控
- 专业版
tools:
- read
- exec
---

# Token用量管理工具（专业版）

## 概述

专业版在免费版的实时用量监控与省钱建议之上，扩展为面向团队与企业的完整 LLM 成本治理平台。新增定时余额监控、跨会话用量追踪、多账号统一管理、团队用量汇总与自动告警，同时与免费版的命令行语法保持向后兼容。

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 用量监控 | 单会话实时 | 单会话 + 跨会话追踪 |
| 余额查询 | 手动查询 | 定时自动监控 + 告警 |
| 告警机制 | 不支持 | 多级告警（余额/用量/异常） |
| 报告生成 | 不支持 | 每日/每周/月度报告 |
| 多账号管理 | 不支持 | 多账号统一管理 |
| 团队汇总 | 不支持 | 团队用量汇总与分摊 |
| 工具集成 | 不支持 | 注册为平台工具直调 |
| 预算管理 | 不支持 | 预算设置与超支告警 |

## 使用场景

### 场景一：团队 LLM 成本治理

团队负责人希望统一监控所有成员的 API 用量与费用。

```bash
# 添加团队成员账号
token-pro account add --name "开发者A" --provider moonshot --key-env MOONSHOT_API_KEY_A
token-pro account add --name "开发者B" --provider openai --key-env OPENAI_API_KEY_B

# 生成团队周报
token-pro team weekly --output team-report-2026-W29.md

# 输出示例
# 📊 团队周报（2026-W29）
# 团队总费用: ¥286.50
#   - 开发者A (Moonshot): ¥123.40
#   - 开发者B (OpenAI): ¥163.10
# 预算使用: 57.3% (¥500/¥872)
# 💡 建议: 开发者B的OpenAI用量偏高，建议部分任务切换至GPT-4o-mini
```

### 场景二：定时余额监控与告警

设置 cron 定时监控余额，低于阈值时自动告警。

```bash
# 设置定时监控（每小时检查一次）
token-pro cron add \
  --name "token-balance-check" \
  --schedule "0 * * * *" \
  --check moonshot --threshold 5

# 告警规则
# 余额 < ¥5    → 发送提醒（冷却1小时）
# 余额 < ¥1    → 发送紧急提醒（冷却30分钟）
# 24小时内3次  → 建议充值
```

```json
// 告警输出示例
{
  "alert": true,
  "balance": 3.50,
  "threshold": 5,
  "messages": {
    "cn": "🚨 [紧急] Token 管家提醒：余额 ¥3.50，低于阈值 ¥5"
  }
}
```

### 场景三：跨会话用量分析与优化

追踪多会话使用模式，生成优化建议。

```bash
# 记录会话
token-pro session record moonshot kimi-k2.5 5000 500 0.06 CNY

# 生成每日报告
token-pro session daily

# 生成每周报告
token-pro session weekly

# 智能建议
token-pro session recommend

# 输出示例
# 📊 每周用量分析
# 总会话数: 42
# 总费用: ¥56.30
# 平均会话费用: ¥1.34
# 💡 优化建议:
#   1. 周二用量峰值，建议拆分大任务
#   2. 35%的会话可用GPT-4o-mini替代，预计节省¥18/周
```

## 快速开始

```bash
# 1. 初始化专业版工作区
token-pro init --workspace ~/token-pro

# 2. 添加账号
token-pro account add --name "个人" --provider moonshot --key-env MOONSHOT_API_KEY

# 3. 设置定时监控
token-pro cron add --name "balance-check" --schedule "0 * * * *" --check moonshot --threshold 5

# 4. 生成报告
token-pro session weekly --output weekly-report.md

# 5. 查看团队汇总
token-pro team summary
```

## 配置示例

```yaml
# ~/token-pro/config.yaml
edition: pro
accounts:
  - name: 个人-Moonshot
    provider: moonshot
    key_env: MOONSHOT_API_KEY
  - name: 团队-OpenAI
    provider: openai
    key_env: OPENAI_API_KEY
cron:
  enabled: true
  schedules:
    - name: balance-check
      cron: "0 * * * *"
      provider: moonshot
      threshold: 5
    - name: daily-report
      cron: "0 9 * * *"
      action: session-daily
alerts:
  levels:
    - level: warning
      threshold: 5
      cooldown: 3600
    - level: urgent
      threshold: 1
      cooldown: 1800
  channels:
    - console
    - webhook
budget:
  monthly: 500
  currency: CNY
  alert_at: 80%
reports:
  formats: [markdown, json]
  output: ~/token-pro/reports
team:
  enabled: true
  members: 3
  cost_allocation: by-usage
```

## 告警规则库

| 条件 | 动作 | 冷却时间 |
|:-----|:-----|:---------|
| 余额 < 阈值 | 发送提醒 | 1 小时 |
| 余额 < ¥1 | 发送紧急提醒 | 30 分钟 |
| 24小时内3次提醒 | 建议充值 | - |
| 预算使用 > 80% | 发送预算告警 | 24 小时 |
| 单会话费用 > ¥5 | 发送异常告警 | 1 小时 |
| 用量突增 > 200% | 发送异常告警 | 1 小时 |

## 最佳实践

* 为每个团队成员建立独立账号档案，便于成本分摊。
* 定时监控间隔建议不少于 1 小时，避免频繁请求 API。
* 告警冷却时间根据团队节奏调整，避免告警风暴。
* 月度预算设置 80% 预警线，留出缓冲空间。
* 定期导出报告至外部存储，便于年度成本审计。
* 网络请求仅访问官方 LLM API，确保数据安全。

## 常见问题

**Q：专业版与免费版的命令兼容吗？**
A：兼容。免费版的所有命令在专业版中可直接使用，专业版额外提供 `cron`、`session`、`team`、`account` 等子命令。

**Q：定时监控需要额外的服务吗？**
A：需要系统支持 cron 调度（Linux/macOS 自带，Windows 需使用任务计划程序）。

**Q：团队用量数据存储在哪里？**
A：所有数据存储在本地 `~/token-pro/data` 目录，不上传至任何第三方服务器。

**Q：支持多少个账号同时管理？**
A：无硬性上限，但建议单个团队不超过 50 个账号以保证监控性能。

**Q：告警支持哪些通知渠道？**
A：默认控制台输出，可配置 Webhook 通知（支持飞书、钉钉、企业微信等）。

**Q：可以与财务系统对接吗？**
A：专业版支持导出 CSV/JSON 格式的费用明细，便于与财务系统对接。直接 API 对接建议通过中间文件中转。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+
- **cron**: 系统自带（Linux/macOS）或任务计划程序（Windows）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | 官方站点下载 |
| cron | 调度器 | 可选 | 系统自带 |

### API Key 配置
- `MOONSHOT_API_KEY` - Kimi/Moonshot API 密钥
- `OPENAI_API_KEY` - OpenAI API 密钥（可选）
- `ANTHROPIC_API_KEY` - Anthropic API 密钥（可选）
- 多账号场景下，建议按 `PROVIDER_API_KEY_NAME` 格式命名环境变量
- API 密钥仅从环境变量读取，不硬编码

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + Node.js脚本 + cron调度）
- **说明**: 专业版在 Markdown 指令基础上，提供命令行工具、定时调度与团队管理能力
