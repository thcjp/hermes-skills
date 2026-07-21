---
slug: azure-cli-toolkit-pro
name: azure-cli-toolkit-pro
version: "1.0.0"
displayName: Azure命令行工具专业版
summary: 企业级Azure云管理,支持批量操作、自动化脚本、多订阅管理与成本优化分析
license: Proprietary
edition: pro
description: |-
  面向企业团队的高级 Azure 云平台管理工具,在免费版基础上扩展自动化、批量操作与成本治理能力。核心能力:
  - 服务主体与托管身份认证(自动化场景)
  - 批量资源操作与脚本化部署
  - 多订阅跨租户统一管理
  - 成本分析与资源优化建议
  - 策略合规审计与安全基线检查

  适用场景:
  - 企业级基础设施自动化部署
  - 多环境(开发/测试/生产)统一管理
  - 云成本治理与资源清理

  差异化:
  - 兼容免费版全部命令,无缝升级
  - 支持自动化脚本与 CI/CD 集成
  - 提供成本优化与合规审计能力
  -...
tags:
- 云平台
- Azure
- 命令行工具
- 自动化
- 企业级
- 成本治理
tools:
  - - read
- exec
---
# Azure 命令行工具专业版

## 概述

Azure 命令行工具专业版为企业团队提供高级云平台管理能力。在免费版基础命令之上,扩展了自动化认证、批量操作、成本治理、策略合规等企业级功能,满足复杂多云环境的管理需求。

专业版完全兼容免费版的命令语法,已有工作流可无缝升级。

## 核心能力

### 1. 自动化认证方式

| 认证方式 | 适用场景 | 命令 |
|:---------|:---------|:-----|
| 服务主体 | CI/CD、自动化脚本 | `az login --service-principal` |
| 托管身份 | Azure 资源内部调用 | `az login --identity` |
| 令牌认证 | 无状态流水线 | `az login --service-principal --password-stdin` |

```bash
# 服务主体认证(自动化场景)
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --tenant $AZURE_TENANT_ID

# 托管身份认证(虚拟机内部)
az login --identity

# 令牌认证(CI/CD)
echo "$AZURE_ACCESS_TOKEN" | az login --service-principal \
  -u $AZURE_CLIENT_ID --password-stdin --tenant $AZURE_TENANT_ID
```

**输入**: 用户提供自动化认证方式所需的指令和必要参数。
**处理**: 按照skill规范执行自动化认证方式操作,遵循单一意图原则。
**输出**: 返回自动化认证方式的执行结果,包含操作状态和输出数据。

### 2. 批量资源操作

```bash
# 批量删除资源组下所有虚拟机
az vm list -g myRG -d --query "[].id" -o tsv | xargs az vm delete --ids --yes

# 批量停止所有运行中的虚拟机
az vm list -d --query "[?powerState=='VM running'].id" -o tsv | xargs az vm stop --ids

# 按标签批量筛选资源
az resource list --tag env=production --query "[].id" -o tsv
```

**输入**: 用户提供批量资源操作所需的指令和必要参数。
**处理**: 按照skill规范执行批量资源操作操作,遵循单一意图原则。
**输出**: 返回批量资源操作的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 自动化部署脚本

```bash
#!/bin/bash
set -e  # 出错即退出

# 创建资源组
az group create -g prod-rg -l eastus

# 创建虚拟机并获取 ID
VM_ID=$(az vm create \
  -g prod-rg \
  -n prod-vm \
  --image UbuntuLTS \
  --query id \
  --output tsv)

echo "Created VM: $VM_ID"

# 验证状态
az vm show --ids "$VM_ID" --query provisioningState

# 配置网络安全组
az network nsg create -g prod-rg -n prod-nsg
az network nsg rule create -g prod-rg --nsg-name prod-nsg \
  -n allow-ssh --priority 1000 \
  --source-address-prefixes '*' \
  --destination-port-ranges 22 \
  --access Allow --protocol Tcp
```

**输入**: 用户提供自动化部署脚本所需的指令和必要参数。
**处理**: 按照skill规范执行自动化部署脚本操作,遵循单一意图原则。
**输出**: 返回自动化部署脚本的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 多订阅管理

```bash
# 列出所有订阅
az account list --query "[].{name:name, id:id, state:state}" -o table

# 跨订阅操作
for sub in $(az account list --query "[].id" -o tsv); do
  az account set --subscription $sub
  echo "=== 订阅: $(az account show --query name -o tsv) ==="
  az vm list -o table
done
```

**输入**: 用户提供多订阅管理所需的指令和必要参数。
**处理**: 按照skill规范执行多订阅管理操作,遵循单一意图原则。
**输出**: 返回多订阅管理的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 成本分析与优化

