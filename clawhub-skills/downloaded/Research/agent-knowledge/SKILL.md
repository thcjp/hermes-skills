---
slug: agent-knowledge
name: agent-knowledge
version: "1.0.0"
displayName: Agent Knowledge Capture
summary: Unified knowledge capture and retrieval for URLs, video/article/paper extracts,
  social posts, and...
license: MIT
description: |-
  Unified knowledge capture and retrieval for URLs, video/article/paper
  extracts, social posts, and...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: retrieval, knowledge, unified, urls, agent, capture
tags:
- Research
tools:
- read
- exec
---

# Agent Knowledge Capture

File-based knowledge organization. Capture fast, search later, clean up automatically.

## Installation

> 安装此Skill请参考SkillHub平台指南

This installs `scripts/know` — add to PATH or use full path:

```bash
~/.skill-platform/skills/knowledge/scripts/know
```

## Storage Location

Default: `~/.soulshare/agent/knowledge/`

Configurable via `~/.config/know/config` or env `KNOWLEDGE_DIR`.

```text
knowledge/
├── INDEX.md      # Auto-maintained browsable index
├── urls/         # Bookmarked URLs
├── extracts/     # Video/article/paper summaries
├── posts/        # Social content (tweets, threads)
└── research/     # Agent-generated research
```

## Adding Content

```bash
know add url <url> --title "..." --tags "a,b" [--summary "..."]
know add video <url> --title "..." --tags "a,b" [--summary "..."]
know add extract --source <url> --type video|article|paper --title "..." --tags "a,b"
know add post --source <url> --title "..." --tags "a,b"
know add research --title "..." --tags "a,b" [--summary "..."]
```

Each add writes a markdown file with YAML frontmatter and updates `INDEX.md`.

## Searching

```bash
know search "query"           # Grep across all entries
know recent --limit 10        # Recent entries
know list --tags security     # Filter by tag
```

## Cleanup & Maintenance

```bash
know tidy                     # Audit: find issues
know tidy --fix               # Auto-fix: normalize tags, move misplaced files, remove empty
know validate                 # Check frontmatter schema
know reindex                  # Rebuild INDEX.md
know config                   # Show active config paths
```

**Recommended:** Run `know tidy --fix` in heartbeats or nightly cron.

## Data Model (frontmatter)

```yaml
---
type: url|extract|post|research
title: "Entry title"
source_url: "https://..."
source_kind: url|video|article|paper|post|research
tags: ["tag1", "tag2"]
added: "2026-02-26"
added_by: "agent-name"
summary: "One-line summary"
---
```

## QMD Integration

Plain markdown → QMD-indexable.

```bash
qmd collection add ~/.soulshare/agent/knowledge --name knowledge
qmd search "query" --collection knowledge
```

## Discipline

* If it's useful later → `know add` immediately
* Don't leave knowledge only in `memory/YYYY-MM-DD.md`
* Every entry needs tags + summary
* Let `know tidy --fix` handle normalization

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
