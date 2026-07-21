---
slug: news-feed
name: news-feed
version: "1.0.0"
displayName: News Feed
summary: Fetch latest news headlines from major RSS feeds (BBC, Reuters, AP, Al Jazeera,
  NPR, The Guardian...
license: MIT
description: |-
  Fetch latest news headlines from major RSS feeds (BBC, Reuters, AP,
  Al Jazeera, NPR, The Guardian。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Research
tools:
  - - read
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

- Fetch latest news headlines from major RSS feeds (BBC, Reuters, AP,
  Al Jazeera, NPR, The Guardian
- 触发关键词: feed, reader, headlines, (rss), simple, fetch, news, latest

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

### Q1: 如何开始使用News Feed？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: News Feed有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
