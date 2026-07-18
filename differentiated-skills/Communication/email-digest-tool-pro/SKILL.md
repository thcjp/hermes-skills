---
slug: email-digest-tool-pro
name: email-digest-tool-pro
version: "1.0.0"
displayName: 邮件日报专业版
summary: 多邮箱AI智能摘要与定时报告，企业级邮件监控与分类方案
license: MIT
edition: pro
description: |-
  邮件日报专业版面向企业用户与高效能个人用户，在免费版邮件摘要能力之上扩展多邮箱聚合、
  AI智能摘要、定时报告推送、邮件智能分类与告警、企业级监控等高级特性。

  核心能力:
  - 多邮箱账户聚合摘要（Gmail/Outlook/QQ/163等统一汇总）
  - AI 智能摘要生成（重要度评分、行动建议、风险提示）
  - 定时报告自动推送（邮件/飞书/钉钉/Slack）
  - 邮件智能分类与标签管理
  - 关键邮件实时告警通知
  - 历史报告归档与趋势分析
  - 自定义摘要规则与过滤策略

  适用场景:
  - 企业管理者的多邮箱统一监控
  - 团队邮件日报自动推送
  - 关键业务邮件实时告警
  - 邮件趋势分析与效能统计
  - 合规审计邮件存档

  差异化: 专业版在免费版全部能力基础上向下兼容，额外提供多邮箱聚合、AI智能摘要、
  定时推送、告警通知与趋势分析，面向企业级邮件监控场景深度优化。

  触发关键词: 邮件摘要, 邮件日报, 多邮箱汇总, AI摘要, 智能分类, 定时报告, 邮件告警, 邮件监控, 趋势分析
tags:
- 沟通协作
- 邮件管理
- 邮件摘要
- 企业效率
- AI智能
tools:
- read
- exec
---

# 邮件日报专业版

**版本**: 1.0.0
**适用对象**: 企业管理者、团队负责人、运维与运营人员
**核心定位**: 企业级多邮箱智能摘要与监控平台
**兼容性**: 完全兼容免费版（email-digest-tool-free）全部功能，可直接升级

---

## 概述

邮件日报专业版是一款面向企业级场景的多邮箱智能摘要与监控工具。在免费版提供的单邮箱摘要生成能力之上，专业版引入多邮箱账户聚合、AI 智能摘要、定时报告推送、邮件智能分类、关键邮件告警与历史趋势分析等高级特性，帮助企业管理者与团队负责人在一个视图中掌握所有邮箱动态，实现邮件的智能化管理与 proactive 监控。

专业版向下完全兼容免费版，现有浏览器自动化流程无需修改即可平滑升级。新增的企业级功能通过扩展命令实现，支持多渠道报告推送与自定义告警规则。

---

## 核心能力

### 多邮箱聚合

- 统一汇总 Gmail、Outlook、QQ邮箱、163邮箱等多个账户
- 跨邮箱合并去重与排序
- 按账户分组展示与统一视图切换
- 多账户健康状态监控

### AI 智能摘要

- 邮件重要度自动评分（高/中/低）
- 智能生成行动建议（回复/审批/跟进）
- 风险邮件识别与提示
- 摘要自然语言生成（支持中文）

### 定时报告推送

- 一次性定时生成报告
- 周期性任务（每日/每周/自定义）
- 多渠道推送（邮件、飞书、钉钉、Slack、Webhook）
- 报告格式自定义（文本/HTML/Markdown）

### 智能分类与标签

- 自动按发件人、主题、内容分类
- 自定义分类规则与标签
- 优先级自动排序
- 分类统计与占比分析

### 告警通知

- 关键邮件实时告警（来自特定发件人或含关键词）
- 未读邮件超量告警
- 告警渠道配置（邮件/即时通讯）
- 告警级别与静默策略

### 趋势分析

- 邮件量趋势图表（日/周/月）
- 发件人排行与占比
- 响应时间统计分析
- 历史报告归档与检索

---

## 使用场景

### 场景一：管理者多邮箱统一日报

企业管理者同时使用 Gmail（对外）和 Outlook（内部），需要每天早晨收到两个邮箱的统一摘要。

```bash
# 生成多邮箱聚合摘要
email-digest-tool aggregate \
  --accounts gmail,outlook \
  --date today \
  --format html \
  --output reports/daily_$(date +%Y%m%d).html

# 自动推送到飞书
email-digest-tool aggregate \
  --accounts gmail,outlook \
  --push feishu \
  --webhook "https://open.feishu.cn/open-apis/bot/v2/hook/xxx"
```

输出报告示例：

