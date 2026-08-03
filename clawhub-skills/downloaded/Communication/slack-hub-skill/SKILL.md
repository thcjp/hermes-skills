---
slug: slack-hub-skill
name: slack-hub-skill
version: "0.1.0"
displayName: Slack Hub Skill
summary: "用Slack Bot发消息/线程回复/搜工作区/列公开频道"
  channels using Slack B...
license: MIT
description: |-
  Send messages, reply in threads, search workspace content, and list
  public channels using Slack B。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

- Send messages, reply in threads, search workspace content, and list
  public channels using Slack B
- 触发关键词: threads, reply, send, search, messages, slack, hub, skill

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

### Q1: 如何开始使用Slack Hub Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Slack Hub Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **消息长度**：Slack API对发送的消息长度有限制，通常不超过4000个字符。如果消息内容超过此限制，需要将其拆分成多个消息发送。
- **搜索结果数量**：`slack_search`工具返回的结果数量有限制，默认为100条。如果需要更多结果，可以使用API提供的分页功能。
- **线程回复**：回复线程时，需要提供有效的`thread_ts`参数，否则无法正确回复到指定线程。

### 性能边界
- **并发请求**：由于Slack API的限制，Skill在短时间内可能无法处理大量并发请求。在高负载情况下，可能需要实施队列或限流策略。
- **响应时间**：Skill的响应时间受底层API调用和网络延迟的影响。在高峰时段，响应时间可能会增加。

### 兼容性约束
- **Slack版本**：Skill可能不支持某些较老版本的Slack，因为API调用可能发生了变化。
- **工作区设置**：某些工作区的设置可能影响Skill的功能，例如禁用某些API或限制消息类型。
- **权限限制**：Skill需要Slack Bot Token具有适当的权限才能执行操作，例如发送消息、读取消息等。如果权限不足，Skill将无法执行相关操作。

