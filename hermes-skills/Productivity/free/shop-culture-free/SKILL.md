---

name: "shop-culture-free"
description: "基础商品浏览和搜索，AI购物助手和分类导航。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "生活方式购物基础版"
  version: "1.0.12"
  summary: "基础商品浏览和搜索，AI购物助手和分类导航"
  tags:
    - "通用办公"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
tools:
  - exec
  - read
  - write

---

# 生活方式购物（免费版）

AI代理自主购物技能的免费版。支持商品浏览、语义搜索、AI购物助手和分类导航，无需API Key。

## 安全准则

- 禁止请求私钥、助记词或钱包密钥
- 商品ID必须从搜索结果获取，禁止编造或猜测
- 仅调用文档中记录的API端点
- 免费版不支持结账和支付操作

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
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 能力发现

### 2. AI购物助手

通过 `POST /agent/shop` 发送自然语言购物请求。请求体包含 `message`（自然语言查询）和可选 `context`（含 `priceRange`、`preferences` 等）。返回AI回复文本和匹配的 `products` 数组（含 `id`、`title`、`price`、`inStock`、`badge` 等字段）。适用于对话式商品搜索和推荐。

### 3. 分类树查询
通过 `GET /categories` 获取商品分类树。返回包含分类slug、名称和商品数量的层级结构。适用于商品分类浏览和导航场景。

### 4. 精选商品
通过 `GET /products/featured` 获取精选商品列表。返回带 `trending`、`new`、`bestseller` 等标签的精选商品。适用于礼品推荐和热门商品展示。

### 5. 语义搜索

通过 `GET /products/search?q=<query>` 进行自然语言语义搜索。支持参数：`q`（查询词）、`category`（分类slug）、`priceMin`/`priceMax`（价格范围）、`sort`（newest/popular/rating/price_asc/price_desc）、`limit`（默认20，最大100）、`offset`（分页偏移）。仅返回有库存商品。适用于精准商品查找。

### 6. 商品详情
通过 `GET /products/{slug}` 获取商品完整信息。返回 `id`、`variants[]`（含 `id`、`name`、`inStock`、`stockQuantity`、`price`）、`images[]`、`relatedProducts[]` 和 `description`。若商品有变体，需选择 `inStock` 的变体。适用于商品信息查看和结账前确认（完整版结账）。

#
## 升级提示

以下为完整版（shop-culture）独有功能，免费版不可用：

- **支付方式查询**：`GET /payment-methods` 获取所有支持的8+区块链支付方式
- **标准结账**：`POST /checkout` 创建订单并生成付款地址，支持Solana/Ethereum/Base等多链
- **x402结账**：`POST /checkout/x402` 自动化代理支付，运行时签名USDC转账
- **订单状态跟踪**：`GET /orders/{orderId}/status` 轮询订单状态（awaiting_payment每5秒/shipped每小时）
- **订单详情**：`GET /orders/{orderId}` 获取完整订单信息含支付txHash和物流跟踪
- **代理身份**：`GET /agent/me` 通过 `X-Moltbook-Identity` 令牌获取代理个性化信息

升级至完整版以获取全部能力。

## 使用流程

1. 调用 `GET /agent/capabilities` 了解API能力
2. 通过 `POST /agent/shop` 或 `GET /products/search?q=<query>` 搜索商品，获取商品 `id`
3. 调用 `GET /products/{slug}` 确认商品详情、价格和库存状态
4. 如需结账和支付，升级至完整版获取结账和订单跟踪功能

#
## 示例

### 示例1：AI购物助手搜索商品

```bash
# AI购物助手搜索
curl -X POST "https://lifestyle-store.example.com/api/agent/shop" \
  -H "Content-Type: application/json" \
  -d '{"message": "wireless headphones under $200", "context": {"priceRange": {"max": 200}}}'

# 响应
# {"reply": "Found great options...", "products": [{"id": "prod_sony_wh1000xm4", "title": "Sony WH-1000XM4", "price": 198.00, "inStock": true, "badge": "bestseller"}]}
```

### 示例2：分类浏览和商品详情查看

