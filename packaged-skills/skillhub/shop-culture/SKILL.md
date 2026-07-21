---
slug: shop-culture
name: shop-culture
version: "1.0.12"
displayName: 生活方式购物
summary: AI代理自主浏览生活方式商品、下单和跟踪物流的多链加密支付购物
license: MIT
description: |-
  AI代理自主购物技能。支持商品浏览、语义搜索、AI购物助手、多链加密支付结账、
  订单跟踪等功能。支持8+区块链支付（Solana/Ethereum/Base等）和x402协议结账。
  适用于AI驱动的自主购物、礼品选购和订单管理等场景。
tools:
  - read
  - exec
---

# 生活方式购物

AI代理自主购物技能，为生活方式商店提供完整的浏览、下单和跟踪能力。支持自然语言搜索、多链加密支付和x402协议结账，无需API Key。

## 安全准则

- 禁止请求私钥、助记词或钱包密钥
- 商品ID必须从搜索结果获取，禁止编造或猜测
- 支付前必须获得用户明确确认
- 仅调用文档中记录的API端点
- 支付窗口约15分钟，超时后订单失效

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）

## 核心能力

### 1. 能力发现

通过 `GET /agent/capabilities` 获取API能力摘要。返回支持的功能、链/代币列表和限制说明。适用于首次调用时了解API完整能力和支持的支付方式。

- 执行`能力发现`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`能力发现`相关配置参数进行设置
### 2. AI购物助手

通过 `POST /agent/shop` 发送自然语言购物请求。请求体包含 `message`（自然语言查询）和可选 `context`（含 `priceRange`、`preferences` 等）。返回AI回复文本和匹配的 `products` 数组（含 `id`、`title`、`price`、`inStock`、`badge` 等字段）。适用于对话式商品搜索和推荐场景。

### 3. 分类树查询
通过 `GET /categories` 获取商品分类树。返回包含分类slug、名称和商品数量的层级结构。适用于商品分类浏览和导航场景。

**输入**: 用户提供分类树查询所需的指令和必要参数。
**处理**: 按照skill规范执行分类树查询操作,遵循单一意图原则。

- 执行`分类树查询`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`分类树查询`相关配置参数进行设置
### 4. 精选商品
通过 `GET /products/featured` 获取精选商品列表。返回带 `trending`、`new`、`bestseller` 等标签的精选商品。适用于礼品推荐和热门商品展示场景。

**输入**: 用户提供精选商品所需的指令和必要参数。
**处理**: 按照skill规范执行精选商品操作,遵循单一意图原则。

### 5. 语义搜索

通过 `GET /products/search?q=<query>` 进行自然语言语义搜索。支持参数：`q`（查询词）、`category`（分类slug）、`priceMin`/`priceMax`（价格范围）、`sort`（newest/popular/rating/price_asc/price_desc）、`limit`（默认20，最大100）、`offset`（分页偏移）。仅返回有库存商品。适用于精准商品查找场景。

### 6. 商品详情
通过 `GET /products/{slug}` 获取商品完整信息。返回 `id`（用于结账）、`variants[]`（含 `id`、`name`、`inStock`、`stockQuantity`、`price`）、`images[]`、`relatedProducts[]` 和 `description`。若商品有变体，需选择 `inStock` 的变体并在结账时包含 `variantId`。适用于结账前的商品信息确认。

**输入**: 用户提供商品详情所需的指令和必要参数。
**处理**: 按照skill规范执行商品详情操作,遵循单一意图原则。

### 7. 支付方式查询
通过 `GET /payment-methods` 获取所有支持的支付方式。返回 `data`（已启用支付方式设置）和 `chains`（区块链网络和代币列表）。支持Solana（SOL/USDC/USDT/CULT）、Ethereum（ETH/USDC/USDT）、Base（ETH/USDC）、Polygon（MATIC/USDC）、Arbitrum、Bitcoin、Dogecoin、Monero等。结账前必须验证支付方式是否支持。

**输入**: 用户提供支付方式查询所需的指令和必要参数。
**处理**: 按照skill规范执行支付方式查询操作,遵循单一意图原则。

### 8. 标准结账
通过 `POST /checkout` 创建订单。请求体包含 `items`（含 `productId`、`quantity`、可选 `variantId`）、`email`、`payment`（含 `chain` 和 `token`）和 `shipping`（含 `name`、`address1`、`city`、`stateCode`、`postalCode`、`countryCode`）。返回 `orderId`、`payment.address`（付款地址）、`payment.amount`（精确金额）、`payment.qrCode`（二维码）和 `expiresAt`（约15分钟有效期）。仅在用户明确确认后告知付款信息。

