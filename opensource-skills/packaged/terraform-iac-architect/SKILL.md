---
slug: terraform-iac-architect
name: terraform-iac-architect
version: 1.0.1
displayName: IaC架构师
summary: Terraform基础设施即代码,模块化多环境CI/CD,云资源一键编排
license: Proprietary
description: IaC架构师——基于HashiCorp官方风格规范生成生产级Terraform代码。覆盖模块化设计、状态管理、多环境部署、CI/CD集成全流程。同时提供阿里云ROS/腾讯云Terraform/华为云Terraform国内云适配方案。适用于云基础设施搭建、多环境管理、模块化设计、状态迁移、CI/CD集成场景。触发关键词:Terraform、IaC、基础设施即代码、HCL、模块、状态管理、workspace、terragrunt、Provider、云基础设施、资源编排、ROS、阿里云
tags:
- Terraform
- 基础设施即代码
- 云架构
- IaC
- 资源编排
tools:
- read
- exec
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# IaC架构师

基于 HashiCorp 官方风格规范,生成可维护、可复用、安全的 Terraform 基础设施代码。同时支持国内主流云厂商(阿里云/腾讯云/华为云)的资源编排,从模块设计到状态管理,从多环境部署到 CI/CD 集成,全流程覆盖。

## 核心能力

1. **HCL 代码生成**:遵循 HashiCorp 官方风格规范,生成 main.tf/variables.tf/outputs.tf/versions.tf 完整模块结构
2. **多云 Provider 适配**:AWS/Azure/GCP 海外云 + 阿里云/腾讯云/华为云国内云,统一抽象
3. **状态管理**:Remote State(S3+DynamoDB/OSS+Tablestore/COS)、状态锁定、状态迁移、状态隔离
4. **多环境部署**:Workspace(轻量)/ Terragrunt(目录级)/ 独立状态文件(完全隔离)三种方案
5. **CI/CD 集成**:GitHub Actions / GitLab CI / Jenkins 流水线,OIDC 安全凭证注入

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 云基础设施搭建 | 云厂商、资源需求清单、拓扑图 | 完整 Terraform 模块代码 + 部署说明 |
| 多环境管理 | dev/staging/prod 环境矩阵 + 差异配置 | Workspace/Terragrunt 配置 + 环境隔离方案 |
| 模块化设计 | 团队复用需求 + 资源分组 | 可复用模块 + 版本管理 + 文档 |
| 状态迁移 | 现有 Local State + 目标后端 | 迁移脚本 + Remote State 配置 + 验证步骤 |
| CI/CD 集成 | 代码仓库 + 部署流程要求 | 流水线配置 + OIDC 凭证 + Plan/Apply 自动化 |
| 国内云适配 | AWS Terraform 代码 + 目标国内云 | Provider 替换 + 资源映射 + 测试用例 |

**不适用于**:
- 临时性手工运维操作(适合可版本化、可审查的长期基础设施)
- 容器编排(Kubernetes/Helm,使用专用工具)
- 配置管理(Ansible/Chef/Puppet,专注于基础设施创建而非运行时配置)
- Serverless 函数部署(使用 Serverless Framework/SAM)
- 数据库 Schema 迁移(使用 Flyway/Liquibase)
- 网络设备配置(路由器/交换机,使用 NETCONF/Ansible)

## 使用流程

### Step 1: 基础设施规划
1. **需求分析**:确定需要的云资源(计算/存储/网络/数据库)
2. **云厂商选择**:海外(AWS/Azure/GCP)/ 国内(阿里云/腾讯云/华为云)/ 多云
3. **架构设计**:绘制基础设施拓扑图,确定资源依赖关系
4. **模块划分**:按功能/环境/团队划分 Terraform 模块
5. **状态策略**:选择 remote state 后端
6. **命名规范**:统一资源命名(项目-环境-组件-序号)

### Step 2: HCL 代码编写(遵循官方风格)
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

### Step 3: 状态管理配置
1. **Remote State 后端选择**
   - AWS: S3 + DynamoDB(锁定)
   - 阿里云: OSS + Tablestore(锁定)
   - 腾讯云: COS + MongoDB(锁定)
   - Terraform Cloud(托管,跨云通用)
2. **状态操作**
   - `terraform init`:初始化后端
   - `terraform plan`:预览变更
   - `terraform apply`:应用变更
   - `terraform state list/mv/rm`:状态管理
3. **状态隔离**
   - Workspace:轻量级隔离(共享配置)
   - Terragrunt:目录级隔离,更强(DRY 原则)
   - 独立状态文件:完全隔离(推荐生产环境)

### Step 4: 多环境部署
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

### Step 5: CI/CD 集成
1. **流水线设计**
   - PR 阶段:`terraform fmt -check` + `terraform validate`
   - Plan 阶段:`terraform plan` 输出到 PR 评论
   - Apply 阶段:合并后 `terraform apply`
