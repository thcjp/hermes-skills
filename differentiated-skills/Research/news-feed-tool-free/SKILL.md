---
slug: news-feed-tool-free
name: news-feed-tool-free
version: "1.0.0"
displayName: RSS新闻订阅免费版
summary: 从主流国际RSS源获取最新新闻标题与摘要，零API密钥零依赖
license: MIT
edition: free
description: |-
  RSS新闻订阅免费版，从BBC、Reuters、AP等主流国际媒体RSS源获取最新新闻标题与摘要。

  核心能力:
  - 从7个国际主流媒体RSS源获取新闻
  - 支持按来源、主题、数量筛选
  - 零API密钥、零外部依赖
  - 仅使用Python标准库和HTTP

  适用场景:
  - 个人用户浏览国际新闻
  - 学生了解全球时事
  - 独立开发者跟踪国际动态

  差异化:
  - 免费版零成本使用，纯Python标准库实现
  - 覆盖7个主流国际RSS源
  - 与PRO版本完全兼容，可平滑升级

  触发关键词: RSS新闻, 新闻订阅, BBC, Reuters, 国际新闻, news feed, headlines
tags:
- 新闻
- RSS
- 国际新闻
- 订阅
tools:
- read
- exec
---

# RSS新闻订阅工具（免费版）

## 概述

RSS新闻订阅工具免费版是一款轻量级的国际新闻获取工具，通过 RSS 协议从 BBC、Reuters、AP、The Guardian 等主流国际媒体获取最新新闻标题和摘要。零 API 密钥、零外部依赖，仅使用 Python 标准库和 HTTP 协议即可运行，适合个人用户快速浏览国际新闻动态。

本版本覆盖 7 个国际主流媒体 RSS 源，支持按来源、主题和数量筛选。如需更多 RSS 源、定时推送和内容聚合等高级能力，可升级至 PRO 版本。

## 核心能力

### RSS 源列表

| 来源 | 可用分类 | 说明 |
|:-----|:---------|:-----|
| BBC | top, world, business, tech, science, health | 英国广播公司 |
| Reuters | top, world, business, tech, science, health | 路透社 |
| AP | top | 美联社 |
| The Guardian | top, world, business, tech, science | 卫报 |
| Al Jazeera | top | 半岛电视台 |
| NPR | top | 美国国家公共广播 |
| DW | top | 德国之声 |

### 免费版能力边界

```text
[支持] 7个国际RSS源新闻获取
[支持] 按来源筛选（--source）
[支持] 按主题筛选（--topic）
[支持] 控制每源条目数（--limit）
[支持] 列出所有可用源（--list-sources）
[限制] 不支持国内RSS源
[限制] 不支持定时自动获取
[限制] 不支持新闻内容全文抓取
[限制] 不支持多源去重与聚合
```

## 使用场景

### 场景一：获取全部源最新新闻

用户希望一次获取所有配置的 RSS 源的最新新闻。

```text
用户：帮我获取最新的国际新闻

Agent 执行流程：
1. 执行 news.py 脚本
2. 从所有7个RSS源获取最新新闻
3. 按来源分组输出
4. 包含标题、摘要、时间和链接
```

示例命令：

```bash
python3 {baseDir}/scripts/news.py
```

示例输出：

```markdown
## BBC News

1. **Global Climate Summit Reaches Historic Agreement**
   - Published: 2026-07-18 08:30 GMT
   - Summary: 195 countries agree on binding emission targets...
   - Link: https://bbc.com/news/...

2. **Tech Giants Face New Antitrust Rules**
   - Published: 2026-07-18 07:15 GMT
   - Summary: EU announces sweeping new regulations...
   - Link: https://bbc.com/news/...

## Reuters

1. **Markets Rally on Fed Decision**
   - Published: 2026-07-18 09:00 GMT
   - Summary: Global stocks surge after Federal Reserve...
   - Link: https://reuters.com/...
```

### 场景二：按来源获取新闻

用户只想看某个特定媒体的新闻。

```text
用户：帮我看看BBC今天的新闻

Agent：
1. 执行带 --source 参数的脚本
2. 仅获取BBC的RSS新闻
3. 输出标题和摘要
```

