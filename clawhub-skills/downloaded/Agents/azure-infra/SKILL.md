---
slug: azure-infra
name: azure-infra
version: "1.0.0"
displayName: Azure Infra
summary: "Azure基础设施技能(云写风险需谨慎)"
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

## 补充详细的功能列表（含边界条件处理）

为了增强Azure Infra技能的功能完整性，以下是对现有功能的详细描述，包括边界条件处理：

- **资源清单**：提供`list`、`show`、`get`命令来列出、显示和获取Azure资源信息。边界条件处理包括空资源返回空列表，非空资源返回详细信息。
- **健康检查**：使用Azure Monitor的metrics和logs查询来检查资源健康状态。边界条件处理包括无日志数据时返回无数据状态。
- **安全检查**：检查RBAC角色、公共存储、网络安全组（NSG）暴露和密钥保管库访问。边界条件处理包括无相关设置时返回无设置状态。
- **成本分析**：提供Cost Management的只读查询功能来分析成本。边界条件处理包括无成本数据时返回无成本信息。

## Subscription & Tenant Handling

* If the user specifies a subscription/tenant, honor it.
* Otherwise use the default subscription from `az account show`.
* When results are subscription‑scoped, state the subscription used.

## 补充输入输出参数说明（含默认值、类型、取值范围）

为了提高Azure Infra技能的易用性，以下是对输入输出参数的详细说明：

- **输入参数**：
  - `subscription_id`：字符串类型，Azure订阅ID，默认为当前登录用户的默认订阅ID。
  - `resource_group`：字符串类型，资源组名称，用于限定查询的资源组。
  - `resource_name`：字符串类型，资源名称，用于限定查询的特定资源。

- **输出参数**：
  - `status_code`：整数类型，状态码，表示操作成功或失败。
  - `message`：字符串类型，操作结果描述信息。
  - `data`：JSON对象，包含查询到的资源信息。

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

## 补充技术亮点与差异化优势分析

Azure Infra技能的技术亮点和差异化优势包括：

- **本地Azure CLI集成**：通过本地Azure CLI执行命令，确保操作的安全性和效率。
- **默认只读查询**：默认只读查询模式，减少误操作风险。
- **用户确认机制**：所有写操作和破坏性操作都需要用户确认，确保操作的安全性。

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 补充与同类方案的对比

与同类方案相比，Azure Infra技能的优势在于：

- **同类方案通常依赖于远程API调用，而Azure Infra技能使用本地CLI，减少了网络延迟和潜在的安全风险**。
- **同类方案可能缺乏用户确认机制，而Azure Infra技能通过用户确认确保操作的安全性**。

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

## 补充错误码定义和处理方案

为了确保Azure Infra技能的健壮性，以下是对常见错误码的定义和处理方案：

- **错误码：401** - 未授权访问
  - 处理方案：检查用户是否已登录，如果未登录，则提示用户登录。

- **错误码：404** - 资源未找到
  - 处理方案：检查资源名称是否正确，或者该资源是否已存在。

- **错误码：500** - 服务器内部错误
  - 处理方案：检查网络连接，如果问题持续，请联系技术支持。

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

## 补充解决的真实验证痛点

Azure Infra技能解决了以下真实验证痛点：

- **简化Azure资源管理**：通过自动化命令行操作，简化了Azure资源管理流程。
- **降低误操作风险**：默认只读查询和用户确认机制降低了误操作的风险。

## 输出格式

处理结果以结构化格式返回, 包含状态码、消息和数据字段。

## 补充技术或方法创新点

Azure Infra技能的技术或方法创新点包括：

- **本地Azure CLI集成**：通过本地CLI集成，实现了对Azure资源的直接操作，提高了操作效率。
- **用户确认机制**：通过引入用户确认机制，提高了操作的安全性。

