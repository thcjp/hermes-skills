---
slug: rss-reader-ai-pro
name: rss-reader-ai-pro
version: "1.0.0"
displayName: RSS智能阅读器专业版
summary: 企业级RSS聚合平台，支持多源批量抓取、AI深度摘要、多渠道推送、定时调度与数据分析。
license: MIT
edition: pro
description: |-
  RSS智能阅读器（专业版）—— 面向团队和企业的全功能信息聚合平台。

  核心能力:
  - 无限订阅源批量抓取与分类管理
  - AI深度摘要与关键词提取
  - 多渠道同时推送（飞书/Telegram/Email/Webhook）
  - 定时调度与任务队列
  - 内容趋势分析与阅读统计
  - 团队订阅共享与权限管理

  适用场景:
  - 企业情报监控与竞品分析
  - 团队信息共享与知识管理
  - 行业趋势追踪与报告生成
  - 多语言内容聚合与翻译

  差异化: 在免费版基础上增加多渠道推送、无限订阅源、深度分析、团队协作等企业级能力，完全兼容免费版配置格式。

  触发关键词: 企业RSS, 多渠道推送, 竞品监控, 情报聚合, 内容分析, 批量抓取, rss, reader, analytics
tags:
- 沟通协作
- 企业级
- 信息聚合
- RSS
- 数据分析
tools:
- read
- exec
---

# RSS智能阅读器（专业版）

## 概述

RSS智能阅读器专业版是一款面向团队和企业的高级信息聚合平台。在免费版的核心能力之上，专业版新增无限订阅源管理、多渠道同时推送、AI深度摘要与关键词提取、定时任务调度、内容趋势分析、团队订阅共享等企业级功能。

专业版完全兼容免费版的配置文件格式，免费版用户可无缝升级，原有配置与数据库无需迁移。

## 核心能力

### 1. 无限订阅源批量管理

支持无数量限制的订阅源，提供分类管理、标签筛选、批量导入导出能力。

### 2. AI深度摘要与关键词提取

除了基础摘要外，专业版支持关键词提取、情感分析、主题分类、重要性评分等深度分析。

### 3. 多渠道同时推送

支持飞书、Telegram、Email、自定义Webhook等多个渠道同时推送，按订阅源类别分配不同渠道。

### 4. 定时调度与任务队列

支持cron表达式定时调度，内置任务队列管理，支持优先级排序与失败重试。

### 5. 内容趋势分析

提供阅读统计、热点趋势、关键词云、来源分布等可视化分析报表。

### 6. 团队订阅共享

支持团队内订阅源共享、推送规则配置、成员权限管理。

## 使用场景

### 场景一：企业竞品情报监控

监控竞品博客、新闻稿、产品更新等RSS源，AI生成摘要并分类推送到不同团队频道。

```python
# competitor_monitor.py
import yaml
import schedule
import time

class CompetitorMonitor:
    """竞品情报监控器"""

    def __init__(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        self.feeds = self.config['feeds']
        self.routes = self.config['routes']

    def fetch_and_summarize(self):
        """抓取并生成摘要"""
        for feed in self.feeds:
            articles = self.fetch_feed(feed['url'])
            for article in articles:
                summary = self.ai_summarize(article, depth="deep")
                keywords = self.extract_keywords(article)
                sentiment = self.analyze_sentiment(article)

                # 按类别路由到不同推送渠道
                route = self.routes.get(feed['category'], 'default')
                self.push_to_channels(route, {
                    'title': article['title'],
                    'summary': summary,
                    'keywords': keywords,
                    'sentiment': sentiment,
                    'source': feed['name'],
                    'url': article['link']
                })

    def ai_summarize(self, article, depth="deep"):
        """AI深度摘要"""
        prompt = f"""
        请对以下内容进行深度分析：
        1. 生成200字以内的中文摘要
        2. 提取3-5个关键词
        3. 判断情感倾向（正面/中性/负面）
        4. 评估重要性（1-5分）
        5. 识别提及的竞品名称

        内容: {article['content']}
        """
        return self.call_llm(prompt)

# 使用示例
monitor = CompetitorMonitor("competitor_config.yaml")
monitor.fetch_and_summarize()
```

