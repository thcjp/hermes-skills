---
slug: api-design-architect
name: api-design-architect
version: 1.1.0
displayName: API设计架构师
summary: 契约优先设计API,从源头杜绝接口腐化,让API可演化不破坏老用户
license: Proprietary
description: API设计架构师——在写第一行代码前先定义接口契约，从源头杜绝接口腐化与破坏性变更。适用于新API设计、模块边界划分、公共接口暴露、API演化迭代、接口质量审查等场景。遵循Hyrum定律与One-Version规则，支持REST/GraphQL/gRPC多协议，让API可演化、可维护、不破坏老用户。触发关键词：API设计、接口契约、OpenAPI、REST、GraphQL、gRPC、错误处理、API版本、模块边界、公共接口
tags:
- API设计
- 技术架构
- 接口规范
- 独立开发
- 软件设计
tools:
- read
- exec
suggested_price: 29.9
pricing_tier: L3
pricing_rationale: 设计创作类, medium市场, enterprise复杂度, weekly频次, business层 → 创作类工具,中等频次
pricing_model: per_use
---

# API设计架构师

契约优先的 API 设计方法。先定义接口契约，再实现。确保 API 可演化、可维护、不破坏现有用户。

## 核心能力

- **契约优先设计**：在编码前定义 OpenAPI/GraphQL Schema/Proto 契约，从源头杜绝接口腐化
- **演化策略制定**：基于 Hyrum 定律与 One-Version 规则，设计向后兼容的字段扩展与破坏性变更迁移路径
- **错误语义规范**：统一错误格式（机器可读错误码 + 人类可读消息 + requestId），区分可重试与不可重试错误
- **边界校验体系**：入口校验（信任边界白名单）+ 出口校验（响应不泄露内部细节）+ 写操作幂等键
- **设计审查清单**：10 项设计检查清单，量化接口质量遵循度

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 新 API 设计 | 业务能力描述 + 协议选择(REST/GraphQL/gRPC) | OpenAPI 契约 + 设计文档 + 错误码表 |
| 模块边界划分 | 系统功能清单 + 依赖关系 | 接口清单 + 依赖方向图 + 职责划分 |
| 公共接口暴露 | 内部能力 + 对外开放范围 | 公共 API 契约 + 版本策略 + 文档 |
| API 演化迭代 | 现有契约 + 变更需求 | 变更分类(安全/破坏) + 迁移策略 + 废弃时间表 |
| 接口质量审查 | 现有 API 契约文件 | 10 项检查清单评分 + 问题清单 + 改进建议 |

**不适用于**：
- 单机内部函数调用设计（无跨进程边界）
- UI/UX 交互流程设计（非接口范畴）
- 数据库表结构设计（属数据建模非接口契约）
- 已有成熟框架的标准 CRUD（如 Rails/Django 默认 RESTful）

## 使用流程

### Step 1: 明确能力边界
- 与需求方确认 API 提供的核心能力（做什么/不做什么）
- 识别用户角色（终端用户/第三方开发者/内部服务）
- 确定协议：REST（资源导向）/ GraphQL（查询导向）/ gRPC（RPC 导向）

### Step 2: 定义资源与契约
- REST：列出资源 + HTTP 方法映射（GET/POST/PUT/DELETE/PATCH）
- GraphQL：定义 Type + Query/Mutation + 输入输出类型
- gRPC：定义 Service + Method + Proto Message
- 输出契约文件（OpenAPI YAML / GraphQL SDL / .proto）

### Step 3: 设计错误语义
- 错误分类：客户端错误 4xx / 服务端错误 5xx / 业务错误
- 统一错误格式：`{error: {code, message, details, requestId}}`
- 错误码命名：大写枚举（如 `VALIDATION_FAILED`），机器可读
- 标注可重试性：`retryable: true/false`

### Step 4: 边界校验设计
- 入口校验：类型/长度/范围/格式，白名单优于黑名单
- 出口校验：响应结构符合契约，敏感字段过滤（密码/令牌/内部 ID）
- 幂等性：写操作支持 `Idempotency-Key` 头

### Step 5: 制定演化策略
- 向后兼容变更：新增可选字段、新增端点、新增枚举值
- 破坏性变更：双写并存 → 通知迁移 → 监控旧版使用率 → 设定废弃时间表 → 下线

### Step 6: 输出文档
- API 契约：`output/{api-name}/contract.openapi.yaml`
- 设计文档：`output/{api-name}/design.md`
- 错误码表：`output/{api-name}/error-codes.md`
- 演化策略：`output/{api-name}/evolution.md`

