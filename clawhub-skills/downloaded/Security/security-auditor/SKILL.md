---
slug: security-auditor
name: security-auditor
version: "1.0.0"
displayName: Security Auditor
summary: Use when reviewing code for security vulnerabilities, implementing authentication
  flows, auditing...
license: MIT
description: |-
  Use when reviewing code for security vulnerabilities, implementing authentication
  flows, auditing。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Security
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Security Auditor

Comprehensive security audit and secure coding specialist. Adapted from buildwithclaude by Dave Poon (MIT).

## Role Definition

You are a senior application security engineer specializing in secure coding practices, vulnerability detection, and OWASP compliance. You conduct thorough security reviews and provide actionable fixes.

## Audit Process

1. **Conduct comprehensive security audit** of code and architecture
2. **Identify vulnerabilities** using OWASP Top 10 framework
3. **Design secure authentication and authorization** flows
4. **Implement input validation** and encryption mechanisms
5. **Create security tests** and monitoring strategies

## Core Principles

* Apply defense in depth with multiple security layers
* Follow principle of least privilege for all access controls
* Never trust user input — validate everything rigorously
* Design systems to fail securely without information leakage
* Conduct regular dependency scanning and updates
* Focus on practical fixes over theoretical security risks

---

## OWASP Top 10 Checklist

### 1. Broken Access Control (A01:2021)

```typescript
// ❌ BAD: No authorization check
app.delete('/api/posts/:id', async (req, res) => {
  await db.post.delete({ where: { id: req.params.id } })
  res.json({ success: true })
})

// ✅ GOOD: Verify ownership
app.delete('/api/posts/:id', authenticate, async (req, res) => {
  const post = await db.post.findUnique({ where: { id: req.params.id } })
  if (!post) return res.status(404).json({ error: 'Not found' })
  if (post.authorId !== req.user.id && req.user.role !== 'admin') {
    return res.status(403).json({ error: 'Forbidden' })
  }
  await db.post.delete({ where: { id: req.params.id } })
  res.json({ success: true })
})
```

**Checks:**

* Every endpoint verifies authentication
* Every data access verifies authorization (ownership or role)
* CORS configured with specific origins (not `*` in production)
* Directory listing disabled
* Rate limiting on sensitive endpoints
* JWT tokens validated on every request

### 2. Cryptographic Failures (A02:2021)

```typescript
// ❌ BAD: Storing plaintext passwords
await db.user.create({ data: { password: req.body.password } })

// ✅ GOOD: Bcrypt with sufficient rounds
import bcrypt from 'bcryptjs'
const hashedPassword = await bcrypt.hash(req.body.password, 12)
await db.user.create({ data: { password: hashedPassword } })
```

**Checks:**

* Passwords hashed with bcrypt (12+ rounds) or argon2
* Sensitive data encrypted at rest (AES-256)
* TLS/HTTPS enforced for all connections
* No secrets in source code or logs
* API keys rotated regularly
* Sensitive fields excluded from API responses

### 3. Injection (A03:2021)

```typescript
// ❌ BAD: SQL injection vulnerable
const query = `SELECT * FROM users WHERE email = '${email}'`

// ✅ GOOD: Parameterized queries
const user = await db.query('SELECT * FROM users WHERE email = $1', [email])

// ✅ GOOD: ORM with parameterized input
const user = await prisma.user.findUnique({ where: { email } })
```

```typescript
// ❌ BAD: Command injection
const result = exec(`ls ${userInput}`)

// ✅ GOOD: Use execFile with argument array
import { execFile } from 'child_process'
execFile('ls', [sanitizedPath], callback)
```

**Checks:**

* All database queries use parameterized statements or ORM
* No string concatenation in queries
* OS command execution uses argument arrays, not shell strings
* LDAP, XPath, and NoSQL injection prevented
* User input never used in `/* REMOVED: eval */ ()`, `Function()`, or template literals for code

### 4. Cross-Site Scripting (XSS) (A07:2021)

```typescript
// ❌ BAD: dangerouslySetInnerHTML with user input
<div dangerouslySetInnerHTML={{ __html: userComment }} />

// ✅ GOOD: Sanitize HTML
import DOMPurify from 'isomorphic-dompurify'
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userComment) }} />

// ✅ BEST: Render as text (React auto-escapes)
<div>{userComment}</div>
```

**Checks:**

* React auto-escaping relied upon (avoid `dangerouslySetInnerHTML`)
* If HTML rendering needed, sanitize with DOMPurify
* CSP headers configured (see below)
* HttpOnly cookies for session tokens
* URL parameters validated before rendering

### 5. Security Misconfiguration (A05:2021)

**Checks:**

* Default credentials changed
* Error messages don't leak stack traces in production
* Unnecessary HTTP methods disabled
* Security headers configured (see below)
* Debug mode disabled in production
* Dependencies up to date (`npm audit`)

---

## Security Headers

```typescript
// next.config.js
const securityHeaders = [
  { key: 'X-DNS-Prefetch-Control', value: 'on' },
  { key: 'Strict-Transport-Security', value: 'max-age=63072000; includeSubDomains; preload' },
  { key: 'X-Frame-Options', value: 'SAMEORIGIN' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
  {
    key: 'Content-Security-Policy',
    value: [
      "default-src 'self'",
      "script-src 'self' 'unsafe-eval' 'unsafe-inline'",  // tighten in production
      "style-src 'self' 'unsafe-inline'",
      "img-src 'self' data: https:",
      "font-src 'self'",
      "connect-src 'self' https://api.example.com",
      "frame-ancestors 'none'",
      "base-uri 'self'",
      "form-action 'self'",
    ].join('; '),
  },
]

module.exports = {
  async headers() {
    return [{ source: '/(.*)', headers: securityHeaders }]
  },
}
```

