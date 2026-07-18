---
slug: news-feed-tool-pro
name: news-feed-tool-pro
version: "1.0.0"
displayName: RSS新闻订阅专业版
summary: 企业级RSS新闻平台，支持50+国内外源、定时获取、全文抓取与API集成
license: MIT
edition: pro
description: |-
  RSS新闻订阅工具专业版，面向企业用户提供50+国内外RSS源、定时自动获取、全文内容抓取与API集成能力。

  核心能力:
  - 50+国内外RSS源（含国内主流媒体）
  - 定时自动获取与突发新闻触发
  - 全文内容抓取与智能摘要
  - 多源去重与主题聚类
  - 多格式导出（Markdown/PDF/Email/Webhook）
  - REST API 集成与自动化工作流
  - 自定义RSS源接入与管理

  适用场景:
  - 企业新闻监控与情报收集
  - 媒体机构多源新闻采编
  - 行业研究信息聚合
  - 品牌舆情实时追踪

  差异化:
  - PRO 版本与免费版完全兼容，支持平滑升级
  - 新增国内RSS源、定时获取、全文抓取等企业级能力
  - 支持自定义RSS源与API集成
  - 提供优先技术支持与定制化服务

  触发关键词: RSS订阅, 定时获取, 新闻全文, 多源去重, 国内RSS, 自定义RSS, news feed pro
tags:
- 新闻
- RSS
- 企业级
- 定时获取
- 全文抓取
tools:
- read
- exec
---

# RSS新闻订阅工具（专业版）

## 概述

RSS新闻订阅工具专业版在免费版 7 个国际 RSS 源的基础上，新增 50+ 国内外 RSS 源、定时自动获取、全文内容抓取、多源去重与主题聚类、多格式导出和 REST API 集成等企业级能力，满足企业新闻监控、媒体采编和行业情报收集的深度需求。

PRO 版本与免费版完全兼容，用户可随时从免费版平滑升级，原有 RSS 源配置均可无缝迁移。

## 核心能力

### 能力矩阵

| 能力项 | 免费版 | PRO 版本 |
|:-------|:-------|:---------|
| RSS源数量 | 7个国际源 | 50+国内外源 |
| 国内源 | 不支持 | 完整支持 |
| 定时获取 | 不支持 | 多时段自动获取 |
| 突发推送 | 不支持 | 实时触发推送 |
| 内容抓取 | 仅标题摘要 | 全文抓取+摘要 |
| 多源去重 | 不支持 | 智能去重+聚类 |
| 导出格式 | 终端输出 | MD/PDF/Email/Webhook |
| 自定义源 | 不支持 | 支持接入管理 |
| API 集成 | 不支持 | REST API |
| 主题聚类 | 不支持 | 自动聚类分析 |
| 历史检索 | 不支持 | 90天历史检索 |
| 多语言 | 英文为主 | 中/英/日/韩多语言 |

### PRO 专属 RSS 源

```text
[PRO] 国内媒体：新华社、央视新闻、澎湃新闻、36氪、IT之家
[PRO] 国内科技：机器之心、量子位、InfoQ、CSDN
[PRO] 国内财经：财联社、证券时报、第一财经
[PRO] 国际科技：TechCrunch、The Verge、Ars Technica、Hacker News
[PRO] 国际财经：Bloomberg、Financial Times、Wall Street Journal
[PRO] 多语言源：日经新闻(Nikkei)、韩联社(Yonhap)、德国之声(DW)
[PRO] 行业垂直：自定义行业RSS源
```

## 使用场景

### 场景一：企业新闻情报中心

企业需要建立全面的新闻情报获取体系，覆盖国内外多个媒体渠道。

```python
# intelligence_config.py - 新闻情报配置
intelligence_sources = {
    "brand_monitoring": {
        "sources": ["all_domestic", "all_international"],
        "keywords": ["企业名称", "品牌名", "CEO", "产品名"],
        "alert_on_match": True,
        "credibility_filter": "B"
    },
    "competitor_tracking": {
        "sources": ["36kr", "techcrunch", "reuters"],
        "keywords": ["竞品A", "竞品B", "竞品C"],
        "daily_digest": True
    },
    "industry_news": {
        "sources": ["jiqizhixin", "techcrunch", "theverge"],
        "topics": ["AI", "云计算", "半导体"],
        "weekly_summary": True
    },
    "regulatory_monitoring": {
        "sources": ["xinhua", "cctv", "reuters"],
        "keywords": ["监管", "政策", "法规", "合规"],
        "immediate_alert": True
    }
}
```

