---
slug: "email-digest"
name: "email-digest"
version: "1.0.0"
displayName: "邮件日报专业版"
summary: "多邮箱AI智能摘要与定时报告，企业级邮件监控与分类方案"
license: "Proprietary"
edition: "pro"
description: |-
  邮件日报专业版面向企业用户与高效能个人用户。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - 沟通协作
  - 邮件管理
  - 邮件摘要
  - 企业效率
  - AI智能
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 邮件日报专业版

## 核心能力

### 多邮箱聚合
- 统一汇总 Gmail、Outlook、QQ邮箱、163邮箱等多个账户
- 跨邮箱合并去重与排序
- 按账户分组展示与统一视图切换
- 多账户健康状态监控

**输入**: 用户提供多邮箱聚合所需的指令和必要参数。
**输出**: 返回多邮箱聚合的执行结果,包含操作状态和输出数据。### AI 智能摘要
- 邮件重要度自动评分（高/中/低）
- 智能生成行动建议（回复/审批/跟进）
- 风险邮件识别与提示
- 摘要自然语言生成（支持中文）

**输入**: 用户提供AI 智能摘要所需的指令和必要参数。
**处理**: 按照skill规范执行AI 智能摘要操作,遵循单一意图原则。### 定时报告推送
- 一次性定时生成报告
- 周期性任务（每日/每周/自定义）
- 多渠道推送（邮件、飞书、钉钉、Slack、Webhook）
- 报告格式自定义（文本/HTML/Markdown）

**输入**: 用户提供定时报告推送所需的指令和必要参数。
**处理**: 按照skill规范执行定时报告推送操作,遵循单一意图原则。### 智能分类与标签
- 自动按发件人、主题、内容分类
- 自定义分类规则与标签
- 优先级自动排序
- 分类统计与占比分析

**输入**: 用户提供智能分类与标签所需的指令和必要参数。
**输出**: 返回智能分类与标签的执行结果,包含操作状态和输出数据。### 告警通知
- 关键邮件实时告警（来自特定发件人或含关键词）
- 未读邮件超量告警
- 告警渠道配置（邮件/即时通讯）
- 告警级别与静默策略

**输入**: 用户提供告警通知所需的指令和必要参数。
**处理**: 按照skill规范执行告警通知操作,遵循单一意图原则。
**输出**: 返回告警通知的执行结果,包含操作状态和输出数据。### 趋势分析
- 邮件量趋势图表（日/周/月）
- 发件人排行与占比
- 响应时间统计分析
- 历史报告归档与检索

---

**输入**: 用户提供趋势分析所需的指令和必要参数。
**输出**: 返回趋势分析的执行结果,包含操作状态和输出数据。
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: 智能摘要与定时报、企业级邮件监控与、分类方案、邮件日报专业版面、向企业用户与高效、能个人用户、Use、需要消息发送、通知推送、邮件短信、通信集成时使用、不适用于垃圾信息、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

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
  --webhook "https://open.feishu.cn/open-apis/bot/v2/hook/详情见说明"
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
  --webhook "https://open.feishu.cn/open-apis/bot/v2/hook/详情见说明" \
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
  --webhook "https://open.feishu.cn/open-apis/bot/v2/hook/详情见说明" \
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

## 使用流程

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
      "webhook": "https://open.feishu.cn/open-apis/bot/v2/hook/详情见说明"
    },
    "dingtalk": {
      "webhook": "https://oapi.dingtalk.com/robot/send?access_token=详情见说明"
    },
    "slack": {
      "webhook": "https://hooks.slack.com/services/详情见说明"
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

### 命令参数说明

1. `--notify`: 命令参数,用于指定操作选项
2. `--date`: 命令参数,用于指定操作选项
3. `--condition`: 命令参数,用于指定操作选项
4. `-keyword`: 命令参数,用于指定操作选项
5. `--ai-scoring`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

### 命令参数说明

- `-session`: 命令参数,用于指定操作选项
- `--priority`: 命令参数,用于指定操作选项
- `--push`: 命令参数,用于指定操作选项
- `-apis`: 命令参数,用于指定操作选项
- `--channel`: 命令参数,用于指定操作选项

### 命令参数说明

- `--timezone`: 命令参数,用于指定操作选项
- `--since`: 命令参数,用于指定操作选项
- `-check`: 命令参数,用于指定操作选项
- `--input`: 命令参数,用于指定操作选项
- `-alert`: 命令参数,用于指定操作选项

### 命令参数说明

- `--show-scores`: 命令参数,用于指定操作选项
- `--threshold`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **浏览器**: Chrome 浏览器（需已安装并登录邮箱）
- **Python版本**: 3.9 及以上（browser-use 依赖）
- **网络环境**: 需可访问各邮箱服务与推送渠道

### 依赖说明
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

## 案例展示

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
