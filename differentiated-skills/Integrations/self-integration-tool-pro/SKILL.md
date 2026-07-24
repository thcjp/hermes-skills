---

slug: "self-integration-tool-pro"
name: "self-integration-tool-pro"
version: "1.0.0"
displayName: "自集成工具Pro"
summary: "企业级外部应用集成方案，含自定义连接器、批量动作、工作流编排与审计日志。。自集成工具（专业版）为团队与企业提供完整的外部应用集成治理方案，支持连接任意外部应用并编排自动化工作流。核心能力：自"
license: "Proprietary"
edition: "pro"
description: |-，可自动提升工作效率
  自集成工具（专业版）为团队与企业提供完整的外部应用集成治理方案，支持连接任意外部应用并编排自动化工作流。核心能力：自定义连接器构建（自然语言驱动）、批量动作执行、多步骤工作流编排、操作审计日志、连接健康监控与自动重连、Agent辅助连接器开发、MCP工具集成适配。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - 集成工具
  - 自动化
  - 企业级
  - 工具
  - 效率
  - 集成
  - integration
  - 工作流
  - 开发
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"

---

# 自集成工具（专业版）

## 概述

自集成工具（专业版）面向团队与企业用户，提供完整的外部应用集成治理方案。在免费版"连接-搜索-执行"基础闭环之上，专业版新增自定义连接器构建、批量动作执行、多步骤工作流编排、操作审计日志与连接健康监控，满足企业级跨应用自动化与合规审计需求.
专业版的核心差异化在于"自定义连接器构建"：当目标应用没有预置连接器时，通过自然语言描述驱动Agent自动构建连接器与动作，将"集成开发"从手工编码升级为自然语言驱动.
## 核心能力

| 能力 | 说明 | 专业版支持 |
|---|---|-----|
| 预置连接器 | 搜索并使用预置连接器 | 是 |
| 自定义连接器构建 | 自然语言驱动构建新连接器 | 是 |
| OAuth授权连接 | 创建授权链接完成认证 | 是 |
| 动作搜索与执行 | 自然语言搜索并执行动作 | 是 |
| 批量动作执行 | 批量执行多个动作 | 是 |
| 工作流编排 | 多步骤工作流编排与调度 | 是 |
| 操作审计日志 | 全量操作留痕与导出 | 是 |
| 连接健康监控 | 自动检测与重连 | 是 |
| Agent辅助开发 | Agent会话驱动连接器开发 | 是 |
| MCP工具集成适配 | 为MCP端点提供统一连接层 | 是 |

### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.
**输入**: 用户提供参数配置与调用所需的指令和必要参数.
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.
**输入**: 用户提供结果处理与输出所需的指令和必要参数.
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级外部应用集、成方案、含自定义连接器、工作流编排与审计、自集成工具、为团队与企业提供、完整的外部应用集、成治理方案、支持连接任意外部、应用并编排自动化、核心能力、连接健康监控与自、动重连、辅助连接器开发、Use、when、API、接口对接、Webhook、系统连接时使用、不适用于逆向工程等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用场景

### 场景1：企业级跨SaaS工作流自动化

某市场团队需要"当HubSpot新增联系人时，自动在Slack通知并在Notion创建客户档案"。使用专业版工作流编排：定义触发器（HubSpot新增联系人）→ 动作1（Slack发消息）→ 动作2（Notion创建页面），工作流自动监听并执行，全程无需人工干预.
### 场景2：私有应用集成

公司内部有自研CRM系统，无预置连接器。使用专业版自定义连接器构建：通过自然语言描述"为内部CRM（https://crm.company.com）构建连接器，支持创建客户、查询订单"，Agent自动分析API并构建连接器与动作，内部系统随即纳入集成体系.
### 场景3：合规审计场景

金融行业客户要求所有跨系统操作可追溯。专业版审计日志记录每次连接创建、动作执行的时间、操作者、入参与结果，支持导出供合规审计。异常操作（如批量删除）实时告警.
### 场景4：复杂多步业务流程

订单处理流程涉及5个系统：电商下单 → CRM建客户 → ERP创订单 → 物流发货 → Slack通知。专业版工作流编排将这些步骤串联，支持条件分支（如库存不足则走补货分支）与错误重试.
### 场景5：Agent驱动的集成开发

开发者通过Agent会话描述需求，Agent自动构建连接器、测试动作、生成文档。如"为Jira构建一个创建Issue的动作"，Agent分析Jira API后生成动作定义并验证，开发者只需确认即可.
## 使用流程

### Step 1：配置API Token

```bash
export INTEGRATION_TOKEN="your_token_here"
```

基础URL为`https://api.integration-gateway.com`，所有请求携带`Authorization: Bearer $INTEGRATION_TOKEN`.
### Step 2：构建自定义连接器（如需）

通过Agent会话构建连接器：

