---
slug: azure-cloud-automator
name: azure-cloud-automator
version: 1.0.1
displayName: Azure云自动化
summary: Azure云自动化:基础设施即代码+成本优化+无服务器架构,云上运维一站搞定
license: Proprietary
description: Azure云自动化——基于Azure云最佳实践，从基础设施即代码到成本优化，从无服务器架构到安全合规，云上运维一站搞定。适用于基础设施部署、成本优化、架构设计、运维自动化、合规审计等场景。支持Bicep/Terraform
  IaC、Azure Functions无服务器、事件驱动架构、监控告警。国内场景可迁移至阿里云/腾讯云。触发关键词：Azure、云自动化、Bicep、ARM模板、无服务器、事件驱动、云成本、云架构、IaC
tags:
- Azure
- 云自动化
- 基础设施即代码
- 成本优化
- 无服务器
tools:
- read
- exec
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "write", "exec"]
tags: "Azure,云计算,DevOps"
---
# Azure云自动化

Azure 云最佳实践与自动化。从基础设施即代码到成本优化，从无服务器架构到安全合规。

## 核心能力

- **基础设施即代码（IaC）**：Bicep（Azure 原生）/ ARM 模板 / Terraform（多云）/ Azure CDK，资源组分层与环境参数化
- **无服务器与事件驱动**：Azure Functions（触发器+绑定）+ Event Grid（事件发布订阅）+ Logic Apps（可视化工作流）+ Saga/CQRS 模式
- **成本优化**：按资源/标签/部门拆分成本分析 + 预留实例/Spot VM/自动缩放 + 存储生命周期管理 + 预算告警
- **监控与可观测性**：Azure Monitor（指标+日志+告警）+ Application Insights（APM+分布式追踪）+ Log Analytics（KQL 查询）
- **安全与合规**：Azure AD + RBAC + 托管身份 + Key Vault 密钥管理 + Azure Policy 合规检查 + Defender for Cloud

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 基础设施部署 | 资源清单 + 环境分层需求 | Bicep/Terraform 模板 + 部署流水线 + 参数化配置 |
| 成本优化 | 云费用账单 + 资源使用数据 | 成本分析报告 + 优化建议清单 + 预算告警配置 |
| 架构设计 | 业务需求 + SLA 要求 | 架构图 + 无服务器/事件驱动方案 + 资源选型 |
| 运维自动化 | 日常运维任务清单 | Runbook 自动化脚本 + 自动缩放规则 + 备份恢复策略 |
| 合规审计 | 合规框架要求(ISO/SOC2) | Azure Policy 配置 + 合规检查报告 + 安全评分 |
| 国内迁移 | Azure 架构 + 迁移需求 | 阿里云/腾讯云对等架构 + 迁移路径 + 配置映射表 |

**不适用于**：
- 本地数据中心运维（非云场景）
- 具体业务代码开发（属应用层而非基础设施层）
- 网络设备配置（交换机/路由器，属网络工程师职责）
- 数据库性能调优（属 DBA 职责）

## 使用流程

### Step 1: 选择 IaC 工具
- Bicep（推荐，Azure 原生，语法简洁）
- ARM 模板（JSON，传统，兼容性好）
- Terraform（多云，适合跨云场景）
- Azure CDK（编程式，TypeScript/Python）

### Step 2: 定义资源结构
- 资源组（Resource Group）：按环境/项目/部门划分
- 计算：App Service / Functions / AKS / VM
- 存储：Storage Account / Cosmos DB / SQL Database
- 网络：VNet / Subnet / NSG / Load Balancer
- 监控：Application Insights / Log Analytics

### Step 3: 环境参数化
- Dev/Staging/Prod 独立资源组
- 参数文件分离（`parameters.dev.json` / `parameters.prod.json`）
- 密钥通过 Key Vault 引用，不硬编码

### Step 4: 设计无服务器架构
- Azure Functions：选择触发器（HTTP/Timer/Service Bus/Event Grid/Cosmos DB）
- 事件网格：系统主题（资源事件）+ 自定义主题
- Logic Apps：可视化工作流 + 200+ 连接器
- 架构模式：事件溯源 / CQRS / Saga

### Step 5: 成本优化配置
- 计算：预留实例（1年/3年）+ Spot VM（可中断）+ 自动缩放规则
- 存储：生命周期管理（热→冷→归档）+ 冗余级别选择（LRS/GRS）
- 网络：VNet 对等减少出站流量 + CDN 加速
- 预算：设定预算阈值 + 超限告警 + 自动通知

### Step 6: 配置监控与安全
- Azure Monitor：指标告警 + 日志查询 + 异常检测
- Application Insights：APM + 分布式追踪 + 可用性测试
- 安全：Azure AD 集成 + RBAC 最小权限 + 托管身份 + Key Vault
- 合规：Azure Policy 合规检查 + Defender for Cloud 安全评分

### Step 7: 输出交付物
- IaC 模板：`output/{project}/infra/`
- 架构图：`output/{project}/architecture.md`
- 成本报告：`output/{project}/cost-report.md`
- 部署指南：`output/{project}/deployment.md`
- 监控配置：`output/{project}/monitoring/`

## 示例

### 示例 1：Web 应用基础设施部署