```text
==========================================
📧 多邮箱日报 - 2026-07-18
==========================================

📊 账户概览:
- Gmail (manager@company.com): 未读 15 封
- Outlook (manager@company.onmicrosoft.com): 未读 8 封
- 合计未读: 23 封

🔴 高优先级邮件 (3 封):
1. [Gmail] 来自 ceo@company.com
   主题: 董事会决议 - 需要签字
   时间: 08:45 | 评分: 9.5/10
   建议: 立即处理

2. [Outlook] 来自 legal@company.com
   主题: 合同审核 - 紧急
   时间: 09:12 | 评分: 9.0/10
   建议: 今日内回复

🟡 中优先级邮件 (12 封):
...

💡 AI 建议:
- 优先回复董事会决议邮件
- 3 封合同邮件需今日审批
- 5 封订阅邮件可批量归档
==========================================
```

### 场景二：定时报告自动推送

设置每天早上9点自动生成摘要并推送到飞书群。

```bash
# 创建定时推送任务
email-digest-tool schedule create \
  --name "morning-digest" \
  --cron "0 9 * * 1-5" \
  --accounts gmail,outlook \
  --format markdown \
  --push feishu \
  --webhook "https://open.feishu.cn/open-apis/bot/v2/hook/xxx" \
  --timezone "Asia/Shanghai"

# 查看所有定时任务
email-digest-tool schedule list

# 查看任务执行历史
email-digest-tool schedule history --name "morning-digest"
```

### 场景三：关键邮件实时告警

配置当收到来自特定发件人或包含紧急关键词的邮件时立即告警。

```bash
# 配置告警规则
email-digest-tool alert create \
  --name "ceo-alert" \
  --condition "from:ceo@company.com" \
  --channel feishu \
  --webhook "https://open.feishu.cn/open-apis/bot/v2/hook/xxx" \
  --priority critical

email-digest-tool alert create \
  --name "urgent-keyword" \
  --condition "subject contains:紧急,urgent,critical" \
  --channel email \
  --notify "admin@company.com" \
  --priority high

# 启动告警监控
email-digest-tool alert start --all

# 查看告警历史
email-digest-tool alert log --since "2026-07-01"
```

---

## 快速开始

### 从免费版升级

专业版完全兼容免费版，现有浏览器自动化流程可直接使用：

```bash
# 免费版命令依然有效
browser-use --browser real open https://mail.google.com
browser-use state
browser-use screenshot inbox.png

# 专业版新增命令
email-digest-tool aggregate --accounts gmail --format html
```

### 配置多邮箱账户

创建账户配置文件 `~/.config/email-digest-tool/accounts.json`：

```json
{
  "accounts": [
    {
      "name": "Gmail工作邮箱",
      "provider": "gmail",
      "url": "https://mail.google.com",
      "mode": "browser-session"
    },
    {
      "name": "Outlook内部邮箱",
      "provider": "outlook",
      "url": "https://outlook.live.com",
      "mode": "browser-session"
    }
  ]
}
```

### 配置推送渠道

```json
{
  "push_channels": {
    "feishu": {
      "webhook": "https://open.feishu.cn/open-apis/bot/v2/hook/xxx"
    },
    "dingtalk": {
      "webhook": "https://oapi.dingtalk.com/robot/send?access_token=xxx"
    },
    "slack": {
      "webhook": "https://hooks.slack.com/services/xxx"
    },
    "email": {
      "smtp_server": "smtp.company.com",
      "port": 587,
      "username": "bot@company.com",
      "password": "your_password"
    }
  }
}
```

---

## 配置示例

### AI 摘要配置

```json
{
  "ai_summary": {
    "enabled": true,
    "provider": "builtin",
    "language": "zh",
    "features": {
      "importance_scoring": true,
      "action_suggestions": true,
      "risk_detection": true,
      "summary_generation": true
    },
    "scoring_rules": {
      "high_priority_senders": ["ceo@company.com", "boss@company.com"],
      "urgent_keywords": ["紧急", "urgent", "critical", "立即"],
      "high_threshold": 8.0,
      "medium_threshold": 5.0
    }
  }
}
```

### 告警规则配置

```json
{
  "alerts": [
    {
      "name": "高管邮件告警",
      "condition": {
        "from": ["ceo@company.com", "cto@company.com"]
      },
      "channel": "feishu",
      "priority": "critical",
      "silent_hours": "22:00-08:00"
    },
    {
      "name": "未读超量告警",
      "condition": {
        "unread_count_gt": 50
      },
      "channel": "email",
      "notify": "admin@company.com",
      "priority": "medium"
    }
  ]
}
```

### 定时任务配置

```json
{
  "schedules": [
    {
      "name": "每日晨报",
      "cron": "0 9 * * 1-5",
      "timezone": "Asia/Shanghai",
      "accounts": ["gmail", "outlook"],
      "format": "html",
      "push": ["feishu", "email"]
    },
    {
      "name": "周报汇总",
      "cron": "0 18 * * 5",
      "timezone": "Asia/Shanghai",
      "accounts": ["gmail", "outlook"],
      "format": "markdown",
      "push": ["feishu"],
      "include_trends": true
    }
  ]
}
```

