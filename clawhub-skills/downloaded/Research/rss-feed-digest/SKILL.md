---
slug: rss-feed-digest
name: rss-feed-digest
version: "1.0.0"
displayName: RSS Feed Digest
summary: Fetch, filter, and summarize RSS/Atom feeds into a clean daily or weekly
  digest. Supports multipl...
license: MIT
description: |-
  Fetch, filter, and summarize RSS/Atom feeds into a clean daily or weekly
  digest. Supports multipl...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: atom, feeds, feed, summarize, rss, fetch, filter, digest
tags:
- Research
tools:
- read
- exec
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

## Example: Daily AI News Digest

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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
