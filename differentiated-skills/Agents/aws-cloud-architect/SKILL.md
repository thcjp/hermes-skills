---
slug: aws-cloud-architect
name: aws-cloud-architect
version: "1.0.0"
displayName: AWS云架构师
summary: 安全审计剧本,成本优化工作流,分层权限模型,智能上下文检测,零暴露密钥。
license: MIT
description: |-
  AWS云架构师是一个基于AWS CLI的智能云基础设施管理助手。针对传统AWS管理"安全误配置风险、成本失控、读写权限混淆、区域配置复杂、IAM排障困难、密钥泄露风险"六大痛点,构建了安全审计剧本、成本优化工作流、分层权限模型、智能上下文检测和零暴露密钥规则五大核心能力。

  核心能力包括:默认只读查询保障安全;写操作与破坏性操作需双重确认;支持--dry-run预演;身份识别先行(sts get-caller-identity);资源清单/健康检查/安全审计/成本分析全场景覆盖;区域与配置文件智能检测。

  适用场景:AWS资源盘点与查询、CloudWatch健康监控与错误排查、IAM与S3安全审计、Cost Explorer成本分析、基础设施变更规划、多区域多账号管理、安全合规检查。

  差异化亮点:相比原始版本,新增安全审计剧本(IAM/S3/SG/KMS检查清单)、成本优化工作流(空闲资源识别+建议生成)、分层权限模型(只读→dry-run→确认写→破坏性)、智能上下文检测(环境变量→配置文件→默认值)、零暴露密钥硬约束、批量查询缓存策略、FAQ与故障排查决策树。

  触发关键词:AWS云架构师、基础设施管理、安全审计、成本优化、AWS CLI、aws-cloud-architect、资源盘点
tags:
- 智能代理
- 云计算
- AWS
- 基础设施
- 安全审计
tools:
- read
- exec
---

# AWS云架构师

使用本地AWS CLI回答关于AWS资源的问题。默认只读查询,仅在用户明确要求变更并确认后执行写/破坏性操作。

## 快速开始

1. **确认身份**(每次会话第一步):
   ```bash
   aws sts get-caller-identity
   ```
2. **检测区域/配置文件**(参见智能上下文检测)
3. **使用只读命令**回答问题
4. **如需变更**,列出精确命令并等待确认后执行

## 安全规则(最高优先级)

* 所有操作默认**只读**,除非用户明确要求变更**且**确认
* 破坏性操作(删除/终止/销毁/修改/扩缩容/计费/IAM凭据)需要确认步骤
* 优先使用 `--dry-run` 预演并展示计划
* **绝不要**透露或记录密钥(访问密钥、会话令牌)
* **绝不要**将密钥输出到聊天或日志

## 智能上下文检测(差异化)

### 区域与配置文件优先级

```
用户明确指定 → 使用用户指定
     │未指定
AWS_PROFILE / AWS_REGION 环境变量 → 使用环境变量
     │未设置
~/.aws/config 默认配置 → 使用默认
     │无配置
询问用户
```

### 检测流程

```bash
# 1. 检查环境变量
echo "Profile: ${AWS_PROFILE:-未设置}, Region: ${AWS_REGION:-未设置}"

# 2. 检查配置文件
aws configure list

# 3. 确认身份
aws sts get-caller-identity
```

结果为区域范围时,明确说明使用的区域。

## 分层权限模型(差异化)

| 层级 | 操作类型 | 策略 | 示例命令 |
|------|----------|------|----------|
| L0 只读 | list/describe/get | 直接执行 | `aws s3 ls` |
| L1 预演 | 写操作(有dry-run) | 展示计划,确认后执行 | `aws ec2 run-instances --dry-run` |
| L2 确认写 | 写操作(无dry-run) | 列出影响范围,等待确认 | `aws s3 cp file.txt s3://bucket/` |
| L3 破坏性 | delete/terminate/destroy | 详细影响分析+确认 | `aws ec2 terminate-instances` |
| L4 敏感 | IAM凭据/计费 | 双重确认+影响警告 | `aws iam create-access-key` |

## 任务指南

### 资源盘点/列表
使用 `list`/`describe`/`get` 命令:
```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType]'
aws s3api list-buckets --query 'Buckets[*].Name'
aws rds describe-db-instances
```

### 健康/错误检查
使用CloudWatch指标/日志查询:
```bash
# EC2 CPU利用率
aws cloudwatch get-metric-statistics --namespace AWS/EC2 \
  --metric-name CPUUtilization --dimensions Name=InstanceId,Value=i-xxx \
  --start-time 2025-01-01T00:00:00Z --end-time 2025-01-02T00:00:00Z \
  --period 3600 --statistics Average

# 查询日志
aws logs filter-log-events --log-group-name /aws/lambda/my-function \
  --filter-pattern "ERROR" --limit 20
```

## 安全审计剧本(差异化)

### IAM审计
```bash
# 列出所有用户
aws iam list-users --query 'Users[*].[UserName,CreateDate]'

# 检查Root账户MFA
aws iam get-account-summary --query 'SummaryMap.AccountMFAEnabled'

# 列出Access Key(不显示密钥值)
aws iam list-access-keys --user-name username

# 检查策略附着
aws iam list-attached-user-policies --user-name username
```

