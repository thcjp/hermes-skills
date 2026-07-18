---
slug: aws-cost-optimizer-tool-pro
name: aws-cost-optimizer-tool-pro
version: "1.0.0"
displayName: AWS成本优化专业版
summary: 企业级AWS成本管理平台，支持多账户、自动优化、RI建议与FinOps治理。
license: MIT
edition: pro
description: |-
  面向企业云财务团队的AWS成本管理平台。支持多账户统一分析、自动
  优化执行、预留实例（RI）/Savings Plans建议、预算告警与FinOps
  治理。内置成本分摊与chargeback报告，全面满足企业云成本管理需求。

  核心能力:
  - 多账户/多组织统一成本分析
  - 自动优化执行（一键清理闲置资源）
  - RI/Savings Plans购买建议
  - 预算告警与异常检测
  - FinOps治理与成本分摊
  - Chargeback/Showback报告
  - 成本预测与年度规划
  - 标签合规性管理

  适用场景:
  - 企业多账户成本管理
  - FinOps云财务治理
  - 自动化成本优化
  - RI/SP采购决策
  - 部门成本分摊

  差异化:
  - 兼容免费版单账户分析，无缝升级
  - 新增多账户与自动优化
  - RI/SP购买建议
  - FinOps治理与chargeback
  - 成本预测与规划

  触发关键词: AWS, 成本优化, 多账户, 自动优化, RI, Savings Plans, FinOps, chargeback, 预算
tags:
- Operations
- AWS
- 成本优化
- 企业级
- FinOps
tools:
- read
- exec
---

# AWS成本优化专业版（PRO版）

## 概述

本平台为企业云财务团队提供全功能的AWS成本管理能力。相比免费版，PRO版新增多账户管理、自动优化、RI/SP建议、FinOps治理和chargeback报告等高级功能，全面满足企业级云成本管理的复杂需求。

PRO版完全兼容免费版单账户分析命令，升级后原有成本分析可直接使用。

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 账户支持 | 单账户 | 多账户/组织 |
| 优化执行 | 仅建议 | 自动执行 |
| RI/SP建议 | 不支持 | 智能建议 |
| 预算告警 | 不支持 | 多级告警 |
| FinOps治理 | 不支持 | 完整体系 |
| Chargeback | 不支持 | 成本分摊 |
| 成本预测 | 不支持 | 年度规划 |
| 标签管理 | 不支持 | 合规管理 |

## 使用场景

### 场景一：多账户成本总览

用户输入："查看整个组织的AWS成本"

```bash
# 多账户成本总览
python3 scripts/cost_pro.py summary \
  --accounts all \
  --month 2026-07 \
  --group-by account

# 输出：
# === 组织成本总览 2026年7月 ===
# 总支出: $125,000
#
# 按账户分解:
# production:  $65,000 (52%)
# staging:     $30,000 (24%)
# development: $20,000 (16%)
# shared:      $10,000 (8%)
#
# 环比: +$5,000 (+4.2%)
# 预测本月: $130,000
```

### 场景二：自动优化

用户输入："自动清理所有闲置资源"

```bash
# 自动优化（先预览）
python3 scripts/cost_pro.py auto-optimize \
  --accounts all \
  --actions "delete_idle_ebs,release_eip,archive_s3" \
  --dry-run

# 确认后执行
python3 scripts/cost_pro.py auto-optimize \
  --accounts all \
  --actions "delete_idle_ebs,release_eip,archive_s3" \
  --apply \
  --output optimization_report.pdf
```

### 场景三：RI购买建议

用户输入："分析是否应该购买预留实例"

```bash
# RI/SP建议
python3 scripts/cost_pro.py ri-recommendations \
  --accounts all \
  --lookback 60 \
  --term 1 \
  --payment "partial_upfront"

# 输出：
# === RI购买建议 ===
# 1. m5.xlarge x10 (us-east-1)
#    当前: $0.192/小时 (按需)
#    RI: $0.115/小时 (1年部分预付)
#    预付: $5,040 | 月节省: $2,136
#    推荐度: 高 (使用率88%)
#
# 总预付: $15,120
# 年节省: $76,560
# ROI: 406%
```

## 快速开始

### PRO版初始化

```bash
# 安装PRO版依赖
pip install -r requirements_pro.txt

# 配置多账户访问
cp config_pro_template.yaml config_pro.yaml
```

### 常用命令

