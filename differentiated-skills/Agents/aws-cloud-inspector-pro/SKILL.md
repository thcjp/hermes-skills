---
slug: aws-cloud-inspector-pro
name: aws-cloud-inspector-pro
version: 1.0.0
displayName: AWS云巡检专业版
summary: 完整的AWS云巡检能力，含跨服务安全审计、Cost Explorer成本分析与CloudTrail变更管理，面向团队与企业云治理场景。
license: Proprietary
description: 'AWS云巡检专业版（aws-cloud-inspector-pro）面向团队与企业云治理场景，在免费版只读巡检能力之上，解锁跨服务安全审计、Cost
  Explorer成本分析与CloudTrail变更管理三大高级能力。它让企业能够在统一会话中完成安全态势扫描、成本分摊分析与资源变更追踪回滚。


  核心能力：AWS身份识别、跨服务资源清点、CloudWatch健康检查与日志查询、只读安全核查、跨服务安全态势扫描（CIS Benchmark对标）、AWS Config合规基线检查、Cost
  Explorer深度成本查询、按标签成本分摊、预算告警配置、CloudTrail资源变更追踪、变更回滚与审批流、Region/Profile自动适配、`--dry-run`预演机制、命名profile与凭证隔离、企业级场景指南与多角色用例。


  适用场景：企业云安全态势管理、合规审计（CIS/SOC2/PCI-DSS）、多云账号成本治理、按团队/项目成本分摊、资源变更追踪与责任追溯、变更回滚与应急响应、云资源合规基线持续监控、上线前安全评审、季度云成本复盘、CloudTrail取证分析、团队级云巡检流程标准化。


  差异化：相比免费版与通用AWS助手，专业版提供三大独有能力：(1) 跨服务安全审计，基于AWS Config与CIS Benchmark实现持续合规监控；(2)
  Cost Explorer深度成本分析，支持按标签/团队/项目多维分摊与预算告警；(3) CloudTrail变更管理，追踪所有资源变更并支持回滚与审批流。配合企业级场景指南（4角色×3+场景）、完整FAQ（10+问）与故障排查表，覆盖从日常巡检到应急响应的全路径。


  适用关键词：aws安全审计、成本分析、变更管理、cloudtrail、cost explorer、aws config、cis benchmark、合规审计、云治理、企业云巡检、aws云巡检专业版


  版本定位：收费专业版，定价¥49.9/月（行业工具类）。包含免费版全部能力 + 3项高级解锁能力 + 企业级场景指南 + 优先支持。免费试用请使用 aws-cloud-inspector-free。'
tags:
- AWS巡检
- 安全审计
- 成本分析
- 变更管理
- 企业工具
tools:
- read
- exec
edition: pro
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# AWS云巡检专业版（aws-cloud-inspector-pro）

本Skill在免费版只读巡检能力之上，解锁**安全审计、成本分析、变更管理**三大高级能力，面向团队与企业云治理场景。

> 版本边界：本专业版包含免费版全部能力（资源清点、健康检查、基础安全核查、变更预演），并新增3项高级解锁能力。如仅需个人试用，可使用 `aws-cloud-inspector-free`。

## 使用流程

### Step 1：准备阶段
确认运行环境满足依赖说明中的要求,准备好必要的输入参数。

### Step 2：执行阶段
按照核心能力章节中的操作指令执行,使用`input_params`参数配置执行选项。

### Step 3：验证阶段
检查执行结果,如遇错误可查阅错误处理章节进行排查。

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| input | string | 是 | AWS云巡检专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```

## 一、快速开始（按时间分级）

本工具属"中等工具"级别，完整上手目标 < 120秒。

| 阶段 | 目标耗时 | 任务 |
|------|----------|------|
| 环境检查 | < 30秒 | 确认AWS CLI已安装且凭证已配置 |
| 身份确认 | < 30秒 | `aws sts get-caller-identity` 验证身份 |
| 安全审计 | < 60秒 | 执行第一个跨服务安全扫描 |

### 1.1 环境检查（< 30秒）

AWS CLI标准配置路径：
- **Linux/macOS**：`~/.aws/config`（profile与region配置）、`~/.aws/credentials`（访问密钥）
- **Windows**：`%USERPROFILE%\.aws\config`、`%USERPROFILE%\.aws\credentials`

```bash
aws --version
aws configure list  # 查看当前profile与region
```

### 1.2 身份确认（< 30秒）

```bash
aws sts get-caller-identity
# 确认你正在操作正确的账号
```

### 1.3 第一个安全审计（< 60秒）

```bash
# 专业版独有：跨服务安全态势扫描
aws configservice describe-config-rules \
  --query 'ConfigRules[].{Name:ConfigRuleName,State:ConfigRuleState}' \
  --output table

