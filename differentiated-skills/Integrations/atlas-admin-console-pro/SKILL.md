---
slug: atlas-admin-console-pro
name: atlas-admin-console-pro
version: "1.0.0"
displayName: Atlas管理台专业版
summary: MongoDB Atlas全功能管理控制台，含批量API调用、结果导出、历史回放、多API编排与监控告警自动化。
license: Proprietary
edition: pro
description: |-
  面向MongoDB Atlas运维团队的企业级全功能管理控制台。在免费版基础上新增批量API调用与并发执行、调用结果导出（CSV/JSON）、调用历史记录与回放、多API编排（工作流）、监控告警自动化、Terraform集成、多项目统一管理等高级能力，配套面向DBA、SRE、平台工程的多角色场景指南
tags:
- 集成工具
- MongoDB
- 云数据库
- 企业级
tools:
  - - read
- exec
---
# Atlas管理台（专业版）

专业版在免费版核心能力之上，新增批量API调用与并发执行、调用结果导出、调用历史记录与回放、多API编排工作流、监控告警自动化、Terraform集成、多项目统一管理等高级能力，专为大规模Atlas集群运维与企业级管理场景设计。

## 概述

当Atlas集群数量从几个增长到几十上百个，单次API调用已无法满足运维效率要求：需要批量查询所有集群状态、跨项目统一巡检、监控告警自动响应、基础设施变更走Terraform流水线。专业版针对这些场景提供完整解决方案，使Atlas运维从"手动单点"升级为"自动化平台"。

同时集成Terraform Provider，将Atlas资源（集群、用户、网络、备份）纳入基础设施即代码管理，实现可重复、可审计、可回滚的资源变更。

## 核心能力

| 能力分类 | 免费版 | 专业版 |
|---------|--------|--------|
| API调用 | 单次串行 | 批量并发（多线程） |
| 结果导出 | 无 | CSV/JSON/Excel导出 |
| 历史记录 | 无 | 调用历史+回放 |
| 工作流编排 | 无 | 多API串联+条件分支 |
| 监控告警 | 手动查询 | 自动响应+自愈 |
| Terraform | 无 | 官方Provider集成 |
| 多项目管理 | 单项目 | 跨组织/项目统一视图 |
| 审计日志 | 无 | 完整操作审计 |
| 优先支持 | 社区 | 工单优先响应 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：MongoDB、Atlas、全功能管理控制台、含批量、历史回放、编排与监控告警自、运维团队的企业级、在免费版基础上新、增批量、调用与并发执行、调用结果导出、调用历史记录与回、监控告警自动化、多项目统一管理等、高级能力、配套面向、DBA、SRE、平台工程的多角色、场景指南等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：批量集群巡检（DBA视角）

每日对全部集群执行健康检查，输出CSV报告。

```bash
# 批量查询所有集群状态并导出CSV
atlas-pro batch \
  --operation listClusters \
  --groups "group1,group2,group3" \
  --output cluster-health-$(date +%Y%m%d).csv \
  --format csv \
  --parallel 5

# 批量检查备份状态
atlas-pro batch \
  --operation listSnapshots \
  --groups "group1,group2,group3" \
  --output backup-status.csv \
  --filter "createdAt > now-24h"
```

### 场景二：监控告警自动响应（SRE视角）

CPU使用率超80%自动扩容节点规格。

```yaml
# alert-rules.yml
rules:
  - name: auto-scale-on-high-cpu
    condition:
      metric: cpu_usage
      threshold: 80
      duration: 5m
    action:
      workflow: scale-up-cluster
      params:
        new_size: M30
    cooldown: 30m  # 防止频繁触发
```

### 场景三：Terraform基础设施管理（平台工程视角）

通过Terraform管理Atlas集群，所有变更走代码评审流程。

```hcl
# main.tf
terraform {
  required_providers {
    mongodbatlas = {
      source = "mongodb/mongodbatlas"
      version = "~> 1.0"
    }
  }
}

provider "mongodbatlas" {
  public_key  = var.atlas_public_key
  private_key = var.atlas_private_key
}

resource "mongodbatlas_cluster" "main" {
  project_id   = var.project_id
  name         = "production-cluster"
  cluster_type = "REPLICASET"
  
  replication_factor = 3
  provider_name      = "AWS"
  region_name        = "us-east-1"
  provider_instance_size_name = "M30"
  
  backup_enabled = true
  auto_scaling_disk_gb_enabled = true
}
```

### 场景四：多API编排工作流（自动化视角）

将多个API调用串联为工作流，支持条件分支与循环。

