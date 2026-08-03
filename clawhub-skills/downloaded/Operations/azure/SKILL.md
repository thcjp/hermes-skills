---
slug: azure
name: azure
version: "1.0.0"
displayName: Azure
summary: "Azure服务部署监控管理,提供经过验证的最佳实践,解决云资源管理复杂度问题"
license: MIT
description: |-
  Deploy, monitor, and manage Azure services with battle-tested patterns。核心能力:

  - 运维工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 系统运维、监控告警、资源管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Operations
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

# Azure

## Cost Traps

* Stopped VMs still pay for attached disks and public IPs — deallocate fully with `az vm deallocate` not just stop from portal
* Premium SSD default on VM creation — switch to Standard SSD for dev/test, saves 50%+
* Log Analytics workspace retention defaults to 30 days free, then charges per GB — set data retention policy and daily cap before production
* Bandwidth between regions is charged both ways — keep paired resources in same region, use Private Link for cross-region when needed
* Cosmos DB charges for provisioned RU/s even when idle — use serverless for bursty workloads or autoscale with minimum RU setting

## Security Rules

* Resource Groups don't provide network isolation — NSGs and Private Endpoints do. RG is for management, not security boundary
* Managed Identity eliminates secrets for Azure-to-Azure auth — use System Assigned for single-resource, User Assigned for shared identity
* Key Vault soft-delete enabled by default (90 days) — can't reuse vault name until purged, plan naming accordingly
* Azure AD conditional access policies don't apply to service principals — use App Registrations with certificate auth, not client secrets
* Private Endpoints don't automatically update DNS — configure Private DNS Zone and link to VNet or resolution fails

## Networking

* NSG rules evaluate by priority (lowest number first) — default rules at 65000+ always lose to custom rules
* Application Gateway v2 requires dedicated subnet — at least /24 recommended for autoscaling
* Azure Firewall premium SKU required for TLS inspection and IDPS — standard can't inspect encrypted traffic
* VNet peering is non-transitive — hub-and-spoke requires routes in each spoke, or use Azure Virtual WAN
* Service Endpoints expose entire service to VNet — Private Endpoints give private IP for specific resource instance

## Performance

* Azure Functions consumption plan has cold start — Premium plan with minimum instances for latency-sensitive
* Cosmos DB partition key choice is permanent and determines scale — can't change without recreating container
* App Service plan density: P1v3 handles ~10 slots, more causes resource contention — monitor CPU/memory per slot
* Azure Cache for Redis Standard tier has no SLA for replication — use Premium for persistence and clustering
* Blob storage hot tier for frequent access — cool has 30-day minimum, archive has 180-day and hours-long rehydration

## Monitoring

* Application Insights sampling kicks in at high volume — telemetry may miss intermittent errors, adjust `MaxTelemetryItemsPerSecond`
* Azure Monitor alert rules charge per metric tracked — consolidate metrics in Log Analytics for complex alerts
* Activity Log only shows control plane operations — diagnostic settings required for data plane (blob access, SQL queries)
* Alert action groups have rate limits — 1 SMS per 5 min, 1 voice call per 5 min, 100 emails per hour per group
* Log Analytics query timeout is 10 minutes — optimize queries with time filters first, then other predicates

## Infrastructure as Code

* ARM templates fail silently on some property changes — use `what-if` deployment mode to preview changes
* Terraform azurerm provider state contains secrets in plaintext — use remote backend with encryption (Azure Storage + customer key)
* Bicep is ARM's replacement — transpiles to ARM, better tooling, use for new projects
* Resource locks prevent accidental deletion but block some operations — CanNotDelete lock still allows modifications
* Azure Policy evaluates on resource creation and updates — existing non-compliant resources need remediation task

## Identity and Access

* RBAC role assignments take up to 30 minutes to propagate — pipeline may fail immediately after assignment
* Owner role can't manage role assignments if PIM requires approval — use separate User Access Administrator
* Service principal secret expiration defaults to 1 year — set calendar reminder or use certificate with longer validity
* Azure AD B2C is separate from Azure AD — different tenant, different APIs, different pricing

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

- Deploy, monitor, and manage Azure services with battle-tested patterns
- 触发关键词: azure, monitor, manage, deploy, services

## 详细功能列表

### 详细功能列表

