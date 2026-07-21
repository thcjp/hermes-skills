---
slug: aws-toolkit-pro
name: aws-toolkit-pro
version: "1.0.0"
displayName: AWS部署专业版
summary: 企业级AWS全服务管理平台，支持多区域、IaC、合规审计与成本优化。
license: Proprietary
edition: pro
description: |-
  面向企业运维团队的AWS全服务管理平台。支持EC2/S3/VPC/RDS/Lambda/
  CloudWatch等全量AWS服务，提供基础设施即代码（IaC）、多区域批量
  部署、合规审计、成本优化与安全扫描功能。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。
tags:
- Operations
- AWS
- 企业级
- 基础设施
tools:
  - - read
- exec
---

# AWS部署专业版（PRO版）

## 概述

本平台为企业运维团队提供全功能的AWS管理能力。相比免费版，PRO版新增全量服务支持、基础设施即代码、多区域部署、合规审计和成本优化等高级功能，全面满足企业级AWS基础设施管理的复杂需求。

PRO版完全兼容免费版全部命令与配置，升级后原有资源管理可直接使用。

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 服务覆盖 | 5项基础服务 | 30+全量服务 |
| 部署方式 | 命令行 | +IaC(Terraform/CFN) |
| 区域支持 | 单区域 | 多区域批量 |
| 合规审计 | 不支持 | 支持 |
| 成本优化 | 不支持 | 分析+建议 |
| 安全扫描 | 不支持 | 自动扫描 |
| 监控告警 | 不支持 | CloudWatch |
| 灾备管理 | 不支持 | 跨区域灾备 |

### 支持的AWS服务

| 类别 | 服务 | PRO版支持 |
| --- | --- | --- |
| 计算 | EC2/Lambda/ECS/EKS/Batch | 支持 |
| 存储 | S3/EBS/EFS/FSx/Glacier | 支持 |
| 网络 | VPC/Route53/CloudFront/ELB | 支持 |
| 数据库 | RDS/DynamoDB/ElastiCache/Redshift | 支持 |
| 安全 | IAM/KMS/WAF/GuardDuty | 支持 |
| 监控 | CloudWatch/CloudTrail/X-Ray | 支持 |
| AI/ML | SageMaker/Rekognition/Lex | 支持 |
| 分析 | Athena/EMR/Kinesis/Glue | 支持 |

## 使用场景

### 场景一：IaC基础设施部署

用户输入："用Terraform部署一套Web应用架构"

```bash
# 生成Terraform配置
python3 scripts/infra.py generate \
  --template "web_app_ha" \
  --regions "us-east-1,us-west-2" \
  --output ./terraform/

# 部署基础设施
python3 scripts/infra.py apply \
  --config ./terraform/ \
  --auto-approve

# 输出：
# VPC: 10.0.0.0/16 (2区域)
# EC2: 4台 (2区域x2可用区)
# RDS: 主从 (跨区域灾备)
# ELB: 负载均衡 (2区域)
# Route53: 健康检查+故障转移
```

### 场景二：合规审计

用户输入："检查AWS环境的合规性"

```bash
# 合规审计
python3 scripts/audit.py run \
  --standards "CIS,PCI-DSS,HIPAA" \
  --output audit_report.pdf

# 输出包含：
# - 合规检查项清单
# - 不合规项详情
# - 修复建议
# - 风险等级评估
```

### 场景三：成本优化

用户输入："分析AWS成本并给出优化建议"

```bash
# 成本分析
python3 scripts/cost.py analyze \
  --period "3m" \
  --output cost_report.xlsx

# 优化建议
python3 scripts/cost.py optimize \
  --apply-recommendations \
  --dry-run

# 输出：
# - 月度成本趋势
# - 各服务成本占比
# - 闲置资源识别
# - 预留实例建议
# - 预估节省金额
```

## 快速开始

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt

# 安装Terraform
# macOS: brew install terraform
# Linux: 下载官方安装包

# 配置多区域凭证
cp config_pro_template.yaml config_pro.yaml
```

### 常用命令

```bash
# IaC部署
python3 scripts/infra.py generate --template "web_app_ha" --regions "us-east-1,us-west-2"
python3 scripts/infra.py apply --config ./terraform/

# 合规审计
python3 scripts/audit.py run --standards "CIS,PCI-DSS"

# 成本优化
python3 scripts/cost.py analyze --period "3m"
python3 scripts/cost.py optimize --dry-run

# 安全扫描
python3 scripts/security.py scan --output security_report.pdf

