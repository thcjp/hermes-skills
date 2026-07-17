---
slug: terraform-iac-architect
name: terraform-iac-architect
version: "1.0.0"
displayName: "IaC架构师"
summary: "Terraform基础设施即代码,模块化多环境CI/CD,云资源一键编排"
license: MIT
description: |-
  IaC架构师——基于HashiCorp官方风格规范生成生产级Terraform代码。模块化设计+状态管理+多环境部署+CI/CD集成,云资源一键编排,让基础设施像代码一样可版本、可审查、可复用。

  核心能力:
  - HCL语法规范:符合官方风格的可维护Terraform代码
  - 模块化设计:可复用模块开发与版本管理
  - 状态管理:Remote State/状态锁定/状态迁移
  - 多环境部署:Workspace/Terragrunt多环境隔离
  - CI/CD集成:GitHub Actions/GitLab CI自动化部署
  - Provider开发:Terraform Plugin Framework自定义资源
  - 云资源编排:AWS/Azure/GCP/Kubernetes一键部署

  适用场景:
  - 独立创业者云基础设施:新项目云资源一键编排搭建
  - SaaS创业者多环境管理:dev/staging/prod多环境隔离
  - 一人公司CI/CD自动化:基础设施变更自动化部署
  - 技术团队模块复用:可复用模块开发与版本管理

  差异化:不是Terraform语法教程,而是基于官方风格规范的生产级IaC架构师,模块化+状态管理+多环境+CI/CD全链路,让小团队也能管理复杂云基础设施。

  触发关键词:Terraform、IaC、基础设施即代码、HCL、模块、状态管理、workspace、terragrunt、Provider、云基础设施、资源编排
tags: [Terraform, 基础设施即代码, 云架构, IaC, 资源编排]
tools: [read, exec]
---

# IaC架构师

基于 HashiCorp 官方风格规范,生成可维护、可复用、安全的 Terraform 基础设施代码。从模块设计到状态管理,从多环境部署到 CI/CD 集成,全流程覆盖。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 云基础设施搭建 | 新项目/新环境 | AWS/Azure/GCP 资源一键编排 |
| 多环境管理 | dev/staging/prod | Workspace/Terragrunt 多环境隔离 |
| 模块化设计 | 团队复用 | 可复用模块开发与版本管理 |
| 状态迁移 | 状态文件管理 | Local→Remote 迁移,状态锁定 |
| CI/CD 集成 | 自动化部署 | GitHub Actions/GitLab CI 集成 |
| Provider 开发 | 自定义资源 | Terraform Plugin Framework |

## 工作流

### 1. 基础设施规划

1. **需求分析**:确定需要的云资源(计算/存储/网络/数据库)
2. **架构设计**:绘制基础设施拓扑图,确定资源依赖关系
3. **模块划分**:按功能/环境/团队划分 Terraform 模块
4. **状态策略**:选择 remote state 后端(S3/Terraform Cloud/Consul)
5. **命名规范**:统一资源命名(项目-环境-组件-序号)

### 2. HCL 代码编写(遵循官方风格)

1. **文件组织**
   - `main.tf`:资源定义
   - `variables.tf`:输入变量
   - `outputs.tf`:输出值
   - `versions.tf`:版本约束
   - `providers.tf`:Provider 配置
   - `terraform.tfvars`:变量值
2. **代码风格**
   - 资源名使用 snake_case
   - 资源类型与名之间对齐
   - 资源内属性按逻辑分组
   - 使用 `for_each` 优于 `count`(除非需要索引)
   - 变量必须有 description 和 type
   - 敏感变量标记 `sensitive = true`
3. **模块化**
   - 每个模块单一职责
   - 模块版本化(Source + version)
   - 输入输出明确文档化
   - 避免模块间循环依赖

### 3. 状态管理

1. **Remote State 配置**
   - S3 + DynamoDB(锁定)
   - Terraform Cloud(托管)
   - Consul(键值存储)
2. **状态操作**
   - `terraform init`:初始化后端
   - `terraform plan`:预览变更
   - `terraform apply`:应用变更
   - `terraform state list/mv/rm`:状态管理
3. **状态隔离**
   - Workspace:轻量级隔离
   - Terragrunt:目录级隔离,更强
   - 独立状态文件:完全隔离

### 4. 多环境部署

1. **Workspace 方式**(简单场景)
   - `terraform workspace new dev/staging/prod`
   - 变量按 workspace 切换
2. **Terragrunt 方式**(复杂场景)
   - 目录结构隔离环境
   - 继承配置,DRY 原则
   - 跨环境依赖管理
3. **环境差异管理**
   - 变量差异化(tfvars 文件)
   - 资源差异化(count/for_each)
   - 模块版本差异化

### 5. CI/CD 集成

1. **流水线设计**
   - PR 阶段:`terraform fmt -check` + `terraform validate`
   - Plan 阶段:`terraform plan` 输出到 PR 评论
   - Apply 阶段:合并后 `terraform apply`
2. **安全实践**
   - 云凭证通过 OIDC/Secret Manager 注入
   - 状态文件加密
   - 敏感变量从 Vault/Secret Manager 读取
   - Plan 输出中隐藏敏感值

## 依赖说明

| 依赖类型 | 要求 | 说明 |
|:---------|:-----|:-----|
| LLM | 任意支持 Agent Skills 的 LLM | Claude/GPT/Gemini 等 |
| 运行环境 | Terraform CLI >= 1.5 | 本地或 CI/CD 环境安装 |
| 云服务 | AWS CLI / Azure CLI / gcloud | 对应云平台 CLI 工具 |
| API Key | 云平台访问凭证 | AWS Access Key / Azure Service Principal / GCP Service Account |
| 可选 | Terragrunt | 多环境管理(复杂场景) |
| 可选 | Terraform Cloud 账号 | 托管状态管理 + CI/CD |

## 异常处理

| 异常场景 | 处理方式 |
|:---------|:---------|
| 状态锁定 | 等待锁释放或手动解锁(`terraform force-unlock`) |
| 资源漂移 | `terraform plan` 检测,`terraform apply` 修正 |
| 资源删除失败 | 检查依赖关系,先删除依赖资源 |
| Provider 版本冲突 | 固定版本约束,逐步升级 |
| 状态文件损坏 | 从备份恢复(S3 版本控制) |
| 敏感信息泄露 | 标记 `sensitive = true`,检查 plan 输出 |

## 示例

### 输入:创建 AWS VPC 模块

```
用户请求:创建一个 AWS VPC 模块,包含 VPC/子网/路由表/IGW/NAT,支持多可用区

输出文件:
- modules/vpc/main.tf (资源定义)
- modules/vpc/variables.tf (输入变量:cidr/azs/subnets)
- modules/vpc/outputs.tf (输出:vpc_id/subnet_ids)
- modules/vpc/versions.tf (版本约束)
```

### 输入:多环境部署

```
用户请求:为 dev/staging/prod 三个环境部署 VPC

输出:
- environments/dev/main.tf (引用 vpc 模块,dev 参数)
- environments/staging/main.tf (引用 vpc 模块,staging 参数)
- environments/prod/main.tf (引用 vpc 模块,prod 参数)
- 每个环境独立状态文件
```
