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
  fetching and read-status c...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: straightforward, digest, skill, feed
tags:
- Research
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
