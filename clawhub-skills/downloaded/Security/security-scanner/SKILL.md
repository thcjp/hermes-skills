---
slug: security-scanner
name: security-scanner
version: "1.0.0"
displayName: Security Scanner
summary: This appears to be a legitimate security-scanning skill, but users must only
  run its active scans...
license: MIT
description: |-
  This appears to be a legitimate security-scanning skill, but users must
  only run its active scans...

  核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: legitimate, scanning, scanner, appears, security
tags:
- Security
tools:
- read
- exec
---

# Security Scanner

Automated security scanning toolkit for penetration testing and vulnerability assessment.

## Quick Start

### Port Scan

```bash
nmap -sV -sC -oN scan.txt TARGET
```

### Vulnerability Scan

```bash
nuclei -u TARGET -o results.txt
```

### SSL Check

```bash
sslscan TARGET
```

## Scan Types

### 1. Quick Recon

Fast initial scan for live hosts and open ports:

```bash
nmap -sn -T4 SUBNET  # Host discovery
nmap -F TARGET       # Fast port scan (top 100)
```

### 2. Full Port Scan

Comprehensive port and service detection:

```bash
nmap -p- -sV -sC -A TARGET -oN full_scan.txt
```

### 3. Web Application Scan

```bash
nuclei -u https://TARGET -t cves/ -t vulnerabilities/ -o web_vulns.txt
nikto -h TARGET -o nikto_report.txt
```

### 4. SSL/TLS Analysis

```bash
sslscan TARGET
testssl.sh TARGET
```

## Output

Save reports to `reports/security-scan-YYYY-MM-DD.md` with:

* Target information
* Open ports and services
* Vulnerabilities found (severity rated)
* Recommendations

## Ethics

* Only scan authorized targets
* Get written permission before testing
* Report vulnerabilities responsibly
* Never exploit without authorization

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
