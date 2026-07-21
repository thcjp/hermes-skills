---
slug: token-manager
name: token-manager
version: "1.2.0"
displayName: Token Manager
summary: Universal LLM Token Manager - Monitor usage and provide cost-saving recommendations
  for Kimi, Ope...
license: MIT
description: |-
  Universal LLM Token Manager - Monitor usage and provide cost-saving
  recommendations for Kimi, Ope。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
---

# Token Manager
Universal LLM Token Manager with proactive monitoring and analytics.

## When to Use
Use this skill when you need to:

* Monitor LLM API token usage and costs
* Get cost-saving recommendations
* Set up automated balance alerts
* Track usage across multiple sessions
* Generate daily/weekly usage reports

## Quick Start
```bash
cd /path/to/token-manager
export MOONSHOT_API_KEY="[REDACTED]"

node scripts/manager.js report 11000 146 42000 200000 off 9.26 moonshot kimi-k2.5
```

## 核心能力
### 1. Usage Monitoring
Real-time session analysis with cost-saving suggestions.

### 2. Scheduled Alerts (P0)
Automatic balance monitoring with proactive notifications.

### 3. Built-in Tool Integration (P1)
Register as Skill平台 tool for seamless usage.

### 4. Cross-Session Analytics (P2)
Track spending patterns and generate reports.

## Supported Providers
| Provider | Balance Query | Token Estimate | Pricing |
| --- | --- | --- | --- |
| Kimi/Moonshot | ✅ API | ✅ API | ¥12/1M tokens |
| OpenAI | ❌ Console | ❌ Approx | USD/1M tokens |
| Anthropic/Claude | ❌ Console | ❌ Approx | USD/1M tokens |
| Google/Gemini | ❌ Console | ❌ Approx | USD/1M tokens |
| Ollama/Local | N/A Free | N/A | FREE |

## Cost-Saving Recommendations
### Context Management
| Scenario | Recommendation | Action |
| --- | --- | --- |
| Context > 80% | 🚨 Critical: Must compact immediately | `/compact` |
| Context > 50% | 📊 Suggest: Consider compacting | `/compact` |
| Session > 50k tokens | ⚠️ Warning: Split tasks now | `/spawn` |
| Session > 20k tokens | 💡 Tip: Use sub-agents for large tasks | `/spawn` |

### Reasoning Optimization
| Scenario | Recommendation | Action |
| --- | --- | --- |
| Reasoning ON + small task (<5k tokens) | 💡 Can disable to save 20-30% | `/thinking off` |
| Reasoning ON + complex task | ✅ Keep on for quality | Keep |

### Provider-Specific Tips
| Scenario | Recommendation |
| --- | --- |
| Balance < ¥5 | 🚨 Enable save mode, avoid large tasks |
| Using GPT-4 | 💡 Consider GPT-4o-mini for 10x savings |
| Using Claude Opus | 💡 Consider Claude Sonnet for 5x savings |
| Running Ollama | 🎉 Free! No API costs |

## Commands
### Manager (Core)
```bash
node scripts/manager.js report <tokensIn> <tokensOut> <contextUsed> <contextMax> <thinking> [balance] [provider] [model] [apiKey]
node scripts/manager.js balance [provider] [apiKey]
node scripts/manager.js estimate <provider> <inputTokens> <outputTokens> [model]
node scripts/manager.js providers
node scripts/manager.js history
```

### Scheduler (P0 - Cron Alerts)
```bash
node scripts/scheduler.js check <provider> <threshold>

node scripts/scheduler.js stats
```

### Session Tracker (P2 - Analytics)
```bash
node scripts/session-tracker.js record <provider> <model> <tokensIn> <tokensOut> <cost> [currency]

node scripts/session-tracker.js daily [date]
node scripts/session-tracker.js weekly
node scripts/session-tracker.js recommend
```

## P0: Scheduled Monitoring & Alerts
Setup automatic balance monitoring with cron jobs.

### Setup Cron Job
```bash
skill-platform cron add \
  --name "token-balance-check" \
  --schedule "0 * * * *" \
  --command "cd /path/to/token-manager && node scripts/scheduler.js check moonshot 5"
```

### Alert Rules
| Condition | Action | Cooldown |
| --- | --- | --- |
| Balance < threshold | Send alert | 1 hour |
| Balance < ¥1 | Send urgent alert | 30 min |
| 3 alerts in 24h | Suggest adding funds | - |

### Alert Output
When triggered, outputs JSON:

```json
{
  "alert": true,
  "balance": 3.50,
  "threshold": 5,
  "messages": {
    "en": "🚨 [URGENT] Token Manager Alert...",
    "cn": "🚨 [紧急] Token 管家提醒..."
  }
}
```

