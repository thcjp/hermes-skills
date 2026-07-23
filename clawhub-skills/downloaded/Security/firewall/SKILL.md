---
slug: firewall
name: firewall
version: "1.0.0"
displayName: Firewall
summary: "在服务器与云服务商上配置防火墙,遵循安全最佳实践,构建网络边界防护"
license: MIT
description: |-
  Configure firewalls on servers and cloud providers with security best
  practices。核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配Skill...
tags:
- Security
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Firewall

## Critical First Steps

* Allow SSH/remote access before enabling any firewall — enabling first locks you out
* Test access in a second session before closing the first — verify the rule actually works
* Know how to access provider console — it's the only way back if locked out

## Default Stance

* Default deny all incoming traffic — only open what you explicitly need
* Default allow outgoing traffic — most apps need to reach the internet
* Every open port is attack surface — question each one before adding

## Essential Ports

* SSH (22 or custom): Always needed for remote access — consider limiting to your IP only
* HTTP (80): Only if serving web traffic — also needed for Let's Encrypt HTTP challenge
* HTTPS (443): For production web services
* Don't open database ports (3306, 5432, 27017) to the internet — access via SSH tunnel or private network

## Provider Firewalls (Hetzner, DigitalOcean, AWS, etc.)

* Provider firewall applies before traffic reaches your server — faster, less server load
* Changes usually apply immediately — no reload command needed
* Stateful by default — allow inbound, responses automatically allowed outbound
* Apply to server groups for consistency — easier than per-server rules
* Provider firewall + OS firewall = defense in depth — use both when possible

## IP Restrictions

* Limit SSH to known IPs when possible — dramatically reduces attack surface
* Your home IP may change — use a VPN with static IP or update rules when it changes
* Allow IP ranges with CIDR notation — /32 is single IP, /24 is 256 IPs
* Some providers support dynamic DNS in rules — check before building complex solutions

## Common Services to Consider

* VPN (WireGuard: 51820/UDP, OpenVPN: 1194) — allows secure access without exposing other ports
* Mail (25, 465, 587) — only if running mail server
* DNS (53 TCP/UDP) — only if running DNS server
* Monitoring agents may need outbound access to specific IPs

## Docker Warning

* Docker bypasses most OS firewalls by default — containers expose ports regardless of UFW/iptables
* Solution: bind containers to localhost only and use reverse proxy for public access
* Or configure Docker to respect firewall rules — requires additional setup
* Provider-level firewalls still work — they block before traffic reaches Docker

## IPv6

* Firewalls often have separate IPv4 and IPv6 rules — configure both
* Provider firewalls may handle both together — check their documentation
* Attackers probe IPv6 when IPv4 is locked down — don't neglect it

## Debugging

* Test from outside your network — rules may look correct but not work
* Provider dashboards often show blocked traffic logs
* "Connection refused" = port closed properly; "Connection timeout" = firewall dropping silently
* Online port scanners verify what's actually open from the internet

## Common Mistakes

* Opening ports "temporarily" and forgetting to close them
* Opening 80/443 when no web server runs — unnecessary exposure
* Forgetting UDP for services that need it — DNS, VPN, game servers
* Assuming firewall is active — verify it's actually running/applied
* Only configuring IPv4 — leaving IPv6 wide open
* Trusting "security through obscurity" — non-standard ports slow attackers, don't stop them

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

- Configure firewalls on servers and cloud providers with security best
  practices
- 触发关键词: firewalls, servers, providers, configure, firewall, cloud

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

### Q1: 如何开始使用Firewall？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Firewall有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 依赖云服务，需要网络连接
