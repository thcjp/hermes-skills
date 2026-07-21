---
slug: api-generator
name: api-generator
version: "2.0.0"
displayName: Api Generator
summary: API code generator. Generate RESTful endpoints, GraphQL schemas, OpenAPI/Swagger
  docs, API client...
license: MIT-0
description: |-
  API code generator。Generate RESTful endpoints, GraphQL schemas, OpenAPI/Swagger
  docs, API client。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
---

# Api Generator

Generate production-ready API code scaffolds from zero. REST, GraphQL, auth, tests — all in one tool.

## Usage

```bash
bash scripts/apigen.sh <command> <resource_name> [options]
```

## Commands

### Core Generation

* **rest** `<name>` — RESTful CRUD endpoints (Express.js)
* **graphql** `<name>` — GraphQL Type + Query + Mutation schema
* **swagger** `<name>` — OpenAPI 3.0 specification document

### Utilities

* **client** `<name>` — Python API client class
* **mock** `<name>` — Mock API server with in-memory store
* **auth** `<type>` — Auth code (`jwt` / `oauth` / `apikey`)
* **rate-limit** `<type>` — Rate limiter (`token-bucket` / `sliding-window`)
* **test** `<name>` — Jest + Supertest API test suite

## 示例

```bash
bash scripts/apigen.sh rest user          # RESTful user endpoints
bash scripts/apigen.sh graphql product    # GraphQL product schema
bash scripts/apigen.sh auth jwt           # JWT authentication
bash scripts/apigen.sh test order         # Order API tests
```

## Output

## All code prints to stdout. Copy or redirect into your project files. Generated code includes full comments and can serve as a project starting point.

💬 Feedback & Feature Requests: <https://bytesagain.com/feedback>
Powered by BytesAgain | bytesagain.com

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

- API code generator
- Generate RESTful endpoints, GraphQL schemas, OpenAPI/Swagger
  docs, API client
- 触发关键词: generator, api, generate, restful, endpoints, code

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Api Generator？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Api Generator有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
