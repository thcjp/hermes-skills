---
pricing_tier: L2
pricing_model: per_use
suggested_price: 19.9
---

# test

Use `wacli` only when the user explicitly asks you to message someone else on WhatsApp or when they ask to sync/search WhatsApp history.
Do NOT use `wacli` for normal user chats; Clawdbot routes WhatsApp conversations automatically.
If the user is chatting with you on WhatsApp, you should not reach for this tool unless they ask you to contact a third party.

Safety

* Require explicit recipient + message text.
* Confirm recipient + message before sending.
* If anything is ambiguous, ask a clarifying question.

Auth + sync

* `wacli auth` (QR login + initial sync)
* `wacli sync --follow` (continuous sync)
* `wacli doctor`

Find chats + messages

* `wacli chats list --limit 20 --query "name or number"`
* `wacli messages search "query" --limit 20 --chat <jid>`
* `wacli messages search "invoice" --after 2025-01-01 --before 2025-12-31`

History backfill

* `wacli history backfill --chat <jid> --requests 2 --count 50`

Send

* Text: `wacli send text --to "+14155551212" --message "Hello! Are you free at 3pm?"`
* Group: `wacli send text --to "1234567890-123456789@g.us" --message "Running 5 min late."`
* File: `wacli send file --to "+14155551212" --file /path/agenda.pdf --caption "Agenda"`

Notes

* Store dir: `~/.wacli` (override with `--store`).
* Use `--json` for machine-readable output when parsing.
* Backfill requires your phone online; results are best-effort.
* WhatsApp CLI is not needed for routine user chats; it’s for messaging other people.
* JIDs: direct chats look like `<number>@s.whatsapp.net`; groups look like `<id>@g.us` (use `wacli chats list` to find).

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

- Send WhatsApp messages to other people or search/sync WhatsApp history
  via the wacli CLI (not for
- 触发关键词: whatsapp, people, messages, send, other, test

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

### Q1: 如何开始使用test？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: test有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