## P1: Tool Integration
Register as Skill平台 tool for direct usage.

### Tool Configuration
Add to `skill-platform.json`:

```json
{
  "tools": {
    "token_status": {
      "command": "cd /path/to/token-manager && node scripts/manager.js report",
      "description": "Check current token usage and costs"
    },
    "token_balance": {
      "command": "cd /path/to/token-manager && node scripts/manager.js balance",
      "description": "Query account balance"
    }
  }
}
```

### Usage After Registration
```bash
skill-platform tool token_status 11000 146 42000 200000 off 9.26 moonshot
skill-platform tool token_balance moonshot
```

## P2: Cross-Session Tracking
Track usage patterns across multiple sessions.

### Recording Sessions
Automatically or manually record each session:

```bash
node scripts/session-tracker.js record moonshot kimi-k2.5 5000 500 0.06 CNY
```

### Daily Report
```bash
node scripts/session-tracker.js daily
```

### Weekly Report
```bash
node scripts/session-tracker.js weekly
```

### Smart Recommendations
```bash
node scripts/session-tracker.js recommend
```

## Environment Variables
* `MOONSHOT_API_KEY` - Kimi/Moonshot API key
* `OPENAI_API_KEY` - OpenAI API key (optional)
* `ANTHROPIC_API_KEY` - Anthropic API key (optional)

## Security
* API keys read from environment variables only
* All data stored locally in `.data/` directory
* No data uploaded to third-party servers
* Network requests only to official LLM APIs
* Alert state persisted locally with cooldown logic

## Pricing Reference
### Kimi/Moonshot
* K2.5: ¥12 / 1M tokens

### OpenAI
* GPT-4o: $2.5 / $10 per 1M
* GPT-4o-mini: $0.15 / $0.6 per 1M
* GPT-3.5-turbo: $0.5 / $1.5 per 1M

### Anthropic
* Claude 3.5 Sonnet: $3 / $15 per 1M
* Claude 3 Opus: $15 / $75 per 1M
* Claude 3 Haiku: $0.25 / $1.25 per 1M

### Google Gemini
* Gemini 1.5 Pro: $3.5 / $10.5 per 1M
* Gemini 1.5 Flash: $0.35 / $1.05 per 1M

### Ollama
* Local execution: FREE

---

---

通用 LLM Token 管理工具，支持主动监控和数据分析。

## 使用场景
在以下情况使用此 skill：

* 监控 LLM API token 使用和费用
* 获取省钱优化建议
* 设置自动余额提醒
* 追踪多会话使用模式
* 生成每日/每周使用报告

## 快速开始
```bash
cd /path/to/token-manager
export MOONSHOT_API_KEY="[REDACTED]"

node scripts/manager.js report 11000 146 42000 200000 off 9.26 moonshot kimi-k2.5
```

## 核心功能
### 1. 使用监控
实时会话分析，提供省钱建议。

### 2. 定时提醒 (P0)
自动余额监控，主动通知。

### 3. 工具集成 (P1)
注册为 Skill平台 工具，无缝使用。

### 4. 跨会话分析 (P2)
追踪消费模式，生成报告。

## 支持的提供商
| 提供商 | 余额查询 | Token 估算 | 价格 |
| --- | --- | --- | --- |
| Kimi/Moonshot | ✅ API | ✅ API | ¥12/百万 |
| OpenAI | ❌ 控制台 | ❌ 估算 | USD/百万 |
| Anthropic/Claude | ❌ 控制台 | ❌ 估算 | USD/百万 |
| Google/Gemini | ❌ 控制台 | ❌ 估算 | USD/百万 |
| Ollama/本地 | N/A 免费 | N/A | 免费 |

## 省钱优化建议
### 上下文管理
| 场景 | 建议 | 操作 |
| --- | --- | --- |
| 上下文 > 80% | 🚨 紧急：必须立即压缩 | `/compact` |
| 上下文 > 50% | 📊 建议：适时压缩 | `/compact` |
| 会话 > 50k tokens | ⚠️ 警告：立即拆分任务 | `/spawn` |
| 会话 > 20k tokens | 💡 提示：大任务使用子代理 | `/spawn` |

### 推理优化
| 场景 | 建议 | 操作 |
| --- | --- | --- |
| Reasoning 开启 + 小任务 (<5k tokens) | 💡 可关闭节省 20-30% | `/thinking off` |
| Reasoning 开启 + 复杂任务 | ✅ 保持开启确保质量 | 保持 |

