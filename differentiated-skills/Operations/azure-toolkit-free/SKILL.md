---
slug: azure-toolkit-free
name: azure-toolkit-free
version: "1.0.0"
displayName: Azure管理入门工具
summary: 微软Azure基础资源管理工具，支持虚拟机/存储/网络常用资源操作。
license: MIT
edition: free
description: |-
  面向个人开发者与初创团队的Azure基础管理工具。支持虚拟机、存储
  账户、虚拟网络等常用资源的创建与管理。通过命令行简化Azure操作，
  适合个人项目与小型应用的云端部署。

  核心能力:
  - 虚拟机创建与管理
  - 存储账户操作
  - 虚拟网络配置
  - 网络安全组管理
  - 基础身份管理

  适用场景:
  - 个人项目云端部署
  - 初创团队基础设施
  - Azure学习与实验
  - 简单应用部署

  差异化:
  - 免费版聚焦基础资源管理
  - 适合个人与小型项目
  - 不支持多区域批量部署
  - 不支持企业级合规治理

  触发关键词: Azure, 虚拟机, 存储, 虚拟网络, 微软云, 云部署, microsoft azure
tags:
- Operations
- Azure
- 云计算
- 部署
tools:
- read
- exec
---

# Azure管理入门工具（免费版）

## 概述

本工具为个人开发者和初创团队提供Azure基础资源管理能力。支持虚拟机、存储账户、虚拟网络等常用资源的创建与管理，通过简化命令行操作降低Azure使用门槛。

## 核心能力

### 资源管理

| 资源类型 | 功能 | 免费版支持 |
| --- | --- | --- |
| 虚拟机 | 创建/启动/停止/删除 | 支持 |
| 存储账户 | 创建/上传/下载 | 支持 |
| 虚拟网络 | 网络/子网配置 | 支持 |
| 网络安全组 | 规则管理 | 支持 |
| 资源组 | 创建/管理 | 支持 |
| 数据库 | SQL数据库 | 不支持 |
| 函数应用 | 无服务器 | 不支持 |
| 监控 | Application Insights | 不支持 |

## 使用场景

### 场景一：创建虚拟机

用户输入："帮我创建一台Azure虚拟机"

```bash
# 创建虚拟机
python3 scripts/azure.py vm create \
  --name "my-vm" \
  --resource-group my-rg \
  --image UbuntuLTS \
  --size Standard_B1s \
  --admin-username azureuser

# 输出虚拟机信息
```

### 场景二：存储账户操作

用户输入："创建存储账户并上传文件"

```bash
# 创建存储账户
python3 scripts/azure.py storage create \
  --name mystorage2026 \
  --resource-group my-rg \
  --sku Standard_LRS

# 上传文件
python3 scripts/azure.py storage upload \
  --account mystorage2026 \
  --container data \
  --file ./data.csv
```

### 场景三：虚拟网络配置

用户输入："创建虚拟网络和子网"

```bash
# 创建虚拟网络
python3 scripts/azure.py vnet create \
  --name my-vnet \
  --resource-group my-rg \
  --address-prefix 10.0.0.0/16

# 创建子网
python3 scripts/azure.py vnet subnet create \
  --vnet my-vnet \
  --name my-subnet \
  --address-prefix 10.0.1.0/24
```

## 快速开始

### 环境准备

```bash
# 安装Azure CLI
# macOS: brew install azure-cli
# Windows: 下载官方安装包

# 登录Azure
az login

# 安装Python依赖
pip install azure-mgmt-compute azure-mgmt-storage azure-identity
```

### 常用命令

```bash
# 虚拟机管理
python3 scripts/azure.py vm create --name "my-vm" --resource-group my-rg --image UbuntuLTS --size Standard_B1s
python3 scripts/azure.py vm list --resource-group my-rg
python3 scripts/azure.py vm start --name "my-vm" --resource-group my-rg
python3 scripts/azure.py vm stop --name "my-vm" --resource-group my-rg

# 存储管理
python3 scripts/azure.py storage create --name mystorage --resource-group my-rg
python3 scripts/azure.py storage upload --account mystorage --container data --file ./file.txt

# 虚拟网络
python3 scripts/azure.py vnet create --name my-vnet --resource-group my-rg --address-prefix 10.0.0.0/16
```

## 配置示例

### Azure配置

```yaml
azure_config:
  subscription_id: "${AZURE_SUBSCRIPTION_ID}"
  tenant_id: "${AZURE_TENANT_ID}"
  client_id: "${AZURE_CLIENT_ID}"
  client_secret: "${AZURE_CLIENT_SECRET}"

  defaults:
    location: "eastus"
    resource_group: "my-rg"
    vm:
      size: "Standard_B1s"
      image: "UbuntuLTS"
      admin_username: "azureuser"
    storage:
      sku: "Standard_LRS"
      encryption: true

  tags:
    Project: "my-project"
    Environment: "dev"
    ManagedBy: "azure-toolkit"
```

## 最佳实践

1. **资源组管理**：按项目或环境分组资源，便于管理
2. **最小权限**：服务主体仅授予必要权限
3. **成本控制**：使用B系列突发型虚拟机，适合开发测试
4. **标签规范**：统一标签规范，便于成本追踪

| 实践要点 | 说明 |
| --- | --- |
| 凭证安全 | 服务主体密钥不要写入代码 |
| 成本控制 | 及时停止/删除不用的资源 |
| 位置选择 | 选择离用户最近的位置 |
| 免费额度 | 关注免费层额度，避免意外收费 |

## 常见问题

### Q1：免费版支持Azure SQL数据库吗？

免费版不包含Azure SQL数据库管理。如需管理数据库资源，建议升级PRO版。

### Q2：如何认证Azure？

推荐使用服务主体（Service Principal）认证。通过 `az ad sp create-for-rbac` 创建服务主体，将凭证配置到环境变量或配置文件。

### Q3：支持多区域部署吗？

免费版主要在单一区域操作。如需多区域批量部署，建议升级PRO版。

### Q4：如何控制Azure成本？

建议：使用B系列虚拟机、及时释放资源、使用Azure Cost Management监控支出、设置预算告警。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+
- **Azure CLI**: 2.0+（推荐，用于登录配置）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| azure-identity | Python库 | 必需 | `pip install azure-identity` |
| azure-mgmt-compute | Python库 | 必需 | `pip install azure-mgmt-compute` |
| azure-mgmt-storage | Python库 | 必需 | `pip install azure-mgmt-storage` |
| azure-mgmt-network | Python库 | 必需 | `pip install azure-mgmt-network` |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| 订阅ID | `AZURE_SUBSCRIPTION_ID` | 必需 | 资源订阅 |
| 租户ID | `AZURE_TENANT_ID` | 必需 | AD认证 |
| 客户端ID | `AZURE_CLIENT_ID` | 必需 | 服务主体 |
| 客户端密钥 | `AZURE_CLIENT_SECRET` | 必需 | 服务主体认证 |

- 凭证通过 `az login` 或服务主体配置
- 建议使用服务主体而非交互式登录

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 通过Azure SDK管理基础云资源
- **免费版限制**: 基础资源管理、单区域、不支持数据库与无服务器
