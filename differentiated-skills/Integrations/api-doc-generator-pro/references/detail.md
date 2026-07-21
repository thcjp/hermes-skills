# 详细参考 - api-doc-generator-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (graphql)

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  orders: [Order!]!
}

type Order {
  id: ID!
  user: User!
  amount: Float!
  status: OrderStatus!
  createdAt: DateTime!
}

enum OrderStatus {
  PENDING
  PAID
  SHIPPED
  COMPLETED
}

type Query {
  user(id: ID!): User
  orders(userId: ID!, limit: Int = 10): [Order!]!
}

type Mutation {
  createOrder(input: CreateOrderInput!): Order!
}

input CreateOrderInput {
  userId: ID!
  items: [OrderItemInput!]!
  totalAmount: Float!
}
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│             API文档生成器专业版 (DOC GENERATOR PRO)              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  采集层      │  │  生成层      │  │  治理层      │              │
│  │  COLLECT    │  │  GENERATE   │  │  GOVERN     │              │
│  │             │  │             │  │             │              │
│  │ 自然语言    │  │ OpenAPI YAML│  │ 版本管理    │              │
│  │ 代码扫描    │  │ Markdown    │  │ 字段diff    │              │
│  │ 函数签名    │  │ GraphQL SDL │  │ 变更追踪    │              │
│  │ curl命令    │  │ 多格式导出  │  │ 规范校验    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  联动层      │  ← Mock与文档互通               │
│                  │  LINK       │    ✅ 专业版                    │
│                  │  Mock服务器 │                                 │
│                  │  测试用例   │                                 │
│                  └─────────────┘                                 │
│                          │                                       │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  协作层      │  ← 团队评审                    │
│                  │  COLLAB     │    ✅ 专业版                    │
│                  │  PR评审     │                                 │
│                  │  评论@提及  │                                 │
│                  │  通知       │                                 │
│                  └─────────────┘                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (bash)

```bash
api-doc scan --lang <lang> --path <dir> --output <file>
api-doc scan --incremental  # 增量扫描
api-doc generate --spec <file> --format <fmt> --output <dir>
api-doc generate --bilingual  # 中英双语
api-doc export --spec <file> --format yaml|json|html|pdf|swagger-ui

api-doc commit --message <msg> --tag <tag>
api-doc diff <v1> <v2>
api-doc log  # 查看版本历史
api-doc mock start --spec <file> --port <port>
api-doc mock reload  # 热重载
api-doc mock stop

api-doc pr create --branch <branch> --reviewers <members>
api-doc pr list --status pending
api-doc pr merge <pr-id>

api-doc lint --spec <file> --ci-mode
api-doc lint --rules <ruleset>  # 自定义规则集
api-doc graphql generate --description <desc> --output <file>
api-doc graphql scan --path <dir> --output <file>

api-doc template lint <file>
api-doc template list  # 列出可用模板
api-doc collab enable --reviewers <members>
api-doc collab invite <email>
api-doc collab audit  # 审计成员权限
```

## 代码示例 (yaml)

```yaml
name: API文档生成与校验
on:
  pull_request:
    paths: ['src/**', 'openapi.yaml']
jobs:
  doc:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 安装文档生成器
        run: npm install -g api-doc-generator-pro
      - name: 扫描代码生成Spec
        run: api-doc scan --lang java --path ./src --output ./openapi.yaml
      - name: 规范校验
        run: api-doc lint --spec ./openapi.yaml --ci-mode
      - name: 与主分支Spec对比
        run: api-doc diff main --spec ./openapi.yaml --fail-on-breaking
      - name: 生成HTML文档
        run: api-doc export --spec ./openapi.yaml --format html --output ./docs/
      - name: 部署文档门户
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs/
```

## 代码示例 (bash)

```bash
api-doc pr create --branch feature/payment-api --reviewers @zhang,@li

PR #42: 新增支付模块接口
========================
Changes: +5 endpoints, +120 lines
Status:  PENDING REVIEW

Reviewers:
  @zhang: APPROVED
  @li:    CHANGES_REQUESTED
    Comment on POST /api/v1/payments:
      "建议 amount 字段用整数（分），避免浮点精度问题"
    Comment on GET /api/v1/payments/{id}:
      "响应里缺少 transaction_id 字段，对账需要"

api-doc pr merge 42
```

### 功能6：GraphQL Schema生成
**解决痛点**：GraphQL项目的Schema也要写文档，与REST文档割裂。

**专业版能力**：从GraphQL代码或自然语言生成SDL与文档。

```bash
api-doc graphql generate --description "用户查询、订单创建、订单查询" --output ./schema.graphql

api-doc graphql scan --path ./schema --output ./graphql-docs.md
```

生成的SDL示例：

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  orders: [Order!]!
}

type Order {
  id: ID!
  user: User!
  amount: Float!
  status: OrderStatus!
  createdAt: DateTime!
}

enum OrderStatus {
  PENDING
  PAID
  SHIPPED
  COMPLETED
}

type Query {
  user(id: ID!): User
  orders(userId: ID!, limit: Int = 10): [Order!]!
}

type Mutation {
  createOrder(input: CreateOrderInput!): Order!
}

input CreateOrderInput {
  userId: ID!
  items: [OrderItemInput!]!
  totalAmount: Float!
}
```



## 架构总览
```text
┌─────────────────────────────────────────────────────────────────┐
│             API文档生成器专业版 (DOC GENERATOR PRO)              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  采集层      │  │  生成层      │  │  治理层      │              │
│  │  COLLECT    │  │  GENERATE   │  │  GOVERN     │              │
│  │             │  │             │  │             │              │
│  │ 自然语言    │  │ OpenAPI YAML│  │ 版本管理    │              │
│  │ 代码扫描    │  │ Markdown    │  │ 字段diff    │              │
│  │ 函数签名    │  │ GraphQL SDL │  │ 变更追踪    │              │
│  │ curl命令    │  │ 多格式导出  │  │ 规范校验    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  联动层      │  ← Mock与文档互通               │
│                  │  LINK       │    ✅ 专业版                    │
│                  │  Mock服务器 │                                 │
│                  │  测试用例   │                                 │
│                  └─────────────┘                                 │
│                          │                                       │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  协作层      │  ← 团队评审                    │
│                  │  COLLAB     │    ✅ 专业版                    │
│                  │  PR评审     │                                 │
│                  │  评论@提及  │                                 │
│                  │  通知       │                                 │
│                  └─────────────┘                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```