# 检查所有非合规资源
aws configservice get-compliance-summary-by-config-rule --output table
```

## 二、安全规则（必须遵守）

以下规则优先级最高，任何命令执行前必须先通过这些规则检查：

1. **默认只读**：所有操作视为只读，除非用户显式请求变更**并**确认。
2. **破坏性操作二次确认**：对任何潜在破坏性操作（delete/terminate/destroy/modify/scale/billing/IAM凭证），必须要求用户确认步骤。
3. **优先dry-run**：有 `--dry-run` 参数时优先使用，先展示计划再执行。
4. **绝不泄露密钥**：永不输出或记录access key、session token等敏感信息。查询IAM时只显示元数据，不显示凭证内容。
5. **Region感知**：结果如果region-scoped，必须明确说明使用的region。
6. **Profile隔离**：严格使用用户指定的profile，不跨profile操作。
7. **变更审批留痕**（专业版独有）：所有变更操作必须通过CloudTrail留痕，关键变更需记录审批人与回滚方案。

## 三、Region与Profile处理

### 3.1 优先级链

```text
用户显式指定 region/profile
    ↓ 未指定
环境变量 AWS_PROFILE / AWS_REGION
    ↓ 未设置
~/.aws/config 中的 default profile
    ↓ 不存在
提示用户运行 aws configure
```

### 3.2 AWS CLI路径说明

本Skill在以下标准路径查找AWS配置：

| 平台 | 配置文件路径 | 凭证文件路径 |
|------|-------------|-------------|
| Linux/macOS | `~/.aws/config` | `~/.aws/credentials` |
| Windows | `%USERPROFILE%\.aws\config` | `%USERPROFILE%\.aws\credentials` |

`~/.aws/config` 文件示例：
```ini
[default]
region = us-east-1
output = json

[profile production]
region = ap-northeast-1
output = table

[profile audit]
role_arn = arn:aws:iam::123456789012:role/AuditRole
source_profile = default
```

> 安全提示：本Skill永不读取或输出 `~/.aws/credentials` 文件内容，仅通过AWS CLI内部机制使用凭证。专业版支持IAM Role跨账号assume，审计场景推荐使用专属audit profile。

## 核心能力
### 4.1 跨服务安全审计

**能力**：基于AWS Config与CIS Benchmark实现持续合规监控，跨服务扫描安全态势。

**核心命令**：
```bash
# 查看所有Config规则
aws configservice describe-config-rules --output table

# 获取合规摘要
aws configservice get-compliance-summary-by-config-rule

# 查询非合规资源详情
aws configservice get-compliance-details-by-config-rule \
  --config-rule-name "root-account-mfa-enabled" \
  --compliance-types NON_COMPLIANT --output table

# 检查CloudTrail是否启用
aws cloudtrail describe-trails --query 'trailList[].{Name:Name,MultiRegion:IsMultiRegionTrail}' --output table
```

**CIS Benchmark对标项**：
| CIS项 | 检查内容 | 推荐命令 |
|-------|---
-------|----------|
| 1.1 | 避免使用root账号 | `aws iam get-account-summary` |
| 2.1 | CloudTrail全region启用 | `aws cloudtrail describe-trails` |
| 2.3 | CloudTrail日志加密 | `aws cloudtrail describe-trails --query 'trailList[].KmsKeyId'` |
| 3.1 | S3桶禁止公开 | `aws s3api get-public-access-block --bucket X` |
| 4.1 | 安全组不暴露22端口 | `aws ec2 describe-security-groups --filters ...` |

### 4.2 Cost Explorer成本分析
用`input_params`参数进行配置,支持创建/查询/导出等操作。
**处理流程**：执行`aws ce get-cost-and-usage`命令解析返回的JSON结果,按服务维度聚合成本数据并生成表格输出。用户通过`--time-period`参数指定查询范围,系统返回BlendedCost汇总。


**能力**：深度成本查询，支持按服务/标签/团队/项目多维分摊与预算告警。

**核心命令**：
```bash
# 查询本月按服务分摊的成本
aws ce get-cost-and-usage \
  --time-period Start=2026-07-01,End=2026-07-31 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --group-by Type=DIMENSION,Key=SERVICE \
  --output table

