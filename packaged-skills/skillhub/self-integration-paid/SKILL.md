---
slug: "self-integration-paid"
name: "self-integration-paid"
version: "1.0.0"
displayName: "自集成工具Pro"
summary: "企业级外部应用集成方案，含自定义连接器、批量动作、工作流编排与审计日志。"
license: "Proprietary"
edition: "pro"
description: |-
  自集成工具（专业版）为团队与企业提供完整的外部应用集成治理方案，支持连接任意外部应用并编排自动化工作流。核心能力：自定义连接器构建（自然语言驱动）、批量动作执行、多步骤工作流编排、操作审计日志、连接健康监控与自动重连、Agent辅助连接器开发、MCP工具集成适配。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
  - 集成工具
  - 自动化
  - 企业级
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# 自集成工具Pro

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 专业版支持 | 支持 | 支持 |
| 预置连接器 | 不支持 | 支持 |
| 自定义连接器构建 | 不支持 | 支持 |
| OAuth授权连接 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力 | 说明 | 专业版支持 |
|------|------|-----------|
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
### 预置连接器

执行预置连接器操作,处理用户输入并返回结果。

**输入**: 用户提供预置连接器所需的参数和指令。

**输出**: 返回预置连接器的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`预置连接器`相关配置参数进行设置
### 自定义连接器构建

执行自定义连接器构建操作,处理用户输入并返回结果。

**输入**: 用户提供自定义连接器构建所需的参数和指令。

**输出**: 返回自定义连接器构建的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`自定义连接器构建`相关配置参数进行设置
### OAuth授权连接

执行OAuth授权连接操作,处理用户输入并返回结果。

**输入**: 用户提供OAuth授权连接所需的参数和指令。

**输出**: 返回OAuth授权连接的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`OAuth授权连接`相关配置参数进行设置
#
## 适用场景

### 场景1：企业级跨SaaS工作流自动化

某市场团队需要"当HubSpot新增联系人时，自动在Slack通知并在Notion创建客户档案"。使用专业版工作流编排：定义触发器（HubSpot新增联系人）→ 动作1（Slack发消息）→ 动作2（Notion创建页面），工作流自动监听并执行，全程无需人工干预。

### 场景2：私有应用集成

公司内部有自研CRM系统，无预置连接器。使用专业版自定义连接器构建：通过自然语言描述"为内部CRM（https://crm.company.com）构建连接器，支持创建客户、查询订单"，Agent自动分析API并构建连接器与动作，内部系统随即纳入集成体系。

### 场景3：合规审计场景

金融行业客户要求所有跨系统操作可追溯。专业版审计日志记录每次连接创建、动作执行的时间、操作者、入参与结果，支持导出供合规审计。异常操作（如批量删除）实时告警。

### 场景4：复杂多步业务流程

订单处理流程涉及5个系统：电商下单 → CRM建客户 → ERP创订单 → 物流发货 → Slack通知。专业版工作流编排将这些步骤串联，支持条件分支（如库存不足则走补货分支）与错误重试。

### 场景5：Agent驱动的集成开发

开发者通过Agent会话描述需求，Agent自动构建连接器、测试动作、生成文档。如"为Jira构建一个创建Issue的动作"，Agent分析Jira API后生成动作定义并验证，开发者只需确认即可。

## 使用流程

### 步骤1：配置API Token

```bash
export INTEGRATION_TOKEN="your_token_here"
```

基础URL为`https://api.integration-gateway.com`，所有请求携带`Authorization: Bearer $INTEGRATION_TOKEN`。

### 步骤2：构建自定义连接器（如需）

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

### 步骤3：定义工作流

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
        text: "新线索：self-integration-paid"
    - id: create_notion_page
      action: notion.create_page
      connection: con_notion
      input:
        parent: "相关信息"
        properties:
          name: "self-integration-paid"
          email: "相关信息"
  on_error:
    - notify_slack
    retry: 3