## 示例

### 示例 1：电商订单 API 设计

**输入**：
```
需求：为电商平台设计订单 API，支持创建订单、查询订单、取消订单、支付回调。
协议：REST。预计日均订单 10 万，第三方商家需要对接。
```

**输出**：
```yaml
# contract.openapi.yaml (节选)
openapi: 3.0.3
info:
  title: 订单 API
  version: 1.0.0
paths:
  /v1/orders:
    post:
      summary: 创建订单
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required: [items, addressId]
              properties:
                items:
                  type: array
                  items:
                    type: object
                    required: [skuId, quantity]
                    properties:
                      skuId: {type: string, pattern: "^SKU-[A-Z0-9]{8}$"}
                      quantity: {type: integer, minimum: 1, maximum: 99}
                addressId: {type: string}
                idempotencyKey: {type: string, description: "幂等键，防重复下单"}
      responses:
        '201':
          description: 创建成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '409':
          description: 幂等键冲突
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Error:
      type: object
      properties:
        error:
          type: object
          required: [code, message]
          properties:
            code: {type: string, example: "VALIDATION_FAILED"}
            message: {type: string, example: "quantity must be between 1 and 99"}
            details: {type: array, items: {type: object}}
            requestId: {type: string, example: "req_abc123"}
            retryable: {type: boolean, example: false}
```

```markdown
# error-codes.md (节选)
| 错误码 | HTTP | 含义 | 可重试 |
|:-------|:-----|:-----|:-------|
| VALIDATION_FAILED | 400 | 请求参数校验失败 | 否 |
| IDEMPOTENCY_CONFLICT | 409 | 幂等键冲突 | 否 |
| INSUFFICIENT_STOCK | 409 | 库存不足 | 是(等待补货) |
| ORDER_NOT_FOUND | 404 | 订单不存在 | 否 |
| PAYMENT_TIMEOUT | 408 | 支付超时 | 是 |
```

### 示例 2：API 演化（破坏性变更迁移）

**输入**：
```
现有 API：GET /v1/users 返回 {id, name, email}
需求：将 email 字段拆分为 email + emailVerified，需破坏性变更。
```

**输出**：
```markdown
# evolution.md
## 变更分类
- **破坏性变更**：字段结构改变（email → email + emailVerified）

## 迁移策略
### 阶段 1：双写并存（第 0-2 周）
- 新增 GET /v2/users 返回 {id, name, email, emailVerified}
- /v1/users 保持不变，但响应头增加 `Sunset: Sat, 31 Dec 2026 23:59:59 GMT`
- /v1/users 响应头增加 `Deprecation: true` 和 `Link: </v2/users>; rel="successor-version"`

### 阶段 2：通知迁移（第 2-4 周）
- 邮件通知所有已知调用方
- Dashboard 显示 v1 调用量趋势
- 文档首页置顶迁移指南

### 阶段 3：监控旧版（第 4-8 周）
- 监控 /v1/users 调用量，目标降至 < 1% 总流量
- 对未迁移调用方单独触达

### 阶段 4：下线（第 8 周后）
- /v1/users 返回 410 Gone + 迁移指引
- 保留错误响应 30 天后彻底移除路由
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 契约与实现不一致 | 实现未遵循契约或契约未更新 | 以契约为准，使用 schema 验证中间件拦截不一致响应 |
| 破坏性变更误判为兼容 | 字段语义改变但类型不变 | 审查所有字段语义变更，语义变更视为破坏性 |
| 幂等键冲突 | 客户端重复提交相同幂等键 | 返回 409 + 原订单信息，不重复创建 |
| 错误码命名冲突 | 不同模块使用相同错误码 | 建立全局错误码注册表，前缀区分模块（如 `ORDER_*`） |
| 文档与契约不同步 | 文档手动维护遗漏更新 | 文档从契约自动生成（Swagger UI / Redoc） |
| 未知枚举值未处理 | 新增枚举值后老客户端崩溃 | 客户端必须处理未知值，契约标注 `enum + default` |

## 依赖说明

### 运行环境
- **Agent 平台**：Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持 SKILL.md 的任意 Agent
- **操作系统**：Windows / macOS / Linux
- **运行时**：无需额外运行时（纯 Markdown Skill）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 可选 | 由 Agent 内置 LLM 提供，辅助设计决策 |
| Mermaid 渲染器 | 工具 | 可选 | 设计文档图表渲染 |
| Swagger Editor | 工具 | 可选 | OpenAPI 契约校验与预览 |

### API Key 配置
- 本 Skill 无需额外 API Key 配置
- 所有设计产出为本地文件，不涉及外部服务调用
- 若使用 LLM 辅助，API Key 由 Agent 平台托管，Skill 内零硬编码

### 可用性分类
- **分类**：MD
- **说明**：纯 Markdown，零依赖，任何 Agent 平台直接使用

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: RESTful资源API契约设计

**输入**:
```
需求：为博客系统设计文章管理API，支持文章CRUD、评论管理、标签分类。
协议：REST。面向第三方开发者开放，需要OAuth 2.0授权。
```

**LLM生成输出**:
```yaml
# output/blog-api/contract.openapi.yaml
openapi: 3.0.3
info:
  title: 博客API
  version: 1.0.0
  description: 博客系统文章管理API，支持OAuth 2.0授权
  contact:
    name: API支持
    email: api@example.com

