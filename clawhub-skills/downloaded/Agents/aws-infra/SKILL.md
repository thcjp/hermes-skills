---
slug: aws-infra
name: aws-infra
version: "1.0.0"
displayName: AWS Infra
summary: Chat-based AWS infrastructure assistance using AWS CLI and console context.
  Use for querying, aud...
license: MIT
description: |-
  Chat-based AWS infrastructure assistance using AWS CLI and console context.
  Use for querying, aud...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: using, chat, assistance, based, infra, aws, infrastructure
tags:
- Agents
tools:
- read
- exec
---

# AWS Infra

## Overview

Use the local AWS CLI to answer questions about AWS resources. Default to read‑only queries. Only propose or run write/destructive actions after explicit user confirmation.

## Quick Start

1. Determine profile/region from environment or `[REDACTED_AWS_PATH]
2. Start with identity:
   * `aws sts get-caller-identity`
3. Use read‑only service commands to answer the question.
4. If the user asks for changes, outline the exact command and ask for confirmation before running.

## Safety Rules (must follow)

* Treat all actions as **read‑only** unless the user explicitly requests a change **and** confirms it.
* For any potentially destructive change (delete/terminate/destroy/modify/scale/billing/IAM credentials), require a confirmation step.
* Prefer `--dry-run` when available and show the plan before execution.
* Never reveal or log secrets (access keys, session tokens).

## Task Guide (common requests)

* **Inventory / list**: use `list`/`describe`/`get` commands.
* **Health / errors**: use CloudWatch metrics/logs queries.
* **Security checks**: IAM, S3 public access, SG exposure, KMS key usage.
* **Costs**: Cost Explorer / billing queries (read‑only).
* **Changes**: show exact CLI command and require confirmation.

## Region & Profile Handling

* If the user specifies a region/profile, honor it.
* Otherwise use `AWS_PROFILE` / `AWS_REGION` if set, then fall back to `[REDACTED_AWS_PATH]
* When results are region‑scoped, state the region used.

## References

See `references/aws-cli-queries.md` for common command patterns.

## Assets

* `assets/icon.svg` — custom icon (dark cloud + terminal prompt)

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
