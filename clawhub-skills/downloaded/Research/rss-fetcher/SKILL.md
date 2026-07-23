---
slug: rss-fetcher
name: rss-fetcher
version: "1.1.0"
displayName: Rss Fetcher
summary: 统一的RSS采集与管理系统 | Unified RSS Feed Fetcher and Manager 支持增量抓取、自动去重、自动标签、源健康监控、HTML报告生成
  Incremental ...
license: MIT-0
description: |-
  统一的RSS采集与管理系统 | Unified RSS Feed Fetcher and Manager 支持增量抓取、自动去重、自动标签、源健康监控、HTML报告生成\
  \ Incremental 。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。
tags: '[''Research'', ''Lifestyle'']'
tools:
  - read
  - exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# RSSééå¨ | RSS Fetcher

## 核心能力

* **增量抓取 / Incremental Fetching** - 只抓取新文章，基于URL哈希自动去重 | Only fetch new articles, auto-deduplicate based on URL hash
* **自动标签 / Auto-tagging** - 优先使用RSS自带category，无则自动提取标题关键词 | Prioritize RSS category, auto-extract keywords from title if absent
* **HTML报告 / HTML Reports** - 生成可筛选的静态HTML页面，支持日期/分类/标签多维度筛选 | Generate filterable static HTML pages with date/category/tag filters
* **源健康监控 / Source Health Monitoring** - 检测RSS源可用性，支持批量检查 | Monitor RSS source availability with batch checking
* **分类管理 / Category Management** - 文章自动继承源的分类，支持多维度筛选 | Articles inherit source categories, multi-dimensional filtering
* **超时设置 / Timeout Setting** - 单源30秒超时，避免长时间阻塞 | 30-second timeout per source to avoid blocking

---

## 数据库设计 | Database Design

### 表结构 | Table Structure

| 表名 / Table | 用途 / Purpose | 核心字段 / Core Fields |
| --- | --- | --- |
| `articles` | 文章主数据 / Article data | id, source_id, **category**, title, url, published_at |
| `tags` | 标签定义 / Tag definitions | id, name |
| `article_tags` | 文章-标签关联 / Article-tag relation | article_id, tag_id |
| `fetch_logs` | 抓取日志 / Fetch logs | source_id, started_at, found, new, status |

**说明 / Note**: RSS源通过 `config/sources.json` 文件管理，不存入数据库 | RSS sources are managed via `config/sources.json` file, not in database

### 关键设计 | Key Design

* **时间戳使用 INTEGER (Unix时间戳)** - 查询更快、比较更简单 | INTEGER Unix timestamps for faster queries
* **published_at NOT NULL** - 必填，缺失时标记为 UNRELIABLE_TIME (1970-01-01) | Required, marked as UNRELIABLE_TIME if missing
* **URL唯一索引 / URL Unique Index** - 确保去重 | Ensure deduplication
* **多标签支持 / Multi-tag Support** - 一篇文章可拥有多个标签 | Multiple tags per article
* **category字段 / Category Field** - 继承自sources.json的分类配置 | Inherited from sources.json configuration

---

## 使用流程

### 1. 初始化数据库 | Initialize Database

```bash
cd skills/rss_fetcher
python3 scripts/init_db.py
```

### 2. 配置RSS源 | Configure RSS Sources

编辑 `config/sources.json`，添加你的RSS源：
Edit `config/sources.json` to add your RSS sources:

```json
{
  "sources": [
    {
      "id": "openai",
      "name": "OpenAI Blog",
      "url": "https://openai.com/blog/rss.xml",
      "category": "tech",
      "enabled": true
    }
  ]
}
```

### 3. 执行抓取 | Execute Fetch

```bash
python3 scripts/fetch.py

python3 scripts/fetch.py --sources openai huggingface

python3 scripts/fetch.py --hours 48

python3 scripts/fetch.py --workers 50
```

**⚠️ 抓取后记得更新HTML报告** - 新抓取的文章需要重新生成页面才能在浏览器中查看
**⚠️ Remember to update HTML report after fetching** - New articles require regeneration to view in browser

```bash
python3 scripts/fetch.py && python3 scripts/generate_html.py
```

### 4. 生成HTML报告 | Generate HTML Report

**注意：每次抓取新文章后，必须重新生成HTML页面才能看到最新内容。**
**Note: Must regenerate HTML after fetching new articles to see latest content.**

```bash
python3 scripts/fetch.py && python3 scripts/generate_html.py

python3 scripts/generate_html.py

open data/index.html  # Mac
```

**HTML报告功能 / HTML Report Features**:

* 📅 **日期筛选 / Date Filter** - 起止日期选择 | Start/end date selection
* 🏷️ **分类筛选 / Category Filter** - 按文章分类筛选 | Filter by article category
* 🔍 **关键词搜索 / Keyword Search** - 实时搜索标题 | Real-time title search
* ☑️ **标签多选 / Multi-tag Selection** - 多标签组合筛选（AND逻辑）| Multi-tag combo filter (AND logic)
* 📊 **实时统计 / Real-time Stats** - 显示筛选结果数量 | Show filtered results count

### 5. 源管理 | Source Management

