---
slug: dns
name: dns
version: "1.0.0"
displayName: DNS
summary: Configure DNS records correctly with proper TTLs, email authentication, and
  migration strategies.
license: MIT
description: |-
  Configure DNS records correctly with proper TTLs, email authentication,
  and migration strategies。核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数...
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# DNS

## Pre-Migration TTL

* Lower TTL to 300s at least 48h before changing records—current TTL must expire first
* Check current cached TTL before planning: `dig +nocmd +noall +answer example.com`
* After migration stable 24h, raise TTL back to 3600-86400s
* Test with multiple resolvers: Google (8.8.8.8), Cloudflare (1.1.1.1), local ISP—they cache independently

## Email Authentication (All Three Required)

* SPF alone insufficient—DKIM and DMARC both needed for deliverability
* DMARC record: `_dmarc.example.com TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@example.com"`
* SPF must be single TXT record—multiple SPF records invalid; use `include:` for multiple sources
* SPF ending: `-all` (reject) or `~all` (soft fail)—never `+all` or `?all`
* Verify complete setup with mail-tester.com after configuration

## CAA Records

* Limits which Certificate Authorities can issue certs for domain—prevents unauthorized issuance
* Basic: `example.com. CAA 0 issue "letsencrypt.org"`
* Wildcard requires separate entry: `CAA 0 issuewild "letsencrypt.org"`
* Incident reporting: `CAA 0 iodef "mailto:security@example.com"`
* Without CAA, any CA can issue—set explicitly for security-conscious domains

## www Handling

* Configure both apex and www—or redirect one to other; leaving www unconfigured breaks links
* Pick canonical form and stick to it: www → apex OR apex → www
* HTTPS redirect requires cert for both variants before redirect works
* Test both URLs explicitly after setup

## Debugging Commands

* `dig +trace example.com`—full resolution chain from root; reveals where problem occurs
* `dig @ns1.provider.com example.com`—query authoritative nameserver directly, bypasses cache
* Compare authoritative vs cached response—mismatch indicates propagation in progress
* Check all relevant record types—A working doesn't mean AAAA, MX, or TXT are correct

## Cloudflare Proxy Behavior

* Orange cloud (proxied) hides origin IP—breaks SSH, mail, game servers; use grey cloud for non-HTTP
* Proxied records ignore your TTL setting—Cloudflare controls caching
* CNAME flattening at apex works in Cloudflare but causes confusion when migrating away
* Universal SSL only on proxied records—DNS-only requires origin certificate

## Wildcard Records

* `*.example.com` does not match apex `example.com`—both need explicit records
* Explicit subdomain record takes precedence over wildcard
* Wildcard SSL certificates require separate issuance—use DNS challenge with Let's Encrypt

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

- Configure DNS records correctly with proper TTLs, email authentication,
  and migration strategies
- 触发关键词: correctly, dns, records, proper, configure

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

### Q1: 如何开始使用DNS？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: DNS有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
