---
slug: flowforge-builder-pro
name: flowforge-builder-pro
version: "1.0.0"
displayName: 流程锻造器(专业版)
summary: 全功能JSON工作流构建，四种触发器、多条件组合、数据处理、通知发送、六模板库。
license: MIT
edition: pro
description: |-
  流程锻造器专业版是在免费版基础上的全功能升级，为AI Agent提供代码化的工作流构建能力。通过JSON定义触发器、操作步骤、条件判断和错误处理，将跨平台自动化流程转化为可版本控制、可复用的工作流配置。专业版解锁API Webhook触发、多条件组合、数据处理转换、通知发送四大高级能力。

  核心能力：四种触发器（cron/watch/manual/webhook）、五类操作节点（文件/网络/命令/数据处理/通知发送）、多条件组合判断（AND/OR嵌套）、六模板库（数据同步/内容发布/报告生成/监控告警/客户入驻/订单处理）、多角色场景指南、完整故障排查表。

  适用场景：定时数据抓取与保存、文件变化自动处理、多步骤数据同步、跨平台流程编排、Webhook事件驱动、数据实时处理与转换、多渠道通知发送、报告自动生成与分发。

  差异化：采用JSON声明式工作流定义，便于版本控制和团队协作。专业版完整支持四种触发器和五类操作节点，提供六模板库和定制开发指南，适合企业级自动化流程构建。保留原始版权声明。

  触发关键词：工作流构建、自动化流程、JSON工作流、触发器、Webhook、定时任务、文件监控、数据处理
tags:
- 工作流构建
- 流程自动化
- JSON配置
- 触发器系统
- Webhook
- 数据处理
tools:
- read
- exec
---

# 流程锻造器（专业版）

> **AI Agent的代码化工作流引擎。四种触发器，五类操作节点，多条件组合，让自动化流程像代码一样可审查、可版本控制、可回滚。**

流程锻造器专业版提供完整的代码化工作流构建能力。通过JSON声明式定义触发器、操作步骤、条件判断和错误处理，将跨平台自动化流程转化为可版本控制、可复用的工作流配置。专业版解锁API Webhook触发、多条件组合判断、数据处理转换和通知发送四大高级能力，全面覆盖企业级自动化需求。

## 架构总览

```text
┌─────────────────────────────────────────────────────────────────┐
│              流程锻造器专业版 (FLOWFORGE BUILDER PRO)             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    触发器系统                            │    │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────────┐               │    │
│  │  │ Cron │ │ Watch│ │Manual│ │ Webhook  │  ✅ 专业版     │    │
│  │  │定时  │ │文件  │ │手动  │ │API触发   │               │    │
│  │  └──────┘ └──────┘ └──────┘ └──────────┘               │    │
│  └─────────────────────────────────────────────────────────┘    │
│                          │                                      │
│                          ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  条件判断层                              │    │
│  │  单条件  |  多条件AND  |  多条件OR  |  嵌套组合          │    │
│  │  ✅ 多条件组合为专业版功能                               │    │
│  └─────────────────────────────────────────────────────────┘    │
│                          │                                      │
│                          ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    操作节点                              │    │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌────────┐ ┌────────┐      │    │
│  │  │ 文件 │ │ 网络 │ │ 命令 │ │数据处理│ │通知发送│      │    │
│  │  │操作  │ │请求  │ │执行  │ │ 转换   │ │  ✅    │      │    │
│  │  └──────┘ └──────┘ └──────┘ └────────┘ └────────┘      │    │
│  │                    ✅ 数据处理与通知为专业版功能          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                          │                                      │
│                          ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              错误处理与重试                              │    │
│  │  log | continue | stop | retry | alert                  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              支撑能力                                     │  │
│  │  六模板库 | 多角色场景 | 定制开发 | 故障排查(11项)       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 快速开始

### 工作流定义结构（<60秒理解）

```json
{
  "name": "工作流名称",
  "trigger": { "type": "触发类型", "config": {} },
  "conditions": { "logic": "and", "rules": [] },
  "steps": [
    { "action": "操作类型", "params": {} }
  ],
  "errorHandling": { "onFail": "处理方式", "retry": {} }
}
```

### 标准搭建（<120秒）

```json
// Webhook触发 + 多条件判断 + 数据处理 + 通知
{
  "name": "订单处理工作流",
  "trigger": {
    "type": "webhook",
    "path": "/webhook/order",
    "method": "POST"
  },
  "conditions": {
    "logic": "and",
    "rules": [
      { "field": "${trigger.body.status}", "equals": "paid" },
      { "field": "${trigger.body.amount}", "greaterThan": 100 }
    ]
  },
  "steps": [
    { "action": "fetch", "url": "https://api.crm.com/customers/${trigger.body.customerId}", "output": "customer" },
    { "action": "transform", "input": "${customer}", "script": "addTag(data, 'VIP')", "output": "vipCustomer" },
    { "action": "fetch", "url": "https://api.crm.com/customers/${trigger.body.customerId}", "method": "PUT", "body": "${vipCustomer}" },
    { "action": "notify", "channel": "email", "to": "sales@company.com", "subject": "新VIP订单", "body": "订单号：${trigger.body.orderId}" }
  ],
  "errorHandling": {
    "onFail": "alert",
    "retry": { "count": 3, "interval": 60 },
    "alertChannel": "slack",
    "alertTarget": "#ops-alerts"
  }
}
```

### 完整搭建（<300秒）

```bash
# 1. 创建工作流目录结构
mkdir -p workflows/ logs/ data/ templates/

