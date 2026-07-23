---
slug: rss-reader
name: rss-reader
version: "1.0.0"
displayName: RSS Reader
summary: "监控RSS与Atom订阅源进行内容研究,追踪博客、新闻、Newsletter,自动化信息采集"
  newsletters, and any fe...
license: MIT
description: |-
  Monitor RSS and Atom feeds for content research。Track blogs, news sites,
  newsletters, and any fe。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# RSS Reader

Monitor any RSS/Atom feed for content ideas, competitor tracking, and industry news.

## Quick Start

```bash
node scripts/rss.js add "https://example.com/feed.xml" --category tech

node scripts/rss.js check

node scripts/rss.js check --category tech

node scripts/rss.js list

node scripts/rss.js remove "https://example.com/feed.xml"
```

## Configuration

Feeds stored in `rss-reader/feeds.json`:

```json
{
  "feeds": [
    {
      "url": "https://example.com/feed.xml",
      "name": "Example Blog",
      "category": "tech",
      "enabled": true,
      "lastChecked": "2026-02-22T00:00:00Z",
      "lastItemDate": "2026-02-21T12:00:00Z"
    }
  ],
  "settings": {
    "maxItemsPerFeed": 10,
    "maxAgeDays": 7,
    "summaryEnabled": true
  }
}
```

## Use Cases

### Content Research

Monitor competitor blogs, industry publications, and thought leaders:

```bash
node scripts/rss.js add "https://competitor.com/blog/feed" --category competitors
node scripts/rss.js add "https://techcrunch.com/feed" --category news
node scripts/rss.js add "https://news.ycombinator.com/rss" --category tech

node scripts/rss.js check --since 24h --format ideas
```

### Newsletter Aggregation

Track newsletters and digests:

```bash
node scripts/rss.js add "https://newsletter.com/feed" --category newsletters
```

### Keyword Monitoring

Filter items by keywords:

```bash
node scripts/rss.js check --keywords "AI,agents,automation"
```

## Output Formats

### Default (list)

```text
[tech] Example Blog - "New Post Title" (2h ago)
  https://example.com/post-1
[news] TechCrunch - "Breaking News" (4h ago)
  https://techcrunch.com/article-1
```

### Ideas (content research mode)

```text
## Content Ideas from RSS (Last 24h)

### Tech
- **"New Post Title"** - [Example Blog]
  Key points: Point 1, Point 2, Point 3
  Angle: How this relates to your niche

### News
- **"Breaking News"** - [TechCrunch]
  Key points: Summary of the article
  Angle: Your take or response
```

### JSON (for automation)

```bash
node scripts/rss.js check --format json
```

## Popular Feeds by Category

### Tech/AI

* `https://news.ycombinator.com/rss` - Hacker News
* `https://www.reddit.com/r/artificial/.rss` - r/artificial
* `https://www.reddit.com/r/LocalLLaMA/.rss` - r/LocalLLaMA
* `https://openai.com/blog/rss.xml` - OpenAI Blog

### Marketing

* `https://www.reddit.com/r/Entrepreneur/.rss` - r/Entrepreneur
* `https://www.reddit.com/r/SaaS/.rss` - r/SaaS

### News

* `https://techcrunch.com/feed/` - TechCrunch
* `https://www.theverge.com/rss/index.xml` - The Verge

## Cron Integration

Set up daily feed checking via heartbeat or cron:

```text
// In HEARTBEAT.md
- Check RSS feeds once daily, summarize new items worth reading
```

Or via cron job:

```bash
clawdbot cron add --schedule "0 8 * * *" --task "Check RSS feeds and summarize: node /root/clawd/skills/rss-reader/scripts/rss.js check --since 24h --format ideas"
```

## Scripts

* `scripts/rss.js` - Main CLI for feed management
* `scripts/parse-feed.js` - Feed parser module (uses xml2js)

## Dependencies

```bash
npm install xml2js node-fetch
```

The script will prompt for installation if dependencies are missing.

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

- Monitor RSS and Atom feeds for content research
- Track blogs, news sites,
  newsletters, and any fe
- 触发关键词: atom, feeds, content, reader, monitor, rss, research

## 示例

### 示例1：基础用法

```
```bash
node scripts/rss.js add "https://example.com/feed.xml" --category tech

node scripts/rss.js check

node scripts/rss.js check --category tech

node scripts/rss.js list

node scripts/rss.js remove "https://example.com/feed.xml"
```
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用RSS Reader？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: RSS Reader有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
