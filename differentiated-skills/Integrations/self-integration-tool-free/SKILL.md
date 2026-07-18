---
slug: self-integration-tool-free
name: self-integration-tool-free
version: "1.0.0"
displayName: 自集成工具
summary: 通过统一网关连接任意外部应用并执行操作，适合个人开发者快速打通多平台。
license: MIT
edition: free
description: |-
  自集成工具（免费版）通过统一集成网关让Agent连接任意外部应用（Slack、HubSpot、Notion等）并执行操作，无需为每个平台单独开发集成。

  核心能力：已有连接查询、连接器搜索、OAuth授权连接创建、动作搜索与执行、基础API参考。

  适用场景：个人开发者打通多个SaaS平台、自动化跨应用工作流、快速验证外部应用集成可行性。

  差异化：聚焦"连接-搜索-执行"最小闭环，使用预置连接器快速上手。专业版新增自定义连接器构建、批量动作、工作流自动化、审计日志等能力。

  触发关键词：自集成、外部应用、连接器、OAuth、动作执行、Membrane
tags:
- 集成工具
- 自动化
tools:
- read
- exec
---

# 自集成工具（免费版）

## 概述

自集成工具（免费版）通过统一集成网关帮助Agent连接任意外部应用并执行操作。传统方式下，每接入一个SaaS平台（Slack、HubSpot、Notion等）都需要单独开发OAuth流程与API适配层。本工具通过"连接器"抽象，将各平台的差异封装为统一接口，Agent只需"建立连接-搜索动作-执行动作"三步即可操作任意已支持的应用。

本免费版聚焦个人开发者的核心集成场景，提供预置连接器查询、OAuth授权连接与动作执行能力，适合快速验证集成可行性与构建简单跨应用工作流。

## 核心能力

| 能力 | 说明 | 免费版支持 |
|------|------|-----------|
| 已有连接查询 | 列出已建立的连接 | 是 |
| 连接器搜索 | 按应用名搜索预置连接器 | 是 |
| OAuth授权连接 | 创建授权链接供用户完成认证 | 是 |
| 动作搜索 | 自然语言搜索可执行动作 | 是 |
| 动作执行 | 执行单个动作并返回结果 | 是 |
| 自定义连接器构建 | 为未支持的应用构建连接器 | 否 |
| 批量动作 | 批量执行多个动作 | 否 |
| 工作流自动化 | 编排多步骤工作流 | 否 |
| 审计日志 | 操作全程留痕 | 否 |

## 使用场景

### 场景1：个人开发者打通Slack与HubSpot

小王是一名独立开发者，希望将Slack中收到的线索自动同步到HubSpot CRM。他使用本工具：搜索Slack连接器并建立连接，搜索HubSpot连接器并建立连接，搜索"创建联系人"动作并在Slack消息触发时执行，实现线索自动入库。

### 场景2：快速验证外部应用集成可行性

产品经理想评估"将Notion文档同步到Slack频道"的可行性。使用本工具搜索Notion与Slack连接器，确认两者均已有预置连接器与相关动作，即可判定集成可行，无需投入开发资源。

### 场景3：MCP工具集成外部应用

当需要将外部应用能力作为MCP工具接入Agent时，本工具提供统一连接层：MCP端点通过本工具建立连接并执行动作，无需为每个应用单独实现MCP适配。

## 快速开始（约150秒）

### 步骤1：配置API Token

在集成网关控制台获取API Token，设置为环境变量：

```bash
export INTEGRATION_TOKEN="your_token_here"
```

所有请求携带`Authorization: Bearer $INTEGRATION_TOKEN`，基础URL为`https://api.integration-gateway.com`。

### 步骤2：检查已有连接

```bash
curl https://api.integration-gateway.com/connections \
  -H "Authorization: Bearer $INTEGRATION_TOKEN"
```

查看是否已有目标应用的连接。若已有且`disconnected`为`false`，可直接跳到步骤4。

### 步骤3：搜索并建立连接

搜索目标应用的连接器：

```bash
curl "https://api.integration-gateway.com/search?q=slack" \
  -H "Authorization: Bearer $INTEGRATION_TOKEN"
```

找到`elementType: "connector"`的结果，使用其`id`创建连接请求：

