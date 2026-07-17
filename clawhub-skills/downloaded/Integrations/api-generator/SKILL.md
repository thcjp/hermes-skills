---
slug: api-generator
name: api-generator
version: "2.0.0"
displayName: Api Generator
summary: API code generator. Generate RESTful endpoints, GraphQL schemas, OpenAPI/Swagger
  docs, API client...
license: MIT-0
description: |-
  API code generator. Generate RESTful endpoints, GraphQL schemas, OpenAPI/Swagger
  docs, API client...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: generator, api, generate, restful, endpoints, code
tags:
- Integrations
tools:
- read
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

## Examples

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