**输入**：
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Azure云自动化处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
需求：部署一个 Web 应用，包含 App Service + SQL Database + Storage Account。
环境：Dev/Staging/Prod 三套。需要参数化配置。
```

**输出**：
```bicep
// main.bicep
param environment string {
  allowed: ['dev', 'staging', 'prod']
  default: 'dev'
}
param appName string
param sqlAdminPassword string  // 从 Key Vault 引用，不硬编码
# ...
var location = resourceGroup().location
var namePrefix = '${appName}-${environment}'
var skuMap = {
  dev: { appService: 'F1', sql: 'Basic', storage: 'Standard_LRS' }
  staging: { appService: 'S1', sql: 'S0', storage: 'Standard_GRS' }
  prod: { appService: 'P1v2', sql: 'S1', storage: 'Standard_GRS' }
}
# ...
resource appService 'Microsoft.Web/sites@2023-12-01' = {
  name: '${namePrefix}-app'
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      netFrameworkVersion: 'v8.0'
      minTlsVersion: '1.2'
      httpsOnly: true
    }
  }
}
# ...
resource sqlServer 'Microsoft.Sql/servers@2023-08-01-preview' = {
  name: '${namePrefix}-sql'
  location: location
  properties: {
    administratorLogin: 'sqladmin'
    administratorLoginPassword: sqlAdminPassword
    minimalTlsVersion: '1.2'
  }
}
# ...
resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: '${replace(namePrefix, '-', '')}storage'
  location: location
  sku: { name: skuMap[environment].storage }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
}
# ...
output appServiceUrl string = 'https://${appService.properties.defaultHostName}'
output sqlServerFqdn string = sqlServer.properties.fullyQualifiedDomainName
```

```json
// parameters.prod.json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "environment": { "value": "prod" },
    "appName": { "value": "myapp" },
    "sqlAdminPassword": {
      "reference": {
        "keyVault": { "id": "/subscriptions/.../vaults/myvault" },
        "secretName": "sqlAdminPassword"
      }
    }
  }
}
```

### 示例 2：成本优化报告

**输入**：
```
需求：分析当前 Azure 订阅的成本，月均 $10,000，需要优化建议。
```

**输出**：
```markdown
# 成本优化报告
# ...
## 成本分布（上月）
| 资源类型 | 月成本 | 占比 | 优化潜力 |
|---:|---:|---:|---:|
| AKS 集群 | $3,500 | 35% | 高（Spot VM + 自动缩放） |
| SQL Database | $2,000 | 20% | 中（预留实例） |
| Storage Account | $1,500 | 15% | 中（冷数据归档） |
| App Service | $1,200 | 12% | 低（已优化） |
| 出站流量 | $1,000 | 10% | 中（VNet 对等） |
| 其他 | $800 | 8% | - |
# ...
## 优化建议
1. **AKS Spot VM**（预计节省 $1,500/月）
   - 将非关键工作负载迁移到 Spot 节点池
   - 配置中断通知 + 自动重调度
2. **SQL 预留实例**（预计节省 $600/月）
   - 1 年预留实例折扣 30%
3. **存储生命周期**（预计节省 $500/月）
   - 30 天前数据自动转冷层
   - 90 天前数据自动转归档层
4. **预算告警**
   - 月预算 $8,000，80% 告警，100% 通知
# ...
## 预计优化后成本
$7,400/月（节省 26%）
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 部署失败 | IaC 模板语法错误或资源冲突 | 使用 `az deployment group validate` 预校验，查看 `deploymentOperations` 排查 |
| 资源配额超限 | 订阅区域配额不足 | 申请配额提升或选择其他区域 |
| Key Vault 引用失败 | 权限不足或 Key Vault 不存在 | 确认托管身份已授予 `Key Vault Secrets User` 角色 |
| Functions 冷启动 | 消费计划空闲后首次请求慢 | 升级到 Premium 计划或配置 `alwaysReady` 实例 |
| 成本超预算 | 资源未配置自动缩放或预留不足 | 设置预算告警 + 自动缩放规则 + 定期成本审查 |
| 跨区域延迟 | 资源分布在不同区域 | 使用 VNet 对等或 CDN 加速，关键资源同区域部署 |
| Terraform 状态冲突 | 多人同时操作状态文件 | 使用远程后端（Azure Storage）+ 状态锁定 |

## 依赖说明

### 运行环境
- **Agent 平台**：Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持 SKILL.md 的任意 Agent
- **操作系统**：Windows / macOS / Linux
- **运行时**：需要 Agent 支持 exec（命令行执行）能力

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Azure CLI | 工具 | 必需（部署时） | `az` 命令行工具 |
| Bicep | 工具 | 可选 | Azure CLI 内置 `az bicep` |
| Terraform | 工具 | 可选 | 多云 IaC 场景 |
| Azure 订阅 | 服务 | 必需（部署时） | Azure 官网注册 |
| 国内云账号 | 服务 | 可选 | 阿里云/腾讯云（国内迁移场景） |

