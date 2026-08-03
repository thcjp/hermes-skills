---
slug: agent-telegram
name: agent-telegram
version: "1.0.0"
displayName: Agent Telegram
summary: Agent 团队 Telegram 通信规范。所有 Agent 向用户发送消息时必须遵循此规范，确保消息正确发送到 Telegram。
license: MIT
description: |-
  Agent 团队 Telegram 通信规范。所有 Agent 向用户发送消息时必须遵循此规范，确保消息正确发送到 Telegram。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Agent Telegram

所有 Agent 向用户 (Legend) 发送 Telegram 消息时必须遵循此规范。

## 账号映射表

| Agent | accountId | Emoji |
| --- | --- | --- |
| main (9527) | `default` | 🤖 |
| architect (亮亮) | `architect` | 🏗️ |
| backend (老崔) | `backend` | 🔧 |
| frontend (小白) | `frontend` | 🎨 |
| product (小黄) | `sproduct` | 🟡 |
| content (世龙) | `content` | ✍️ |
| crawler (湘君) | `crawler` | 🕷️ |
| qa (赵飞) | `qa` | 🧪 |

**用户 Telegram ID**: `5440561025`

## 发送消息

### 标准格式

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "<你的accountId>",
  target: "5440561025",
  message: "<你的emoji> <内容>"
})
```

### 示例

**产品经理发送：**

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "sproduct",
  target: "5440561025",
  message: "🟡 需求文档已完成，请查看：~/Desktop/project/docs/product/001-prd.md"
})
```

**后端工程师发送：**

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "backend",
  target: "5440561025",
  message: "🔧 API 接口开发完成，接口文档：~/Desktop/project/docs/backend/api.md"
})
```

## 汇报时机

* ✅ **收到任务时** - 立即汇报"收到任务，开始执行"
* ✅ **每完成子任务** - 汇报完成情况和输出
* ✅ **遇到问题** - 汇报问题并请求决策
* ✅ **任务全部完成** - 汇报最终结果

## 常见错误

| 错误 | 后果 | 正确做法 |
| --- | --- | --- |
| 忘记 `accountId` | 消息发不出去 | 必须指定你的 accountId |
| 用 `sessions_send` | 消息不会发到 Telegram | 用 `message` 工具 |
| product 用 `accountId: "product"` | 账号不存在 | 应该是 `sproduct` |
| target 写错 | 发给错误的人 | 固定用 `5440561025` |

## 消息模板

### 任务开始

```text
<emoji> 收到任务：<任务名>
📝 开始执行...
```

### 任务完成

```text
<emoji> <任务名> 完成
✅ 已完成: <子任务>
📁 输出: <文件路径>
```

### 遇到问题

```text
<emoji> <任务名> 遇到问题
❌ 问题: <描述>
💡 建议: <解决方案或请求决策>
```

## 配置位置

* **主配置**: `~/.skill-platform/skill-platform.json` → `channels.telegram.accounts`
* **此 Skill**: `~/.skill-platform/workspace/skills/agent-telegram/SKILL.md`

---

**记住**：发送 Telegram 消息 = `message` 工具 + `accountId` + `target: "5440561025"`

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

- Agent 团队 Telegram 通信规范
- 所有 Agent 向用户发送消息时必须遵循此规范，确保消息正确发送到 Telegram
- 触发关键词: 息时必须遵循, 所有, 团队, telegram, 向用户发送消, agent, 通信规范

## 差异化优势

Agent Telegram 的差异化优势主要体现在以下几个方面：首先，它通过预定义的账号映射表和标准化的消息格式，实现了团队内部通信的规范化，提高了沟通效率。其次，通过使用 emoji 作为账号标识，使得消息发送更加直观和易于识别。此外，Agent Telegram 的消息模板功能为不同类型的消息提供了预设格式，减少了人工编写模板的工作量。最后，其与 Agent 平台的集成方式，使得 Agent 可以直接通过技能发送消息，无需额外的配置和操作，极大地方便了使用。

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 场景扩展

为了进一步拓展 Agent Telegram 的应用场景，我们可以考虑以下扩展：1. 引入多语言支持，使得 Agent Telegram 能够支持多语言用户，提高国际化程度；2. 开发一个基于 Web 的管理界面，允许管理员查看和监控团队通信情况，进行权限管理；3. 集成第三方服务，如日历、待办事项等，使得 Agent Telegram 能够发送提醒和通知，成为团队协作的一个中心节点。

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 常见问题

### Q1: 如何开始使用Agent Telegram？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Agent Telegram有什么限制？
A: 请参考已知限制章节了解具体限制。

## 用户体验亮点

为了提升用户体验，我们可以考虑以下改进措施：1. 设计一套更加友好的用户界面，使得 Agent Telegram 的操作更加直观；2. 提供个性化配置选项，允许用户自定义消息格式和 emoji；3. 开发一个消息归档功能，方便用户查看历史消息；4. 引入机器学习算法，根据用户行为自动优化消息发送策略。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
