---
slug: liquidity-mgr-tool-free
name: liquidity-mgr-tool-free
version: "1.0.0"
displayName: 流动性管理工具
summary: 面向个人用户的 Uniswap V2/V3/V4 流动性查询与基础管理工具。
license: MIT
edition: free
description: |-
  面向个人用户的去中心化交易所流动性管理工具。

  核心能力:
  - V2/V3/V4 池子与头寸查询
  - 单头寸添加与移除流动性
  - 价格区间与费率查询
  - 收益与无常损失基础估算

  适用场景:
  - 个人查看 LP 头寸与收益
  - 单池子添加/移除流动性
  - V3/V4 区间与费率选择

  差异化: 免费版聚焦个人单头寸查询与管理，提供基础收益估算，零成本使用。

  触发关键词: 流动性, uniswap, v2, v3, v4, lp, 头寸, 添加流动性, 无常损失, liquidity
tags:
- DeFi
- 流动性
- 个人效率
- 其他工具
tools:
- read
- exec
---

# 流动性管理工具（免费版）

## 概述

本工具帮助个人用户管理 Uniswap V2/V3/V4 流动性，覆盖池子与头寸查询、单头寸添加/移除、价格区间与费率查询、收益与无常损失基础估算。适合个人单头寸管理。

## 核心能力

| 能力 | 说明 | 免费版范围 |
|:-----|:-----|:-----------|
| 池子查询 | V2/V3/V4 池子信息 | 只读 |
| 头寸管理 | 查询/添加/移除 | 单头寸 |
| 区间费率 | V3/V4 区间与费率 | 查询 |
| 收益估算 | 费用收益与无常损失 | 基础 |

## 使用场景

### 场景一：查询头寸

```bash
# 查询我的 V3 头寸
{baseDir}/scripts/liq.sh positions --version v3 --address 0xYOUR

# 查询池子信息
{baseDir}/scripts/liq.sh pool --version v3 --pool 0xPOOL
```

### 场景二：添加流动性

```bash
# V3 集中流动性
{baseDir}/scripts/liq.sh add \
  --version v3 \
  --token0 WETH \
  --token1 USDC \
  --fee 3000 \
  --lower 1800 \
  --upper 2200 \
  --amount0 1 \
  --amount1 2000
```

### 场景三：收益估算

```python
# 无常损失基础估算
initial_ratio = 0.5  # 初始 50/50
new_ratio = 0.6      # 价格变动后
# IL = 2*sqrt(r/(1-r)) - 1 近似
import math
il = 2 * math.sqrt(new_ratio / (1-new_ratio)) - 1
print(f"无常损失近似: {il:.2%}")
```

## 快速开始

1. 配置钱包与 RPC。
2. 查询现有头寸与池子。
3. 选择区间与费率添加流动性。
4. 定期查看收益与区间。

## 配置示例

V2/V3/V4 费率对照：

| 版本 | 支持费率 |
|:-----|:---------|
| V2 | 0.3%（固定） |
| V3 | 0.01% / 0.05% / 0.3% / 1% |
| V4 | 自定义（Hook 可调） |

## 最佳实践

- **区间别太窄**：V3 区间过窄易被套利踢出，赚不到手续费。
- **费率按波动选**：稳定币对 0.05%，主流对 0.3%，长尾 1%。
- **无常损失要算**：价格剧烈波动时无常损失可能吃掉手续费。
- **定期再平衡**：V3 区间偏离需再平衡，免费版手动操作。
- **小额定投试**：新池先小额试，熟悉再放量。

## 常见问题

**Q1：V2 和 V3 怎么选？**
A：被动持有选 V2，主动管理选 V3 集中流动性收益更高。

**Q2：免费版能批量管理吗？**
A：不能。批量头寸与自动再平衡为专业版能力。

**Q3：无常损失能避免吗？**
A：不能完全避免，区间越窄越易触发，稳定币对损失较小。

**Q4：V4 的 Hook 是什么？**
A：V4 通过 Hook 自定义池子逻辑（动态费率、限价单等）。

**Q5：移除流动性要 gas 吗？**
A：要。所有链上操作都需 gas，建议低 gas 时段操作。

## 进阶用法

### V3 区间选择策略

```text
区间选择原则:
  全范围:   收益低但永不踢出，适合被动持有
  宽区间:   ±30% 价格范围，平衡收益与稳定
  窄区间:   ±10% 价格范围，收益高但易被踢出

选择依据:
  - 高波动对: 选宽区间，避免频繁再平衡
  - 稳定币对: 选窄区间，收益最大化
  - 看不懂走势: 选全范围，被动持有
```

### 无常损失详解

```python
# 无常损失精确计算
import math

def impermanent_loss(price_ratio):
    """price_ratio = 新价格/旧价格"""
    r = price_ratio
    il = 2 * math.sqrt(r) / (1 + r) - 1
    return il

# 价格涨 2 倍
print(f"IL: {impermanent_loss(2):.2%}")   # IL: -5.72%
# 价格涨 4 倍
print(f"IL: {impermanent_loss(4):.2%}")   # IL: -20.00%
```

```text
关键结论:
  - 价格变动越大，无常损失越大
  - 无常损失是「相对持有可能」，不是绝对亏损
  - 手续费收入需覆盖无常损失才盈利
```

### 头寸监控

```bash
# 查询头寸详情
{baseDir}/scripts/liq.sh position --id 12345

# 查看收益
{baseDir}/scripts/liq.sh earnings --id 12345

# 检查区间偏离
{baseDir}/scripts/liq.sh deviation --id 12345
```

## V2/V3/V4 对比

| 特性 | V2 | V3 | V4 |
|:-----|:---|:---|:---|
| 流动性 | 均匀分布 | 集中区间 | 集中+Hook |
| 费率 | 固定 0.3% | 多档可选 | 自定义 |
| 再平衡 | 不需要 | 手动 | 可自动 |
| 复杂度 | 低 | 中 | 高 |
| 适合 | 被动持有 | 主动管理 | 高级策略 |

## 风险提示

- **无常损失**：价格剧烈波动时无常损失可能吃掉手续费。
- **区间被踢**：V3 窄区间价格超出即停止赚手续费。
- **智能合约风险**：协议漏洞可能导致资金损失。
- **gas 成本**：频繁操作消耗 gas，需计入成本。
- **价格风险**：代币本身价格下跌是最大风险。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 可访问以太坊/L2 RPC

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | nodejs.org |
| ethers.js | 链交互 | 必需 | `npm install ethers` |
| EVM 钱包 | 签名 | 必需 | MetaMask 等 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- `RPC_URL`：以太坊/L2 节点 RPC 地址（Alchemy/Infura 等）
- 钱包私钥仅本地签名，不上传
- 建议私钥存环境变量或权限 0600 配置文件

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 调用合约管理流动性
