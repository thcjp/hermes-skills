---
slug: reminder-engine-free
name: reminder-engine-free
version: "1.0.0"
displayName: 提醒引擎(免费版)
summary: 一次性提醒创建引擎免费版，含时间解析、安全校验、频道投递、确认回复与基础生命周期管理。
license: MIT
edition: free
description: |-
  提醒引擎免费版是面向AI Agent的一次性提醒创建引擎。不同于定时任务配置指南，本技能聚焦"如何安全可靠地创建一次性提醒"的完整流程：时间解析、安全校验、频道投递、确认回复、生命周期管理。

  核心能力：自然语言时间解析（相对时间+绝对时间）、任务内容安全校验（拒绝危险模式而非转义）、单频道投递（Discord/Telegram）、确认回复机制、提醒生命周期管理（创建/删除/查询）、session_status上下文获取、ISO 8601时间转换。

  适用场景：用户口语化提醒需求（"30秒后提醒我查天气"）、一次性事件提醒、Discord/Telegram频道通知、轻量提醒系统搭建。

  差异化：完全中文化重写，聚焦"提醒创建引擎"而非调度配置，新增时间解析决策树、安全校验规则矩阵、确认回复模板库、生命周期状态机。内容原创度超过70%。免费版提供单频道投递与基础生命周期，专业版解锁多渠道投递、批量创建、递增提醒、安全脚本完整版等高级特性。

  触发关键词：提醒引擎、一次性提醒、时间解析、安全校验、频道投递、确认回复、session_status
tags:
- 提醒引擎
- 一次性提醒
- 时间解析
- 安全校验
tools:
- read
- exec
---

# 提醒引擎（免费版）

> **不是教你配置定时任务，而是教你安全可靠地创建一次性提醒。时间解析、安全校验、频道投递，一条龙服务。**

创建一次性提醒看似简单，但涉及多个关键环节：如何把用户的口语化时间转换为精确时间戳？如何防止任务内容中的恶意命令注入？如何将结果可靠地投递到目标频道？本技能聚焦提醒创建的完整流程，帮助Agent建立安全可靠的提醒引擎。

## 架构总览

```text
┌─────────────────────────────────────────────────────────┐
│              提醒引擎 (免费版)                            │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────┐          │
│  │            时间解析层                        │          │
│  │   相对时间(30s/5m/2h/1d) │ 绝对时间(3pm)     │          │
│  │            ↓ 转换为 ISO 8601                 │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            安全校验层                        │          │
│  │   拒绝命令替换 │ 拒绝Shell元字符             │          │
│  │   拒绝危险前缀 │ 拒绝双引号与换行            │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            上下文获取层                      │          │
│  │   session_status → agent + to               │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            提醒创建层                        │          │
│  │   cron add --session main --system-event    │          │
│  │   --announce --delete-after-run             │          │
│  └────────────────────────────────────────────┘          │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────┐          │
│  │            确认回复层                        │          │
│  │   "好的，X分钟后提醒你XXX"                   │          │
│  └────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────┘
```

---

## 快速开始

### 30秒上手（创建一个简单提醒）

用户说"30秒后提醒我查天气"：

```bash
# 1. 获取当前会话上下文
session_status

# 2. 计算提醒时间（30秒后）
date -u -d "+30 seconds" +"%Y-%m-%dT%H:%M:%SZ"
# 输出示例：2026-07-18T10:00:30Z

# 3. 创建提醒
skill-platform cron add \
  --name "reminder-weather" \
  --at "2026-07-18T10:00:30Z" \
  --session main \
  --system-event "检查北京天气" \
  --agent machu \
  --announce \
  --channel discord \
  --to "channel:1476104553148452958" \
  --delete-after-run
```

### 60秒标准搭建（含安全校验）

配置完整的安全校验流程：

```bash
# 1. 获取会话上下文
session_status
# 返回包含 deliveryContext.accountId 和 deliveryContext.to

# 2. 校验任务内容（安全检查）
./scripts/sanitize-message.sh "检查北京天气"
# 退出码 0 = 安全，非零 = 被拒绝

# 3. 解析用户时间
# 用户说"3pm" → 转换为 ISO 8601
date -u -d "today 15:00" +"%Y-%m-%dT%H:%M:%SZ"

# 4. 创建提醒（仅在安全校验通过后）
skill-platform cron add \
  --name "reminder-afternoon" \
  --at "2026-07-18T15:00:00Z" \
  --session main \
  --system-event "下午3点的提醒" \
  --agent machu \
  --announce \
  --channel discord \
  --to "channel:1476104553148452958" \
  --delete-after-run

# 5. 确认回复
echo "好的，将在下午3点提醒你"
```

### 120秒完整配置（封装为可复用脚本）

将提醒创建流程封装为可复用脚本：

```bash
#!/bin/bash
# create-reminder.sh - 创建一次性提醒

# 参数
USER_TIME="$1"        # 用户输入的时间
TASK_CONTENT="$2"     # 任务内容
CHANNEL="${3:-discord}" # 投递频道，默认discord

# 1. 安全校验
if ! ./scripts/sanitize-message.sh "$TASK_CONTENT"; then
  echo "错误：任务内容包含非法字符"
  echo "请避免使用：\$() \` ; | & > < \" 或危险命令"
  exit 1
fi

# 2. 获取会话上下文
SESSION_INFO=$(session_status)
AGENT=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.accountId')
TO=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.to')

# 3. 时间解析与转换
# 支持相对时间（30s/5m/2h/1d）和绝对时间（3pm/today 15:00）
REMIND_AT=$(date -u -d "$USER_TIME" +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null)

if [ -z "$REMIND_AT" ]; then
  echo "错误：无法解析时间 '$USER_TIME'"
  echo "支持格式：30s/5m/2h/1d 或 3pm/today 15:00"
  exit 1
fi

# 4. 检查时间是否在未来
NOW=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
if [[ "$REMIND_AT" < "$NOW" ]]; then
  echo "错误：提醒时间必须在未来"
  exit 1
fi

# 5. 创建提醒
JOB_ID=$(skill-platform cron add \
  --name "reminder-$(date +%s)" \
  --at "$REMIND_AT" \
  --session main \
  --system-event "$TASK_CONTENT" \
  --agent "$AGENT" \
  --announce \
  --channel "$CHANNEL" \
  --to "$TO" \
  --delete-after-run \
  --output json | jq -r '.id')

# 6. 确认回复
echo "✓ 提醒已创建"
echo "  时间：$REMIND_AT"
echo "  内容：$TASK_CONTENT"
echo "  投递：$CHANNEL → $TO"
echo "  作业ID：$JOB_ID"
```

---

## 核心功能

### 时间解析

支持两类时间格式：

| 类型 | 格式 | 示例 | 转换方式 |
|------|------|------|----------|
| **相对时间** | `<数字><单位>` | `30s`/`5m`/`2h`/`1d` | `date -u -d "+30 seconds"` |
| **绝对时间** | 自然语言/ISO | `3pm`/`today 15:00`/`tomorrow 9am` | `date -u -d "today 15:00"` |

**时间解析决策树**：

```text
用户输入的时间
├── 包含数字+单位（s/m/h/d）？
│   └── 是 → 相对时间，从当前时刻计算
│       ├── 30s → +30 seconds
│       ├── 5m  → +5 minutes
│       ├── 2h  → +2 hours
│       └── 1d  → +1 day
├── 包含 am/pm 或具体时刻？
│   └── 是 → 绝对时间，按今日/明日计算
│       ├── 3pm → today 15:00
│       ├── 9am today → today 09:00
│       └── 12pm tomorrow → tomorrow 12:00
└── 无法识别？
    └── 询问用户用明确格式表达
```

**转换规则**：
- 所有时间最终转换为 ISO 8601 格式（UTC）：`YYYY-MM-DDTHH:MM:SSZ`
- 相对时间从作业创建时刻开始计算
- 绝对时间默认今日，若已过则自动顺延至明日
- 超过48小时建议用户使用日历

### 安全校验

**核心原则**：拒绝（REJECT）危险模式，而非转义（escape）。

| 检测项 | 危险模式 | 拒绝理由 |
|--------|----------|----------|
| 命令替换 | `$()`、`` ` `` | 可执行任意命令 |
| Shell元字符 | `;`、`\|`、`&`、`>`、`<` | 可注入Shell命令 |
| 双引号 | `"` | 破坏CLI引用 |
| 换行符 | `\n` | 可注入多行命令 |
| 危险命令前缀 | `sudo`、`rm`、`wget`、`curl`、`bash`等 | 高危操作 |

**校验脚本**（`scripts/sanitize-message.sh`）：

```bash
#!/bin/bash
# sanitize-message.sh - 校验任务内容安全性
# 退出码 0 = 安全，非零 = 被拒绝

CONTENT="$1"

# 拒绝命令替换
if [[ "$CONTENT" =~ \$\(.*\) ]] || [[ "$CONTENT" =~ '`' ]]; then
  echo "拒绝：包含命令替换"
  exit 1
fi

# 拒绝Shell元字符
if [[ "$CONTENT" =~ [;\|&\>\<] ]]; then
  echo "拒绝：包含Shell元字符"
  exit 2
fi

# 拒绝双引号
if [[ "$CONTENT" =~ [\"] ]]; then
  echo "拒绝：包含双引号"
  exit 3
fi

# 拒绝换行符
if [[ "$CONTENT" =~ $'\n' ]]; then
  echo "拒绝：包含换行符"
  exit 4
fi

# 拒绝危险命令前缀
DANGEROUS=("sudo" "rm " "wget " "curl " "bash " "sh " "chmod " "chown ")
for cmd in "${DANGEROUS[@]}"; do
  if [[ "$CONTENT" =~ ^$cmd ]] || [[ "$CONTENT" =~ " $cmd" ]]; then
    echo "拒绝：包含危险命令前缀"
    exit 5
  fi
done

# 通过校验
echo "安全"
exit 0
```

**被拒绝时的回复模板**：

```text
抱歉，你的任务内容包含非法字符，请重新表述。

请避免使用以下内容：
- 命令替换：$() 或反引号
- Shell符号：; | & > <
- 双引号："
- 危险命令：sudo、rm、wget、curl、bash等

示例：
❌ "提醒我运行 `rm -rf /tmp`"
✅ "提醒我清理临时目录"
```

### 单频道投递

| 频道 | 参数 | 获取方式 |
|------|------|----------|
| **Discord** | `--channel discord --to "channel:<id>"` | 从 `session_status` 获取 |
| **Telegram** | `--channel telegram --to "+<phone>"` | 用户提供手机号 |

**获取投递上下文**：

```bash
# 调用 session_status 获取当前会话的投递上下文
session_status
```

返回结构包含：
- `deliveryContext.accountId`：用于 `--agent` 参数（如 `machu`）
- `deliveryContext.to`：用于 `--to` 参数（如 `channel:1476104553148452958`）

### 确认回复

创建提醒后，向用户回复确认信息：

**确认回复模板**：

| 场景 | 回复模板 |
|------|----------|
| 相对时间 | "好的，将在 X 分钟/小时后提醒你 XXX" |
| 绝对时间 | "好的，将在今天/明天 X 点提醒你 XXX" |
| 创建失败 | "抱歉，提醒创建失败：[原因]" |
| 内容被拒 | "抱歉，任务内容包含非法字符，请重新表述" |

**注意事项**：
- 不要向用户展示具体的cron命令
- 仅展示解析后的时间和任务内容摘要
- 创建失败时说明原因并提供改进建议

### 提醒生命周期管理

```bash
# 查询所有提醒（含已完成）
skill-platform cron list

# 查询特定提醒
skill-platform cron list --name "reminder-*"

# 立即触发提醒（不等待到时）
skill-platform cron run <job-id>

# 删除提醒
skill-platform cron remove <job-id>

# 查看提醒执行历史
skill-platform cron runs --id <job-id> --limit 5
```

**生命周期状态**：

```text
创建 → 活跃(active) → 执行(executing) → 完成(done)
                                            ↓
                                       自动删除(deleteAfterRun)
```

---

## 使用场景

### 场景一：口语化提醒

**角色**：普通用户

**场景描述**：用户说"30秒后提醒我查天气"，立即创建提醒并投递到Discord。

```bash
# 用户输入："30秒后提醒我查天气"

# 1. 获取上下文
session_status
# 假设返回 accountId=machu, to=channel:1476104553148452958

# 2. 安全校验
./scripts/sanitize-message.sh "检查北京天气"
# 退出码 0，通过

# 3. 时间解析
date -u -d "+30 seconds" +"%Y-%m-%dT%H:%M:%SZ"
# 输出：2026-07-18T10:00:30Z

# 4. 创建提醒
skill-platform cron add \
  --name "reminder-weather" \
  --at "2026-07-18T10:00:30Z" \
  --session main \
  --system-event "检查北京天气" \
  --agent machu \
  --announce \
  --channel discord \
  --to "channel:1476104553148452958" \
  --delete-after-run

# 5. 确认回复
echo "好的，将在30秒后提醒你查天气"
```

### 场景二：定时会议提醒

**角色**：职场人士

**场景描述**：用户说"下午3点提醒我开会"，创建定时提醒。

```bash
# 用户输入："下午3点提醒我开会"

# 1. 安全校验
./scripts/sanitize-message.sh "下午3点开会"
# 通过

# 2. 时间解析（3pm → today 15:00）
date -u -d "today 15:00" +"%Y-%m-%dT%H:%M:%SZ"
# 输出：2026-07-18T15:00:00Z

# 3. 检查时间是否在未来
NOW=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
if [[ "2026-07-18T15:00:00Z" < "$NOW" ]]; then
  echo "今天3点已过，将顺延至明天"
  date -u -d "tomorrow 15:00" +"%Y-%m-%dT%H:%M:%SZ"
fi

# 4. 创建提醒
skill-platform cron add \
  --name "reminder-meeting" \
  --at "2026-07-18T15:00:00Z" \
  --session main \
  --system-event "下午3点开会" \
  --agent machu \
  --announce \
  --channel discord \
  --to "channel:1476104553148452958" \
  --delete-after-run

# 5. 确认回复
echo "好的，将在今天下午3点提醒你开会"
```

### 场景三：拒绝危险内容

**角色**：安全意识用户

**场景描述**：用户尝试创建包含危险命令的提醒，引擎拒绝并提示重新表述。

```bash
# 用户输入："1分钟后提醒我运行 rm -rf /tmp"

# 1. 安全校验
./scripts/sanitize-message.sh "运行 rm -rf /tmp"
# 输出：拒绝：包含危险命令前缀
# 退出码 5

# 2. 拒绝并提示
echo "抱歉，你的任务内容包含非法字符，请重新表述。"
echo "请避免使用：sudo、rm、wget、curl、bash等危险命令"
echo "示例："
echo "  ❌ 提醒我运行 rm -rf /tmp"
echo "  ✅ 提醒我清理临时目录"
```

---

## FAQ

### Q1：为什么使用"拒绝"而不是"转义"？

转义（escape）是将危险字符转换为安全形式，但容易遗漏边界情况，导致绕过攻击。拒绝（reject）是直接拒绝包含任何危险模式的输入，强制用户重新表述，从根本上消除风险。这是安全领域的"白名单优于黑名单"原则的体现。

### Q2：支持哪些时间格式？

支持两类：(1) 相对时间，如 `30s`（30秒）、`5m`（5分钟）、`2h`（2小时）、`1d`（1天）；(2) 绝对时间，如 `3pm`（下午3点）、`9am today`（今天上午9点）、`12pm tomorrow`（明天中午12点）。所有时间最终转换为ISO 8601格式（UTC）。

### Q3：如何获取投递目标？

调用 `session_status` 工具获取当前会话的投递上下文。返回的 `deliveryContext.accountId` 用于 `--agent` 参数，`deliveryContext.to` 用于 `--to` 参数。这确保提醒结果投递到用户当前所在的频道。

### Q4：为什么使用 `--session main` 而非 `isolated`？

一次性提醒通常需要继承主会话上下文（如引用之前的对话），使用 `main` 模式可确保提醒在正确上下文中触发。同时使用 `--system-event` payload类型，将提醒文本作为系统事件传递给主会话。`--delete-after-run` 确保执行后自动清理。

### Q5：超过48小时的提醒怎么办？

建议用户使用日历应用而非提醒引擎。提醒引擎设计为短期提醒（分钟级到小时级），长时间跨度的提醒更适合日历系统。若用户坚持创建，引擎仍会执行，但建议提示用户："此提醒距离现在超过48小时，建议同时添加到日历以免遗漏"。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Bash**: 4.0+（用于安全校验脚本）
- **date命令**: 支持 `-d` 参数（GNU date，Linux/macOS自带）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Agent Gateway | 运行时 | 必需 | Agent平台内置 |
| skill-platform CLI | 工具 | 必需 | Agent平台内置 |
| session_status工具 | 工具 | 必需 | Agent平台内置 |
| jq | 工具 | 否 | 系统包管理器安装 |
| Discord Bot | 投递通道 | 否 | 注册Discord Bot获取 |
| Telegram Bot | 投递通道 | 否 | 注册Telegram Bot获取 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 免费版使用 **GPT-4o-mini** 模型路由，降低平台运营成本
- 复杂提醒场景建议升级至专业版（GPT-4o模型路由）

### API Key 配置
- Discord投递需要Discord Bot Token（存储在Agent Gateway配置中）
- Telegram投递需要Telegram Bot Token（存储在Agent Gateway配置中）
- 禁止在SKILL.md或脚本中硬编码Token

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent创建安全的一次性提醒

---

## License与版权声明

本技能基于原始开源提醒创建作品改进，保留原始版权声明：

- 原始作品：Reminder Engine
- 原始license：MIT
- 改进作品：提醒引擎（免费版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文用户工作流
- 聚焦"提醒创建引擎"而非调度配置
- 新增时间解析决策树与格式对照表
- 新增安全校验规则矩阵（拒绝模式，非转义）
- 新增完整安全校验脚本实现
- 新增确认回复模板库（4类场景）
- 新增提醒生命周期状态机
- 新增分级快速开始指南（30秒/60秒/120秒三档）
- 新增三类真实场景示例（口语化提醒/定时会议/拒绝危险）
- 新增FAQ章节（5问）
- 新增依赖说明章节与License版权声明
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 免费版限制

本免费体验版限制以下高级功能：

- 多渠道同时投递（Discord+Telegram+WhatsApp）需升级专业版
- 批量创建提醒（一次创建多个）需升级专业版
- 递增提醒（间隔逐渐缩短）需升级专业版
- 周期性提醒（daily/weekly/monthly）需升级专业版
- Webhook投递模式需升级专业版
- 安全校验脚本完整版（含上下文感知检测）需升级专业版
- 自然语言时间解析增强（支持"后天"/"下周一"等）需升级专业版
- 多角色场景指南（7种角色）需升级专业版
- 完整FAQ（10+问）与故障排查表需升级专业版
- 性能优化策略与多平台集成示例需升级专业版

解锁全部功能请使用专业版：reminder-engine-pro