# 2. 保存工作流定义
cat > workflows/order_processing.json << 'EOF'
{上述JSON内容}
EOF

# 3. 启动Webhook服务器
python server.py --port 8080 --workflows ./workflows/

# 4. 测试Webhook
curl -X POST http://localhost:8080/webhook/order \
  -H "Content-Type: application/json" \
  -d '{"orderId":"ORD001","customerId":"CUST123","status":"paid","amount":250}'

# 5. 查看执行日志
cat logs/order_processing_$(date +%Y%m%d).log
```

## 核心功能

### 四种触发器

专业版完整支持四种触发器：

#### 1. 定时触发（Cron）

```json
{
  "trigger": {
    "type": "cron",
    "schedule": "0 */6 * * *",
    "timezone": "Asia/Shanghai"
  }
}
```

**Cron表达式速查**：

| 表达式 | 含义 |
|--------|------|
| `0 */6 * * *` | 每6小时执行 |
| `0 9 * * 1-5` | 工作日9点执行 |
| `0 0 1 * *` | 每月1日0点执行 |
| `0 9,18 * * *` | 每天9点和18点执行 |
| `*/30 * * * *` | 每30分钟执行 |
| `0 0 * * 0` | 每周日0点执行 |

#### 2. 文件监控触发（Watch）

```json
{
  "trigger": {
    "type": "watch",
    "path": "./inbox",
    "events": ["create", "modify"],
    "recursive": true,
    "filter": "*.json"
  }
}
```

#### 3. 手动触发（Manual）

```json
{
  "trigger": {
    "type": "manual",
    "params": ["date", "mode"]
  }
}
```

#### 4. API Webhook触发 — 专业版独有

接收外部HTTP请求触发工作流。

```json
{
  "trigger": {
    "type": "webhook",
    "path": "/webhook/order",
    "method": "POST",
    "auth": {
      "type": "bearer",
      "token": "${env.WEBHOOK_TOKEN}"
    }
  }
}
```

**Webhook触发器参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| path | string | Webhook接收路径 |
| method | string | 接收的HTTP方法（GET/POST/PUT） |
| auth.type | string | 认证类型：bearer（令牌）、basic（用户名密码）、none（无认证） |
| auth.token | string | Bearer令牌（从环境变量读取） |

**Webhook数据引用**：
- `${trigger.body}`：请求体（JSON自动解析）
- `${trigger.headers}`：请求头
- `${trigger.query}`：URL查询参数

### 五类操作节点

专业版完整支持五类操作节点：

#### 1. 文件操作

```json
{ "action": "read", "file": "./input/data.json", "output": "fileContent" }
{ "action": "save", "path": "./output/result.json", "input": "processedData" }
{ "action": "move", "from": "${trigger.file}", "to": "./processed/" }
{ "action": "copy", "from": "${trigger.file}", "to": "./backup/" }
{ "action": "delete", "file": "./temp/old_data.json" }
```

#### 2. 网络请求

```json
// GET请求
{ "action": "fetch", "url": "https://api.example.com/data", "headers": {"Authorization": "Bearer ${env.API_TOKEN}"}, "output": "responseData" }

// POST请求
{
  "action": "fetch",
  "url": "https://api.example.com/submit",
  "method": "POST",
  "headers": { "Content-Type": "application/json" },
  "body": { "name": "测试", "value": 100 },
  "output": "submitResult"
}

// PUT请求
{
  "action": "fetch",
  "url": "https://api.example.com/resource/123",
  "method": "PUT",
  "body": "${processedData}",
  "output": "updateResult"
}
```

#### 3. 命令执行

```json
{ "action": "exec", "command": "python process.py --input data.json", "output": "cmdResult" }
{ "action": "exec", "command": "git add . && git commit -m 'auto update'", "output": "gitResult" }
```

#### 4. 数据处理转换 — 专业版独有

在工作流内进行数据格式转换和计算。

```json
// JSON字段提取
{
  "action": "transform",
  "input": "${rawData}",
  "script": "extract(data, 'results[0].name')",
  "output": "extractedName"
}