```

### 步骤4：启用审计日志

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

### 步骤5：批量执行动作

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
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 现象 | 可能原因 | 解决方案 |
|------|---------|---------|
| 连接器构建超时 | 目标API复杂或文档不全 | 补充API文档链接，通过会话消息指导 |
| 工作流步骤间数据传递失败 | 变量引用路径错误 | 检查`按流程执行`路径是否正确 |
| 批量动作限流 | 目标应用速率限制 | 降低批量并发数或增加间隔 |
| 连接频繁断开 | 凭据过期或网络问题 | 启用自动重连并检查凭据有效期 |
| 审计日志缺失 | 日志服务未启动 | 检查audit配置与存储权限 |

## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux
- **网络**：可访问集成网关与目标应用API

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| 集成网关账户 | 在线服务 | 必需 | 在网关控制台注册 |
| 目标应用账户 | 在线服务 | 必需 | 各SaaS平台注册 |
| 对象存储 | 基础设施 | 可选 | 审计日志归档 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- **集成网关Token**：存储于环境变量`INTEGRATION_TOKEN`
- **目标应用凭据**：由网关托管，通过OAuth授权建立连接
- **禁止**：在代码或脚本中硬编码Token或应用凭据

### 可用性分类
- **分类**：MD+EXEC（）
- **说明**：基于Markdown的AI Skill，

## 案例展示

### 自定义连接器构建（Agent会话）

```bash
# 创建会话
curl -X POST https://api.integration-gateway.com/agent/sessions \
  -H "Authorization: Bearer $INTEGRATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "为Jira（https://company.atlassian.net）构建连接器，支持创建Issue与查询项目"}'

# 轮询状态（state为idle或status为completed即完成）
curl "https://api.integration-gateway.com/agent/sessions/sess_xyz?wait=true&timeout=30" \
  -H "Authorization: Bearer $INTEGRATION_TOKEN"

# 发送后续指令（如需调整）
curl -X POST https://api.integration-gateway.com/agent/sessions/sess_xyz/message \
  -H "Authorization: Bearer $INTEGRATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"input": "创建Issue时需要支持指定优先级字段"}'

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
        sku: "相关信息"
    - id: branch
      if: "处理结果"
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
        text: "订单 相关信息 处理完成"
```

## 常见问题

### Q1：自定义连接器构建需要多长时间？
A：取决于目标应用API的复杂度。简单REST API通常1-3分钟，复杂API（如需OAuth流程）可能5-10分钟。构建过程中可通过会话消息交互调整。

### Q2：工作流执行失败如何排查？
A：查看工作流运行日志，定位失败步骤。专业版记录每步的输入、输出与错误信息。常见原因包括连接失效（需重新授权）、入参不符Schema、目标应用限流。

### Q3：批量动作部分失败怎么办？
A：根据配置策略处理。若配置为"全部尝试"，失败的动作会在结果中标记；若配置为"任一失败即停止"，后续动作不执行。失败的可通过重试接口单独重试。

### Q4：可以连接多少个外部应用？
A：专业版不限制连接数量。每个连接独立管理，按应用维度组织。

### Q5：审计日志会记录敏感数据吗？
A：不会。入参记录哈希值而非原值，连接凭据由网关托管不记录。日志仅记录操作者、时间、动作、状态等元数据。

### Q6：Agent会话构建连接器失败怎么办？
A：可通过会话消息补充信息（如API文档链接、认证方式说明）让Agent重新尝试。也可中止会话后用更详细的prompt重新开始。

### Q7：如何对接MCP工具生态？
A：专业版提供MCP端点集成适配，MCP工具通过本工具建立连接并执行动作。配置MCP server时指定本工具的网关地址与Token，MCP端点即可操作任意外部应用。

### Q8：工作流支持定时触发吗？
A：支持。工作流触发器可配置为cron表达式定时触发，适合定期同步等场景。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

