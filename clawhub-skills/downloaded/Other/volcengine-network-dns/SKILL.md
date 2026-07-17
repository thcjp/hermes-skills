---
slug: volcengine-network-dns
name: volcengine-network-dns
version: "1.0.0"
displayName: Volcengine Network Dns
summary: DNS record management on Volcengine networking services. Use when users need
  zone record query/up...
license: MIT
description: |-
  DNS record management on Volcengine networking services. Use when users
  need zone record query/up...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: network, dns, volcengine, record, management, services, networking
tags:
- Other
tools:
- read
- exec
---

# Volcengine Network Dns

Manage DNS records with strict change scoping and verification steps.

## Execution Checklist

1. Confirm domain zone, record type, and target value.
2. Query existing records before modifications.
3. Apply add/update/delete operation with TTL constraints.
4. Validate propagation using authoritative and recursive checks.

## Safety Rules

* Avoid blind overwrite; diff against existing records.
* Keep rollback values in output.
* Minimize TTL before migration windows.

## References

* `references/sources.md`

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
