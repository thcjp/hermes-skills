---
slug: azure-cloud-architect
name: azure-cloud-architect
version: "1.0.0"
displayName: Azure云架构师
summary: 多订阅导航,角色审计最小权限,成本分析,合规检查,跨订阅批量操作。
license: MIT
description: |-
  Azure云架构师是一个基于Azure CLI的智能云基础设施管理助手。针对传统Azure管理"多订阅/租户管理复杂、RBAC角色混乱、成本治理缺失、安全合规难落地、NSG/Key Vault访问审计困难、跨订阅操作繁琐"六大痛点,构建了多订阅导航器、角色审计与最小权限、成本分析工作流、合规检查清单和跨订阅批量操作五大核心能力。

  核心能力包括:默认只读查询保障安全;写操作与破坏性操作需确认;支持--dry-run预演;az account show身份确认先行;资源清单/健康监控/安全审计/成本管理全场景覆盖;订阅与租户智能检测。

  适用场景:Azure资源盘点与查询、Azure Monitor健康监控与错误排查、RBAC角色与NSG安全审计、Cost Management成本分析、基础设施变更规划、多订阅多租户管理、安全合规检查。

  差异化亮点:相比原始版本,新增多订阅导航器(自动列出并选择订阅)、角色审计与最小权限原则(过度授权检测)、成本分析工作流(按资源组/服务维度)、合规检查清单(RBAC/存储/NSG/Key Vault)、跨订阅批量操作模板、设备码登录流程、FAQ与故障排查决策树。

  触发关键词:Azure云架构师、基础设施管理、多订阅、RBAC审计、成本分析、Azure CLI、azure-cloud-architect
tags:
- 智能代理
- 云计算
- Azure
- 基础设施
- 安全合规
tools:
- read
- exec
---

# Azure云架构师

使用本地Azure CLI回答关于Azure资源的问题。默认只读查询,仅在用户明确要求变更并确认后执行写/破坏性操作。

## 快速开始

1. **确认登录**(每次会话第一步):
   ```bash
   az account show
   ```
   如未登录: `az login --use-device-code`

2. **选择订阅**(多订阅时,参见多订阅导航器)

3. **使用只读命令**回答问题

4. **如需变更**,列出精确命令并等待确认后执行

## 安全规则(最高优先级)

* 所有操作默认**只读**,除非用户明确要求变更**且**确认
* 破坏性操作(删除/终止/销毁/修改/扩缩容/计费/凭据)需要确认步骤
* 优先使用 `--dry-run` 或 `what-if` 预演并展示计划
* **绝不要**透露或记录密钥(密钥、客户端密钥、令牌)
* **绝不要**将密钥输出到聊天或日志

## 多订阅导航器(差异化)

### 订阅检测与选择

```bash
# 1. 列出所有可访问的订阅
az account list --output table

# 2. 如有多个订阅,询问用户选择
# 输出示例:
# Name               CloudName    SubscriptionId    State
# Production         AzureCloud   xxx-xxx-xxx       Enabled
# Development        AzureCloud   yyy-yyy-yyy       Enabled

# 3. 设置活跃订阅
az account set --subscription "Production"
# 或用ID
az account set --subscription xxx-xxx-xxx
```

### 订阅与租户处理规则

```
用户明确指定订阅/租户 → 使用用户指定
     │未指定
az account show 有默认订阅 → 使用默认订阅
     │无默认
az account list 多个订阅 → 询问用户选择
     │仅一个
直接使用
```

结果为订阅范围时,明确说明使用的订阅。

## 分层权限模型(差异化)

| 层级 | 操作类型 | 策略 | 示例命令 |
|------|----------|------|----------|
| L0 只读 | list/show/get | 直接执行 | `az vm list` |
| L1 预演 | 写操作(有what-if) | 展示计划,确认后执行 | `az deployment group create --what-if` |
| L2 确认写 | 写操作(无预演) | 列出影响范围,等待确认 | `az storage blob upload` |
| L3 破坏性 | delete | 详细影响分析+确认 | `az vm delete` |
| L4 敏感 | 凭据/密钥/计费 | 双重确认+影响警告 | `az ad app credential reset` |

## 任务指南

### 资源盘点/列表
使用 `list`/`show` 命令:
```bash
# 列出所有VM
az vm list --query '[].{Name:name,ResourceGroup:resourceGroup,State:powerState}' -d --output table

# 列出存储账户
az storage account list --query '[].{Name:name,ResourceGroup:resourceGroup,SKU:sku.name}' --output table

# 列出资源组
az group list --query '[].{Name:name,Location:location}' --output table
```

### 健康/错误检查
使用Azure Monitor指标/日志查询:
```bash
# VM CPU使用率
az monitor metrics list --resource <resource-id> \
  --metric "Percentage CPU" \
  --start-time 2025-01-01T00:00:00Z --end-time 2025-01-02T00:00:00Z

# 查询Activity Log
az monitor activity-log list --resource-group myRG --max-events 20
```

## 安全审计剧本(差异化)

### RBAC角色审计
```bash
# 列出订阅级角色分配
az role assignment list --output table

# 检查特定用户的角色
az role assignment list --assignee user@domain.com --output table

# 列出自定义角色
az role definition list --custom-role-only true --output table

# 检查Owner角色分配(过度权限检测)
az role assignment list --role "Owner" --query '[].{Assignee:principalName,Scope:scope}' --output table
```

### 存储安全检查
```bash
# 检查存储账户公共访问
az storage account show --name mystorage --query 'allowBlobPublicAccess'

# 检查存储账户HTTPS要求
az storage account show --name mystorage --query 'enableHttpsTrafficOnly'

# 检查最小TLS版本
az storage account show --name myststorage --query 'minimumTlsVersion'
```