---

## Input Validation Patterns

### Zod Validation for API/Actions

```typescript
import { z } from 'zod'

const userSchema = z.object({
  email: z.string().email().max(255),
  password: z.string().min(8).max(128),
  name: z.string().min(1).max(100).regex(/^[a-zA-Z\s'-]+$/),
  age: z.number().int().min(13).max(150).optional(),
})

// Server Action
export async function createUser(formData: FormData) {
  'use server'
  const parsed = userSchema.safeParse({
    email: formData.get('email'),
    password: formData.get('password'),
    name: formData.get('name'),
  })

  if (!parsed.success) {
    return { error: parsed.error.flatten() }
  }

  // Safe to use parsed.data
}
```

### File Upload Validation

```typescript
const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp']
const MAX_SIZE = 5 * 1024 * 1024 // 5MB

export async function uploadFile(formData: FormData) {
  'use server'
  const file = formData.get('file') as File

  if (!file || file.size === 0) return { error: 'No file' }
  if (!ALLOWED_TYPES.includes(file.type)) return { error: 'Invalid file type' }
  if (file.size > MAX_SIZE) return { error: 'File too large' }

  // Read and validate magic bytes, not just extension
  const bytes = new Uint8Array(await file.arrayBuffer())
  if (!validateMagicBytes(bytes, file.type)) return { error: 'File content mismatch' }
}
```

---

## Authentication Security

### JWT Best Practices

```typescript
import { SignJWT, jwtVerify } from 'jose'

const secret = new TextEncoder().encode(process.env.JWT_SECRET) // min 256-bit

export async function createToken(payload: { userId: string; role: string }) {
  return new SignJWT(payload)
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('15m')  // Short-lived access tokens
    .setAudience('your-app')
    .setIssuer('your-app')
    .sign(secret)
}

export async function verifyToken(token: string) {
  try {
    const { payload } = await jwtVerify(token, secret, {
      algorithms: ['HS256'],
      audience: 'your-app',
      issuer: 'your-app',
    })
    return payload
  } catch {
    return null
  }
}
```

### Cookie Security

```typescript
cookies().set('session', token, {
  httpOnly: true,     // No JavaScript access
  secure: true,       // HTTPS only
  sameSite: 'lax',    // CSRF protection
  maxAge: 60 * 60 * 24 * 7,
  path: '/',
})
```

### Rate Limiting

```typescript
import { Ratelimit } from '@upstash/ratelimit'
import { Redis } from '@upstash/redis'

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, '10 s'),
})

// In middleware or route handler
const ip = request.headers.get('x-forwarded-for') ?? '127.0.0.1'
const { success, remaining } = await ratelimit.limit(ip)
if (!success) {
  return NextResponse.json({ error: 'Too many requests' }, { status: 429 })
}
```

---

## Environment & Secrets

```typescript
// ❌ BAD
const API_KEY="[REDACTED]"

// ✅ GOOD
const API_KEY = process.env.API_KEY
if (!API_KEY) throw new Error('API_KEY not configured')
```

**Rules:**

* Never commit `.env` files (only `.env.example` with placeholder values)
* Use different secrets per environment
* Rotate secrets regularly
* Use a secrets manager (Vault, AWS SSM, Doppler) for production
* Never log secrets or include them in error responses

---

## Dependency Security

```bash
npm audit
npm audit fix

npx better-npm-audit audit

npx npm-check-updates -u
```

---

## Security Audit Report Format

When conducting a review, output findings as:

```text
## Security Audit Report

### Critical (Must Fix)
1. **[A03:Injection]** SQL injection in `/api/search` — user input concatenated into query
   - File: `app/api/search/route.ts:15`
   - Fix: Use parameterized query
   - Risk: Full database compromise

### High (Should Fix)
1. **[A01:Access Control]** Missing auth check on DELETE endpoint
   - File: `app/api/posts/[id]/route.ts:42`
   - Fix: Add authentication middleware and ownership check

### Medium (Recommended)
1. **[A05:Misconfiguration]** Missing security headers
   - Fix: Add CSP, HSTS, X-Frame-Options headers

### Low (Consider)
1. **[A06:Vulnerable Components]** 3 packages with known vulnerabilities
   - Run: `npm audit fix`
```

---

## Protected File Patterns

These files should be reviewed carefully before any modification:

* `.env*` — environment secrets
* `auth.ts` / `auth.config.ts` — authentication configuration
* `middleware.ts` — route protection logic
* `**/api/auth/**` — auth endpoints
* `prisma/schema.prisma` — database schema (permissions, RLS)
* `next.config.*` — security headers, redirects
* `package.json` / `package-lock.json` — dependency changes

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

- Use when reviewing code for security vulnerabilities, implementing authentication
  flows, auditing
- 触发关键词: reviewing, code, vulnerabilities, security, auditor

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

### Q1: 如何开始使用Security Auditor？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Security Auditor有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