```bash
python3 {baseDir}/scripts/news.py --source bbc
```

### 场景三：按主题筛选

用户关注某个特定主题的新闻。

```text
用户：帮我获取关于"climate"的新闻

Agent：
1. 执行带 --topic 参数的脚本
2. 从所有源获取新闻
3. 筛选包含"climate"的条目
4. 输出匹配结果
```

```bash
python3 {baseDir}/scripts/news.py --topic "climate"
```

## 快速开始

### 步骤一：列出可用源

```bash
python3 {baseDir}/scripts/news.py --list-sources
```

输出示例：

```text
Available News Sources:
  bbc        - BBC News (top, world, business, tech, science, health)
  reuters    - Reuters (top, world, business, tech, science, health)
  ap         - Associated Press (top)
  guardian   - The Guardian (top, world, business, tech, science)
  aljazeera  - Al Jazeera (top)
  npr        - NPR (top)
  dw         - Deutsche Welle (top)
```

### 步骤二：获取新闻

```bash
# 获取所有源的最新新闻（默认每源8条）
python3 {baseDir}/scripts/news.py

# 获取特定源的新闻
python3 {baseDir}/scripts/news.py --source bbc

# 按主题筛选
python3 {baseDir}/scripts/news.py --topic "technology"

# 控制每源条目数
python3 {baseDir}/scripts/news.py --limit 20
```

### 步骤三：组合筛选

```bash
# 获取BBC关于乌克兰的报道
python3 {baseDir}/scripts/news.py --source bbc --topic "ukraine"

# 获取Guardian科技类新闻，最多15条
python3 {baseDir}/scripts/news.py --source guardian --topic "tech" --limit 15
```

## 配置示例

### RSS源配置

```python
# feeds.py - RSS源配置
FEEDS = {
    "bbc": {
        "name": "BBC News",
        "feeds": {
            "top": "http://feeds.bbci.co.uk/news/rss.xml",
            "world": "http://feeds.bbci.co.uk/news/world/rss.xml",
            "business": "http://feeds.bbci.co.uk/news/business/rss.xml",
            "tech": "http://feeds.bbci.co.uk/news/technology/rss.xml",
            "science": "http://feeds.bbci.co.uk/news/science/rss.xml",
            "health": "http://feeds.bbci.co.uk/news/health/rss.xml",
        }
    },
    "reuters": {
        "name": "Reuters",
        "feeds": {
            "top": "https://www.reuters.com/rssFeed/topNews",
            "world": "https://www.reuters.com/rssFeed/worldNews",
            "business": "https://www.reuters.com/rssFeed/businessNews",
            "tech": "https://www.reuters.com/rssFeed/technologyNews",
        }
    },
    "ap": {
        "name": "Associated Press",
        "feeds": {
            "top": "https://apnews.com/rss/apf-topnews.xml",
        }
    },
    "guardian": {
        "name": "The Guardian",
        "feeds": {
            "top": "https://www.theguardian.com/world/rss",
            "world": "https://www.theguardian.com/international/rss",
            "business": "https://www.theguardian.com/business/rss",
            "tech": "https://www.theguardian.com/technology/rss",
            "science": "https://www.theguardian.com/science/rss",
        }
    },
    "aljazeera": {
        "name": "Al Jazeera",
        "feeds": {
            "top": "https://www.aljazeera.com/xml/rss/all.xml",
        }
    },
    "npr": {
        "name": "NPR",
        "feeds": {
            "top": "https://feeds.npr.org/1001/rss.xml",
        }
    },
    "dw": {
        "name": "Deutsche Welle",
        "feeds": {
            "top": "https://rss.dw.com/rdf/rss-en-all",
        }
    }
}

DEFAULT_LIMIT = 8  # 每源默认获取条目数
```

### 输出格式配置

```python
# output_format.py - 输出格式
OUTPUT_TEMPLATE = """
## {source_name}

{items}
"""

ITEM_TEMPLATE = """{index}. **{title}**
   - Published: {pub_date}
   - Summary: {description}
   - Link: {link}
"""
```