### 场景二：多渠道团队信息分发

```yaml
# 多渠道分发配置
feeds:
  - name: "行业新闻"
    url: "https://feeds.example.com/industry-news.xml"
    category: "industry"
  - name: "技术博客"
    url: "https://feeds.example.com/tech-blog.xml"
    category: "tech"
  - name: "产品更新"
    url: "https://feeds.example.com/product-updates.xml"
    category: "product"

# 按类别路由到不同渠道
routes:
  industry:
    channels: ["feishu:industry-channel", "email:leadership@company.com"]
    priority: "high"
  tech:
    channels: ["feishu:tech-channel", "telegram:tech-group"]
    priority: "medium"
  product:
    channels: ["feishu:product-channel"]
    priority: "high"
  default:
    channels: ["feishu:general-channel"]
    priority: "low"

# 多渠道推送配置
notify:
  feishu:
    enabled: true
    webhooks:
      industry-channel: "${FEISHU_INDUSTRY_WEBHOOK}"
      tech-channel: "${FEISHU_TECH_WEBHOOK}"
      product-channel: "${FEISHU_PRODUCT_WEBHOOK}"
      general-channel: "${FEISHU_GENERAL_WEBHOOK}"

  telegram:
    enabled: true
    bot_token: "${TELEGRAM_BOT_TOKEN}"
    chat_ids:
      tech-group: "${TELEGRAM_TECH_CHAT_ID}"

  email:
    enabled: true
    smtp_host: "smtp.company.com"
    smtp_port: 587
    username: "${SMTP_USER}"
    password: "${SMTP_PASSWORD}"
    recipients:
      leadership: "leadership@company.com"

  webhook:
    enabled: true
    url: "https://internal.company.com/api/rss-webhook"
    method: "POST"
    headers:
      Authorization: "Bearer ${WEBHOOK_TOKEN}"
```

### 场景三：内容趋势分析报告

```python
# analytics_report.py
class ContentAnalytics:
    """内容趋势分析报告生成器"""

    def generate_weekly_report(self):
        """生成周度分析报告"""
        report = {
            "周期": "2026-07-12 至 2026-07-18",
            "总抓取量": self.get_total_count(),
            "总推送量": self.get_pushed_count(),
            "去重过滤": self.get_dedup_count(),
            "分类统计": self.get_category_stats(),
            "热点关键词": self.get_trending_keywords(top_n=20),
            "高频来源": self.get_top_sources(top_n=10),
            "情感分布": self.get_sentiment_distribution(),
            "推送渠道统计": self.get_channel_stats()
        }
        return self.format_report(report)

    def get_trending_keywords(self, top_n=20):
        """获取热点关键词"""
        # 从数据库提取本周关键词频率
        return [
            {"keyword": "AI编程", "count": 45, "trend": "+30%"},
            {"keyword": "WebAssembly", "count": 32, "trend": "+15%"},
            {"keyword": "边缘计算", "count": 28, "trend": "+8%"},
        ]

# 生成报告
analytics = ContentAnalytics()
report = analytics.generate_weekly_report()
print(report)
```

## 快速开始

### 安装

```bash
# 安装专业版
mkdir ~/rss-reader-pro && cd ~/rss-reader-pro
pip install -r requirements.txt

# 从免费版升级（兼容迁移）
python migrate.py --from-free ~/rss-reader/my_config.yaml --to-pro ./config.yaml
```

### 基本使用

```bash
# 单次执行
python main.py --once

# 启动定时调度
python main.py --daemon

# 生成分析报告
python main.py --report weekly

# 批量导入订阅源
python main.py --import-feeds feeds.opml

# 导出订阅源
python main.py --export-feeds --format opml --output my_feeds.opml
```

### 命令行参数

```bash
python main.py [options]

--config, -c        配置文件路径 (默认: config.yaml)
--once              单次执行模式
--daemon            守护进程模式（定时调度）
--report            生成分析报告 (daily/weekly/monthly)
--import-feeds      批量导入订阅源 (OPML格式)
--export-feeds      导出订阅源
--stats             显示运行统计
--db                数据库路径 (默认: rss_reader_pro.db)
--workers           并发工作线程数 (默认: 3)
--verbose           详细日志输出
```