### 国内替代方案
| Azure 服务 | 阿里云替代 | 腾讯云替代 | 说明 |
|-----:|:-----|-----:|-----:|
| App Service | 阿里云轻量应用服务器 / 函数计算 | 腾讯云 SCF / 轻量应用服务器 | Web 应用托管 |
| Azure Functions | 阿里云函数计算（FC） | 腾讯云云函数（SCF） | 无服务器函数 |
| Cosmos DB | 阿里云表格存储 / MongoDB | 腾讯云 TcaplusDB / MongoDB | NoSQL 数据库 |
| SQL Database | 阿里云 RDS SQL Server | 腾讯云 TDSQL-C | 关系型数据库 |
| Storage Account | 阿里云 OSS | 腾讯云 COS | 对象存储 |
| Event Grid | 阿里云事件总线（EventBridge） | 腾讯云事件总线（EventBridge） | 事件驱动 |
| Azure Monitor | 阿里云监控 / 日志服务 SLS | 腾讯云监控 / CLS | 监控告警 |
| Key Vault | 阿里云 KMS | 腾讯云 KMS | 密钥管理 |
| Azure AD | 阿里云 IDaaS | 腾讯云身份管家 | 身份认证 |
| AKS | 阿里云 ACK | 腾讯云 TKE | Kubernetes 托管 |

### API Key 配置
- **AZURE_SUBSCRIPTION_ID**：必需（部署时），从 Azure Portal 获取
- **AZURE_CREDENTIALS**：必需（部署时），服务主体认证凭据
- 配置方式：在 Agent 的环境变量或 `.env` 文件中设置
- **Skill 内零硬编码**，所有凭据通过环境变量引用

### 可用性分类
- **分类**：MD + EXEC
- **说明**：纯 Markdown 方法论，实际部署需要 Azure 订阅和 CLI 工具，纯设计阶段无需额外依赖

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: Web应用三环境IaC部署

**输入**:
```
需求: 为电商Web应用部署Azure基础设施。
要求:
1. 包含App Service + SQL Database + Storage Account + Application Insights
2. Dev/Staging/Prod三套环境，参数化配置
3. 数据库密码通过Key Vault引用，不硬编码
4. 生产环境强制HTTPS、TLS 1.2+
项目名: shopapp
```

**LLM生成输出**:
```bicep
// output/shopapp/infra/main.bicep
targetScope = 'resourceGroup'
# ...
@description('环境')
param environment string {
  allowed: ['dev', 'staging', 'prod']
  default: 'dev'
}
# ...
@description('应用名')
param appName string
# ...
@description('SQL管理员密码 (Key Vault引用)')
@secure()
param sqlAdminPassword string
# ...
@description('数据库容量(GB)')
param dbCapacityGB int = 50
# ...
var location = resourceGroup().location
var namePrefix = '${appName}-${environment}'
var uniqueSuffix = uniqueString(resourceGroup().id)
# ...
// 各环境的SKU配置
var skuMap = {
  dev: {
    appServicePlan: 'F1'
    appService: { tier: 'Shared', size: 'D1' }
    sql: { tier: 'Basic', capacity: 5 }
    storage: 'Standard_LRS'
    storageReplication: 'LRS'
  }
  staging: {
    appServicePlan: 'S1'
    appService: { tier: 'Standard', size: 'S1' }
    sql: { tier: 'Standard', capacity: 10 }
    storage: 'Standard_GRS'
    storageReplication: 'GRS'
  }
  prod: {
    appServicePlan: 'P1v2'
    appService: { tier: 'PremiumV2', size: 'P1v2' }
    sql: { tier: 'Standard', capacity: 50 }
    storage: 'Standard_GRS'
    storageReplication: 'GRS'
  }
}
# ...
// App Service Plan
resource appServicePlan 'Microsoft.Web/serverfarms@2023-12-01' = {
  name: '${namePrefix}-plan'
  location: location
  sku: {
    name: skuMap[environment].appServicePlan
    capacity: (environment == 'prod') ? 3 : 1  // 生产3实例
  }
  properties: { reserved: false }
}
# ...
// App Service
resource appService 'Microsoft.Web/sites@2023-12-01' = {
  name: '${namePrefix}-app-${uniqueSuffix}'
  location: location
  identity: {
    type: 'SystemAssigned'  // 托管身份，访问Key Vault
  }
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      netFrameworkVersion: 'v8.0'
      minTlsVersion: '1.2'        // 强制TLS 1.2+
      httpsOnly: true              // 强制HTTPS
      ftpsState: 'Disabled'        // 禁用FTP
      http20Enabled: true
    }
  }
  tags: {
    environment: environment
    project: appName
  }
}
# ...
// SQL Server
resource sqlServer 'Microsoft.Sql/servers@2023-08-01-preview' = {
  name: '${namePrefix}-sql-${uniqueSuffix}'
  location: location
  properties: {
    administratorLogin: 'sqladmin'
    administratorLoginPassword: sqlAdminPassword
    minimalTlsVersion: '1.2'
    publicNetworkAccess: (environment == 'prod') ? 'Disabled' : 'Enabled'
  }
  tags: { environment: environment, project: appName }
}
# ...
// SQL Database
resource sqlDatabase 'Microsoft.Sql/servers/databases@2023-08-01-preview' = {
  parent: sqlServer
  name: '${appName}db'
  location: location
  sku: {
    name: skuMap[environment].sql.tier
    capacity: skuMap[environment].sql.capacity
  }
  properties: {
    collation: 'SQL_Latin1_General_CP1_CI_AS'
    maxSizeBytes: dbCapacityGB * 1024 * 1024 * 1024
  }
}
# ...
// Storage Account
resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: '${replace(namePrefix, '-', '')}storage${uniqueSuffix}'
  location: location
  sku: { name: skuMap[environment].storage }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false       // 禁止公开访问
    supportsHttpsTrafficOnly: true
    networkAcls: {
      defaultAction: (environment == 'prod') ? 'Deny' : 'Allow'
    }
  }
  tags: { environment: environment, project: appName }
}
# ...
// Application Insights
resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: '${namePrefix}-ai'
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    SamplingPercentage: (environment == 'prod') ? 10 : 100
  }
}
# ...
// 输出
output appServiceUrl string = 'https://${appService.properties.defaultHostName}'
output sqlServerFqdn string = sqlServer.properties.fullyQualifiedDomainName
output appInsightsInstrumentationKey string = appInsights.properties.InstrumentationKey
output storageAccountName string = storage.name
```

