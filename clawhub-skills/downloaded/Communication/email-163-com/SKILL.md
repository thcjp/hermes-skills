---
slug: email-163-com
name: email-163-com
version: "1.0.5"
displayName: Email 163 Com
summary: Comprehensive Python tool for managing 163.com emails with sending, reading,
  searching, folder, a...
license: MIT-0
description: |-
  Comprehensive Python tool for managing 163。com emails with sending,
  reading, searching, folder, a。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Email 163 Com

**版本**: 1.0.0
**创建日期**: 2026-02-19
**作者**: Skill平台
**描述**: 163 邮箱完整邮件管理工具（Python 实现）

---

## 核心能力

### 核心功能

* ✅ **发送邮件** - 支持纯文本和 HTML 格式
* ✅ **发送附件** - 支持单个或多个附件
* ✅ **读取邮件** - 支持 IMAP ID 认证（163 邮箱要求）
* ✅ **文件夹管理** - 列出、创建、删除文件夹
* ✅ **邮件搜索** - 按发件人、主题、日期等搜索
* ✅ **邮件操作** - 删除、移动、标记已读/未读
* ✅ **附件管理** - 下载、查看附件
* ✅ **配置管理** - 邮箱配置和账户管理

### 技术特点

* ✅ 支持 163 邮箱 IMAP ID 扩展（RFC 2971）
* ✅ TLS/SSL 加密连接
* ✅ 支持中文主题和发件人
* ✅ 支持 HTML 邮件
* ✅ 支持多附件发送
* ✅ 命令行友好界面

---

## 使用流程

### 依赖说明

```bash
```

### 2. 配置邮箱

编辑 `~/.config/email-163-com/config.json`:

```json
{
  "email": "your_email@163.com",
  "password": "your_auth_code",
  "imap_server": "imap.163.com",
  "imap_port": 993,
  "smtp_server": "smtp.163.com",
  "smtp_port": 465
}
```

### 3. 基本使用

```bash
email-163-com --help

email-163-com read

email-163-com send --to friend@example.com --subject "Hello" --body "Hi!"

email-163-com send --to friend@example.com --subject "File" --attach file.pdf

email-163-com folders
```

---

## 📖 命令参考

### 发送邮件

```bash
email-163-com send --to <email> --subject <subject> --body <body>

email-163-com send --to <email> --subject <subject> --html "<h1>Hello</h1>"

email-163-com send --to <email> --subject <subject> --attach file1.pdf --attach file2.txt

email-163-com send --to <email> --subject <subject> --file message.txt
```

### 读取邮件

```bash
email-163-com read

email-163-com read --count 10

email-163-com read --folder "已发送" --count 5

email-163-com read --id 123 --full
```

### 文件夹管理

```bash
email-163-com folders

email-163-com folder create "MyFolder"

email-163-com folder delete "MyFolder"
```

### 邮件搜索

```bash
email-163-com search --from "Cloudflare"

email-163-com search --subject "verify"

email-163-com search --from "阿里云" --subject "通知" --count 10
```

### 邮件操作

```bash
email-163-com delete --id 123

email-163-com move --id 123 --to "已删除"

email-163-com flag --id 123 --set seen

email-163-com flag --id 123 --unset seen
```

### 附件管理

```bash
email-163-com attachments --id 123

email-163-com attachments --id 123 --download --output ~/Downloads/
```

---

## 🔧 配置文件

### 位置

`~/.config/email-163-com/config.json`

### 格式

```json
{
  "email": "your_email@163.com",
  "password": "your_auth_code",
  "imap_server": "imap.163.com",
  "imap_port": 993,
  "smtp_server": "smtp.163.com",
  "smtp_port": 465,
  "imap_id": {
    "name": "Skill平台",
    "version": "1.0.0",
    "vendor": "email-163-com",
    "support_email": "support@email-163-com.skill"
  },
  "defaults": {
    "folder": "INBOX",
    "count": 5,
    "output_dir": "~/Downloads"
  }
}
```

---

## 示例

### 示例 1: 发送日常工作邮件

```bash
email-163-com send \
  --to colleague@example.com \
  --subject "项目进度更新" \
  --file report.txt \
  --attach progress.pdf
```

### 示例 2: 查看未读邮件

```bash
email-163-com read --count 10 --unread
```

### 示例 3: 搜索特定邮件

```bash
email-163-com search \
  --from "Cloudflare" \
  --subject "verify" \
  --count 5
```

### 示例 4: 清理垃圾邮件

```bash
email-163-com search --folder "垃圾邮件" --count 100
email-163-com delete --folder "垃圾邮件" --all
```

---

## 📋 输出格式

### 读取邮件

```text
📬 INBOX: 16 messages total

📧 From: 阿里云
   Subject: 域名信息修改成功通知
   Date: Wed, 18 Feb 2026 22:00:53
   ID: 16
   Flags: \Seen
--------------------------------------------------

📧 From: "Cloudflare" <noreply@notify.cloudflare.com>
   Subject: [Action required] Verify your email address
   Date: Wed, 18 Feb 2026 14:17:02
   ID: 15
   Flags:
--------------------------------------------------
```

### 发送邮件

```text
✅ Message sent successfully!
   To: friend@example.com
   Subject: Hello
   Attachments: file.pdf (1.2 MB)
```

---

## 🔐 安全说明

### 授权码

* 不要使用邮箱登录密码
* 使用 163 邮箱的"客户端授权码"
* 获取方式：登录网页版 → 设置 → POP3/SMTP/IMAP

### 配置文件权限

```bash
chmod 600 ~/.config/email-163-com/config.json
```

### 环境变量（可选）

也可以使用环境变量代替配置文件：

```bash
export EMAIL_163_USER="your_email@163.com"
export EMAIL_163_PASS="your_auth_code"
```

---

## 错误处理

### 问题 1: IMAP 连接失败

```text
Error: SELECT Unsafe Login
```

**解决**: 确保配置了 IMAP ID 信息（默认已配置）

### 问题 2: 认证失败

```text
Error: LOGIN failed
```

**解决**: 检查授权码是否正确（不是登录密码）

### 问题 3: 附件发送失败

```text
Error: Cannot attach file
```

**解决**: 检查文件路径是否正确，文件是否可读

---

## 📚 技术参考

* **RFC 2971**: IMAP4 ID extension
* **RFC 3501**: IMAP4rev1
* **RFC 5322**: Internet Message Format
* **163 邮箱帮助**: <https://help.mail.163.com/>

---

## 🔄 更新日志

### v1.0.0 (2026-02-19)

* ✅ 初始版本
* ✅ 支持发送邮件（文本/HTML）
* ✅ 支持发送附件
* ✅ 支持读取邮件（IMAP ID）
* ✅ 支持文件夹管理
* ✅ 支持邮件搜索
* ✅ 支持邮件操作（删除/移动/标记）
* ✅ 支持附件下载

---

## 📞 支持

* **文档**: `~/.skill-platform/workspace/skills/email-163-com/README.md`
* **配置**: `~/.config/email-163-com/config.json`
* **脚本**: `~/.skill-platform/workspace/skills/email-163-com/main.py`

---

**首次发布**: 2026-02-19
**维护者**: Skill平台 Team

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
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

## 常见问题

### Q1: 如何开始使用Email 163 Com？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Email 163 Com有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