## 配置示例

```yaml
# config.yaml - 专业版完整配置
feeds:
  - name: "Hacker News"
    url: "https://hnrss.org/frontpage"
    category: "tech"
    priority: "high"
  - name: "阮一峰周刊"
    url: "https://www.ruanyifeng.com/blog/atom.xml"
    category: "tech"
    priority: "medium"

# AI深度分析配置
llm:
  provider: "claude"
  model: "claude-sonnet-4-20250514"
  api_key: "${ANTHROPIC_API_KEY}"
  summary_length: "medium"
  language: "zh-CN"
  deep_analysis:                # 专业版扩展
    enabled: true
    extract_keywords: true      # 关键词提取
    sentiment_analysis: true    # 情感分析
    importance_scoring: true    # 重要性评分
    topic_classification: true  # 主题分类

# 多渠道推送配置
notify:
  feishu:
    enabled: true
    webhooks:
      default: "${FEISHU_DEFAULT_WEBHOOK}"
      tech: "${FEISHU_TECH_WEBHOOK}"
  telegram:
    enabled: true
    bot_token: "${TELEGRAM_BOT_TOKEN}"
    chat_ids:
      default: "${TELEGRAM_DEFAULT_CHAT_ID}"
  email:
    enabled: true
    smtp_host: "smtp.company.com"
    smtp_port: 587
    username: "${SMTP_USER}"
    password: "${SMTP_PASSWORD}"
  webhook:
    enabled: true
    url: "${CUSTOM_WEBHOOK_URL}"

# 按类别路由
routes:
  tech:
    channels: ["feishu:tech", "telegram:default"]
  industry:
    channels: ["email", "feishu:default"]
  default:
    channels: ["feishu:default"]

# 定时调度
schedule:
  cron: "0 */2 * * *"          # 每2小时执行一次
  timezone: "Asia/Shanghai"
  priority_queue: true          # 优先级队列
  max_workers: 5                # 最大并发数
  retry:
    enabled: true
    max_attempts: 3
    backoff_seconds: 60

# 去重配置
dedup:
  enabled: true
  db_path: "rss_reader_pro.db"
  retention_days: 90

# 分析配置
analytics:
  enabled: true
  keyword_extraction: true
  sentiment_analysis: true
  trending_topics: true
  report_schedule: "weekly"     # daily/weekly/monthly

# 团队配置
team:
  shared_feeds: true            # 团队共享订阅
  permissions:
    admin: ["read", "write", "manage"]
    editor: ["read", "write"]
    viewer: ["read"]
```

## 最佳实践

### 免费版 vs 专业版能力对比

| 能力 | 免费版 | 专业版 |
|:-----|:------:|:------:|
| RSS/Atom抓取 | 是 | 是 |
| AI中文摘要 | 是 | 是 |
| SQLite去重 | 是 | 是 |
| 单渠道推送 | 是 | 是 |
| 多渠道同时推送 | 否 | 是 |
| 无限订阅源 | 否（20个） | 是 |
| 关键词提取 | 否 | 是 |
| 情感分析 | 否 | 是 |
| 重要性评分 | 否 | 是 |
| 定时调度 | 否 | 是 |
| 内容趋势分析 | 否 | 是 |
| OPML导入导出 | 否 | 是 |
| 团队共享 | 否 | 是 |
| 优先技术支持 | 否 | 是 |

### 企业级使用建议

1. **分类路由**: 按内容类别设置不同推送渠道，避免信息过载
2. **优先级管理**: 对关键订阅源设置高优先级，确保及时推送
3. **并发控制**: 根据服务器性能调整 workers 数量
4. **重试机制**: 启用失败重试，保证推送可靠性
5. **定期报告**: 每周生成分析报告，掌握信息趋势

### 性能优化

