---
slug: openclaw-reminder
name: openclaw-reminder
version: "1.0.5"
displayName: Reminder
summary: Create one-time reminder tasks using OpenClaw cron. User specifies reminder
  time and task content...
license: MIT
description: |-
  Create one-time reminder tasks using OpenClaw cron. User specifies reminder
  time and task content...

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: using, create, tasks, openclaw, reminder, time
tags:
- Automation
tools:
- read
- exec
---

# Reminder

Create one-time reminder tasks using Skill平台 cron.

## Usage

When user says "remind me to XXX in 30 seconds" or "remind me at 3pm", I create a cron job that executes the task and returns the result when the time comes.

## Parameter Configuration

### Fixed Parameters

* `--session main` - Use main session to inherit Discord context
* `--system-event` - System event payload for main session
* `--channel discord` - Discord channel
* `--announce` - Send result directly to Discord
* `--delete-after-run` - Delete task after execution

### Dynamic Parameters (from current session context)

Use `session_status` tool to get current session's deliveryContext:

* `--agent` - Get from `deliveryContext.accountId` (e.g., `machu`)
* `--to` - Get from `deliveryContext.to` (e.g., `channel:1476104553148452958`)

How to get:

```bash
session_status
```

## Time Parsing

Parse user input time, support:

* Relative time: `30 seconds`, `1 minute`, `30 minutes`, `2 hours`, `1 day`
* Absolute time: `3pm`, `9am today`, `12pm tomorrow`

Convert to ISO 8601 format for cron.

## Usage Example

User says "remind me to check weather in 30 seconds":

```bash
session_status

date -u -d "+30 seconds" +"%Y-%m-%dT%H:%M:%SZ"

skill-platform cron add \
  --name "reminder-weather" \
  --at "2026-02-26T13:30:00Z" \
  --session main \
  --system-event "Check Beijing weather" \
  --agent machu \
  --announce \
  --channel discord \
  --to "channel:1476104553148452958" \
  --delete-after-run
```

## Task Content (SECURITY)

User-specified task content must be sanitized before passing to cron:

1. **Validation Method**: REJECT dangerous patterns (not escape)

   The script rejects any input containing:

   * Command substitution: `$()`, backticks `` ` ``
   * Shell metacharacters: `;`, `|`, `&`, `>`, `<`
   * Double quotes: `"` (breaks CLI quoting)
   * Newlines: `\n` (can inject multiple commands)
   * Dangerous command prefixes: `sudo`, `rm`, `wget`, `curl`, `bash`, etc.
2. **Sanitization Script**:
   Use `scripts/sanitize-message.sh` to validate input:

   bash

   ```
   ./scripts/sanitize-message.sh "user's task content"
   # Exit code 0 = safe, non-zero = rejected
   ```
3. **If rejected**: Tell user the task contains invalid characters and ask them to rephrase without: $() ` ; | & > < " or dangerous commands.

## Confirmation Reply

After creating the task, reply to user to confirm:

* "OK, will remind you in X minutes/to do XXX"
* Don't tell user the specific cron command

## Notes

1. Time must be in the future, not the past
2. Task content should be concise and clear
3. If time exceeds 48 hours, suggest using calendar
4. Always use `--session main` + `--system-event` for reliable Discord delivery
5. Validate task content with sanitize-message.sh before creating job

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