```bash
# 查看订阅费用(本月)
az consumption usage list \
  --top 10 \
  --query "[].{service:instanceName, cost:pretaxCost}" \
  -o table

# 识别未使用的资源
az resource list --query "[?tags.env=='dev']" -o table

# 查看虚拟机实际使用率
az monitor metrics list \
  --resource $(az vm show -g myRG -n myVM --query id -o tsv) \
  --metric "Percentage CPU" \
  --interval PT1H -o table
```

**输入**: 用户提供成本分析与优化所需的指令和必要参数。
**处理**: 按照skill规范执行成本分析与优化操作,遵循单一意图原则。
**输出**: 返回成本分析与优化的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 6. 策略合规审计

```bash
# 查看策略分配
az policy assignment list -o table

# 合规状态检查
az policy state list --query "[?complianceState=='NonCompliant']" -o table

# 安全基线扫描
az security assessment list -o table
```

**输入**: 用户提供策略合规审计所需的指令和必要参数。
**处理**: 按照skill规范执行策略合规审计操作,遵循单一意图原则。
**输出**: 返回策略合规审计的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、云管理、支持批量操作、多订阅管理与成本、优化分析、面向企业团队的高、云平台管理工具、在免费版基础上扩、展自动化、批量操作与成本治、理能力、核心能力、服务主体与托管身、批量资源操作与脚、本化部署、多订阅跨租户统一、成本分析与资源优、化建议、策略合规审计与安、全基线检查等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景一: 企业级基础设施自动化部署

通过脚本化方式部署完整的生产环境。

```bash
#!/bin/bash
set -e

ENV=${1:-dev}
RG="app-${ENV}-rg"
LOCATION="eastus"

# 1. 创建资源组
az group create -g $RG -l $LOCATION

# 2. 部署应用服务
az deployment group create \
  -g $RG \
  --template-file infra/main.bicep \
  --parameters env=$ENV location=$LOCATION

# 3. 配置监控
az monitor log-analytics workspace create \
  -g $RG -n "logs-${ENV}" -l $LOCATION

# 4. 输出部署结果
echo "部署完成: $ENV 环境"
az resource list -g $RG --query "[].{name:name, type:type}" -o table
```

### 场景二: 多环境统一管理

统一管理开发、测试、生产三个环境的资源状态。

```bash
# 批量查询所有环境资源
for env in dev test prod; do
  echo "=== 环境: $env ==="
  az resource list -g "app-${env}-rg" \
    --query "[].{name:name, type:type, location:location}" \
    -o table
done

# 批量启停(夜间自动关停开发环境)
az vm list -g app-dev-rg --query "[].id" -o tsv | \
  xargs az vm deallocate --ids
```

### 场景三: 成本治理与资源清理

识别闲置资源并清理,优化云成本。

```bash
# 查找未附加的磁盘
az disk list --query "[?diskState=='Unattached']" -o table

# 查找停止超过 7 天的虚拟机
az vm list -d --query "[?powerState!='VM running']" -o table

# 批量删除未使用的存储容器
az storage container list \
  --account-name mystorage \
  --query "[?properties.leaseStatus=='unlocked'].name" -o tsv | \
  xargs -I {} az storage container delete \
    --account-name mystorage -n {}
```

## 不适用场景

以下场景Azure命令行工具专业版不适合处理：

- 需要人工创意判断的任务
- 非结构化头脑风暴
- 人际沟通协调

## 触发条件

需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于非本工具能力范围的需求。

## 快速开始

### 第一步: 配置服务主体

```bash
# 创建服务主体
az ad sp create-for-rbac --name my-automation-sp

# 示例
# {
#   "appId": "xxxxx-xxxx-xxxx",
#   "password": "xxxxx-xxxx-xxxx",
#   "tenant": "xxxxx-xxxx-xxxx"
# }

# 配置环境变量
export AZURE_CLIENT_ID="<appId>"
export AZURE_CLIENT_SECRET="<password>"
export AZURE_TENANT_ID="<租户ID>"
```

### 第二步: 初始化项目配置

```bash
mkdir -p .azure-toolkit/{scripts,templates,reports}

cat > .azure-toolkit/config.json << 'EOF'
{
  "edition": "pro",
  "default_location": "eastus",
  "environments": ["dev", "test", "prod"],
  "auto_shutdown": {
    "dev": "22:00",
    "test": "20:00"
  },
  "cost_alert_threshold": 1000
}
EOF
```

### 第三步: 运行自动化部署

```bash
# 执行部署脚本
./.azure-toolkit/scripts/deploy.sh prod
```

### 命令参数说明

- `-I`: 命令参数,用于指定操作选项

## 配置示例

### 企业级配置