```python
# 专业版并发抓取优化
import concurrent.futures

class ParallelFetcher:
    """并发抓取器"""

    def __init__(self, max_workers=5):
        self.max_workers = max_workers

    def fetch_all(self, feeds):
        """并发抓取所有订阅源"""
        results = []
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            futures = {
                executor.submit(self.fetch_feed, feed): feed
                for feed in feeds
            }
            for future in concurrent.futures.as_completed(futures):
                feed = futures[future]
                try:
                    result = future.result(timeout=30)
                    results.append(result)
                except Exception as e:
                    print(f"抓取失败 [{feed['name']}]: {e}")
        return results
```

## 常见问题

### Q: 专业版与免费版如何兼容？

专业版完全兼容免费版的配置文件格式与数据库结构。升级时只需运行迁移脚本，原有订阅配置与去重记录自动迁移。

### Q: 专业版支持多少个订阅源？

专业版无数量限制，实际上限取决于服务器性能与网络带宽。建议单实例配置不超过500个订阅源，超过时建议分布式部署。

### Q: 多渠道推送会不会导致重复推送？

不会。专业版采用统一的去重机制，无论推送到多少渠道，每篇内容只会被处理一次，然后分发到所有配置的渠道。

### Q: 定时调度支持哪些格式？

```bash
# Cron表达式
schedule:
  cron: "0 */2 * * *"          # 每2小时
  cron: "0 9 * * 1-5"           # 工作日每天9点
  cron: "0 0 * * 0"             # 每周日0点

# 也支持自然语言（通过Agent解析）
"每天早上8点推送"
"工作日每2小时抓取一次"
```

### Q: 团队共享订阅如何管理权限？

```bash
# 设置团队成员权限
python team_manager.py add-member --user "alice" --role "editor"
python team_manager.py add-member --user "bob" --role "viewer"

# 共享订阅源到团队
python team_manager.py share-feed --feed-id 12 --team "engineering"
```

### Q: 分析报告可以导出吗？

```bash
# 导出报告为多种格式
python main.py --report weekly --format pdf --output report.pdf
python main.py --report weekly --format html --output report.html
python main.py --report weekly --format json --output report.json
```

## 依赖说明

### 运行环境

- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.8+
- **网络环境**: 需能访问订阅源URL和AI API端点
- **数据库**: 内置SQLite，无需额外安装数据库服务

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | python.org 官方下载 |
| feedparser | Python库 | 必需 | `pip install feedparser` |
| requests | Python库 | 必需 | `pip install requests` |
| anthropic / openai | Python库 | 必需 | `pip install anthropic` 或 `pip install openai` |
| sqlite3 | 标准库 | 必需 | Python内置 |
| pyyaml | Python库 | 必需 | `pip install pyyaml` |
| schedule | Python库 | 必需 | `pip install schedule` |
| apscheduler | Python库 | 推荐 | `pip install apscheduler` |
| jinja2 | Python库 | 推荐 | `pip install jinja2`（报告模板） |
| matplotlib | Python库 | 可选 | `pip install matplotlib`（图表生成） |
| LLM API | API | 必需 | 由Agent内置LLM提供或自行配置 |

### API Key 配置

```bash
# AI摘要与分析API（必选其一）
export ANTHROPIC_API_KEY="your_claude_api_key"
# 或
export OPENAI_API_KEY="your_openai_api_key"

# 多渠道推送API
export FEISHU_DEFAULT_WEBHOOK="your_feishu_webhook_1"
export FEISHU_TECH_WEBHOOK="your_feishu_webhook_2"
export TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
export TELEGRAM_DEFAULT_CHAT_ID="your_chat_id"
export SMTP_USER="your_email@company.com"
export SMTP_PASSWORD="your_smtp_password"
export CUSTOM_WEBHOOK_URL="your_custom_webhook_url"
export WEBHOOK_TOKEN="your_webhook_auth_token"
```

### 可用性分类

- **分类**: MD+EXEC+SCRIPT+DAEMON（Markdown指令 + 命令行执行 + Python脚本 + 守护进程）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行任务，专业版支持定时调度、并发处理与数据分析
- **适用人群**: 企业团队、情报分析人员、产品经理、市场团队
- **兼容性**: 完全兼容免费版配置与数据库，支持无缝升级
- **支持级别**: 优先技术支持，工作日24小时内响应
