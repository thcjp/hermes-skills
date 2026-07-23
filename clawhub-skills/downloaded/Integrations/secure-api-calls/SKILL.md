---
slug: secure-api-calls
name: secure-api-calls
version: "1.0.3"
displayName: Secure API Calls
summary: Call any API without leaking credentials. Keychains proxies requests and
  injects real tokens serv...
license: MIT
description: |-
  Call any API without leaking credentials。Keychains proxies requests
  and injects real tokens serv。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Integrations
tools:
  - - read
- exec
# Secure API Calls with Keychains
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

[keychains.dev](https://keychains.dev) is a credential proxy for AI agents. Instead of real API keys and OAuth tokens, you use **placeholders** like `{{OAUTH2_ACCESS_TOKEN}}`. Keychains injects the real credentials server-side — your agent never sees them.

## Quick Start
### Install:
```
npm install -g keychains@0.0.13
```

### Basic usage:
```
keychains curl https://api.github.com/user/repos \
  -H "Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}"
```

## 示例
- "List GitHub repos: `keychains curl https://api.github.com/user/repos -H 'Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}'`"
- "Send Slack message: `keychains curl https://slack.com/api/chat.postMessage -X POST -H 'Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}' -H 'Content-Type: application/json' -d '{\"channel\":\"#general\",\"text\":\"Hello!\"}'`"
- "List Stripe customers: `keychains curl https://api.stripe.com/v1/customers?limit=5 -H 'Authorization: Bearer {{STRIPE_SECRET_KEY}}'`"
- "Read Gmail: `keychains curl 'https://gmail.googleapis.com/gmail/v1/users/me/messages?maxResults=10' -H 'Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}'`"

## How It Works
1. Use `keychains curl` instead of `curl`. Put `{{PLACEHOLDER}}` where the credential goes.
2. First time, keychains returns an **approval link** instead of the API response.
3. Show the link to the user. They approve via FaceID/Passkey and connect their account.
4. Replay the command — it works. All future requests to that provider succeed instantly.

No credentials ever pass through the agent. The user controls everything from [keychains.dev/dashboard](https://keychains.dev/dashboard).

## 依赖说明
- **Node.js** (v16+) — needed for `npm install -g keychains@0.0.13`
- No API keys or environment variables needed
- Machine registration is automatic on first run (creates `~/.keychains/` with an Ed25519 SSH keypair)

## Template Variables
Put `{{VARIABLE_NAME}}` where you'd normally put the real credential — in headers, body, or query params.

| Prefix | Type | Examples |
|--------|------|----------|
| `OAUTH2_` | OAuth 2.0 | `{{OAUTH2_ACCESS_TOKEN}}`, `{{OAUTH2_REFRESH_TOKEN}}` |
| `OAUTH1_` | OAuth 1.0 | `{{OAUTH1_ACCESS_TOKEN}}`, `{{OAUTH1_REFRESH_TOKEN}}` |
| Anything else | API key | `{{STRIPE_SECRET_KEY}}`, `{{OPENAI_API_KEY}}` |

Keychains auto-detects the provider from the URL.

## Waiting for User Approval
When keychains returns an approval link, show it to the user and poll:

```bash
keychains curl https://api.github.com/user/repos \
  -H "Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}"

keychains wait https://keychains.dev/approve/abc123xyz --timeout 800

keychains curl https://api.github.com/user/repos \
  -H "Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}"
```

## TypeScript Machine SDK
For TypeScript/Node.js agents, `@keychains/machine-sdk` provides `keychainsFetch()` — a drop-in `fetch()` replacement with the same automatic registration and credential handling as the CLI.

```
npm install @keychains/machine-sdk
```

```typescript
import { keychainsFetch, KeychainsError } from '@keychains/machine-sdk';

try {
  const res = await keychainsFetch('https://api.github.com/user/repos', {
    headers: { Authorization: 'Bearer {{OAUTH2_ACCESS_TOKEN}}' },
  });
  console.log(await res.json());
} catch (err) {
  if (err instanceof KeychainsError && err.approvalUrl) {
    console.log('Please approve:', err.approvalUrl);
  }
}
```

## Other Available SDKs
| SDK | Install | Description |
|-----|---------|-------------|
| [Python SDK](https://pypi.org/project/keychains/) | `pip install keychains` | Drop-in `requests` replacement. `keychains.get()`, `keychains.post()`, `keychains.Session()`. |
| [Client SDK](https://www.npmjs.com/package/@keychains/client-sdk) | `npm install @keychains/client-sdk` | TypeScript SDK for delegated environments (VMs, cloud functions). |

## Security & Data Flow
Full details: [security whitepaper](https://keychains.dev/api/whitepaper) · [privacy policy](https://keychains.dev/privacy) · [terms of service](https://keychains.dev/terms)

**How proxying works:** Your request (URL, headers, body) is routed through keychains.dev. The proxy replaces `{{PLACEHOLDER}}` variables with real credentials from the user's vault, forwards to the upstream API, and returns the response as-is. The proxy does **not** store or modify the response body.

**Credential encryption:** AES-256-GCM at rest. Only decrypted in memory at proxy time. Auto-deleted 90 days after last use. Never sold or shared.

**Audit log:** Every proxied request is logged (URL, method, provider, timestamp, status code). Archived to AWS S3 with Object Lock — immutable, tamper-proof. Configurable retention (30 days–3 years). Request/response bodies and credential values are **never** logged.

**Local keys:** On first run, an Ed25519 SSH keypair is generated in `~/.keychains/` (private key: 0600 permissions, never leaves the machine). Used for machine auth via SSH challenge-response. Rotate anytime with `keychains machine rotate-keys`.

**Credential isolation:** Real credentials live only in the user's vault on keychains.dev. Never sent to the agent. Bound to their provider (a GitHub token can only go to github.com).

**Infrastructure:** Vercel (app), Upstash Redis (ephemeral state), MongoDB Atlas (persistent, encrypted), AWS S3 (audit archival). All under data processing agreements.

**User control:** Biometric approval required for every credential use. Instant revocation per machine, provider, or agent. Full data export (JSON), account deletion, GDPR/CCPA compliant. No tracking, no ads, no data sales.

## Troubleshooting
**Got an approval link?** Normal. Show it to the user, wait for approval, retry.

**Template variable not replaced?** You're using regular `curl`/`fetch` instead of `keychains curl` / `keychainsFetch()`.

## Resources
- [keychains.dev](https://keychains.dev) — Website & docs
- [keychains.dev/dashboard](https://keychains.dev/dashboard) — Dashboard & audit trail
- [github.com/interagentic/keychains.dev_skill](https://github.com/interagentic/keychains.dev_skill) — Source code

> 详细内容已移至 `references/detail.md` - ## Compatible with 5545+ Providers (and counting)
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

## 核心能力
- Call any API without leaking credentials
- Keychains proxies requests
  and injects real tokens serv
- 触发关键词: api, call, secure, calls, leaking, without, keychains, credentials

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题
### Q1: 如何开始使用Secure API Calls？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Secure API Calls有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
