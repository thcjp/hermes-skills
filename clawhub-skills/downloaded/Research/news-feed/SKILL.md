---
slug: news-feed
name: news-feed
version: "1.0.0"
displayName: Simple news feed reader (RSS)
summary: Fetch latest news headlines from major RSS feeds (BBC, Reuters, AP, Al Jazeera,
  NPR, The Guardian...
license: MIT
description: |-
  Fetch latest news headlines from major RSS feeds (BBC, Reuters, AP,
  Al Jazeera, NPR, The Guardian...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: feed, reader, headlines, (rss), simple, fetch, news, latest
tags:
- Research
tools:
- read
- exec
---

# Simple news feed reader (RSS)

Fetch current news headlines and summaries from major international RSS feeds. Zero API keys, zero dependencies — uses only Python stdlib and HTTP.

## Available Commands

### Command: news

**What it does:** Fetch latest headlines from all configured feeds (or a specific source).
**How to execute:**

```bash
python3 {baseDir}/scripts/news.py
```

### Command: news from a specific source

**What it does:** Fetch headlines from one source only.
**How to execute:**

```bash
python3 {baseDir}/scripts/news.py --source bbc
python3 {baseDir}/scripts/news.py --source reuters
python3 {baseDir}/scripts/news.py --source ap
python3 {baseDir}/scripts/news.py --source guardian
python3 {baseDir}/scripts/news.py --source aljazeera
python3 {baseDir}/scripts/news.py --source npr
python3 {baseDir}/scripts/news.py --source dw
```

### Command: news by topic

**What it does:** Fetch headlines filtered to a specific topic/keyword.

```bash
python3 {baseDir}/scripts/news.py --topic "climate"
python3 {baseDir}/scripts/news.py --source bbc --topic "ukraine"
```

### Command: news with more items

**What it does:** Control how many items per feed (default 8).

```bash
python3 {baseDir}/scripts/news.py --limit 20
```

### Command: list sources

**What it does:** Show all available feed sources and their categories.

```bash
python3 {baseDir}/scripts/news.py --list-sources
```

## Available Sources

| Source | Categories |
| --- | --- |
| bbc | top, world, business, tech, science, health |
| reuters | top, world, business, tech, science, health |
| ap | top |
| guardian | top, world, business, tech, science |
| aljazeera | top |
| npr | top |
| dw | top |

## When to Use

* User asks for latest news, current events, headlines
* User wants a news briefing or daily digest
* User asks "what's happening in the world"
* User asks about news on a specific topic
* User asks for a morning briefing

## Output Format

Returns markdown with headlines, short descriptions, publication times, and links. Grouped by source.

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
