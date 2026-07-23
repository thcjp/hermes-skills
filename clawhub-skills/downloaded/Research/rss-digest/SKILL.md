---
slug: rss-digest
name: rss-digest
version: "0.2.1"
displayName: Rss Digest
summary: Agentic RSS digest using the feed CLI. Fetch, triage, and summarize RSS feeds
  to surface high-sig...
license: MIT
description: |-
  Agentic RSS digest using the feed CLI。Fetch, triage, and summarize
  RSS feeds to surface high-sig。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Rss Digest

Surface what's worth reading from RSS feeds. Requires `feed` CLI (`brew install odysseus0/tap/feed`).

## Workflow

1. **Scan** — `feed get entries --limit 50` for recent unread (title, feed, date, URL, summary). Auto-fetches if stale. If 0 results, run `feed get stats` — if 0 feeds, import starter set: `feed import https://github.com/odysseus0/feed/raw/main/hn-popular-blogs-2025.opml` and retry.
2. **Triage** — Pick 5-10 high-signal posts based on the user's prompt. If no specific interest given, prioritize surprising, contrarian, or unusually insightful pieces.
3. **Read + Synthesize** — For each picked entry, read the full content and summarize in 2-3 sentences. Prefer fetching the URL directly (e.g. WebFetch) if available — keeps full text out of context. Otherwise use `feed get entry <id>` to read the stored content. Parallelize when possible.
4. **Present** — Compile the summaries into a digest. Group by theme if natural clusters emerge.

## Commands

```text
feed get entries --limit N              # list unread entries (table)
feed get entries --feed <id> --limit N  # filter by feed
feed get entry <id>                     # read full post (markdown)
feed fetch                              # pull latest from all feeds
feed search "<query>"                   # full-text search
feed update entries --read <id> ...     # batch mark read
feed get feeds                          # list feeds with unread counts
feed get stats                          # database stats
```

## Notes

* The entries table includes full URLs. Prefer fetching URLs directly (keeps full text out of your context window). Fall back to `feed get entry <id>` if you don't have a web fetch tool.
* Do NOT mark entries as read. The user decides what to mark read.
* Default output is table — most token-efficient for scanning. Avoid `-o json`.
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

- Agentic RSS digest using the feed CLI
- Fetch, triage, and summarize
  RSS feeds to surface high-sig
- 触发关键词: agentic, using, feed, rss, fetch, digest

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

### Q1: 如何开始使用Rss Digest？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Rss Digest有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
