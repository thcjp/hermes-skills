---
slug: security-scanner
name: security-scanner
version: "1.0.0"
displayName: Security Scanner
summary: "安全扫描技能,执行主动扫描前需用户确认,防止误操作影响生产环境稳定性"
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

---
## 边界条件与限制

### 输入限制
- **目标地址格式**：输入的目标地址必须是有效的IP地址或域名，否则技能将无法执行。
- **扫描深度**：对于网络扫描，输入的子网或目标地址不能超过技能支持的扫描深度限制。
- **文件路径**：输出的报告文件路径不能包含非法字符，且不能超过文件系统路径的最大长度限制。

### 性能边界
- **扫描速度**：由于扫描任务可能涉及大量网络请求，扫描速度受限于目标网络响应速度和技能的并发处理能力。
- **结果准确性**：技能的扫描结果依赖于所使用的扫描工具和数据库的准确性，不能保证100%的漏洞检测率。

### 兼容性约束
- **操作系统**：技能在Windows、macOS和Linux操作系统上运行，但某些扫描工具可能在特定操作系统上表现不佳。
- **网络环境**：技能在稳定的网络环境下表现最佳，网络延迟或中断可能导致扫描任务失败。
- **权限要求**：执行某些扫描任务可能需要管理员权限，否则技能可能无法访问必要的系统资源。

### 其他限制
- **扫描频率**：频繁的扫描可能导致目标服务器负载过高，影响正常服务。
- **扫描范围**：技能不支持扫描未授权的目标，用户必须确保拥有适当的权限和授权。
- **报告格式**：技能生成的报告格式固定，不支持自定义报告内容或格式。