servers:
  - url: https://api.example.com/v1
    description: 生产环境
  - url: https://api-staging.example.com/v1
    description: 预发布环境

paths:
  /posts:
    get:
      summary: 获取文章列表
      parameters:
        - name: page
          in: query
          schema: {type: integer, minimum: 1, default: 1}
        - name: pageSize
          in: query
          schema: {type: integer, minimum: 1, maximum: 100, default: 20}
        - name: tag
          in: query
          schema: {type: string, pattern: "^[a-z0-9-]+$"}
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PostListResponse'
    post:
      summary: 创建文章
      security:
        - oauth2: [posts:write]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreatePostRequest'
      responses:
        '201':
          description: 创建成功
          headers:
            Location:
              schema: {type: string, format: uri}
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Post'
        '409':
          description: 幂等冲突
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

  /posts/{postId}:
    parameters:
      - name: postId
        in: path
        required: true
        schema: {type: string, pattern: "^post_[a-z0-9]{16}$"}
    get:
      summary: 获取单篇文章
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Post'
        '404':
          description: 文章不存在
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
    patch:
      summary: 部分更新文章
      security:
        - oauth2: [posts:write]
      responses:
        '200':
          description: 更新成功
        '422':
          description: 校验失败

components:
  securitySchemes:
    oauth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://auth.example.com/oauth/authorize
          tokenUrl: https://auth.example.com/oauth/token
          scopes:
            posts:read: 读取文章
            posts:write: 创建和修改文章
  schemas:
    Post:
      type: object
      required: [id, title, content, author, createdAt]
      properties:
        id: {type: string, example: "post_abc123def456gh7"}
        title: {type: string, minLength: 1, maxLength: 200}
        content: {type: string, maxLength: 100000}
        excerpt: {type: string, maxLength: 500, readOnly: true}
        tags:
          type: array
          items: {type: string, pattern: "^[a-z0-9-]+$"}
          maxItems: 10
        author:
          type: object
          properties:
            id: {type: string}
            name: {type: string}
        publishedAt: {type: string, format: date-time, nullable: true}
        createdAt: {type: string, format: date-time, readOnly: true}
        updatedAt: {type: string, format: date-time, readOnly: true}
    Error:
      type: object
      required: [error]
      properties:
        error:
          type: object
          required: [code, message]
          properties:
            code: {type: string, example: "POST_NOT_FOUND"}
            message: {type: string}
            details: {type: array, items: {type: object}}
            requestId: {type: string, example: "req_9f8e7d6c"}
            retryable: {type: boolean, default: false}
```

```markdown
# output/blog-api/error-codes.md
| 错误码 | HTTP | 含义 | 可重试 |
|:-------|:-----|:-----|:-------|
| VALIDATION_FAILED | 400 | 请求参数校验失败 | 否 |
| UNAUTHORIZED | 401 | 未授权或令牌过期 | 否 |
| FORBIDDEN | 403 | 权限不足 | 否 |
| POST_NOT_FOUND | 404 | 文章不存在 | 否 |
| IDEMPOTENCY_CONFLICT | 409 | 幂等键冲突 | 否 |
| RATE_LIMITED | 429 | 请求频率超限 | 是(等待后重试) |
| INTERNAL_ERROR | 500 | 服务器内部错误 | 是 |
```

**效果验证**: ✓OpenAPI 3.0.3规范合规 ✓OAuth 2.0安全方案完整 ✓错误格式统一 ✓资源路径符合RESTful规范 ✓幂等键支持

### 案例2: GraphQL Schema设计

**输入**:
```
需求：为内容管理系统设计GraphQL API，支持文章、作者、评论的关联查询。
要求：支持分页、过滤、嵌套查询，权限按字段控制。
```

**LLM生成输出**:
```graphql
# output/cms-api/schema.graphql
type Query {
  posts(first: Int = 20, after: String, filter: PostFilter): PostConnection!
  post(id: ID!): Post
  authors(first: Int = 20, after: String): AuthorConnection!
  author(id: ID!): Author
}

