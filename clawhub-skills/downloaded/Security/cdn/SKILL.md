---
slug: cdn
name: cdn
version: "1.0.1"
displayName: CDN
summary: Configure, optimize, and troubleshoot CDN deployments with caching strategies,
  security hardening...
license: MIT
description: |-
  Configure, optimize, and troubleshoot CDN deployments with caching strategies,
  security hardening...

  核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: deployments, configure, cdn, optimize, troubleshoot
tags:
- Security
tools:
- read
- exec
---

# CDN

## When to Use

User wants to set up, optimize, or debug a CDN. Covers provider selection, caching, security, and performance monitoring.

## Quick Reference

| Topic | File |
| --- | --- |
| Provider comparison & CLIs | `providers.md` |
| Security hardening | `security.md` |
| Caching strategies | `caching.md` |
| Troubleshooting | `troubleshooting.md` |

## Core Capabilities

1. **Provider selection** — Compare Cloudflare, CloudFront, Bunny, Fastly based on use case, traffic, budget
2. **Cache configuration** — Set optimal cache-control headers, TTLs, cache keys
3. **Security setup** — SSL/TLS, WAF rules, DDoS protection, origin shielding
4. **Performance monitoring** — Cache hit ratios, TTFB, regional latency
5. **Invalidation** — Purge strategies, CI/CD integration, tagged invalidation
6. **Cost optimization** — Bandwidth analysis, tier recommendations, multi-CDN strategies
7. **Troubleshooting** — Debug cache misses, stale content, origin overload

## Cache-Control Checklist

Before deploying, verify:

* Hashed assets (JS/CSS) → `Cache-Control: public, max-age=31536000, immutable`
* HTML pages → Short TTL or `no-cache` with revalidation
* Images → Long TTL with content-based URLs or versioning
* API responses → Usually `no-store` unless explicitly cacheable
* User-specific content → `private` or `no-store`

## Security Checklist

* TLS 1.2+ enforced, weak ciphers disabled
* HSTS enabled with appropriate max-age
* Origin IPs hidden, authenticated origin pulls configured
* Rate limiting on sensitive endpoints (login, API)
* Security headers: CSP, X-Frame-Options, X-Content-Type-Options

## Common Mistakes

* Caching user-specific responses (auth tokens, personalized content)
* Using `max-age` without `immutable` for versioned assets
* Purging entire cache instead of targeted paths
* Ignoring `Vary` headers (cache poisoning risk)
* Origin not rejecting direct access (bypassing CDN protections)

## Decision: Do I Need a CDN?

Ask about:

* Geographic distribution of users
* Current page load times and Core Web Vitals
* Static vs dynamic content ratio
* Traffic volume and patterns

If users are mostly local and traffic is low → CDN may add complexity without benefit.
If global users OR heavy static assets OR need DDoS protection → CDN adds value.

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
