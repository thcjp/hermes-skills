---
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
summary: "发丰富交易告警到Telegram,任一加密事件或组合更新"
---
# Telegram Alerts

Send rich trading alerts to Telegram for any crypto event or portfolio update.

## Alert Types

* **Trade alerts**: entry/exit with P&L, entry price, stop, target
* **Price alerts**: trigger when asset crosses threshold
* **Portfolio summaries**: NAV, daily P&L, positions
* **Stop-loss warnings**: drawdown approaching limit
* **Win/loss streaks**: celebration + tilt prevention
* **Scheduled reports**: daily 18:00, weekly Monday

## Usage

```text
Use telegram-alerts to send a trade entry notification for BTC LONG at $68,000

Use telegram-alerts to send my daily portfolio summary

Use telegram-alerts to alert me when SOL breaks $90
```

## 示例

```text
🟢 TRADE OPENED
Asset: BTC/USDT | LONG
Entry: $68,247 | Stop: $67,200 | Target: $70,000
Risk: $0.38 (0.05% NAV) | R:R = 1:2.6
```

## Setup

Requires TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in your .env file.

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

## 核心能力

- Send formatted trading alerts, portfolio updates, and market signals
  via Telegram
- Supports price
- 触发关键词: trading, alerts, portfolio, telegram, rho, send, formatted

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Telegram Alerts？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Telegram Alerts有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **Telegram账号要求**：用户必须拥有一个Telegram账号，并且该账号能够接收消息。
- **消息长度限制**：Telegram消息长度有限制，因此发送的告警信息可能需要截断，导致部分信息丢失。
- **加密事件类型**：技能仅支持已知的加密事件类型，对于自定义或未知的加密事件，技能可能无法正确识别和告警。

### 性能边界
- **并发处理能力**：技能的并发处理能力有限，大量并发请求可能导致处理延迟。
- **响应时间**：在高峰时段，技能的响应时间可能会增加，因为网络和服务器资源可能被大量请求占用。

### 兼容性约束
- **操作系统兼容性**：技能在Windows、macOS和Linux操作系统上运行，但不保证在其他操作系统上的兼容性。
- **Agent平台兼容性**：技能支持SKILL.md的任意AI Agent，但某些特定功能可能因Agent的不同而有所差异。
- **网络连接**：技能依赖于稳定的网络连接，网络不稳定可能导致服务不可用或响应延迟。

