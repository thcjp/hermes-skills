---
slug: tardis
name: tardis
version: "1.2.0"
displayName: TARDIS
summary: The core time tracker appears legitimate, but the package also includes broad
  secret loading, pub...
license: MIT
description: |-
  The core time tracker appears legitimate, but the package also includes
  broad secret loading, pub...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: tracker, legitimate, appears, core, time, tardis
tags:
- Other
tools:
- read
- exec
---

# TARDIS

Life event tracker with three modes, milestone notifications, and tamper-evident verification.

> **SkillHub Note:** This skill is published as **TARDIS** on SkillHub after the original `hour-meter` listing was lost due to a repository sync issue.

## Three Modes

### COUNT UP — Time since an event

```bash
meter.py create smoke-free --start "2025-06-15T08:00:00Z" -d "Last cigarette"
meter.py milestone smoke-free -t hours -v 720 -m "🎉 30 days smoke-free!"
meter.py lock smoke-free  # → Gives you paper code to save
```

### COUNT DOWN — Time until an event

```bash
meter.py create baby --start "2026-01-15" --end "2026-10-15" --mode down -d "Baby arriving!"
meter.py milestone baby -t percent -v 33 -m "👶 First trimester complete!"
```

### COUNT BETWEEN — Journey from start to end

```bash
meter.py create career --start "1998-05-15" --end "2038-05-15" -d "40-year career"
meter.py milestone career -t percent -v 50 -m "📊 Halfway through career!"
meter.py career --meter career --rate 85 --raise-pct 2.5
```

## Tamper-Evident Persistence

When you lock a meter, you get a **paper code** — a short, checksummed code you can write on paper:

```text
╔══════════════════════════════════════════════════════════════╗
║  PAPER CODE (write this down):                               ║
║     318B-3229-C523-2F9C-V                                    ║
╚══════════════════════════════════════════════════════════════╝
```

### Four Ways to Save (Non-Technical)

**1️⃣ PAPER** — Write the code on paper/sticky note

* 20 characters with dashes, easy to copy
* Built-in checksum catches typos when verifying
* Keep in wallet, safe, or taped to equipment

**2️⃣ PHOTO** — Screenshot or photograph the lock screen

* Store in camera roll, cloud photos
* Visual backup, no typing required

**3️⃣ WITNESS FILE** — Auto-saved to `~/.skill-platform/meter-witness.txt`

* Append-only log of all locked meters
* Sync folder to Dropbox/iCloud/Google Drive for cloud backup
* Contains paper code + full hash + timestamp

**4️⃣ EMAIL TO SELF** — Click the mailto: link or copy the one-liner

* Opens your email client with pre-filled subject and body
* Or copy the compact message: `🔒 my-meter | Code: XXXX-XXXX-XXXX-XXXX-C | Locked: 2026-02-02`
* Send to yourself, search inbox later to verify

**5️⃣ SENDGRID EMAIL** — Auto-send verification email on lock

```bash
export SENDGRID_API_KEY=SG.xxxxx
export SENDGRID_FROM_EMAIL=verified@yourdomain.com

meter.py lock my-meter --email you@example.com
```

* Sends a beautifully formatted HTML email with paper code
* Requires a verified sender in SendGrid (see SendGrid docs)
* Great for automated workflows

### Verifying Later

```bash
meter.py verify my-meter "318B-3229-C523-2F9C-V"

```

## Milestones

```bash
meter.py milestone <name> --type hours --value 1000 --message "1000 hours!"
meter.py milestone <name> --type percent --value 50 --message "Halfway!"
meter.py check-milestones  # JSON output for automation
```

### Email Milestone Notifications (v1.3.0)

Get milestone notifications sent directly to your email:

```bash
meter.py create my-meter \
  --notify-email you@example.com \
  --from-email verified@yourdomain.com \
  -d "My tracked event"

meter.py milestone my-meter -t hours -v 24 -m "🎉 24 hours complete!"

meter.py check-milestones
```

**Email includes:**

* 🎯 Milestone message
* ⏱️ Current elapsed time
* 📝 Meter description

Requires `SENDGRID_API_KEY` environment variable.

### Milestone Notifications: Heartbeat vs Cron

**Recommended: HEARTBEAT** (~30 min resolution)