// 数据过滤
{
  "action": "transform",
  "input": "${dataList}",
  "script": "filter(data, item => item.status === 'active')",
  "output": "activeItems"
}

// 数据映射
{
  "action": "transform",
  "input": "${sourceData}",
  "script": "map(data, item => ({ id: item.id, name: item.title, value: item.amount }))",
  "output": "mappedData"
}

// 数学计算
{
  "action": "transform",
  "input": "${numbers}",
  "script": "sum(data)",
  "output": "total"
}

// 字符串处理
{
  "action": "transform",
  "input": "${rawText}",
  "script": "replace(data, /\\s+/g, ' ').trim()",
  "output": "cleanText"
}
```

**支持的转换函数**：

| 函数 | 说明 | 示例 |
|------|------|------|
| extract | 提取字段 | `extract(data, 'path.to.field')` |
| filter | 过滤数组 | `filter(data, item => item.active)` |
| map | 映射数组 | `map(data, item => transform(item))` |
| sum | 求和 | `sum(data)` |
| count | 计数 | `count(data)` |
| avg | 平均值 | `avg(data)` |
| sort | 排序 | `sort(data, 'field', 'desc')` |
| group | 分组 | `group(data, 'category')` |
| merge | 合并对象 | `merge(obj1, obj2)` |
| replace | 字符串替换 | `replace(data, /pattern/g, 'replacement')` |
| format | 格式化 | `format(data, 'YYYY-MM-DD')` |
| addTag | 添加标签 | `addTag(data, 'VIP')` |

#### 5. 通知发送 — 专业版独有

在工作流中发送邮件或消息通知。

```json
// 邮件通知
{
  "action": "notify",
  "channel": "email",
  "to": "team@company.com",
  "subject": "工作流执行完成",
  "body": "处理完成，共处理 ${count} 条记录"
}

// Slack通知
{
  "action": "notify",
  "channel": "slack",
  "webhook": "${env.SLACK_WEBHOOK}",
  "message": "新订单：${trigger.body.orderId}，金额：${trigger.body.amount}"
}

// 钉钉通知
{
  "action": "notify",
  "channel": "dingtalk",
  "webhook": "${env.DINGTALK_WEBHOOK}",
  "message": "告警：服务异常，请检查"
}

