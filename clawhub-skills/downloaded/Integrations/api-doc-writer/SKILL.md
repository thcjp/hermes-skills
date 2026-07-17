---
slug: api-doc-writer
name: api-doc-writer
version: "1.0.1"
displayName: API Doc Writer
summary: API接口文档助手。用于编写REST API文档、定义接口规范、生成接口说明。当需要编写API文档、接口规范时触发。
license: MIT-0
description: |-
  API接口文档助手。用于编写REST API文档、定义接口规范、生成接口说明。当需要编写API文档、接口规范时触发。

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 生成接口说明, api, 用于编写, rest, 接口文档助手, writer, 文档, doc
tags:
- Integrations
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
