---
name: azure-cli-toolkit
slug: azure-cli-toolkit
displayName: "azure-cli"
version: "1.0.0"
summary: "命令行全面管理Azure云平台,一条命令搞定资源运维(社区下载版)"
description: "命令行全面管理Azure云平台,一条命令搞定资源运维(社区下载版)。触发关键词: azure-cli, cli, comprehensive, azure, platform, management, cloud。内置错误恢复与降级机制,多格式兼容,适配多源数据。支持多种输入格式,输出结构化结果,适配独立开发者与小型团队。"
license: "MIT"
tools:
  - read
---

# azure-cli

**Master the Azure command-line interface for cloud infrastructure management, automation, and DevOps workflows.**

Azure CLI is Microsoft's powerful cross-platform command-line tool for managing Azure resources. This skill provides comprehensive knowledge of Azure CLI commands, authentication, resource management, and automation patterns.

## What You'll Learn

### Core Concepts

* Azure subscription and resource group architecture
* Authentication methods and credential management
* Resource Provider organization and registration
* Global parameters, output formatting, and query syntax
* Automation scripting and error handling

### Major Service Areas (66 command modules)

* **Compute:** Virtual Machines, Scale Sets, Kubernetes (AKS), Containers
* **Networking:** Virtual Networks, Load Balancers, CDN, Traffic Manager
* **Storage & Data:** Storage Accounts, Data Lake, Cosmos DB, Databases
* **Application Services:** App Service, Functions, Container Apps
* **Databases:** SQL Server, MySQL, 关系型数据库, CosmosDB
* **Integration & Messaging:** Event Hubs, Service Bus, Logic Apps
* **Monitoring & Management:** Azure Monitor, Policy, RBAC, Cost Management
* **AI & Machine Learning:** Cognitive Services, Machine Learning
* **DevOps:** Azure DevOps, Pipelines, Extensions

## Quick Start

### Installation

**macOS:**

```bash
brew install azure-cli
```

**Linux (Ubuntu/Debian):**

```bash
curl -sL https://aka.ms/InstallAzureCliLinux | bash
```

**Windows:**

```powershell
choco install azure-cli
```

**Verify Installation:**

```bash
az --version          # Show version
az --help             # Show general help
```

### First Steps

```bash
az login

az account list

az account set --subscription "My Subscription"

az group create -g myResourceGroup -l eastus

az group list
```

## Essential Commands

### Authentication & Accounts

```bash
az login                                    # Interactive login
az login --service-principal -u APP_ID -p PASSWORD -t TENANT_ID
az login --identity                         # Managed identity
az logout                                   # Sign out
az account show                             # Current account
az account list                             # All accounts
az account set --subscription SUBSCRIPTION  # Set default
```

### Global Flags (Use with Any Command)

```bash
--subscription ID       # Target subscription
--resource-group -g RG  # Target resource group
--output -o json|table|tsv|yaml  # Output format
--query JMESPATH_QUERY  # Filter/extract output
--verbose -v            # Verbose output
--debug                 # Debug mode
--help -h               # Command help
```

### Resource Groups

```bash
az group list           # List all resource groups
az group create -g RG -l LOCATION  # Create
az group delete -g RG   # Delete
az group show -g RG     # Get details
az group update -g RG --tags key=value  # Update tags
```

### Virtual Machines (Compute)

```bash
az vm create -g RG -n VM_NAME --image UbuntuLTS
az vm list -g RG
az vm show -g RG -n VM_NAME
az vm start -g RG -n VM_NAME
az vm stop -g RG -n VM_NAME
az vm restart -g RG -n VM_NAME
az vm delete -g RG -n VM_NAME
```

### Storage Operations

```bash
az storage account create -g RG -n ACCOUNT --sku Standard_LRS
az storage account list
az storage container create --account-name ACCOUNT -n CONTAINER
az storage blob upload --account-name ACCOUNT -c CONTAINER -n BLOB -f LOCAL_FILE
az storage blob download --account-name ACCOUNT -c CONTAINER -n BLOB -f LOCAL_FILE
```

### Azure Kubernetes Service (AKS)

```bash
az aks create -g RG -n CLUSTER --node-count 2
az aks get-credentials -g RG -n CLUSTER
az aks list
az aks show -g RG -n CLUSTER
az aks delete -g RG -n CLUSTER
```

## Common Patterns

### Pattern 1: Output Formatting

```bash
az vm list --query "[].{name: name, state: powerState}"

az vm list --query "[].name" -o tsv

az vm list --query "[?powerState=='VM running'].name"
```

### Pattern 2: Automation & Scripting