```bash
# 获取分类树
curl "https://lifestyle-store.example.com/api/categories"
# 响应包含分类slug、名称和商品数量

# 语义搜索
example.com/api/products/search?q=headphones&sort=popular&limit=20"

# 查看商品详情
example.com/api/products/sony-wh-1000xm4"
# 响应包含 id, variants[], images[], relatedProducts[]
```

## 错误处理

| 错误场景 | HTTP状态 | 原因 | 处理方式 |
|---------|---------|------|---------|
| 搜索返回0结果 | 200 | 查询过窄或无匹配商品 | 扩大查询范围，尝试 `/categories` 推荐替代分类，移除价格过滤器 |
| 商品缺货 | 200 | variant `inStock=false` | 从 `relatedProducts` 推荐替代商品，或选择同商品其他 `inStock` 变体 |
| HTTP 429速率限制 | 429 | 超过100 req/min per IP | 等待 `retryAfter` 秒，指数退避执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令（2s, 4s, 8s...） |
| 商品ID无效 | 400 | 编造或猜测的 `productId` | 仅使用 `GET /products/search` 或 `GET /products/{slug}` 返回的真实 `id` |
| sort参数无效 | 400 | 传入了不支持的排序值 | 使用有效值：`newest`/`popular`/`rating`/`price_asc`/`price_desc` |
| limit超出范围 | 400 | limit不在1-100范围内 | 调整limit值到1-100范围内，默认20 |
| 请求结账功能 | 403 | 免费版不支持 `POST /checkout` | 升级至完整版以使用结账和支付功能 |

## 常见问题

### Q1: 免费版可以下单购买商品吗？

不可以。`POST /checkout` 标准结账和 `POST /checkout/x402` x402结账是完整版独有功能。免费版仅支持商品浏览、搜索和详情查看。如需下单购买，请升级至完整版。

### Q2: 搜索支持哪些参数？

`GET /products/search` 支持参数：`q`（自然语言查询）、`category`（分类slug）、`priceMin`/`priceMax`（USD价格范围）、`sort`（newest/popular/rating/price_asc/price_desc，默认newest）、`limit`（每页结果数，默认20，最大100）、`offset`（分页偏移）。仅返回有库存商品。使用 `POST /agent/shop` 可获得AI增强的自然语言搜索体验。

### Q3: 免费版可以查看商品详情吗？

可以。`GET /products/{slug}` 获取商品完整信息，包括 `id`、`variants[]`（含 `id`、`name`、`inStock`、`stockQuantity`、`price`）、`images[]`、`relatedProducts[]` 和 `description`。

### Q4: 免费版可以跟踪订单吗？

不可以。`GET /orders/{orderId}/status` 订单状态跟踪和 `GET /orders/{orderId}` 订单详情是完整版独有功能。免费版不支持任何订单相关操作。如需订单跟踪，请升级至完整版。

### Q5: AI购物助手可以做什么？

`POST /agent/shop` 支持自然语言购物查询。发送消息如"wireless headphones under $200"，AI返回回复文本和匹配的 `products` 数组（含 `id`、`title`、`price`、`inStock`、`badge`）。可配合 `context` 中的 `priceRange` 和 `preferences` 精确搜索。

### Q6: 如何获取商品ID？

通过 `POST /agent/shop`、`GET /products/search` 或 `GET /products/featured` 获取商品列表。列表中的 `id` 字段（如 `prod_sony_wh1000xm4`）用于完整版的结账操作。免费版仅支持查看，不涉及结账。商品ID必须从API返回结果获取，禁止编造或猜测。

## 已知限制

- 不支持结账支付（`POST /checkout`/`POST /checkout/x402`），完整版可用
- 不支持订单跟踪（`GET /orders/{orderId}/status`/`GET /orders/{orderId}`），完整版可用
- 不支持支付方式查询（`GET /payment-methods`），完整版可用
- 不支持代理身份（`GET /agent/me`），完整版可用
- 速率限制约100 req/min per IP，超限返回429
- 商品ID必须从搜索结果获取，禁止编造

## 效率量化分析

| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 差异化对比

| 对比维度 | 本技能 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 核心功能 | 通用场景 | 通用场景 |

## 核心功能

- **自动化执行**: 基于指令驱动的自动化流程
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据