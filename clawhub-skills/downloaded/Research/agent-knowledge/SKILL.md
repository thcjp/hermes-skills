---
slug: agent-knowledge
name: agent-knowledge
version: "1.0.0"
displayName: Agent Knowledge
summary: Unified knowledge capture and retrieval for URLs, video/article/paper extracts,
  social posts, and...
license: MIT
description: |-
  Unified knowledge capture and retrieval for URLs, video/article/paper
  extracts, social posts, and。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。
tags:
- Research
tools:
  - - read
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

- Unified knowledge capture and retrieval for URLs, video/article/paper
  extracts, social posts, and
- 触发关键词: retrieval, knowledge, unified, urls, agent, capture

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

### Q1: 如何开始使用Agent Knowledge？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Agent Knowledge有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