2. **安全实践**
   - 云凭证通过 OIDC/Secret Manager 注入
   - 状态文件加密
   - 敏感变量从 Vault/Secret Manager 读取
   - Plan 输出中隐藏敏感值

### Step 6: 验证与交付
1. `terraform fmt -check` 格式检查
2. `terraform validate` 语法校验
3. `terraform plan` 预览变更
4. `tflint` 静态分析(最佳实践检查)
5. `terraform apply` 应用变更

## 国内外云 Provider 对照

| 维度 | AWS | 阿里云 | 腾讯云 | 华为云 |
|:-----|:-----|:-----|:-----|:-----|
| Provider | hashicorp/aws | aliyun/alicloud | tencentcloudstack/tencentcloud | huaweicloud/huaweicloud |
| 对象存储 | S3 | OSS | COS | OBS |
| 计算 | EC2 | ECS | CVM | ECS |
| 数据库 | RDS | RDS | CDB | RDS |
| VPC | VPC | VPC | VPC | VPC |
| 状态后端 | S3+DynamoDB | OSS+Tablestore | COS+MongoDB | OBS+DynamoDB 兼容 |
| 国内替代方案 | ROS(资源编排) | - | TIC | RFS |
| 凭证 | AccessKey | AccessKey | SecretId/SecretKey | AK/SK |

## 示例