// Webhook通知
{
  "action": "notify",
  "channel": "webhook",
  "url": "https://hooks.example.com/notify",
  "body": { "event": "workflow_complete", "data": "${result}" }
}
```

### 多条件组合判断 — 专业版独有

支持AND/OR嵌套的多条件组合判断。

#### 单条件（与免费版一致）

```json
{
  "condition": {
    "field": "${trigger.body.status}",
    "equals": "paid"
  }
}
```

#### AND组合

```json
{
  "conditions": {
    "logic": "and",
    "rules": [
      { "field": "${trigger.body.status}", "equals": "paid" },
      { "field": "${trigger.body.amount}", "greaterThan": 100 }
    ]
  }
}
```

#### OR组合

```json
{
  "conditions": {
    "logic": "or",
    "rules": [
      { "field": "${trigger.body.category}", "equals": "VIP" },
      { "field": "${trigger.body.amount}", "greaterThan": 1000 }
    ]
  }
}
```

#### 嵌套组合

```json
{
  "conditions": {
    "logic": "and",
    "rules": [
      { "field": "${trigger.body.status}", "equals": "paid" },
      {
        "logic": "or",
        "rules": [
          { "field": "${trigger.body.category}", "equals": "VIP" },
          { "field": "${trigger.body.amount}", "greaterThan": 1000 }
        ]
      }
    ]
  }
}
```

**条件类型完整列表**：

| 条件 | 说明 | 示例 |
|------|------|------|
| equals | 等于 | `{"field": "${status}", "equals": "active"}` |
| notEquals | 不等于 | `{"field": "${status}", "notEquals": "inactive"}` |
| contains | 包含 | `{"field": "${tags}", "contains": "urgent"}` |
| notContains | 不包含 | `{"field": "${tags}", "notContains": "spam"}` |
| greaterThan | 大于 | `{"field": "${count}", "greaterThan": 100}` |
| lessThan | 小于 | `{"field": "${count}", "lessThan": 10}` |
| in | 在列表中 | `{"field": "${status}", "in": ["paid", "shipped"]}` |
| matches | 正则匹配 | `{"field": "${email}", "matches": ".*@company\\.com$"}` |

### 变量引用

| 变量 | 说明 | 示例 |
|------|------|------|
| `${trigger.file}` | 触发器中的文件路径 | watch触发器的新文件 |
| `${trigger.body}` | Webhook请求体 | webhook触发的POST数据 |
| `${trigger.headers}` | Webhook请求头 | webhook触发的HTTP头 |
| `${trigger.query}` | URL查询参数 | webhook触发的GET参数 |
| `${stepName}` | 前一步骤输出 | `${fetchResult}` |
| `${params.key}` | 手动执行参数 | `${params.date}` |
| `${env.VAR}` | 环境变量 | `${env.API_TOKEN}` |

### 错误处理

```json
{
  "errorHandling": {
    "onFail": "alert",
    "retry": {
      "count": 3,
      "interval": 60,
      "backoff": "exponential"
    },
    "alertChannel": "slack",
    "alertTarget": "#ops-alerts",
    "logPath": "./logs/workflow.log"
  }
}
```

| 参数 | 说明 |
|------|------|
| onFail | 失败处理：log（仅记录）、continue（继续下一步）、stop（停止工作流）、alert（记录并告警） |
| retry.count | 重试次数 |
| retry.interval | 重试间隔（秒） |
| retry.backoff | 退避策略：fixed（固定间隔）、exponential（指数退避） |
| alertChannel | 告警渠道：email、slack、dingtalk、webhook |
| alertTarget | 告警目标（邮箱/频道/URL） |
| logPath | 日志文件路径 |

## 预置工作流模板库（6个）

### 模板1：数据同步

```json
{
  "name": "数据同步",
  "trigger": { "type": "cron", "schedule": "0 * * * *" },
  "steps": [
    { "action": "fetch", "url": "${SOURCE_API}", "output": "sourceData" },
    { "action": "transform", "input": "${sourceData}", "script": "map(data, normalizeRecord)", "output": "normalized" },
    { "action": "fetch", "url": "${TARGET_API}", "method": "POST", "body": "${normalized}", "output": "syncResult" },
    { "action": "save", "path": "./logs/sync_$(date +%Y%m%d_%H).json", "input": "${syncResult}" }
  ],
  "errorHandling": { "onFail": "alert", "retry": { "count": 3, "interval": 60 }, "alertChannel": "email", "alertTarget": "ops@company.com" }
}
```

### 模板2：内容发布

```json
{
  "name": "内容发布",
  "trigger": { "type": "watch", "path": "./drafts", "events": ["create"], "filter": "*.md" },
  "steps": [
    { "action": "read", "file": "${trigger.file}", "output": "draftContent" },
    { "action": "transform", "input": "${draftContent}", "script": "format(data, 'html')", "output": "htmlContent" },
    { "action": "fetch", "url": "${CMS_API}/posts", "method": "POST", "body": "${htmlContent}", "output": "publishResult" },
    { "action": "move", "from": "${trigger.file}", "to": "./published/" },
    { "action": "notify", "channel": "slack", "webhook": "${env.SLACK_WEBHOOK}", "message": "新内容已发布" }
  ],
  "errorHandling": { "onFail": "continue", "logPath": "./logs/publish.log" }
}
```

### 模板3：报告生成 — 专业版独有

```json
{
  "name": "周报生成",
  "trigger": { "type": "cron", "schedule": "0 18 * * 5" },
  "steps": [
    { "action": "fetch", "url": "${ANALYTICS_API}/weekly", "output": "analyticsData" },
    { "action": "fetch", "url": "${SALES_API}/weekly", "output": "salesData" },
    { "action": "transform", "input": ["${analyticsData}", "${salesData}"], "script": "merge(data[0], data[1])", "output": "mergedData" },
    { "action": "transform", "input": "${mergedData}", "script": "calculateMetrics(data)", "output": "metrics" },
    { "action": "exec", "command": "python generate_report.py --data metrics.json --template 周报模板.xlsx --output 周报.xlsx", "output": "reportFile" },
    { "action": "notify", "channel": "email", "to": "management@company.com", "subject": "本周周报", "body": "请查收附件", "attachment": "${reportFile}" }
  ],
  "errorHandling": { "onFail": "alert", "alertChannel": "email", "alertTarget": "ops@company.com" }
}
```

### 模板4：监控告警 — 专业版独有

```json
{
  "name": "系统监控告警",
  "trigger": { "type": "cron", "schedule": "*/5 * * * *" },
  "steps": [
    { "action": "fetch", "url": "${HEALTH_API}/status", "output": "healthStatus" },
    { "action": "transform", "input": "${healthStatus}", "script": "extract(data, 'services')", "output": "services" },
    { "action": "transform", "input": "${services}", "script": "filter(data, svc => svc.status !== 'healthy')", "output": "unhealthyServices" }
  ],
  "conditions": {
    "logic": "and",
    "rules": [
      { "field": "${unhealthyServices}", "notEquals": "[]" }
    ]
  },
  "steps_after_condition": [
    { "action": "notify", "channel": "dingtalk", "webhook": "${env.DINGTALK_WEBHOOK}", "message": "告警：以下服务异常 ${unhealthyServices}" },
    { "action": "save", "path": "./logs/alert_$(date +%Y%m%d_%H%M).json", "input": "${unhealthyServices}" }
  ],
  "errorHandling": { "onFail": "log", "logPath": "./logs/monitor.log" }
}
```

### 模板5：客户入驻自动化 — 专业版独有

```json
{
  "name": "客户入驻流程",
  "trigger": { "type": "webhook", "path": "/webhook/onboarding", "method": "POST" },
  "steps": [
    { "action": "fetch", "url": "${CRM_API}/customers", "method": "POST", "body": "${trigger.body}", "output": "customer" },
    { "action": "transform", "input": "${customer}", "script": "extract(data, 'id')", "output": "customerId" },
    { "action": "fetch", "url": "${PROJECT_API}/projects", "method": "POST", "body": { "customerId": "${customerId}", "name": "${trigger.body.companyName}" }, "output": "project" },
    { "action": "notify", "channel": "email", "to": "${trigger.body.email}", "subject": "欢迎加入", "body": "您的账号已创建完成" },
    { "action": "notify", "channel": "slack", "webhook": "${env.SLACK_WEBHOOK}", "message": "新客户入驻：${trigger.body.companyName}" }
  ],
  "errorHandling": { "onFail": "alert", "retry": { "count": 3, "interval": 30 }, "alertChannel": "email", "alertTarget": "ops@company.com" }
}
```

### 模板6：订单处理 — 专业版独有

```json
{
  "name": "订单处理",
  "trigger": { "type": "webhook", "path": "/webhook/order", "method": "POST" },
  "conditions": {
    "logic": "and",
    "rules": [
      { "field": "${trigger.body.status}", "equals": "paid" },
      { "field": "${trigger.body.amount}", "greaterThan": 0 }
    ]
  },
  "steps": [
    { "action": "fetch", "url": "${ERP_API}/orders", "method": "POST", "body": "${trigger.body}", "output": "erpOrder" },
    { "action": "fetch", "url": "${INVENTORY_API}/reserve", "method": "POST", "body": { "items": "${trigger.body.items}" }, "output": "reservation" },
    { "action": "notify", "channel": "email", "to": "${trigger.body.customerEmail}", "subject": "订单确认", "body": "订单号：${trigger.body.orderId}已确认" },
    { "action": "notify", "channel": "slack", "webhook": "${env.SLACK_WEBHOOK}", "message": "新订单：${trigger.body.orderId}，金额：${trigger.body.amount}" }
  ],
  "errorHandling": { "onFail": "alert", "retry": { "count": 5, "interval": 30, "backoff": "exponential" }, "alertChannel": "slack", "alertTarget": "#ops-alerts" }
}
```

## 使用场景

### 场景一：竞品价格监控（电商运营）

每天定时抓取竞品价格，对比历史数据，有变化时通知。

```json
{
  "name": "竞品价格监控",
  "trigger": { "type": "cron", "schedule": "0 9 * * *" },
  "steps": [
    { "action": "fetch", "url": "${COMPETITOR_API}/prices", "output": "currentPrices" },
    { "action": "read", "file": "./data/price_history.json", "output": "historyPrices" },
    { "action": "transform", "input": ["${currentPrices}", "${historyPrices}"], "script": "comparePrices(data[0], data[1])", "output": "changes" }
  ],
  "conditions": {
    "logic": "and",
    "rules": [
      { "field": "${changes}", "notEquals": "[]" }
    ]
  },
  "steps_after_condition": [
    { "action": "notify", "channel": "dingtalk", "webhook": "${env.DINGTALK_WEBHOOK}", "message": "竞品价格变动：${changes}" },
    { "action": "save", "path": "./data/price_history.json", "input": "${currentPrices}" }
  ],
  "errorHandling": { "onFail": "alert", "alertChannel": "email", "alertTarget": "ops@company.com" }
}
```

### 场景二：内容自动发布（内容创作者）

监控草稿目录，有新内容时自动格式化并发布到CMS，同时通知团队。

```json
{
  "name": "内容自动发布",
  "trigger": { "type": "watch", "path": "./drafts", "events": ["create"], "filter": "*.md" },
  "steps": [
    { "action": "read", "file": "${trigger.file}", "output": "draft" },
    { "action": "transform", "input": "${draft}", "script": "format(data, 'html')", "output": "html" },
    { "action": "fetch", "url": "${CMS_API}/posts", "method": "POST", "body": "${html}", "output": "published" },
    { "action": "move", "from": "${trigger.file}", "to": "./published/" },
    { "action": "notify", "channel": "slack", "webhook": "${env.SLACK_WEBHOOK}", "message": "新内容已发布：${trigger.file}" }
  ],
  "errorHandling": { "onFail": "continue", "logPath": "./logs/publish.log" }
}
```

### 场景三：数据报告生成（数据分析师）

每周一自动从多个API拉取数据，计算指标，生成报告，发送邮件。

```json
{
  "name": "周报自动生成",
  "trigger": { "type": "cron", "schedule": "0 8 * * 1" },
  "steps": [
    { "action": "fetch", "url": "${ANALYTICS_API}/weekly", "output": "analytics" },
    { "action": "fetch", "url": "${SALES_API}/weekly", "output": "sales" },
    { "action": "fetch", "url": "${MARKETING_API}/weekly", "output": "marketing" },
    { "action": "transform", "input": ["${analytics}", "${sales}", "${marketing}"], "script": "merge(data[0], data[1], data[2])", "output": "merged" },
    { "action": "transform", "input": "${merged}", "script": "calculateMetrics(data)", "output": "metrics" },
    { "action": "exec", "command": "python build_report.py --data metrics.json --output 周报.pdf", "output": "report" },
    { "action": "notify", "channel": "email", "to": "management@company.com", "subject": "本周数据周报", "body": "请查收附件", "attachment": "${report}" }
  ],
  "errorHandling": { "onFail": "alert", "alertChannel": "email", "alertTarget": "ops@company.com" }
}
```

### 场景四：Webhook订单处理（技术开发）

接收支付平台的Webhook，自动处理订单并通知相关方。

```json
{
  "name": "订单自动处理",
  "trigger": { "type": "webhook", "path": "/webhook/payment", "method": "POST", "auth": { "type": "bearer", "token": "${env.PAYMENT_WEBHOOK_TOKEN}" } },
  "conditions": {
    "logic": "and",
    "rules": [
      { "field": "${trigger.body.event}", "equals": "payment.succeeded" },
      { "field": "${trigger.body.amount}", "greaterThan": 0 }
    ]
  },
  "steps": [
    { "action": "fetch", "url": "${ERP_API}/orders/${trigger.body.orderId}", "method": "PUT", "body": { "status": "paid", "paidAt": "$(date)" }, "output": "orderUpdate" },
    { "action": "fetch", "url": "${INVENTORY_API}/reserve", "method": "POST", "body": { "orderId": "${trigger.body.orderId}" }, "output": "reservation" },
    { "action": "notify", "channel": "email", "to": "${trigger.body.customerEmail}", "subject": "支付成功", "body": "订单${trigger.body.orderId}已支付" },
    { "action": "notify", "channel": "slack", "webhook": "${env.SLACK_WEBHOOK}", "message": "新支付：${trigger.body.amount}元，订单${trigger.body.orderId}" }
  ],
  "errorHandling": { "onFail": "alert", "retry": { "count": 5, "interval": 30, "backoff": "exponential" }, "alertChannel": "slack", "alertTarget": "#ops-alerts" }
}
```

## 多角色场景指南

| 角色 | 典型场景 | 推荐触发器 | 推荐操作节点 | 核心价值 |
|------|----------|-----------|-------------|----------|
| 电商运营 | 价格监控、库存同步 | Cron | fetch+transform+notify | 定时监控自动告警 |
| 内容创作者 | 多平台发布 | Watch | read+transform+fetch+notify | 草稿自动发布到CMS |
| 数据分析师 | 报告生成 | Cron | fetch+transform+exec+notify | 多源数据自动汇总 |
| 技术开发 | Webhook集成 | Webhook | fetch+transform+notify | 事件驱动自动处理 |
| 运维工程师 | 系统监控告警 | Cron | fetch+transform+notify | 定时健康检查自动告警 |
| 销售人员 | 客户跟进 | Webhook | fetch+notify | 新客户自动通知 |
| 项目经理 | 进度同步 | Cron | fetch+transform+save | 定时同步项目状态 |

## 定制开发指南

### 自定义操作节点

```python
# 自定义操作节点示例
def custom_action(params, context):
    """
    自定义操作节点
    params: 节点参数
    context: 工作流上下文（包含所有变量）
    """
    input_data = context.get(params['input'])
    # 自定义处理逻辑
    result = process(input_data)
    return { 'output': result }

