---
slug: ssl
name: ssl
version: "1.0.2"
displayName: SSL
summary: "配HTTPS/管TLS证书/调安全连接问题(社区下载版)"
license: MIT
description: |-
  Set up HTTPS, manage TLS certificates, and debug secure connection issues。核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---


# SSL

## Triggers

Activate on: SSL certificate, HTTPS setup, Let's Encrypt, certbot, TLS configuration, certificate expired, mixed content, certificate chain error.

## Core Tasks

| Task | Tool/Method |
| --- | --- |
| Get free cert | `certbot`, acme.sh, Caddy (auto) |
| Check cert status | `openssl s_client -connect host:443` |
| View cert details | `openssl x509 -in cert.pem -text -noout` |
| Test config | ssllabs.com/ssltest or `testssl.sh` |
| Convert formats | See `formats.md` |

## Quick Cert Commands

```bash
certbot certonly --nginx -d example.com -d www.example.com

echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates

openssl s_client -connect example.com:443 -servername example.com
```

## Common Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `certificate has expired` | Cert past valid date | Renew with certbot renew |
| `unable to verify` / `self signed` | Missing intermediate cert | Include full chain in config |
| `hostname mismatch` | Cert doesn't cover this domain | Get cert for correct domain or add SAN |
| `mixed content` | HTTP resources on HTTPS page | Change all URLs to HTTPS or use `//` |
| `ERR_CERT_AUTHORITY_INVALID` | Self-signed or untrusted CA | Use Let's Encrypt or install CA cert |

For detailed troubleshooting steps, see `troubleshooting.md`.

## Server Config Patterns

**Nginx:**

nginx

```
server {
    listen 443 ssl http2;
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
}
```

**Apache:**

apache

```
SSLEngine on
SSLCertificateFile /path/to/cert.pem
SSLCertificateKeyFile /path/to/privkey.pem
SSLCertificateChainFile /path/to/chain.pem
```

For Node.js, Caddy, Traefik, and HAProxy, see `servers.md`.

## Renewal

Let's Encrypt certs expire in 90 days. Always automate:

```bash
certbot renew --dry-run

0 0 * * * certbot renew --quiet
```

## Certificate Types

| Type | Use case |
| --- | --- |
| Single domain | One site (example.com) |
| Wildcard (*.domain.com) | All subdomains |
| Multi-domain (SAN) | Multiple different domains on one cert |
| Self-signed | Local dev only — browsers will warn |

## What This Doesn't Cover

* Application auth (JWT, OAuth) → see `oauth` skill
* SSH keys → see `linux` or server skills
* VPN/tunnel setup → see networking skills
* Firewall configuration → see server/infrastructure skills

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

- Set up HTTPS, manage TLS certificates, and debug secure connection issues
- 触发关键词: certificates, debug, secure, manage, ssl, https

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

### Q1: 如何开始使用SSL？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: SSL有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
