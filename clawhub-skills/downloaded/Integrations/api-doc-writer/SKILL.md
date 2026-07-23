---
slug: api-doc-writer
name: api-doc-writer
version: "1.0.1"
displayName: API Doc Writer
summary: API接口文档助手。用于编写REST API文档、定义接口规范、生成接口说明。当需要编写API文档、接口规范时触发。
license: MIT-0
description: |-
  API接口文档助手。用于编写REST API文档、定义接口规范、生成接口说明。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# API Doc Writer

## API文档模板

```markdown

版本：V1.0
更新日期：YYYY-MM-DD
维护人：XXX

---

## 接口概览

| 模块 | 接口数 | 负责人 |
|------|--------|--------|
| 用户模块 | 5 | @xxx |
| 订单模块 | 8 | @xxx |
| 支付模块 | 4 | @xxx |

---

## 通用说明

### 认证方式
```

Authorization: Bearer

```text
### 请求格式
```

Content-Type: application/json

```text
### 响应格式
```json
{
  "code": 0,
  "message": "success",
  "data": {}
}
```

### 状态码

| 状态码 | 说明 |
| --- | --- |
| 0 | 成功 |
| 1001 | 参数错误 |
| 2001 | 未授权 |
| 3001 | 资源不存在 |
| 5001 | 服务器错误 |

---

## 接口详情

### 1. 用户接口

#### 1.1 获取用户信息

**接口地址**

```text
GET /api/v1/users/{id}
```

**请求参数**

| 参数名 | 类型 | 位置 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | long | path | 是 | 用户ID |

**请求示例**

```text
GET /api/v1/users/123
```

**响应示例**

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 123,
    "name": "张三",
    "email": "zhangsan@example.com",
    "phone": "13800138000",
    "created_at": "2024-01-01 10:00:00"
  }
}
```

**错误示例**

```json
{
  "code": 3001,
  "message": "用户不存在",
  "data": null
}
```

---

#### 1.2 创建用户

**接口地址**

```text
POST /api/v1/users
```

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 用户名 |
| email | string | 是 | 邮箱 |
| phone | string | 否 | 手机号 |
| password | string | 是 | 密码 |

**请求示例**

```json
{
  "name": "张三",
  "email": "zhangsan@example.com",
  "phone": "13800138000",
  "password": "123456"
}
```

**响应示例**

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 123,
    "name": "张三"
  }
}
```

---

### 2. 订单接口

#### 2.1 订单列表

**接口地址**

```text
GET /api/v1/orders
```

**请求参数**

| 参数名 | 类型 | 位置 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| page | int | query | 否 | 页码，默认1 |
| page_size | int | query | 否 | 每页数量，默认20 |
| status | string | query | 否 | 订单状态 |

**请求示例**

```text
GET /api/v1/orders?page=1&page_size=10&status=paid
```

**响应示例**

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "total": 100,
    "page": 1,
    "page_size": 10,
    "list": [
      {
        "id": "ORD202401010001",
        "user_id": 123,
        "amount": 100.00,
        "status": "paid",
        "created_at": "2024-01-01 10:00:00"
      }
    ]
  }
}
```

---

## 接口变更记录

| 版本 | 日期 | 变更内容 | 变更人 |
| --- | --- | --- | --- |
| V1.0 | YYYY-MM-DD | 初始版本 | @xxx |
| V1.1 | YYYY-MM-DD | 新增xxx接口 | @xxx |

```text
## 接口设计原则

### RESTful规范
| 方法 | 用途 | 示例 |
|------|------|------|
| GET | 查询 | GET /users |
| POST | 创建 | POST /users |
| PUT | 完整更新 | PUT /users/1 |
| PATCH | 部分更新 | PATCH /users/1 |
| DELETE | 删除 | DELETE /users/1 |

### URL命名规范
```markdown
- 使用名词复数：/users
- 使用小写：/user-info
- 使用连字符分隔：/order-details
- 避免动词：不用 /getUser
```

### 状态码规范

| 类别 | 状态码 | 说明 |
| --- | --- | --- |
| 1xx | 信息 | 接收的请求正在处理 |
| 2xx | 成功 | 请求正常处理完毕 |
| 3xx | 重定向 | 需要附加操作完成请求 |
| 4xx | 客户端错误 | 请求有语法错误 |
| 5xx | 服务器错误 | 服务器处理出错 |

### 安全建议

* 敏感信息加密传输
* 身份验证Token过期机制
* 接口调用频率限制
* 参数校验过滤

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

- 用于编写REST API文档、定义接口规范、生成接口说明
- 当需要编写API文档、接口规范时触发
- 触发关键词: 生成接口说明, api, 用于编写, rest, 接口文档助手, writer, 文档, doc

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

### Q1: 如何开始使用API Doc Writer？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: API Doc Writer有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