---

## 最佳实践

### 多邮箱管理策略

```bash
# 按角色分组管理邮箱
email-digest-tool accounts group create --name "管理层" --accounts gmail,outlook
email-digest-tool accounts group create --name "客服" --accounts service1,service2

# 按分组生成摘要
email-digest-tool aggregate --group "管理层" --format html
```

### 告警策略优化

- 区分告警级别，避免告警疲劳
- 设置静默时段，非工作时间不打扰
- 关键告警多渠道推送，确保触达

```bash
# 测试告警规则
email-digest-tool alert test --name "ceo-alert"

# 调整静默时段
email-digest-tool alert update --name "ceo-alert" --silent-hours "22:00-08:00"
```

### 报告归档与检索

```bash
# 归档历史报告
email-digest-tool archive --since "2026-01-01" --dir reports/archive/

# 检索历史报告
email-digest-tool archive search --keyword "董事会" --since "2026-01-01"
```

---

## 免费版与专业版对比

| 能力 | 免费版 | 专业版 |
|:-----|:------:|:------:|
| 单邮箱摘要 | ✅ | ✅ |
| 浏览器会话复用 | ✅ | ✅ |
| 邮件统计 | 基础统计 | 高级统计 |
| 多邮箱聚合 | ❌ | ✅ |
| AI 智能摘要 | ❌ | ✅（重要度评分） |
| 定时报告推送 | ❌ | ✅（多渠道） |
| 智能分类 | ❌ | ✅（自定义规则） |
| 告警通知 | ❌ | ✅（实时告警） |
| 趋势分析 | ❌ | ✅（图表分析） |
| 报告归档 | ❌ | ✅（可检索） |
| 推送渠道 | 截图 | 邮件/飞书/钉钉/Slack |
| 技术支持 | 社区支持 | 优先支持 |

---

## 常见问题

### 问题1：多邮箱聚合时部分账户失败

**解决**: 检查对应账户的浏览器登录状态，确保会话有效：

```bash
# 验证账户状态
email-digest-tool accounts health-check

# 重新登录失效账户
browser-use --browser real open https://mail.google.com
```

### 问题2：AI 摘要质量不佳

**解决**: 调整评分规则与关键词配置：

```bash
# 更新评分规则
email-digest-tool config update --ai-scoring rules.json

# 查看评分详情
email-digest-tool aggregate --accounts gmail --show-scores
```

### 问题3：定时推送未送达

**解决**: 检查推送渠道配置与网络：

```bash
# 测试推送渠道
email-digest-tool push test --channel feishu

# 查看推送日志
email-digest-tool push log --since "2026-07-01"
```

### 问题4：告警频繁打扰

**解决**: 优化告警规则与静默策略：

```bash
# 查看告警频率统计
email-digest-tool alert stats

# 调整告警阈值
email-digest-tool alert update --name "unread-alert" --threshold 100
```

### 问题5：报告格式不兼容

**解决**: 专业版支持多种格式互转：

```bash
# 格式转换
email-digest-tool convert --input report.html --format markdown
```

---

## 命令参考速查

| 命令 | 功能 | 专业版独有 |
|:-----|:-----|:----------:|
| `aggregate` | 多邮箱聚合摘要 | ✅ |
| `schedule` | 定时任务管理 | ✅ |
| `alert` | 告警规则管理 | ✅ |
| `push` | 推送渠道管理 | ✅ |
| `archive` | 报告归档检索 | ✅ |
| `accounts` | 多账户管理 | ✅ |
| `config` | 配置管理 | ✅ |
| `convert` | 格式转换 | ✅ |

---

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **浏览器**: Chrome 浏览器（需已安装并登录邮箱）
- **Python版本**: 3.9 及以上（browser-use 依赖）
- **网络环境**: 需可访问各邮箱服务与推送渠道

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| browser-use | CLI工具 | 必需 | `uv pip install browser-use[cli]` |
| Chrome 浏览器 | 浏览器 | 必需 | 官方网站下载安装 |
| 邮箱账户 | 账户 | 必需 | 注册主流邮箱服务 |
| 推送渠道 Webhook | 集成 | 可选 | 飞书/钉钉/Slack 机器人配置 |
| cron 服务 | 系统服务 | 可选 | 系统自带（定时任务需要） |
| 数据库 | 存储引擎 | 可选 | 用于报告归档（可选 SQLite 文件存储） |

### API Key 配置

- 本工具通过浏览器会话复用访问邮箱，无需邮箱 API Key
- AI 智能摘要使用 Agent 内置 LLM，无需额外 API Key
- 推送渠道（飞书/钉钉/Slack）需配置对应平台的 Webhook URL
- Webhook URL 通过配置文件提供，建议加密存储

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，部分功能需要 exec 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行浏览器自动化与多渠道推送任务，支持定时调度与告警监控
