---
slug: token-layer
name: token-layer
version: "1.0.3"
displayName: Token Layer
summary: Token Layer - Censorship resistant crosschain public token infrastructure.
  Launch once, trade eve...
license: MIT
description: |-
  Token Layer - Censorship resistant crosschain public token infrastructure。Launch once, trade eve。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Operations
tools:
  - - read
- exec
---
# Token Layer

## 核心能力

- Token Layer - Censorship resistant crosschain public token infrastructure
- Launch once, trade eve
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。


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

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
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

### Q2: 遇到错误怎么办？
A: 

### Q3: Token Layer有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
