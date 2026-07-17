---
slug: rss-digest
name: rss-digest
version: "0.2.1"
displayName: Rss Digest
summary: Agentic RSS digest using the feed CLI. Fetch, triage, and summarize RSS feeds
  to surface high-sig...
license: MIT
description: |-
  Agentic RSS digest using the feed CLI. Fetch, triage, and summarize
  RSS feeds to surface high-sig...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: agentic, using, feed, rss, fetch, digest
tags:
- Research
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
