---
slug: manage-liquidity
name: manage-liquidity
version: "0.1.0"
displayName: Manage Liquidity
summary: Add liquidity, remove liquidity, or collect fees on Uniswap V2/V3/V4 pools.
  Handles the full flow...
license: MIT
description: |-
  Add liquidity, remove liquidity, or collect fees on Uniswap V2/V3/V4
  pools。Handles the full flow。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Uniswap Manage Liquidity

## Overview

This is the primary skill for all liquidity operations on Uniswap. It handles three distinct actions:

1. **Add liquidity** — Find the best pool, recommend a range, handle approvals, deposit tokens
2. **Remove liquidity** — Withdraw tokens from an existing position (partial or full)
3. **Collect fees** — Claim accumulated trading fees from a position

Each action delegates to the `liquidity-manager` agent for execution, with optional `pool-researcher` delegation for intelligent pool selection. This skill extracts the user's intent, validates parameters, and orchestrates the right agent workflow.

## When to Use

Activate when the user says anything related to providing, removing, or managing Uniswap liquidity:

**Adding liquidity:**

* "Add liquidity to ETH/USDC"
* "Provide LP for WETH/USDC on Base"
* "LP into the best pool for ETH/USDC"
* "Open a position in UNI/WETH"
* "I want to LP $5000 into ETH/USDC"
* "Deposit liquidity into the 0.05% pool"
* "Add $10K to my WETH/USDC position"

**Removing liquidity:**

* "Remove my liquidity"
* "Close my ETH/USDC position"
* "Withdraw 50% from position #12345"
* "Exit my LP position"

**Collecting fees:**

* "Collect my fees"
* "Claim accumulated fees from position #12345"
* "How much in fees have I earned?" (check first, then offer to collect)

## Parameters

### For Adding Liquidity

| Parameter | Required | Default | How to Extract |
| --- | --- | --- | --- |
| action | Yes | — | Always "add" for this sub-flow |
| token0 | Yes | — | First token: "ETH", "WETH", "USDC", or 0x address |
| token1 | Yes | — | Second token |
| amount | Yes | — | Dollar amount ("$5000"), token amount ("2.5 ETH"), or both |
| chain | No | ethereum | "ethereum", "base", "arbitrum", "optimism", "polygon" |
| version | No | v3 | "v2" (passive), "v3" (concentrated), "v4" (hooks) |
| range | No | medium | "narrow" (±5%), "medium" (±15%), "wide" (±50%), "full" (±∞) |
| feeTier | No | Auto-detect | "0.01%", "0.05%", "0.3%", "1%" or bps: 100, 500, 3000, 10000 |

### For Removing Liquidity / Collecting Fees

| Parameter | Required | Default | How to Extract |
| --- | --- | --- | --- |
| action | Yes | — | "remove" or "collect" |
| positionId | Yes* | — | NFT token ID ("position #12345") or found via search |
| chain | No | ethereum | Chain where the position exists |
| percentage | No | 100 | "50%", "all", "half" — only for remove |
| collectFees | No | true | Whether to also collect fees when removing |

*If the user doesn't provide a position ID (e.g., "remove my ETH/USDC position"), search for it using `get_positions_by_owner` and confirm with the user before proceeding.

## Workflow

### Add Liquidity Flow

```text
Step 1: PARSE INTENT
├── Extract: tokens, amount, chain, version, range, fee tier
├── Normalize: "ETH" → "WETH", "$5K" → "$5000"
└── If any required params missing → ASK the user (don't guess)

Step 2: POOL SELECTION (if user didn't specify exact pool)
├── If "best pool" or no fee tier specified:
│   └── Delegate to pool-researcher: "Find the best pool for {token0}/{token1} on {chain}"
│       Pool researcher returns ranked pools with APY, TVL, depth
│       Pick the recommended pool (or present top 3 if user wants to choose)
└── If specific pool given: use directly

Step 3: PRE-FLIGHT CHECKS
├── Check safety status via check_safety_status
├── Verify wallet has sufficient token balances
└── If checks fail → STOP and tell user what's wrong

Step 4: DELEGATE TO LIQUIDITY-MANAGER
├── Pass: token0, token1, amount, chain, version, range, feeTier, pool address
├── The liquidity-manager agent handles:
│   a. Check and execute token approvals (Permit2)
│   b. Calculate optimal tick range based on range strategy
│   c. Simulate the add-liquidity transaction
│   d. Route through safety-guardian for validation
│   e. Execute the transaction
│   f. Wait for confirmation
└── Returns: positionId, amounts deposited, tick range, tx hash

Step 5: PRESENT RESULT
├── Position ID (NFT token ID)
├── Tokens deposited with USD values
├── Price range (lower price, upper price, current price)
├── Estimated fee APY (from pool-researcher data)
├── Explorer link to the transaction
└── Tip: "Monitor with /track-performance"
```

### Remove Liquidity Flow

