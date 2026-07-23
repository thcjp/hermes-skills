---
slug: rss-feed-digest
name: rss-feed-digest
version: "1.0.0"
displayName: RSS Feed Digest
summary: "获取过滤总结RSS/Atom订阅为每日或每周摘要,支持多源聚合,解决信息过载"
  digest. Supports multipl...
license: MIT
description: |-
  Fetch, filter, and summarize RSS/Atom feeds into a clean daily or weekly
  digest。Supports multipl。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L1-入门级"
pricing_model: "per_use"
suggested_price: 9.9
---


# RSS Feed Digest

Aggregate multiple RSS/Atom feeds into a clean, summarized digest. Perfect for automated newsletters, news monitoring, or daily briefings.

## Usage

### Fetch and display recent items

```bash
python3 {baseDir}/scripts/rss_digest.py fetch \
  --feeds "https://hnrss.org/frontpage" "https://feeds.arstechnica.com/arstechnica/technology-lab" \
  --hours 24 \
  --limit 20
```

### Filter by keywords

```bash
python3 {baseDir}/scripts/rss_digest.py fetch \
  --feeds "https://hnrss.org/frontpage" \
  --keywords "AI,LLM,agent,Skill平台" \
  --hours 48
```

### Output as Markdown file

```bash
python3 {baseDir}/scripts/rss_digest.py fetch \
  --feeds "https://hnrss.org/frontpage" \
  --output digest.md \
  --format markdown
```

### Use a feed list file

```bash
python3 {baseDir}/scripts/rss_digest.py fetch \
  --feed-file feeds.txt \
  --hours 24
```

## Features

* 📰 Supports RSS 2.0 and Atom feeds
* 🔍 Keyword filtering (include/exclude)
* 🔄 Deduplication across multiple feeds
* 📅 Time-based filtering (last N hours)
* 📝 Markdown or plain text output
* 📋 Feed list file support for managing many sources

## Dependencies

```bash
pip3 install feedparser
```

## 示例

```bash
https://hnrss.org/frontpage
https://feeds.arstechnica.com/arstechnica/technology-lab
https://www.artificialintelligence-news.com/feed/
https://openai.com/blog/rss.xml

python3 rss_digest.py fetch --feed-file feeds.txt --keywords "AI,LLM,GPT,Claude,agent" --hours 24 --output /tmp/daily-ai-digest.md
```

## Use Cases

* **Daily briefings**: Summarize industry news for your team
* **Newsletter automation**: Generate content for Beehiiv/Substack newsletters
* **Competitive monitoring**: Track mentions of competitors or keywords
* **Research**: Aggregate academic/industry feeds on a topic
* **Heartbeat integration**: Run during Skill平台 heartbeat to check for relevant news

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

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用RSS Feed Digest？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: RSS Feed Digest有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
