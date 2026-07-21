---
slug: email-toolkit
name: email-toolkit
version: "1.0.0"
displayName: 邮件工具箱专业版
summary: 企业邮件自动化与批量发送方案，支持模板与定时调度
license: Proprietary
edition: pro
description: |-
  邮件工具箱专业版面向企业用户与高效能个人用户。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
tags:
- 沟通协作
- 邮件管理
- 邮件发送
- 企业效率
- 批量操作
tools:
  - - read
- exec
---
# 邮件工具箱专业版

## 核心能力

### 批量发送引擎
- **收件人列表**: 支持 CSV/JSON 收件人列表文件
- **变量替换**: 模板中支持 `（根据实际场景填充）`、`（根据实际场景填充）` 等变量插值
- **速率控制**: 可配置发送速率与并发数
- **失败重试**: 自动重试失败邮件
- **发送日志**: 完整记录发送结果

### 邮件模板系统
- **内置模板**: 通知、报告、邀请、提醒、审批等常用模板
- **自定义模板**: 创建、编辑、删除自定义模板
- **变量插值**: 支持 `（根据实际场景填充）` 语法
- **条件渲染**: 支持条件判断逻辑
- **模板预览**: 渲染效果预览

**输入**: 用户提供邮件模板系统所需的指令和必要参数。
**处理**: 按照skill规范执行邮件模板系统操作,遵循单一意图原则。### 定时调度
- **一次性定时**: 指定时间发送
- **周期性任务**: 每日/每周/每月/自定义 cron
- **任务队列**: 管理待发送任务
- **状态监控**: 实时查看任务执行状态

**输入**: 用户提供定时调度所需的指令和必要参数。
**输出**: 返回定时调度的执行结果,包含操作状态和输出数据。### 多服务商负载均衡
- **多 SMTP 池**: 配置多个 SMTP 服务商
- **负载分配**: 按权重或轮询分配发送
- **故障切换**: 自动切换到可用服务商
- **用量监控**: 各服务商发送量统计

**输入**: 用户提供多服务商负载均衡所需的指令和必要参数。
**输出**: 返回多服务商负载均衡的执行结果,包含操作状态和输出数据。### 发送队列与重试
- **异步队列**: 非阻塞发送，提升吞吐量
- **优先级队列**: 支持邮件优先级
- **自动重试**: 可配置重试次数与间隔
- **死信处理**: 失败邮件单独存储

**输入**: 用户提供发送队列与重试所需的指令和必要参数。
**输出**: 返回发送队列与重试的执行结果,包含操作状态和输出数据。### 退信处理
- **退信检测**: 自动识别退信邮件
- **地址清理**: 自动清理无效地址
- **退信报告**: 退信统计与分析

**输入**: 用户提供退信处理所需的指令和必要参数。
**输出**: 返回退信处理的执行结果,包含操作状态和输出数据。### 分析报告
- **发送统计**: 成功/失败/退信统计
- **趋势分析**: 发送量趋势图表
- **服务商效能**: 各 SMTP 服务商性能对比
- **导出报告**: CSV/JSON 格式导出

---

## 适用场景

### 场景一：批量发送个性化营销邮件
市场部需要向2000名客户发送个性化的促销邮件，每封邮件包含客户姓名与专属优惠码。

**准备收件人列表** `customers.csv`:

```csv
email,name,discount_code,category
customer1@example.com,张三,SAVE20,电子
customer2@example.com,李四,SAVE15,服装
customer3@example.com,王五,SAVE25,家居
```

**创建邮件模板** `templates/promo.html`:

```html
<h1>（根据实际场景填充），专属优惠等你来！</h1>
<p>尊敬的 （根据实际场景填充）：</p>
<p>感谢您对我们 （根据实际场景填充） 品类的关注，为您奉上专属优惠码：<strong>（根据实际场景填充）</strong></p>
<p>优惠码有效期至2026年7月31日，请尽快使用。</p>
```

**执行批量发送**:

```bash
# 试运行（预览不实际发送）
python email_sender.py batch-send \
  --recipients customers.csv \
  --template templates/promo.html \
  --subject "（根据实际场景填充） - 专属优惠码 （根据实际场景填充）" \
  --rate-limit 20 \
  --dry-run

# 正式发送（使用多 SMTP 负载均衡）
python email_sender.py batch-send \
  --recipients customers.csv \
  --template templates/promo.html \
  --subject "（根据实际场景填充） - 专属优惠码 （根据实际场景填充）" \
  --rate-limit 20 \
  --pool gmail,outlook \
  --retry 3 \
  --log batch_promo.log
```

输出示例：

```text
📋 批量发送任务
   收件人: 2000
   模板: templates/promo.html
   速率: 20 封/分钟
   SMTP 池: gmail, outlook

[1/2000] ✅ customer1@example.com - 张三 - SAVE20 (via gmail)
[2/2000] ✅ customer2@example.com - 李四 - SAVE15 (via outlook)
...
📊 发送完成: 1998 成功, 2 失败
   失败列表: failures.csv
   发送报告: batch_promo_report.json
```

### 场景二：定时发送每日报告
运维团队需要每天早上8点自动发送系统监控日报给管理层。

```bash
# 创建定时任务
python email_sender.py schedule create \
  --name "daily-report" \
  --cron "0 8 * * 1-5" \
  --to "management@company.com" \
  --subject "系统监控日报 - （根据实际场景填充）" \
  --template templates/daily_report.html \
  --data-source "generate_report.py" \
  --timezone "Asia/Shanghai"

# 查看所有定时任务
python email_sender.py schedule list

# 查看任务执行历史
python email_sender.py schedule history --name "daily-report"
```

### 场景三：多 SMTP 负载均衡发送
企业有3个邮箱账户用于发送，需要负载均衡分配发送量。

```python
from email_sender import EmailSender, SMTPPool

# 配置多 SMTP 服务商
pool = SMTPPool([
    {"name": "gmail-primary", "smtp_server": "smtp.gmail.com", "smtp_port": 587,
     "username": "sender1@company.com", "password": "pass1", "weight": 50},
    {"name": "outlook-backup", "smtp_server": "smtp.office365.com", "smtp_port": 587,
     "username": "sender2@company.com", "password": "pass2", "weight": 30},
    {"name": "yahoo-extra", "smtp_server": "smtp.mail.yahoo.com", "smtp_port": 587,
     "username": "sender3@company.com", "password": "pass3", "weight": 20},
])

sender = EmailSender(pool=pool)

# 批量发送
results = sender.batch_send(
    recipients="customers.csv",
    template="templates/promo.html",
    subject="优惠通知",
    rate_limit=30,
    retry=3
)

print(f"成功: {results.success}, 失败: {results.failed}")
print(f"服务商分配: {results.provider_stats}")
```

---

## 使用流程

### 从免费版升级
专业版完全兼容免费版，现有配置与 API 无需修改：

```python
# 免费版 API 依然有效
from email_sender import EmailSender
sender = EmailSender("email_config.json")
sender.send_email(to_email="x@y.com", subject="测试", body="内容")

# 专业版新增 API
sender.batch_send(recipients="list.csv", template="tpl.html", subject="通知")
```

### 配置多 SMTP 池
创建 `smtp_pool.json`：

```json
{
  "pool": [
    {
      "name": "primary",
      "smtp_server": "smtp.gmail.com",
      "smtp_port": 587,
      "username": "sender1@company.com",
      "password": "app_password_1",
      "weight": 50,
      "daily_limit": 500
    },
    {
      "name": "backup",
      "smtp_server": "smtp.office365.com",
      "smtp_port": 587,
      "username": "sender2@company.com",
      "password": "app_password_2",
      "weight": 50,
      "daily_limit": 500
    }
  ],
  "strategy": "weighted",
  "failover": true
}
```

