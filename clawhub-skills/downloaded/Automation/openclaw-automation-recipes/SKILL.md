---
slug: openclaw-automation-recipes
name: openclaw-automation-recipes
version: "1.1.0"
displayName: Openclaw Automation Recipes
summary: OpenClaw 自动化配方 - 10 个实用自动化场景。适合：效率工具爱好者、自动化新手。
license: MIT-0
description: |-
  OpenClaw 自动化配方 - 10 个实用自动化场景。适合：效率工具爱好者、自动化新手。

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 效率工具爱好, 适合, 自动化配方, recipes, automation, openclaw, 个实用自动化, 场景
tags:
- Automation
tools:
- read
- exec
---

# Openclaw Automation Recipes

10 个开箱即用的自动化场景。

## 配方 1：每日新闻摘要

每天早上自动推送新闻摘要。

```yaml
trigger:
  type: schedule
  cron: "0 8 * * *"  # 每天 8:00

actions:
  - type: fetch
    url: https://news.ycombinator.com/rss
  - type: summarize
    prompt: "总结今日科技新闻，列出前 5 条"
  - type: send
    to: telegram
```

## 配方 2：邮件自动回复

检测关键词自动回复邮件。

```yaml
trigger:
  type: email
  keywords: ["合作", "商务", "咨询"]

actions:
  - type: reply
    template: "感谢来信，我会在 24 小时内回复..."
```

## 配方 3：GitHub Issue 监控

自动监控项目 Issues 并通知。

```yaml
trigger:
  type: github
  event: issues
  repo: owner/repo

actions:
  - type: send
    to: discord
    template: "新 Issue: {{title}}"
```

## 配方 4：价格监控

监控商品价格变动。

```yaml
trigger:
  type: schedule
  cron: "0 */4 * * *"  # 每 4 小时

actions:
  - type: fetch
    url: "https://example.com/product"
  - type: extract
    selector: ".price"
  - type: condition
    if: "price < 100"
    then:
      type: send
      to: telegram
      message: "价格降到 {{price}}！"
```

## 配方 5：会议提醒

自动提醒即将到来的会议。

```yaml
trigger:
  type: calendar
  before: 15m

actions:
  - type: send
    to: dingtalk
    message: "15 分钟后有会议：{{title}}"
```

## 配方 6：客服自动分流

根据问题类型分流客服。

```yaml
trigger:
  type: message

actions:
  - type: classify
    categories: ["技术", "账单", "投诉"]
  - type: route
    technical: tech_support
    billing: billing_team
    complaint: manager
```

## 配方 7：内容发布

自动发布内容到多平台。

```yaml
trigger:
  type: schedule
  cron: "0 9 * * 1-5"  # 工作日 9:00

actions:
  - type: generate
    prompt: "写一篇关于 AI 的短文"
  - type: publish
    platforms: [juejin, zhihu, twitter]
```

## 配方 8：数据备份

定期备份重要数据。

```yaml
trigger:
  type: schedule
  cron: "0 2 * * *"  # 每天凌晨 2:00

actions:
  - type: backup
    source: ~/.skill-platform/data
    dest: s3://backup-bucket/
  - type: notify
    message: "备份完成"
```

## 配方 9：社交媒体监控

监控品牌提及。

```yaml
trigger:
  type: social
  keywords: ["Skill平台", "AI助手"]

actions:
  - type: save
    to: database
  - type: alert
    if: "sentiment == 'negative'"
```

## 配方 10：智能排程

根据日历自动安排任务。

```yaml
trigger:
  type: schedule
  cron: "0 7 * * *"

actions:
  - type: analyze_calendar
  - type: prioritize_tasks
  - type: send
    message: "今日任务优先级：{{tasks}}"
```

## 如何使用

1. 复制配方到 `~/.skill-platform/automations/`
2. 修改参数（URL、时间等）
3. 重启 Skill平台

```bash
skill-platform restart
```

## 需要定制？

* 单个配方定制：¥99
* 企业自动化方案：¥999

联系：微信 yang1002378395 或 Telegram @yangster151

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
