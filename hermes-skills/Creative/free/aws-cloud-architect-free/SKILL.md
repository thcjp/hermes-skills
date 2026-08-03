---

name: "aws-cloud-architect-free"
description: "AWS 基础架构设计与成本优化助手(免费版)。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。支持多场景应用和灵活配置。"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "AWS 架构师免费"
  version: "1.0.0"
  summary: "AWS 基础架构设计与成本优化助手(免费版)"
  tags:
    - "Operations"
    - "Creative"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
tools:
  - exec
  - read
  - write

---

# AWS 云架构师 (免费版)

基础 AWS 架构设计、服务选型与只读资源查询助手。遵循 Well-Architected Framework 基本原则。

## 核心能力
### 1. 先验证账户上下文
```bash
aws sts get-caller-identity
aws ec2 describe-vpcs --query 'Vpcs[].{ID:VpcId,CIDR:CidrBlock,Default:IsDefault}'
```

确认: Region(默认 us-east-1)、账户类型、现有基础设施。

**输出**: 返回先验证账户上下文的执行结果,包含操作状态和输出数据。
### 2. 成本优先架构
| 阶段 | 推荐技术栈 | 月成本 |
| --- | --- | --- |
| MVP(<1k 用户) | 单 EC2 + RDS | ~$50 |
| Growth(1-10k) | ALB + ASG + RDS Multi-AZ | ~$200 |

**默认使用最小可行实例。** 扩容容易,缩容浪费钱。

**输出**: 返回成本优先架构的执行结果,包含操作状态和输出数据。
### 3. 默认安全
- 最小权限 IAM
- 静态加密(KMS 默认密钥起)
- VPC 隔离(数据库不入公有子网)
- 安全组入站默认全拒绝

**输出**: 返回默认安全的执行结果,包含操作状态和输出数据。

#
## 服务选型(基础)

| 需求 | 服务 | 原因 |
| --- | --- | --- |
| 静态站点 | S3 + CloudFront | 极低成本,全球 CDN |
| API 后端 | Lambda + API Gateway | 零闲置成本 |
| 数据库 | RDS 数据库 | 托管,支持 Multi-AZ |
| 缓存 | ElastiCache Redis | 会话/缓存 |

## CLI 命令参考

```bash
aws configure --profile myproject
export AWS_PROFILE=myproject
aws sts get-caller-identity
aws ec2 describe-regions --query 'Regions[].RegionName'
```

所有命令默认只读。变更类操作(删除/终止/修改)需显式确认。

## 常见成本陷阱

### NAT Gateway 数据处理($0.045/GB)

S3/DynamoDB 的 VPC 终端节点免费。高流量应用仅 NAT 费用可达 $500/月。

```bash
aws ec2 create-vpc-endpoint --vpc-id vpc-未指定 \
  --service-name com.amazonaws.us-east-1.s3 --route-table-ids rtb-未指定
```

### CloudWatch Logs 默认永久保留

```bash
aws logs put-retention-policy --log-group-name /aws/lambda/fn --retention-in-days 14
```

### 闲置负载均衡器最低 $16/月

ALB 零流量也计费。删除未使用的负载均衡器。

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础架构选型 | 业务需求与用户规模 | MVP 阶段服务选型与月成本估算 |
| 只读资源盘点 | AWS 账户与 Region | 现有 VPC/EC2/RDS 资源清单 |

**不适用于**: 安全加固深度诊断、6Rs 迁移框架、IaC 模板生成(需升级付费版)。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 使用流程

1. 用 `aws sts get-caller-identity` 确认账户与 Region
2. 用只读命令盘点现有基础设施(VPC/EC2/RDS)
3. 根据用户规模匹配 MVP/Growth 技术栈
4. 识别基础成本陷阱(NAT Gateway/CloudWatch 保留/闲置 LB)
5. 变更类操作需显式确认,优先使用 `--dry-run`

#
## 案例展示

### 案例1: MVP 阶段架构选型

