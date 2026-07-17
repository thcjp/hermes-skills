---
slug: test
name: test
version: "0.0.1"
displayName: Test
summary: CLI for crypto portfolio tracking, market data, and CEX history. Use when
  the user asks about cry...
license: MIT
description: |-
  CLI for crypto portfolio tracking, market data, and CEX history. Use
  when the user asks about cry...

  核心能力:

  - 金融工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 交易分析、投资决策、财务计算

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: portfolio, tracking, data, crypto, market, test
tags:
- Finance
tools:
- read
- exec
---

# Test

CLI for crypto portfolio tracking, market data, and CEX history.

## Invocation

```text
onchain <command>
```

## Commands

### Market Data

```bash
onchain price <token>         # Token price (btc, eth, sol, etc.)
onchain markets               # Market overview with trending
```

### Wallet Data

```bash
onchain balance [address]           # Token balances (auto-detects EVM/Solana)
onchain balance --chain polygon     # Filter by chain
onchain history [address]           # Transaction history
onchain portfolio [address]         # Full portfolio with DeFi positions
```

### CEX Data

```bash
onchain coinbase balance      # Coinbase balances
onchain coinbase history      # Coinbase trade history
onchain binance balance       # Binance balances
onchain binance history       # Binance trade history
```

### Prediction Markets

```bash
onchain polymarket trending          # Trending markets
onchain polymarket search <query>    # Search markets
onchain polymarket view <slug>       # View market details
```

### Configuration

```bash
onchain setup                 # Interactive setup wizard
onchain config                # View current config
onchain config wallet add <name> <address>
onchain config wallet set-default <name>
```

## Global Options

* `--json` - Output as JSON (agent-friendly)
* `--plain` - Disable colors and emoji
* `--timeout <ms>` - Request timeout

## Configuration

Config file: `~/.config/onchain/config.json5`

### Required API Keys

| Feature | API Key | Get Key |
| --- | --- | --- |
| EVM wallets | `DEBANK_API_KEY` | [DeBank](https://cloud.debank.com/) |
| Solana wallets | `HELIUS_API_KEY` | [Helius](https://helius.xyz/) |
| Coinbase CEX | `COINBASE_API_KEY` + `COINBASE_API_SECRET` | [Coinbase](https://www.coinbase.com/settings/api) |
| Binance CEX | `BINANCE_API_KEY` + `BINANCE_API_SECRET` | [Binance](https://www.binance.com/en/my/settings/api-management) |

### Optional API Keys

| Feature | API Key | Notes |
| --- | --- | --- |
| Market data | `COINGECKO_API_KEY` | Free tier works, Pro for higher limits |
| Market fallback | `COINMARKETCAP_API_KEY` | Alternative market data source |

## Examples

### Get Bitcoin price

```bash
onchain price btc
```

### Check wallet balance

```bash
onchain balance 0x1234...5678
```

### View portfolio with DeFi positions

```bash
onchain portfolio main  # Uses saved wallet named "main"
```

### Get trending prediction markets

```bash
onchain polymarket trending -n 5
```

### JSON output for scripts

```bash
onchain --json price eth | jq '.priceUsd'
```

## Supported Chains

### EVM (via DeBank)

Ethereum, BNB Chain, Polygon, Arbitrum, Optimism, Avalanche, Base, zkSync Era, Linea, Scroll, Blast, Mantle, Gnosis, Fantom, Celo, and more.

### Solana (via Helius)

Full Solana mainnet support including SPL tokens and NFTs.

## Agent Integration

This CLI is designed for agent use. Key patterns:

1. **Always use `--json`** for programmatic access
2. **Check exit codes** - 0 for success, 1 for error
3. **Use saved wallets** - Configure once with `onchain setup`, reference by name
4. **Rate limiting** - APIs have rate limits, add delays between rapid calls

### Example Agent Usage

```bash
VALUE=$(onchain --json portfolio main | jq -r '.totalValueUsd')

onchain --json price btc | jq '{price: .priceUsd, change24h: .priceChange24h}'

CHANGE=$(onchain --json markets | jq '.marketCapChange24h')
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
