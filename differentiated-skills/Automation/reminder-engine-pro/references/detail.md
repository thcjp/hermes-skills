# 详细参考 - reminder-engine-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (bash)

```bash
#!/bin/bash
SESSION_INFO=$(session_status)
AGENT=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.accountId')
DISCORD_TO=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.to')

DEADLINE="2026-07-20T17:00:00Z"
CONTENT="项目A即将截止，请确认完成状态"

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

## 代码示例 (bash)

```bash
#!/bin/bash
CONTENT="$1"
MODE="${2:-strict}"  # strict / whitelist
if [[ "$CONTENT" =~ \$\(.*\) ]] || [[ "$CONTENT" =~ '`' ]]; then
  echo "拒绝：包含命令替换"; exit 1
fi

if [[ "$CONTENT" =~ [;\|&\>\<] ]]; then
  echo "拒绝：包含Shell元字符"; exit 2
fi

if [[ "$CONTENT" =~ [\"] ]]; then
  echo "拒绝：包含双引号"; exit 3
fi

if [[ "$CONTENT" =~ $'\n' ]]; then
  echo "拒绝：包含换行符"; exit 4
fi

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

if [[ "$CONTENT" =~ %[0-9a-fA-F]{2} ]]; then
  echo "拒绝：包含URL编码字符"
  exit 6
fi

if [[ "$CONTENT" =~ \\u[0-9a-fA-F]{4} ]]; then
  echo "拒绝：包含Unicode转义"
  exit 7
fi

if [[ "$CONTENT" =~ \&[a-z]+; ]]; then
  echo "拒绝：包含HTML实体"
  exit 8
fi

if [ "$MODE" == "whitelist" ]; then
  if ! [[ "$CONTENT" =~ ^[[:alnum:][:space:][:punct:]\u4e00-\u9fa5]+$ ]]; then
    echo "拒绝：包含非白名单字符"
    exit 9
  fi
fi

if [ ${#CONTENT} -gt 500 ]; then
  echo "拒绝：内容过长（超过500字符）"
  exit 10
fi

echo "安全"
exit 0
```

## 代码示例 (bash)

```bash
#!/bin/bash
REMINDERS_JSON='[
  {"time": "+1 hour", "content": "参加项目评审会议", "channels": ["discord", "telegram"]},
  {"time": "+2 hours", "content": "提交周报", "channels": ["discord"]},
  {"time": "today 18:00", "content": "下班前检查邮件", "channels": ["telegram"]},
  {"time": "tomorrow 09:00", "content": "明早站会准备", "channels": ["discord", "telegram"]}
]'

SESSION_INFO=$(session_status)
AGENT=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.accountId')
DISCORD_TO=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.to')
TELEGRAM_TO="+8613800138000"

echo "$REMINDERS_JSON" | jq -c '.[]' | while read -r reminder; do
  TIME=$(echo "$reminder" | jq -r '.time')
  CONTENT=$(echo "$reminder" | jq -r '.content')
  CHANNELS=$(echo "$reminder" | jq -r '.channels[]')

  if ! ./scripts/sanitize-message.sh "$CONTENT"; then
    echo "跳过（内容不安全）：$CONTENT"
    continue
  fi

  REMIND_AT=$(date -u -d "$TIME" +"%Y-%m-%dT%H:%M:%SZ")
  if [ -z "$REMIND_AT" ]; then
    echo "跳过（时间无法解析）：$TIME"
    continue
  fi

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

## 代码示例 (python)

```python
import re
from datetime import datetime, timedelta

def parse_natural_date(text, now=None):
    """解析中文自然语言日期"""
    if now is None:
        now = datetime.now()

    text = text.strip()

    if text == "后天":
        return now + timedelta(days=2)

    if text == "大后天":
        return now + timedelta(days=3)

    m = re.match(r"下周([一二三四五六日天])", text)
    if m:
        day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
        target_day = day_map[m.group(1)]
        days_ahead = (target_day - now.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return now + timedelta(days=days_ahead)

    m = re.match(r"下个月(\d+)号", text)
    if m:
        day = int(m.group(1))
        next_month = now.month + 1 if now.month < 12 else 1
        next_year = now.year if now.month < 12 else now.year + 1
        return now.replace(year=next_year, month=next_month, day=day)

    m = re.match(r"(\d+)天后", text)
    if m:
        return now + timedelta(days=int(m.group(1)))

    m = re.match(r"(\d+)小时后", text)
    if m:
        return now + timedelta(hours=int(m.group(1)))

    m = re.match(r"(\d+)分钟后", text)
    if m:
        return now + timedelta(minutes=int(m.group(1)))

    return None
```

## 代码示例 (text)

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

## 代码示例 (bash)

```bash
session_status

./scripts/sanitize-message.sh "参加项目评审会议"
REMIND_AT=$(date -u -d "+1 hour" +"%Y-%m-%dT%H:%M:%SZ")

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

echo "好的，将在1小时后通过Discord和Telegram提醒你参加项目评审"
```

## 代码示例 (bash)

```bash
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

## 代码示例 (bash)

```bash
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

## 代码示例 (bash)

```bash
skill-platform cron list

skill-platform cron list --status active

skill-platform cron list --name "reminder-*"

skill-platform cron run <job-id>

skill-platform cron pause <job-id>

skill-platform cron resume <job-id>

skill-platform cron edit <job-id> --system-event "新内容"

skill-platform cron remove <job-id>

skill-platform cron runs --id <job-id> --limit 10

skill-platform cron cleanup --status done --older-than 7d
```

## 代码示例 (bash)

```bash
DEADLINE="2026-07-20T17:00:00Z"

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

## 代码示例 (bash)

```bash
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

## 代码示例 (bash)

```bash
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

### 300秒完整配置（递增提醒 + 周期性提醒）
实现紧急程度递增的提醒与周期性提醒：

```bash
#!/bin/bash
SESSION_INFO=$(session_status)
AGENT=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.accountId')
DISCORD_TO=$(echo "$SESSION_INFO" | jq -r '.deliveryContext.to')

DEADLINE="2026-07-20T17:00:00Z"
CONTENT="项目A即将截止，请确认完成状态"

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