```json
// output/shopapp/infra/parameters.prod.json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "environment": { "value": "prod" },
    "appName": { "value": "shopapp" },
    "dbCapacityGB": { "value": 100 },
    "sqlAdminPassword": {
      "reference": {
        "keyVault": { "id": "/subscriptions/abc123/resourceGroups/shopapp-prod-rg/providers/Microsoft.KeyVault/vaults/shopapp-prod-kv" },
        "secretName": "sqlAdminPassword"
      }
    }
  }
}
```

```markdown
# output/shopapp/deployment.md
## 部署命令
# Dev环境
az deployment group create \
  --resource-group shopapp-dev-rg \
  --template-file main.bicep \
  --parameters @parameters.dev.json
# ...
# Prod环境（密钥从Key Vault引用）
az deployment group create \
  --resource-group shopapp-prod-rg \
  --template-file main.bicep \
  --parameters @parameters.prod.json
# ...
## Key Vault配置
1. 创建Key Vault: shopapp-prod-kv
2. 授予App Service托管身份 "Key Vault Secrets User" 角色
3. 存储SQL密码: az keyvault secret set --vault-name shopapp-prod-kv --name sqlAdminPassword --value <password>
```

**效果验证**: ✓三环境参数化分离 ✓Key Vault密钥引用（零硬编码） ✓生产环境强制HTTPS+TLS 1.2 ✓托管身份访问Key Vault ✓生产环境3实例高可用

### 案例2: 无服务器事件驱动架构

**输入**:
```
需求: 设计订单处理事件驱动架构。
流程: 订单创建 → 库存检查 → 支付处理 → 物流通知 → 订单完成
要求: 使用Azure Functions + Event Grid，支持Saga模式补偿事务
```

**LLM生成输出**:
```python
# output/order-saga/functions/order_orchestrator.py
# Saga协调器：编排订单处理流程
import azure.functions as func
import json
import logging
from azure.eventgrid import EventGridPublisherClient
# ...
app = func.FunctionApp()
# ...
# Saga状态机
SAGA_STEPS = [
    {"name": "create_order", "compensate": "cancel_order"},
    {"name": "check_inventory", "compensate": "release_inventory"},
    {"name": "process_payment", "compensate": "refund_payment"},
    {"name": "notify_logistics", "compensate": "cancel_logistics"},
]
# ...
@app.event_grid_message(argument_name="event")
def order_saga_orchestrator(event: func.EventGridEvent):
    """Saga协调器: 监听订单事件，编排后续步骤"""
    data = event.get_json()
    order_id = data["orderId"]
    current_step = data.get("currentStep", 0)
# ...
    logging.info(f"Processing order {order_id}, step {current_step}")
# ...
    if current_step >= len(SAGA_STEPS):
        # 所有步骤完成
        publish_event("order_completed", {"orderId": order_id})
        return
# ...
    step = SAGA_STEPS[current_step]
    try:
        # 发布步骤事件
        publish_event(step["name"], {
            "orderId": order_id,
            "currentStep": current_step,
            "data": data
        })
    except Exception as e:
        # 触发补偿
        trigger_compensation(order_id, current_step)
        logging.error(f"Saga failed at step {step['name']}: {e}")
# ...
def trigger_compensation(order_id: str, failed_step: int):
    """触发补偿事务（反向执行已完成步骤的补偿）"""
    for i in range(failed_step - 1, -1, -1):
        compensate_action = SAGA_STEPS[i]["compensate"]
        publish_event(compensate_action, {"orderId": order_id})
    publish_event("order_failed", {"orderId": order_id, "failedAt": failed_step})
```

```python
# output/order-saga/functions/inventory_check.py
import azure.functions as func
import json
# ...
app = func.FunctionApp()
# ...
@app.event_grid_message(argument_name="event")
def check_inventory(event: func.EventGridEvent):
    """库存检查: 监听check_inventory事件"""
    data = event.get_json()
    order_id = data["orderId"]
    items = data["data"]["items"]
# ...
    # 检查库存
    inventory_ok = check_stock(items)
# ...
    if inventory_ok:
        # 锁定库存，继续下一步
        lock_stock(items, order_id)
        publish_event("order_step_completed", {
            "orderId": order_id,
            "currentStep": data["currentStep"] + 1,
            "data": data["data"]
        })
    else:
        # 库存不足，触发补偿
        publish_event("order_step_failed", {
            "orderId": order_id,
            "failedStep": data["currentStep"],
            "reason": "INSUFFICIENT_STOCK"
        })
# ...
@app.event_grid_message(argument_name="event")
def release_inventory(event: func.EventGridEvent):
    """补偿: 释放库存"""
    data = event.get_json()
    release_stock(data["orderId"])
```