* Add to `HEARTBEAT.md`: `Run meter.py check-milestones and notify triggered`
* Batches with other periodic checks
* Cost-efficient: shares token usage with other heartbeat tasks
* Good for most use cases (quit tracking, career milestones, etc.)

### Milestone Messages

Milestones post their message text to the configured notification channel when triggered:

```bash
meter.py milestone my-meter -t hours -v 24 -m "🎉 24 hours complete!"
```

Configure in HEARTBEAT.md:

```markdown
- Run meter.py check-milestones and post triggered milestone messages to the configured channel
```

> **Advanced:** Milestone messages prefixed with `ACTION:` can optionally be treated as agent instructions by your heartbeat config. This is an opt-in feature — see README.md for security considerations.

**Alternative: CRON** (precise timing)

* Use when exact timing matters (e.g., countdown to event)
* ⚠️ **Cost warning:** Cron at 1-minute intervals = 1,440 API calls/day = expensive!
* If using cron, keep intervals ≥15 minutes to manage costs
* Best for one-shot reminders, not continuous monitoring

**Rule of thumb:** If 30-minute resolution is acceptable, use heartbeat. Save cron for precision timing.

## Quick Reference

```bash
meter.py create <name> [--start T] [--end T] [--mode up|down|between] [-d DESC]
meter.py lock <name>                # Seal + get paper code
meter.py verify <name> <code>       # Verify paper code
meter.py check <name>               # Status + progress
meter.py milestone <name> -t hours|percent -v N -m "..."
meter.py check-milestones           # All milestones (JSON)
meter.py witness [--show] [--path]  # Witness file
meter.py list                       # All meters
meter.py career [--meter M] [--rate R] [--raise-pct P]
meter.py export [name]              # JSON export
```

## SendGrid Email Webhook Server

Receive real-time notifications when recipients open, click, bounce, or unsubscribe from your meter verification emails.

### Setup

```bash
python sendgrid_webhook.py --port 8089 --discord-webhook https://discord.com/api/webhooks/xxx/yyy

python sendgrid_webhook.py --process-events
python sendgrid_webhook.py --process-events --json
```

### Discord Webhook Setup (Recommended)

1. In your Discord channel, go to **Settings > Integrations > Webhooks**
2. Click **New Webhook**, copy the URL
3. Pass to `--discord-webhook` or set `DISCORD_WEBHOOK_URL` env var

### SendGrid Setup

1. Go to **SendGrid > Settings > Mail Settings > Event Webhook**
2. Click **"Create new webhook"** (or edit existing)
3. Set HTTP POST URL to: `https://your-domain.com/webhooks/sendgrid`
4. Select all event types under **Actions to be posted**:
   * **Engagement data:** Opened, Clicked, Unsubscribed, Spam Reports, Group Unsubscribes, Group Resubscribes
   * **Deliverability Data:** Processed, Dropped, Deferred, Bounced, Delivered
   * **Account Data:** Account Status Change
5. Click **"Test Integration"** to verify - this fires all event types to your webhook
6. **Important:** Click **Save** to enable the webhook!
7. (Optional) Enable **Signed Event Webhook** for security and set `SENDGRID_WEBHOOK_PUBLIC_KEY`

### Event Types

| Event | Emoji | Description |
| --- | --- | --- |
| delivered | ✅ | Email reached recipient |
| open | 👀 | Recipient opened email |
| click | 🔗 | Recipient clicked a link |
| bounce | ⚠️ | Email bounced |
| unsubscribe | 🔕 | Recipient unsubscribed |
| spamreport | 🚨 | Marked as spam |

### Environment Variables

```bash
SENDGRID_WEBHOOK_PUBLIC_KEY    # For signature verification (optional)
SENDGRID_WEBHOOK_MAX_AGE_SECONDS  # Max timestamp age (default: 300)
WEBHOOK_PORT                   # Server port (default: 8089)
DISCORD_WEBHOOK_URL            # Discord webhook URL
WEBHOOK_LOG_FILE               # Log file path
```

## The 80,000 Hours Concept

Career as finite inventory: 40 years × 2,000 hrs/year = 80,000 hours.

```bash
meter.py career --hours-worked 56000 --rate 85 --raise-pct 2.5
```

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