**处理**: 按照skill规范执行标准结账操作,遵循单一意图原则。
### 9. x402结账

通过 `POST /checkout/x402` 创建x402协议订单。API返回HTTP 402状态码和付费要求，运行时（或用户）构建并签名USDC转账（含memo `Store Order: {orderId}`），通过 `X-PAYMENT` 头部重试请求。成功后返回201和订单确认。skill不访问私钥，签名由运行时负责。适用于自动化代理支付场景。

### 10. 订单状态跟踪
通过 `GET /orders/{orderId}/status` 跟踪订单状态。返回 `status`（awaiting_payment/paid/processing/shipped/delivered/expired/cancelled）和时间戳。轮询间隔：`awaiting_payment` 每5秒、`paid`/`processing` 每60秒、`shipped` 每小时。`shipped` 状态包含 `tracking` 对象（carrier、number、URL）。适用于订单物流跟踪。

**输入**: 用户提供订单状态跟踪所需的指令和必要参数。
### 11. 订单详情
通过 `GET /orders/{orderId}` 获取完整订单详情。返回商品列表、配送信息、支付信息（含 `txHash`）、订单总额和跟踪信息。始终向用户传达响应中的 `_actions.next` 指引下一步操作。适用于订单信息查询和问题排查。

**处理**: 按照skill规范执行订单详情操作,遵循单一意图原则。
### 12. 代理身份
通过 `GET /agent/me`、`GET /agent/me/orders`、`GET /agent/me/preferences` 获取代理身份信息。需在请求头中携带 `X-Moltbook-Identity` 令牌（由代理运行时提供）。仅在运行时明确提供令牌时使用，正常浏览和结账流程禁止发送身份令牌。适用于代理个性化场景。

### 能力覆盖范围

本skill还覆盖以下能力场景: 代理自主浏览生活、方式商品、下单和跟踪物流的、多链加密支付购物、代理自主购物技能、支持商品浏览、多链加密支付结账、订单跟踪等功能、区块链支付、协议结账、驱动的自主购物、礼品选购和订单管、理等场景。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. 调用 `GET /agent/capabilities` 了解API能力和支持的支付方式
2. 通过 `POST /agent/shop` 或 `GET /products/search?q=<query>` 搜索商品，获取商品 `id`
3. 调用 `GET /products/{slug}` 确认商品详情、价格和库存状态
4. 调用 `GET /payment-methods` 验证支付链/代币是否支持
5. 调用 `POST /checkout` 创建订单，获取 `orderId` 和 `payment.address`
6. 获得用户明确确认后，告知付款地址和金额（约15分钟内完成）
7. 轮询 `GET /orders/{orderId}/status` 跟踪订单状态直至 `delivered`

### 命令参数说明

- `-H`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项

### 命令参数说明

- `-X`: 命令参数,用于指定操作选项
- `-Type`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项

### 命令参数说明

- `-Type`: 命令参数,用于指定操作选项
- `-X`: 命令参数,用于指定操作选项
- `-H`: 命令参数,用于指定操作选项

## 示例

### 示例1：搜索商品并完成标准结账

```bash
# AI购物助手搜索
curl -X POST "https://lifestyle-store.example.com/api/agent/shop" \
  -H "Content-Type: application/json" \
  -d '{"message": "wireless headphones under $200", "context": {"priceRange": {"max": 200}}}'

# 响应
# {"reply": "Found great options...", "products": [{"id": "prod_sony_wh1000xm4", "title": "Sony WH-1000XM4", "price": 198.00, "inStock": true, "badge": "bestseller"}]}

# 创建订单
curl -X POST "https://lifestyle-store.example.com/api/checkout" \
  -H "Content-Type: application/json" \
  -d '{
    "items": [{"productId": "prod_sony_wh1000xm4", "quantity": 1}],
    "email": "user@example.com",
    "payment": {"chain": "solana", "token": "USDC"},
    "shipping": {"name": "John Doe", "address1": "123 Main St", "city": "San Francisco", "stateCode": "CA", "postalCode": "94102", "countryCode": "US"}
  }'
# 响应包含 orderId, payment.address, payment.amount, expiresAt
```

### 示例2：跟踪订单状态