```text
Step 1: IDENTIFY POSITION
├── If position ID given → use directly
├── If "my ETH/USDC position" → call get_positions_by_owner
│   ├── Filter by token pair and chain
│   ├── If multiple matches → LIST them and ask user to choose
│   └── If no matches → tell user "No positions found for {pair}"
└── Confirm: "I found position #{id} — {pair} {feeTier} with {value}. Remove?"

Step 2: DELEGATE TO LIQUIDITY-MANAGER
├── Pass: positionId, chain, percentage (default 100%), collectFees
├── Agent handles: fee collection → partial/full removal → safety validation → execution
└── Returns: tokens received, fees collected, tx hash

Step 3: PRESENT RESULT
├── Tokens received with USD values
├── Fees collected (if any)
├── Total value received
├── Explorer link
└── If partial removal: remaining position details
```

### Collect Fees Flow

```text
Step 1: IDENTIFY POSITION (same as remove)

Step 2: CHECK UNCOLLECTED FEES
├── Call get_position to see tokensOwed0 and tokensOwed1
├── If fees are zero → "No fees to collect on this position"
└── Show fee amounts and ask to proceed

Step 3: DELEGATE TO LIQUIDITY-MANAGER
├── Pass: positionId, chain, action: "collect"
└── Returns: fees collected, tx hash

Step 4: PRESENT RESULT
├── Fees collected (token amounts + USD values)
├── Explorer link
└── Tip: "Your position is still active and earning more fees"
```

## Critical Decision Points

These are the moments where the skill must **stop and ask** rather than assume:

| Situation | Action |
| --- | --- |
| Multiple positions match | List all matches, ask user to pick one |
| Amount exceeds wallet balance | Show balance, ask if they want a smaller amount |
| Pool TVL < $10,000 | Warn about low liquidity risk, ask to confirm |
| Range strategy not specified | Default to "medium" but mention the tradeoffs |
| First time LPing | Briefly explain IL risk before proceeding |
| Remove > 50% of pool liquidity | Warn about price impact on exit |

## Output Format

### Successful Add

```text
Liquidity Added Successfully

  Position: #456789
  Pool:     WETH/USDC 0.05% (V3, Ethereum)

  Deposited:
    0.5 WETH  ($980)
    980 USDC  ($980)
    Total:    $1,960

  Range:
    Lower: $1,700 (tick -204714)
    Upper: $2,300 (tick -199514)
    Current: $1,963 — IN RANGE ✓
    Width: ±15% (medium)

  Expected Fee APY: ~15-21% (based on 7d pool data)

  Tx: https://etherscan.io/tx/0x...

  Next steps:
  - Monitor with: "How are my positions doing?"
  - Rebalance if out of range: "Rebalance position #456789"
  - Collect fees anytime: "Collect fees from position #456789"
```

### Successful Remove

```text
Liquidity Removed

  Position: #456789 (CLOSED)

  Received:
    0.52 WETH  ($1,020)
    950 USDC   ($950)
    Total:     $1,970

  Fees Collected:
    0.01 WETH  ($19.60)
    15.20 USDC ($15.20)
    Total fees: $34.80

  Net Result: +$44.80 (+2.3%) including fees

  Tx: https://etherscan.io/tx/0x...
```

## Important Notes

* **IL risk**: Always mention impermanent loss risk when adding liquidity to volatile pairs. Don't bury it.
* **Gas costs**: On Ethereum mainnet, LP operations cost $15-50 in gas. Mention this for small positions.
* **Range tradeoffs**: Narrow = higher fees but more rebalancing. Wide = lower fees but less maintenance. Always explain.
* **V2 vs V3**: V2 is "set and forget" with lower returns. V3 requires active management but earns more. Help the user choose.
* **Never auto-execute**: For remove and rebalance, always confirm with the user before executing.

## Error Handling

| Error | User-Facing Message | Suggested Action |
| --- | --- | --- |
| Wallet not configured | "No wallet configured for transactions." | Set WALLET_TYPE + PRIVATE_KEY in .env |
| Insufficient balance | "You have X but need Y to add liquidity." | Reduce amount or swap for needed tokens |
| Pool not found | "No pool found for X/Y at this fee tier." | Try different fee tier or check token names |
| Position not found | "Position #ID not found on this chain." | Check chain and position ID |
| Safety check failed | "Transaction blocked by safety: {reason}" | Adjust parameters or check safety config |
| Transaction reverted | "Transaction failed: {reason}" | Check slippage, amounts, or try again |
| liquidity-manager unavailable | "Liquidity agent is not available." | Check agent configuration |

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

This is the primary skill for all liquidity operations on Uniswap. It handles three distinct actions:

1. **Add liquidity** — Find the best pool, recommend a range, handle approvals, deposit tokens
2. **Remove liquidity** — Withdraw tokens from an existing position (partial or full)
3. **Collect fees** — Claim accumulated trading fees from a position

Each action delegates to the `liquidity-manager` agent for execution, with optional `pool-researcher` delegation for intelligent pool selection. This skill extracts the user's intent, validates parameters, and orchestrates the right agent workflow.

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Manage Liquidity？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Manage Liquidity有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