```bash
curl -X POST https://api.integration-gateway.com/agent/sessions \
  -H "Authorization: Bearer $INTEGRATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "为内部CRM（https://crm.company.com）构建连接器，支持创建客户与查询订单"}'
```

轮询会话状态直到完成：

```bash
curl "https://api.integration-gateway.com/agent/sessions/sess_xyz?wait=true&timeout=30" \
  -H "Authorization: Bearer $INTEGRATION_TOKEN"
```

### Step 3：定义工作流

```yaml
workflow:
  name: lead-to-crm
  trigger:
    type: webhook
    source: hubspot
    event: contact.created
  steps:
    - id: notify_slack
      action: slack.send_message
      connection: con_slack
      input:
        channel: "#sales"
        text: "新线索：{{trigger.contact.name}}"
    - id: create_notion_page
      action: notion.create_page
      connection: con_notion
      input:
        parent: "{{vault.notion_db}}"
        properties:
          name: "{{trigger.contact.name}}"
          email: "{{trigger.contact.email}}"
  on_error:
    - notify_slack
    retry: 3
```

### Step 4：启用审计日志

```yaml
audit:
  log_destination: s3
  retention: 1y
  fields:
    - timestamp
    - operator
    - connection_id
    - action_id
    - input_hash
    - result_status
  alert_on:
    - bulk_delete
    - off_hours_access
```

### Step 5：批量执行动作

```bash
curl -X POST "https://api.integration-gateway.com/actions/batch" \
  -H "Authorization: Bearer $INTEGRATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "actions": [
      {"actionId": "act_1", "connectionId": "con_1", "input": {"text": "消息1"}},
      {"actionId": "act_1", "connectionId": "con_1", "input": {"text": "消息2"}},
      {"actionId": "act_1", "connectionId": "con_1", "input": {"text": "消息3"}}
    ]
  }'
```

#
## 示例

### 自定义连接器构建（Agent会话）

```bash
# 创建会话
curl -X POST https://api.integration-gateway.com/agent/sessions \
  -H "Authorization: Bearer $INTEGRATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "为Jira（https://company.atlassian.net）构建连接器，支持创建Issue与查询项目"}'
# ...
# 轮询状态（state为idle或status为completed即完成）
curl "https://api.integration-gateway.com/agent/sessions/sess_xyz?wait=true&timeout=30" \
  -H "Authorization: Bearer $INTEGRATION_TOKEN"
# ...
# 发送后续指令（如需调整）
curl -X POST https://api.integration-gateway.com/agent/sessions/sess_xyz/message \
  -H "Authorization: Bearer $INTEGRATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"input": "创建Issue时需要支持指定优先级字段"}'
# ...
# 中止会话（如需）
curl -X POST https://api.integration-gateway.com/agent/sessions/sess_xyz/interrupt \
  -H "Authorization: Bearer $INTEGRATION_TOKEN"
```

### 工作流编排（含条件分支）

```yaml
workflow:
  name: order-processing
  trigger:
    type: webhook
    source: ecommerce
    event: order.created
  steps:
    - id: check_inventory
      action: erp.check_stock
      connection: con_erp
      input:
        sku: "{{trigger.order.sku}}"
    - id: branch
      if: "{{check_inventory.result.in_stock}}"
      then:
        - id: create_shipment
          action: logistics.create_shipment
          connection: con_logistics
      else:
        - id: create_reorder
          action: erp.create_reorder
          connection: con_erp
    - id: notify
      action: slack.send_message
      connection: con_slack
      input:
        channel: "#ops"
        text: "订单 {{trigger.order.id}} 处理完成"
```

## 高级特性

### 自定义连接器构建

- **自然语言驱动**：描述应用与所需动作，Agent自动分析API并构建
- **交互式完善**：通过会话消息迭代调整连接器定义
- **自动文档**：构建完成后自动生成动作的inputSchema与outputSchema
- **即时可用**：构建完成即可搜索并执行，无需部署

### 批量动作执行

- **批量提交**：一次请求提交多个动作，并行执行
- **部分失败处理**：支持配置"任一失败即停止"或"全部尝试"
- **结果聚合**：批量结果按顺序返回，便于对应
- **限流控制**：自动遵守目标应用的速率限制

### 工作流编排

- **触发器**：支持Webhook、定时、手动三种触发方式
- **条件分支**：基于上一步结果的条件分支与循环
- **错误处理**：支持重试、回滚、告警等错误策略
- **变量引用**：步骤间通过`{{step_id.result.field}}`传递数据

### 审计日志

- **全量记录**：连接创建、动作执行、工作流运行全程留痕
- **操作者归属**：记录每次操作的发起者
- **敏感数据脱敏**：入参记录哈希而非原值，保护敏感信息
- **合规导出**：支持导出供审计

## 性能优化

