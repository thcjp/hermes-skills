---
slug: vpn
name: vpn
version: "1.0.0"
displayName: VPN
summary: Configure and troubleshoot VPN connections for privacy and remote access.
license: MIT
description: |-
  Configure and troubleshoot VPN connections for privacy and remote access.

  核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: privacy, configure, remote, vpn, connections, troubleshoot
tags:
- Security
tools:
- read
- exec
---

# VPN

## Privacy Misconceptions

* VPN shifts trust from ISP to VPN provider — provider sees all traffic, not eliminated
* "No logs" claims are marketing — unverifiable without independent audits
* VPN doesn't provide anonymity — browser fingerprinting, account logins, payment methods still identify
* Free VPNs monetize traffic data — if not paying, you're the product
* Self-hosted VPN exits from your IP — no privacy benefit, services see your home address

## DNS Leaks

* DNS queries can bypass tunnel — reveals visited sites despite encrypted traffic
* Test after every setup — leak test sites show if DNS goes through ISP instead of tunnel
* System DNS settings may override VPN — force DNS through tunnel in client settings

## Kill Switch

* Brief VPN disconnects expose real IP — happens without user noticing
* Kill switch blocks all traffic when tunnel drops — essential for privacy use cases
* Test by forcing disconnect — traffic should stop completely, not fall back to direct

## Split Tunneling Risks

* Misconfiguration sends sensitive traffic direct — defeats VPN purpose
* Full tunnel safer default — split only when deliberately excluding specific apps
* Local network access often requires split — printing, casting break with full tunnel

## Protocol Traps

* PPTP encryption is broken — trivially cracked, never use regardless of convenience
* UDP blocked on some networks — TCP fallback needed for restrictive firewalls
* WireGuard uses fixed ports — easier to block than OpenVPN on 443

## Mobile Issues

* WiFi calling fails through most VPNs — carrier limitation, not fixable
* Banking apps detect and block VPN — may need exclusion in split tunnel
* Battery drain varies significantly — WireGuard most efficient by large margin

## Connection Failures

* "Connected" but no internet — usually DNS misconfigured, not routing issue
* Works on phone not laptop — local firewall or antivirus interfering
* Constant reconnects — try TCP instead of UDP, increase keepalive interval

## Self-Hosted Traps

* Exit IP is your home IP — services see where you live, no geo-bypass benefit
* Requires static IP or dynamic DNS — clients can't find changing endpoints
* Unmaintained server becomes liability — security updates are your responsibility

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
