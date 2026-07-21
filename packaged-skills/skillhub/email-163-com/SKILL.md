---
slug: email-163-com
name: email-163-com
version: "1.0.0"
displayName: 163邮箱管理专家
summary: 163邮箱CLI工具,支持IMAP ID认证收发邮件、附件、文件夹、搜索与邮件操作
license: MIT
description: |-
  163邮箱完整邮件管理Skill,基于Python CLI实现,覆盖发送、读取、搜索、文件夹、附件与邮件操作全链路。

  核心能力:
  - 发送邮件(纯文本/HTML/多附件/文件正文)
  - 读取邮件(IMAP ID扩展RFC 2971,163邮箱必需)
  - 文件夹管理(列出/创建/删除)
  - 邮件搜索(按发件人/主题/日期/文件夹)
  - 邮件操作(删除/移动/标记已读未读)
  - 附件管理(查看/批量下载)
  - TLS/SSL加密连接与中文主题支持

  适用场景:
  - 日常工作邮件批量发送与附件处理
  - 未读邮件快速查阅与分类管理
  - 按发件人/主题精准搜索历史邮件
  - 垃圾邮件批量清理与文件夹整理
tags:
  - Communication
  - Productivity
  - Email
tools:
  - read
  - exec
---

# 163邮箱管理专家

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD（纯Markdown指令，无需exec命令行能力）

## 核心能力

本Skill基于163邮箱IMAP/SMTP协议实现完整邮件管理,重点解决以下领域问题:

- **IMAP ID认证**: 163邮箱强制要求IMAP ID扩展(RFC 2971),未配置会触发 `SELECT Unsafe Login` 错误
- **发送邮件**: 支持纯文本(`--body`)、HTML(`--html`)、文件正文(`--file`)、多附件(`--attach`)
- **读取邮件**: 支持 `--count`、`--folder`、`--id`、`--full`、`--unread` 多维筛选
- **文件夹管理**: 列出(`folders`)、创建(`folder create`)、删除(`folder delete`)
- **邮件搜索**: 按发件人(`--from`)、主题(`--subject`)、文件夹(`--folder`)、数量(`--count`)组合查询
- **邮件操作**: 删除(`delete`)、移动(`move`)、标记已读/未读(`flag --set/--unset seen`)
- **附件管理**: 查看(`attachments --id`)、下载(`attachments --id --download --output`)
- **配置管理**: JSON配置文件 + 环境变量双模式,支持默认文件夹与下载目录
### IMAP ID认证

执行IMAP ID认证操作,处理用户输入并返回结果。

**输入**: 用户提供IMAP ID认证所需的参数和指令。

**输出**: 返回IMAP ID认证的处理结果。

- 执行`IMAP ID认证`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`IMAP ID认证`相关配置参数进行设置
### 发送邮件

执行发送邮件操作,处理用户输入并返回结果。

**输入**: 用户提供发送邮件所需的参数和指令。

**输出**: 返回发送邮件的处理结果。

- 执行`发送邮件`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`发送邮件`相关配置参数进行设置
### 读取邮件

执行读取邮件操作,处理用户输入并返回结果。

**输入**: 用户提供读取邮件所需的参数和指令。

**输出**: 返回读取邮件的处理结果。

- 执行`读取邮件`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`读取邮件`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: CLI、认证收发邮件、搜索与邮件操作、邮箱完整邮件管理、Python、覆盖发送、附件与邮件操作全。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`email-163-com`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 适用场景

### 场景一： 日常工作邮件批量发送
- **输入**: 收件人 colleague@example.com,主题"项目进度更新",正文来自 report.txt,附件 progress.pdf
- **处理**: 执行 `email-163-com send --to colleague@example.com --subject "项目进度更新" --file report.txt --attach progress.pdf`
- **输出**: 发送成功确认,显示收件人、主题、附件名及大小

### 场景二： 未读邮件快速查阅与分类
- **输入**: 需要查看最近10封未读邮件,并将Cloudflare验证邮件移动到"运维"文件夹
- **处理**: 先执行 `email-163-com read --count 10 --unread`;定位Cloudflare邮件ID后执行 `email-163-com move --id 15 --to "运维"`
- **输出**: 未读邮件列表(含发件人/主题/日期/ID/Flags) + 移动操作确认

