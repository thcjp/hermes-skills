---
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
summary: "REST API参考文档,147服务含认证端点与坑"
---
# Publish Api

REST API reference documentation. 147 services with authentication, endpoints, and gotchas.

## Setup

On first use, read `setup.md` for usage guidelines.

## When to Use

User asks about integrating a third-party API. This skill provides:

* Authentication documentation
* Endpoint reference with curl examples
* Rate limits and pagination patterns
* Common mistakes to avoid

## Architecture

```text
apis/                    # API reference files by category
  ├── ai-ml.md           # OpenAI, Anthropic, Cohere, etc.
  ├── payments.md        # Stripe, PayPal, Square, etc.
  ├── communication.md   # Twilio, SendGrid, Slack, etc.
  └── ...

~/api/                   # User preferences (optional)
  └── preferences.md     # Preferred language for examples
```

## Quick Reference

| File | Purpose |
| --- | --- |
| `setup.md` | Usage guidelines |
| `credentials.md` | Multi-account credential naming (`{SERVICE}_{ACCOUNT}_{TYPE}`) |
| `auth.md` | Authentication patterns |
| `pagination.md` | Pagination patterns |
| `resilience.md` | Error handling patterns |
| `webhooks.md` | Webhook patterns |

## API Categories

| Category | File | Services |
| --- | --- | --- |
| AI/ML | `apis/ai-ml.md` | anthropic, openai, cohere, groq, mistral, perplexity, huggingface, replicate, stability, elevenlabs, deepgram, assemblyai, together, anyscale |
| Payments | `apis/payments.md` | stripe, paypal, square, plaid, chargebee, paddle, lemonsqueezy, recurly, wise, coinbase, binance, alpaca, polygon |
| Communication | `apis/communication.md` | twilio, sendgrid, mailgun, postmark, resend, mailchimp, slack, discord, telegram, zoom |
| Realtime | `apis/realtime.md` | sendbird, stream-chat, pusher, ably, onesignal, courier, knock, novu |
| CRM | `apis/crm.md` | salesforce, hubspot, pipedrive, attio, close, apollo, outreach, gong |
| Marketing | `apis/marketing.md` | drift, crisp, front, customer-io, braze, iterable, klaviyo |
| Developer | `apis/developer.md` | github, gitlab, bitbucket, vercel, netlify, railway, render, fly, digitalocean, heroku, cloudflare, circleci, pagerduty, launchdarkly, split, statsig |
| Database | `apis/database.md` | supabase, firebase, planetscale, neon, upstash, mongodb, fauna, xata, convex, appwrite |
| Auth | `apis/auth-providers.md` | clerk, auth0, workos, stytch |
| Media | `apis/media.md` | cloudinary, mux, bunny, imgix, uploadthing, uploadcare, transloadit, vimeo, youtube, spotify, unsplash, pexels, giphy, tenor |
| Social | `apis/social.md` | twitter, linkedin, instagram, tiktok, pinterest, reddit, twitch |
| Productivity | `apis/productivity.md` | notion, airtable, google-sheets, google-drive, google-calendar, dropbox, linear, jira, asana, trello, monday, clickup, figma, calendly, cal, loom, typeform |
| Business | `apis/business.md` | shopify, docusign, hellosign, bitly, dub |
| Geo | `apis/geo.md` | openweather, mapbox, google-maps |
| Support | `apis/support.md` | intercom, zendesk, freshdesk, helpscout |
| Analytics | `apis/analytics.md` | mixpanel, amplitude, posthog, segment, sentry, datadog, algolia |

## How to Navigate API Files

Each category file contains multiple APIs. Use the index at the top of each file:

1. **Read the index first** — Each file starts with an index table showing API names and line numbers
2. **Jump to specific API** — Use the line number to read only that section (50-100 lines each)
3. **Example:**

   bash

   ```
   # Read index
   head -20 apis/ai-ml.md
   # Read specific API section
   sed -n '119,230p' apis/ai-ml.md
   ```

## Core Rules

1. **Find the right file first** — Use the API Categories table to locate the service.
2. **Read the index, then jump** — Each file has an index. Read only the section you need.
3. **Include Content-Type** — POST/PUT/PATCH requests need `Content-Type: application/json`.
4. **Handle rate limits** — Check `X-RateLimit-Remaining` header. Implement backoff on 429.
5. **Validate responses** — Some APIs return 200 with error in body. Check response structure.
6. **Use idempotency keys** — For payments and critical operations.

## Common Mistakes

* Missing `Content-Type: application/json` on POST requests
* API keys in URL query params (use headers instead)
* Ignoring pagination (most APIs default to 10-25 items)
* No retry logic for 429/5xx errors
* Assuming HTTP 200 means success

## Scope

This skill is **documentation only**. It provides:

* API endpoint reference
* Authentication patterns
* Code examples for reference

The user manages their own API keys and runs commands themselves.

## External Endpoints

This skill documents external APIs. Example endpoints shown are for the respective service providers (Stripe, OpenAI, etc.).

## Related Skills

Install with `* 安装此Skill请参考SkillHub平台指南

* `http` — HTTP request patterns
* `webhook` — Webhook handling
* `json` — JSON processing

## Feedback

* If useful: `
* Stay updated: `

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

- REST API reference for 147 services
- Authentication patterns, endpoints,
  rate limits, and common
- 触发关键词: api, rest, patterns, publish, authentication, reference, services

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

### Q1: 如何开始使用Publish Api？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Publish Api有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