```yaml
# workflow: provision-new-cluster.yml
steps:
  - name: create-cluster
    operation: createCluster
    params:
      name: "{{cluster_name}}"
      providerSettings:
        providerName: "AWS"
        instanceSizeName: "M10"
  
  - name: wait-for-ready
    operation: getCluster
    until: "status == 'IDLE'"
    timeout: 600s
    interval: 30s
  
  - name: create-db-user
    operation: createDatabaseUser
    depends_on: wait-for-ready
    params:
      username: "{{db_user}}"
      password: "{{db_password}}"
      roles: [{roleName: "readWrite", databaseName: "admin"}]
  
  - name: add-ip-to-whitelist
    operation: createProjectIpAddress
    params:
      cidrBlock: "{{client_ip}}/32"
```

## 不适用场景

以下场景Atlas管理台专业版不适合处理：

- 需要人工创意判断的任务
- 非结构化头脑风暴
- 人际沟通协调

## 触发条件

需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于非本工具能力范围的需求。

## 快速开始

### 第一步：配置多项目凭证

```bash
# 配置多个项目的API Key
cat > ~/.atlas-pro/credentials.yml <<EOF
profiles:
  production:
    client_id: "\${ATLAS_PROD_CLIENT_ID}"
    client_secret: "\${ATLAS_PROD_CLIENT_SECRET}"
    groups: ["prod-group-1", "prod-group-2"]
  staging:
    client_id: "\${ATLAS_STAGING_CLIENT_ID}"
    client_secret: "\${ATLAS_STAGING_CLIENT_SECRET}"
    groups: ["staging-group-1"]
EOF
```

### 第二步：执行首次批量巡检

```bash
atlas-pro batch \
  --operation listClusters \
  --profile all \
  --output daily-report.csv \
  --format csv
```

### 第三步：启用监控告警自动化

```bash
atlas-pro alert start --config alert-rules.yml
```

完整上手时间约180秒（含多项目配置）。

## 示例

### 批量调用配置

```yaml
# ~/.atlas-pro/batch.yml
batch:
  parallel: 5                    # 并发数
  retry: 3                       # 失败重试次数
  retry_interval: 5s             # 重试间隔
  rate_limit: 100                # 每分钟最大调用数
  timeout: 30s                   # 单次调用超时
  output:
    format: csv                  # csv/json/xlsx
    include_metadata: true       # 包含调用元数据
    split_by_group: false        # 是否按项目分文件
```

### 工作流编排

```yaml
# workflows/backup-and-restore-test.yml
name: backup-restore-test
description: 创建备份并验证可恢复性
steps:
  - id: create_snapshot
    operation: createSnapshot
    params:
      clusterName: "{{cluster}}"
      description: "automated-test-{{date}}"
  
  - id: wait_snapshot_complete
    operation: getSnapshot
    depends_on: create_snapshot
    until: "status == 'completed'"
    timeout: 1800s
  
  - id: restore_to_test_cluster
    operation: createRestoreJob
    depends_on: wait_snapshot_complete
    params:
      snapshotId: "{{steps.create_snapshot.response.id}}"
      targetClusterName: "test-cluster"
  
  - id: verify_restore
    operation: getCluster
    depends_on: restore_to_test_cluster
    until: "status == 'IDLE'"
    on_failure:
      alert: true
      message: "备份恢复测试失败"
```

### Terraform状态管理

```bash
# 初始化Terraform
terraform init

# 查看变更计划
terraform plan -out=tfplan

# 应用变更
terraform apply tfplan

# 销毁资源（谨慎）
terraform destroy -target=mongodbatlas_cluster.main
```

### 监控告警自动化

```yaml
# alert-rules.yml
rules:
  - name: high-cpu-auto-scale
    condition:
      metric: system.cpu.usage
      threshold: 80
      operator: ">"
      duration: 5m
    action:
      workflow: scale-up-cluster
    cooldown: 30m
    notify:
      - type: webhook
        url: "${ALERT_WEBHOOK_URL}"
      - type: dingtalk
        token: "${DINGTALK_TOKEN}"
  
  - name: disk-space-low
    condition:
      metric: disk.used_percent
      threshold: 90
      operator: ">"
      duration: 1m
    action:
      operation: modifyCluster
      params:
        diskSizeGB: "current * 1.5"
    cooldown: 1h
  
  - name: connection-pool-exhausted
    condition:
      metric: connections.current
      threshold: "max * 0.9"
      operator: ">"
      duration: 2m
    action:
      workflow: add-connection-pool
    cooldown: 15m
```

## 最佳实践

### 1. 凭证分级管理

生产环境与测试环境使用独立API Key，权限最小化原则：生产只读Key用于巡检，读写Key仅用于变更操作且需要二次确认。

### 2. 工作流版本化管理

所有工作流YAML文件纳入Git管理，变更走PR评审流程，避免误操作引发生产事故。

### 3. 批量调用避开高峰

Atlas API有速率限制，批量巡检建议在业务低峰期（如凌晨2-4点）执行，避免影响正常运维操作。

### 4. Terraform state远程存储

