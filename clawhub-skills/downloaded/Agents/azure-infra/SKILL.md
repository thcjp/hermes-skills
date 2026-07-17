---
slug: azure-infra
name: azure-infra
version: "1.0.0"
displayName: Azure Infra
summary: This Azure infrastructure skill appears purpose-aligned and disclosed, with
  cloud-write risk cons...
license: MIT
description: |-
  This Azure infrastructure skill appears purpose-aligned and disclosed,
  with cloud-write risk cons...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: appears, azure, infra, infrastructure, skill
tags:
- Agents
tools:
- read
- exec
---

# Azure Infra

## Overview

Use the local Azure CLI to answer questions about Azure resources. Default to read‑only queries. Only propose or run write/destructive actions after explicit user confirmation.

## Quick Start

1. Ensure login: `az account show` (if not logged in, run `az login --use-device-code`).
2. If multiple subscriptions exist, ask the user to pick one; otherwise use the default subscription.
3. Use read‑only commands to answer the question.
4. If the user asks for changes, outline the exact command and ask for confirmation before running.

## Safety Rules (must follow)

* Treat all actions as **read‑only** unless the user explicitly requests a change **and** confirms it.
* For any potentially destructive change (delete/terminate/destroy/modify/scale/billing/IAM credentials), require a confirmation step.
* Prefer `--dry-run` when available and show the plan before execution.
* Never reveal or log secrets (keys, client secrets, tokens).

## Task Guide (common requests)

* **Inventory / list**: use `list`/`show`/`get` commands.
* **Health / errors**: use Azure Monitor metrics/logs queries.
* **Security checks**: RBAC roles, public storage, NSG exposure, Key Vault access.
* **Costs**: Cost Management (read‑only).
* **Changes**: show exact CLI command and require confirmation.

## Subscription & Tenant Handling

* If the user specifies a subscription/tenant, honor it.
* Otherwise use the default subscription from `az account show`.
* When results are subscription‑scoped, state the subscription used.

## References

See `references/azure-cli-queries.md` for common command patterns.

## Assets

* `assets/icon.svg` — custom icon (dark cloud + terminal prompt, Azure‑blue accent)

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
