---
slug: "token-layer"
name: "token-layer"
version: 1.0.4
displayName: "Token Layer"
summary: "抗审查跨链公共代币基础设施,一次发行处处交易"
license: "Proprietary"
description: |-
  Token Layer - Censorship resistant crosschain public token infrastructure。Launch once, trade eve
tags:
  - Operations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
category: "Automation"
---
# Token Layer

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

- Token Layer - Censorship resistant crosschain public token infrastructure
- Launch once, trade eve
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 质量审查 | 代码文件与检查规则 | 审查报告与评级 |
| 抗审查跨链公共代币基 | 目标数据与配置参数 | 处理结果与执行状态 |
| 一次发行处处交易 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | token-layer处理的内容输入 |,  |
| content | string | 否 | token-layer处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "layer 相关配置参数",
    result: "layer 相关配置参数",
    result: "layer 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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

### Check Wallet

```bash
curl -s -X GET "https://api.tokenlayer.network/functions/v1/me" \
  -H "Authorization: Bearer $TOKENLAYER_API_KEY" | jq
```

### Enter Referral

```bash
curl -s -X POST "https://api.tokenlayer.network/functions/v1/enter-referral-code" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKENLAYER_API_KEY" \
  -d '{"referral_code": "YOUR_CODE"}' | jq
```

### Create Token

Image can be URL or base64 data URI:

```bash
curl -s -X POST "https://api.tokenlayer.network/functions/v1/create-token-transaction" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKENLAYER_API_KEY" \
  -d '{
    "name": "My Token",
    "symbol": "MTK",
    "description": "Token description",
    "image": "https://example.com/logo.png",
    "chainSlug": "base",
    "tags": ["ai", "agent"],
    "amountIn": 10
  }' | jq
```

With base64 image:

```bash
"image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAY..."
```

### Quote Token (Get Price Before Trading)

```bash
curl -s -X POST "https://api.tokenlayer.network/functions/v1/quote-token" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKENLAYER_API_KEY" \
  -d '{
    "tokenId": "UUID-FROM-GET-TOKENS",
    "chainSlug": "base",
    "amount": 10,
    "direction": "buy",
    "inputToken": "usdc"
  }' | jq
```

### Buy Token

```bash
curl -s -X POST "https://api.tokenlayer.network/functions/v1/trade-token" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKENLAYER_API_KEY" \
  -d '{
    "tokenId": "UUID-FROM-GET-TOKENS",
    "chainSlug": "base",
    "direction": "buy",
    "buyAmountUSD": 10
  }' | jq
```

### Sell Token

```bash
curl -s -X POST "https://api.tokenlayer.network/functions/v1/trade-token" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKENLAYER_API_KEY" \
  -d '{
    "tokenId": "UUID-FROM-GET-TOKENS",
    "chainSlug": "base",
    "direction": "sell",
    "sellAmountToken": 500000
  }' | jq
```

### Send Transaction

```bash
curl -s -X POST "https://api.tokenlayer.network/functions/v1/send-transaction" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKENLAYER_API_KEY" \
  -d '{
    "to": "0x...",
    "amount": "0",
    "data": "0x...",
    "chainSlug": "base"
  }' | jq
```

### Get Trending Tokens

```bash
curl -s -X POST "https://api.tokenlayer.network/functions/v1/get-tokens-v2" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKENLAYER_API_KEY" \
  -d '{
    "order_by": "volume_1h",
    "order_direction": "DESC",
    "limit": 10
  }' | jq
```

### Filter by Chain

```bash
curl -s -X POST "https://api.tokenlayer.network/functions/v1/get-tokens-v2" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKENLAYER_API_KEY" \
  -d '{
    "chains": ["solana", "base"],
    "order_by": "market_cap",
    "order_direction": "DESC",
    "limit": 10
  }' | jq
```

## 常见问题

### Q1: 如何开始使用Token Layer？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

