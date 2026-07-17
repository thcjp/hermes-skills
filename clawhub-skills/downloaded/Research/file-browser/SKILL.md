---
slug: file-browser
name: file-browser
version: "1.0.0"
displayName: file-browser
summary: Read-only file browsing and reading in the OpenClaw workspace (/home/alfred/.openclaw/workspace)....
license: MIT-0
description: |-
  Read-only file browsing and reading in the OpenClaw workspace (/home/alfred/.openclaw/workspace)....

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: read, reading, browsing, file, browser, file-browser
tags:
- Research
tools:
- read
- exec
---

# file-browser

## Quick Start

Resolve all paths relative to WORKSPACE=/home/alfred/.skill-platform/workspace. Sanitize inputs to prevent escapes or absolutes.

* To list directory: exec("scripts/list_files.sh", [rel_path]) → JSON {success: bool, data: array of names, error: string}
* To read file: exec("scripts/read_file.sh", [rel_path]) → JSON {success: bool, data: string (text content), error: string}
* Handle errors: For binary/large/non-text files, return error JSON.

## Step-by-Step Workflow

1. Parse user query for action (list/read) and relative path.
2. Call appropriate script with sanitized rel_path.
3. Parse JSON output; respond to user with results or error message.
4. If path invalid or outside workspace, reject immediately.

## Safety Guidelines

* Enforce read-only: No writes, deletes, or exec beyond scripts.
* Log accesses if verbose mode enabled.
* For large files (>10k chars), truncate or summarize.

## Edge Cases

* Empty path: Default to "." (workspace root).
* Binary file: Return error "Non-text file".
* See references/examples.md for more (if added).

## Bundled Resources

* scripts/list_files.sh: Bash wrapper for ls.
* scripts/read_file.sh: Bash wrapper for cat with limits.

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