```python
# output/order-saga/functions/payment_processor.py
import azure.functions as func
# ...
app = func.FunctionApp()
# ...
@app.event_grid_message(argument_name="event")
def process_payment(event: func.EventGridEvent):
    """支付处理: 幂等性设计"""
    data = event.get_json()
    order_id = data["orderId"]
# ...
    # 幂等检查: 防止重复扣款
    if is_payment_processed(order_id):
        return  # 已处理，跳过
# ...
    try:
        charge_payment(order_id, data["data"]["amount"])
        mark_payment_processed(order_id)
# ...
        publish_event("order_step_completed", {
            "orderId": order_id,
            "currentStep": data["currentStep"] + 1,
            "data": data["data"]
        })
    except PaymentFailedException:
        publish_event("order_step_failed", {
            "orderId": order_id,
            "failedStep": data["currentStep"],
            "reason": "PAYMENT_FAILED"
        })
# ...
@app.event_grid_message(argument_name="event")
def refund_payment(event: func.EventGridEvent):
    """补偿: 退款"""
    data = event.get_json()
    refund_order(data["orderId"])
```

```bicep
// output/order-saga/infra/functions.bicep
param location string = resourceGroup().location
param storageAccountName string
# ...
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageAccountName
  location: location
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
}
# ...
resource functionApp 'Microsoft.Web/sites@2023-12-01' = {
  name: 'order-saga-func'
  location: location
  kind: 'functionapp,linux'
  properties: {
    siteConfig: {
      linuxFxVersion: 'Python|3.11'
      appSettings: [
        { name: 'AzureWebJobsStorage', value: '@Microsoft.KeyVault(...)' }
        { name: 'EVENT_GRID_TOPIC_ENDPOINT', value: eventGridTopic.endpoint }
        { name: 'EVENT_GRID_TOPIC_KEY', value: '@Microsoft.KeyVault(...)' }
        { name: 'DATABASE_URL', value: '@Microsoft.KeyVault(...)' }
      ]
    }
  }
}
# ...
resource eventGridTopic 'Microsoft.EventGrid/topics@2023-12-15-preview' = {
  name: 'order-events'
  location: location
  properties: { inputSchema: 'CloudEventSchemaV1_0' }
}
```

**效果验证**: ✓Saga模式补偿事务完整 ✓4步骤编排正确 ✓幂等性设计（防重复扣款） ✓Event Grid事件驱动 ✓补偿函数反向执行

### 案例3: 成本优化分析与预算告警

**输入**:
```
需求: 分析Azure订阅成本，月均$15,000，识别优化机会。
要求:
1. 按资源类型/标签/部门拆分成本
2. 提供优化建议（预计节省金额）
3. 配置预算告警（80%警告，100%通知）
```

**LLM生成输出**:
```python
# output/cost-optimization/analyze_cost.py
from azure.mgmt.costmanagement import CostManagementClient
from azure.identity import DefaultAzureCredential
import pandas as pd
# ...
credential = DefaultAzureCredential()
client = CostManagementClient(credential)
# ...
subscription_id = "abc-123-456"
# ...
# 1. 按资源类型查询成本
query_result = client.query.usage(
    f"/subscriptions/{subscription_id}",
    {
        "type": "ActualCost",
        "timeframe": "MonthToDate",
        "dataset": {
            "granularity": "Daily",
            "aggregation": {
                "totalCost": {"name": "Cost", "function": "Sum"}
            },
            "grouping": [
                {"type": "Dimension", "name": "ResourceType"}
            ]
        }
    }
)
# ...
# 转换为DataFrame分析
rows = []
for row in query_result.rows:
    rows.append({
        "date": row[0],
        "resource_type": row[1],
        "cost": row[2],
        "currency": row[3]
    })
df = pd.DataFrame(rows)
# ...
# 2. 按资源类型汇总
cost_by_type = df.groupby("resource_type")["cost"].sum().sort_values(ascending=False)
print("成本分布（按资源类型）:")
print(cost_by_type)
# ...
# 3. 按标签（部门）查询
tag_query = client.query.usage(
    f"/subscriptions/{subscription_id}",
    {
        "type": "ActualCost",
        "timeframe": "MonthToDate",
        "dataset": {
            "granularity": "None",
            "aggregation": {"totalCost": {"name": "Cost", "function": "Sum"}},
            "grouping": [{"type": "Tag", "name": "Department"}]
        }
    }
)
```

