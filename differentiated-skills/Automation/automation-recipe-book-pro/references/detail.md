# 详细参考 - automation-recipe-book-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
actions:
  - type: condition
    if: "score > 90"
    then:
      - type: send
        message: "优秀"
    elif: "score > 60"
    then:
      - type: send
        message: "及格"
    else:
      - type: send
        message: "不及格"

actions:
  - type: parallel
    branches:
      - type: fetch
        url: "api1"
      - type: fetch
        url: "api2"
      - type: fetch
        url: "api3"
    wait: all  # all | any | first_n(2)
on_failure:
  retry: 3
  backoff: exponential
  on_max_retry: escalate
  notify: admin

actions:
  - type: call_recipe
    name: data-backup
    params:
      source: ~/workspace/data
```

## 代码示例 (yaml)

```yaml
name: approval-flow
description: 多级审批自动流转与通知
trigger:
  type: webhook
  path: /approval/request
actions:
  - type: classify
    categories: ["小额", "中额", "大额"]
  - type: condition
    if: "amount < 1000"
    then:
      - type: send
        to: direct_manager
        message: "小额审批请求：{{title}}"
    elif: "amount < 10000"
    then:
      - type: send
        to: direct_manager
      - type: send
        to: department_head
        message: "中额审批请求：{{title}}"
    else:
      - type: send
        to: direct_manager
      - type: send
        to: department_head
      - type: send
        to: vp
        message: "大额审批请求：{{title}}"
on_failure:
  retry: 3
  notify: admin
```

## 代码示例 (yaml)

```yaml
name: etl-pipeline
trigger:
  type: schedule
  cron: "0 1 * * *"
actions:
  - type: parallel
    branches:
      - type: extract
        source: mysql
      - type: extract
        source: mongodb
    wait: all
  - type: transform
    script: clean_and_dedupe.py
  - type: load
    target: warehouse
  - type: verify
    checks: ["row_count", "null_ratio", "uniqueness"]
  - type: condition
    if: "verify_passed"
    then:
      - type: send
        to: ops
        message: "ETL成功"
    else:
      - type: send
        to: ops
        message: "ETL校验失败，请检查"
on_failure:
  retry: 2
  backoff: exponential
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│           自动化配方手册专业版 (AUTOMATION RECIPE BOOK PRO)        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │  25+配方库    │  │  配方生成器   │  │  高级模式     │           │
│  │  Recipe Lib  │  │  Generator   │  │  Advanced    │           │
│  │  ✅ 专业版    │  │  ✅ 专业版    │  │  ✅ 专业版    │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  企业模板     │  ← 审批流/SLA/合规              │
│                  │  Enterprise  │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  调试工具包   │  ← 可视化/追踪/分析             │
│                  │  Debug Kit   │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  版本管理     │  ← 版本控制/回滚/分享           │
│                  │  Versioning  │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (json)

```json
// ~/workspace/automations/config.json
{
  "edition": "pro",
  "generator": {
    "enabled": true,
    "ai_model": "gpt-4o",
    "validation": true
  },
  "advanced": {
    "parallel_execution": true,
    "condition_branch": true,
    "error_handling": true,
    "retry_max": 3
  },
  "enterprise": {
    "approval_flow": true,
    "sla_monitoring": true,
    "compliance_check": true
  },
  "debug": {
    "visualization": true,
    "execution_trace": true,
    "performance_analysis": true
  },
  "versioning": {
    "enabled": true,
    "max_versions": 20,
    "auto_rollback_on_failure": true
  }
}
```

## 代码示例 (text)

```text
用户："帮我生成一个配方：监控竞品网站价格变化，降价超过10%就通知我，同时记录到表格"

Agent："正在生成配方...
  分析需求：
  - 触发：定时（监控需要周期性）
  - 动作1：抓取竞品价格
  - 动作2：计算降幅
  - 动作3：条件判断（降幅>10%）
  - 动作4：通知 + 记录

  已生成配方：
  trigger: schedule (每6小时)
  actions:
    1. fetch 竞品URL
    2. extract 价格
    3. calculate 降幅 = (历史价格 - 当前价格) / 历史价格
    4. condition: 降幅 > 10%
    5. send notification + append to spreadsheet

  配方已验证（语法正确，逻辑合理）
  保存至 ~/workspace/automations/recipes/competitor-price-alert.yaml"
```

## 代码示例 (yaml)

```yaml
name: compliance-check
description: 定期合规检查与报告
trigger:
  type: schedule
  cron: "0 9 * * 1"
actions:
  - type: scan
    targets: ["codebase", "configurations", "access_logs"]
  - type: check_compliance
    standards: ["GDPR", "SOC2", "ISO27001"]
  - type: generate_report
    format: pdf
  - type: send
    to: compliance_team
    attach: report
  - type: condition
    if: "violations > 0"
    then:
      - type: create_ticket
        priority: high
        assignee: security_team
```

## 代码示例 (yaml)

```yaml
name: sla-monitor
description: 监控任务SLA达标情况
trigger:
  type: schedule
  cron: "0 * * * *"
actions:
  - type: analyze_sla
    metric: response_time
    threshold: "2h"
  - type: condition
    if: "sla_breached"
    then:
      - type: send
        to: dingtalk
        message: "SLA违规：{{task}} 响应超时"
      - type: escalate
        to: manager
on_failure:
  retry: 1
  notify: ops
```

### 功能一：25+配方库（6大类别）
| 类别 | 配方数 | 典型配方 |
|------|--------|----------|
| 效率工具 | 5 | 每日新闻摘要、智能排程、待办提醒、会议纪要、邮件分类 |
| 监控告警 | 5 | 价格监控、网站可用性、社交媒体舆情、日志告警、SSL证书过期 |
| 内容发布 | 4 | 多平台发布、内容生成、SEO优化、社媒排期 |
| 数据处理 | 4 | 数据备份、ETL流水线、数据清洗、报表生成 |
| 团队协作 | 4 | 会议提醒、审批通知、任务分配、周报自动生成 |
| 企业流程 | 3+ | 审批流自动化、SLA监控、合规检查 |

**专业版新增配方示例**：

```yaml
name: approval-flow
description: 多级审批自动流转与通知
trigger:
  type: webhook
  path: /approval/request
actions:
  - type: classify
    categories: ["小额", "中额", "大额"]
  - type: condition
    if: "amount < 1000"
    then:
      - type: send
        to: direct_manager
        message: "小额审批请求：{{title}}"
    elif: "amount < 10000"
    then:
      - type: send
        to: direct_manager
      - type: send
        to: department_head
        message: "中额审批请求：{{title}}"
    else:
      - type: send
        to: direct_manager
      - type: send
        to: department_head
      - type: send
        to: vp
        message: "大额审批请求：{{title}}"
on_failure:
  retry: 3
  notify: admin
```

```yaml
name: sla-monitor
description: 监控任务SLA达标情况
trigger:
  type: schedule
  cron: "0 * * * *"
actions:
  - type: analyze_sla
    metric: response_time
    threshold: "2h"
  - type: condition
    if: "sla_breached"
    then:
      - type: send
        to: dingtalk
        message: "SLA违规：{{task}} 响应超时"
      - type: escalate
        to: manager
on_failure:
  retry: 1
  notify: ops
```



