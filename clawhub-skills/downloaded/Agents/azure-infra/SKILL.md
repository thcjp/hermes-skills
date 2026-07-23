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
  with cloud-write risk cons。Use when 用户需要Azure Infra相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags:
- Agents
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

Use the local Azure CLI to answer questions about Azure resources. Default to read‑only queries. Only propose or run write/destructive actions after explicit user confirmation.

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
1. Ensure login: `az account show` (if not logged in, run `az login --use-device-code`).
2. If multiple subscriptions exist, ask the user to pick one; otherwise use the default subscription.
3. Use read‑only commands to answer the question.
4. If the user asks for changes, outline the exact command and ask for confirmation before running.
```

## 错误处理
- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Azure Infra？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Azure Infra有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 依赖云服务，需要网络连接

<!-- 触发条件: 用户明确请求时激活 -->

## 案例展示

```json
{
  "input": "示例输入",
  "output": "处理结果"
}
```

## 输出格式

处理结果以结构化格式返回, 包含状态码、消息和数据字段。
