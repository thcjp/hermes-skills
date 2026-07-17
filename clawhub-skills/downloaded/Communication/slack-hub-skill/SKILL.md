---
slug: slack-hub-skill
name: slack-hub-skill
version: "0.1.0"
displayName: Slack Hub Skill
summary: Send messages, reply in threads, search workspace content, and list public
  channels using Slack B...
license: MIT
description: |-
  Send messages, reply in threads, search workspace content, and list
  public channels using Slack B...

  核心能力:

  - 沟通协作领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 消息发送、社交管理、通知提醒

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: threads, reply, send, search, messages, slack, hub, skill
tags:
- Communication
tools:
- read
- exec
---

# Slack Hub Skill

Professional Slack integration for Skill平台. Supports messaging, threading, and workspace search.

## Configuration

Requires a Slack Bot Token (`xoxb-...`) in your `.env` as `SLACK_BOT_TOKEN`.

## Tools

### slack_send

Send a message to a channel or user.

* `target`: Channel ID or name (e.g., "#general").
* `message`: Text content.
* `thread_ts`: (Optional) Timestamp for replying to a thread.

### slack_search

Search the workspace for messages or files.

* `query`: The search term.

### slack_list_channels

List all public channels in the workspace.

## Implementation Notes

* Uses `https://slack.com/api/chat.postMessage`
* Uses `https://slack.com/api/search.messages`
* Implements rate-limit handling for high-volume workspaces.

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
