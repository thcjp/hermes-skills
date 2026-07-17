---
slug: feed-to-md
name: feed-to-md
version: "1.2.0"
displayName: Feed To Md
summary: Convert RSS or Atom feed URLs into Markdown using the bundled local converter
  script. Use this wh...
license: MIT
description: |-
  Convert RSS or Atom feed URLs into Markdown using the bundled local
  converter script. Use this wh...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: convert, atom, urls, feed
tags:
- Research
tools:
- read
- exec
---

# Feed To Md

Use this skill when the task is to convert an RSS/Atom feed URL into Markdown.

## What this skill does

* Converts a feed URL to Markdown via a bundled local script
* Supports stdout output or writing to a Markdown file
* Supports limiting article count and summary controls

## Inputs

* Required: RSS/Atom URL
* Optional:
  + output path
  + max item count
  + template preset (`short` or `full`)

## Usage

Run the local script:

```bash
python3 scripts/feed_to_md.py "<feed_url>"
```

Write to file:

```bash
python3 scripts/feed_to_md.py "https://example.com/feed.xml" --output feed.md
```

Limit to 10 items:

```bash
python3 scripts/feed_to_md.py "https://example.com/feed.xml" --limit 10
```

Use full template with summaries:

```bash
python3 scripts/feed_to_md.py "https://example.com/feed.xml" --template full
```

## Security rules (required)

* Never interpolate raw user input into a shell string.
* Always pass arguments directly to the script as separate argv tokens.
* URL must be `http` or `https` and must not resolve to localhost/private addresses.
* Every HTTP redirect target (and final URL) is re-validated and must also resolve to public IPs.
* Output path must be workspace-relative and end in `.md`.
* Do not use shell redirection for output; use `--output`.

Safe command pattern:

```bash
cmd=(python3 scripts/feed_to_md.py "$feed_url")
[[ -n "${output_path:-}" ]] && cmd+=(--output "$output_path")
[[ -n "${limit:-}" ]] && cmd+=(--limit "$limit")
[[ "${template:-short}" = "full" ]] && cmd+=(--template full)
"${cmd[@]}"
```

## Script options

* `-o, --output <file>`: write markdown to file
* `--limit <number>`: max number of articles
* `--no-summary`: exclude summaries
* `--summary-max-length <number>`: truncate summary length
* `--template <preset>`: `short` (default) or `full`

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