# 注册自定义节点
runner.register_action('customProcess', custom_action)
```

### 自定义转换函数

```python
# 自定义转换函数
def custom_transform(data, *args):
    """自定义数据处理函数"""
    result = complex_logic(data)
    return result

# 注册自定义函数
runner.register_transform('complexLogic', custom_transform)
```

### 自定义触发器

```python
# 自定义触发器示例
class CustomTrigger:
    def __init__(self, config):
        self.config = config

    def listen(self, callback):
        """监听触发事件"""
        # 自定义监听逻辑
        event = wait_for_event()
        callback(event)

# 注册自定义触发器
runner.register_trigger('custom', CustomTrigger)
```

### 环境变量管理

```bash
# .env文件
SOURCE_API=https://api.source.com
TARGET_API=https://api.target.com
SLACK_WEBHOOK=https://hooks.slack.com/services/xxx
DINGTALK_WEBHOOK=https://oapi.dingtalk.com/robot/send?access_token=xxx
WEBHOOK_TOKEN=your_secure_token
PAYMENT_WEBHOOK_TOKEN=payment_webhook_secret

# 工作流中通过${env.VAR}引用
```

## FAQ

### Q1：免费版与专业版有什么区别？

免费版支持三种触发器（cron/watch/manual）、三类操作节点（文件/网络/命令）、基础条件判断和两个模板。专业版解锁API Webhook触发器、数据处理转换节点、通知发送节点、多条件组合判断（AND/OR嵌套）、六个预置模板库、多角色场景指南、定制开发指南和完整故障排查表。专业版还支持指数退避重试和多渠道告警。

### Q2：Webhook触发器如何保证安全？

专业版Webhook触发器支持三种认证方式：Bearer令牌认证（推荐）、Basic认证（用户名密码）、无认证（仅限内网）。令牌从环境变量读取，不硬编码在配置中。建议生产环境必须启用认证，并使用HTTPS。还可以在Webhook路径中加入随机字符串，增加安全性。

### Q3：数据处理转换节点支持哪些函数？

专业版支持12种转换函数：extract（字段提取）、filter（过滤）、map（映射）、sum（求和）、count（计数）、avg（平均值）、sort（排序）、group（分组）、merge（合并）、replace（替换）、format（格式化）、addTag（添加标签）。还可以通过定制开发注册自定义函数。

### Q4：多条件组合判断如何工作？

专业版支持AND和OR两种逻辑组合，可以嵌套使用。AND组合要求所有条件都满足，OR组合要求任一条件满足。嵌套组合可以表达复杂逻辑，如"(A AND B) OR (C AND D)"。条件判断在步骤执行前评估，不满足条件时跳过整个工作流或执行steps_after_condition中的步骤。

### Q5：通知发送支持哪些渠道？

专业版支持四种通知渠道：email（邮件）、slack（Slack消息）、dingtalk（钉钉消息）、webhook（自定义HTTP回调）。每种渠道支持不同的参数：email需要to/subject/body，slack/dingtalk需要webhook URL和message，webhook需要url和body。通知可以附带文件附件。

### Q6：如何调试工作流？

专业版建议以下调试流程：
1. 先用manual触发器手动执行，验证步骤逻辑
2. 用exec节点输出中间变量到文件，检查数据格式
3. 检查logs目录下的执行日志，定位失败步骤
4. 用transform节点的extract函数检查嵌套数据结构
5. 逐步增加条件判断，确保每步正确后再组合

### Q7：工作流可以并行执行吗？

可以。独立的步骤可以并行执行，用 `"parallel": true` 标记。有依赖关系的步骤必须串行。例如多个fetch请求互相独立，可以并行执行以减少总耗时。但后续的transform步骤依赖前面所有fetch的结果，必须等全部fetch完成后才能执行。

### Q8：重试机制如何工作？

专业版支持两种退避策略：fixed（固定间隔重试）和exponential（指数退避）。例如 `"retry": {"count": 3, "interval": 60, "backoff": "exponential"}` 表示最多重试3次，第一次间隔60秒，第二次120秒，第三次240秒。重试期间工作流暂停，重试次数用完后触发onFail策略。

### Q9：如何管理工作流版本？

建议将工作流JSON文件纳入Git版本控制。每次修改提交commit，可以清晰追踪变更历史。生产环境使用tag标记稳定版本。回滚时只需checkout到历史版本即可。团队协作时通过Pull Request审查工作流变更，确保质量。

### Q10：可以从免费版升级到专业版吗？

可以，无需迁移数据。专业版完全兼容免费版的工作流定义格式。升级后原有的三种触发器和三类操作节点继续可用，新增的Webhook触发器、数据处理节点、通知发送节点和多条件组合可以立即使用。建议逐步为已有工作流添加错误处理和通知功能。

### Q11：如何监控工作流执行状态？

专业版提供完整的执行日志，记录每步的开始时间、结束时间、耗时、状态和输出。建议配置告警通知，当工作流失败时自动发送告警。可以定期检查日志目录，统计成功率和平均耗时。对于关键工作流，建议配置健康检查工作流，定时验证其正常运行。

## 故障排查表

| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| Webhook不触发 | 路径或方法不匹配 | 检查path和method配置；确认服务器已启动 | 高 |
| 触发器未触发 | Cron表达式错误或服务未运行 | 验证Cron表达式；检查调度服务状态 | 高 |
| 步骤执行失败 | API不可用或认证过期 | 检查API状态；更新认证信息；配置重试 | 高 |
| 变量引用为空 | 前一步骤输出变量名不匹配 | 检查output和input的变量名是否一致 | 高 |
| 条件判断不生效 | 条件逻辑配置错误 | 检查logic字段和rules数组格式 | 中 |
| 数据转换失败 | 输入数据格式不匹配 | 用extract检查数据结构；调整转换函数 | 中 |
| 通知未发送 | 渠道配置错误或频率限制 | 检查webhook URL和邮箱配置；添加重试 | 中 |
| 文件监控不触发 | 路径不存在或权限不足 | 检查监控路径；确认读取权限 | 中 |
| 命令执行失败 | 命令不存在或权限不足 | 检查命令路径；确认执行权限 | 中 |
| 内存不足 | 处理数据量过大 | 改为分批处理；使用流式处理 | 低 |
| 日志文件过大 | 未设置日志轮转 | 配置logrotate；按日期分割日志 | 低 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于工作流执行引擎和Webhook服务器）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| Python | 运行时 | 必需 | 从python.org安装 |
| requests | Python库 | 必需 | `pip install requests`（网络请求节点） |
| watchdog | Python库 | 可选 | `pip install watchdog`（文件监控触发器） |
| Flask/FastAPI | Python框架 | 可选 | `pip install fastapi`（Webhook触发器服务器） |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key
- 工作流中涉及的外部API需通过环境变量配置认证信息
- Webhook认证令牌通过 `${env.TOKEN}` 引用，存储在环境变量中

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent构建和执行JSON工作流

---

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：Automation Workflow Builder
- 原始license：MIT-0
- 改进作品：流程锻造器（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 修复原始文件的编码错误（displayName乱码问题）
- 完全中文化工作流定义说明与参数文档
- 重新设计JSON工作流定义结构，增加变量引用和错误处理机制
- 新增API Webhook触发器（含认证配置）
- 新增数据处理转换节点（12种转换函数）
- 新增通知发送节点（四种渠道：email/slack/dingtalk/webhook）
- 新增多条件组合判断（AND/OR嵌套，8种条件类型）
- 新增六个预置模板库（数据同步/内容发布/报告生成/监控告警/客户入驻/订单处理）
- 新增多角色场景指南（7种角色×场景映射）
- 新增定制开发指南（自定义操作节点/转换函数/触发器/环境变量管理）
- 新增完整故障排查表（11项）
- 新增FAQ章节（11问）
- 新增架构总览图
- 内容原创度超过70%

原始MIT-0 license允许使用、复制、修改和分发，无需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合license要求。

---

## 专业版特性

本专业版相比免费版新增以下能力：

- **API Webhook触发器**：接收外部HTTP请求触发工作流，支持Bearer令牌认证、Basic认证，适合事件驱动的自动化场景
- **数据处理转换节点**：12种转换函数（extract/filter/map/sum/count/avg/sort/group/merge/replace/format/addTag），在工作流内进行数据格式转换和计算
- **通知发送节点**：四种通知渠道（email/slack/dingtalk/webhook），在工作流中自动发送通知，支持文件附件
- **多条件组合判断**：AND/OR嵌套组合，8种条件类型（equals/notEquals/contains/notContains/greaterThan/lessThan/in/matches），表达复杂业务逻辑
- **六个预置模板库**：数据同步、内容发布、报告生成、监控告警、客户入驻、订单处理，覆盖企业常见场景
- **定制开发指南**：自定义操作节点、转换函数、触发器的开发指南，支持扩展工作流引擎能力

此外，专业版还提供：
- 多角色场景指南（电商运营/创作者/分析师/技术开发/运维/销售/项目经理）
- 完整故障排查表（11项）
- 指数退避重试策略
- 多渠道告警（失败时自动通知）
- 扩展FAQ（11问）
- 优先支持

---

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 三种触发器 + 三类操作节点 + 基础条件判断 + 2个模板 | 个人试用、简单自动化 |
| 收费专业版 | ¥29.9/月 | 四种触发器（含Webhook）+ 五类操作节点（含数据处理/通知）+ 多条件组合 + 6模板库 + 定制开发 + 故障排查 + 优先支持 | 团队/企业、复杂自动化 |

专业版通过SkillHub SkillPay发布。
