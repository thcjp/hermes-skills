---
slug: email-daily-summary
name: email-daily-summary
version: "0.1.0"
displayName: Email Daily Summary
  and generates daily email summaries. Use when the user wants to get a summary of
  their emails, check important messages, or create daily email digests.
summary: "自动登录Gmail/Outlook/QQ等邮箱生成每日邮件摘要"
  generates daily email ...
license: MIT
description: |-
  Automatically logs into email accounts (Gmail, Outlook, QQ Mail, etc。)
  and generates daily email。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Automatically logs into email accounts (Gmail, Outlook, QQ Mail, etc.) and generates daily email summaries. Use when the user wants to get a summary of their emails, check important messages, or create daily email digests.

这个技能帮助你自动登录邮箱，获取邮件内容，并生成每日邮件总结。

## 功能特性

* 🔐 支持多种邮箱登录（Gmail、Outlook、QQ 邮箱、163 邮箱等）
* 📧 自动获取最新邮件列表
* 📝 智能生成邮件摘要
* 🏷️ 按重要性/发件人/主题分类
* 📊 生成每日邮件统计报告

## 前置要求

1. 安装 browser-use CLI：

```bash
uv pip install browser-use[cli]
browser-use install
```

2. 确保已在浏览器中登录过邮箱（使用 real 模式可直接复用登录状态）

## 使用方法

### 方式一：使用已登录的浏览器（推荐）

使用 `--browser real` 模式可以复用你 Chrome 浏览器中已登录的邮箱会话：

```bash
browser-use --browser real open https://mail.google.com

browser-use --browser real open https://outlook.live.com

browser-use --browser real open https://mail.qq.com

browser-use --browser real open https://mail.163.com
```

### 方式二：手动登录流程

如果需要手动登录，使用 `--headed` 模式查看操作过程：

```bash
browser-use --headed open https://accounts.google.com

browser-use state

browser-use input <email_input_index> "your-email@gmail.com"
browser-use click <next_button_index>

browser-use input <password_input_index> "your-password"
browser-use click <login_button_index>

browser-use open https://mail.google.com
```

## 获取邮件列表

登录成功后，获取邮件列表：

```bash
browser-use state

browser-use screenshot emails_$(date +%Y%m%d).png

browser-use eval "
  const emails = [];
  document.querySelectorAll('tr.zA').forEach((row, i) => {
    if (i < 20) {
      const sender = row.querySelector('.yX.xY span')?.innerText || '';
      const subject = row.querySelector('.y6 span')?.innerText || '';
      const snippet = row.querySelector('.y2')?.innerText || '';
      const time = row.querySelector('.xW.xY span')?.innerText || '';
      emails.push({ sender, subject, snippet, time });
    }
  });
  JSON.stringify(emails, null, 2);
"
```

## 使用 Python 生成邮件总结

```bash
browser-use python "
emails_data = []
summary_date = '$(date +%Y-%m-%d)'
"

browser-use python "
for i in range(3):
    browser.scroll('down')
    import time
    time.sleep(1)
"

browser-use python "
import json

html = browser.html

print(f'=== 邮件日报 {summary_date} ===')
print(f'页面 URL: {browser.url}')
print(f'页面标题: {browser.title}')
"

browser-use python "
browser.screenshot(f'email_summary_{summary_date}.png')
print(f'截图已保存: email_summary_{summary_date}.png')
"
```

## 完整的每日邮件总结脚本

创建一个完整的总结流程：

```bash
#!/bin/bash

DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M:%S)
OUTPUT_DIR="./email_summaries"
mkdir -p "$OUTPUT_DIR"

echo "=========================================="
echo "📧 邮件日报生成中..."
echo "日期: $DATE $TIME"
echo "=========================================="

browser-use --browser real open https://mail.google.com

sleep 3

echo ""
echo "📋 当前邮箱状态:"
browser-use state

echo ""
echo "📸 保存截图..."
browser-use screenshot "$OUTPUT_DIR/inbox_$DATE.png"

echo ""
echo "📊 邮件统计:"
browser-use eval "
(() => {
  const unreadCount = document.querySelectorAll('.zE').length;
  const totalVisible = document.querySelectorAll('tr.zA').length;
  return JSON.stringify({
    unread: unreadCount,
    visible: totalVisible,
    timestamp: new Date().toISOString()
  });
})()
"

echo ""
echo "✅ 完成！截图保存至: $OUTPUT_DIR/inbox_$DATE.png"
browser-use close
```

## 支持的邮箱服务

| 邮箱服务 | 登录 URL | 收件箱 URL |
| --- | --- | --- |
| Gmail | <https://accounts.google.com> | <https://mail.google.com> |
| Outlook | <https://login.live.com> | <https://outlook.live.com> |
| QQ 邮箱 | <https://mail.qq.com> | <https://mail.qq.com> |
| 163 邮箱 | <https://mail.163.com> | <https://mail.163.com> |
| 126 邮箱 | <https://mail.126.com> | <https://mail.126.com> |
| 企业微信邮箱 | <https://exmail.qq.com> | <https://exmail.qq.com> |

## 生成 AI 邮件摘要

如果配置了 API Key，可以使用 AI 自动生成邮件摘要：

```bash
browser-use --browser real open https://mail.google.com
browser-use extract "提取前 10 封邮件的发件人、主题和摘要，按重要性排序"
```

## 定时任务设置

### macOS/Linux (crontab)

```bash
crontab -e

0 9 * * * /path/to/email_daily_summary.sh >> /path/to/logs/email_summary.log 2>&1
```

### macOS (launchd)

创建 `~/Library/LaunchAgents/com.email.dailysummary.plist`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.email.dailysummary</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/path/to/email_daily_summary.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/email_summary.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/email_summary_error.log</string>
</dict>
</plist>
```

加载任务：

```bash
launchctl load ~/Library/LaunchAgents/com.email.dailysummary.plist
```

## 示例

生成的邮件总结报告格式：

```text
==========================================
📧 邮件日报 - 2026-01-30
==========================================

📊 统计概览:
- 未读邮件: 12 封
- 今日新邮件: 28 封
- 重要邮件: 5 封

🔴 重要邮件:
1. [工作] 来自 boss@company.com
   主题: 项目进度汇报 - 紧急
   时间: 09:30

2. [财务] 来自 finance@bank.com
   主题: 账单提醒
   时间: 08:15

📬 今日邮件分类:
- 工作相关: 15 封
- 订阅通知: 8 封
- 社交媒体: 3 封
- 其他: 2 封

💡 建议操作:
- 回复 boss@company.com 的邮件
- 处理 3 封需要审批的邮件

==========================================
```

## 安全提示

⚠️ **重要安全建议**：

1. **不要在脚本中明文保存密码**，优先使用 `--browser real` 模式复用已登录会话
2. **敏感信息使用环境变量**存储
3. **定期检查授权应用**，移除不需要的第三方访问
4. **启用两步验证**保护邮箱安全
5. **日志文件不要包含敏感信息**

## 故障排除

**登录失败？**

```bash
browser-use --browser real --headed open https://mail.google.com
```

**页面元素找不到？**

```bash
sleep 5
browser-use state
```

**会话过期？**

```bash
browser-use close --all
browser-use --browser real open https://mail.google.com
```

## 清理

完成后记得关闭浏览器：

```bash
browser-use close
```

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Email Daily Summary？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Email Daily Summary有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