## 最佳实践

### 1. 合理使用 --limit 参数

```bash
# 推荐 - 适度获取
python3 {baseDir}/scripts/news.py --limit 10

# 不推荐 - 获取过多导致信息过载
python3 {baseDir}/scripts/news.py --limit 100
```

### 2. 善用主题筛选

```bash
# 精准筛选感兴趣的主题
python3 {baseDir}/scripts/news.py --topic "artificial intelligence"
python3 {baseDir}/scripts/news.py --topic "climate change"
python3 {baseDir}/scripts/news.py --topic "space exploration"
```

### 3. 按来源偏好选择

```bash
# 偏好英国视角
python3 {baseDir}/scripts/news.py --source bbc --source guardian

# 偏好美国视角
python3 {baseDir}/scripts/news.py --source ap --source npr

# 偏好中东视角
python3 {baseDir}/scripts/news.py --source aljazeera
```

### 4. 多源对比

```bash
# 获取多个源关于同一主题的报道
python3 {baseDir}/scripts/news.py --source bbc --topic "ukraine"
python3 {baseDir}/scripts/news.py --source reuters --topic "ukraine"
python3 {baseDir}/scripts/news.py --source aljazeera --topic "ukraine"
```

## 常见问题

### Q1：免费版需要安装额外的 Python 包吗？

不需要。免费版仅使用 Python 标准库（urllib、xml.etree、html.parser 等），无需 pip install 任何第三方包。

### Q2：RSS 源无法访问怎么办？

部分国际 RSS 源可能需要网络代理才能访问。请确认网络环境是否可以正常访问目标媒体网站。

```bash
# 测试RSS源连通性
curl -s -o /dev/null -w "%{http_code}" http://feeds.bbci.co.uk/news/rss.xml
# 预期输出: 200
```

### Q3：免费版支持国内新闻源吗？

免费版仅支持 7 个国际主流媒体 RSS 源。如需国内新闻源（新华社、央视等），请升级至 PRO 版本。

### Q4：新闻数据是否实时？

RSS 源的更新频率取决于各媒体，通常为 15-60 分钟更新一次。免费版在执行时获取 RSS 源当前内容。

### Q5：免费版与 PRO 版本的区别？

| 对比项 | 免费版 | PRO 版本 |
|:-------|:-------|:---------|
| RSS源数量 | 7个国际源 | 50+国内外源 |
| 国内源 | 不支持 | 完整支持 |
| 定时获取 | 不支持 | 支持自动获取 |
| 内容抓取 | 仅标题摘要 | 全文抓取 |
| 多源去重 | 不支持 | 智能去重 |
| 导出格式 | 终端输出 | MD/PDF/Email |
| API 集成 | 不支持 | REST API |

## 依赖说明

### 运行环境

- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.6 及以上（仅使用标准库）
- **网络连接**: 需要可访问国际互联网以获取 RSS 源

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Python 3.6+ | 运行时 | 必需 | 系统包管理器安装 |
| Python 标准库 | 内置 | 必需 | Python 自带（urllib, xml, html） |

### API Key 配置

免费版零 API Key 设计，所有 RSS 源均为公开免费服务，无需任何认证配置。

```bash
# 验证Python环境
python3 --version
# 预期输出: Python 3.6+

# 验证标准库可用
python3 -c "import urllib.request, xml.etree.ElementTree; print('OK')"
# 预期输出: OK

# 验证RSS源连通性
curl -s -o /dev/null -w "%{http_code}" http://feeds.bbci.co.uk/news/rss.xml
# 预期输出: 200
```

### 可用性分类

- **分类**: MD+EXEC（纯 Markdown 指令 + Python 脚本执行）
- **说明**: 基于 Python 标准库通过 HTTP 获取 RSS 源新闻，零外部依赖
- **适用规模**: 个人用户、轻量级国际新闻浏览场景
- **特殊优势**: 零成本、零依赖、零配置，开箱即用
- **升级路径**: 可无缝升级至 news-feed-tool-pro 获取国内外源与定时获取能力
