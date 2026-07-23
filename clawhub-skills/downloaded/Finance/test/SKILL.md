---
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
summary: "加密组合跟踪/市场数据/CEX历史CLI"
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

## 示例

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

- CLI for crypto portfolio tracking, market data, and CEX history
- Use
  when the user asks about cry
- 触发关键词: portfolio, tracking, data, crypto, market, test

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

### Q1: 如何开始使用Test？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Test有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