### 提供商特定建议
| 场景 | 建议 |
| --- | --- |
| 余额 < ¥5 | 🚨 开启省钱模式，避免大任务 |
| 使用 GPT-4 | 💡 考虑 GPT-4o-mini 省 10 倍 |
| 使用 Claude Opus | 💡 考虑 Claude Sonnet 省 5 倍 |
| 运行 Ollama | 🎉 免费！无 API 费用 |

## 命令
### 管理器（核心）
```bash
node scripts/manager.js report <输入tokens> <输出tokens> <上下文已用> <上下文上限> <推理状态> [余额] [提供商] [模型] [apiKey]
node scripts/manager.js balance [提供商] [apiKey]
node scripts/manager.js estimate <提供商> <输入tokens> <输出tokens> [模型]
node scripts/manager.js providers
node scripts/manager.js history
```

### 调度器 (P0 - 定时提醒)
```bash
node scripts/scheduler.js check <提供商> <阈值>

node scripts/scheduler.js stats
```

### 会话追踪器 (P2 - 分析)
```bash
node scripts/session-tracker.js record <提供商> <模型> <输入tokens> <输出tokens> <费用> [货币]

node scripts/session-tracker.js daily [日期]
node scripts/session-tracker.js weekly
node scripts/session-tracker.js recommend
```

## P0: 定时监控与提醒
使用 cron 设置自动余额监控。

### 设置定时任务
```bash
skill-platform cron add \
  --name "token-balance-check" \
  --schedule "0 * * * *" \
  --command "cd /path/to/token-manager && node scripts/scheduler.js check moonshot 5"
```

### 提醒规则
| 条件 | 动作 | 冷却时间 |
| --- | --- | --- |
| 余额 < 阈值 | 发送提醒 | 1 小时 |
| 余额 < ¥1 | 发送紧急提醒 | 30 分钟 |
| 24 小时内 3 次提醒 | 建议充值 | - |

### 提醒输出
触发时输出 JSON：

```json
{
  "alert": true,
  "balance": 3.50,
  "threshold": 5,
  "messages": {
    "en": "🚨 [URGENT] Token Manager Alert...",
    "cn": "🚨 [紧急] Token 管家提醒..."
  }
}
```

## P1: 工具集成
注册为 Skill平台 工具直接使用。

### 工具配置
添加到 `skill-platform.json`：

```json
{
  "tools": {
    "token_status": {
      "command": "cd /path/to/token-manager && node scripts/manager.js report",
      "description": "Check current token usage and costs"
    },
    "token_balance": {
      "command": "cd /path/to/token-manager && node scripts/manager.js balance",
      "description": "Query account balance"
    }
  }
}
```

### 注册后使用
```bash
skill-platform tool token_status 11000 146 42000 200000 off 9.26 moonshot
skill-platform tool token_balance moonshot
```

## P2: 跨会话追踪
追踪多会话使用模式。

### 记录会话
自动或手动记录每个会话：

```bash
node scripts/session-tracker.js record moonshot kimi-k2.5 5000 500 0.06 CNY
```

### 每日报告
```bash
node scripts/session-tracker.js daily
```

### 每周报告
```bash
node scripts/session-tracker.js weekly
```

### 智能建议
```bash
node scripts/session-tracker.js recommend
```

## 环境变量
* `MOONSHOT_API_KEY` - Kimi/Moonshot API 密钥
* `OPENAI_API_KEY` - OpenAI API 密钥（可选）
* `ANTHROPIC_API_KEY` - Anthropic API 密钥（可选）

## 安全说明
* API 密钥仅从环境变量读取
* 所有数据本地存储在 `.data/` 目录
* 无数据上传到第三方服务器
* 网络请求仅访问官方 LLM API
* 提醒状态本地持久化，带冷却逻辑

## 价格参考
### Kimi/Moonshot
* K2.5: ¥12 / 百万 tokens

### OpenAI
* GPT-4o: $2.5 / $10 每百万
* GPT-4o-mini: $0.15 / $0.6 每百万
* GPT-3.5-turbo: $0.5 / $1.5 每百万

### Anthropic
* Claude 3.5 Sonnet: $3 / $15 每百万
* Claude 3 Opus: $15 / $75 每百万
* Claude 3 Haiku: $0.25 / $1.25 每百万

### Google Gemini
* Gemini 1.5 Pro: $3.5 / $10.5 每百万
* Gemini 1.5 Flash: $0.35 / $1.05 每百万

### Ollama
* 本地运行：免费

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 示例
### 示例1：基础用法
```
```bash
cd /path/to/token-manager
export MOONSHOT_API_KEY="[REDACTED]"

node scripts/manager.js report 11000 146 42000 200000 off 9.26 moonshot kimi-k2.5
```
```

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Token Manager？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Token Manager有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 性能取决于底层模型能力
