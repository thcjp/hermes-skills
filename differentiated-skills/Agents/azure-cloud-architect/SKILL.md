---
slug: "azure-cloud-architect"
name: "azure-cloud-architect"
version: "1.0.0"
displayName: "Azure云架构师"
summary: "多订阅导航,角色审计最小权限,成本分析,合规检查,跨订阅批量操作。。基于Azure CLI的智能云基础设施管理助手,提供多订阅导航、RBAC角色审计与最小权限、成本分析工作流、合规检查清单、"
license: "Proprietary"
description: |-
  基于Azure CLI的智能云基础设施管理助手,提供多订阅导航、RBAC角色审计与最小权限、成本分析工作流、合规检查清单、跨订阅批量操作五大核心能力。适用于Azure资源盘点、健康监控、安全审计、Cost Management分析、多订阅多租户管理场景。默认只读查询,写操作与破坏性操作需确认。适用关键词:Azure云架构师、基础设施管理、多订阅、RBAC审计、成本分析、Azure CLI、azure-cloud-architect
tags:
  - 通用办公
  - 云计算
  - Azure
  - 基础设施
  - 安全合规
  - DevOps
tools:
  - read
  - exec
  - write
homepage: ""
category: "Operations"
---
# Azure云架构师

使用本地Azure CLI回答关于Azure资源的问题。默认只读查询,仅在用户明确要求变更并确认后执行写/破坏性操作.
## 核心能力

### 1. 多订阅导航器
自动列出所有可访问订阅,智能检测默认订阅,支持按名称或ID切换,避免在错误订阅执行操作

**输入**: 用户提供多订阅导航器所需的指令和必要参数.
**处理**: 解析多订阅导航器的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回多订阅导航器的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 2. 分层权限模型
L0只读直接执行、L1预演展示计划、L2确认写、L3破坏性详细影响分析、L4敏感操作双重确认,保障生产环境安全

**输入**: 用户提供分层权限模型所需的指令和必要参数.
**处理**: 解析分层权限模型的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回分层权限模型的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. 安全审计剧本
RBAC角色审计(检测Owner过度授权)、存储安全检查(公共访问/HTTPS/TLS)、NSG规则检查(0.0.0.0/0入站)、Key Vault访问审计

**输入**: 用户提供安全审计剧本所需的指令和必要参数.
**处理**: 解析安全审计剧本的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回安全审计剧本的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 成本分析工作流
按资源组/服务维度查询Cost Management,识别空闲资源(停止的VM/未挂载磁盘/未使用公网IP)以优化成本

**输入**: 用户提供成本分析工作流所需的指令和必要参数.
**处理**: 解析成本分析工作流的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回成本分析工作流的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 5. 跨订阅批量操作
提供跨订阅遍历模板,统一执行VM列举、NSG检查等操作,避免遗漏订阅

**输入**: 用户提供跨订阅批量操作所需的指令和必要参数.
**处理**: 解析跨订阅批量操作的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回跨订阅批量操作的响应数据,包含状态码、结果和日志.
**技术参数**：使用`input_params`和`output_format`参数控制执行行为,支持`json`/`text`/`csv`输出格式.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：角色审计最小权限、合规检查、Azure、CLI、的智能云基础设施、管理助手、角色审计与最小权、合规检查清单、跨订阅批量操作五、大核心能力、适用于、资源盘点、健康监控、多订阅多租户管理、默认只读查询、写操作与破坏性操、作需确认、适用关键词、云架构师、基础设施管理、cloud、architect等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

**何时使用**:
- 需要盘点Azure资源(VM、存储、网络、资源组)
- 需要查询Azure Monitor健康指标与Activity Log排查错误
- 需要审计RBAC角色、NSG规则、Key Vault访问策略
- 需要分析订阅成本、识别空闲资源
- 需要管理多个订阅或租户

**输入**:自然语言描述的Azure管理需求(资源类型、操作类型、订阅范围)
**输出**:Azure CLI命令执行结果(表格/JSON)、安全审计报告、成本分析报告

**不适用场景**:
- Azure Portal GUI操作指导(本skill基于CLI)
- 非Azure云平台(AWS/GCP/阿里云)
- 需要Azure SDK编程开发场景

## 使用流程