### 场景三： 按发件人精准搜索历史邮件
- **输入**: 搜索阿里云发来的所有"通知"主题邮件,最多返回10封
- **处理**: 执行 `email-163-com search --from "阿里云" --subject "通知" --count 10`
- **输出**: 匹配邮件列表,含发件人、主题、日期、ID、Flags

### 场景四： 垃圾邮件批量清理
- **输入**: 清理"垃圾邮件"文件夹中的所有邮件
- **处理**: 先执行 `email-163-com search --folder "垃圾邮件" --count 100` 确认数量;再执行 `email-163-com delete --folder "垃圾邮件" --all`
- **输出**: 搜索结果列表 + 批量删除确认

## 案例展示

### 案例1: 发送带附件的项目周报
**背景**: 每周五需向团队发送项目周报,正文在本地 report.txt,附带你 progress.pdf 与 stats.xlsx 两个文件。

**操作**:
```bash
email-163-com send \
  --to team@example.com \
  --subject "项目周报-2026年第7周" \
  --file report.txt \
  --attach progress.pdf \
  --attach stats.xlsx
```

**输出**:
```text
✅ Message sent successfully!
   To: team@example.com
   Subject: 项目周报-2026年第7周
   Attachments: progress.pdf (1.2 MB), stats.xlsx (85 KB)
```

**要点**: `--file` 指定正文文件,`--attach` 可多次使用添加多个附件;中文主题与附件名均正常处理。

### 案例2: 搜索并下载Cloudflare验证邮件附件
**背景**: 需要找到Cloudflare发来的验证邮件,下载其中的验证文档。

**操作**:
```bash
# 第一步:搜索Cloudflare邮件
email-163-com search --from "Cloudflare" --subject "verify" --count 5

# 第二步:查看邮件ID为15的附件列表
email-163-com attachments --id 15

# 第三步:下载附件到指定目录
email-163-com attachments --id 15 --download --output ~/Downloads/
```

**输出**:
```text
📧 From: "Cloudflare" <noreply@notify.cloudflare.com>
   Subject: [Action required] Verify your email address
   Date: Wed, 18 Feb 2026 14:17:02
   ID: 15
   Flags:
--------------------------------------------------
📎 Attachments for message #15:
   1. verification.pdf (245 KB)
   2. instructions.txt (3 KB)
✅ Downloaded 2 attachments to ~/Downloads/
```

**要点**: 搜索支持 `--from` 与 `--subject` 组合;附件下载前先用 `attachments --id` 确认附件清单。

### 案例3: 批量清理垃圾邮件并标记重要邮件
**背景**: 垃圾邮件积累过多需批量清理,但其中有一封阿里云通知需先移动到收件箱保留。

**操作**:
```bash
# 第一步:查看垃圾邮件
email-163-com search --folder "垃圾邮件" --count 100

# 第二步:定位阿里云通知邮件(ID=42),移动到收件箱
email-163-com move --id 42 --to "INBOX"

# 第三步:标记为已读
email-163-com flag --id 42 --set seen

# 第四步:批量删除剩余垃圾邮件
email-163-com delete --folder "垃圾邮件" --all
```

**要点**: 批量删除前务必确认重要邮件已移出;`flag --set seen` 标记已读,`--unset seen` 标记未读。

## 异常处理

### 1. IMAP连接失败: SELECT Unsafe Login
**原因**: 163邮箱强制要求IMAP ID扩展(RFC 2971),未配置IMAP ID信息会拒绝登录
**处理**: 确认配置文件中已配置 `imap_id` 字段(name/version/vendor/support_email);默认配置已内置,若自定义需保留该字段

### 2. 认证失败: LOGIN failed
**原因**: 使用了邮箱登录密码而非客户端授权码
**处理**: 登录163网页版,进入 设置 → POP3/SMTP/IMAP,开启IMAP/SMTP服务并生成客户端授权码;将授权码填入配置文件的 `password` 字段,不要使用登录密码

### 3. 附件发送失败: Cannot attach file
**原因**: 文件路径错误、文件不存在或无读取权限
**处理**: 确认文件路径为绝对路径或相对于当前工作目录的正确路径;检查文件权限;附件大小不超过163邮箱单邮件限制(通常50MB)

### 4. 中文文件夹名操作失败
**原因**: 终端编码非UTF-8导致中文文件夹名(如"已发送""垃圾邮件")传输异常
**处理**: 确保终端使用UTF-8编码;Windows PowerShell执行 `chcp 65001` 切换编码;或使用文件夹的英文名(如INBOX)

### 5. HTML邮件显示为纯文本
**原因**: `--html` 参数内容未正确转义,或邮件客户端不支持HTML渲染
**处理**: 确认 `--html` 内容为合法HTML;使用 `--file` 指定HTML文件避免命令行转义问题;测试时先发送给自己验证渲染效果

### 6. 搜索结果为空但邮件存在
**原因**: 163邮箱IMAP搜索对中文支持有限,或搜索条件过严
**处理**: 放宽搜索条件,先只用 `--from` 或只用 `--subject`;确认搜索的文件夹正确(默认INBOX);改用 `read --folder` 浏览定位

### 7. 邮件移动后原文件夹仍可见
**原因**: IMAP移动是复制+删除,删除标记需EXPUNGE才会物理清除
**处理**: 移动后刷新文件夹列表;必要时执行删除操作触发EXPUNGE;163邮箱通常会在会话结束时自动清理

### 8. 附件下载乱码或损坏
**原因**: 附件为中文文件名时编码处理异常,或下载中断
**处理**: 确认输出目录存在且有写权限;检查磁盘空间;若文件名乱码,重命名后验证文件完整性

## FAQ

### Q1: 为什么必须使用客户端授权码而不是登录密码?
A: 163邮箱出于安全考虑,IMAP/SMTP登录必须使用客户端授权码而非账号登录密码。获取方式:登录163网页版 → 设置 → POP3/SMTP/IMAP → 开启服务并生成授权码。授权码仅显示一次,请妥善保存。

### Q2: 配置文件应该放在哪里?格式是什么?
A: 默认路径 `~/.config/email-163-com/config.json`,包含 `email`、`password`(授权码)、`imap_server`(imap.163.com)、`imap_port`(993)、`smtp_server`(smtp.163.com)、`smtp_port`(465)等字段。也可使用环境变量 `EMAIL_163_USER` 和 `EMAIL_163_PASS` 替代配置文件。建议执行 `chmod 600 config.json` 设置文件权限。

### Q3: 如何发送HTML格式邮件?
A: 使用 `--html` 参数直接传入HTML内容,如 `email-163-com send --to x@example.com --subject "Hello" --html "<h1>标题</h1><p>正文</p>"`。HTML内容较长时建议使用 `--file` 指定HTML文件,避免命令行转义问题。

### Q4: IMAP ID是什么?为什么163邮箱必需?
A: IMAP ID是RFC 2971定义的IMAP4 ID扩展,用于向服务器标识客户端身份(名称、版本、厂商等)。163邮箱强制要求IMAP ID,未配置会返回 `SELECT Unsafe Login` 错误。本Skill默认已内置IMAP ID配置,自定义时需保留 `imap_id` 字段。

### Q5: 如何批量下载某封邮件的所有附件?
A: 先用 `email-163-com attachments --id <ID>` 查看附件清单,再用 `email-163-com attachments --id <ID> --download --output ~/Downloads/` 批量下载到指定目录。下载目录可在配置文件 `defaults.output_dir` 中设置默认值。

### Q6: 邮件搜索支持哪些条件?可以组合使用吗?
A: 支持 `--from`(发件人)、`--subject`(主题)、`--folder`(文件夹)、`--count`(数量)等条件,可组合使用。如 `email-163-com search --from "阿里云" --subject "通知" --count 10`。注意163邮箱IMAP搜索对中文支持有限,若结果异常可放宽条件逐项排查。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 仅支持163邮箱(imap.163.com/smtp.163.com),不兼容其他邮箱服务商
- IMAP搜索对中文发件人/主题支持有限,复杂搜索可能需结合 `read` 浏览定位
- 单邮件附件总大小受163邮箱限制(通常50MB),超大文件建议使用网盘链接
- 配置文件明文存储授权码,需手动设置文件权限(600)保护
- 邮件移动依赖IMAP COPY+STORE+EXPUNGE,网络中断可能导致状态不一致
- HTML邮件渲染效果取决于收件客户端,不同客户端可能有差异
- 不支持邮件草稿保存与定时发送(需使用网页版或专业邮件客户端)
- IMAP ID默认配置内置,深度自定义需了解RFC 2971规范