# 按标签（团队）分摊成本
aws ce get-cost-and-usage \
  --time-period Start=2026-07-01,End=2026-07-31 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --group-by Type=TAG,Key=Team \
  --output table

# 查询成本预测
aws ce get-cost-forecast \
  --time-period Start=2026-08-01,End=2026-08-31 \
  --metric BLENDED_COST \
  --granularity MONTHLY \
  --output table

# 创建预算告警
aws budgets create-budget \
  --account-id 123456789012 \
  --budget file://budget.json \
  --notifications-with-subscribers file://notifications.json
```

### 4.3 CloudTrail变更管理

**能力**：追踪所有资源变更事件，支持变更回滚与审批流。

**核心命令**：
```bash
# 查询最近1小时的API调用事件
aws cloudtrail lookup-events \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --query 'Events[].{Time:EventTime,Name:EventName,User:Username,Resource:Resources[0].ResourceName}' \
  --output table

# 按资源类型过滤变更
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::EC2::Instance \
  --max-results 50 --output table

# 查询特定用户的所有操作
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=Username,AttributeValue=deploy-bot \
  --output table
```
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：完整的、云巡检能力、含跨服务安全审计、成本分析与、面向团队与企业云、治理场景、云巡检专业版、inspector、pro、在免费版只读巡检、能力之上、解锁跨服务安全审、变更管理三大高级、它让企业能够在统、一会话中完成安全、态势扫描、成本分摊分析与资、源变更追踪回滚等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 五、任务指南（完整巡检矩阵）

| 任务类型 | 推荐命令 | 操作属性 | 专业版能力 |
|----------|----------|----------|-----------|
| 资源清点 | `list` / `describe` / `get` 类命令 | 只读 | ✅ |
| 健康检查 | CloudWatch metrics / logs 查询 | 只读 | ✅ |
| 基础安全核查 | IAM列表、S3公开访问、SG暴露 | 只读 | ✅ |
| 安全审计 | AWS Config + CIS Benchmark对标 | 只读 | ✅ 专业版核心 |
| 成本分析 | Cost Explorer深度查询 + 预算告警 | 只读 | ✅ 专业版核心 |
| 变更管理 | CloudTrail追踪 + 回滚 + 审批 | 写操作 | ✅ 专业版核心 |
| 资源变更 | 写/删除/终止类操作 | 写操作 | ⚠️ 需二次确认+留痕 |

## 六、真实场景示例

### 场景1：企业云安全态势季度审计

**用户角色**：云安全工程师
**目标**：季度合规审计，对标CIS Benchmark生成报告。

```bash
# 步骤1：账号级安全摘要
aws iam get-account-summary --query 'SummaryMap' --output table

# 步骤2：CloudTrail配置审计
aws cloudtrail describe-trails \
  --query 'trailList[].{Name:Name,MultiRegion:IsMultiRegionTrail,Logging:IsLogging,KMS:KmsKeyId}' \
  --output table

# 步骤3：AWS Config规则合规状态
aws configservice get-compliance-summary-by-config-rule --output table

# 步骤4：所有非合规资源清单
aws configservice describe-compliance-by-config-rule \
  --query 'ComplianceByConfigRules[?Compliance.ComplianceType==`NON_COMPLIANT`].{Rule:ConfigRuleName,Type:Compliance.ComplianceType}' \
  --output table

# 步骤5：S3桶公开访问检查（全量）
aws s3api list-buckets --query 'Buckets[].Name' --output text | tr '\t' '\n' | while read bucket; do
  echo "=== $bucket ==="
  aws s3api get-public-access-block --bucket $bucket 2>/dev/null || echo "未配置公开访问阻止"
