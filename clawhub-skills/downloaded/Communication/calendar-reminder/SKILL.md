---
slug: calendar-reminder
name: calendar-reminder
version: "1.0.0"
displayName: Calendar Reminder
summary: 每晚22:00自动扫描明天的Outlook日历，上午日程提前2小时提醒，下午日程12:00统一提醒，通过飞书发送通知。依赖 owa-outlook
  skill。
license: MIT
description: |-
  每晚22:00自动扫描明天的Outlook日历，上午日程提前2小时提醒，下午日程12:00统一提醒，通过飞书发送通知。依赖 owa-outlook\
  \ skill。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。
tags: '[''Communication'']'
tools:
  - read
  - exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

## 依赖说明

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

## 核心能力

每晚 22:00 自动扫描明天的 Outlook 日历，按时间段设置提醒：

* 上午日程（< 12:00）→ 提前 2 小时飞书提醒
* 下午日程（>= 12:00）→ 当天 12:00 统一飞书提醒
* 扫描完成后立即发送汇报消息

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Calendar Reminder？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Calendar Reminder有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