### 场景二：定时多源聚合

媒体机构需要定时从多个 RSS 源获取新闻，自动去重后生成采编参考。

```bash
# 配置定时聚合
cat > ~/news-feed-pro/schedules/editorial.yaml << 'EOF'
schedules:
  # 早间国际新闻聚合
  - name: "intl_morning"
    cron: "0 6 * * 1-5"
    sources: [bbc, reuters, ap, guardian, aljazeera]
    max_items: 15
    deduplicate: true
    full_text: false
    output:
      format: markdown
      path: "~/news-feed-pro/reports/intl_morning_{date}.md"

  # 午间国内科技新闻
  - name: "tech_noon"
    cron: "0 12 * * 1-5"
    sources: [36kr, jiqizhixin, ithome, baijia]
    max_items: 20
    deduplicate: true
    full_text: true
    output:
      format: pdf
      path: "~/news-feed-pro/reports/tech_noon_{date}.pdf"
      email_to: ["editor@media.local"]

  # 晚间综合简报
  - name: "comprehensive_evening"
    cron: "0 18 * * 1-5"
    sources: all
    max_items: 30
    deduplicate: true
    cluster: true
    output:
      format: markdown
      path: "~/news-feed-pro/reports/evening_{date}.md"
      webhook: "https://hooks.editorial.local/news"
EOF
```

### 场景三：全文抓取与智能摘要

用户需要获取新闻全文而不仅仅是标题摘要。

```text
用户：获取BBC关于"AI监管"的新闻全文并生成摘要

Agent 执行流程：
1. 从BBC RSS源获取匹配"AI监管"的新闻
2. 逐条抓取新闻全文
3. 使用AI生成智能摘要（每篇200字以内）
4. 输出含全文链接和摘要的报告
```

示例输出：

```markdown
## AI监管新闻全文摘要 (2026-07-18)

### 1. EU Passes Landmark AI Regulation
**来源**: BBC | **时间**: 2026-07-18 08:30 GMT
**智能摘要**: 欧盟通过《人工智能法案》，对高风险AI系统实施严格
监管要求，包括透明度义务、人类监督和定期审计。法案将于2026年底
生效，违规企业最高面临全球营业额6%的罚款。
**全文链接**: https://bbc.com/news/...

### 2. US Considers Federal AI Framework
**来源**: Reuters | **时间**: 2026-07-18 10:00 GMT
**智能摘要**: 美国国会正在讨论联邦层面的AI监管框架，
可能参考欧盟法案但更注重创新平衡。两党在关键条款上
存在分歧，预计秋季推出草案。
**全文链接**: https://reuters.com/...
```

## 快速开始

### 步骤一：初始化 PRO 环境

```bash
# 创建 PRO 版本工作目录
mkdir -p ~/news-feed-pro/{config,schedules,reports,exports,history,custom_feeds}

# 初始化配置文件
cat > ~/news-feed-pro/config.yaml << 'EOF'
edition: pro
version: "1.0.0"

feeds:
  international:
    - bbc
    - reuters
    - ap
    - guardian
    - aljazeera
    - npr
    - dw
    - techcrunch
    - theverge
    - wired
    - arstechnica
    - hackernews
  domestic:
    - xinhua
    - cctv
    - thepaper
    - 36kr
    - ithome
    - jiqizhixin
    - baijia
    - cls
    - stcn
    - yicai
  multilingual:
    - nikkei
    - yonhap
    - dw_de

custom_feeds:
  enabled: true
  config_path: "~/news-feed-pro/custom_feeds/feeds.yaml"

fetching:
  default_limit: 10
  max_limit: 50
  timeout_seconds: 30
  full_text: false
  concurrent_fetches: 10

processing:
  deduplicate: true
  similarity_threshold: 0.85
  cluster_topics: false
  auto_summarize: false
  summary_max_words: 200

scheduling:
  enabled: true
  timezone: "Asia/Shanghai"
  config_path: "~/news-feed-pro/schedules/"

export:
  formats: ["markdown", "pdf", "email", "webhook"]
  path: "~/news-feed-pro/exports/"

history:
  enabled: true
  retention_days: 90
  searchable: true

api:
  enabled: true
  rate_limit: "200/hour"

languages: ["zh-CN", "en-US", "ja-JP", "ko-KR", "de-DE"]
EOF
```