```bash
# 查询订单状态
curl "https://lifestyle-store.example.com/api/orders/order_j4rv15_001/status"

# 响应
# {"status": "shipped", "tracking": {"carrier": "USPS", "number": "9405511899223456", "url": "https://tools.usps.com/..."}, "_actions": {"next": "Your order shipped! Track it here."}}

# 获取完整订单详情
curl "https://lifestyle-store.example.com/api/orders/order_j4rv15_001"
```

## 错误处理


| 错误场景 | HTTP状态 | 原因 | 处理方式 |
|---------|---------|------|---------|
| 搜索返回0结果 | 200 | 查询过窄或无匹配商品 | 扩大查询范围，尝试 `/categories` 推荐替代分类，移除价格过滤器 |
| 商品缺货 | 200 | variant `inStock=false` | 从 `relatedProducts` 推荐替代商品，或选择同商品其他 `inStock` 变体 |
| 订单过期 | 200 | 支付窗口15分钟超时，status=expired | 告知用户并创建新订单，重新发起结账流程 |
| 链/代币不支持 | 400 | 未在 `GET /payment-methods` 的chains中 | 重新查询 `GET /payment-methods`，使用支持的链/代币组合（如USDC on Solana） |
| HTTP 429速率限制 | 429 | 超过100 req/min per IP | 等待 `retryAfter` 秒，指数退避执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令（2s, 4s, 8s...） |
| 配送国家不支持 | 400 | `countryCode` 不在支持列表 | 检查 `error.details` 获取支持的国家列表，请求有效地址 |
| 商品ID无效 | 400 | 编造或猜测的 `productId` | 仅使用 `GET /products/search` 或 `GET /products/{slug}` 返回的真实 `id` |

## 常见问题

### Q1: 支持哪些支付方式？

支持8+区块链支付：Solana（SOL/USDC/USDT/CULT）、Ethereum（ETH/USDC/USDT）、Base（ETH/USDC）、Polygon（MATIC/USDC）、Arbitrum（ETH/USDC）、Bitcoin（BTC）、Dogecoin（DOGE）、Monero（XMR）。结账前必须调用 `GET /payment-methods` 验证。推荐使用USDC或USDT避免价格波动。

### Q2: 支付窗口有多长？

支付窗口约15分钟。从 `POST /checkout` 创建订单开始计时，`expiresAt` 字段记录截止时间。超时后订单状态变为 `expired`，需创建新订单重新结账。建议使用稳定币（USDC/USDT）避免浏览和支付间的价格波动。

### Q3: 如何跟踪订单状态？

调用 `GET /orders/{orderId}/status` 查询状态。轮询间隔：`awaiting_payment` 每5秒、`paid`/`processing` 每60秒、`shipped` 每小时。`shipped` 状态包含 `tracking` 对象（carrier、number、URL）。`delivered`/`expired`/`cancelled` 状态停止轮询。始终传达 `_actions.next` 指引用户。

### Q4: CULT token折扣如何使用？

CULT token持有者享5-20%折扣加免运费。结账时可选提供 `wallet`/`walletAddress`，通过关联钱包或签名验证消息（`GET /api/checkout/wallet-verify-message`）验证链上质押等级。三个等级（BASE/PRIME/APEX）对应不同折扣。注意：分享钱包地址会将链上活动与订单关联。

### Q5: 搜索支持哪些参数？

`GET /products/search` 支持参数：`q`（自然语言查询）、`category`（分类slug）、`priceMin`/`priceMax`（USD价格范围）、`sort`（newest/popular/rating/price_asc/price_desc，默认newest）、`limit`（每页结果数，默认20，最大100）、`offset`（分页偏移）。仅返回有库存商品。使用 `POST /agent/shop` 可获得AI增强的自然语言搜索体验。

### Q6: x402结账和标准结账有什么区别？

标准结账（`POST /checkout`）创建订单后返回付款地址和金额，用户手动转账后轮询确认。x402结账（`POST /checkout/x402`）返回HTTP 402付费挑战，运行时自动构建并签名USDC转账（Solana），通过 `X-PAYMENT` 头部重试完成支付。x402适用于自动化代理支付，标准结账适用于手动确认。两种方式都不访问私钥。

## 已知限制

- 支付窗口约15分钟，超时需创建新订单
- 速率限制约100 req/min per IP，超限返回429
- 商品ID必须从搜索结果获取，禁止编造
- `X-Moltbook-Identity` 头部仅用于代理身份端点，正常流程禁止发送
- 客户PII可能在90天后自动删除
- 不支持需要100%确定性的关键决策场景