```markdown
# output/cost-optimization/cost-report.md
# Azure成本优化报告
# ...
## 1. 成本总览
- **本月总成本**: $15,234.56
- **环比上月**: +8.2% ($1,156增加)
- **预测月末**: $16,800（超预算$1,800）
# ...
## 2. 成本分布
# ...
### 按资源类型
| 资源类型 | 月成本 | 占比 | 趋势 | 优化潜力 |
|:------:|--------|:-------|:------:|--------|
| AKS集群 | $5,200 | 34% | ↑12% | 高（Spot VM） |
| SQL Database | $3,800 | 25% | →0% | 中（预留实例） |
| Storage Account | $2,100 | 14% | ↑5% | 中（冷数据归档） |
| App Service | $1,800 | 12% | →0% | 低（已优化） |
| 虚拟机 | $1,500 | 10% | ↑8% | 高（自动缩放） |
| 出站流量 | $834 | 5% | →0% | 中（VNet对等） |
# ...
### 按部门标签
| 部门 | 月成本 | 占比 |
|----|:--:|---:|
| 工程部 | $6,500 | 43% |
| 数据部 | $4,200 | 28% |
| 运营部 | $2,800 | 18% |
| 未标记 | $1,734 | 11% |
# ...
## 3. 优化建议（预计节省 $4,650/月, 30%）
# ...
### 高优先级
1. **AKS Spot VM节点池**（节省 $1,800/月）
   - 将非关键工作负载迁移到Spot节点池
   - 配置中断通知 + 自动重调度
   - 风险: Spot实例可能被抢占
# ...
2. **VM自动缩放**（节省 $800/月）
   - 工作时间8-22点: 3实例
   - 非工作时间: 1实例
   - 周末: 1实例
# ...
### 中优先级
3. **SQL预留实例**（节省 $1,140/月）
   - 1年预留: 30%折扣
   - 3年预留: 55%折扣（长期稳定负载推荐）
# ...
4. **存储生命周期管理**（节省 $630/月）
   - 30天前数据: 转冷层（Cool）
   - 90天前数据: 转归档层（Archive）
   - 归档层成本仅为热层的$0.002/GB vs $0.045/GB
# ...
5. **VNet对等**（节省 $280/月）
   - 跨区域流量改为VNet对等
   - 出站流量成本从$0.087/GB降至$0.035/GB
# ...
## 4. 预算告警配置
```

```bicep
# output/cost-optimization/budget-alert.bicep
param subscriptionId string
param budgetAmount int = 15000  # 月预算$15,000
param alertEmail string
# ...
resource budget 'Microsoft.Consumption/budgets@2023-05-01' = {
  name: 'monthly-budget'
  properties: {
    amount: budgetAmount
    timeGrain: 'Monthly'
    timePeriod: {
      startDate: '2024-01-01T00:00:00Z'
      endDate: '2025-12-31T23:59:59Z'
    }
    filter: {
      dimensions: {
        name: 'ResourceId'
        values: []
      }
    }
    notifications: {
      '80-percent-warning': {
        enabled: true
        operator: 'GreaterThanEqualTo'
        threshold: 80
        contactEmails: [alertEmail]
        contactRoles: ['Owner', 'Contributor']
        locale: 'en-us'
      }
      '100-percent-alert': {
        enabled: true
        operator: 'GreaterThanEqualTo'
        threshold: 100
        contactEmails: [alertEmail]
        contactRoles: ['Owner']
        locale: 'en-us'
      }
    }
  }
}
```

**效果验证**: ✓成本按资源类型/部门拆分 ✓5项优化建议含预计节省金额 ✓预算80%警告+100%通知 ✓优化潜力分级 ✓总节省30%可量化

### 案例4: Azure监控告警配置

**输入**:
```
需求: 为生产环境App Service配置监控告警。
要求:
1. CPU使用率 > 80% 持续5分钟告警
2. HTTP 5xx错误率 > 5% 告警
3. 响应时间P95 > 2秒告警
4. 健康检查探针失败告警
5. 告警分级: 严重/警告/信息
```