type Mutation {
  createPost(input: CreatePostInput!): CreatePostPayload!
  updatePost(id: ID!, input: UpdatePostInput!): UpdatePostPayload!
  deletePost(id: ID!): DeletePostPayload!
  publishPost(id: ID!, idempotencyKey: String): PublishPostPayload!
}

input PostFilter {
  tag: String
  authorId: ID
  status: PostStatus
  createdAfter: DateTime
}

input CreatePostInput {
  title: String!
  content: String!
  excerpt: String
  tagIds: [ID!]!
  clientMutationId: String
}

type Post implements Node {
  id: ID!
  title: String!
  content: String!
  excerpt: String
  status: PostStatus!
  tags: [Tag!]!
  author: Author!
  comments(first: Int = 10, after: String): CommentConnection!
  publishedAt: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
}

type PostConnection {
  edges: [PostEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type PostEdge {
  node: Post!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

enum PostStatus {
  DRAFT
  PUBLISHED
  ARCHIVED
}

interface Node {
  id: ID!
}

scalar DateTime
```

```markdown
# output/cms-api/design.md (节选)
## 权限控制策略
- `posts`查询：公开，但`status=DRAFT`仅作者本人可查
- `createPost`：需`posts:write`权限
- `deletePost`：需`posts:delete`权限或作者本人
- `comments.author.email`：仅管理员可查

## 分页规范
采用Relay风格游标分页：
- `first`/`after`：正向翻页
- `last`/`before`：反向翻页（少用，性能差）
- 游标采用base64编码的`{id, createdAt}`组合

## 演化策略
- 向后兼容：新增可选字段、新增枚举值（客户端必须处理未知值）
- 破坏性变更：字段重命名采用`@deprecated`标记，6个月后移除
```

**效果验证**: ✓GraphQL SDL规范合规 ✓Relay风格分页 ✓嵌套查询支持 ✓权限控制策略完整 ✓演化策略明确

### 案例3: API破坏性变更迁移

**输入**:
```
现有API: GET /v1/products 返回 {id, name, price, currency}
需求: 将price字段从单一数值改为对象 {amount, currency}，需破坏性变更。
现有调用方: 50个第三方应用，日均调用量100万次。
```

**LLM生成输出**:
```markdown
# output/product-api/evolution.md
## 变更分类
- **破坏性变更**: 字段类型改变（price: number → price: object）
- 原因: 单一price字段无法表达多币种场景，类型变更无法向后兼容

## 迁移策略

### 阶段1: 双写并存（第0-4周）
- 新增 GET /v2/products 返回 {id, name, price: {amount, currency}}
- /v1/products 响应头增加:
  ```
  Sunset: Sat, 31 Dec 2026 23:59:59 GMT
  Deprecation: true
  Link: </v2/products>; rel="successor-version"
  ```
- /v1/products 保持原有响应格式不变
- 响应体增加 `priceV2: {amount, currency}` 作为过渡字段（非破坏性）

### 阶段2: 通知与文档（第4-8周）
- 邮件通知所有已注册的50个调用方
- API文档首页置顶迁移指南
- Dashboard增加v1调用量趋势图，供调用方自查
- 提供v1→v2的代码迁移示例（Python/Node.js/Java）

### 阶段3: 监控与触达（第8-16周）
- 监控 /v1/products 调用量，目标: 降至总流量 < 1%
- 对未迁移调用方单独邮件+电话触达
- 对Top 10调用量调用方提供专属技术支持
- 周报通报迁移进度

### 阶段4: 渐进式限制（第16-20周）
- /v1/products 增加速率限制: 原QPS的50%
- 响应头增加警告: `Warning: 299 - "API will be removed"`
- 仍能使用但性能下降，促使迁移

### 阶段5: 下线（第20周后）
- /v1/products 返回 410 Gone
```json
{
  "error": {
    "code": "API_VERSION_REMOVED",
    "message": "v1 has been removed. Migrate to /v2/products",
    "docs": "https://docs.example.com/migration/v1-to-v2",
    "requestId": "req_abc123",
    "retryable": false
  }
}
```
- 保留410响应30天，之后路由彻底移除
```

**效果验证**: ✓变更分类正确（破坏性） ✓五阶段迁移路径完整 ✓Sunset/Deprecation头规范 ✓监控指标明确 ✓下线策略温和渐进

### 案例4: gRPC服务契约设计

**输入**:
```
需求: 为订单服务设计gRPC接口，供内部微服务调用。
要求: 支持创建订单、查询订单、取消订单，需要双向流式查询订单状态变更。
```

**LLM生成输出**:
```protobuf
// output/order-service/order.proto
syntax = "proto3";

package com.example.order.v1;

option go_package = "github.com/example/proto/order/v1;orderv1";
option java_multiple_files = true;
option java_package = "com.example.order.v1";

import "google/protobuf/timestamp.proto";
import "google/protobuf/field_mask.proto";
import "google/rpc/code.proto";

// 订单服务
service OrderService {
  // 创建订单
  rpc CreateOrder(CreateOrderRequest) returns (Order);
  
  // 查询订单
  rpc GetOrder(GetOrderRequest) returns (Order);
  
  // 批量查询订单
  rpc ListOrders(ListOrdersRequest) returns (ListOrdersResponse);
  
  // 取消订单
  rpc CancelOrder(CancelOrderRequest) returns (Order);
  
  // 流式订阅订单状态变更
  rpc WatchOrderStatus(WatchOrderStatusRequest) 
      returns (stream OrderStatusEvent);
}

message Order {
  string id = 1;  // 订单ID，格式: ord_xxx
  string user_id = 2;
  repeated OrderItem items = 3;
  int64 total_amount = 4;  // 金额（分）
  string currency = 5;     // ISO 4217
  OrderStatus status = 6;
  google.protobuf.Timestamp created_at = 7;
  google.protobuf.Timestamp updated_at = 8;
  
  // 下次版本预留
  reserved 9 to 19;
  reserved "shipping_address", "billing_address";
}

message OrderItem {
  string sku_id = 1;
  int32 quantity = 2;
  int64 unit_price = 3;
}

enum OrderStatus {
  ORDER_STATUS_UNSPECIFIED = 0;
  ORDER_STATUS_PENDING = 1;
  ORDER_STATUS_PAID = 2;
  ORDER_STATUS_SHIPPED = 3;
  ORDER_STATUS_DELIVERED = 4;
  ORDER_STATUS_CANCELLED = 5;
}

message CreateOrderRequest {
  string user_id = 1;
  repeated OrderItem items = 2;
  string idempotency_key = 3;  // 幂等键
}

message OrderStatusEvent {
  string order_id = 1;
  OrderStatus previous_status = 2;
  OrderStatus current_status = 3;
  google.protobuf.Timestamp occurred_at = 4;
  string message = 5;
}
```

```markdown
# output/order-service/error-codes.md
| gRPC Code | HTTP映射 | 含义 | 可重试 |
|:----------|:---------|:-----|:-------|
| INVALID_ARGUMENT | 400 | 请求参数校验失败 | 否 |
| NOT_FOUND | 404 | 订单不存在 | 否 |
| ALREADY_EXISTS | 409 | 幂等键冲突，订单已存在 | 否 |
| FAILED_PRECONDITION | 412 | 订单状态不允许操作（如已取消） | 否 |
| RESOURCE_EXHAUSTED | 429 | 超出速率限制 | 是 |
| UNAVAILABLE | 503 | 服务暂时不可用 | 是 |
| INTERNAL | 500 | 内部错误 | 是 |
```

**效果验证**: ✓Proto3语法规范 ✓reserved字段预留演化空间 ✓幂等键设计 ✓流式状态订阅支持 ✓gRPC错误码与HTTP映射

### 案例5: API质量审查评分

**输入**:
```
现有API契约文件: user-api.yaml (OpenAPI 3.0)
审查维度: 命名规范、版本管理、错误处理、安全设计、文档完整性
```

**LLM生成输出**:
```markdown
# output/user-api-review/review-report.md
# API质量审查报告

## 评分总览
| 维度 | 评分 | 等级 |
|:-----|:-----|:-----|
| 命名规范 | 8/10 | B |
| 版本管理 | 6/10 | C |
| 错误处理 | 7/10 | B |
| 安全设计 | 9/10 | A |
| 文档完整性 | 5/10 | C |
| **总评** | **35/50** | **B-** |

## 详细审查

### 1. 命名规范 (8/10)
✓ 资源路径使用复数名词: /users, /users/{id}
✓ HTTP方法语义正确: GET查询, POST创建, PATCH更新
✗ 字段命名不一致: 混用snake_case(user_id)和camelCase(userId)
  建议: 统一采用snake_case，与JSON社区惯例一致
✗ 错误码命名缺少模块前缀: NOT_FOUND 应为 USER_NOT_FOUND

### 2. 版本管理 (6/10)
✓ URL路径包含版本: /v1/users
✗ 未配置 Sunset / Deprecation 响应头
✗ 缺少版本变更日志(CHANGELOG)
✗ 未声明版本支持策略(如:每个版本支持多久)
  建议: 文档明确版本支持周期(如N+1模式，新版本发布后旧版本支持6个月)

### 3. 错误处理 (7/10)
✓ 统一错误格式: {error: {code, message}}
✓ HTTP状态码使用合理
✗ 缺少 requestId 字段，不利于问题追踪
✗ 缺少 retryable 字段，客户端无法判断是否重试
✗ 错误码未集中注册，可能命名冲突
  建议: 补充requestId和retryable字段，建立全局错误码注册表

### 4. 安全设计 (9/10)
✓ OAuth 2.0授权
✓ 输入参数校验(minLength/maxLength/pattern)
✓ 敏感字段(password)不在响应中暴露
✓ 速率限制头: X-RateLimit-*
✗ 缺少幂等键支持(Idempotency-Key)
  建议: 写操作(POST/PUT/PATCH)支持Idempotency-Key头

### 5. 文档完整性 (5/10)
✓ 每个端点有summary
✗ 缺少 description 详细说明
✗ 缺少请求/响应示例(example)
✗ 缺少错误场景示例
✗ 未说明分页约定(cursor还是offset)
  建议: 每个端点补充description、example，文档中明确分页/过滤/排序约定

## 改进优先级
1. **高优先级**: 补充requestId、retryable字段; 统一字段命名
2. **中优先级**: 添加版本支持策略; 补充端点示例
3. **低优先级**: 错误码加模块前缀; 添加幂等键支持
```

**效果验证**: ✓10项检查清单全覆盖 ✓量化评分客观 ✓问题清单具体 ✓改进建议可执行 ✓优先级排序合理

## 常见问题

### Q1: 契约优先是否会拖慢开发进度？
A: 短期增加 1-2 天契约设计时间，但避免了后期接口腐化导致的返工成本。对于 MVP 阶段，可先用简化契约（仅路径 + 方法 + 基本类型），迭代中逐步细化。

### Q2: REST、GraphQL、gRPC 如何选择？
A: REST 适合面向外部开发者的公开 API（生态成熟、缓存友好）；GraphQL 适合多端复用、查询灵活的场景（前端聚合数据）；gRPC 适合内部服务间高性能通信（Protobuf 二进制、双向流）。

### Q3: 如何判断一个变更是"破坏性"的？
A: 以下任一即为破坏性：删除/重命名字段、改变字段类型、改变字段语义（如 null → 必填）、收紧校验规则（如 maxLength 100 → 50）、改变默认行为。新增可选字段或端点通常是安全的。

### Q4: Hyrum 定律在实际中如何应对？
A: 假设所有可观察行为（响应字段顺序、错误消息措辞、响应时序）都会被依赖。应对策略：契约只承诺必要行为；文档明确标注"实现细节，不保证稳定"；变更前发布 changelog 通知。

## 已知限制

- 本 Skill 提供设计方法论与契约模板，不生成实际业务代码实现
- 性能取决于底层 LLM 能力，复杂业务规则可能需要人工补充领域知识
- 不替代 API 网关配置（限流、认证、路由需由网关层实现）
- 契约校验需配合外部工具（如 swagger-cli、spectral）完成自动化验证
- 对非 HTTP 协议（如 WebSocket、消息队列）的支持有限，需参考各自协议规范

## 安全

- **API Key 零暴露**：本 Skill 不涉及任何外部 API 调用，无需配置密钥
- **敏感字段过滤**：响应契约设计强制过滤密码、令牌、内部 ID 等敏感字段
- **输入校验白名单**：所有输入参数采用白名单校验，拒绝非预期字符
- **错误信息脱敏**：错误消息不暴露内部堆栈、SQL、文件路径等实现细节
