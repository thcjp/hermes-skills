---
slug: feed-to-md
name: feed-to-md
version: "1.2.0"
displayName: Feed To Md
summary: "将RSS或Atom订阅URL转为Markdown,使用本地转换脚本,离线生成可读文档"
  script. Use this wh...
license: MIT
description: |-
  Convert RSS or Atom feed URLs into Markdown using the bundled local
  converter script。Use this wh。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

- Convert RSS or Atom feed URLs into Markdown using the bundled local
  converter script
- Use this wh
- 触发关键词: convert, atom, urls, feed

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

### Q1: 如何开始使用Feed To Md？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Feed To Md有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 本地运行，不支持多设备同步
