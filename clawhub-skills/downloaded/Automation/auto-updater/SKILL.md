---
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
---

# Auto-Updater Skill

Keep your Clawdbot and skills up to date automatically with daily update checks.

## What It Does

This skill sets up a daily cron job that:

1. Updates Clawdbot itself (via `clawdbot doctor` or package manager)
2. Updates all installed skills (via `clawdhub update --all`)
3. Messages you with a summary of what was updated

## Setup

### Quick Start

Ask Clawdbot to set up the auto-updater:

```text
Set up daily auto-updates for yourself and all your skills.
```

Or manually add the cron job:

```bash
clawdbot cron add \
  --name "Daily Auto-Update" \
  --cron "0 4 * * *" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --wake now \
  --deliver \
  --message "Run daily auto-updates: check for Clawdbot updates and update all skills. Report what was updated."
```

### Configuration Options

| Option | Default | Description |
| --- | --- | --- |
| Time | 4:00 AM | When to run updates (use `--cron` to change) |
| Timezone | System default | Set with `--tz` |
| Delivery | Main session | Where to send the update summary |

## How Updates Work

### Clawdbot Updates

For **npm/pnpm/bun installs**:

```bash
npm update -g clawdbot@latest
```

For **source installs** (git checkout):

```bash
clawdbot update
```

Always run `clawdbot doctor` after updating to apply migrations.

### Skill Updates

```bash
clawdhub update --all
```

This checks all installed skills against the registry and updates any with new versions available.

## Update Summary Format

After updates complete, you'll receive a message like:

```text
🔄 Daily Auto-Update Complete

**Clawdbot**: Updated to v2026.1.10 (was v2026.1.9)

**Skills Updated (3)**:
- prd: 2.0.3 → 2.0.4
- browser: 1.2.0 → 1.2.1
- nano-banana-pro: 3.1.0 → 3.1.2

**Skills Already Current (5)**:
gemini, sag, things-mac, himalaya, peekaboo

No issues encountered.
```

## Manual Commands

Check for updates without applying:

```bash
clawdhub update --all --dry-run
```

View current skill versions:

```bash
clawdhub list
```

Check Clawdbot version:

```bash
clawdbot --version
```

## Troubleshooting

### Updates Not Running

1. Verify cron is enabled: check `cron.enabled` in config
2. Confirm Gateway is running continuously
3. Check cron job exists: `clawdbot cron list`

### Update Failures

If an update fails, the summary will include the error. Common fixes:

* **Permission errors**: Ensure the Gateway user can write to skill directories
* **Network errors**: Check internet connectivity
* **Package conflicts**: Run `clawdbot doctor` to diagnose

### Disabling Auto-Updates

Remove the cron job:

```bash
clawdbot cron remove "Daily Auto-Update"
```

Or disable temporarily in config:

```json
{
  "cron": {
    "enabled": false
  }
}
```

## Resources

* [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating)
* [SkillHub CLI](https://docs.clawd.bot/tools/clawdhub)
* [Cron Jobs](https://docs.clawd.bot/cron)

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

## 核心能力

- Automatically update Clawdbot and all installed skills once daily
- 触发关键词: automatically, auto-updater, auto, clawdbot, installed, updater, update,
  skills

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
Ask Clawdbot to set up the auto-updater:

```text
Set up daily auto-updates for yourself and all your skills.
```

Or manually add the cron job:

```bash
clawdbot cron add \
  --name "Daily Auto-Update" \
  --cron "0 4 * * *" \
  --tz "America/Los_Angeles" \
  --session isolated \
  --wake now \
  --deliver \
  --message "Run daily auto-updates: check for Clawdbot updates and update all skills. Report what was updated."
```
```

## 常见问题

### Q1: 如何开始使用Auto-Updater Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Auto-Updater Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