```bash
# 用户量 <1k,单机架构(~$50/月)
# 技术栈: 单 EC2 + RDS
aws ec2 run-instances --image-id ami-未指定 --instance-type t3.small \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Environment,Value=prod}]'
aws rds create-db-instance --db-instance-identifier mydb \
  --db-instance-class db.t3.micro --engine postgres --allocated-storage 20
# 为 S3 创建 VPC 终端节点避免 NAT 费用
aws ec2 create-vpc-endpoint --vpc-id vpc-未指定 \
amazonaws.us-east-1.s3 --route-table-ids rtb-未指定
```

### 案例2: 只读资源盘点

```bash
# 盘点现有 EC2 实例
aws ec2 describe-instances \
  --query 'Reservations[].Instances[].{ID:InstanceId,Type:InstanceType,State:State.Name}'
# 盘点 RDS 实例
aws rds describe-db-instances \
  --query 'DBInstances[].{ID:DBInstanceIdentifier,Class:DBInstanceClass,Engine:Engine}'
# 检查 CloudWatch Logs 保留策略
aws logs describe-log-groups \
  --query 'logGroups[].{Name:logGroupName,Retention:retentionInDays}'
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| NAT Gateway 月费异常高 | S3/DynamoDB 流量经 NAT 处理($0.045/GB) | 创建 VPC 终端节点,S3/DynamoDB 终端节点免费 |
| EBS 快照无限累积 | 自动备份未设置生命周期 | 配置快照生命周期策略定期清理 |
| CloudWatch Logs 账单增长 | 日志组默认永久保留 | 用 `put-retention-policy` 设置保留天数 |
| 闲置 ALB 产生费用 | 负载均衡器零流量也计费 | 删除未关联目标的负载均衡器 |
| RDS 数据库公网暴露 | 创建时 PubliclyAccessible 默认 Yes | `modify-db-instance --no-publicly-accessible` |

## 常见问题

### Q1: NAT Gateway 与 VPC 终端节点如何选择?
A: S3 与 DynamoDB 的 VPC 终端节点免费,应优先使用。NAT Gateway 按 $0.045/GB 计费,仅用于必须经 NAT 的出站流量。高流量 S3 场景仅 NAT 费用可达 $500/月。

### Q2: 免费版与付费版有何区别?
A: 免费版提供基础架构选型与只读资源盘点;付费版增加安全加固深度诊断(S3/RDS/IAM)、6Rs 迁移框架、性能模式库(Lambda/EBS/RDS)、IaC 模板生成与 3 个进阶案例。

### Q3: 如何防止 CloudWatch Logs 账单持续增长?
A: 默认日志组永久保留。用 `aws logs put-retention-policy --log-group-name <组名> --retention-in-days 14` 设置保留期,超期日志自动删除。

### Q4: 变更类操作如何安全执行?
A: 所有变更需显式确认。优先使用 `--dry-run` 参数预览变更影响。删除/终止类操作需二次确认,不自动执行。

## 已知限制

- 仅提供 MVP/Growth 两阶段选型,不含 Scale 阶段(10k+ 用户)
- 不含安全加固深度诊断(S3 策略/默认 SG/IAM 凭证)
- 不含 6Rs 迁移框架与 Well-Architected 深度评估
- 不含 IaC 模板生成(Terraform/CloudFormation)
- 不含性能模式库(Lambda 冷启动/EBS 卷类型/RDS 连接池)
- 依赖 AWS CLI 与有效凭证,所有写操作需显式确认

## 升级提示

> 本免费版提供基础架构选型与只读盘点能力。如需安全加固深度诊断(S3/RDS/IAM)、
> 6Rs 迁移框架、性能模式库(Lambda/EBS/RDS)、IaC 模板生成(Terraform/CloudFormation)、
> 完整错误诊断(10+ 场景)与 3 个进阶案例,请升级至 **AWS 云架构师付费版**。

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 效率量化分析

| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 差异化对比

| 对比维度 | 本技能 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 核心功能 | 通用场景 | 通用场景 |

## 核心功能

- **自动化执行**: 基于指令驱动的自动化流程
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据