- **自动化部署**: 支持自动化部署Azure服务，包括虚拟机、容器、数据库等。
- **监控告警**: 提供实时监控和告警功能，支持自定义告警规则和通知方式。
- **资源管理**: 支持资源分组、标签、策略等资源管理功能，简化资源管理流程。
- **安全审计**: 提供安全审计日志，帮助用户跟踪和审计资源访问和操作。
- **成本优化**: 提供成本分析工具，帮助用户优化资源使用和降低成本。

**边界条件处理**:
- 资源部署失败时，提供重试机制和错误日志。
- 监控数据异常时，提供数据回溯和异常分析。
- 资源管理操作失败时，提供回滚机制。

## 输入输出参数说明

### 输入输出参数说明

| 参数名 | 类型 | 默认值 | 取值范围 | 说明 |
|-------|-----|---------|---------|------|
| azure_resource_type | String | - | - | 资源类型，如虚拟机、容器等 |
| azure_resource_name | String | - | - | 资源名称 |
| alert_rule | Object | - | - | 告警规则配置 |
| resource_group | String | - | - | 资源组名称 |
| tag | Object | - | - | 资源标签配置 |

**参数类型说明**:
- String: 字符串类型
- Object: 对象类型，包含多个键值对

**取值范围**:
- 资源类型和资源名称的取值范围由Azure平台定义。

## 错误码定义和处理方案

### 错误码定义和处理方案

| 错误码 | 描述 | 处理方案 |
|-------|------|---------|
| ERROR_DEPLOYMENT_FAILED | 资源部署失败 | 检查资源配置和依赖，重试部署 |
| ERROR_MONITORING_FAILED | 监控数据异常 | 检查监控配置和数据源，回溯数据 |
| ERROR_RESOURCE_MANAGEMENT_FAILED | 资源管理操作失败 | 检查资源配置和权限，回滚操作 |

**错误码说明**:
- ERROR_DEPLOYMENT_FAILED: 资源部署失败，可能由于资源配置错误或依赖问题导致。
- ERROR_MONITORING_FAILED: 监控数据异常，可能由于监控配置错误或数据源问题导致。
- ERROR_RESOURCE_MANAGEMENT_FAILED: 资源管理操作失败，可能由于资源配置错误或权限问题导致。

## 技术示例

### 技术示例

```yaml
# ARM模板示例
resources:
- type: Microsoft.Compute/virtualMachines
  apiVersion: 2021-04-01
  name: myVM
  location: eastus
  properties:
    osProfile:
      adminUsername: azureuser
      adminPassword: azurepassword
    storageProfile:
      imageReference:
        publisher: MicrosoftWindowsServer
        offer: WindowsServerSemiAnnual
        sku: 2019-Datacenter
        version: 'latest'
    networkProfile:
      networkInterfaces:
      - id: /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Network/networkInterfaces/{nic-name}
```

## 常见问题

### 常见问题

#### Q1: 如何设置告警规则？
A: 登录Azure门户，进入监控服务，创建新的告警规则，配置触发条件、通知条件和操作组。

#### Q2: 如何查看监控数据？
A: 登录Azure门户，进入监控服务，选择相应的资源，查看监控数据图表和日志。

#### Q3: 如何优化资源使用降低成本？
A: 使用Azure成本管理服务，分析资源使用情况，优化资源配置和策略。

#### Q4: 如何处理资源部署失败？
A: 检查资源配置和依赖，重试部署或联系技术支持。

#### Q5: 如何查看资源使用情况？
A: 登录Azure门户，进入资源组或资源，查看资源使用情况。

## 安全架构说明

### 安全架构说明

Azure服务部署监控管理采用多层次的安全架构，包括以下方面：
- **身份验证**: 使用Azure Active Directory进行身份验证，确保只有授权用户才能访问服务。
- **授权**: 使用基于角色的访问控制（RBAC）进行授权，确保用户只能访问其有权访问的资源。
- **数据加密**: 使用TLS加密数据传输，使用Azure Key Vault存储敏感数据。
- **安全审计**: 记录所有操作日志，以便进行安全审计。

## 技术亮点与差异化优势

### 技术亮点与差异化优势

Azure服务部署监控管理具有以下技术亮点和差异化优势：
- **自动化部署**: 支持自动化部署Azure服务，提高部署效率。
- **智能监控**: 提供智能监控和告警功能，帮助用户及时发现和解决问题。
- **成本优化**: 提供成本分析工具，帮助用户优化资源使用和降低成本。
- **安全可靠**: 采用多层次的安全架构，确保服务安全可靠。

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Azure？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Azure有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 依赖云服务，需要网络连接
