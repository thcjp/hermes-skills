---
slug: token-manager
name: token-manager
version: "1.2.0"
displayName: Token Manager
summary: "通用LLM Token管理器,监控Kimi/OpenAI等用量并提供省钱建议,降低API成本"
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
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

---
## 边界条件与限制

Token Manager 作为一款通用 LLM Token 管理器，存在以下边界条件和限制：

### 输入限制
- **Token 数量**：单个会话中处理的 Token 数量受限于 LLM API 的限制，通常在数万到数十万 Token 之间。
- **输入格式**：输入文本必须符合 LLM API 的要求，包括正确的编码格式和长度限制。

### 性能边界
- **处理速度**：Token Manager 的处理速度受限于 LLM API 的响应时间和网络延迟。
- **并发处理**：同时处理多个会话的能力受限于系统资源，如内存和CPU。

### 兼容性约束
- **LLM API**：Token Manager 支持的 LLM API 有限，不支持所有 LLM 服务。
- **操作系统**：Token Manager 主要在 Windows、macOS 和 Linux 操作系统上测试和验证。

### 数据存储
- **本地存储**：Token Manager 使用本地存储来保存数据，存储空间有限，可能需要定期清理旧数据。

### 安全限制
- **API 密钥**：API 密钥不应泄露，应妥善保管，避免未授权访问。
- **数据安全**：Token Manager 不上传数据到第三方服务器，但本地存储的数据安全依赖于操作系统和用户的安全设置。

### 使用场景限制
- **非人员绩效评估**：Token Manager 不适用于实际人员绩效评估，仅用于项目管理、任务规划、进度跟踪和团队协作。

## 已知限制

Token Manager 在使用过程中可能遇到以下已知限制：

### Token 数量限制
- Token Manager 支持的 Token 数量有限，超过限制可能导致处理失败或性能下降。

### 模型兼容性
- Token Manager 可能不支持某些特定 LLM 模型的功能，如特定版本的 GPT 或 Claude。

### 网络依赖
- Token Manager 的性能和可用性高度依赖于网络连接的稳定性和速度。

### 系统资源
- Token Manager 的运行需要一定的系统资源，如内存和CPU，资源不足可能导致性能问题。

### 定时任务限制
- 定时任务（如自动余额提醒）的设置和执行可能受到系统时间设置和cron作业调度限制的影响。

### 数据隐私
- Token Manager 不会存储或分享用户数据，但用户应确保其 API 密钥和其他敏感信息的安全。

## 兼容性说明

Token Manager 与以下系统或服务兼容：

- **操作系统**：Windows 10/11，macOS 10.15+，Linux
- **LLM API**：Kimi/Moonshot，OpenAI，Anthropic/Claude，Google/Gemini，Ollama/Local
- **编程语言**：Node.js

不兼容的情况包括：

- **旧版操作系统**：不支持 Windows 7 及以下版本，macOS 10.14 及以下版本。
- **非官方 LLM API**：不支持未列在支持提供商列表中的 LLM API。
- **非标准 Node.js 环境**：不支持非标准或定制化的 Node.js 环境。

## 安全注意事项

使用 Token Manager 时，请注意以下安全事项：

- **API 密钥保护**：确保 API 密钥不会泄露给未授权的第三方。
- **数据加密**：Token Manager 不存储敏感数据，但建议在传输和存储敏感信息时使用加密。
- **系统安全**：保持操作系统和应用程序的更新，以防止安全漏洞。
- **访问控制**：限制对 Token Manager 的访问，确保只有授权用户可以访问。

遵循这些安全注意事项有助于保护您的数据和系统安全。


## 差异化优势

### 与同类方案对比

在LLM Token管理领域，Token Manager与以下替代方案相比展现出显著的优势：

1. **手动操作**：手动管理LLM Token不仅耗时且容易出错，需要开发者不断监控API使用情况和成本。Token Manager通过自动化监控和报告功能，大幅减少了手动操作的需求，节省了开发者宝贵的时间。

2. **其他工具**：虽然市场上存在一些LLM Token监控工具，但它们通常功能单一，如仅提供余额查询或使用统计。Token Manager则集成了多种功能，包括跨会话分析、自动提醒和智能建议，为用户提供了一个全面的解决方案。

3. **通用方法**：通用方法可能包括自定义脚本或工作流程，但这些通常缺乏灵活性，难以适应不同的LLM API和复杂的使用场景。Token Manager作为专门设计的工具，能够更好地适应各种需求和变化。

### 独特功能

Token Manager的独特功能和创新组合包括：

1. **实时会话分析**：提供实时会话分析，帮助用户了解每个会话的Token使用情况，从而优化后续操作。

2. **跨会话分析**：追踪跨会话的Token使用模式，生成详细报告，帮助用户识别节省成本的潜在机会。

3. **自动提醒和智能建议**：自动监控账户余额，并在达到特定阈值时发送提醒，同时提供基于使用模式的智能建议。

4. **工具集成**：作为Skill平台工具，Token Manager可以直接集成到现有的工作流程中，无缝使用。

5. **多提供商支持**：支持多种LLM API，包括Kimi/Moonshot、OpenAI、Anthropic/Claude等，为用户提供广泛的兼容性。

### 效率提升

使用Token Manager，用户可以：

- **节省时间**：自动化监控和报告功能减少了手动操作的需求，让开发者能够专注于核心任务。
- **减少步骤**：集成多种功能，简化了Token管理流程，减少了需要执行的步骤。

### 应用场景创新

Token Manager的创新应用场景包括：

1. **自动化工作流**：集成Token Manager到自动化工作流中，确保API使用符合预算和性能要求。

2. **团队协作**：在团队环境中使用Token Manager，确保所有成员都能了解Token使用情况，共同优化成本。

3. **个人项目**：独立开发者可以使用Token Manager来监控和管理个人项目中的LLM API使用，确保资源得到有效利用。

