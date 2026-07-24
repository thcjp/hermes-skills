---
slug: "security-scanner"
name: "security-scanner"
version: 1.0.1
displayName: "Security Scanner"
summary: "安全扫描技能,主动扫描需仅在授权目标运行。This appears to be a legitimate security-scanning skill, but users must on"
license: "MIT"
description: |-
  This appears to be a legitimate security-scanning skill, but users must
  only run its active scans。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标.
tags:
  - Security
  - 安全
  - 加密
  - 工具
  - bash
  - target
  - scan
  - agent
tools:
  - read
  - exec
homepage: ""
category: "Security"
---
# Security Scanner

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Security Scanner安全扫描 | 不支持 | 支持 |
| Security Scanner主动扫描 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |

## 核心能力

- This appears to be a legitimate security-scanning skill, but users must
  only run its active scans
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 安全扫描 | 目标URL或代码路径 | 漏洞扫描报告和风险等级 |
| 依赖漏洞检测 | 依赖文件(package.json/requirements.txt) | 已知漏洞和修复版本 |
| 配置安全检查 | 配置文件和环境变量 | 安全配置问题和修复建议 |

**不适用于**：需要深度渗透测试和漏洞利用的场景

## 使用流程

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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| scan_target | string | 是 | 扫描目标URL或文件路径 |
| scan_mode | string | 否 | 扫描模式, 可选: quick/full/custom, 默认: quick |

## 输出格式

Save reports to `reports/security-scan-YYYY-MM-DD.md` with:

* Target information
* Open ports and services
* Vulnerabilities found (severity rated)
* Recommendations

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 工具依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 示例1：基础用法

```
### Port Scan(补充)
# ...
```bash
nmap -sV -sC -oN scan.txt TARGET
```
# ...
### Vulnerability Scan(补充)
# ...
```bash
nuclei -u TARGET -o results.txt
```
# ...
### SSL Check(补充)
# ...
```bash
sslscan TARGET
```
```

## 常见问题

### Q1: 如何开始使用Security Scanner？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