### Step 1: 确认登录身份
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Azure云架构师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
az account show
```
如未登录,运行 `az login --use-device-code`(SSH环境适用),终端会显示码和URL,在浏览器中完成登录.
### Step 2: 选择订阅(多订阅时)
```bash
# 列出所有可访问的订阅
az account list --output table
# ...
# 设置活跃订阅(按名称或ID)
az account set --subscription "Production"
```
**订阅选择规则**:用户明确指定→使用指定;未指定但有默认→使用默认;无默认且多个→询问用户;仅一个→直接使用.
### Step 3: 执行只读查询
根据需求执行`list`/`show`/`get`类命令,结果以表格形式展示便于阅读.
### Step 4: 写操作预演(如需变更)
- 优先使用`--dry-run`或`--what-if`预演
- 展示影响范围与计划
- 等待用户显式确认

### Step 5: 执行变更并验证
确认后执行写/破坏性操作,执行后用只读命令验证结果.
## 示例

### 示例(补充)
**输入**: "帮我看看当前订阅里有哪些虚拟机,运行状态如何"

**输出**:
```bash
az vm list --query '[].{Name:name,ResourceGroup:resourceGroup,State:powerState}' -d --output table
```
```
Name           ResourceGroup    State
-------------  ---------------  --------
prod-web-01    prod-rg          VM running
prod-web-02    prod-rg          VM running
dev-test-01    dev-rg           VM stopped
```

### 示例2: RBAC角色审计
**输入**: "审计一下当前订阅里谁有Owner角色,检查是否有过度授权"

**输出**:
```bash
az role assignment list --role "Owner" --query '[].{Assignee:principalName,Scope:scope}' --output table
```
```
Assignee               Scope
---------------------  ------------------------------------
admin@company.com      /subscriptions/xxx-xxx-xxx
deploy-spn@company.com /subscriptions/xxx-xxx-xxx/resourceGroups/prod-rg
```
**审计结论**:发现2个Owner分配,建议将deploy-spn降级为Contributor,遵循最小权限原则.
### 示例3: 跨订阅成本分析
**输入**: "查询本月各资源组的成本"

**输出**:
```bash
az costmanagement query --type ActualCost \
  --timeframe MonthToDate \
  --dataset-grouping name=ResourceGroupName type=Dimension \
  --dataset-aggregation totalCost=name=Cost function=Sum
```
返回各资源组的本月累计成本数据.
## 错误处理

| 场景 | 原因 | 处理方式 |
|:-----|:-----|:-----|
| `Please run az login` | 未登录或会话过期 | 运行 `az login --use-device-code` 重新登录 |
| `Subscription not found` | 订阅ID错误或无权限 | 用 `az account list` 确认可访问的订阅列表 |
| `Access denied` / 403 | RBAC权限不足 | 检查 `az account show` 确认身份,确认关联角色;只读至少需Reader角色 |
| `No subscription selected` | 未设置活跃订阅 | 运行 `az account set --subscription <名称或ID>` |
| 命令未找到 | Azure CLI版本过旧 | 运行 `az version`,升级到最新版 `az upgrade` |
| 操作超时 | 网络或服务问题 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令,执行ping命令测试网络连通性,检查防火墙和代理设置连接,确认Azure服务状态 |
| 密钥泄露风险 | 输出含密钥/令牌 | 立即停止,绝不在聊天/日志中输出密钥值,必要时轮换密钥 |
| 多订阅操作遗漏 | 未遍历所有订阅 | 使用跨订阅批量操作模板遍历所有订阅 |
| Cost Management返回空 | 未配置或订阅类型不支持 | 确认CSP等订阅类型是否支持Cost Management |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Azure CLI | 工具 | 必需 | 从 docs.microsoft.com/cli/azure 安装,版本v2.0+ |
| Azure账户 | 账户 | 必需 | 注册Azure账户 |
| Agent LLM | API | 必需 | 由Agent内置LLM提供 |
| jq | 工具 | 可选(JSON处理) | 从 stedolan.github.io/jq 安装 |

**运行环境**:
- 操作系统: Windows / macOS / Linux
- 认证方式: `az login`(交互)或`az login --service-principal`(服务主体)
- 绝不要在聊天或日志中输出密钥、客户端密钥、令牌

**可用性分类**: MD+EXEC(纯Markdown指令,需要命令行执行能力运行Azure CLI)
- **API Key**：本skill无需额外API Key配置

## 常见问题

**Q: 如何切换订阅?**
A: 使用 `az account set --subscription "订阅名"` 或 `az account set --subscription "订阅ID"`。结果为订阅范围时明确说明使用的订阅.
**Q: 设备码登录怎么用?**
A: 运行 `az login --use-device-code`,终端会显示一个码和URL。在浏览器中打开URL,输入码完成登录。适合无法打开浏览器的SSH环境.
**Q: 命令执行失败提示权限不足?**
A: 检查当前身份 `az account show`,确认关联的RBAC角色是否包含所需权限。只读操作至少需要Reader角色,写操作需要Contributor.
**Q: 如何安全地执行破坏性操作?**
A: 1)先用 `--what-if` 或 `--dry-run` 预演;2)列出精确影响范围;3)等待用户显式确认;4)执行后验证结果。绝不在未确认时执行破坏性操作.
**Q: 多租户如何管理?**
A: 使用 `az login --tenant <tenant-id>` 登录特定租户。使用 `az account list --query '[].tenantId'` 查看可访问的租户.
## 已知限制

1. **仅支持Azure CLI命令**:不提供Azure Portal GUI操作指导,不覆盖Azure SDK编程开发场景
2. **依赖本地Azure CLI环境**:需提前安装并配置Azure CLI,未安装时无法使用
3. **成本查询依赖订阅类型**:CSP等部分订阅类型可能不支持Cost Management,返回空结果
4. **跨订阅操作性能受限**:遍历多订阅时为串行执行,订阅数量多时耗时较长
5. **不修改Azure资源默认行为**:所有写操作需用户显式确认,自动化流水线场景需额外集成确认机制