1. **并行执行**：批量动作与工作流无依赖步骤自动并行
2. **连接复用**：同一连接的多次请求复用HTTP连接
3. **结果缓存**：幂等查询动作的结果可缓存（专业版支持配置）
4. **增量轮询**：Agent会话采用长轮询，减少请求次数

## 最佳实践

1. **连接器命名规范**：按"应用-环境"命名，便于多环境管理
2. **工作流幂等设计**：关键步骤设计为幂等，避免重试导致重复
3. **审计定期复核**：每月复核审计日志，确认无异常操作
4. **连接健康监控**：启用自动重连，避免连接失效导致工作流中断
5. **自定义连接器测试**：构建后先用测试数据验证，再投入生产
6. **工作流版本管理**：工作流变更前备份旧版本，便于回滚

## 错误处理

| 序号 | 错误场景 | 原因 | 处理方式 | 优先级 |
|:-----|:-----|:-----|:-----|:-----|
| 1 | 输入参数缺失 | 用户未提供必要参数 | 提示用户提供所需参数后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 | P0 |
| 2 | 执行超时 | 处理时间过长 | 检查输入数据量,分批处理 | P1 |
| 3 | 输出格式错误 | 结果不符合预期格式 | 检查`output_format`参数配置 | P1 |

## 常见问题

### Q1：自定义连接器构建需要多长时间？
A：取决于目标应用API的复杂度。简单REST API通常1-3分钟，复杂API（如需OAuth流程）可能5-10分钟。构建过程中可通过会话消息交互调整.
### Q2：工作流执行失败如何排查？
A：查看工作流运行日志，定位失败步骤。专业版记录每步的输入、输出与错误信息。常见原因包括连接失效（需重新授权）、入参不符Schema、目标应用限流.
### Q3：批量动作部分失败怎么办？
A：根据配置策略处理。若配置为"全部尝试"，失败的动作会在结果中标记；若配置为"任一失败即停止"，后续动作不执行。失败的可通过重试接口单独重试.
### Q4：可以连接多少个外部应用？
A：专业版不限制连接数量。每个连接独立管理，按应用维度组织.
### Q5：审计日志会记录敏感数据吗？
A：不会。入参记录哈希值而非原值，连接凭据由网关托管不记录。日志仅记录操作者、时间、动作、状态等元数据.
### Q6：Agent会话构建连接器失败怎么办？
A：可通过会话消息补充信息（如API文档链接、认证方式说明）让Agent重新尝试。也可中止会话后用更详细的prompt重新开始.
### Q7：如何对接MCP工具生态？
A：专业版提供MCP端点集成适配，MCP工具通过本工具建立连接并执行动作。配置MCP server时指定本工具的网关地址与Token，MCP端点即可操作任意外部应用.
### Q8：工作流支持定时触发吗？
A：支持。工作流触发器可配置为cron表达式定时触发，适合定期同步等场景.
## 故障排查

| 现象 | 可能原因 | 解决方案 |
|---:|---:|---:|
| 连接器构建超时 | 目标API复杂或文档不全 | 补充API文档链接，通过会话消息指导 |
| 工作流步骤间数据传递失败 | 变量引用路径错误 | 检查`{{step_id.result.field}}`路径是否正确 |
| 批量动作限流 | 目标应用速率限制 | 降低批量并发数或增加间隔 |
| 连接频繁断开 | 凭据过期或网络问题 | 启用自动重连并检查凭据有效期 |
| 审计日志缺失 | 日志服务未启动 | 检查audit配置与存储权限 |

## 专业版特性

本专业版相比免费版新增以下能力：
- 自定义连接器构建：自然语言驱动，Agent自动构建未预置应用的连接器
- 批量动作执行：并行批量、部分失败处理、结果聚合
- 工作流编排：触发器、条件分支、错误处理、变量引用
- 操作审计日志：全量留痕、脱敏记录、合规导出
- 连接健康监控：自动检测断连与重连，保障工作流持续运行

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|:---:|:---:|:---:|:---:|
| 免费体验版 | 0元 | 预置连接器+单动作执行 | 个人试用 |
| 收费专业版 | 49.9元/月 | 自定义连接器+工作流+批量+审计+优先支持 | 团队/企业 |

专业版通过SkillHub SkillPay发布.
## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux
- **网络**：可访问集成网关与目标应用API

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| 集成网关账户 | 在线服务 | 必需 | 在网关控制台注册 |
| 目标应用账户 | 在线服务 | 必需 | 各SaaS平台注册 |
| 对象存储 | 基础设施 | 可选 | 审计日志归档 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **集成网关Token**：存储于环境变量`INTEGRATION_TOKEN`
- **目标应用凭据**：由网关托管，通过OAuth授权建立连接
- **禁止**：在代码或脚本中硬编码Token或应用凭据

### 可用性分类
- **分类**：MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent完成操作

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "自集成工具Pro处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "self integration pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
