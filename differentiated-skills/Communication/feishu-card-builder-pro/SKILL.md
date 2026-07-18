---
slug: feishu-card-builder-pro
name: feishu-card-builder-pro
version: "1.0.0"
displayName: 飞书卡片专业版
summary: 企业级飞书交互卡片与批量推送，支持模板与高级组件
license: MIT
edition: pro
description: |-
  飞书卡片专业版面向企业用户与高效能个人用户，在免费版卡片消息发送能力之上扩展
  批量推送、卡片模板系统、高级交互组件、数据动态绑定、卡片版本管理与发送分析等
  企业级特性。

  核心能力:
  - 批量卡片推送（多用户/多群组同时发送）
  - 卡片模板系统（内置与自定义模板，变量插值）
  - 高级交互组件（表单、选择器、多按钮、分栏布局）
  - 数据动态绑定（JSON 数据源自动填充）
  - 卡片版本管理与回滚
  - 发送统计与阅读追踪
  - 定时推送与条件触发
  - 优先技术支持与 SLA 保障

  适用场景:
  - 企业批量通知与公告推送
  - 数据报表卡片自动生成与推送
  - 审批流程卡片交互
  - 营销活动卡片群发
  - 多团队统一消息管理

  差异化: 专业版在免费版全部能力基础上向下兼容，额外提供批量推送引擎、模板系统、
  高级交互组件与发送分析，面向企业级飞书卡片场景深度优化。

  触发关键词: 飞书卡片, 批量推送, 卡片模板, 交互组件, 数据绑定, 卡片版本, 阅读追踪, 企业通知, 飞书群发
tags:
- 沟通协作
- 飞书
- 卡片消息
- 企业效率
- 批量操作
tools:
- read
- exec
---

# 飞书卡片专业版

**版本**: 1.0.0
**适用对象**: 企业用户、运营与营销人员、团队管理者
**核心定位**: 企业级飞书交互卡片构建与批量推送平台
**兼容性**: 完全兼容免费版（feishu-card-builder-free）全部命令与配置，可直接升级

---

## 概述

飞书卡片专业版是一款面向企业级场景的飞书卡片深度构建与推送工具。在免费版提供的卡片消息发送、Markdown 渲染、按钮交互与图片嵌入能力之上，专业版引入批量推送引擎、卡片模板系统、高级交互组件、数据动态绑定、卡片版本管理与发送分析等高级特性，满足企业在批量通知、数据报表、审批交互与营销活动等复杂场景下的需求。

专业版向下完全兼容免费版，现有 `send.js` 命令与配置无需修改即可平滑升级。新增的企业级功能通过扩展命令实现，支持模板化批量推送与交互组件构建。

---

## 核心能力

### 批量推送引擎

- **多目标发送**: 一次性向多个用户与群组推送
- **收件人列表**: 支持 CSV/JSON 收件人列表
- **变量替换**: 每个目标收到个性化内容
- **速率控制**: 可配置发送速率与并发
- **失败重试**: 自动重试失败目标

### 卡片模板系统

- **内置模板**: 通知、报告、审批、邀请、告警等企业常用模板
- **自定义模板**: 创建、编辑、删除自定义模板
- **变量插值**: 支持 `{{variable}}` 语法
- **条件渲染**: 支持条件判断与循环
- **模板预览**: 渲染效果实时预览
- **版本管理**: 模板版本控制与回滚

### 高级交互组件

- **表单组件**: 输入框、文本域、选择器
- **多按钮组**: 多个操作按钮排列
- **分栏布局**: 多列内容布局
- **分隔线**: 内容分隔
- **备注组件**: 折叠展开内容
- **数据表格**: 结构化数据展示

### 数据动态绑定

- **JSON 数据源**: 从 JSON 文件自动填充卡片内容
- **API 数据源**: 从外部 API 获取数据填充
- **数据映射**: 字段映射与转换
- **条件显示**: 根据数据动态显示/隐藏组件

### 发送分析

- **送达统计**: 成功/失败/已读统计
- **阅读追踪**: 卡片打开率追踪
- **按钮点击**: 按钮点击统计
- **趋势分析**: 发送量趋势图表
- **导出报告**: CSV/JSON 格式导出

### 定时与触发

- **定时推送**: 指定时间或周期性发送
- **条件触发**: 满足条件自动发送
- **任务队列**: 管理待发送任务
- **状态监控**: 实时查看任务状态

---

## 使用场景

### 场景一：批量推送个性化通知

HR 部门需要向500名员工发送包含个人信息的工资条通知卡片。

**准备收件人列表** `employees.csv`:

```csv
open_id,name,department,salary_month,amount
ou_001,张三,技术部,2026年7月,¥15000
ou_002,李四,市场部,2026年7月,¥12000
ou_003,王五,财务部,2026年7月,¥13000
```

**创建卡片模板** `templates/salary_card.json`:

```json
{
  "header": {
    "title": "工资条通知 - {{salary_month}}",
    "color": "blue"
  },
  "elements": [
    {
      "type": "div",
      "text": "尊敬的 **{{name}}**（{{department}}）："
    },
    {
      "type": "div",
      "text": "您本月工资为 **{{amount}}**，请登录系统查看详情。"
    },
    {
      "type": "action",
      "actions": [
        {
          "type": "button",
          "text": "查看详情",
          "url": "https://hr.company.com/salary/{{open_id}}"
        }
      ]
    }
  ]
}
```

**执行批量推送**:

```bash
# 试运行（预览不实际发送）
node skills/feishu-card-builder/batch-send.js \
  --recipients employees.csv \
  --template templates/salary_card.json \
  --rate-limit 20 \
  --dry-run

# 正式发送
node skills/feishu-card-builder/batch-send.js \
  --recipients employees.csv \
  --template templates/salary_card.json \
  --rate-limit 20 \
  --log batch_send.log
```

输出示例：

```text
📋 批量推送任务
   收件人: 500
   模板: templates/salary_card.json
   速率: 20 条/分钟

[1/500] ✅ ou_001 - 张三 - 技术部
[2/500] ✅ ou_002 - 李四 - 市场部
...
📊 推送完成: 498 成功, 2 失败
   发送报告: batch_send_report.json
```

### 场景二：数据报表卡片自动生成

运维团队需要每天自动生成系统监控报表卡片并推送到管理群。

```bash
# 创建定时任务
node skills/feishu-card-builder/schedule.js create \
  --name "daily-monitor-report" \
  --cron "0 9 * * 1-5" \
  --target "oc_management_group" \
  --template templates/monitor_report.json \
  --data-source "fetch_metrics.py" \
  --timezone "Asia/Shanghai"

# 查看定时任务
node skills/feishu-card-builder/schedule.js list

# 查看任务历史
node skills/feishu-card-builder/schedule.js history --name "daily-monitor-report"
```

### 场景三：交互式审批卡片

发送包含审批按钮的交互卡片，支持批准/驳回操作。

```bash
# 发送交互式审批卡片
node skills/feishu-card-builder/interactive-send.js \
  --target "ou_manager" \
  --template templates/approval.json \
  --data '{"applicant":"张三","amount":"¥5000","purpose":"差旅报销"}' \
  --callback-url "https://api.company.com/approval/callback"
```

审批卡片模板 `templates/approval.json`:

```json
{
  "header": {
    "title": "审批申请",
    "color": "orange"
  },
  "elements": [
    {"type": "div", "text": "申请人: **{{applicant}}**"},
    {"type": "div", "text": "金额: **{{amount}}**"},
    {"type": "div", "text": "事由: {{purpose}}"},
    {
      "type": "action",
      "actions": [
        {"type": "button", "text": "批准", "value": "approve", "type": "primary"},
        {"type": "button", "text": "驳回", "value": "reject", "type": "danger"}
      ]
    }
  ]
}
```

---

## 快速开始

### 从免费版升级

专业版完全兼容免费版，现有命令无需修改：

```bash
# 免费版命令依然有效
node skills/feishu-card-builder/send.js --target "ou_xxx" --text "Hello"
node skills/feishu-card-builder/send_safe.js --target "ou_xxx" --text "内容" --title "通知"

# 专业版新增命令
node skills/feishu-card-builder/batch-send.js --recipients list.csv --template tpl.json
node skills/feishu-card-builder/interactive-send.js --target "ou_xxx" --template tpl.json
```

### 配置模板系统

```json
{
  "templates": {
    "dir": "templates/",
    "builtins": ["notification", "report", "approval", "alert"],
    "version_control": true,
    "max_versions": 10
  }
}
```

### 配置发送分析

```json
{
  "analytics": {
    "enabled": true,
    "tracking": {
      "delivery": true,
      "read_receipt": true,
      "button_click": true
    },
    "log_file": "~/.config/feishu-card-builder/analytics.log",
    "retention_days": 90
  }
}
```

---

## 配置示例

### 批量推送配置

```json
{
  "batch": {
    "rate_limit": 20,
    "max_recipients": 2000,
    "retry_count": 3,
    "retry_delay": 30,
    "concurrency": 5,
    "on_failure": "log",
    "failure_log": "~/.config/feishu-card-builder/batch_failures.log"
  }
}
```

### 定时任务配置

```json
{
  "schedules": [
    {
      "name": "weekly-report",
      "cron": "0 10 * * 1",
      "timezone": "Asia/Shanghai",
      "target": "oc_team_group",
      "template": "templates/weekly_report.json",
      "data_source": "generate_report.py"
    }
  ]
}
```

### 交互回调配置

```json
{
  "interactive": {
    "callback_url": "https://api.company.com/feishu/callback",
    "callback_secret": "your_callback_secret",
    "timeout": 30,
    "retry": 3
  }
}
```

---

## 最佳实践

### 批量推送安全