### 示例1: 创建 AWS VPC 模块(输入→输出)

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | IaC架构师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
用户请求:创建一个 AWS VPC 模块,包含 VPC/子网/路由表/IGW/NAT,支持多可用区
CIDR: 10.0.0.0/16
可用区: us-east-1a, us-east-1b, us-east-1c
```

**输出**(modules/vpc/main.tf 片段):
```hcl
terraform {
  required_version = ">= 1.5"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
# ...
resource "aws_vpc" "this" {
  cidr_block           = var.cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = merge(var.tags, { Name = "${var.name_prefix}-vpc" })
}
# ...
resource "aws_subnet" "public" {
  for_each = toset(var.availability_zones)
# ...
  vpc_id                  = aws_vpc.this.id
  cidr_block              = cidrsubnet(var.cidr_block, 8, index(var.availability_zones, each.value))
  availability_zone       = each.value
  map_public_ip_on_launch = true
  tags = merge(var.tags, { Name = "${var.name_prefix}-public-${each.value}" })
}
# ...
resource "aws_internet_gateway" "this" {
  vpc_id = aws_vpc.this.id
  tags   = merge(var.tags, { Name = "${var.name_prefix}-igw" })
}
# ...
resource "aws_nat_gateway" "this" {
  for_each = toset(var.availability_zones)
# ...
  allocation_id = aws_eip.nat[each.key].id
  subnet_id     = aws_subnet.public[each.key].id
  depends_on     = [aws_internet_gateway.this]
  tags           = merge(var.tags, { Name = "${var.name_prefix}-nat-${each.key}" })
}
```

### 示例2: 阿里云 VPC 模块(国内替代)

**输入**:
```
用户请求:将上述 AWS VPC 模块改为阿里云版本
Region: cn-hangzhou
可用区: cn-hangzhou-a, cn-hangzhou-b, cn-hangzhou-c
```

**输出**(modules/vpc/main.tf 片段):
```hcl
terraform {
  required_providers {
    alicloud = {
      source  = "aliyun/alicloud"
      version = "~> 1.220"
    }
  }
}
# ...
resource "alicloud_vpc" "this" {
  vpc_name   = "${var.name_prefix}-vpc"
  cidr_block = var.cidr_block
}
# ...
resource "alicloud_vswitch" "public" {
  for_each = toset(var.availability_zones)
# ...
  vpc_id            = alicloud_vpc.this.id
  cidr_block        = cidrsubnet(var.cidr_block, 8, index(var.availability_zones, each.value))
  zone_id           = each.value
  vswitch_name      = "${var.name_prefix}-public-${each.value}"
}
```

### 示例3: 多环境部署(输入→输出)

**输入**:
```
用户请求:为 dev/staging/prod 三个环境部署 VPC
方案: 独立状态文件 + tfvars 差异化
```

**输出**(目录结构):
```
environments/
├── dev/
│   ├── main.tf          (引用 vpc 模块)
│   ├── terraform.tfvars (cidr=10.0.0.0/16, azs=1个)
│   └── backend.tf       (OSS bucket=state-dev)
├── staging/
│   ├── main.tf
│   ├── terraform.tfvars (cidr=10.1.0.0/16, azs=2个)
│   └── backend.tf       (OSS bucket=state-staging)
└── prod/
    ├── main.tf
    ├── terraform.tfvars (cidr=10.2.0.0/16, azs=3个)
    └── backend.tf       (OSS bucket=state-prod)
```

## 错误处理
- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断
- 重试机制: 失败时自动重试, 最多3次

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 状态锁定 | 上一次 apply 异常中断,锁未释放 | 等待 5 分钟或手动 `terraform force-unlock <lock-id>` |
| 资源漂移 | 人工修改了云资源 | `terraform plan` 检测差异,`terraform apply` 修正或 `terraform import` 导入 |
| 资源删除失败 | 存在依赖关系 | 先删除依赖资源(如先删 ECS 再删 VPC) |
| Provider 版本冲突 | 多模块使用不同版本 | 固定版本约束,使用 `terraform init -upgrade` 逐步迁移 |
| 状态文件损坏 | 后端存储故障 | 从备份恢复(S3/OSS 版本控制) |
| 敏感信息泄露 | 未标记 sensitive | 添加 `sensitive = true`,检查 plan 输出 |
| 国内 Provider 不支持资源 | 阿里云/腾讯云 Provider 滞后 | 使用 aliyun CLI/tccli 补充,或自定义资源 |
| OSS 状态后端配置错误 | 权限或 region 配置错误 | 检查 RAM 权限、bucket region、endpoint |
| Terraform Cloud 国内访问慢 | 网络延迟 | 切换自建后端(OSS+COS)或使用国内代理 |
| tflint 报错过多 | 团队规范未对齐 | 渐进式修复,先 Critical 后 Warning |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: Terraform CLI >= 1.5

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代 |
|:------|------:|:------|:------|------:|
| Terraform CLI | 工具 | 必需 | hashicorp.com 官方下载 | 国内镜像源 mirrors.aliyun.com/terraform |
| AWS CLI | 工具 | AWS 必需 | aws.amazon.com/cli | 阿里云 CLI(aliyun cli) |
| 阿里云 CLI | 工具 | 阿里云必需 | aliyun.com | - |
| 腾讯云 CLI | 工具 | 腾讯云必需 | cloud.tencent.com | - |
| Terragrunt | 工具 | 可选(复杂场景) | github.com/gruntwork-io/terragrunt | - |
| Terraform Cloud | 服务 | 可选 | hashicorp.com | 自建 OSS/COS 后端 |
| tflint | 工具 | 可选(质量检查) | github.com/terraform-linters/tflint | - |

### API Key 配置
- **AWS**: Access Key ID + Secret Access Key(从 IAM 控制台获取)
- **阿里云**: AccessKey ID + AccessKey Secret(从 RAM 控制台获取)
- **腾讯云**: SecretId + SecretKey(从 CAM 控制台获取)
- **华为云**: AK + SK(从 IAM 控制台获取)
- **安全要求**:
  - 凭证仅通过环境变量或 OIDC 注入,绝不硬编码
  - 生产环境使用 RAM 子账号 + 最小权限策略
  - CI/CD 使用 OIDC 替代长期凭证
  - .gitignore 配置 *.tfvars(可能含敏感值)、.terraform/

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,需 exec 能力运行 terraform 命令

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 阿里云ECS+RDS+SLB基础设施(完整模块)

**输入**:
```
云厂商: 阿里云
Region: cn-hangzhou
需求: 2台ECS(负载均衡)+ 1台RDS(MySQL)+ SLB + VPC网络
规格: ECS ecs.g6.large, RDS rds.mysql.s2.large, SLB slb.s1.small
要求: 模块化,可复用,符合HashiCorp官方风格
```

**LLM生成输出** (`output/aliyun-infra/modules/vpc/main.tf`):
```hcl
# modules/vpc/main.tf
terraform {
  required_version = ">= 1.5"
  required_providers {
    alicloud = {
      source  = "aliyun/alicloud"
      version = "~> 1.220"
    }
  }
}
# ...
resource "alicloud_vpc" "this" {
  vpc_name   = "${var.name_prefix}-vpc"
  cidr_block = var.cidr_block
  tags       = merge(var.tags, { Name = "${var.name_prefix}-vpc" })
}
# ...
resource "alicloud_vswitch" "private" {
  for_each = toset(var.availability_zones)
# ...
  vpc_id       = alicloud_vpc.this.id
  cidr_block   = cidrsubnet(var.cidr_block, 8, index(var.availability_zones, each.value) + 10)
  zone_id      = each.value
  vswitch_name = "${var.name_prefix}-private-${each.value}"
  tags         = merge(var.tags, { Name = "${var.name_prefix}-private-${each.value}" })
}
# ...
resource "alicloud_vswitch" "public" {
  for_each = toset(var.availability_zones)
# ...
  vpc_id       = alicloud_vpc.this.id
  cidr_block   = cidrsubnet(var.cidr_block, 8, index(var.availability_zones, each.value))
  zone_id      = each.value
  vswitch_name = "${var.name_prefix}-public-${each.value}"
  tags         = merge(var.tags, { Name = "${var.name_prefix}-public-${each.value}" })
}
# ...
resource "alicloud_nat_gateway" "this" {
  vpc_id        = alicloud_vpc.this.id
  nat_gateway_name = "${var.name_prefix}-nat"
  specification = "Small"
  vswitch_id    = alicloud_vswitch.public[var.availability_zones[0]].id
  tags          = var.tags
}
# ...
resource "alicloud_eip" "nat" {
  bandwidth            = 100
  internet_charge_type = "PayByTraffic"
}
# ...
resource "alicloud_eip_association" "nat" {
  allocation_id = alicloud_eip.nat.id
  instance_id   = alicloud_nat_gateway.this.id
}
# ...
resource "alicloud_snat_entry" "this" {
  for_each = alicloud_vswitch.private
# ...
  snat_table_id     = alicloud_nat_gateway.this.snat_table_ids[0]
  source_vswitch_id = each.value.id
  snat_ip           = alicloud_eip.nat.ip_address
}
```

**LLM生成输出** (`output/aliyun-infra/modules/vpc/variables.tf`):
```hcl
variable "name_prefix" {
  description = "资源命名前缀,如 myapp-prod"
  type        = string
}
# ...
variable "cidr_block" {
  description = "VPC CIDR块,如 10.0.0.0/16"
  type        = string
  default     = "10.0.0.0/16"
}
# ...
variable "availability_zones" {
  description = "可用区列表"
  type        = list(string)
}
# ...
variable "tags" {
  description = "全局标签"
  type        = map(string)
  default     = {}
}
```

**LLM生成输出** (`output/aliyun-infra/modules/vpc/outputs.tf`):
```hcl
output "vpc_id" {
  description = "VPC ID"
  value       = alicloud_vpc.this.id
}
# ...
output "private_subnet_ids" {
  description = "私有子网ID映射"
  value       = { for k, v in alicloud_vswitch.private : k => v.id }
}
# ...
output "public_subnet_ids" {
  description = "公有子网ID映射"
  value       = { for k, v in alicloud_vswitch.public : k => v.id }
}
```

**LLM生成输出** (`output/aliyun-infra/modules/ecs/main.tf`):
```hcl
# modules/ecs/main.tf
resource "alicloud_security_group" "this" {
  name        = "${var.name_prefix}-sg"
  description = "Security group for ${var.name_prefix}"
  vpc_id      = var.vpc_id
  tags        = var.tags
}
# ...
resource "alicloud_security_group_rule" "allow_http" {
  type              = "ingress"
  ip_protocol       = "tcp"
  port_range        = "80/80"
  security_group_id = alicloud_security_group.this.id
  cidr_ip           = "0.0.0.0/0"
}
# ...
resource "alicloud_security_group_rule" "allow_https" {
  type              = "ingress"
  ip_protocol       = "tcp"
  port_range        = "443/443"
  security_group_id = alicloud_security_group.this.id
  cidr_ip           = "0.0.0.0/0"
}
# ...
resource "alicloud_security_group_rule" "allow_ssh" {
  type              = "ingress"
  ip_protocol       = "tcp"
  port_range        = "22/22"
  security_group_id = alicloud_security_group.this.id
  cidr_ip           = var.ssh_cidr
}
# ...
resource "alicloud_instance" "this" {
  for_each = toset(var.availability_zones)
# ...
  instance_type           = var.instance_type
  image_id                = var.image_id
  security_groups         = [alicloud_security_group.this.id]
  vswitch_id              = var.vswitch_ids[each.value]
  instance_name           = "${var.name_prefix}-ecs-${each.value}"
  host_name               = "${var.name_prefix}-${substr(each.value, -1, 1)}"
  system_disk_category    = "cloud_essd"
  system_disk_size        = var.system_disk_size
  internet_max_bandwidth_out = 0  # 通过NAT访问外网
  tags                    = merge(var.tags, { Name = "${var.name_prefix}-ecs-${each.value}" })
}
```

**LLM生成输出** (`output/aliyun-infra/modules/slb/main.tf`):
```hcl
# modules/slb/main.tf
resource "alicloud_slb_load_balancer" "this" {
  load_balancer_name   = "${var.name_prefix}-slb"
  vswitch_id           = var.vswitch_id
  load_balancer_spec   = var.slb_spec
  address_type         = "internet"
  internet_charge_type = "PayByTraffic"
  tags                 = var.tags
}
# ...
resource "alicloud_slb_listener" "http" {
  load_balancer_id = alicloud_slb_load_balancer.this.id
  backend_port     = 80
  frontend_port    = 80
  protocol         = "http"
  bandwidth        = 10
  health_check     = "on"
  health_check_type = "tcp"