```bash
#!/bin/bash
set -e  # Exit on error

VM_ID=$(az vm create \
  -g myRG \
  -n myVM \
  --image UbuntuLTS \
  --query id \
  --output tsv)

echo "Created VM: $VM_ID"

az vm show --ids "$VM_ID" --query provisioningState
```

### Pattern 3: Batch Operations

```bash
az vm list -g myRG -d --query "[].id" -o tsv | xargs az vm delete --ids

az resource list --tag env=production
```

### Pattern 4: Using Defaults

```bash
az configure --defaults group=myRG subscription=mySubscription location=eastus

az vm create -n myVM --image UbuntuLTS  # group, subscription, location inherited
```

## Helper Scripts

This skill includes helper bash scripts for common operations:

* **azure-vm-status.sh** — Check VM status across subscription
* **azure-resource-cleanup.sh** — Identify and remove unused resources
* **azure-storage-analysis.sh** — Analyze storage account usage and costs
* **azure-subscription-info.sh** — Get subscription quotas and limits
* **azure-rg-deploy.sh** — Deploy infrastructure with monitoring

**Usage:**

```bash
./scripts/azure-vm-status.sh -g myResourceGroup
./scripts/azure-storage-analysis.sh --subscription mySubscription
```

## Advanced Topics

### Output Querying with JMESPath

Azure CLI supports powerful output filtering using JMESPath:

```bash
az vm list --query "sort_by([], &name)"

az vm list --query "[?location=='eastus' && powerState=='VM running'].name"

az vm list --query "length([])"  # Count VMs
```

### Error Handling

```bash
az vm create -g RG -n VM --image UbuntuLTS
if [ $? -eq 0 ]; then
  echo "VM created successfully"
else
  echo "Failed to create VM"
  exit 1
fi
```

### Authentication Methods

**Service Principal (Automation):**

```bash
az login --service-principal \
  --username $AZURE_CLIENT_ID \
  --password $AZURE_CLIENT_SECRET \
  --租户 $AZURE_TENANT_ID
```

**Managed Identity (Azure Resources):**

```bash
az login --identity
```

**Token-based (CI/CD):**

```bash
echo "$AZURE_ACCESS_TOKEN" | az login --service-principal -u $AZURE_CLIENT_ID --password-stdin --租户 $AZURE_TENANT_ID
```

## Key Resources

* **Official Documentation:** <https://learn.microsoft.com/en-us/cli/azure/>
* **Command Reference:** <https://learn.microsoft.com/en-us/cli/azure/reference-index>
* **GitHub Repository:** <(已移除原仓库链接)
* **Comprehensive Guide:** See 
* **Release Notes:** <(已移除原仓库链接)

## Tips & Tricks

1. **Enable Tab Completion:**

   bash

   ```
   # macOS with Homebrew
   eval "$(az completion init zsh)"

   # Linux (bash)
   eval "$(az completion init bash)"
   ```
2. **Find Commands Quickly:**

   bash

   ```
   az find "create virtual machine"  # Search for commands
   ```
3. **Use --no-wait for Long Operations:**

   bash

   ```
   az vm create -g RG -n VM --image UbuntuLTS --no-wait
   # Check status later with az vm show
   ```
4. **Save Frequently Used Parameters:**

   bash

   ```
   az configure --defaults group=myRG location=eastus
   ```
5. **Combine with Other Tools:**

   bash

   ```
   # Use with jq for advanced JSON processing
   az vm list | jq '.[] | select(.powerState == "VM running") | .name'

   # Use with xargs for batch operations
   az storage account list --query "[].name" -o tsv | xargs -I {} az storage account show -g RG -n {}
   ```

## Next Steps

* Review  for comprehensive command documentation
* Explore helper scripts in the `scripts/` directory
* Practice with non-production resources first
* Review Azure best practices and cost optimization strategies

---

**Version:** 1.0.0
**License:** MIT
**Compatible with:** Azure CLI v2.50+, Azure Subscription

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex /  CLI等)
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

- 触发关键词: azure-cli, cli, comprehensive, azure, platform, management, cloud

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
### Installation

**macOS:**

```bash
brew install azure-cli
```

**Linux (Ubuntu/Debian):**

```bash
curl -sL https://aka.ms/InstallAzureCliLinux | bash
```

**Windows:**

```powershell
choco install azure-cli
```

**Verify Installation:**

```bash
az --version          # Show version
az --help             # Show general help
```

### First Steps

```bash
az login

az account list

az account set --subscription "My Subscription"

az group create -g myResourceGroup -l eastus

az group list
```
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用azure-cli？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: azure-cli有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 依赖云服务，需要网络连接
