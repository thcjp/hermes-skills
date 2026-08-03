---
slug: security-audit
name: security-audit
version: "1.0.0"
displayName: Security Audit
summary: "Clawdbot部署全面安全审计,扫描暴露凭证、开放端口、配置漏洞,加固系统安全"
  credentials, open por...
license: MIT
description: |-
  Comprehensive security auditing for Clawdbot deployments。Scans for
  exposed credentials, open por。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Security
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Security Audit

## When to use

Run a security audit to identify vulnerabilities in your Clawdbot setup before deployment or on a schedule. Use auto-fix to remediate common issues automatically.

## Setup

No external dependencies required. Uses native system tools where available.

## How to

### Quick audit (common issues)

```bash
node skills/security-audit/scripts/audit.cjs
```

### Full audit (comprehensive scan)

```bash
node skills/security-audit/scripts/audit.cjs --full
```

### Auto-fix common issues

```bash
node skills/security-audit/scripts/audit.cjs --fix
```

### Audit specific areas

```bash
node skills/security-audit/scripts/audit.cjs --credentials      # Check for exposed API keys
node skills/security-audit/scripts/audit.cjs --ports            # Scan for open ports
node skills/security-audit/scripts/audit.cjs --configs          # Validate configuration
node skills/security-audit/scripts/audit.cjs --permissions      # Check file permissions
node skills/security-audit/scripts/audit.cjs --docker           # Docker security checks
```

### Generate report

```bash
node skills/security-audit/scripts/audit.cjs --full --json > audit-report.json
```

## Output

The audit produces a report with:

| Level | Description |
| --- | --- |
| 🔴 CRITICAL | Immediate action required (exposed credentials) |
| 🟠 HIGH | Significant risk, fix soon |
| 🟡 MEDIUM | Moderate concern |
| 🟢 INFO | FYI, no action needed |

## Checks Performed

### Credentials

* API keys in environment files
* Tokens in command history
* Hardcoded secrets in code
* Weak password patterns

### Ports

* Unexpected open ports
* Services exposed to internet
* Missing firewall rules

### Configs

* Missing rate limiting
* Disabled authentication
* Default credentials
* Open CORS policies

### Files

* World-readable files
* Executable by anyone
* Sensitive files in public dirs

### Docker

* Privileged containers
* Missing resource limits
* Root user in container

## Auto-Fix

The `--fix` option automatically:

* Sets restrictive file permissions (600 on .env)
* Secures sensitive configuration files
* Creates .gitignore if missing
* Enables basic security headers

## Related skills

* `security-monitor` - Real-time monitoring (available separately)

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

- Comprehensive security auditing for Clawdbot deployments
- Scans for
  exposed credentials, open por
- 触发关键词: deployments, comprehensive, auditing, clawdbot, audit, security

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

### Q1: 如何开始使用Security Audit？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Security Audit有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
