---
slug: afrexai-cybersecurity-engine
name: afrexai-cybersecurity-engine
version: "1.0.0"
displayName: Cybersecurity Engine
summary: Complete cybersecurity assessment, threat modeling, and hardening system.
  Use when conducting sec...
license: MIT
description: |-
  Complete cybersecurity assessment, threat modeling, and hardening system。Use when conducting sec。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Security
tools:
  - - read
- exec
# Cybersecurity Engine
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

Complete methodology for security assessment, threat modeling, vulnerability management, incident response, and security program design. No tools required — pure agent knowledge that works with any codebase, infrastructure, or organization.

## Phase 1: Security Posture Assessment

### Quick Health Check (5 minutes)
> 详细内容已移至 `references/detail.md`

### Full Assessment Brief

## Phase 2: Threat Modeling (STRIDE+)

### Step 1 — Decompose the System
> 详细内容已移至 `references/detail.md`

### Step 2 — STRIDE Analysis Per Component
For EACH component crossing a trust boundary:

| Threat | Question | Example Attack |
| --- | --- | --- |
| **S**poofing | Can an attacker pretend to be someone else? | Stolen JWT, session hijacking, credential stuffing |
| **T**ampering | Can data be modified in transit or at rest? | Man-in-the-middle, SQL injection, parameter manipulation |
| **R**epudiation | Can someone deny they did something? | Missing audit logs, unsigned transactions |
| **I**nformation Disclosure | Can sensitive data leak? | Error messages, API over-fetching, side channels |
| **D**enial of Service | Can the service be overwhelmed? | DDoS, resource exhaustion, regex DoS |
| **E**levation of Privilege | Can someone gain unauthorized access? | IDOR, broken access control, privilege escalation |

### Step 3 — Threat Register

### Priority Rules
* **P0** (risk ≥ 20): Fix immediately, stop other work
* **P1** (risk 12-19): Fix within 1 week
* **P2** (risk 6-11): Fix within 1 sprint
* **P3** (risk ≤ 5): Track, fix when convenient

## Phase 3: Application Security (OWASP Top 10 + Beyond)

### A01: Broken Access Control
> 详细内容已移至 `references/detail.md`

### A02: Cryptographic Failures
**Decision tree:**

### A03: Injection
> 详细内容已移至 `references/detail.md`

### A04: Insecure Design
**Secure design checklist:**

* Business logic abuse scenarios documented
* Rate limiting on expensive operations
* Fail-safe defaults (deny by default)
* Separation of duties for critical operations
* Multi-step transactions use CSRF tokens
* API pagination has max limit
* File uploads have size limits AND type validation (magic bytes, not extension)
* Background job payloads are signed/validated

### A05: Security Misconfiguration
**Server hardening checklist:**

### A06-A10 Quick Checks
| Vuln | Test | Fix |
| --- | --- | --- |
| A06: Vulnerable Components | `npm audit`, `pip-audit`, `trivy fs .` | Update, pin versions, automate scanning in CI |
| A07: Auth Failures | Brute force test, password policy audit, MFA coverage | Rate limit + lockout, enforce MFA, bcrypt/Argon2 |
| A08: Data Integrity | Can unsigned data modify app behavior? | Sign all serialized data, verify checksums, SRI for CDN |
| A09: Logging Gaps | Do you log auth events, access changes, failures? | Structured logging, SIEM integration, alert on anomalies |
| A10: SSRF | Can user input trigger server-side requests? | Allowlist URLs, block internal IPs, no redirects to internal |

## Phase 4: Infrastructure Security
### Network Security Baseline

### Container Security

### Cloud Security (AWS/GCP/Azure Universal)

## Phase 5: Vulnerability Management Program
### Vulnerability Lifecycle
```text
Discovery → Triage → Prioritize → Remediate → Verify → Close
    ↓          ↓         ↓            ↓          ↓
  Scan/     Confirm   CVSS +       Fix or     Retest
  Report    real?     context      compensate
```

### Severity SLA
| Severity | CVSS | Remediation SLA | Escalation |
| --- | --- | --- | --- |
| Critical | 9.0-10.0 | 24 hours | CTO/CISO immediately |
| High | 7.0-8.9 | 7 days | Team lead + security |
| Medium | 4.0-6.9 | 30 days | Sprint backlog |
| Low | 0.1-3.9 | 90 days | Track, fix when convenient |
| Info | 0 | No SLA | Document for awareness |

### Vulnerability Report Template

### Scanning Schedule
| Scan Type | Frequency | Tool Examples |
| --- | --- | --- |
| Dependency scan | Every CI build | npm audit, pip-audit, trivy |
| SAST (code) | Every PR | Semgrep, CodeQL, Bandit |
| Secret scanning | Every commit | GitLeaks, truffleHog, GitHub secret scanning |
| Container scan | Every image build | Trivy, Grype, Snyk Container |
| DAST (runtime) | Weekly | OWASP ZAP, Burp Suite, Nuclei |
| Cloud config | Daily | ScoutSuite, Prowler, CloudSploit |
| Penetration test | Quarterly | Manual + automated |
| Red team | Annually | External firm |