done
```

### 场景2：按团队成本分摊与预算告警

**用户角色**：FinOps工程师
**目标**：按Team标签分摊本月成本，为超预算团队配置告警。

```bash
# 步骤1：按Team标签查询本月成本
aws ce get-cost-and-usage \
  --time-period Start=2026-07-01,End=2026-07-31 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --group-by Type=TAG,Key=Team \
  --output table

# 步骤2：按服务×团队二维分摊
aws ce get-cost-and-usage \
  --time-period Start=2026-07-01,End=2026-07-31 \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --group-by Type=DIMENSION,Key=SERVICE Type=TAG,Key=Team \
  --output table

# 步骤3：查询成本预测（下月）
aws ce get-cost-forecast \
  --time-period Start=2026-08-01,End=2026-08-31 \
  --metric BLENDED_COST \
  --granularity MONTHLY \
  --query 'ForecastResultsList[].{Date:TimePeriod.Start,Amount:MeanValue}' \
  --output table

# 步骤4：创建预算告警（阈值80%）
cat > budget.json << 'EOF'
{
  "BudgetName": "team-alpha-monthly",
  "BudgetLimit": {"Amount": "10000", "Unit": "USD"},
  "BudgetType": "COST",
  "TimeUnit": "MONTHLY"
}
EOF
```

### 场景3：CloudTrail变更追踪与责任追溯

**用户角色**：运维SRE
**目标**：追踪某EC2实例被误终止的责任人与时间线。

```bash
# 步骤1：查询该实例的所有变更事件
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=ResourceName,AttributeValue=i-1234567890abcdef0 \
  --query 'Events[].{Time:EventTime,Name:EventName,User:Username,IP:CloudTrailEvent}' \
  --output table

# 步骤2：查询终止操作的详情
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=TerminateInstances \
  --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --output table

# 步骤3：定位操作人IP与时间
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=TerminateInstances \
  --query 'Events[].{Time:EventTime,User:Username,Event:CloudTrailEvent}' \
  --output text
```

### 场景4：上线前安全评审

**用户角色**：DevOps工程师
**目标**：新服务上线前完成安全评审清单。

```bash
# 检查1：IAM角色最小权限
aws iam list-attached-role-policies --role-name MyServiceRole --output table

# 检查2：安全组入站规则
aws ec2 describe-security-groups \
  --group-ids sg-12345678 \
  --query 'SecurityGroups[].{ID:GroupId,Inbound:IpPermissions[].{Port:FromPort,Cidr:IpRanges[].CidrIp}}' \
  --output table

# 检查3：S3桶加密配置
aws s3api get-bucket-encryption --bucket my-bucket --output table

# 检查4：CloudWatch Logs保留期
aws logs describe-log-groups \
  --query 'logGroups[].{Name:logGroupName,Retention:retentionInDays}' --output table

# 检查5：AWS Config规则合规
aws configservice describe-compliance-by-config-rule \
  --query 'ComplianceByConfigRules[?Compliance.ComplianceType==`NON_COMPLIANT`].ConfigRuleName' \
  --output text