```bash
curl -X POST https://api.integration-gateway.com/connection-requests \
  -H "Authorization: Bearer $INTEGRATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"connectorId": "cnt_abc123"}'
```

响应中的`url`需在浏览器中打开，完成OAuth授权。

### 步骤4：搜索并执行动作

授权完成后，搜索可用动作：

```bash
curl "https://api.integration-gateway.com/actions?connectionId=con_abc123&intent=send+a+message&limit=10" \
  -H "Authorization: Bearer $INTEGRATION_TOKEN"
```

执行动作：

```bash
curl -X POST "https://api.integration-gateway.com/actions/act_xyz/run?connectionId=con_abc123" \
  -H "Authorization: Bearer $INTEGRATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"input": {"channel": "#general", "text": "Hello!"}}'
```

## 配置示例

### 查询已有连接

```bash
curl https://api.integration-gateway.com/connections \
  -H "Authorization: Bearer $INTEGRATION_TOKEN"
```

响应字段说明：`id`（连接ID）、`name`（连接名）、`connectorId`（连接器ID）、`disconnected`（是否已断开）、`state`（状态：READY表示可用）。

### 创建连接请求

```bash
curl -X POST https://api.integration-gateway.com/connection-requests \
  -H "Authorization: Bearer $INTEGRATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "connectorId": "cnt_abc123",
    "name": "我的Slack工作区"
  }'
```

响应包含`url`（授权链接）与`requestId`（用于轮询状态）。

### 轮询连接结果

```bash
curl https://api.integration-gateway.com/connection-requests/req_xyz \
  -H "Authorization: Bearer $INTEGRATION_TOKEN"
```

状态说明：`pending`（等待用户授权）、`success`（成功，使用`resultConnectionId`）、`error`（失败，查看`resultError`）。

## 最佳实践

1. **复用已有连接**：执行动作前先查询已有连接，避免重复授权
2. **动作搜索用自然语言**：`intent`参数支持自然语言描述，如"发送消息"而非精确动作名
3. **inputSchema校验**：执行动作前查看动作的`inputSchema`，确保入参符合要求
4. **连接命名清晰**：创建连接时设置有意义的`name`，便于多连接管理
5. **及时断开无用连接**：不再使用的连接及时断开，减少安全暴露面

## 常见问题

### Q1：搜索不到目标应用的连接器怎么办？
A：免费版仅支持预置连接器。若目标应用未预置，可使用专业版的自定义连接器构建功能，通过自然语言描述自动构建。

### Q2：连接请求一直pending怎么办？
A：用户需在浏览器中打开返回的`url`完成OAuth授权。确认用户已访问链接并完成授权后，轮询状态应变为`success`。

### Q3：动作执行报inputSchema校验错误？
A：执行动作前先查看动作的`inputSchema`字段，了解所需参数的名称、类型与是否必填。确保`input`对象符合Schema定义。

### Q4：可以同时连接多个应用吗？
A：可以。每个应用建立独立连接，通过`connectionId`区分。执行动作时需指定对应的`connectionId`。

### Q5：Token泄露后如何处理？
A：立即在控制台撤销该Token并生成新Token。已建立的连接不受影响，但需用新Token重新发起请求。

## 免费版限制

本免费体验版限制以下高级功能：
- 不支持自定义连接器构建（仅预置连接器）
- 不支持批量动作执行
- 不支持多步骤工作流编排
- 不支持操作审计日志
- 不支持连接健康监控与自动重连

解锁全部功能请使用专业版：`self-integration-tool-pro`

## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux
- **网络**：可访问集成网关与目标应用API

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| 集成网关账户 | 在线服务 | 必需 | 在网关控制台注册 |
| 目标应用账户 | 在线服务 | 必需 | 各SaaS平台注册 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| curl或HTTP客户端 | 命令行工具 | 可选 | 系统自带或pip/npm安装 |

### API Key 配置
- **集成网关Token**：存储于环境变量`INTEGRATION_TOKEN`
- **目标应用凭据**：由网关托管，通过OAuth授权建立连接，本地不保存
- **禁止**：在代码或脚本中硬编码Token或应用凭据

### 可用性分类
- **分类**：MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务