**LLM生成输出**:
```bicep
// output/monitoring/alerts.bicep
param appServiceName string
param appInsightsName string
param actionGroupEmail string
# ...
// Action Group（告警通知组）
resource criticalActionGroup 'Microsoft.Insights/actionGroups@2023-01-01' = {
  name: 'critical-alerts'
  location: 'Global'
  properties: {
    groupShortName: 'critical'
    enabled: true
    emailReceivers: [
      {
        name: 'ops-team'
        emailAddress: actionGroupEmail
        useCommonAlertSchema: true
      }
    ]
    webhookReceivers: [
      {
        name: 'pagerduty'
        serviceUri: 'https://events.pagerduty.com/integration/xxx/enqueue'
        useCommonAlertSchema: true
      }
    ]
  }
}
# ...
resource warningActionGroup 'Microsoft.Insights/actionGroups@2023-01-01' = {
  name: 'warning-alerts'
  location: 'Global'
  properties: {
    groupShortName: 'warning'
    enabled: true
    emailReceivers: [
      { name: 'dev-team', emailAddress: actionGroupEmail, useCommonAlertSchema: true }
    ]
  }
}
# ...
// 1. CPU使用率告警（严重）
resource cpuAlert 'Microsoft.Insights/metricAlerts@2023-03-01-preview' = {
  name: 'cpu-high-critical'
  location: 'Global'
  properties: {
    severity: 0  // 0=Severe, 1=Warning, 2=Info, 3=Verbose
    enabled: true
    scopes: [resourceId('Microsoft.Web/sites', appServiceName)]
    evaluationFrequency: 'PT1M'
    windowSize: 'PT5M'
    criteria: {
      'allOf': [
        {
          metricName: 'CpuPercentage'
          operator: 'GreaterThan'
          threshold: 80
          timeAggregation: 'Average'
          criterionType: 'StaticThresholdCriterion'
        }
      ]
    }
    actions: [
      { actionGroupId: criticalActionGroup.id }
    ]
  }
}
# ...
// 2. HTTP 5xx错误率告警（严重）
resource http5xxAlert 'Microsoft.Insights/metricAlerts@2023-03-01-preview' = {
  name: 'http-5xx-critical'
  location: 'Global'
  properties: {
    severity: 0
    enabled: true
    scopes: [resourceId('Microsoft.Web/sites', appServiceName)]
    evaluationFrequency: 'PT1M'
    windowSize: 'PT5M'
    criteria: {
      'allOf': [
        {
          metricName: 'Http5xx'
          operator: 'GreaterThan'
          threshold: 10  // 5分钟内超过10次5xx错误
          timeAggregation: 'Count'
        }
      ]
    }
    actions: [{ actionGroupId: criticalActionGroup.id }]
  }
}
# ...
// 3. 响应时间P95告警（警告）
resource responseTimeAlert 'Microsoft.Insights/metricAlerts@2023-03-01-preview' = {
  name: 'response-time-p95-warning'
  location: 'Global'
  properties: {
    severity: 1
    enabled: true
    scopes: [resourceId('Microsoft.Insights/components', appInsightsName)]
    evaluationFrequency: 'PT5M'
    windowSize: 'PT15M'
    criteria: {
      'allOf': [
        {
          metricNamespace: 'Microsoft.Insights/Components'
          metricName: 'requests/duration'
          operator: 'GreaterThan'
          threshold: 2000  // 2000ms = 2秒
          timeAggregation: 'Percentile'
          criterionType: 'StaticThresholdCriterion'
        }
      ]
    }
    actions: [{ actionGroupId: warningActionGroup.id }]
  }
}
# ...
// 4. 健康检查探针告警（严重）
resource healthCheckAlert 'Microsoft.Insights/metricAlerts@2023-03-01-preview' = {
  name: 'health-check-failed-critical'
  location: 'Global'
  properties: {
    severity: 0
    enabled: true
    scopes: [resourceId('Microsoft.Web/sites', appServiceName)]
    evaluationFrequency: 'PT1M'
    windowSize: 'PT2M'
    criteria: {
      'allOf': [
        {
          metricName: 'HealthCheckStatus'
          operator: 'LessThan'
          threshold: 1
          timeAggregation: 'Average'
        }
      ]
    }
    actions: [{ actionGroupId: criticalActionGroup.id }]
  }
}
# ...
// 5. CPU使用率早期预警（信息）
resource cpuEarlyWarningAlert 'Microsoft.Insights/metricAlerts@2023-03-01-preview' = {
  name: 'cpu-medium-info'
  location: 'Global'
  properties: {
    severity: 2  // 2=Info
    enabled: true
    scopes: [resourceId('Microsoft.Web/sites', appServiceName)]
    evaluationFrequency: 'PT5M'
    windowSize: 'PT10M'
    criteria: {
      'allOf': [
        {
          metricName: 'CpuPercentage'
          operator: 'GreaterThan'
          threshold: 60
          timeAggregation: 'Average'
          criterionType: 'StaticThresholdCriterion'
        }
      ]
    }
    actions: [{ actionGroupId: warningActionGroup.id }]
  }
}
```

```kql
// output/monitoring/diagnostic-queries.kql
// 1. 查询最近1小时5xx错误
requests
| where timestamp > ago(1h)
| where resultCode >= 500
| summarize count() by resultCode, url
| order by count_ desc
# ...
// 2. P95响应时间趋势
requests
| where timestamp > ago(24h)
| summarize p95 = percentile(duration, 95) by bin(timestamp, 1h)
| render timechart
# ...
// 3. 最慢的10个请求
requests
| where timestamp > ago(1h)
| top 10 by duration desc
| project timestamp, url, duration, resultCode
# ...
// 4. 异常依赖调用
dependencies
| where timestamp > ago(1h)
| where success == false
| summarize count() by name, type
```

**效果验证**: ✓CPU>80%持续5分钟告警 ✓5xx错误率告警 ✓P95响应时间告警 ✓健康检查探针告警 ✓三级严重度分级

### 案例5: 国内云迁移架构映射

**输入**:
```
需求: 将现有Azure架构迁移到阿里云，保持功能对等。
现有Azure资源:
- App Service (P1v2, 3实例)
- SQL Database (Standard S1, 50GB)
- Storage Account (GRS, Hot/Cool/Archive)
- Azure Functions (消费计划)
- Event Grid
- Application Insights
- Key Vault
- Azure AD
要求: 提供完整的映射表和迁移路径
```

