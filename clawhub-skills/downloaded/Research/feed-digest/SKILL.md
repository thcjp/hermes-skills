---
slug: feed-digest
name: feed-digest
version: "1.0.0"
displayName: Feed Digest
summary: This skill is a straightforward feed digest helper with disclosed feed fetching
  and read-status c...
license: MIT
description: |-
  This skill is a straightforward feed digest helper with disclosed feed
  fetching and read-status c。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Research
tools:
  - - read
- exec
---

# Feed Digest

Surface what's worth reading from your feeds. Requires `feed` CLI (`brew install odysseus0/tap/feed`).

## Workflow

1. **Fetch** — `feed fetch` to pull latest entries.
2. **Scan** — `feed get entries --limit 50` for recent unread (title, feed, date, summary).
3. **Triage** — Pick 5-10 high-signal posts. Prioritize: AI progress, systems engineering, developer tools, anything surprising or contrarian.
4. **Read** — `feed get entry <id>` for each pick (full post as Markdown).
5. **Synthesize** — For each post: title, source, 2-3 sentence summary of why it matters. Group by theme if natural clusters emerge.
6. **Mark read** — `feed update entries --read <id1> <id2> ...` to mark triaged entries as read.

## Commands

```text
feed fetch                              # pull latest from all feeds
feed get entries --limit N              # list unread entries (table)
feed get entries --feed <id> --limit N  # filter by feed
feed get entry <id>                     # read full post (Markdown)
feed search "<query>"                   # full-text search
feed update entries --read <id> ...     # batch mark read
feed get feeds                          # list feeds with unread counts
feed get stats                          # database stats
```

## Notes

* Default output is table — most token-efficient for scanning. Avoid `-o json`.
* `feed get entry <id>` returns Markdown — read this for the actual post content.
* Filter by feed if too many entries: `--feed <feed_id>`.

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

- This skill is a straightforward feed digest helper with disclosed feed
  fetching and read-status c
- 触发关键词: straightforward, digest, skill, feed

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

### Q1: 如何开始使用Feed Digest？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Feed Digest有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
