---
slug: dns-lookup
name: dns-lookup
version: "1.0.0"
displayName: Dns Lookup
summary: Resolve hostnames to IP addresses using `dig` from bind-utils.
license: MIT
description: |-
  Resolve hostnames to IP addresses using `dig` from bind-utils.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: resolve, addresses, using, dns, hostnames, lookup
tags:
- Other
tools:
- read
- exec
---

# Dns Lookup

Resolve hostnames to IP addresses using `dig`. Provided by the `bind-utils` package.

## Basic Lookup

Resolve A records for a hostname:

```bash
dig example.com A +short
```

## IPv6 Lookup

Resolve AAAA records:

```bash
dig example.com AAAA +short
```

## Full DNS Record

Get the full DNS response with authority and additional sections:

```bash
dig example.com ANY
```

## Reverse Lookup

Find the hostname for an IP address:

```bash
dig -x 93.184.216.34 +short
```

## Install

```bash
sudo dnf install bind-utils
```

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
