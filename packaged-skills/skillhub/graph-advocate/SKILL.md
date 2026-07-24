---
slug: "graph-advocate"
name: "graph-advocate"
version: 2.9.2
displayName: "Graph Advocate"
summary: "把区块链数据问题路由到对的Graph Protocol服务,返实时数据。Route any blockchain data question to the right Graph Proto"
license: "MIT"
description: |-
  Route any blockchain data question to the right Graph Protocol service。Returns live data from 15。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - Integrations
  - 工具
  - 效率
  - 创意
  - 图像
  - polymarket
  - paid
  - api
  - hyperliquid
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# Graph Advocate

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

- Route any blockchain data question to the right Graph Protocol service
- Returns live data from 15
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 区块链数据查询 | 链上数据问题和子图类型 | Graph Protocol服务路由和建议 |
| 子图选择 | 数据需求和合约地址 | 最优子图索引和查询端点 |
| 查询优化 | GraphQL查询和子图模式 | 优化查询和性能建议 |

**不适用于**：非区块链数据的图数据库查询

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| question | string | 是 | 区块链数据查询问题 |
| chain | string | 否 | 区块链网络, 可选: ethereum/polygon/arbitrum, 默认: ethereum |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 工具依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

```text
"Top 10 USDC holders on Ethereum"           → token-api
"Best subgraph for Uniswap V3 on Arbitrum?" → subgraph-registry
"Aave V3 liquidations above $50K"           → graph-aave-mcp
"Hottest Polymarket markets"                → token-api (/v1/polymarket/markets)
"Polymarket OHLCV for Bitcoin market"       → token-api (/v1/polymarket/markets/ohlc)
"Polymarket trader P&L for 0x..."           → token-api (/v1/polymarket/users/positions)
"Polymarket live orderbook depth"           → graph-polymarket-mcp (advanced)
"Polymarket trader winrate/drawdown"        → graph-polymarket-mcp (subgraph P&L stats)
"Score Hyperliquid trader 0x..."            → /hyperliquid/score (paid)
"Hyperliquid top traders for HYPE"          → /hyperliquid/screen (paid)
"Evaluate Hyperliquid vault 0x..."          → /hyperliquid/vault (paid)
"Compare Aave vs Compound TVL"              → graph-lending-mcp
"x402 payment volume on Base today"         → x402-analytics
"Top 10 x402 recipients in the last 30 days" → /ask (paid, NL→SQL)
"When did x402 volume on Base inflect?"     → /ask (paid, NL→SQL)
"Has 0x0FF5A6… ever been paid via x402?"     → /onchain-x402/address (paid, decentralized)
"Polymarket vs Limitless spread on 'trump'"  → /predmarket/spread (paid, cross-venue JOIN)
"Kalshi vs Polymarket fed-rate arbitrage"    → /kalshi-polymarket/spread (paid)
"Find agents that do trading"               → 8004scan
```

## 常见问题

### Q1: 如何开始使用Graph Advocate？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