### NSG网络安全组检查
```bash
# 列出NSG规则
az network nsg rule list --nsg-name myNSG --resource-group myRG --output table

# 检查开放到0.0.0.0/0的入站规则
az network nsg rule list --nsg-name myNSG --resource-group myRG \
  --query "[?sourceAddressPrefix=='*' || sourceAddressPrefix=='0.0.0.0/0'].{Name:name,Port:destinationPortRange,Access:access}"
```

### Key Vault访问审计
```bash
# 列出Key Vault访问策略
az keyvault show --name myVault --query 'properties.accessPolicies'

# 检查Key Vault防火墙
az keyvault show --name myVault --query 'properties.networkAcls'
```

## 成本分析工作流(差异化)

### 成本分析(只读)
```bash
# 按资源组查询成本
az costmanagement query --type ActualCost \
  --timeframe MonthToDate \
  --dataset-grouping name=ResourceGroupName type=Dimension \
  --dataset-aggregation totalCost=name=Cost function=Sum

# 按服务查询成本
az costmanagement query --type ActualCost \
  --timeframe MonthToDate \
  --dataset-grouping name=ServiceName type=Dimension \
  --dataset-aggregation totalCost=name=Cost function=Sum
```

### 空闲资源识别
```bash
# 停止的VM
az vm list --show-details --query "[?powerState=='VM stopped'].{Name:name,ResourceGroup:resourceGroup}" --output table

# 未挂载的磁盘
az disk list --query "[?diskState=='Unattached'].{Name:name,ResourceGroup:resourceGroup,Size:diskSizeGb}" --output table

# 未使用的公网IP
az network public-ip list --query "[?ipConfiguration==null].{Name:name,ResourceGroup:resourceGroup}" --output table
```

## 跨订阅批量操作(差异化)

```bash
# 跨订阅列出所有VM
for sub in $(az account list --query '[].id' -o tsv); do
  echo "=== 订阅: $(az account show --subscription $sub --query name -o tsv) ==="
  az vm list --subscription $sub --query '[].{Name:name,RG:resourceGroup}' -o table
done

# 跨订阅检查安全组
for sub in $(az account list --query '[].id' -o tsv); do
  az network nsg list --subscription $sub --query '[].{Name:name,RG:resourceGroup}' -o table
done
```

## 合规检查清单(差异化)

| 检查项 | 命令 | 合规标准 |
|--------|------|----------|
| 存储公共访问 | `az storage account show --name X --query 'allowBlobPublicAccess'` | 应为false |
| 存储HTTPS | `az storage account show --name X --query 'enableHttpsTrafficOnly'` | 应为true |
| Key Vault防火墙 | `az keyvault show --name X --query 'properties.networkAcls.defaultAction'` | 应为Deny |
| NSG开放规则 | `az network nsg rule list ...` | 无0.0.0.0/0入站 |
| Owner角色数量 | `az role assignment list --role "Owner"` | 最小化 |
| VM磁盘加密 | `az vm encryption show --name X -g RG` | 应已启用 |

## 常见问题FAQ

**Q: 如何切换订阅?**
A: 使用 `az account set --subscription "订阅名"` 或 `az account set --subscription "订阅ID"`。结果为订阅范围时明确说明使用的订阅。

**Q: 设备码登录怎么用?**
A: 运行 `az login --use-device-code`,终端会显示一个码和URL。在浏览器中打开URL,输入码完成登录。适合无法打开浏览器的SSH环境。

**Q: 命令执行失败提示权限不足?**
A: 检查当前身份 `az account show`,确认关联的RBAC角色是否包含所需权限。只读操作至少需要Reader角色。

**Q: 如何安全地执行破坏性操作?**
A: 1)先用 `--what-if` 或 `--dry-run` 预演;2)列出精确影响范围;3)等待用户显式确认;4)执行后验证结果。绝不在未确认时执行破坏性操作。

**Q: 多租户如何管理?**
A: 使用 `az login --tenant <tenant-id>` 登录特定租户。使用 `az account list --query '[].tenantId'` 查看可访问的租户。

**Q: 成本查询返回空?**
A: 确认Cost Management已在Azure Portal中配置。确认订阅类型支持Cost Management(CSP等某些类型可能不支持)。

## 故障排查

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `Please run az login` | 未登录 | 运行 `az login --use-device-code` |
| `Subscription not found` | 订阅ID错误或无权限 | 用 `az account list` 确认可访问的订阅 |
| `Access denied` | RBAC权限不足 | 检查身份 `az account show`,确认角色 |
| `No subscription selected` | 未设置活跃订阅 | 运行 `az account set --subscription X` |
| 命令未找到 | Azure CLI版本过旧 | 运行 `az version`,升级到最新版 |
| 超时 | 网络或服务问题 | 重试,检查网络连接,确认服务状态 |
| 密钥泄露风险 | 输出含密钥 | 立即停止,绝不在聊天/日志中输出密钥值 |
| 多订阅操作遗漏 | 未遍历所有订阅 | 使用跨订阅批量操作模板遍历 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent
- **操作系统**: Windows / macOS / Linux
- **Azure CLI**: v2.0+

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Azure CLI | 工具 | 必需 | 从docs.microsoft.com/cli/azure安装 |
| Azure账户 | 账户 | 必需 | 注册Azure账户 |
| jq | 工具 | 可选(JSON处理) | 从stedolan.github.io/jq安装 |

### API Key 配置
- 通过 `az login` 认证,无需手动配置API Key
- 服务主体认证需 `az login --service-principal -u <app-id> -p <password> --tenant <tenant>`
- **绝不要**在聊天或日志中输出密钥、客户端密钥、令牌

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,需要命令行执行能力运行Azure CLI)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent使用Azure CLI管理云基础设施。需要Azure CLI和Azure账户。
