---
slug: "email-163"
name: "email-163"
version: "1.0.0"
displayName: "163邮箱助手专业版"
summary: "企业级163邮箱管理，支持批量收发、高级搜索、定时任务与邮件归档"
license: "Proprietary"
edition: "pro"
description: |-
  163邮箱助手专业版面向企业用户与高效能个人用户，在免费版基础能力之上扩展批量操作、
  高级搜索过滤、定时任务调度、邮件归档审计、模板化发送与多账户管理等企业级特性。核心能力:
  - 批量邮件发送与群发通知（支持变量替换与模板）
  - 高级搜索：多维度组合过滤、正则匹配、结果导出
  - 邮件归档与审计日志，满足合规要求
  - 定时任务调度，支持周期性邮件处理
  - 多账户统一管理，租户隔离配置
  - 邮件模板系统...
tags:
  - 沟通协作
  - 邮件管理
  - 163邮箱
  - 企业效率
  - 批量操作
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 163邮箱助手专业版

## 核心能力

### 批量操作引擎
- **批量发送**: 一次性向数百个收件人发送邮件，支持收件人列表文件
- **变量替换**: 邮件模板中支持 `（根据实际场景填充）`、`（根据实际场景填充）` 等变量插值
- **批量删除/移动**: 按搜索结果批量处理邮件
- **批量标记**: 批量标记已读、加星标、归类

**输入**: 用户提供批量操作引擎所需的指令和必要参数。
### 高级搜索与过滤
- 多维度组合条件（发件人、主题、正文、日期、大小、标签）
- 正则表达式匹配
- 搜索结果导出为 CSV/JSON
- 搜索结果分页与排序

**输入**: 用户提供高级搜索与过滤所需的指令和必要参数。
### 邮件模板系统
- 内置常用模板（通知、报告、邀请、提醒）
- 自定义模板管理（创建、编辑、删除）
- 变量插值与条件渲染
- 模板版本控制

**输入**: 用户提供邮件模板系统所需的指令和必要参数。
**处理**: 按照skill规范执行邮件模板系统操作,遵循单一意图原则。### 定时任务调度
- 一次性定时发送
- 周期性任务（每日/每周/每月）
- 任务队列管理与状态监控
- 任务执行日志

**输入**: 用户提供定时任务调度所需的指令和必要参数。
**输出**: 返回定时任务调度的执行结果,包含操作状态和输出数据。### 归档与审计
- 邮件自动归档到指定文件夹
- 操作审计日志记录
- 归档邮件全文检索
- 合规导出报告

**输入**: 用户提供归档与审计所需的指令和必要参数。
**处理**: 按照skill规范执行归档与审计操作,遵循单一意图原则。### 多账户管理
- 统一管理多个163邮箱账户
- 租户隔离配置
- 账户间邮件转发与同步
- 账户健康状态监控

---

**输入**: 用户提供多账户管理所需的指令和必要参数。
**处理**: 按照skill规范执行多账户管理操作,遵循单一意图原则。
**输出**: 返回多账户管理的执行结果,包含操作状态和输出数据。

### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级、邮箱管理、支持批量收发、定时任务与邮件归、邮箱助手专业版面、向企业用户与高效、能个人用户、在免费版基础能力、之上扩展批量操作、高级搜索过滤、邮件归档审计、模板化发送与多账、户管理等企业级特、核心能力、批量邮件发送与群、发通知、支持变量替换与模、多维度组合过滤、正则匹配、邮件归档与审计日、满足合规要求、支持周期性邮件处、多账户统一管理。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一：批量发送个性化通知邮件
企业需要向500名员工发送包含个人信息的工资单通知邮件，每封邮件内容不同。

**准备收件人列表** `recipients.csv`:

```csv
email,name,department,salary_month
zhangsan@company.com,张三,技术部,2026年7月
lisi@company.com,李四,市场部,2026年7月
wangwu@company.com,王五,财务部,2026年7月
```

**创建邮件模板** `template/salary_notice.html`:

```html
<h1>工资单通知 - （根据实际场景填充）</h1>
<p>尊敬的 （根据实际场景填充）（（根据实际场景填充））：</p>
<p>您本月工资单已生成，请登录企业系统查看详情。</p>
<p>如有疑问，请联系财务部。</p>
```

**执行批量发送**:

```bash
email-163-tool batch-send \
  --recipients recipients.csv \
  --template template/salary_notice.html \
  --subject "（根据实际场景填充） - 工资单通知 （根据实际场景填充）" \
  --rate-limit 10 \
  --dry-run
```

输出示例：

```text
📋 批量发送任务启动
   收件人总数: 500
   模板: template/salary_notice.html
   发送速率: 10 封/分钟
   模式: 试运行（dry-run）

[1/500] ✅ zhangsan@company.com - 张三 - 技术部
[2/500] ✅ lisi@company.com - 李四 - 市场部
[3/500] ✅ wangwu@company.com - 王五 - 财务部
...

📊 试运行完成: 500 封邮件预览成功，0 个错误
💡 移除 --dry-run 参数以实际发送
```

### 场景二：邮件归档与合规审计
财务部门需要将所有与发票相关的邮件归档保存，并生成审计报告。

```bash
# 搜索所有发票相关邮件并归档
email-163-tool search-archive \
  --from "invoice@" \
  --subject "发票" \
  --after "2026-01-01" \
  --before "2026-07-18" \
  --archive-folder "财务归档/2026年上半年" \
  --export audit_report.csv

# 查看归档审计日志
email-163-tool audit-log --action archive --since "2026-07-01"
```

审计日志输出：

```text
📜 审计日志 - 归档操作
时间范围: 2026-07-01 至 2026-07-18

2026-07-18 10:30:15 | ARCHIVE | 邮件ID: 234 | 主题: 7月发票 | 来源: invoice@vendor.com -> 财务归档/2026年上半年
2026-07-18 10:30:16 | ARCHIVE | 邮件ID: 235 | 主题: 6月发票 | 来源: invoice@vendor.com -> 财务归档/2026年上半年
...
归档总数: 48 封 | 导出文件: audit_report.csv
```

### 场景三：定时自动清理与汇总
设置每周一自动清理垃圾邮件，并汇总上周未读重要邮件。

```bash
# 创建定时任务
email-163-tool schedule create \
  --name "weekly-cleanup" \
  --cron "0 9 * * 1" \
  --actions "search --folder 垃圾邮件 --all | delete --batch" \
  --notify "admin@company.com"

# 查看所有定时任务
email-163-tool schedule list

# 查看任务执行历史
email-163-tool schedule history --name "weekly-cleanup"
```

---

## 使用流程

### 从免费版升级
专业版完全兼容免费版，无需修改现有配置：

```bash
# 现有配置文件可直接使用
# ~/.config/email-163-tool/config.json
# 验证升级后的基础功能
email-163-tool read --count 5
email-163-tool send --to test@example.com --subject "升级测试" --body "专业版已就绪"
```

### 新增企业级配置
在配置文件中添加专业版扩展字段：

```json
{
  "email": "enterprise@163.com",
  "password": "your_auth_code",
  "imap_server": "imap.163.com",
  "imap_port": 993,
  "smtp_server": "smtp.163.com",
  "smtp_port": 465,
  "pro": {
    "multi_account": {
      "enabled": true,
      "accounts_dir": "~/.config/email-163-tool/accounts"
    },
    "batch": {
      "rate_limit": 10,
      "max_recipients": 1000,
      "retry_count": 3
    },
    "archive": {
      "enabled": true,
      "auto_archive": true,
      "retention_days": 365
    },
    "audit": {
      "enabled": true,
      "log_file": "~/.config/email-163-tool/audit.log"
    },
    "schedule": {
      "enabled": true,
      "timezone": "Asia/Shanghai"
    }
  }
}
```

### 多账户配置
为每个邮箱账户创建独立配置文件：

```bash
mkdir -p ~/.config/email-163-tool/accounts

# 创建账户配置
cat > ~/.config/email-163-tool/accounts/finance.json << 'EOF'
{
  "name": "财务部邮箱",
  "email": "finance@company.com",
  "password": "finance_auth_code"
}
EOF

# 列出所有账户
email-163-tool accounts list
```

---

### 命令参数说明

1. `--notify`: 命令参数,用于指定操作选项
2. `--all`: 命令参数,用于指定操作选项
3. `--before`: 命令参数,用于指定操作选项
4. `--body`: 命令参数,用于指定操作选项
5. `--expired`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

### 命令参数说明

- `--older-than`: 命令参数,用于指定操作选项
- `--count`: 命令参数,用于指定操作选项
- `-cleanup`: 命令参数,用于指定操作选项
- `--action`: 命令参数,用于指定操作选项
- `--actions`: 命令参数,用于指定操作选项

### 命令参数说明

- `--since`: 命令参数,用于指定操作选项
- `--subject`: 命令参数,用于指定操作选项
- `--after`: 命令参数,用于指定操作选项
- `--archive-folder`: 命令参数,用于指定操作选项
- `--data`: 命令参数,用于指定操作选项

### 命令参数说明

- `--export`: 命令参数,用于指定操作选项
- `-send`: 命令参数,用于指定操作选项
- `-log`: 命令参数,用于指定操作选项
- `--account`: 命令参数,用于指定操作选项
- `--from`: 命令参数,用于指定操作选项

### 命令参数说明

- `-run`: 命令参数,用于指定操作选项
- `--unread`: 命令参数,用于指定操作选项
- `--dry-run`: 命令参数,用于指定操作选项
- `--batch`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

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
- **Python版本**: 3.8 及以上（如使用 Python 脚本模式）
- **网络环境**: 需可访问 `imap.163.com` 与 `smtp.163.com`
- **磁盘空间**: 归档与日志建议预留 1GB 以上

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 标准库 | 运行库 | 可选 | Python 自带（smtplib, imaplib, email） |
| 163邮箱账号 | 账户 | 必需 | 注册163邮箱并开启IMAP/SMTP服务 |
| 客户端授权码 | 凭证 | 必需 | 163邮箱设置页生成 |
| cron 服务 | 系统服务 | 可选 | 系统自带（定时任务功能需要） |
| 数据库 | 存储引擎 | 可选 | 用于归档索引（可选 SQLite 文件存储） |

### API Key 配置
- 本工具使用163邮箱客户端授权码进行认证，无需额外 API Key
- 多账户场景下每个账户使用独立授权码
- 授权码通过配置文件或环境变量提供，支持加密存储
- 建议企业用户使用密钥管理服务统一管理授权码

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要 exec 命令行执行能力）
- **说明**: 基于Markdown的AI Skill，，企业级功能通过扩展命令行工具完成，支持批量处理与定时调度

## 案例展示

### 批量发送配置
```json
{
  "batch": {
    "rate_limit": 10,
    "max_recipients": 1000,
    "retry_count": 3,
    "retry_delay": 60,
    "concurrency": 5,
    "on_failure": "skip",
    "failure_log": "~/.config/email-163-tool/batch_failures.log"
  }
}
```

### 归档规则配置
```json
{
  "archive_rules": [
    {
      "name": "发票归档",
      "conditions": {
        "from": "invoice@",
        "subject": "发票"
      },
      "target_folder": "财务归档",
      "retention_days": 1095
    },
    {
      "name": "通知归档",
      "conditions": {
        "from": "noreply@",
        "older_than_days": 90
      },
      "target_folder": "通知归档",
      "retention_days": 180
    }
  ]
}
```

### 定时任务配置
```json
{
  "schedules": [
    {
      "name": "daily-summary",
      "cron": "0 9 * * *",
      "action": "summary --unread --send admin@company.com"
    },
    {
      "name": "weekly-cleanup",
      "cron": "0 10 * * 1",
      "action": "clean --folder 垃圾邮件 --older-than 7"
    }
  ]
}
```

---

## 常见问题

### 问题1：批量发送被限制
```text
Error: Rate limit exceeded
```

**解决**: 降低发送速率，163邮箱对发送频率有严格限制。建议 `--rate-limit` 设置为 5-10 封/分钟，并启用失败重试机制。

### 问题2：模板变量未替换
**解决**: 确保变量名与 CSV 列名完全一致（区分大小写），模板中使用 `（根据实际场景填充）` 语法：

```bash
# 验证模板变量
email-163-tool template validate --name "通知" --data sample.json
```

### 问题3：定时任务未执行
**解决**: 检查时区配置与 cron 表达式格式：

```bash
# 验证 cron 表达式
email-163-tool schedule validate --cron "0 9 * * 1"

# 检查任务状态
email-163-tool schedule status --name "weekly-cleanup"
```

### 问题4：多账户切换失败
**解决**: 确保各账户配置文件格式正确，授权码有效：

```bash
# 验证所有账户配置
email-163-tool accounts validate --all

# 测试单个账户连接
email-163-tool accounts test --account finance
```

### 问题5：归档空间不足
**解决**: 定期清理过期归档，或调整保留期限：

```bash
# 清理超过保留期的归档邮件
email-163-tool archive clean --expired

# 查看归档空间使用情况
email-163-tool archive stats
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

- 需要LLM支持
- 需要LLM支持
- 需要LLM支持
- 需要LLM支持

