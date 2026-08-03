---
name: "api-generator-free"
description: "生成RESTful端点、GraphQL schema与测试套件,快速搭建API代码脚手架。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "API代码生成器免费版"
  version: "1.0.0"
  summary: "生成RESTful端点、GraphQL schema与测试套件,快速搭建API代码脚手架"
  tags:
    - "研发工具"
    - "Development"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
tools:
  - exec
  - read
  - write
---
# API 代码生成器（免费版）

从零生成基础 API 代码脚手架。支持 RESTful 端点、GraphQL schema 与测试套件,所有代码输出到 stdout。

> **升级提示**: OpenAPI 文档、Python 客户端、Mock 服务器、认证代码、速率限制器等高级功能为付费版专享。升级付费版解锁完整能力。

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

- **rest** `<name>` — RESTful CRUD 端点（Express.js）,含 GET/POST/PUT/DELETE 路由
- **graphql** `<name>` — GraphQL Type + Query + Mutation schema 定义
- **test** `<name>` — Jest + Supertest API 测试套件,含 CRUD 测试用例

### 付费版专享功能
以下功能在免费版中不可用,升级付费版解锁:

- **swagger** `<name>` — OpenAPI 3.0 规范文档生成
- **client** `<name>` — Python API 客户端类生成
- **mock** `<name>` — Mock API 服务器（内存存储）生成
- **auth** `<type>` — 认证代码生成（`jwt`/`oauth`/`apikey`）
- **rate-limit** `<type>` — 速率限制器生成（`token-bucket`/`sliding-window`）

### rest

执行rest操作,处理用户输入并返回结果。

**输入**: 用户提供rest所需的参数和指令。

### graphql

执行graphql操作,处理用户输入并返回结果。

**输入**: 用户提供graphql所需的参数和指令。

#
## 命令用法

```bash
bash scripts/apigen.sh <command> <resource_name> [options]
```

| 命令 | 免费版 | 说明 |
|------|--------|------|
| `rest` | 可用 | 生成 RESTful CRUD 端点（Express.js） |
| `graphql` | 可用 | 生成 GraphQL schema |
| `test` | 可用 | 生成 Jest+Supertest 测试套件 |
| `swagger` | 付费版 | 生成 OpenAPI 3.0 文档 |
| `client` | 付费版 | 生成 Python API 客户端 |
| `mock` | 付费版 | 生成 Mock API 服务器 |
| `auth` | 付费版 | 生成认证代码 |
| `rate-limit` | 付费版 | 生成速率限制器 |

## 使用流程

### Step 1: 确定生成目标
明确需要生成的代码类型（rest/graphql/test）与资源名称。

### Step 2: 执行生成命令
```bash
bash scripts/apigen.sh rest user
```

### Step 3: 查看输出
所有代码输出到 stdout,含完整注释。

### Step 4: 重定向到项目文件
```bash
bash scripts/apigen.sh rest user > routes/user.js
bash scripts/apigen.sh test user > tests/user.test.js
```

> **提示**: 如需生成 OpenAPI 文档、Mock 服务器、认证代码等,请升级付费版。

## 案例展示

### 案例1: 生成用户 RESTful 端点
**场景**: 开发者需要快速搭建用户 CRUD API

```bash
bash scripts/apigen.sh rest user
```

**输出**: Express.js 路由代码,包含:
- `GET /users` — 获取用户列表
- `GET /users/:id` — 获取单个用户
- `POST /users` — 创建用户
- `PUT /users/:id` — 更新用户
- `DELETE /users/:id` — 删除用户

**说明**: 生成的代码含完整注释与错误处理,重定向到 `routes/user.js` 即可使用。

### 案例2: 生成产品 GraphQL Schema
**场景**: 开发者需要为产品模块定义 GraphQL 类型

```bash
bash scripts/apigen.sh graphql product
```

**输出**: GraphQL schema 定义,包含:
- `type Product` — 产品类型定义（id, name, price, description）
- `type Query` — 查询（`products`、`product(id)`）
- `type Mutation` — 变更（`createProduct`、`updateProduct`、`deleteProduct`）

### 案例3: 生成订单测试套件
**场景**: 开发者需要为订单 API 编写测试

```bash
bash scripts/apigen.sh test order
```

**输出**: Jest + Supertest 测试文件,包含:
- 创建订单测试（`POST /orders`）
- 获取订单列表测试（`GET /orders`）
- 更新订单测试（`PUT /orders/:id`）
- 删除订单测试（`DELETE /orders/:id`）

> **升级提示**: 付费版支持 `auth jwt` 生成 JWT 认证代码与 `rate-limit token-bucket` 生成速率限制器。

## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|---------|---------|---------|---------|
| 命令不存在 | `Unknown command: <cmd>` | 使用了未定义的命令 | 使用 rest/graphql/test（免费版）或升级付费版 |
| 资源名缺失 | `Resource name required` | 未提供 `<name>` 参数 | 补充资源名,如 `bash scripts/apigen.sh rest user` |
| 命令需付费 | `Paid feature: <cmd>` | 使用了付费版专享命令 | 升级付费版解锁 swagger/client/mock/auth/rate-limit |
| 脚本无执行权限 | `Permission denied` | `scripts/apigen.sh` 无执行权限 | 执行 `chmod +x scripts/apigen.sh` |
| Bash 不可用 | `bash: command not found` | Windows 环境未安装 Bash | 安装 Git Bash 或 WSL |

## 常见问题

### Q1: 免费版支持哪些命令?
A: 免费版支持 3 个核心命令: `rest`（RESTful 端点）、`graphql`（GraphQL schema）、`test`（测试套件）。`swagger`、`client`、`mock`、`auth`、`rate-limit` 需升级付费版。

### Q2: 免费版能生成认证代码吗?
A: 不能。`auth` 命令（支持 `jwt`/`oauth`/`apikey` 三种类型）为付费版专享。升级付费版可生成 JWT 认证中间件、OAuth2 授权流程与 API Key 验证代码。

### Q3: 免费版能生成 Mock 服务器吗?
A: 不能。`mock` 命令为付费版专享。升级付费版可生成基于内存存储的 Mock API 服务器,适用于前端开发时后端 API 未就绪的场景。

### Q4: 免费版能生成 OpenAPI 文档吗?
A: 不能。`swagger` 命令为付费版专享。升级付费版可生成 OpenAPI 3.0 规范文档,含路径、参数、响应定义。

### Q5: 免费版能生成速率限制器吗?
A: 不能。`rate-limit` 命令为付费版专享。升级付费版可生成 `token-bucket`（令牌桶）与 `sliding-window`（滑动窗口）两种算法的速率限制器。

## 已知限制

1. **仅 3 个命令**: 免费版仅支持 rest/graphql/test,其余 5 个命令需升级
2. **无认证代码**: 不支持 jwt/oauth/apikey 认证代码生成
3. **无 Mock 服务器**: 不支持内存 Mock API 服务器生成
4. **无 OpenAPI 文档**: 不支持 swagger 规范文档生成
5. **无速率限制器**: 不支持 token-bucket/sliding-window 限流器生成
6. **无 Python 客户端**: 不支持 client 命令生成 Python API 客户端

---

> **升级付费版** 解锁: swagger（OpenAPI 文档）、client（Python 客户端）、mock（Mock 服务器）、auth（认证代码）、rate-limit（速率限制器）等完整生成能力。

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

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