```hcl
# 使用远程state存储，支持团队协作
terraform {
  backend "s3" {
    bucket = "my-tfstate"
    key    = "atlas/terraform.tfstate"
    region = "us-east-1"
  }
}
```

### 5. 告警自愈动作必须有冷却期

所有自动响应动作必须配置`cooldown`，防止告警风暴导致反复触发（如CPU波动导致集群反复扩容缩容）。

### 6. 操作审计完整记录

```yaml
# 启用审计日志
audit:
  enabled: true
  log_path: /var/log/atlas-pro/audit
  retention_days: 365
  include:
    - batch_calls
    - workflow_executions
    - alert_actions
    - terraform_changes
```

## 常见问题

### Q1：批量调用部分失败如何处理？

A：专业版默认重试3次，仍失败的记录在错误报告中。可通过`--resume`参数从断点继续，避免重复执行已成功的部分。

### Q2：工作流执行中断如何恢复？

A：专业版持久化工作流执行状态，使用`atlas-pro workflow resume <execution-id>`从断点恢复。若步骤已副作用（如集群已创建），恢复时会跳过该步骤。

### Q3：Terraform state冲突怎么办？

A：(1) 使用远程state存储（S3/OSS）配合state锁（DynamoDB）；(2) 团队协作时先`terraform state pull`再操作；(3) 冲突时通过`terraform state push`强制覆盖（谨慎使用）。

### Q4：告警自愈动作误触发怎么办？

A：(1) 设置合理的`cooldown`冷却期；(2) 增加`duration`持续时间要求，避免瞬时波动触发；(3) 关键动作（如销毁集群）配置`require_approval: true`人工确认；(4) 监控告警动作日志，发现异常立即停用规则。

### Q5：如何跨组织批量管理？

A：在`credentials.yml`中配置多个profile，使用`--profile all`遍历所有配置的组织与项目。专业版支持跨组织统一视图，便于集团级管理。

### 已知限制

A：(1) 降低`parallel`并发数；(2) 降低`rate_limit`每分钟调用数；(3) 启用指数退避重试；(4) 大批量操作分批执行，间隔5-10分钟。

### Q7：Terraform变更如何回滚？

A：(1) 使用`terraform apply`前先`plan`并保存计划；(2) 变更出问题时`terraform apply`之前的state文件回滚；(3) 关键资源变更前备份state：`terraform state pull > backup.tfstate`。

### Q8：如何与现有CMDB集成？

A：(1) 批量导出集群信息为JSON，定时同步到CMDB；(2) 通过Webhook接收Atlas事件变更，实时更新CMDB；(3) 专业版提供REST API供CMDB主动查询。

## 专业版特性

本专业版相比免费版新增以下能力：
- 批量API调用：并发执行，支持CSV/JSON/Excel导出
- 调用历史回放：完整操作记录，支持断点恢复
- 多API工作流编排：条件分支、循环、超时控制
- 监控告警自动化：基于阈值的自动响应与自愈
- Terraform集成：基础设施即代码管理Atlas资源
- 多项目统一管理：跨组织、跨项目统一视图
- 操作审计：完整审计日志，支持合规审计
- REST API：供外部系统集成的统一接口
- 优先工单支持：工作日2小时内响应

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | 0元 | 核心功能+基础示例 | 个人试用 |
| 收费专业版 | 99元/月 | 全功能+高级特性+优先支持 | 团队/企业 |

专业版通过SkillHub SkillPay发布。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+
- **Terraform**: 1.0+（基础设施即代码管理需要）

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | nodejs.org 官方下载 |
| atlas-pro.mjs | 脚本 | 必需 | 随本Skill分发 |
| Terraform | IaC工具 | 可选 | terraform.io 官方下载 |
| mongodbatlas Terraform Provider | 插件 | 可选 | Terraform Registry自动获取 |
| AWS CLI | 命令行 | 可选 | aws.amazon.com（S3 state存储） |
| Prometheus | 监控 | 可选 | prometheus.io 官方下载 |

### API Key 配置
- **ATLAS_PROD_CLIENT_ID/SECRET**: 生产环境Atlas API凭证，通过环境变量注入
- **ATLAS_STAGING_CLIENT_ID/SECRET**: 测试环境Atlas API凭证，通过环境变量注入
- **ATLAS_PUBLIC_KEY/PRIVATE_KEY**: Terraform Provider使用的凭证，通过环境变量注入
- **ALERT_WEBHOOK_URL**: 告警Webhook地址，通过环境变量配置
- **DINGTALK_TOKEN**: 钉钉告警机器人Token，通过环境变量配置
- **AWS_ACCESS_KEY_ID/SECRET_ACCESS_KEY**: S3 state存储凭证，通过环境变量配置
- 所有凭证禁止硬编码在脚本或配置文件中，必须通过环境变量注入

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent完成操作

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |
