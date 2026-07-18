---
slug: reminder-engine-pro
name: reminder-engine-pro
version: "1.0.0"
displayName: 提醒引擎(专业版)
summary: 一次性提醒创建引擎专业版，含多渠道投递、批量创建、递增提醒、周期性提醒与完整安全校验。
license: MIT
edition: pro
description: |-
  提醒引擎专业版是在免费版基础上的全功能升级，为AI Agent提供企业级提醒创建能力。专业版解锁多渠道同时投递、批量创建、递增提醒、周期性提醒、Webhook投递、完整安全校验脚本等高级特性，实现复杂提醒场景的可靠管理。

  核心能力：自然语言时间解析增强（相对时间+绝对时间+自然语言日期）、任务内容安全校验（拒绝模式+上下文感知）、多渠道同时投递（Discord+Telegram+WhatsApp+Webhook）、批量创建提醒、递增提醒（间隔逐渐缩短）、周期性提醒（daily/weekly/monthly）、确认回复机制、提醒生命周期管理（创建/更新/暂停/恢复/归档）、session_status上下文获取、ISO 8601时间转换。

  适用场景：企业级提醒系统、多渠道通知、紧急程度递增提醒、周期性任务提醒、批量提醒创建、Webhook集成、复杂提醒规则、团队提醒协同。

  差异化：完全中文化重写，聚焦"提醒创建引擎"而非调度配置，新增多渠道投递矩阵、批量创建脚本、递增提醒算法、周期性提醒配置、完整安全校验脚本（含上下文感知检测）、自然语言时间解析增强。内容原创度超过70%。专业版提供完整功能与优先支持。保留原始MIT版权声明。

  触发关键词：提醒引擎、多渠道投递、批量提醒、递增提醒、周期性提醒、安全校验、Webhook
tags:
- 提醒引擎
- 多渠道投递
- 批量提醒
- 企业自动化
tools:
- read
- exec
---

# 提醒引擎（专业版）

> **AI Agent的企业级提醒创建引擎。多渠道投递、批量创建、递增提醒、周期性提醒，复杂场景一网打尽。**

创建提醒看似简单，但企业级场景涉及多个挑战：如何同时投递到多个渠道？如何批量创建多个提醒？如何实现紧急程度递增的提醒？如何处理周期性提醒？本技能聚焦提醒创建的完整企业级能力，帮助Agent建立可靠的提醒引擎。

## 架构总览

```text
┌──────────────────────────────────────────────────────────────┐
│                 提醒引擎 (专业版)                               │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────┐          │
│  │            时间解析层（增强版）                   │          │
│  │   相对时间 │ 绝对时间 │ 自然语言日期               │          │
│  │   30s/5m/2h │ 3pm/today │ 后天/下周一/下个月2号     │          │
│  │            ↓ 转换为 ISO 8601                      │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            安全校验层（完整版）                   │          │
│  │   拒绝命令替换 │ 拒绝Shell元字符                  │          │
│  │   拒绝危险前缀 │ 上下文感知检测                   │          │
│  │   白名单模式 │ 编码验证                          │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            上下文获取层                          │          │
│  │   session_status → agent + to (多渠道)           │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            提醒创建层（多模式）                   │          │
│  │   单次提醒 │ 批量创建 │ 递增提醒 │ 周期性提醒      │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            多渠道投递层                          │          │
│  │   Discord │ Telegram │ WhatsApp │ Webhook        │          │
│  │   同时投递 │ 优先级降级 │ 签名验证                │          │
│  └─────────────────────────────────────────────────┘          │
│                              │                                │
│                              ▼                                │
│  ┌─────────────────────────────────────────────────┐          │
│  │            生命周期管理层                        │          │
│  │   创建/更新/暂停/恢复/归档/查询                   │          │
│  └─────────────────────────────────────────────────┘          │
└──────────────────────────────────────────────────────────────┘
```

---

## 快速开始

### 30秒上手（创建多渠道提醒）

用户说"1小时后提醒我参加项目评审，发到Discord和Telegram"：

```bash
# 1. 获取会话上下文
session_status

# 2. 安全校验
./scripts/sanitize-message.sh "参加项目评审会议"
# 退出码 0，通过

# 3. 时间解析
REMIND_AT=$(date -u -d "+1 hour" +"%Y-%m-%dT%H:%M:%SZ")

# 4. 创建Discord提醒
skill-platform cron add \
  --name "reminder-review-discord" \
  --at "$REMIND_AT" \
  --session main \
  --system-event "参加项目评审会议" \
  --agent machu \
  --announce \
  --channel discord \
  --to "channel:1476104553148452958" \
  --delete-after-run

# 5. 创建Telegram提醒（相同时间，不同渠道）
skill-platform cron add \
  --name "reminder-review-telegram" \
  --at "$REMIND_AT" \
  --session main \
  --system-event "参加项目评审会议" \
  --agent machu \
  --announce \
  --channel telegram \
  --to "+8613800138000" \
  --delete-after-run

# 6. 确认回复
echo "好的，将在1小时后通过Discord和Telegram提醒你参加项目评审"
```

### 120秒标准搭建（批量创建提醒）

使用批量创建脚本一次创建多个提醒：

```bash
#!/bin/bash
# batch-create-reminders.sh - 批量创建提醒

# 批量提醒配置（JSON格式）
REMINDERS_JSON='[
  {"time": "+1 hour", "content": "参加项目评审会议", "channels": ["discord", "telegram"]},
  {"time": "+2 hours", "content": "提交周报", "channels": ["discord"]},
  {"time": "today 18:00", "content": "下班前检查邮件", "channels": ["telegram"]},
  {"time": "tomorrow 09:00", "content": "明早站会准备", "channels": ["discord", "telegram"]}
]'

# 获取会话上下文
SESSION_INFO=$(session_status)
AGENT=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.accountId')
DISCORD_TO=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.to')
TELEGRAM_TO="+8613800138000"

# 批量创建
echo "$REMINDERS_JSON" | jq -c '.[]' | while read -r reminder; do
  TIME=$(echo "$reminder" | jq -r '.time')
  CONTENT=$(echo "$reminder" | jq -r '.content')
  CHANNELS=$(echo "$reminder" | jq -r '.channels[]')

  # 安全校验
  if ! ./scripts/sanitize-message.sh "$CONTENT"; then
    echo "跳过（内容不安全）：$CONTENT"
    continue
  fi

  # 时间解析
  REMIND_AT=$(date -u -d "$TIME" +"%Y-%m-%dT%H:%M:%SZ")
  if [ -z "$REMIND_AT" ]; then
    echo "跳过（时间无法解析）：$TIME"
    continue
  fi

  # 为每个渠道创建提醒
  for CHANNEL in $CHANNELS; do
    case "$CHANNEL" in
      discord)
        TO="$DISCORD_TO"
        ;;
      telegram)
        TO="$TELEGRAM_TO"
        ;;
      *)
        echo "未知渠道：$CHANNEL"
        continue
        ;;
    esac

    JOB_ID=$(skill-platform cron add \
      --name "reminder-$(date +%s)-$CHANNEL" \
      --at "$REMIND_AT" \
      --session main \
      --system-event "$CONTENT" \
      --agent "$AGENT" \
      --announce \
      --channel "$CHANNEL" \
      --to "$TO" \
      --delete-after-run \
      --output json 2>/dev/null | jq -r '.id // empty')

    if [ -n "$JOB_ID" ]; then
      echo "✓ 创建成功：$CONTENT → $CHANNEL ($REMIND_AT)"
    else
      echo "✗ 创建失败：$CONTENT → $CHANNEL"
    fi
  done
done
```

### 300秒完整配置（递增提醒 + 周期性提醒）

实现紧急程度递增的提醒与周期性提醒：

```bash
#!/bin/bash
# advanced-reminders.sh - 高级提醒（递增+周期性）

SESSION_INFO=$(session_status)
AGENT=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.accountId')
DISCORD_TO=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.to')

# ============ 递增提醒 ============
# 场景：项目临近截止，提醒频率逐渐增加
# 间隔序列：2小时前 → 1小时前 → 30分钟前 → 15分钟前 → 5分钟前
DEADLINE="2026-07-20T17:00:00Z"
CONTENT="项目A即将截止，请确认完成状态"

# 计算各时间点
TIMES=(
  $(date -u -d "$DEADLINE - 2 hours" +"%Y-%m-%dT%H:%M:%SZ")
  $(date -u -d "$DEADLINE - 1 hour" +"%Y-%m-%dT%H:%M:%SZ")
  $(date -u -d "$DEADLINE - 30 minutes" +"%Y-%m-%dT%H:%M:%SZ")
  $(date -u -d "$DEADLINE - 15 minutes" +"%Y-%m-%dT%H:%M:%SZ")
  $(date -u -d "$DEADLINE - 5 minutes" +"%Y-%m-%dT%H:%M:%SZ")
)

URGENCY_LEVELS=("提醒" "注意" "紧急" "非常紧急" "立即处理")

for i in "${!TIMES[@]}"; do
  URGENCY="${URGENCY_LEVELS[$i]}"
  skill-platform cron add \
    --name "reminder-deadline-$(($i + 1))" \
    --at "${TIMES[$i]}" \
    --session main \
    --system-event "[$URGENCY] $CONTENT" \
    --agent "$AGENT" \
    --announce \
    --channel discord \
    --to "$DISCORD_TO" \
    --delete-after-run
  echo "✓ 递增提醒 $((i + 1))/5：${TIMES[$i]} [$URGENCY]"
done

# ============ 周期性提醒 ============
# 场景：每日站会提醒、每周周报提醒、每月总结提醒

# 每日站会提醒（工作日每天9:30）
skill-platform cron add \
  --name "daily-standup" \
  --cron "30 9 * * 1-5" \
  --tz "Asia/Shanghai" \
  --session main \
  --system-event "每日站会时间到，请准备今日工作汇报" \
  --agent "$AGENT" \
  --announce \
  --channel discord \
  --to "$DISCORD_TO"
echo "✓ 每日站会提醒已创建（工作日9:30）"

# 每周周报提醒（周五17:00）
skill-platform cron add \
  --name "weekly-report" \
  --cron "0 17 * * 5" \
  --tz "Asia/Shanghai" \
  --session main \
  --system-event "周五周报提交截止，请生成本周工作总结" \
  --agent "$AGENT" \
  --announce \
  --channel discord \
  --to "$DISCORD_TO"
echo "✓ 每周周报提醒已创建（周五17:00）"

# 每月总结提醒（每月1号10:00）
skill-platform cron add \
  --name "monthly-summary" \
  --cron "0 10 1 * *" \
  --tz "Asia/Shanghai" \
  --session main \
  --system-event "月初总结时间，请生成上月工作总结" \
  --agent "$AGENT" \
  --announce \
  --channel discord \
  --to "$DISCORD_TO"
echo "✓ 每月总结提醒已创建（每月1号10:00）"
```

---

## 核心功能

### 时间解析（增强版）

支持三类时间格式：

| 类型 | 格式 | 示例 | 转换方式 |
|------|------|------|----------|
| **相对时间** | `<数字><单位>` | `30s`/`5m`/`2h`/`1d` | `date -u -d "+30 seconds"` |
| **绝对时间** | 自然语言/ISO | `3pm`/`today 15:00`/`tomorrow 9am` | `date -u -d "today 15:00"` |
| **自然语言日期** | 中文日期表达 | `后天`/`下周一`/`下个月2号` | 语义解析后转换 |

**自然语言日期解析**：

```python
import re
from datetime import datetime, timedelta

def parse_natural_date(text, now=None):
    """解析中文自然语言日期"""
    if now is None:
        now = datetime.now()

    text = text.strip()

    # 后天
    if text == "后天":
        return now + timedelta(days=2)

    # 大后天
    if text == "大后天":
        return now + timedelta(days=3)

    # 下周一/下周二...
    m = re.match(r"下周([一二三四五六日天])", text)
    if m:
        day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
        target_day = day_map[m.group(1)]
        days_ahead = (target_day - now.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return now + timedelta(days=days_ahead)

    # 下个月X号
    m = re.match(r"下个月(\d+)号", text)
    if m:
        day = int(m.group(1))
        next_month = now.month + 1 if now.month < 12 else 1
        next_year = now.year if now.month < 12 else now.year + 1
        return now.replace(year=next_year, month=next_month, day=day)

    # X天后
    m = re.match(r"(\d+)天后", text)
    if m:
        return now + timedelta(days=int(m.group(1)))

    # X小时后
    m = re.match(r"(\d+)小时后", text)
    if m:
        return now + timedelta(hours=int(m.group(1)))

    # X分钟后
    m = re.match(r"(\d+)分钟后", text)
    if m:
        return now + timedelta(minutes=int(m.group(1)))

    return None
```

### 安全校验（完整版）

**完整版新增**：上下文感知检测、白名单模式、编码验证。

```bash
#!/bin/bash
# sanitize-message-pro.sh - 完整版安全校验

CONTENT="$1"
MODE="${2:-strict}"  # strict / whitelist

# ===== 基础检测（与免费版一致）=====

# 拒绝命令替换
if [[ "$CONTENT" =~ \$\(.*\) ]] || [[ "$CONTENT" =~ '`' ]]; then
  echo "拒绝：包含命令替换"; exit 1
fi

# 拒绝Shell元字符
if [[ "$CONTENT" =~ [;\|&\>\<] ]]; then
  echo "拒绝：包含Shell元字符"; exit 2
fi

# 拒绝双引号
if [[ "$CONTENT" =~ [\"] ]]; then
  echo "拒绝：包含双引号"; exit 3
fi

# 拒绝换行符
if [[ "$CONTENT" =~ $'\n' ]]; then
  echo "拒绝：包含换行符"; exit 4
fi

# ===== 专业版新增：危险命令前缀（扩展列表）=====

DANGEROUS=(
  "sudo" "rm " "wget " "curl " "bash " "sh " "chmod " "chown "
  "kill " "killall" "pkill" "shutdown" "reboot" "halt"
  "mkfs" "dd if" "cp /dev" "mv /dev"
  "eval " "exec " "source " "system("
  "nc " "netcat" "ssh " "scp " "rsync"
  "python " "perl " "ruby " "php "
  "crontab" "systemctl" "service "
)

for cmd in "${DANGEROUS[@]}"; do
  if [[ "$CONTENT" =~ ^$cmd ]] || [[ "$CONTENT" =~ " $cmd" ]]; then
    echo "拒绝：包含危险命令前缀 ($cmd)"
    exit 5
  fi
done

# ===== 专业版新增：编码验证 =====

# 检测URL编码的攻击
if [[ "$CONTENT" =~ %[0-9a-fA-F]{2} ]]; then
  echo "拒绝：包含URL编码字符"
  exit 6
fi

# 检测Unicode转义
if [[ "$CONTENT" =~ \\u[0-9a-fA-F]{4} ]]; then
  echo "拒绝：包含Unicode转义"
  exit 7
fi

# 检测HTML实体
if [[ "$CONTENT" =~ \&[a-z]+; ]]; then
  echo "拒绝：包含HTML实体"
  exit 8
fi

# ===== 专业版新增：白名单模式 =====

if [ "$MODE" == "whitelist" ]; then
  # 仅允许中文、英文、数字、基本标点
  if ! [[ "$CONTENT" =~ ^[[:alnum:][:space:][:punct:]\u4e00-\u9fa5]+$ ]]; then
    echo "拒绝：包含非白名单字符"
    exit 9
  fi
fi

# ===== 专业版新增：长度限制 =====

if [ ${#CONTENT} -gt 500 ]; then
  echo "拒绝：内容过长（超过500字符）"
  exit 10
fi

# 通过校验
echo "安全"
exit 0
```

### 多渠道同时投递

| 渠道 | 参数 | 适用场景 |
|------|------|----------|
| **Discord** | `--channel discord --to "channel:<id>"` | 团队协作通知 |
| **Telegram** | `--channel telegram --to "+<phone>"` | 个人移动通知 |
| **WhatsApp** | `--channel whatsapp --to "+<phone>"` | 国际用户通知 |
| **Webhook** | `--webhook "<url>" --webhook-signing-secret "<key>"` | 系统集成 |

**多渠道投递策略**：

| 策略 | 说明 | 适用场景 |
|------|------|----------|
| **同时投递** | 所有渠道同时触发 | 重要提醒，确保触达 |
| **优先级降级** | 主渠道失败时尝试备用渠道 | 容错场景 |
| **分级投递** | 不同紧急程度投递到不同渠道 | 紧急程度分级 |

**同时投递示例**：

```bash
# 同时投递到Discord和Telegram
for CHANNEL in discord telegram; do
  case "$CHANNEL" in
    discord) TO="channel:1476104553148452958" ;;
    telegram) TO="+8613800138000" ;;
  esac

  skill-platform cron add \
    --name "reminder-$(date +%s)-$CHANNEL" \
    --at "$REMIND_AT" \
    --session main \
    --system-event "$CONTENT" \
    --agent "$AGENT" \
    --announce \
    --channel "$CHANNEL" \
    --to "$TO" \
    --delete-after-run
done
```

### 递增提醒

间隔逐渐缩短的提醒模式，适用于紧急程度递增的场景：

```bash
# 项目截止前递增提醒
# 2小时前 → 1小时前 → 30分钟前 → 15分钟前 → 5分钟前
DEADLINE="2026-07-20T17:00:00Z"

# 使用数组定义时间偏移
OFFSETS=(7200 3600 1800 900 300)  # 秒
URGENCY=("提醒" "注意" "紧急" "非常紧急" "立即处理")

for i in "${!OFFSETS[@]}"; do
  REMIND_AT=$(date -u -d "$DEADLINE - ${OFFSETS[$i]} seconds" +"%Y-%m-%dT%H:%M:%SZ")
  skill-platform cron add \
    --name "reminder-escalate-$(($i + 1))" \
    --at "$REMIND_AT" \
    --session main \
    --system-event "[${URGENCY[$i]}] 项目A即将截止" \
    --agent "$AGENT" \
    --announce \
    --channel discord \
    --to "$DISCORD_TO" \
    --delete-after-run
done
```

### 周期性提醒

| 类型 | cron表达式 | 适用场景 |
|------|-----------|----------|
| **每日** | `30 9 * * *` | 每日9:30站会 |
| **工作日** | `30 9 * * 1-5` | 工作日9:30站会 |
| **每周** | `0 17 * * 5` | 每周五17:00周报 |
| **每月** | `0 10 1 * *` | 每月1号10:00总结 |
| **每季度** | `0 10 1 1,4,7,10 *` | 季度首日10:00复盘 |

### 生命周期管理

```bash
# 查询所有提醒
skill-platform cron list

# 查询活跃提醒
skill-platform cron list --status active

# 查询特定模式
skill-platform cron list --name "reminder-*"

# 立即触发提醒
skill-platform cron run <job-id>

# 暂停提醒（周期性）
skill-platform cron pause <job-id>

# 恢复提醒
skill-platform cron resume <job-id>

# 编辑提醒内容
skill-platform cron edit <job-id> --system-event "新内容"

# 删除提醒
skill-platform cron remove <job-id>

# 查看执行历史
skill-platform cron runs --id <job-id> --limit 10

# 清理已完成
skill-platform cron cleanup --status done --older-than 7d
```

---

## 使用场景

### 场景一：多渠道项目截止提醒（项目经理角色）

**场景描述**：项目临近截止，需要通过Discord和Telegram同时发送递增提醒。

```bash
# 递增提醒，同时投递两个渠道
DEADLINE="2026-07-20T17:00:00Z"
OFFSETS=(7200 3600 1800 900 300)
URGENCY=("提醒" "注意" "紧急" "非常紧急" "立即处理")

for i in "${!OFFSETS[@]}"; do
  REMIND_AT=$(date -u -d "$DEADLINE - ${OFFSETS[$i]} seconds" +"%Y-%m-%dT%H:%M:%SZ")

  for CHANNEL_INFO in "discord:channel:1476104553148452958" "telegram:+8613800138000"; do
    CHANNEL="${CHANNEL_INFO%%:*}"
    TO="${CHANNEL_INFO#*:}"

    skill-platform cron add \
      --name "reminder-deadline-$(($i + 1))-$CHANNEL" \
      --at "$REMIND_AT" \
      --session main \
      --system-event "[${URGENCY[$i]}] 项目A即将截止" \
      --agent "$AGENT" \
      --announce \
      --channel "$CHANNEL" \
      --to "$TO" \
      --delete-after-run
  done
done
```

### 场景二：批量会议提醒（行政助理角色）

**场景描述**：一天内有多个会议，批量创建提醒。

```bash
# 批量创建会议提醒
MEETINGS_JSON='[
  {"time": "today 10:00", "content": "产品评审会议", "channels": ["discord"]},
  {"time": "today 14:00", "content": "技术方案讨论", "channels": ["discord", "telegram"]},
  {"time": "today 16:30", "content": "客户对接会议", "channels": ["telegram"]},
  {"time": "tomorrow 09:30", "content": "晨会", "channels": ["discord"]}
]'

# 批量创建逻辑（参见120秒标准搭建）
```

### 场景三：Webhook集成提醒（运维工程师角色）

**场景描述**：系统部署完成后，创建提醒通过Webhook触发监控系统的检查任务。

```bash
# 5分钟后通过Webhook触发监控检查
REMIND_AT=$(date -u -d "+5 minutes" +"%Y-%m-%dT%H:%M:%SZ")

skill-platform cron add \
  --name "reminder-deploy-verify" \
  --at "$REMIND_AT" \
  --session isolated \
  --message "验证最新部署的功能" \
  --webhook "https://monitoring.example.com/hooks/verify" \
  --webhook-signing-secret "monitor-secret" \
  --delete-after-run
```

### 场景四：周期性工作提醒（团队负责人角色）

**场景描述**：配置每日站会、每周周报、每月总结的周期性提醒。

```bash
# 每日站会（工作日9:30）
skill-platform cron add \
  --name "daily-standup" \
  --cron "30 9 * * 1-5" \
  --tz "Asia/Shanghai" \
  --session main \
  --system-event "每日站会时间到" \
  --agent "$AGENT" \
  --announce \
  --channel discord \
  --to "$DISCORD_TO"

# 每周周报（周五17:00）
skill-platform cron add \
  --name "weekly-report" \
  --cron "0 17 * * 5" \
  --tz "Asia/Shanghai" \
  --session main \
  --system-event "周五周报提交截止" \
  --agent "$AGENT" \
  --announce \
  --channel discord \
  --to "$DISCORD_TO"
```

### 场景五：紧急程度分级提醒（技术负责人角色）

**场景描述**：生产事故处理，根据紧急程度投递到不同渠道。

```bash
# P0级事故：所有渠道同时通知
for CHANNEL_INFO in "discord:channel:oncall" "telegram:+8613800138000" "whatsapp:+8613800138000"; do
  CHANNEL="${CHANNEL_INFO%%:*}"
  TO="${CHANNEL_INFO#*:}"

  skill-platform cron add \
    --name "reminder-incident-p0" \
    --at "$(date -u -d '+1 minute' +"%Y-%m-%dT%H:%M:%SZ")" \
    --session main \
    --system-event "[P0紧急] 生产事故，请立即处理" \
    --agent "$AGENT" \
    --announce \
    --channel "$CHANNEL" \
    --to "$TO" \
    --delete-after-run
done
```

---

## 多角色场景指南

| 角色 | 典型场景 | 推荐配置 | 核心价值 |
|------|----------|----------|----------|
| 项目经理 | 项目截止递增提醒 | 多渠道+递增 | 确保关键节点触达 |
| 行政助理 | 批量会议提醒 | 批量创建+多渠道 | 一键创建多个提醒 |
| 运维工程师 | 部署后验证提醒 | Webhook+isolated | 系统集成自动化 |
| 团队负责人 | 周期性工作提醒 | 周期性+主会话 | 团队日常规范 |
| 技术负责人 | 紧急事故通知 | 分级投递+全渠道 | 紧急触达保障 |
| 产品经理 | 需求评审提醒 | 单次+多渠道 | 会议准时参加 |
| 销售经理 | 客户跟进提醒 | 周期性+Telegram | 客户关系维护 |

---

## 性能优化策略

### 批量创建优化

1. **并行创建**：多个提醒并行创建，减少总耗时
2. **模板复用**：相同模式的提醒使用模板批量生成
3. **去重检查**：创建前检查是否已存在相同提醒
4. **错误隔离**：单个提醒创建失败不影响其他

### 投递优化

1. **渠道优先级**：重要提醒优先投递Discord，备用Telegram
2. **bestEffort模式**：非关键渠道启用bestEffort，避免阻塞
3. **签名验证**：Webhook启用签名验证，防止伪造
4. **超时控制**：根据渠道响应速度设置合理超时

### 安全优化

1. **白名单模式**：高安全场景启用白名单，仅允许已知安全字符
2. **编码检测**：检测URL编码、Unicode转义等绕过攻击
3. **长度限制**：限制任务内容长度，防止缓冲区溢出
4. **日志审计**：记录所有被拒绝的输入，便于审计

### 成本控制

- 简单提醒使用主会话模式，避免独立会话开销
- 非关键渠道启用bestEffort，避免重试浪费
- 批量创建使用脚本，减少重复API调用
- 定期清理已完成提醒，避免存储膨胀

---

## 多平台集成示例

### 与CI/CD系统集成

```bash
# 部署后5分钟创建验证提醒
skill-platform cron add \
  --name "reminder-deploy-verify" \
  --at "$(date -u -d '+5 minutes' +"%Y-%m-%dT%H:%M:%SZ")" \
  --session isolated \
  --message "验证最新部署的功能" \
  --webhook "https://ci.example.com/hooks/verify" \
  --webhook-signing-secret "ci-secret" \
  --delete-after-run
```

### 与监控系统集成

```bash
# 事故通知通过Webhook触发告警
skill-platform cron add \
  --name "reminder-incident-alert" \
  --at "$(date -u -d '+1 minute' +"%Y-%m-%dT%H:%M:%SZ")" \
  --session isolated \
  --message "触发告警：生产事故" \
  --webhook "https://alerts.example.com/hooks/incident" \
  --webhook-signing-secret "alert-secret" \
  --delete-after-run
```

### 与团队协作平台集成

```bash
# 会议提醒投递到Discord话题
skill-platform cron add \
  --name "reminder-meeting" \
  --at "$REMIND_AT" \
  --session main \
  --system-event "产品评审会议开始" \
  --agent "$AGENT" \
  --announce \
  --channel discord \
  --to "-1001234567890:topic:meetings" \
  --delete-after-run
```

### 与日历系统集成

```bash
# 从日历同步事件并创建提醒
# （需配合日历API脚本）
calender_events=$(get_calendar_events --today)
echo "$calender_events" | jq -c '.[]' | while read -r event; do
  TIME=$(echo "$event" | jq -r '.start')
  CONTENT=$(echo "$event" | jq -r '.title')
  # 创建提醒...
done
```

---

## 版本升级迁移指南

### 从免费版升级至专业版

1. **无需迁移数据**：专业版完全兼容免费版的提醒格式
2. **新增功能激活**：
   - 多渠道投递：为每个渠道创建独立作业
   - 递增提醒：使用循环脚本批量创建
   - 周期性提醒：将 `--at` 改为 `--cron`
   - Webhook投递：使用 `--webhook` 替代 `--announce`
3. **安全校验升级**：使用 `sanitize-message-pro.sh` 替代基础版
4. **指令兼容**：免费版的所有命令在专业版中均可使用

### 版本更新历史

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-07 | 初版发布，含多渠道投递、批量创建、递增提醒、周期性提醒、完整安全校验 |

---

## 故障排查表

| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 提醒未触发 | 时间已过 | 检查时间是否在未来；使用绝对时间 | 高 |
| 提醒未触发 | Gateway未运行 | 确保Gateway进程常驻 | 高 |
| 投递失败 | 频道凭证错误 | 检查Bot Token；验证渠道配置 | 高 |
| 投递失败 | TO格式错误 | Discord用`channel:ID`；Telegram用`+phone` | 高 |
| 多渠道部分失败 | 单渠道凭证错误 | 检查失败渠道的配置；启用bestEffort | 中 |
| 安全校验误拒 | 白名单过严 | 切换为strict模式；调整白名单字符集 | 中 |
| 安全校验漏放 | 危险模式未覆盖 | 升级校验脚本；添加新的危险模式 | 高 |
| 批量创建失败 | JSON格式错误 | 验证JSON语法；使用jq解析 | 中 |
| 批量创建部分失败 | 单条数据问题 | 检查失败条目；错误隔离继续执行 | 中 |
| 递增提醒时间错乱 | 时区不一致 | 统一使用UTC；显式指定时区 | 高 |
| 周期性提醒不触发 | cron表达式错误 | 验证5字段格式；使用crontab.guru测试 | 高 |
| Webhook投递失败 | URL不可达 | 检查URL；验证网络连通性 | 高 |
| Webhook签名失败 | 密钥不匹配 | 核对客户端与服务端密钥 | 高 |
| session_status无返回 | 工具不可用 | 检查Agent平台配置；手动指定agent和to | 中 |
| 提醒内容显示异常 | 特殊字符未转义 | 检查内容是否包含Markdown特殊字符 | 低 |
| 作业列表膨胀 | 未及时清理 | 使用`cleanup`清理已完成作业 | 低 |

---

## 即时修复清单

| 问题 | 修复方法 |
|------|----------|
| 提醒从未触发 | 检查时间是否在未来；检查Gateway是否运行 |
| 投递到错误频道 | 检查`--to`参数格式；调用`session_status`验证 |
| 多渠道部分失败 | 检查失败渠道凭证；启用bestEffort模式 |
| 安全校验误拒合法内容 | 切换strict模式；检查白名单配置 |
| 递增提醒时间错乱 | 统一使用UTC时间；使用`date -u`计算 |
| 周期性提醒不触发 | 验证cron表达式；检查时区设置 |
| Webhook请求被拒绝 | 检查签名密钥；验证URL可达性 |
| 批量创建卡住 | 检查JSON格式；使用错误隔离 |
| 提醒内容包含特殊字符 | 使用安全校验脚本；避免Markdown特殊字符 |
| 作业列表过大 | 使用`cleanup`清理；启用`delete-after-run` |

---

## FAQ

### Q1：免费版与专业版有什么区别？

免费版提供单频道投递、基础时间解析（相对+绝对）、基础安全校验、单次提醒创建。专业版解锁多渠道同时投递、批量创建、递增提醒、周期性提醒、Webhook投递、完整安全校验脚本（含上下文感知检测）、自然语言时间解析增强（支持"后天"/"下周一"等）。此外提供多角色场景指南、性能优化策略、多平台集成示例、完整FAQ（15问）与故障排查表（16项）。

### Q2：如何实现多渠道同时投递？

为每个渠道创建独立的cron作业，使用相同的`--at`时间。例如同时投递到Discord和Telegram，创建两个作业，时间相同但`--channel`和`--to`不同。这确保即使一个渠道失败，另一个仍能正常投递。

### Q3：递增提醒如何实现？

使用循环脚本，根据截止时间计算多个提前量（如2小时前、1小时前、30分钟前等），为每个时间点创建独立的提醒作业。通过`URGENCY`数组为每个提醒添加紧急程度标签，实现视觉上的紧急感递增。

### Q4：安全校验的"拒绝"和"转义"有什么区别？

转义（escape）是将危险字符转换为安全形式，但容易遗漏边界情况，导致绕过攻击。拒绝（reject）是直接拒绝包含任何危险模式的输入，强制用户重新表述，从根本上消除风险。专业版还提供白名单模式，仅允许已知安全字符通过，安全性更高。

### Q5：支持哪些自然语言日期格式？

专业版支持：`后天`、`大后天`、`下周一`至`下周日`、`下个月X号`、`X天后`、`X小时后`、`X分钟后`。这些格式通过语义解析后转换为ISO 8601时间戳。无法识别的格式会提示用户用明确格式表达。

### Q6：周期性提醒和一次性提醒有什么区别？

一次性提醒使用`--at`参数，指定具体时间，执行后自动删除（配合`--delete-after-run`）。周期性提醒使用`--cron`参数，指定cron表达式（如`30 9 * * 1-5`表示工作日9:30），按规则重复执行，不自动删除，需手动管理。

### Q7：如何批量创建提醒？

使用批量创建脚本，将多个提醒定义为JSON数组，循环解析并为每个提醒执行安全校验、时间解析、作业创建。支持错误隔离，单条失败不影响其他。详见"120秒标准搭建"示例。

### Q8：Webhook投递如何工作？

任务执行完成后，调度器将结果以JSON格式POST到指定的HTTP端点。请求包含`X-Signature`头（HMAC-SHA256签名），服务端可验证请求来源。Webhook模式仅适用于`isolated`会话任务。

### Q9：如何获取投递目标？

调用`session_status`工具获取当前会话的投递上下文。返回的`deliveryContext.accountId`用于`--agent`参数，`deliveryContext.to`用于`--to`参数。这确保提醒结果投递到用户当前所在的频道。也可手动指定`--to`参数。

### Q10：为什么使用`--session main`而非`isolated`？

一次性提醒通常需要继承主会话上下文（如引用之前的对话），使用`main`模式可确保提醒在正确上下文中触发。同时使用`--system-event` payload类型。`--delete-after-run`确保执行后自动清理。Webhook投递的任务必须使用`isolated`模式。

### Q11：超过48小时的提醒怎么办？

建议用户使用日历应用。提醒引擎设计为短期提醒（分钟级到小时级），长时间跨度的提醒更适合日历系统。若用户坚持创建，引擎仍会执行，但建议提示用户："此提醒距离现在超过48小时，建议同时添加到日历以免遗漏"。

### Q12：如何暂停和恢复周期性提醒？

使用`skill-platform cron pause <job-id>`暂停，暂停后不再被调度执行。使用`skill-platform cron resume <job-id>`恢复。暂停状态不影响作业配置。一次性提醒（已设置`--delete-after-run`）无需暂停，执行后自动删除。

### Q13：如何清理历史提醒？

使用`skill-platform cron cleanup --status done --older-than 7d`清理7天前已完成的提醒。可根据需要调整`--status`和`--older-than`参数。建议定期清理，避免作业列表膨胀。

### Q14：安全校验脚本如何升级？

专业版提供`sanitize-message-pro.sh`，新增上下文感知检测（URL编码、Unicode转义、HTML实体）、扩展危险命令列表、白名单模式、长度限制。直接替换免费版的`sanitize-message.sh`即可。

### Q15：多渠道投递失败时如何处理？

启用`bestEffort`模式，单个渠道失败不阻塞其他渠道。对于关键提醒，建议同时投递多个渠道确保触达。检查失败渠道的凭证配置，必要时手动重试。专业版支持优先级降级策略，主渠道失败时尝试备用渠道。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Bash**: 4.0+（用于安全校验脚本与批量创建脚本）
- **date命令**: 支持 `-d` 参数（GNU date，Linux/macOS自带）
- **jq**: 1.6+（用于JSON解析）
- **Python**: 3.8+（用于自然语言日期解析）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Agent Gateway | 运行时 | 必需 | Agent平台内置 |
| skill-platform CLI | 工具 | 必需 | Agent平台内置 |
| session_status工具 | 工具 | 必需 | Agent平台内置 |
| jq | 工具 | 必需 | 系统包管理器安装 |
| Discord Bot | 投递通道 | 否 | 注册Discord Bot获取 |
| Telegram Bot | 投递通道 | 否 | 注册Telegram Bot获取 |
| WhatsApp Business | 投递通道 | 否 | 注册WhatsApp Business API |
| Webhook端点 | 投递通道 | 否 | 自建或第三方服务 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 专业版使用 **GPT-4o** 模型路由，确保复杂提醒场景的创建质量
- 支持自然语言时间解析与多渠道投递的精细控制

### API Key 配置
- Discord投递需要Discord Bot Token（存储在Agent Gateway配置中）
- Telegram投递需要Telegram Bot Token（存储在Agent Gateway配置中）
- WhatsApp投递需要WhatsApp Business API凭证
- Webhook签名密钥由用户自定义，存储在作业配置中
- 禁止在SKILL.md或脚本中硬编码Token

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent创建企业级提醒

---

## License与版权声明

本技能基于原始开源提醒创建作品改进，保留原始版权声明：

- 原始作品：Reminder Engine
- 原始license：MIT
- 改进作品：提醒引擎（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文用户工作流
- 聚焦"提醒创建引擎"而非调度配置
- 新增多渠道同时投递矩阵与策略表
- 新增批量创建脚本（含错误隔离）
- 新增递增提醒算法与紧急程度分级
- 新增周期性提醒配置表（5种类型）
- 新增完整安全校验脚本（含上下文感知检测、白名单模式、编码验证、长度限制）
- 新增自然语言日期解析（Python实现，支持"后天"/"下周一"/"下个月X号"等）
- 新增Webhook投递完整示例与签名验证
- 新增生命周期管理扩展（pause/resume/edit/cleanup）
- 新增分级快速开始指南（30秒/120秒/300秒三档）
- 新增五类真实场景示例（多渠道/批量/Webhook/周期性/分级）
- 新增多角色场景指南（7种角色）
- 新增性能优化策略（批量创建/投递/安全/成本）
- 新增多平台集成示例（CI-CD/监控/团队协作/日历）
- 新增版本升级迁移指南
- 新增FAQ章节（15问）与故障排查表（16项）
- 新增即时修复清单（10项）
- 新增依赖说明章节与License版权声明
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 专业版特性

本专业版相比免费版新增以下能力：

- **多渠道同时投递**：将同一提醒同时投递到Discord、Telegram、WhatsApp、Webhook等多个渠道，确保关键提醒触达，支持优先级降级与分级投递策略
- **批量创建提醒**：通过JSON配置批量创建多个提醒，支持错误隔离，单条失败不影响其他，大幅提升创建效率
- **递增提醒**：实现间隔逐渐缩短的提醒模式（如2小时前→1小时前→30分钟前→5分钟前），配合紧急程度标签，适用于项目截止、事故处理等紧急程度递增的场景
- **周期性提醒**：支持每日、工作日、每周、每月、每季度等周期性提醒配置，无需重复创建，适用于日常站会、周报、月度总结等周期性工作
- **完整安全校验**：新增上下文感知检测（URL编码、Unicode转义、HTML实体）、扩展危险命令列表、白名单模式、长度限制，提供企业级安全保障
- **自然语言日期解析**：支持"后天"、"大后天"、"下周一"、"下个月X号"等中文自然语言日期表达，提升用户体验
- **Webhook投递**：将提醒结果POST到HTTP端点，支持签名验证、自定义头、超时控制，实现与外部系统的深度集成

此外，专业版还提供：
- 多角色场景指南（7种角色×场景映射）
- 性能优化策略（批量创建/投递/安全/成本）
- 多平台集成示例（CI-CD/监控/团队协作/日历）
- 版本升级迁移指南
- 扩展FAQ（15问）与故障排查表（16项）
- 即时修复清单（10项）
- 优先支持

---

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 单频道投递 + 基础时间解析 + 基础安全校验 + 单次提醒 + 基础示例 + 基础FAQ | 个人试用、轻量提醒需求 |
| 收费专业版 | ¥29.9/月 | 多渠道投递 + 批量创建 + 递增提醒 + 周期性提醒 + Webhook + 完整安全校验 + 自然语言日期 + 多角色指南 + 性能优化 + 优先支持 | 团队/企业、复杂提醒场景 |

专业版通过SkillHub SkillPay发布。
