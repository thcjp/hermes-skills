---
slug: security-audit
name: security-audit
version: "1.0.0"
displayName: Security Audit
summary: Comprehensive security auditing for Clawdbot deployments. Scans for exposed
  credentials, open por...
license: MIT
description: |-
  Comprehensive security auditing for Clawdbot deployments. Scans for
  exposed credentials, open por...

  核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: deployments, comprehensive, auditing, clawdbot, audit, security
tags:
- Security
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
