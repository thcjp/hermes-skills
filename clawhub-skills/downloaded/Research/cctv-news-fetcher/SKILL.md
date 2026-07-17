---
slug: cctv-news-fetcher
name: cctv-news-fetcher
version: "1.0.0"
displayName: CCTV News Fetcher
summary: Fetch and parse news highlights from CCTV News Broadcast (Xinwen Lianbo)
  for a given date.
license: MIT
description: |-
  Fetch and parse news highlights from CCTV News Broadcast (Xinwen Lianbo)
  for a given date.

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: fetcher, highlights, parse, cctv, fetch, news
tags:
- Research
tools:
- read
- exec
---

# CCTV News Fetcher

This skill allows you to fetch summary titles and content from the CCTV News Broadcast for any specific date.

## Usage

You can ask the agent to:

* "Fetch CCTV news for 20250210"
* "Give me the news highlights for yesterday"

## Instructions

When the user asks for news from a specific date:

1. Format the date as `YYYYMMDD`. If the user says "yesterday" or "today", calculate the date relative to the current local time.
2. Execute the script at `{baseDir}/scripts/news_crawler.js` using `bun` or `node`.
   * Command: `bun {baseDir}/scripts/news_crawler.js <YYYYMMDD>`
3. Parse the JSON output and summarize it for the user. Group news by "Domestic" and "International" if possible based on titles, or just list the highlights.

## Configuration

The skill depends on `node-html-parser`.
Ensure `bun` is installed in the environment.

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