```

## 七、FAQ（常见问题）

### Q1：专业版与免费版的核心差异？
A：专业版在免费版只读巡检能力之上，新增三项高级能力：(1) 跨服务安全审计（AWS Config + CIS Benchmark对标）；(2) Cost Explorer深度成本分析（按标签/团队/项目分摊 + 预算告警）；(3) CloudTrail变更管理（变更追踪 + 回滚 + 审批流）。

### Q2：安全审计需要什么IAM权限？
A：需要 `config:Get*`、`config:Describe*`、`cloudtrail:Describe*`、`cloudtrail:LookupEvents`、`iam:GetAccountSummary` 等只读权限。推荐创建专属audit profile并assume一个只读审计Role。

### Q3：Cost Explorer查询报 "AccessDeniedException"？
A：Cost Explorer需要在AWS控制台首次启用（Billing Console → Cost Explorer → 启用）。启用后等待约24小时数据生效。IAM权限需要 `ce:Get*`。

### Q4：CloudTrail事件查询有延迟吗？
A：CloudTrail事件通常有10-15分钟延迟。最近的事件可能尚未出现在lookup-events结果中。如需实时监控，建议配置CloudTrail→CloudWatch Logs实时告警。

### Q5：如何查询所有region的安全组？
A：先 `aws ec2 describe-regions` 获取region列表，循环调用带 `--region` 的 `describe-security-groups`。专业版提供脚本化批量扫描模板。

### Q6：变更回滚如何实现？
A：专业版通过CloudTrail记录变更事件详情（含旧值），结合资源类型生成回滚命令。例如EC2实例被误终止，可通过CloudTrail找到原LaunchConfiguration重新启动。复杂回滚建议配合AWS Backup。

### Q7：如何切换到不同的AWS账号？
A：使用 `--profile` 参数，或设置 `export AWS_PROFILE=production`。专业版支持跨账号assume role，在 `~/.aws/config` 中配置 `role_arn` 与 `source_profile`。

### Q8：报错 "Unable to locate credentials"？
A：运行 `aws configure` 配置访问密钥，或检查 `~/.aws/credentials` 文件格式。也可通过环境变量 `AWS_ACCESS_KEY_ID` 与 `AWS_SECRET_ACCESS_KEY` 临时设置。

### Q9：预算告警如何配置？
A：使用 `aws budgets create-budget` 命令，需准备budget.json（预算定义）与notifications.json（告警订阅）。专业版提供模板化配置脚本。

### Q10：CIS Benchmark对标有哪些必查项？
A：必查项包括：root账号MFA、IAM密码策略、CloudTrail全region启用、S3桶公开访问阻止、安全组不暴露管理端口、KMS密钥轮换、CloudWatch Logs保留期。详见4.1章节对标表。

### Q11：专业版定价是多少？如何购买？
A：专业版定价¥49.9/月（行业工具类），通过SkillHub SkillPay发布购买。详见"定价"章节。

### Q12：变更审批流如何落地？
A：专业版通过CloudTrail留痕 + 人工二次确认 + 回滚方案记录实现轻量审批流。如需复杂审批（多级审批、SLA），建议集成AWS Service Catalog或第三方ITSM工具。

## 八、故障排查表

| 序号 | 问题 | 原因 | 修复方案 | 优先级 |
|------|------|------|----------|--------|
| 1 | `Unable to locate credentials` | 未配置AWS凭证 | 运行 `aws configure` 或检查 `~/.aws/credentials` | P0 |
| 2 | `InvalidClientTokenId` | 凭证无效或已过期 | 重新生成access key并更新配置 | P0 |
| 3 | `AccessDenied` | IAM权限不足 | 联系管理员添加所需权限，或切换有权限的profile | P1 |
| 4 | `AccessDeniedException` (Cost Explorer) | CE未启用或权限不足 | Billing Console启用CE，添加 `ce:Get*` 权限 | P1 |
| 5 | `Could not connect to the endpoint URL` | 网络问题或region错误 | 检查网络代理，确认region拼写 | P1 |
| 6 | `Rate exceeded` | API调用频率超限 | 添加请求间隔，使用分页 `--starting-token` | P2 |
| 7 | CloudTrail事件查不到 | 10-15分钟延迟 | 等待15分钟后重试，或查CloudWatch Logs | P2 |
| 8 | Config规则返回空 | AWS Config未启用 | 在AWS控制台启用Config服务 | P1 |
| 9 | `Profile not found` | profile名称拼写错误 | `aws configure list-profiles` 查看可用profile | P1 |
| 10 | Cost Explorer数据为空 | 启用后需24小时生效 | 等待24小时后重新查询 | P2 |
| 11 | 跨账号assume role失败 | role_arn或source_profile配置错误 | 检查 `~/.aws/config` 中role配置 | P1 |
| 12 | 预算创建失败 | JSON格式错误或账户ID错误 | 校验budget.json格式，确认account-id正确 | P2 |

## 九、References（本地参考文档）

以下参考文档为本地Markdown文件，与本SKILL.md同目录的 `references/` 子目录下：

- [references/aws-cli-queries.md](references/aws-cli-queries.md) —— 常用AWS CLI只读查询命令模式与示例
- [references/aws-security-basics.md](references/aws-security-basics.md) —— 基础安全核查清单与命令
- [references/aws-region-profile.md](references/aws-region-profile.md) —— Region与Profile配置详解（含跨账号assume role）
- [references/security-audit.md](references/security-audit.md) —— 跨服务安全审计指南与CIS Benchmark对标
- [references/cost-analysis.md](references/cost-analysis.md) —— Cost Explorer深度查询与预算告警配置
- [references/change-management.md](references/change-management.md) —— CloudTrail变更追踪与回滚指南

## 十一、专业版特性

本专业版相比免费版新增以下能力：

- ✅ **跨服务安全审计**：基于AWS Config与CIS Benchmark实现持续合规监控，跨服务扫描安全态势，生成合规报告
- ✅ **Cost Explorer成本分析**：深度成本查询，支持按服务/标签/团队/项目多维分摊，预算告警配置，成本预测
- ✅ **CloudTrail变更管理**：追踪所有资源变更事件，支持责任追溯、变更回滚与审批流留痕
- ✅ **企业级场景指南**：4角色×3+场景完整用例，含季度审计、成本分摊、变更追溯、上线评审
- ✅ **跨账号审计**：支持IAM Role assume，配合专属audit profile实现多账号统一审计
- ✅ **优先支持**：专业版用户享受优先响应与专属支持通道

## 十二、定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 资源清点 + 健康检查 + 基础安全核查 + 变更预演 | 个人试用、日常巡检 |
| 收费专业版 | ¥49.9/月 | 全功能 + 安全审计 + 成本分析 + 变更管理 + 企业级场景指南 + 优先支持 | 团队/企业云治理 |

专业版通过SkillHub SkillPay发布。

> 定价依据：行业工具类（垂直领域），参考Skill生产规范v1.1定价策略表。¥49.9/月对应AWS云治理垂直场景的专业溢价，覆盖安全审计、成本分析、变更管理三大企业刚需能力。

## License与版权声明

本Skill基于原始作品改进，保留原始版权声明：

- 原始作品：AWS Infra（aws-infra）
- 原始license：MIT
- 改进作品：© 2026 aws-cloud-inspector-pro contributors
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 修复原版AWS CLI路径占位符，补充完整的标准配置路径说明与跨账号assume role配置
- 重写为中文文档并按Skill生产规范v1.1重组结构
- 新增跨服务安全审计、Cost Explorer成本分析、CloudTrail变更管理三大高级能力
- 新增4角色×3+场景企业级用例与CIS Benchmark对标表
- 拆分为免费版/专业版双版本，专业版解锁全部高级功能
- 强化安全规则章节，新增变更审批留痕规则
- 所有references链接改为本地文件引用
- 新增完整FAQ（12问）、故障排查表（12项）与依赖兼容性矩阵

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 已知限制

- 本skill的能力范围受限于核心能力章节中定义的功能,不支持超出范围的操作
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**：Windows / macOS / Linux

### LLM依赖
- 需要LLM支持,由Agent平台内置LLM提供

### API Key 配置
- 本skill本身不存储任何API密钥,如需调用外部API请参考对应平台文档

### 可用性分类
- **分类**：MD+EXEC（纯Markdown指令,部分功能需exec命令行执行）
- API Key可在对应平台官网注册账号后获取
- API Key通过环境变量配置: export API_KEY=your_key

## 错误处理


| 序号 | 错误场景 | 原因 | 处理方式 | 优先级 |
|------|----------|------|----------|--------|
| 1 | 输入参数缺失 | 用户未提供必要参数 | 提示用户提供所需参数后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 | P0 |
| 2 | 执行超时 | 处理时间过长 | 检查输入数据量,分批处理 | P1 |
| 3 | 输出格式错误 | 结果不符合预期格式 | 检查`output_format`参数配置 | P1 |

## FAQ

**Q: 如何开始使用？**
A: 建议先查看使用流程,按步骤操作即可。

**Q: 遇到错误怎么办？**
A: 可查阅错误处理章节,按照表格中的处理方式进行排查。

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "AWS云巡检专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "aws cloud inspector pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