### S3安全检查
```bash
# 检查公共访问阻止设置
aws s3api get-public-access-block --bucket bucket-name

# 检查Bucket策略
aws s3api get-bucket-policy --bucket bucket-name

# 列出无加密的Bucket
aws s3api get-bucket-encryption --bucket bucket-name  # 无返回=未加密
```

### 安全组检查
```bash
# 检查开放到0.0.0.0/0的规则
aws ec2 describe-security-groups \
  --filters Name=ip-permission.cidr,Values=0.0.0.0/0 \
  --query 'SecurityGroups[*].[GroupName,IpPermissions]'
```

### KMS密钥使用检查
```bash
# 列出KMS密钥
aws kms list-keys

# 检查密钥轮换
aws kms get-key-rotation-status --key-id key-id
```

## 成本优化工作流(差异化)

### 成本分析(只读)
```bash
# 月度成本
aws ce get-cost-and-usage --time-period Start=2025-01-01,End=2025-02-01 \
  --granularity MONTHLY --metrics BlendedCost \
  --group-by Type=SERVICE

# 按服务分组成本
aws ce get-cost-and-usage --time-period Start=2025-01-01,End=2025-02-01 \
  --granularity DAILY --metrics BlendedCost \
  --group-by Type=SERVICE
```

### 空闲资源识别
```bash
# 停止的EC2实例
aws ec2 describe-instances --filters Name=instance-state-name,Values=stopped \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType]'

# 未挂载的EBS卷
aws ec2 describe-volumes --filters Name=status,Values=available \
  --query 'Volumes[*].[VolumeId,Size,VolumeType]'

# 未使用的Elastic IP
aws ec2 describe-addresses --query 'Addresses[?InstanceId==null].[PublicIp,AllocationId]'
```

## 批量查询缓存策略(差异化)

对频繁查询的结果进行缓存,减少API调用:

```bash
# 缓存资源列表到本地
aws ec2 describe-instances > /tmp/ec2-instances.json
aws s3api list-buckets > /tmp/s3-buckets.json

# 后续查询从缓存读取
cat /tmp/ec2-instances.json | jq '.Reservations[*].Instances[*].InstanceId'
```

**缓存策略:**
- 资源列表缓存5-10分钟
- 成本数据缓存1小时
- 安全配置缓存30分钟
- 变更操作后立即刷新对应缓存

## 常见问题FAQ

**Q: 如何切换区域?**
A: 使用 `--region` 参数指定,如 `aws ec2 describe-instances --region us-west-2`。或在环境变量设置 `AWS_REGION=us-west-2`。结果为区域范围时明确说明使用的区域。

**Q: 多账号如何管理?**
A: 使用 `--profile` 参数指定配置文件,如 `aws ec2 describe-instances --profile production`。配置文件在 `~/.aws/config` 中定义。

**Q: 命令执行失败提示权限不足?**
A: 检查当前身份 `aws sts get-caller-identity`,确认关联的IAM角色/策略是否包含所需权限。只读操作至少需要ReadOnlyAccess策略。

**Q: 如何安全地执行破坏性操作?**
A: 1)先用 `--dry-run` 预演;2)列出精确影响范围;3)等待用户显式确认;4)执行后验证结果。绝不在未确认时执行破坏性操作。

**Q: 成本查询返回空?**
A: 确认Cost Explorer已在AWS Console中启用。时间格式为 `YYYY-MM-DD`,结束日期是排他的(不包含当天)。

## 故障排查

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `Unable to locate credentials` | 未配置凭据 | 运行 `aws configure` 或设置环境变量 |
| `Access Denied` | IAM权限不足 | 检查身份 `sts get-caller-identity`,确认策略 |
| 区域错误 | 不支持的区域 | 确认区域支持目标服务,用 `--region` 指定 |
| 命令未找到 | AWS CLI版本过旧 | 运行 `aws --version`,升级到最新版 |
| 超时 | 网络或服务问题 | 重试,检查网络连接,确认服务状态 |
| 输出格式混乱 | 默认输出格式 | 使用 `--output table` 或 `--output json` |
| 密钥泄露风险 | 输出含密钥 | 立即停止,绝不在聊天/日志中输出密钥值 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent
- **操作系统**: Windows / macOS / Linux
- **AWS CLI**: v2.0+

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| AWS CLI | 工具 | 必需 | 从aws.amazon.com/cli安装 |
| AWS账户 | 账户 | 必需 | 注册AWS账户 |
| jq | 工具 | 可选(JSON处理) | 从stedolan.github.io/jq安装 |

### API Key 配置
- 需要AWS访问密钥(AWS_ACCESS_KEY_ID、AWS_SECRET_ACCESS_KEY)
- 通过 `aws configure` 配置,或设置环境变量
- **绝不要**在聊天或日志中输出密钥值

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,需要命令行执行能力运行AWS CLI)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent使用AWS CLI管理云基础设施。需要AWS CLI和AWS账户。