```bash
# 始终先试运行
node skills/feishu-card-builder/batch-send.js \
  --recipients list.csv --template tpl.json --dry-run

# 控制速率
node skills/feishu-card-builder/batch-send.js \
  --recipients list.csv --template tpl.json --rate-limit 20

# 失败重试与日志
node skills/feishu-card-builder/batch-send.js \
  --recipients list.csv --template tpl.json \
  --retry 3 --log batch.log
```

### 模板管理

```bash
# 创建模板
node skills/feishu-card-builder/template.js create --name "通知" --file templates/notice.json

# 预览模板
node skills/feishu-card-builder/template.js preview --name "通知" --data sample.json

# 版本管理
node skills/feishu-card-builder/template.js versions --name "通知"
node skills/feishu-card-builder/template.js rollback --name "通知" --version 2
```

### 交互卡片设计

- 按钮数量适中（建议不超过3个）
- 操作按钮颜色区分（primary/danger）
- 回调接口确保幂等性
- 超时设置合理（建议30秒）

### 发送分析

```bash
# 查看发送统计
node skills/feishu-card-builder/analytics.js stats --since "2026-07-01"

# 查看阅读追踪
node skills/feishu-card-builder/analytics.js tracking --card-id "card_xxx"

# 导出报告
node skills/feishu-card-builder/analytics.js export --month 2026-07 --format csv
```

---

## 免费版与专业版对比

| 能力 | 免费版 | 专业版 |
|:-----|:------:|:------:|
| 基础卡片发送 | ✅ | ✅ |
| Markdown 渲染 | ✅ | ✅ |
| 彩色头部 | ✅ | ✅ |
| 底部按钮 | ✅ | ✅ |
| 图片嵌入 | ✅ | ✅ |
| 安全发送 | ✅ | ✅ |
| 人设消息 | ✅ | ✅ |
| 批量推送 | ❌ | ✅（变量替换） |
| 卡片模板 | ❌ | ✅（模板系统） |
| 高级交互组件 | ❌ | ✅（表单/选择器） |
| 数据动态绑定 | ❌ | ✅（JSON/API） |
| 卡片版本管理 | ❌ | ✅（回滚） |
| 发送分析 | ❌ | ✅（阅读追踪） |
| 定时推送 | ❌ | ✅（cron） |
| 技术支持 | 社区支持 | 优先支持 |

---

## 常见问题

### 问题1：批量推送触发频率限制

**解决**: 降低发送速率，飞书 API 有频率限制：

```bash
node skills/feishu-card-builder/batch-send.js \
  --recipients list.csv --template tpl.json --rate-limit 10
```

### 问题2：模板变量未替换

**解决**: 确保变量名与数据源字段一致：

```bash
# 验证模板
node skills/feishu-card-builder/template.js validate --name "通知" --data sample.json
```

### 问题3：交互回调无响应

**解决**: 检查回调 URL 与密钥配置：

```bash
# 测试回调
node skills/feishu-card-builder/interactive.js test-callback

# 查看回调日志
node skills/feishu-card-builder/interactive.js callback-log
```

### 问题4：定时任务未执行

**解决**: 检查 cron 表达式与时区：

```bash
node skills/feishu-card-builder/schedule.js validate --cron "0 9 * * 1-5"
node skills/feishu-card-builder/schedule.js status --name "daily-report"
```

### 问题5：卡片内容超长

**解决**: 飞书卡片有内容长度限制，超长内容建议拆分或使用折叠组件：

```json
{
  "type": "note",
  "elements": [
    {"type": "div", "text": "折叠的详细内容..."}
  ]
}
```

---

## 命令参考速查

| 命令 | 功能 | 专业版独有 |
|:-----|:-----|:----------:|
| `send.js` | 发送卡片 | - |
| `send_safe.js` | 安全发送 | - |
| `send_persona.js` | 人设消息 | - |
| `batch-send.js` | 批量推送 | ✅ |
| `interactive-send.js` | 交互卡片 | ✅ |
| `template.js` | 模板管理 | ✅ |
| `schedule.js` | 定时任务 | ✅ |
| `analytics.js` | 发送分析 | ✅ |

---

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 16 及以上
- **网络环境**: 需可访问飞书开放平台 API
- **磁盘空间**: 模板与日志建议预留 500MB 以上

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | 官方网站下载安装 |
| feishu-common | 模块 | 必需 | 飞书通用认证模块 |
| 飞书应用 | 应用 | 必需 | 飞书开放平台创建应用 |
| app_id/app_secret | 凭证 | 必需 | 飞书应用配置页获取 |
| cron 服务 | 系统服务 | 可选 | 系统自带（定时任务需要） |
| 数据库 | 存储引擎 | 可选 | 用于模板版本与日志（可选 SQLite 文件存储） |

### API Key 配置

- 本工具通过飞书应用凭证（app_id 与 app_secret）进行认证
- 凭证由 feishu-common 模块统一管理
- 交互回调需配置 callback_secret
- 无需额外 API Key
- 应用需在飞书开放平台开通消息发送与交互回调权限

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，部分功能需要 exec 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行 Node.js 脚本，支持批量推送、模板渲染、交互组件与发送分析等企业级功能