## Phase 6: Incident Response
### Incident Severity Levels
| Level | Definition | Response Time | Team |
| --- | --- | --- | --- |
| SEV-1 | Active breach, data exfiltration, service down | 15 min | All hands + management + legal |
| SEV-2 | Vulnerability actively exploited, partial compromise | 1 hour | Security + affected team leads |
| SEV-3 | Suspicious activity, potential compromise indicators | 4 hours | Security team |
| SEV-4 | Low-risk finding, policy violation, failed attack | Next business day | Assigned engineer |

### Communication Templates
> 详细内容已移至 `references/detail.md`

## Phase 7: Security Headers & Browser Security
### Required HTTP Headers
```text
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Resource-Policy: same-origin
X-XSS-Protection: 0  # Disabled — CSP handles this; old header can cause issues
```

### Cookie Security
```text
Set-Cookie: session=<token>;
  Secure;                    # HTTPS only
  HttpOnly;                  # No JavaScript access
  SameSite=Lax;              # CSRF protection (Strict if no cross-site navigation needed)
  Path=/;                    # Scope appropriately
  Max-Age=3600;              # 1 hour (adjust per use case)
  Domain=.yourdomain.com;    # Explicit domain
```

## Phase 8: Authentication & Authorization Deep Dive
### Password Policy (NIST 800-63B aligned)

### JWT Security Checklist

### OAuth 2.0 / OIDC Checklist
* Use Authorization Code flow with PKCE (never Implicit)
* Validate `state` parameter to prevent CSRF
* Validate `nonce` for OIDC to prevent replay
* Validate token issuer and audience
* Store tokens server-side, not in browser
* Implement token rotation for refresh tokens
* Set minimal scopes (principle of least privilege)
* Register exact redirect URIs (no wildcards)

## Phase 9: Security Program Design

### Building a Security Program from Scratch
> 详细内容已移至 `references/detail.md`

### Security Metrics Dashboard

## Phase 10: Penetration Testing Methodology
### Reconnaissance

### Testing Phases
> 详细内容已移至 `references/detail.md`

### Penetration Test Report Template

## Phase 11: Supply Chain Security
### Dependency Security
> 详细代码示例已移至 `references/detail.md`

## Phase 12: Security Scoring Rubric
> 详细内容已移至 `references/detail.md`

## Common Mistakes
1. **Security through obscurity** — hiding admin panel at /secret-admin is not security
2. **Client-side only validation** — always validate server-side
3. **Trusting internal networks** — assume breach, verify everything
4. **Logging sensitive data** — passwords, tokens, PII in logs = breach waiting to happen
5. **"We're too small to be targeted"** — automated attacks don't check company size
6. **One-time audit mentality** — security is continuous, not a checkbox
7. **Ignoring security in dev/staging** — attackers find your staging environment too
8. **Over-permissioning for convenience** — least privilege, always
9. **No backup testing** — backups you haven't tested are hopes, not backups
10. **Treating compliance as security** — SOC 2 ≠ secure; it's a starting point

## Edge Cases
* **Startup with zero security:** Start with Phase 9 Quarter 1 — foundation first
* **Legacy application:** Focus on network segmentation + WAF + monitoring before code fixes
* **Microservices:** Service mesh for mTLS, centralized auth (OAuth/OIDC), API gateway
* **IoT/embedded:** Assume physical access, encrypt firmware, signed updates, minimal attack surface
* **Mobile apps:** Certificate pinning, root/jailbreak detection, binary protection, secure local storage
* **Serverless:** Function-level IAM, no secrets in code, API Gateway throttling, cold start timing attacks
* **Multi-tenant SaaS:** Tenant isolation verification, noisy neighbor prevention, cross-tenant data leak testing

## Natural Language Commands
```text
"Audit security of [project/repo]" → Full assessment (Phase 1-4)
"Threat model [system/feature]" → STRIDE analysis (Phase 2)
"Check OWASP top 10 for [app]" → Application security review (Phase 3)
"Harden [server/container/cloud]" → Infrastructure checklist (Phase 4)
"Create incident response plan" → IR playbook (Phase 6)
"Design security program" → Phased program build (Phase 9)
"Pentest methodology for [target]" → Testing phases (Phase 10)
"Score security of [system]" → 100-point rubric (Phase 12)
"Review auth implementation" → Auth deep dive (Phase 8)
"Check security headers" → Header audit (Phase 7)
"Vulnerability report for [finding]" → Report template (Phase 5)
"Supply chain security review" → Dependency audit (Phase 11)
```

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
- Complete cybersecurity assessment, threat modeling, and hardening system
- Use when conducting sec
- 触发关键词: assessment, engine, threat, complete, cybersecurity, modeling, afrexai

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
### Q1: 如何开始使用Cybersecurity Engine？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Cybersecurity Engine有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 性能取决于底层模型能力
