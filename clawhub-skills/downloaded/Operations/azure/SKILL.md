---
slug: azure
name: azure
version: "1.0.0"
displayName: Azure
summary: Deploy, monitor, and manage Azure services with battle-tested patterns.
license: MIT
description: |-
  Deploy, monitor, and manage Azure services with battle-tested patterns.

  核心能力:

  - 运维工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 系统运维、监控告警、资源管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: azure, monitor, manage, deploy, services
tags:
- Operations
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