**LLM生成输出**:
```markdown
# output/aliyun-migration/migration-plan.md
# Azure → 阿里云迁移方案
# ...
## 1. 服务映射表
# ...
| Azure服务 | 阿里云对等服务 | 配置映射 | 迁移难度 |
|-------|-------|-------|-------|
| App Service (P1v2, 3实例) | 阿里云轻量应用服务器 / 函数计算 | P1v2→2核4G, 3实例→3台SLB后端 | 中 |
| SQL Database (S1, 50GB) | 阿里云RDS SQL Server | S1→高可用版 1核2G, 50GB存储 | 低 |
| Storage Account (GRS) | 阿里云OSS | GRS→跨区域复制, Hot/Cool/Archive→标准/低频/归档 | 低 |
| Azure Functions | 阿里云函数计算FC | 消费计划→按量付费, Python 3.11支持 | 中 |
| Event Grid | 阿里云事件总线EventBridge | 自定义主题→自定义事件总线 | 中 |
| Application Insights | 阿里云ARMS + SLS | APM→ARMS, 日志→SLS | 高 |
| Key Vault | 阿里云KMS + 凭据管家 | 密钥管理→KMS, 凭据→凭据管家 | 低 |
| Azure AD | 阿里云IDaaS | 用户/组/SSO→IDaaS完整支持 | 中 |
# ...
## 2. 迁移路径（6周计划）
# ...
### 第1-2周: 基础设施迁移
1. **RDS迁移**（DTS工具）
   - 创建阿里云RDS实例（同版本SQL Server）
   - 使用DTS全量+增量迁移
   - 验证数据一致性后切换
# ...
2. **OSS迁移**（ossutil工具）
   - 创建OSS Bucket（跨区域复制）
   - 使用ossutil批量迁移对象
   - 配置生命周期规则（30天→低频, 90天→归档）
# ...
3. **KMS迁移**
   - 在KMS创建对应密钥
   - 更新应用配置引用新密钥ID
# ...
### 第3-4周: 应用层迁移
1. **App Service → 轻量应用服务器**
   - Docker化应用（如未容器化）
   - 部署到轻量应用服务器
   - 配置SLB负载均衡（3实例）
   - 配置HTTPS证书
# ...
2. **Azure Functions → 函数计算FC**
   - 改写触发器绑定（Event Grid → EventBridge）
   - 调整SDK调用（Azure SDK → 阿里云SDK）
   - 测试事件处理流程
# ...
### 第5周: 监控与告警
1. **ARMS配置**
   - 部署ARMS Agent到应用
   - 配置APM监控（响应时间/错误率/依赖）
   - 迁移告警规则
# ...
2. **SLS日志**
   - 配置日志采集
   - 迁移KQL查询到SLS SQL语法
   - 配置仪表盘
# ...
### 第6周: 切换与验证
1. DNS切换（灰度）
2. 流量监控
3. 回滚预案验证
4. Azure资源下线
```

```python
# output/aliyun-migration/oss_migration.py
# OSS对象批量迁移脚本
import oss2
# ...
# 阿里云OSS配置
auth = oss2.Auth(
    os.getenv("ALIYUN_ACCESS_KEY_ID"),
    os.getenv("ALIYUN_ACCESS_KEY_SECRET")
)
bucket = oss2.Bucket(auth, "oss-cn-beijing.aliyuncs.com", "shopapp-prod")
# ...
def migrate_blob(blob_name: str, content: bytes, tier: str):
    """迁移单个blob到OSS"""
    # 存储类型映射
    tier_map = {
        "Hot": oss2.BUCKET_STORAGE_CLASS_STANDARD,
        "Cool": oss2.BUCKET_STORAGE_CLASS_IA,
        "Archive": oss2.BUCKET_STORAGE_CLASS_ARCHIVE,
    }
# ...
    headers = {
        oss2.OBJECT_STORAGE_CLASS: tier_map.get(tier, oss2.BUCKET_STORAGE_CLASS_STANDARD)
    }
# ...
    bucket.put_object(blob_name, content, headers=headers)
```

**效果验证**: ✓8个Azure服务完整映射阿里云 ✓6周迁移路径详细 ✓DTS/OSS工具迁移方案 ✓监控告警迁移 ✓灰度切换+回滚预案

## 常见问题

### Q1: 国内环境是否必须使用 Azure？
A: 非必需。本 Skill 提供的方法论（IaC、成本优化、无服务器、监控）同样适用于阿里云/腾讯云。依赖说明中的"国内替代方案"表提供了完整的服务映射。若业务无海外需求，建议直接使用国内云以降低延迟和合规风险。

### Q2: Bicep 与 Terraform 如何选择？
A: Bicep 适合纯 Azure 环境（原生支持、语法简洁、与 Azure 深度集成）；Terraform 适合多云或跨云场景（生态成熟、Provider 丰富、状态管理灵活）。单 Azure 项目优先 Bicep。

### Q3: 如何避免密钥泄露在 IaC 模板中？
A: 所有密钥通过 Key Vault 引用（`reference` 语法），不直接写在参数文件中。部署时使用服务主体 + 托管身份，避免本地存储凭据。CI/CD 流水线中密钥通过变量组注入。

### Q4: Azure Functions 冷启动如何优化？
A: 消费计划冷启动通常 1-3 秒。优化方案：升级 Premium 计划（预热实例）、配置 `alwaysReady`（保持实例常驻）、减少依赖包体积、使用 Durable Functions 预热模式。

## 已知限制

- 本 Skill 提供架构设计与 IaC 模板，实际部署需要 Azure 订阅和网络连接
- 国内访问 Azure 可能存在网络延迟，建议使用 Azure 中国区（世纪互联运营）或迁移至国内云
- 性能取决于底层 LLM 能力，复杂架构决策可能需要人工审查
- 不替代专业的云架构师认证（如 AZ-305），复杂场景建议咨询专业架构师
- 部分高级服务（如 Azure Synapse Analytics、Azure Machine Learning）的深度配置需参考各自文档

## 安全

- **API Key 零暴露**：所有凭据（Subscription ID、Service Principal）通过环境变量注入，Skill 内零硬编码
- **密钥管理**：使用 Azure Key Vault 集中管理密钥，IaC 模板通过 `reference` 引用，不直接存储
- **最小权限**：服务主体遵循最小权限原则，按角色分配 RBAC（Reader/Contributor/Owner）
- **网络隔离**：生产环境使用 Private Endpoints + VNet 集成，避免公网暴露
- **加密**：存储加密（静态）+ TLS 1.2+（传输）+ 客户自管理密钥（CMK）
- **合规审计**：Azure Policy 强制合规检查 + Defender for Cloud 安全评分监控
