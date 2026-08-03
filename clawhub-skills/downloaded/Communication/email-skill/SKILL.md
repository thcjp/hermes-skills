---
slug: email-skill
name: email-skill
version: "0.1.0"
displayName: Email
summary: "邮件管理与自动化,跨多提供商发/读/搜/整理"
  across multiple providers.
license: MIT
description: |-
  Email management and automation。Send, read, search, and organize emails
  across multiple providers。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Email

Email management and automation with attachment support.

## Features

* Send emails with attachments
* Support for multiple email providers (Gmail, Outlook, Yahoo, etc.)
* HTML and plain text email support
* CC and BCC recipients
* Test email functionality
* Secure TLS/SSL connections

## Setup Instructions

### 1. Configure Email Credentials

Create a configuration file `email_config.json` in your workspace:

```json
{
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587,
  "username": "your-email@gmail.com",
  "password": "your-app-password",
  "sender_name": "Skill平台 Assistant",
  "use_tls": true,
  "use_ssl": false
}
```

### 2. For Gmail Users (Recommended)

1. Enable 2-factor authentication on your Google account
2. Generate an App Password:
   * Go to <https://myaccount.google.com/security>
   * Under "Signing in to Google," select "App passwords"
   * Generate a new app password for "Mail"
   * Use this 16-character password in your config

### 3. Alternative: Environment Variables

Set these environment variables instead of using a config file:

```bash
set SMTP_SERVER=smtp.gmail.com
set SMTP_PORT=587
set EMAIL_USERNAME=your-email@gmail.com
set EMAIL_PASSWORD=your-app-password
set EMAIL_SENDER_NAME="Skill平台 Assistant"

export SMTP_SERVER=smtp.gmail.com
export SMTP_PORT=587
export EMAIL_USERNAME=your-email@gmail.com
export EMAIL_PASSWORD=your-app-password
export EMAIL_SENDER_NAME="Skill平台 Assistant"
```

## 示例

### Send a Simple Email

```bash
python email_sender.py --to "recipient@example.com" --subject "Hello" --body "This is a test email"
```

### Send Email with Attachment

```bash
python email_sender.py --to "recipient@example.com" --subject "Report" --body "Please find attached" --attachment "report.pdf" --attachment "data.xlsx"
```

### Send Test Email

```bash
python email_sender.py --to "your-email@gmail.com" --test
```

### Using with Skill平台 Commands

```text
"Send email to recipient@example.com with subject Meeting Notes and body Here are the notes from today's meeting"
"Send test email to verify configuration"
"Email the report.pdf file to team@company.com"
```

## Supported Email Providers

| Provider | SMTP Server | Port | TLS |
| --- | --- | --- | --- |
| Gmail | smtp.gmail.com | 587 | Yes |
| Outlook/Office365 | smtp.office365.com | 587 | Yes |
| Yahoo | smtp.mail.yahoo.com | 587 | Yes |
| QQ Mail | smtp.qq.com | 587 | Yes |
| Custom SMTP | your.smtp.server.com | 587/465 | As configured |

## Python API Usage

```python
from email_sender import EmailSender

sender = EmailSender("email_config.json")

result = sender.send_email(
    to_email="recipient@example.com",
    subject="Important Document",
    body="Please review the attached document.",
    attachments=["document.pdf", "data.csv"]
)

if result["success"]:
    print(f"Email sent with {result['attachments']} attachments")
else:
    print(f"Error: {result['error']}")
```

## Troubleshooting

### Common Issues:

1. **Authentication Failed**

   * Verify your username and password
   * For Gmail: Use app password instead of regular password
   * Check if 2FA is enabled
2. **Connection Refused**

   * Verify SMTP server and port
   * Check firewall settings
   * Try different port (465 for SSL)
3. **Attachment Too Large**

   * Most providers limit attachments to 25MB
   * Consider compressing files or using cloud storage links

## Security Notes

* Never commit email credentials to version control
* Use environment variables for production deployments
* Regularly rotate app passwords
* Consider using dedicated email accounts for automation

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 常见问题

### Q1: 如何开始使用Email？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Email有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

Email skill在执行邮件发送、读取、搜索和整理等操作时，存在以下边界条件和限制：

1. **输入格式限制**：邮件地址格式必须符合标准格式，否则可能导致发送失败。
2. **邮件大小限制**：大多数邮件提供商对邮件大小有限制，通常不超过25MB，包括附件。
3. **附件类型限制**：某些邮件提供商可能对附件类型有限制，如不允许发送压缩文件或特定格式的文件。
4. **并发请求限制**：频繁或大量的并发邮件发送请求可能会导致邮件服务提供商限制或拒绝服务。
5. **邮件内容限制**：邮件内容中不应包含垃圾邮件标记词汇，以免被邮件提供商识别为垃圾邮件。
6. **安全性限制**：使用TLS/SSL连接时，如果配置不当，可能会导致连接失败。
7. **2FA和App密码**：使用支持2FA的邮箱时，必须生成并使用App密码，而非常规密码。
8. **邮件服务提供商限制**：不同邮件提供商的SMTP服务器地址、端口和TLS/SSL配置可能不同，需要根据实际情况进行配置。
9. **性能限制**：邮件操作可能受到网络延迟和邮件服务提供商性能的影响。
10. **语言和编码限制**：邮件内容应使用UTF-8编码，以支持多语言邮件发送。

---

