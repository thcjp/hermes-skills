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
  security hardening。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Security
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
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

- Configure, optimize, and troubleshoot CDN deployments with caching strategies,
  security hardening
- 触发关键词: deployments, configure, cdn, optimize, troubleshoot

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

### Q1: 如何开始使用CDN？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: CDN有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
