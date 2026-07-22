---
slug: "rest-api-reference"
name: "rest-api-reference"
version: "1.0.0"
displayName: "REST API参考手册"
summary: "147个第三方服务的REST API参考,含认证模式、端点、速率限制、分页与Webhook模式"
license: "Proprietary"
description: |-
  REST API 参考文档库。覆盖 147 个第三方服务的认证模式、端点参考、速率限制、分页模式与 Webhook 处理。
  按类别组织（AI/ML、支付、通信、CRM、数据库、媒体等 16 类）,每类含索引表与逐服务详解。
  提供多账户凭证命名规范、错误处理模式、幂等键使用等工程实践。仅作文档参考,不代用户执行请求。
tags:
  - 研发工具
  - Productivity
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
---
# REST API 参考手册

147 个第三方服务的 REST API 参考文档。按类别组织,每类含索引表与逐服务详解,覆盖认证模式、端点参考、速率限制、分页模式与 Webhook 处理。

**范围外**（本技能不做）: 逆向工程闭源 API、代用户执行实际 API 请求、管理用户 API Key、代理 API 调用。

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
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

- **147 服务覆盖**: 涵盖 AI/ML、支付、通信、CRM、数据库、媒体等 16 大类服务
- **认证文档**: 每个服务的认证方式（API Key / OAuth2 / Bearer Token / Basic Auth）
- **端点参考**: 含 curl 示例的端点说明,支持快速查阅
- **速率限制**: 各服务的 `X-RateLimit-Remaining` 头与 429 处理策略
- **分页模式**: cursor / offset / page 三种分页模式的实现参考
- **Webhook 模式**: 签名验证、重试策略、事件类型文档
- **多账户凭证命名**: `{SERVICE}_{ACCOUNT}_{TYPE}` 规范
- **幂等键使用**: 支付与关键操作的 `Idempotency-Key` 头规范
### 147 服务覆盖

执行147 服务覆盖操作,处理用户输入并返回结果。

**输入**: 用户提供147 服务覆盖所需的参数和指令。

**输出**: 返回147 服务覆盖的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`服务覆盖`相关配置参数进行设置
### 认证文档

执行认证文档操作,处理用户输入并返回结果。

**输入**: 用户提供认证文档所需的参数和指令。

**输出**: 返回认证文档的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`认证文档`相关配置参数进行设置
### 端点参考

执行端点参考操作,处理用户输入并返回结果。

**输入**: 用户提供端点参考所需的参数和指令。

**输出**: 返回端点参考的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`端点参考`相关配置参数进行设置
#
## API 分类索引

| 分类 | 文件 | 代表服务 |
| --- | --- | --- |
| AI/ML | `apis/ai-ml.md` | anthropic, openai, cohere, groq, mistral, perplexity, huggingface, replicate, stability, elevenlabs, deepgram, assemblyai |
| Payments | `apis/payments.md` | stripe, paypal, square, plaid, chargebee, paddle, lemonsqueezy, recurly, wise, coinbase, binance |
| Communication | `apis/communication.md` | twilio, sendgrid, mailgun, postmark, resend, mailchimp, slack, discord, telegram, zoom |
| Realtime | `apis/realtime.md` | sendbird, stream-chat, pusher, ably, onesignal, courier, knock, novu |
| CRM | `apis/crm.md` | salesforce, hubspot, pipedrive, attio, close, apollo, outreach, gong |
| Marketing | `apis/marketing.md` | drift, crisp, front, customer-io, braze, iterable, klaviyo |
| Developer | `apis/developer.md` | github, gitlab, bitbucket, vercel, netlify, railway, render, fly, digitalocean, cloudflare |
| Database | `apis/database.md` | supabase, firebase, planetscale, neon, upstash, mongodb, fauna, xata, convex, appwrite |
| Auth | `apis/auth-providers.md` | clerk, auth0, workos, stytch |
| Media | `apis/media.md` | cloudinary, mux, bunny, imgix, uploadthing, uploadcare, vimeo, youtube, spotify, unsplash |
| Social | `apis/social.md` | twitter, linkedin, instagram, tiktok, pinterest, reddit, twitch |
| Productivity | `apis/productivity.md` | notion, airtable, google-sheets, google-drive, google-calendar, linear, jira, asana, trello, figma |
| Business | `apis/business.md` | shopify, docusign, hellosign, bitly, dub |
| Geo | `apis/geo.md` | openweather, mapbox, google-maps |
| Support | `apis/support.md` | intercom, zendesk, freshdesk, helpscout |
| Analytics | `apis/analytics.md` | mixpanel, amplitude, posthog, segment, sentry, datadog, algolia |

