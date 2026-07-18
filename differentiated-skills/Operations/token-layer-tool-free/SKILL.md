---
slug: token-layer-tool-free
name: token-layer-tool-free
version: "1.0.0"
displayName: 跨链代币入门工具
summary: 跨链代币数据查询工具，支持主流链代币信息与基础价格查询。
license: MIT
edition: free
description: |-
  面向个人加密货币用户的跨链代币数据查询工具。支持以太坊/BSC/
  Polygon等主流链上的代币信息查询，包括合约地址、价格、流动性
  等基础数据。适合个人用户进行跨链代币研究。

  核心能力:
  - 多链代币信息查询
  - 代币价格与流动性
  - 合约地址验证
  - 基础链上数据获取

  适用场景:
  - 个人跨链代币研究
  - 代币信息验证
  - 价格查询
  - 投资决策辅助

  差异化:
  - 免费版聚焦基础数据查询
  - 适合个人用户低频使用
  - 不支持批量查询与深度分析
  - 不支持实时监控与告警

  触发关键词: 跨链, 代币, 多链, 合约地址, 流动性, 价格, token, multi-chain, cross-chain
tags:
- Operations
- 加密货币
- 跨链
- 代币
tools:
- read
- exec
---

# 跨链代币入门工具（免费版）

## 概述

本工具为个人加密货币用户提供跨链代币数据查询能力。支持主流区块链上的代币信息查询，包括合约地址、价格、流动性等基础数据。适合个人用户进行跨链代币研究与投资决策辅助。

## 核心能力

### 查询功能

| 功能 | 说明 | 免费版支持 |
| --- | --- | --- |
| 代币信息 | 合约地址/精度/总量 | 支持 |
| 价格查询 | 实时价格 | 支持 |
| 流动性 | 流动性池规模 | 支持 |
| 多链支持 | 支持的区块链 | 主流5条链 |
| 批量查询 | 多代币并行 | 不支持 |
| 跨链桥 | 桥接信息 | 不支持 |
| 实时监控 | 价格告警 | 不支持 |
| 深度分析 | 链上行为 | 不支持 |

### 支持的区块链

| 链名称 | 代币数量 | 免费版支持 |
| --- | --- | --- |
| Ethereum | 10000+ | 支持 |
| BSC | 5000+ | 支持 |
| Polygon | 3000+ | 支持 |
| Arbitrum | 2000+ | 支持 |
| Optimism | 1500+ | 支持 |

## 使用场景

### 场景一：查询代币信息

用户输入："查一下USDC在不同链上的合约地址"

```bash
# 跨链代币查询
python3 scripts/token.py info \
  --symbol USDC \
  --chains "ethereum,bsc,polygon"

# 输出：
# === USDC 跨链信息 ===
# Ethereum:  0xA0b8...eB48 (精度:6)
# BSC:       0x8AC7...e14E (精度:18)
# Polygon:   0x2791...ca44 (精度:6)
```

### 场景二：价格查询

用户输入："查UNI在各链上的价格"

```bash
# 跨链价格查询
python3 scripts/token.py price \
  --symbol UNI \
  --chains "ethereum,arbitrum,optimism"

# 输出各链价格
```

### 场景三：流动性查询

用户输入："查UNI在以太坊上的流动性"

```bash
# 流动性查询
python3 scripts/token.py liquidity \
  --symbol UNI \
  --chain ethereum

# 输出流动性池信息
```

## 快速开始

### 环境准备

```bash
# 安装依赖
pip install requests web3

# 查询代币
python3 scripts/token.py info --symbol USDC --chains "ethereum,bsc"
```

### 常用命令

```bash
# 代币信息
python3 scripts/token.py info --symbol USDC --chains "ethereum,bsc,polygon"
python3 scripts/token.py info --address 0xA0b8...eB48 --chain ethereum

# 价格查询
python3 scripts/token.py price --symbol UNI --chains "ethereum,arbitrum"

# 流动性
python3 scripts/token.py liquidity --symbol UNI --chain ethereum

# 代币列表
python3 scripts/token.py list --chain ethereum --top 20

# 合约验证
python3 scripts/token.py verify --address 0x... --chain ethereum
```

## 配置示例

### 查询配置

```yaml
token_config:
  api:
    endpoints:
      ethereum: "https://api.etherscan.io"
      bsc: "https://api.bscscan.com"
      polygon: "https://api.polygonscan.com"
    api_keys:
      ethereum: "${ETHERSCAN_API_KEY}"
      bsc: "${BSCSCAN_API_KEY}"

  chains:
    supported: ["ethereum", "bsc", "polygon", "arbitrum", "optimism"]
    default: ethereum

  cache:
    ttl: 60
    storage: "./cache/"

  rpc:
    ethereum: "https://mainnet.infura.io/v3/${INFURA_KEY}"
    bsc: "https://bsc-dataseed.binance.org"
```

## 最佳实践

1. **合约验证**：投资前务必验证合约地址的真实性
2. **多链对比**：同一代币在不同链上可能有不同合约
3. **流动性关注**：低流动性代币交易滑点大
4. **数据时效**：链上数据实时变化，查询结果仅供参考

| 实践要点 | 说明 |
| --- | --- |
| 合约安全 | 仅信任官方公布的合约地址 |
| 精度差异 | 同一代币在不同链上精度可能不同 |
| 桥接风险 | 跨链桥接存在安全风险，了解后再使用 |
| 免责声明 | 数据仅供参考，不构成投资建议 |

## 常见问题

### Q1：免费版支持多少条链？

免费版支持以太坊、BSC、Polygon、Arbitrum和Optimism五条主流链。如需更多链支持，建议升级PRO版。

### Q2：数据来源是什么？

代币数据来自各链的区块浏览器API（如Etherscan）和去中心化数据源（如CoinGecko）。价格数据可能有延迟。

### Q3：支持跨链桥接查询吗？

免费版不包含跨链桥接信息查询。如需查询跨链桥接路径与费用，建议升级PRO版。

### Q4：可以监控代币价格变化吗？

免费版仅支持即时查询，不支持价格监控。如需实时价格告警，建议升级PRO版。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| requests | Python库 | 必需 | `pip install requests` |
| web3 | Python库 | 可选 | `pip install web3`（链上查询） |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| Etherscan | `ETHERSCAN_API_KEY` | 推荐 | 以太坊数据查询 |
| BSCScan | `BSCSCAN_API_KEY` | 推荐 | BSC数据查询 |
| Infura | `INFURA_KEY` | 可选 | RPC节点访问 |

- 未配置API Key时使用免费公共接口，频率较低
- 所有Key存储在本地环境变量

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 通过区块浏览器API和RPC查询跨链代币数据
- **免费版限制**: 5条链、基础查询、不支持批量与监控