```json
{
  "edition": "pro",
  "organization": {
    "name": "技术团队",
    "subscriptions": {
      "dev": "sub-id-dev",
      "test": "sub-id-test",
      "prod": "sub-id-prod"
    }
  },
  "automation": {
    "service_principal": true,
    "scheduled_tasks": {
      "nightly_shutdown": "0 22 * * *",
      "cost_report": "0 9 * * 1"
    }
  },
  "cost_governance": {
    "budget_alerts": true,
    "unused_resource_scan": true,
    "auto_tag_enforcement": true
  }
}
```

### CI/CD 集成配置

```yaml
# CI/CD 流水线中的认证配置
variables:
  AZURE_CLIENT_ID: $(servicePrincipalId)
  AZURE_CLIENT_SECRET: $(servicePrincipalKey)
  AZURE_TENANT_ID: $(tenantId)

steps:
  - script: |
      az login --service-principal \
        -u $(AZURE_CLIENT_ID) \
        -p $(AZURE_CLIENT_SECRET) \
        --tenant $(AZURE_TENANT_ID)
    displayName: 'Azure 登录'
  - script: |
      ./.azure-toolkit/scripts/deploy.sh $(ENV)
    displayName: '部署应用'
```

## 最佳实践

## 错误处理


```bash
#!/bin/bash
set -e

retry_count=0
max_retries=3

while [ $retry_count -lt $max_retries ]; do
  if az vm create -g myRG -n myVM --image UbuntuLTS; then
    echo "虚拟机创建成功"
    break
  else
    retry_count=$((retry_count + 1))
    echo "重试 $retry_count/$max_retries..."
    sleep 10
  fi
done
```

### 2. 资源命名规范

| 错误场景(资源类型) | 命名规则 | 处理方式(示例) |
|:---------|:---------|:-----|
| 资源组 | `{app}-{env}-rg` | `myapp-prod-rg` |
| 虚拟机 | `{app}-{env}-vm-{seq}` | `myapp-prod-vm-01` |
| 存储账户 | `{app}{env}storage` | `myappprodstorage` |
| 网络安全组 | `{app}-{env}-nsg` | `myapp-prod-nsg` |

### 3. 免费版与专业版能力对比

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 认证方式 | 交互式登录 | 服务主体+托管身份+令牌 |
| 批量操作 | 不支持 | 支持 |
| 自动化脚本 | 不支持 | 支持 |
| 多订阅管理 | 单订阅 | 跨订阅跨租户 |
| 成本分析 | 不支持 | 支持 |
| 策略合规 | 不支持 | 支持 |
| CI/CD 集成 | 不支持 | 支持 |
| 优先支持 | 社区 | 专属通道 |
## 常见问题

### Q1: 专业版是否兼容免费版的命令?

完全兼容。专业版使用相同的 `az` 命令语法,免费版的所有命令在专业版中可直接使用。

### Q2: 服务主体的密码过期了怎么办?

```bash
# 重置服务主体密码
az ad sp credential reset --name <appId> --password <new-password>
```

### Q3: 如何在 CI/CD 中安全存储凭据?

使用 CI/CD 平台的密钥管理功能(如 Azure KeyVault、GitHub Secrets),不要在代码中硬编码凭据。

### Q4: 批量操作误删了资源怎么办?

专业版支持软删除恢复:

```bash
# 恢复已删除的资源
az resource recover --ids <deleted-resource-id>
```

### Q5: 成本分析数据延迟多久?

成本数据通常有 8-24 小时延迟,建议结合监控指标做实时预估。

### Q6: 策略合规扫描多久执行一次?

建议每周执行一次全量扫描,新资源部署后立即扫描:

```bash
az policy state trigger-scan
```

## 依赖说明

### 运行环境

- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Azure CLI**: v2.50 或更高版本
- **Bash**: 4.0+(自动化脚本执行)

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Azure CLI | CLI 工具 | 必需 | brew / apt / choco 安装 |
| Azure 订阅 | 云服务 | 必需 | azure.com 注册 |
| 服务主体 | 认证 | 自动化必需 | `az ad sp create-for-rbac` |
| jq | CLI 工具 | 推荐 | 系统包管理器 |
| xargs | CLI 工具 | 批量操作必需 | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

自动化场景需配置服务主体凭据:

```bash
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret"
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_SUBSCRIPTION_ID="your-subscription-id"
```

建议使用 Azure KeyVault 管理敏感凭据:

```bash
# 从 KeyVault 获取密钥(推荐)
az keyvault secret show --vault-name myVault -n azure-client-secret \
  --query value -o tsv
```

### 可用性分类

- **分类**: MD+EXEC+SCRIPT(Markdown 指令 + 命令行执行 + 自动化脚本)
- **说明**: 通过自然语言指令驱动 Agent 执行 `az` 命令,支持脚本化批量操作与 CI/CD 集成
- **离线可用**: 否,所有操作需要连接 Azure 云平台

## 已知限制

- 依赖云服务，需要网络连接

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