## 参考文件

| 文件 | 用途 |
| --- | --- |
| `setup.md` | 使用指南与首次配置 |
| `credentials.md` | 多账户凭证命名规范 `{SERVICE}_{ACCOUNT}_{TYPE}` |
| `auth.md` | 认证模式详解（API Key / OAuth2 / Bearer / Basic） |
| `pagination.md` | 分页模式（cursor / offset / page） |
| `resilience.md` | 错误处理与重试模式 |
| `webhooks.md` | Webhook 签名验证与重试策略 |

## 核心能力
1. **先定位文件** — 用 API 分类索引表找到服务所属类别文件
2. **先读索引再跳转** — 每个文件顶部有索引表,标注服务名与行号,按行号读取对应段落
3. **必带 Content-Type** — POST/PUT/PATCH 请求需 `Content-Type: application/json`
4. **处理速率限制** — 检查 `X-RateLimit-Remaining` 响应头,429 时实现指数退避
5. **校验响应体** — 部分API返回 HTTP 200 但 body 含错误,需检查响应结构
6. **使用幂等键** — 支付与关键操作使用 `Idempotency-Key` 头防止重复

## 使用流程

### Step 1: 定位服务类别
根据用户提到的服务名,查阅 API 分类索引表,找到对应的 `apis/*.md` 文件。

### Step 2: 读取文件索引
```bash
# 读取 AI/ML 分类文件索引
head -20 apis/ai-ml.md
```

### Step 3: 跳转到目标服务段落
```bash
# 按索引行号读取 openai 段落（示例行号 119-230）
sed -n '119,230p' apis/ai-ml.md
```

### Step 4: 提取关键信息
- 认证方式（API Key / OAuth2 / Bearer）
- 端点路径与 HTTP 方法
- 必需参数与可选参数
- 速率限制与分页策略
- 常见陷阱与注意事项

### Step 5: 生成集成建议
基于文档内容,为用户提供含 curl 示例的集成方案,并标注常见错误。

#
## 案例展示

### 案例1: Stripe 支付集成参考
**场景**: 开发者需要集成 Stripe 支付 API

```bash
# 读取 Payments 分类索引
head -20 apis/payments.md
# 跳转到 stripe 段落
sed -n '45,120p' apis/payments.md
```

**提取信息**:
- 认证: Bearer Token（`Authorization: Bearer sk_live_xxx`）
- 端点: `POST /v1/charges` 创建收款
- 幂等键: `Idempotency-Key` 头防止重复扣款
- 速率限制: 100 读/秒, 100 写/秒
- 分页: cursor 模式, `starting_after` 参数

**集成建议**:
```bash
curl https://api.stripe.com/v1/charges \
  -H "Authorization: Bearer sk_live_xxx" \
  -H "Idempotency-Key: 6f68e0ed-5b5f-4d0d-8e3c-a6b3c7e9f1a2" \
  -d amount=2000 \
  -d currency=usd \
  -d source=tok_visa
```

**说明**: 支付操作必须使用 `Idempotency-Key` 头,网络重试时不会重复扣款。

### 案例2: OpenAI API 集成参考
**场景**: 开发者需要调用 OpenAI Chat Completions

```bash
head -20 apis/ai-ml.md
sed -n '119,230p' apis/ai-ml.md
```

**提取信息**:
- 认证: Bearer Token（`Authorization: Bearer sk-xxx`）
- 端点: `POST /v1/chat/completions`
- 必需头: `Content-Type: application/json`
- 速率限制: `X-RateLimit-Remaining` 头,429 时指数退避
- 分页: 无（流式响应）

