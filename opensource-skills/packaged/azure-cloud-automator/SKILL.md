---
slug: azure-cloud-automator
name: azure-cloud-automator
version: "1.0.0"
displayName: "Azure云自动化"
summary: "Azure云自动化:基础设施即代码+成本优化+无服务器架构,云上运维一站搞定"
license: MIT
description: |-
  Azure云自动化——基于Azure云最佳实践,从基础设施即代码到成本优化,从无服务器架构到安全合规,云上运维一站搞定。让Azure云资源管理像写代码一样可控可审计。

  核心能力:
  - 基础设施即代码:CDK/ARM/Bicep模板自动化部署
  - 成本优化:浪费识别+资源右配+预留实例建议
  - 无服务器架构:Functions/Logic Apps事件驱动
  - 资源管理与监控:资源编排/监控告警/自动恢复
  - 安全合规:合规框架对齐+安全基线检查
  - 运维自动化:日常运维任务自动化

  适用场景:
  - 独立创业者Azure部署:IaC自动化部署云资源
  - SaaS创业者成本优化:云费用过高,识别浪费+优化建议
  - 一人公司无服务器架构:Functions+事件驱动,按需付费
  - 企业运维自动化:监控/告警/自动恢复日常运维

  差异化:不是Azure文档翻译,而是基于最佳实践的云自动化专家,IaC+成本优化+无服务器+安全合规全链路,让小团队也能高效管理Azure云资源。

  触发关键词:Azure、云自动化、Azure CDK、Bicep、ARM模板、无服务器、事件驱动、云成本、Azure运维、云架构
tags: [Azure, 云自动化, 基础设施即代码, 成本优化, 无服务器]
tools: [read, exec]
---

# Azure云自动化

Azure 云最佳实践与自动化。从基础设施即代码到成本优化,从无服务器架构到安全合规。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 基础设施部署 | 部署 Azure 资源 | IaC 自动化部署 |
| 成本优化 | 云费用过高 | 识别浪费+优化建议 |
| 架构设计 | 设计云架构 | 无服务器/事件驱动方案 |
| 运维自动化 | 日常运维 | 监控/告警/自动恢复 |
| 合规审计 | 安全合规检查 | 合规框架对齐 |

## 工作流

### 1. 基础设施即代码

1. **IaC 工具选择**:
   - Bicep(推荐,Azure 原生)
   - ARM 模板(JSON,传统)
   - Terraform(多云)
   - Azure CDK(编程式)
2. **资源定义**:
   - 资源组(Resource Group)
   - 计算(App Service/Functions/AKS/VM)
   - 存储(Storage Account/Cosmos DB)
   - 网络(VNet/Subnet/NSG)
   - 监控(Application Insights/Log Analytics)
3. **环境分层**:Dev/Staging/Prod 参数化
4. **部署流水线**:CI/CD 集成

### 2. 无服务器与事件驱动

1. **Azure Functions**:
   - 触发器:HTTP/Timer/Service Bus/Event Grid/Cosmos DB
   - 绑定:输入/输出绑定简化代码
   - 消费计划:按需付费 vs 高级计划
2. **事件网格(Event Grid)**:
   - 事件发布/订阅模式
   - 系统主题(资源事件)+ 自定义主题
   - 事件处理 Functions/Logic Apps/Webhooks
3. **Logic Apps**:
   - 可视化工作流
   - 200+ 连接器
   - 业务流程自动化
4. **架构模式**:
   - 事件溯源(Event Sourcing)
   - CQRS(命令查询职责分离)
   - Saga 模式(分布式事务)

### 3. 成本优化

1. **成本分析**:
   - 按资源/标签/部门拆分
   - 识别高成本资源
   - 趋势分析与预测
2. **优化策略**:
   - 计算:预留实例/Spot VM/自动缩放
   - 存储:生命周期管理(冷/热/归档)
   - 网络:出站流量优化/VNet 对等
   - 函数:消费计划优化/避免冷启动
3. **预算与告警**:设定预算阈值,超限告警
4. **标签策略**:成本归属标签规范

### 4. 资源管理与监控

1. **Azure Monitor**:
   - 指标(Metrics):性能数据
   - 日志(Logs):诊断日志
   - 告警(Alerts):阈值/异常检测
2. **Application Insights**:
   - 应用性能监控(APM)
   - 分布式追踪
   - 依赖映射
   - 可用性测试
3. **Log Analytics**:
   - KQL 查询语言
   - 日志聚合与分析
   - 自定义仪表盘
4. **自动化运维**:
   - Azure Automation(Runbook)
   - 自动缩放规则
   - 自动备份与恢复

### 5. 安全与合规

1. **身份与访问**:
   - Azure AD 集成
   - RBAC 角色分配
   - 托管身份(Managed Identity)
   - 条件访问策略
2. **网络安全**:
   - VNet/子网/NSG
   - Azure Firewall
   - DDoS 防护
   - Private Endpoints
3. **数据安全**:
   - 存储加密(静态)
   - TLS 1.2+(传输)
   - Key Vault 密钥管理
   - 客户自管理密钥(CMK)
4. **合规框架**:
   - ISO 27001/SOC 2/HIPAA/GDPR
   - Azure Policy 合规检查
   - Defender for Cloud 安全评分

## 最佳实践

1. **IaC 优先**:所有资源通过代码部署,避免手动操作
2. **不可变基础设施**:重建而非修改
3. **环境隔离**:Dev/Staging/Prod 独立资源组
4. **最小权限**:RBAC 最小权限原则
5. **标签规范**:统一标签策略(项目/环境/负责人/成本中心)
6. **成本治理**:定期审查+预算告警

## 输出规范

- IaC 模板:`output/{project}/infra/`(Bicep/Terraform)
- 架构图:`output/{project}/architecture.md`
- 成本报告:`output/{project}/cost-report.md`
- 部署指南:`output/{project}/deployment.md`
- 监控配置:`output/{project}/monitoring/`

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Azure CLI | 工具 | 可选 | az命令行(用于部署和资源管理) |
| Bicep/Terraform | 工具 | 可选 | IaC模板工具 |
| Azure订阅 | 服务 | 可选 | Azure云服务账号 |

### API Key 配置
- **AZURE_SUBSCRIPTION_ID**: 可选 - Azure云部署
- **AZURE_CREDENTIALS**: 可选 - Azure认证凭据
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
本Skill为Azure云最佳实践指导。实际部署需要Azure订阅和CLI工具,纯设计阶段无需额外依赖。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用