### 步骤二：添加自定义 RSS 源

```yaml
# custom_feeds/feeds.yaml - 自定义RSS源
custom_feeds:
  - name: "企业博客"
    url: "https://blog.company.com/rss.xml"
    category: "corporate"
    language: "zh-CN"
    tier: "A"

  - name: "行业研究报告"
    url: "https://research.industry.local/feed.xml"
    category: "research"
    language: "en-US"
    tier: "A"

  - name: "技术团队博客"
    url: "https://tech.company.com/feed"
    category: "tech"
    language: "zh-CN"
    tier: "B"
```

### 步骤三：执行首次多源聚合

```bash
# 执行多源聚合（国内+国际）
python3 ~/news-feed-pro/scripts/aggregate.py \
    --sources all \
    --deduplicate \
    --limit 15 \
    --output ~/news-feed-pro/reports/initial_aggregation.md
```

## 配置示例

### 全文抓取配置

```python
# full_text_fetcher.py - 全文抓取配置
class FullTextFetcher:
    def __init__(self):
        self.timeout = 30
        self.user_agent = "NewsFeedPro/1.0"
        self.respect_robots_txt = True

    def fetch_full_text(self, url):
        """抓取新闻全文"""
        try:
            # 检查robots.txt
            if not self._allowed_by_robots(url):
                return None, "Blocked by robots.txt"

            # 抓取网页
            html = self._fetch_url(url)
            if not html:
                return None, "Fetch failed"

            # 提取正文
            article = self._extract_article(html)
            return article, "Success"
        except Exception as e:
            return None, str(e)

    def generate_summary(self, article, max_words=200):
        """生成智能摘要"""
        # 使用LLM生成摘要
        prompt = f"请用{max_words}字以内总结以下新闻的核心内容：\n{article}"
        summary = llm_summarize(prompt)
        return summary
```

### 主题聚类配置

```python
# clustering.py - 主题聚类配置
class TopicClusterer:
    def __init__(self):
        self.vectorizer = TextVectorizer()
        self.clusterer = KMeansClusterer()

    def cluster_articles(self, articles, n_clusters=None):
        """对新闻文章进行主题聚类"""
        # 1. 文本向量化
        vectors = [self.vectorizer.encode(a['title'] + a['summary'])
                   for a in articles]

        # 2. 自动确定聚类数
        if n_clusters is None:
            n_clusters = min(len(articles) // 3, 10)

        # 3. 聚类
        labels = self.clusterer.fit_predict(vectors, n_clusters)

        # 4. 组织输出
        clusters = {}
        for article, label in zip(articles, labels):
            cluster_name = f"主题{label + 1}"
            if cluster_name not in clusters:
                clusters[cluster_name] = []
            clusters[cluster_name].append(article)

        return clusters
```

### REST API 集成

```python
# api_client.py - PRO 版本 API 客户端
import requests

class NewsFeedProClient:
    def __init__(self, api_key, base_url="https://api.news-feed-pro.local"):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.base_url = base_url

    def fetch_news(self, sources=None, topic=None, limit=10):
        """获取新闻"""
        params = {"limit": limit}
        if sources:
            params["sources"] = ",".join(sources)
        if topic:
            params["topic"] = topic
        resp = requests.get(
            f"{self.base_url}/v1/news",
            headers=self.headers,
            params=params
        )
        return resp.json()

    def fetch_full_text(self, url):
        """获取新闻全文"""
        resp = requests.post(
            f"{self.base_url}/v1/fulltext",
            headers=self.headers,
            json={"url": url}
        )
        return resp.json()

    def create_schedule(self, config):
        """创建定时获取任务"""
        resp = requests.post(
            f"{self.base_url}/v1/schedules",
            headers=self.headers,
            json=config
        )
        return resp.json()

    def add_custom_feed(self, name, url, category):
        """添加自定义RSS源"""
        resp = requests.post(
            f"{self.base_url}/v1/feeds",
            headers=self.headers,
            json={"name": name, "url": url, "category": category}
        )
        return resp.json()
```

## 最佳实践

### 1. 按场景配置 RSS 源组合