```bash
python3 scripts/source.py check

python3 scripts/source.py stats

python3 scripts/source.py add myblog "My Blog" "https://example.com/feed.xml" tech

python3 scripts/source.py disable myblog
python3 scripts/source.py enable myblog
python3 scripts/source.py remove myblog
```

### 6. 查看文章列表 | View Article List

```bash
python3 scripts/list.py

python3 scripts/list.py --hours 48

python3 scripts/list.py --category tech

python3 scripts/list.py --json
```

---

## 配置文件 | Configuration Files

### sources.json

```json
{
  "_description": "RSS源配置文件 | RSS source config file",
  "_updated": "2026-03-15",
  "_total_sources": 111,
  "sources": [
    {
      "id": "openai",
      "name": "OpenAI Blog",
      "url": "https://openai.com/blog/rss.xml",
      "category": "tech",
      "enabled": true
    }
  ]
}
```

**字段说明 / Field Description：**

* `id` - 源唯一标识 | Source unique identifier
* `name` - 显示名称 | Display name
* `url` - RSS订阅地址 | RSS feed URL
* `category` - 文章分类 | Article category
* `enabled` - 是否启用 | Whether enabled

**分类可自由定义**，在 `sources.json` 中使用任意分类名称即可。
**Categories can be freely defined** using any category name in `sources.json`.

---

## 自动标签系统 | Auto-tagging System

### 标签生成逻辑 | Tag Generation Logic

1. **优先使用RSS自带category** - 提取 `<category>` 标签内容
   **Prioritize RSS category** - Extract `<category>` tag content
2. **Fallback关键词提取** - 无category时从标题提取：
   **Fallback keyword extraction** - Extract from title if no category:
   * 规则匹配（AI/区块链/股票等预定义规则）| Rule matching (AI/blockchain/stocks etc.)
   * 名词提取（英文大写单词、中文词组）| Noun extraction (English caps, Chinese phrases)

### 预定义标签规则 | Predefined Tag Rules

| 关键词 / Keywords | 标签 / Tag |
| --- | --- |
| AI, GPT, 大模型, 机器学习 | AI |
| 区块链, 比特币, crypto | 区块链 / Blockchain |
| 股票, 股市, equity | 股票 / Stocks |
| 游戏, gaming, esports | 游戏 / Gaming |
| ... | ... |

规则定义在 `fetch.py` 的 `TAG_RULES` 中，可自由扩展。
Rules defined in `TAG_RULES` in `fetch.py`, freely extensible.

---

## 示例

### 获取今天所有文章 | Get Today's Articles

```sql
SELECT title, url, source_id
FROM articles
WHERE date(fetched_at, 'unixepoch') = date('now')
ORDER BY published_at DESC;
```

### 获取某分类的文章 | Get Articles by Category

```sql
SELECT * FROM articles
WHERE category = 'tech'
AND published_at > strftime('%s', 'now', '-24 hours');
```

### 获取带标签的文章 | Get Articles with Tags

```sql
SELECT a.title, a.url, GROUP_CONCAT(t.name) as tags
FROM articles a
LEFT JOIN article_tags at ON a.id = at.article_id
LEFT JOIN tags t ON at.tag_id = t.id
WHERE a.category = 'tech'
GROUP BY a.id;
```

### 获取热门标签 | Get Popular Tags

```sql
SELECT t.name, COUNT(*) as count
FROM tags t
JOIN article_tags at ON t.id = at.tag_id
GROUP BY t.id
ORDER BY count DESC;
```

---

## 文件位置 | File Locations

```text
rss_fetcher/
├── SKILL.md                    # 本文档 | This document
├── config/
│   └── sources.json           # RSS源配置 | RSS source config
├── scripts/
│   ├── init_db.py             # 数据库初始化 | DB initialization
│   ├── fetch.py               # 核心抓取脚本（含自动标签）| Core fetch script
│   ├── generate_html.py       # HTML报告生成 | HTML report generation
│   ├── source.py              # 源健康检查与管理 | Source health check
│   ├── list.py                # 终端文章列表 | Terminal article list
│   └── query.py               # 数据查询工具 | Data query tool
├── data/
│   ├── rss_fetcher.db         # SQLite数据库 | SQLite database
│   └── index.html             # 生成的HTML报告 | Generated HTML report
└── references/
    └── schema.sql             # 数据库结构参考 | DB schema reference
```

## 数据库位置 | Database Location

```text
rss_fetcher/data/rss_fetcher.db
```

---

## 已知限制

1. **首次抓取会比较慢** - 需要抓所有历史文章
   **First fetch is slow** - Need to fetch all historical articles
2. **SQLite并发** - 单进程访问，避免并发写入
   **SQLite concurrency** - Single process access, avoid concurrent writes
3. **时间不可靠文章** - published_at = 0 的文章需人工审核
   **Unreliable time articles** - Articles with published_at = 0 need manual review
4. **标签自动累积** - 随着文章增多，标签会自动丰富
   **Tags auto-accumulate** - Tags enrich as more articles are fetched
5. **定期重新生成HTML** - 抓取新文章后需重新运行 `generate_html.py`
   **Regularly regenerate HTML** - Must rerun `generate_html.py` after fetching new articles

---

*Part of Skill平台 Daily Research System*

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Rss Fetcher？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Rss Fetcher有什么限制？
A: 请参考已知限制章节了解具体限制。