# 多区域管理
python3 scripts/regions.py deploy --template web_app --regions "us-east-1,eu-west-1,ap-southeast-1"
```

## 示例

### PRO企业级配置

```yaml
pro_config:
  regions:
    primary: "us-east-1"
    secondary: ["us-west-2", "eu-west-1", "ap-southeast-1"]

  infrastructure:
    iac: "terraform"               # terraform | cloudformation
    state_backend: "s3"
    state_bucket: "my-tf-state"
    state_lock: "dynamodb"

  services:
    compute: ["ec2", "lambda", "ecs", "eks"]
    database: ["rds", "dynamodb", "elasticache"]
    storage: ["s3", "ebs", "efs"]
    networking: ["vpc", "route53", "cloudfront"]
    security: ["iam", "kms", "waf", "guardduty"]
    monitoring: ["cloudwatch", "cloudtrail", "x-ray"]

  audit:
    standards: ["CIS", "PCI-DSS", "HIPAA", "SOC2"]
    schedule: "weekly"
    auto_remediation: false        # 自动修复（谨慎开启）

  cost:
    analysis_period: "3m"
    recommendations: true
    budget_alerts:
      monthly: 10000
      alert_threshold: 0.8

  security:
    scan_frequency: "daily"
    vulnerability_scan: true
    config_compliance: true

  disaster_recovery:
    enabled: true
    rpo: 15                        # 恢复点目标（分钟）
    rto: 30                        # 恢复时间目标（分钟）
    cross_region: true
```

## 最佳实践

### PRO版企业实践

| 实践领域 | 建议做法 |
| --- | --- |
| IaC管理 | 使用Terraform版本控制，团队协作 |
| 多区域 | 关键业务多区域部署，确保高可用 |
| 合规审计 | 定期运行合规检查，及时修复 |
| 成本治理 | 设置预算告警，定期审查支出 |
| 安全扫描 | 每日扫描，高危漏洞及时修复 |

### 免费版兼容性

```text
免费版命令 → PRO版命令（增强）：
aws.py ec2 create       → infra.py generate + apply (IaC)
aws.py s3 create-bucket → +加密+版本控制+生命周期
单区域操作               → 多区域批量部署+灾备
```

## 常见问题

### Q1：Terraform和CloudFormation选哪个？

Terraform跨云通用、语法简洁、社区活跃；CloudFormation为AWS原生、深度集成、无额外依赖。建议新项目用Terraform，AWS深度用户可选CloudFormation。

### Q2：合规审计支持哪些标准？

支持CIS AWS Benchmark、PCI-DSS、HIPAA、SOC2等主流合规标准。每项标准包含数十至数百个检查项，覆盖安全配置、访问控制、日志审计等方面。

### Q3：成本优化能节省多少？

视环境而定。常见优化项包括：删除闲置资源（可节省10-30%）、购买预留实例（可节省30-60%）、使用Spot实例（可节省70-90%）。PRO版提供详细建议与预估节省金额。

### Q4：安全扫描包含什么？

包含：开放端口检测、IAM权限过度、S3公开访问、安全组过宽、SSL证书过期、已知漏洞等。扫描结果按风险等级分类，提供修复建议。

### Q5：多区域灾备如何实现？

通过Terraform在多个区域部署相同架构，使用Route53健康检查实现自动故障转移。RDS使用跨区域只读副本，S3开启跨区域复制。RPO和RTO可根据业务需求配置。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+
- **Terraform**: 1.0+（IaC部署需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| boto3 | Python库 | 必需 | `pip install boto3` |
| awscli | CLI工具 | 必需 | `pip install awscli` |
| terraform | CLI工具 | 可选 | 官网下载（IaC部署） |
| botocore | Python库 | 必需 | 随boto3安装 |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| AWS Access Key | `AWS_ACCESS_KEY_ID` | 必需 | API认证 |
| AWS Secret | `AWS_SECRET_ACCESS_KEY` | 必需 | API认证 |
| AWS Region | `AWS_DEFAULT_REGION` | 必需 | 默认区域 |
| 多区域凭证 | 配置文件profile | 推荐 | 多区域操作 |

- 建议使用IAM角色而非Access Key（EC2上）
- 凭证通过 `aws configure --profile` 管理多账户

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+IaC执行）
- **说明**: 企业级AWS全服务管理平台，支持IaC与合规审计
- **PRO版特性**: 全量服务、IaC部署、多区域、合规审计、成本优化、安全扫描
- **兼容性**: 完全兼容免费版命令与配置

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 依赖云服务，需要网络连接