### 专业版扩展配置
```json
{
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587,
  "username": "your-email@gmail.com",
  "password": "your-app-password",
  "sender_name": "企业邮件系统",
  "use_tls": true,
  "pro": {
    "batch": {
      "rate_limit": 20,
      "max_recipients": 5000,
      "retry_count": 3,
      "retry_delay": 60,
      "concurrency": 10
    },
    "pool": {
      "config_file": "smtp_pool.json",
      "strategy": "weighted",
      "failover": true
    },
    "schedule": {
      "enabled": true,
      "timezone": "Asia/Shanghai",
      "queue_dir": "~/.config/email-toolkit/queue"
    },
    "bounce": {
      "enabled": true,
      "check_interval": 3600,
      "auto_clean": true
    },
    "analytics": {
      "enabled": true,
      "log_file": "~/.config/email-toolkit/analytics.log"
    }
  }
}
```

---

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
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8 及以上
- **网络环境**: 需可访问各邮箱 SMTP 服务器
- **磁盘空间**: 队列与日志建议预留 1GB 以上

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 官方网站下载安装 |
| Python 标准库 | 运行库 | 必需 | Python 自带（smtplib, email, csv, json） |
| 邮箱账户 | 账户 | 必需 | 注册主流邮箱服务商 |
| 应用专用密码 | 凭证 | 必需 | 邮箱安全设置页生成 |
| cron 服务 | 系统服务 | 可选 | 系统自带（定时任务需要） |
| 数据库 | 存储引擎 | 可选 | 用于队列与日志（可选 SQLite 文件存储） |

### API Key 配置
- 本工具使用邮箱 SMTP 认证，无需额外 API Key
- 多 SMTP 池场景下每个服务商使用独立凭证
- 凭证通过配置文件或环境变量提供，支持加密存储
- 企业用户建议使用密钥管理服务统一管理凭证

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要 exec 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行 Python 脚本，支持批量发送、模板渲染、定时调度与负载均衡等企业级自动化功能

## 案例展示

### 模板系统配置
```json
{
  "templates": {
    "dir": "templates/",
    "builtins": ["notification", "report", "invitation", "reminder"],
    "custom": [
      {
        "name": "月度报告",
        "file": "templates/monthly_report.html",
        "variables": ["month", "data", "summary"]
      }
    ]
  }
}
```

### 定时任务配置
```json
{
  "schedules": [
    {
      "name": "weekly-newsletter",
      "cron": "0 10 * * 1",
      "recipients": "subscribers.csv",
      "template": "templates/newsletter.html",
      "subject": "本周资讯 （根据实际场景填充）",
      "timezone": "Asia/Shanghai"
    }
  ]
}
```

---

## 常见问题

### 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制
**解决**: 使用多 SMTP 负载均衡分散发送量：

```bash
# 使用多个服务商
python email_sender.py batch-send --recipients list.csv --pool gmail,outlook,yahoo --rate-limit 10
```

### 问题2：模板变量未替换
**解决**: 确保变量名与 CSV 列名一致：

```bash
# 验证模板
python email_sender.py template validate --name "通知" --data sample.json
```

### 问题3：定时任务未执行
**解决**: 检查 cron 表达式与时区：

```bash
# 验证 cron 表达式
python email_sender.py schedule validate --cron "0 8 * * 1-5"

# 检查任务状态
python email_sender.py schedule status --name "daily-report"
```

### 问题4：SMTP 池故障切换失败
**解决**: 检查各服务商凭证有效性：

```bash
# 测试所有 SMTP 服务商
python email_sender.py pool test --all

# 查看服务商状态
python email_sender.py pool status
```

### 问题5：退信率过高
**解决**: 定期清理无效地址，优化收件人列表：

```bash
# 分析退信原因
python email_sender.py bounce analyze --since "2026-06-01"

# 清理无效地址
python email_sender.py bounce clean --recipients customers.csv --output cleaned.csv
```

---

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 需要LLM支持
- 需要LLM支持
- 需要LLM支持

