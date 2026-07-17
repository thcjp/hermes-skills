---
slug: calendar-reminder
name: calendar-reminder
version: "1.0.0"
displayName: "Calendar Reminder æ\x97¥å\x8E\x86æ\x8F\x90é\x86\x92"
summary: 每晚22:00自动扫描明天的Outlook日历，上午日程提前2小时提醒，下午日程12:00统一提醒，通过飞书发送通知。依赖 owa-outlook
  skill。
license: MIT
description: |-
  每晚22:00自动扫描明天的Outlook日历，上午日程提前2小时提醒，下午日程12:00统一提醒，通过飞书发送通知。依赖 owa-outlook\
  \ skill。\n\n核心能力:\n- 沟通协作领域的专业化AI辅助工具\n- 基于高人气开源Skill深度优化升级\n- 移除风险代码,增强安全性和稳定性\n\
  \n适用场景:\n- 消息发送、社交管理、通知提醒\n- 独立开发者与一人公司效率提升\n- 自动化工作流与智能决策辅助\n\n差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。\n\
  \n触发关键词: 上午日程提前, 日历, 每晚, calendar, æ\x97¥å\x8E\x86æ\x8F\x90é\x86\x92, 小时提醒, reminder,\
  \ 自动扫描明天
tags: '[''Communication'']'
tools: '[read, exec]'
---

# Calendar Reminder æ¥åæé

## 功能

每晚 22:00 自动扫描明天的 Outlook 日历，按时间段设置提醒：

* 上午日程（< 12:00）→ 提前 2 小时飞书提醒
* 下午日程（>= 12:00）→ 当天 12:00 统一飞书提醒
* 扫描完成后立即发送汇报消息

## 依赖

* `owa-outlook` skill（提供 `owa_calendar.py`）
* `skill-platform` CLI
* Python 3.9+（需要 `zoneinfo` 模块）

## 安装后配置

### 1. 注册每晚扫描 cron

```bash
skill-platform cron add \
  --name "calendar-daily-scan" \
  --cron "0 22 * * *" \
  --tz "Asia/Shanghai" \
  --session main \
  --system-event "CALENDAR_SCAN: 请立即运行 python3 ~/.skill-platform/workspace/skills/calendar-reminder/calendar_reminder.py 并等待完成" \
  --description "每晚22:00扫描明天日历并设置提醒"
```

### 2. 修改脚本中的飞书 open_id

编辑 `calendar_reminder.py`，将 `send_feishu` 函数中的 `target` 改为你自己的飞书 open_id：

```python
"--target", "user:ou_xxxxxxxxxxxxxxxx",
```

## 手动运行

```bash
python3 ~/.skill-platform/workspace/skills/calendar-reminder/calendar_reminder.py
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
