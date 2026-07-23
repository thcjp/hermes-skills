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
  only run its active scans。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Security
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

- This appears to be a legitimate security-scanning skill, but users must
  only run its active scans
- 触发关键词: legitimate, scanning, scanner, appears, security

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
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
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Security Scanner？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Security Scanner有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