**集成建议**:
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer sk-xxx" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4","messages":[{"role":"user","content":"Hello"}]}'
```

### 案例3: Slack Webhook 处理参考
**场景**: 开发者需要处理 Slack 事件 Webhook

```bash
head -20 apis/communication.md
sed -n '180,250p' apis/communication.md
```

**提取信息**:
- 签名验证: `X-Slack-Signature` 与 `X-Slack-Request-Timestamp` 头
- 重试: Slack 在 3 秒内未收到 200 会重试,最多 3 次
- 事件类型: `message`, `reaction_added`, `team_join` 等

## 错误处理


| 错误场景 | 原因分析 | 处理方式 |
|---------|---------|---------|
| 缺少 `Content-Type` | POST 请求未设 `Content-Type: application/json` | 所有 POST/PUT/PATCH 必带该头,否则返回 415 或 400 |
| API Key 暴露在 URL | 将密钥放在查询参数 `?api_key=xxx` | 改用请求头 `Authorization: Bearer xxx`,避免日志泄露 |
| 忽略分页 | 未处理 `cursor` / `next_page_token` | 默认返回 10-25 项,需循环分页获取完整数据 |
| 无 429 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令逻辑 | 收到 429 直接报错 | 检查 `X-RateLimit-Remaining`,429 时指数退避（2s/4s/8s） |
| HTTP 200 含错误 | 仅检查状态码,未校验 body | 部分API返回 200 但 body 含 `error` 字段,需检查响应结构 |
| 幂等键缺失 | 支付操作无 `Idempotency-Key` | 网络执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令导致重复扣款,支付类操作必带幂等键 |
| OAuth Token 过期 | 使用过期 `access_token` | 使用 `refresh_token` 刷新,或重新走 OAuth 流程 |

## 常见问题

### Q1: 147 个服务都覆盖了哪些类别?
A: 覆盖 16 大类: AI/ML（14 服务）、Payments（13）、Communication（10）、Realtime（8）、CRM（8）、Marketing（7）、Developer（17）、Database（10）、Auth（4）、Media（14）、Social（7）、Productivity（17）、Business（5）、Geo（3）、Support（4）、Analytics（7）。

### Q2: 文档中包含 curl 示例吗?
A: 是的,每个服务的端点参考都包含 curl 示例,含认证头、请求体与预期响应结构。示例仅供参考,用户需自行替换 API Key 与参数。

### Q3: 如何快速找到某个服务的文档?
A: 先确定服务所属类别（如 Stripe 属于 Payments）,打开对应 `apis/payments.md`,读取顶部索引表找到行号,按行号跳转读取该服务段落（通常 50-100 行）。

### Q4: 多账户场景如何管理凭证?
A: 参考 `credentials.md` 的命名规范: `{SERVICE}_{ACCOUNT}_{TYPE}`。例如 `STRIPE_PRODUCTION_SECRET`、`OPENAI_DEV_API_KEY`,便于环境变量管理与多账户隔离。

### Q5: 文档会代我执行 API 请求吗?
A: 不会。本技能是纯文档参考,提供端点、认证、参数与示例。用户自行管理 API Key 并执行请求。技能不存储、不代理、不代发任何 API 调用。

### Q6: Webhook 签名验证怎么做?
A: 参考 `webhooks.md`,不同服务签名方式不同。如 Slack 使用 `X-Slack-Signature` HMAC-SHA256,Stripe 使用 `Stripe-Signature` 头含时间戳与签名。文档提供各服务的验证代码示例。

## 已知限制

1. **纯文档参考**: 不代用户执行 API 请求,不管理 API Key,不代理调用
2. **服务覆盖范围**: 覆盖 147 个主流服务,非 exhaustive,小众服务可能未收录
3. **不替代官方文档**: 建议结合各服务官方 API 文档使用,官方文档更新更及时
4. **不含 SDK 示例**: 以 curl 示例为主,不提供各语言 SDK 的完整代码
5. **凭证安全**: 文档中不存储任何真实 API Key,示例中使用占位符
6. **版本时效**: API 版本可能更新,使用前建议核对官方最新文档