```bash
# 多账户分析
python3 scripts/cost_pro.py summary --accounts all --group-by account
python3 scripts/cost_pro.py trend --accounts all --months 12

# 自动优化
python3 scripts/cost_pro.py auto-optimize --accounts all --dry-run
python3 scripts/cost_pro.py auto-optimize --accounts all --apply

# RI建议
python3 scripts/cost_pro.py ri-recommendations --accounts all --term 1

# 预算管理
python3 scripts/cost_pro.py budget set --account production --monthly 10000
python3 scripts/cost_pro.py budget alerts --channels "email,webhook"

# Chargeback
python3 scripts/cost_pro.py chargeback --month 2026-07 --by department
python3 scripts/cost_pro.py chargeback export --format excel --output chargeback.xlsx

# FinOps
python3 scripts/cost_pro.py finops scorecard --accounts all
python3 scripts/cost_pro.py finops report --output finops_report.pdf
```

## 配置示例

### PRO企业级配置

```yaml
pro_config:
  organization:
    master_account: "${MASTER_ACCOUNT_ID}"
    role_name: "OrganizationAccountAccessRole"
    member_accounts: "auto"       # 自动发现所有成员账户

  analysis:
    currency: "USD"
    group_by: ["account", "service", "region", "tag:Department"]
    forecast:
      method: "linear_regression"
      forecast_months: 3

  optimization:
    auto_execute:
      - delete_idle_ebs            # 删除闲置EBS
      - release_eip                # 释放未关联EIP
      - archive_old_s3             # 归档旧S3数据
      - rightsize_ec2              # EC2规格优化
    safe_mode: true                # 安全模式（需确认）
    require_approval: true         # 生产环境需审批

  reserved_instances:
    lookback_days: 60
    terms: [1, 3]                  # 1年/3年
    payment_options: ["no_upfront", "partial_upfront", "all_upfront"]
    min_utilization: 0.7           # 最低使用率阈值

  budget:
    accounts:
      production: 50000
      staging: 20000
      development: 10000
    alerts:
      thresholds: [0.5, 0.8, 0.9, 1.0]
      channels: ["email", "webhook", "slack"]
    anomaly_detection: true        # 异常支出检测

  finops:
    chargeback:
      enabled: true
      allocation: "tag:Department"
      shared_costs: "proportional"  # 共享成本按比例分摊
    scorecard:
      metrics: ["efficiency", "visibility", "optimization", "planning"]
    tags:
      required: ["Department", "Project", "Environment"]
      compliance_check: true

  storage:
    type: "postgresql"
    retention_years: 3
```

## 最佳实践

### PRO版FinOps实践

| 实践领域 | 建议做法 |
| --- | --- |
| 多账户管理 | 使用组织主账户统一管理，角色跨账户访问 |
| 自动优化 | 先dry-run预览，确认影响后再apply |
| RI采购 | 使用率>70%时考虑购买，注意预付资金占用 |
| Chargeback | 按部门标签分摊，共享成本按比例分配 |
| 预算管理 | 设置多级阈值（50%/80%/90%/100%） |

### 免费版兼容性

```text
免费版命令 → PRO版命令（增强）：
cost.py summary (单账户)  → cost_pro.py summary --accounts all
cost.py recommendations   → cost_pro.py auto-optimize --apply
基础优化建议               → +RI建议+自动执行+chargeback
```

## 常见问题

### Q1：如何管理多账户成本？

PRO版通过AWS Organizations主账户，使用OrganizationAccountAccessRole跨账户访问。自动发现所有成员账户，统一分析成本。无需为每个账户单独配置凭证。

### Q2：自动优化安全吗？

PRO版采用安全模式：先dry-run预览影响，确认后apply。生产环境需额外审批（require_approval）。所有优化操作记录审计日志，支持回滚。

### Q3：RI建议基于什么？

基于过去60天的实例使用率数据，分析按需实例的稳定使用模式。使用率>70%的实例推荐购买RI。综合考虑预付金额、节省金额和ROI。

### Q4：Chargeback如何分摊？

通过资源标签（如Department/Project）将成本归因到各部门。共享成本（如网络、监控）按使用比例分摊。生成chargeback报告用于内部结算。

### Q5：异常检测如何工作？

PRO版基于历史成本模式建立基线，当某天/某账户的支出偏离基线时触发告警。能及时发现异常增长（如配置错误导致的资源浪费）。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| boto3 | Python库 | 必需 | `pip install boto3` |
| pandas | Python库 | 必需 | `pip install pandas`（数据分析） |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |
| psycopg2 | Python库 | 可选 | `pip install psycopg2-binary`（存储） |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| AWS主账户 | `AWS_ACCESS_KEY_ID` | 必需 | 组织管理 |
| AWS Secret | `AWS_SECRET_ACCESS_KEY` | 必需 | API认证 |
| 组织角色 | 配置文件 | 推荐 | 跨账户访问 |

- 建议使用组织主账户的IAM角色
- 成员账户通过OrganizationAccountAccessRole访问

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+API执行）
- **说明**: 企业级AWS成本管理平台，支持多账户与FinOps治理
- **PRO版特性**: 多账户、自动优化、RI建议、预算告警、FinOps、chargeback、预测
- **兼容性**: 完全兼容免费版单账户分析命令