```python
# 推荐的RSS源组合
SOURCE_PRESETS = {
    "国际要闻": ["bbc", "reuters", "ap", "aljazeera"],
    "科技动态": ["techcrunch", "theverge", "36kr", "jiqizhixin"],
    "财经资讯": ["bloomberg", "cls", "stcn", "reuters"],
    "国内要闻": ["xinhua", "cctv", "thepaper"],
    "全方位监控": "all"
}
```

### 2. 利用定时获取减少手动操作

```bash
# 配置工作日早间自动获取
cat > ~/news-feed-pro/schedules/daily.yaml << 'EOF'
schedules:
  - name: "每日早报"
    cron: "0 7 * * 1-5"
    sources: [xinhua, cctv, bbc, reuters]
    max_items: 10
    deduplicate: true
    output:
      format: markdown
      path: "~/news-feed-pro/reports/daily_{date}.md"
EOF
```

### 3. 利用全文抓取获取深度信息

```text
用户：获取今天BBC和Reuters所有AI相关新闻的全文摘要

Agent：
1. 从BBC和Reuters RSS获取AI相关新闻
2. 逐条抓取全文
3. 生成200字以内的智能摘要
4. 按重要度排序输出
```

### 4. 利用主题聚类发现热点

```text
用户：对今天所有新闻进行主题聚类，发现热点话题

Agent：
1. 获取所有源的今日新闻
2. 文本向量化
3. 自动聚类
4. 按聚类输出热点主题
```

## 常见问题

### Q1：PRO 版本如何获取国内 RSS 源？

PRO 版本内置了新华社、央视新闻、澎湃新闻等国内主流媒体的 RSS 源配置，直接在配置中启用即可。

### Q2：全文抓取会遵守 robots.txt 吗？

是的，PRO 版本的全文抓取功能默认遵守目标网站的 robots.txt 规则。可通过配置关闭此行为，但不建议。

### Q3：定时获取最小间隔是多少？

定时获取最小间隔为 15 分钟，突发新闻触发推送为实时（延迟 < 1 分钟）。

### Q4：自定义 RSS 源如何管理？

通过配置文件或 API 添加自定义 RSS 源，支持设置名称、分类、语言和质量等级。可在管理界面查看所有源的状态和最近获取情况。

### Q5：免费版的脚本是否兼容 PRO 版本？

PRO 版本完全兼容免费版的 `news.py` 脚本，同时提供增强版的 `aggregate.py` 脚本支持更多功能。

### Q6：API 调用频率限制？

默认每小时 200 次调用，可通过配置调整。定时获取和突发推送不受频率限制。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.10 及以上（推荐 3.12）
- **网络连接**: 稳定的互联网连接，访问国际源需配置代理
- **存储空间**: 至少 500MB 用于历史新闻与报告存储

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Python 3.10+ | 运行时 | 必需 | 系统包管理器安装 |
| Python 标准库 | 内置 | 必需 | Python 自带 |
| requests | Python 包 | 可选 | `pip install requests` |
| beautifulsoup4 | Python 包 | 可选 | `pip install beautifulsoup4`（全文抓取） |
| PyYAML | Python 包 | 可选 | `pip install pyyaml` |
| scikit-learn | Python 包 | 可选 | `pip install scikit-learn`（主题聚类） |
| pandoc | 工具 | 可选 | 系统包管理器安装（PDF导出） |
| 网络代理 | 服务 | 可选 | 用于访问国际RSS源 |

### API Key 配置

PRO 版本支持 API 集成，需配置相关密钥：

```bash
# 配置 API 认证
export NEWS_FEED_PRO_API_KEY="your_api_key"

# 代理配置（访问国际RSS源）
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

# LLM API（用于智能摘要）
export LLM_API_KEY="your_llm_key"

# 或写入配置文件
cat > ~/news-feed-pro/.env << 'EOF'
NEWS_FEED_PRO_API_KEY=your_api_key
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
LLM_API_KEY=your_llm_key
EOF
```

### 可用性分类

- **分类**: MD+EXEC+API（Markdown 指令 + Python 脚本执行 + API 集成）
- **说明**: PRO 版本支持多源聚合、定时获取、全文抓取、主题聚类与 REST API 集成
- **适用规模**: 企业新闻监控、媒体采编团队、行业研究机构
- **兼容性**: 与 news-feed-tool-free 完全兼容，支持配置迁移与平滑升级
- **特殊优势**: 免费版脚本完全兼容，PRO增强脚本提供高级功能
- **支持级别**: 优先技术支持，提供自定义 RSS 源接入与全文抓取规则定制服务
