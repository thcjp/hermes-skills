---
slug: "rss-reader-ai"
name: "rss-reader-ai"
version: 1.0.1
displayName: "RSS智能阅读器专业版"
summary: "企业级RSS聚合平台，支持多源批量抓取、AI深度摘要、多渠道推送、定时调度与数据分析。。RSS智能阅读器（专业版）—— 面向团队和企业的全功能信息聚合平台。核心能力: - 无限订阅源批量抓取"
license: "MIT"
edition: "pro"
description: |-
  RSS智能阅读器（专业版）—— 面向团队和企业的全功能信息聚合平台。核心能力:
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

  差异化: 在免费版基础上增加多渠道推送、无限订阅源、深度分析、团队协作等企业级能力...
tags:
  - 沟通协作
  - 企业级
  - 信息聚合
  - RSS
  - 数据分析
  - 订阅
  - 信息
  - self
  - article
  - feeds
  - 验证返回
tools:
  - read
  - exec
homepage: ""
category: "Knowledge"
---
# RSS智能阅读器专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| RSS智能阅读器专业版支持多源批量抓取 | 不支持 | 支持 |
| RSS智能阅读器专业版定时调度与数据分析 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

### 1. 无限订阅源批量管理
支持无数量限制的订阅源，提供分类管理、标签筛选、批量导入导出能力.
**处理**: 解析无限订阅源批量管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证返回数据的完整性和格式正确性
- 参考`无限订阅源批量管理`的配置文档进行参数调优
### 2. AI深度摘要与关键词提取
除了基础摘要外，专业版支持关键词提取、情感分析、主题分类、重要性评分等深度分析.
**输入**: 用户提供AI深度摘要与关键词提取所需的指令和必要参数.
**输出**: 返回AI深度摘要与关键词提取的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`AI深度摘要与关键词提取`的配置文档进行参数调优
### 3. 多渠道同时推送
支持飞书、Telegram、Email、自定义Webhook等多个渠道同时推送，按订阅源类别分配不同渠道.
**输入**: 用户提供多渠道同时推送所需的指令和必要参数.
**处理**: 解析多渠道同时推送的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多渠道同时推送的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`多渠道同时推送`的配置文档进行参数调优
### 4. 定时调度与任务队列
支持cron表达式定时调度，内置任务队列管理，支持优先级排序与失败重试.
**输入**: 用户提供定时调度与任务队列所需的指令和必要参数.
**输出**: 返回定时调度与任务队列的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`定时调度与任务队列`的配置文档进行参数调优
### 5. 内容趋势分析
提供阅读统计、热点趋势、关键词云、来源分布等可视化分析报表.
**输出**: 返回内容趋势分析的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`内容趋势分析`的配置文档进行参数调优
### 6. 团队订阅共享
支持团队内订阅源共享、推送规则配置、成员权限管理.
**输入**: 用户提供团队订阅共享所需的指令和必要参数.
**处理**: 解析团队订阅共享的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回团队订阅共享的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`团队订阅共享`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：企业竞品情报监控
监控竞品博客、新闻稿、产品更新等RSS源，AI生成摘要并分类推送到不同团队频道.
```python
import yaml
import schedule
import time
# ...
class CompetitorMonitor:
    """竞品情报监控器"""
# ...
    def __init__(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        self.feeds = self.config['feeds']
        self.routes = self.config['routes']
# ...
    def fetch_and_summarize(self):
        """抓取并生成摘要"""
        for feed in self.feeds:
            articles = self.fetch_feed(feed['url'])
            for article in articles:
                summary = self.ai_summarize(article, depth="deep")
                keywords = self.extract_keywords(article)
                sentiment = self.analyze_sentiment(article)
# ...
                route = self.routes.get(feed['category'], 'default')
                self.push_to_channels(route, {
                    'title': article['title'],
                    'summary': summary,
                    'keywords': keywords,
                    'sentiment': sentiment,
                    'source': feed['name'],
                    'url': article['link']
                })
# ...
    def ai_summarize(self, article, depth="deep"):
        """AI深度摘要"""
        prompt = f"""
        请对以下内容进行深度分析：
        1. 生成200字以内的中文摘要
        2. 提取3-5个关键词
        3. 判断情感倾向（正面/中性/负面）
        4. 评估重要性（1-5分）
        5. 识别提及的竞品名称
# ...
        内容: {article['content']}
        """
        return self.call_llm(prompt)
# ...
monitor = CompetitorMonitor("competitor_config.yaml")
monitor.fetch_and_summarize()
```

### 场景二：多渠道团队信息分发
```yaml
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
# ...
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
# ...
notify:
  feishu:
    enabled: true
    webhooks:
      industry-channel: "${FEISHU_INDUSTRY_WEBHOOK}"
      tech-channel: "${FEISHU_TECH_WEBHOOK}"
      product-channel: "${FEISHU_PRODUCT_WEBHOOK}"
      general-channel: "${FEISHU_GENERAL_WEBHOOK}"
# ...
  telegram:
    enabled: true
    bot_token: "${TELEGRAM_BOT_TOKEN}"
    chat_ids:
      tech-group: "${TELEGRAM_TECH_CHAT_ID}"
# ...
  email:
    enabled: true
    smtp_host: "smtp.company.com"
    smtp_port: 587
    username: "${SMTP_USER}"
    password: "${SMTP_PASSWORD}"
    recipients:
      leadership: "leadership@company.com"
# ...
  webhook:
    enabled: true
    url: "https://internal.company.com/api/rss-webhook"
    method: "POST"
    headers:
      Authorization: "Bearer ${WEBHOOK_TOKEN}"
```

### 场景三：内容趋势分析报告
```python
class ContentAnalytics:
    """内容趋势分析报告生成器"""
# ...
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
# ...
    def get_trending_keywords(self, top_n=20):
        """获取热点关键词"""
        return [
            {"keyword": "AI编程", "count": 45, "trend": "+30%"},
            {"keyword": "WebAssembly", "count": 32, "trend": "+15%"},
            {"keyword": "边缘计算", "count": 28, "trend": "+8%"},
        ]
# ...
analytics = ContentAnalytics()
report = analytics.generate_weekly_report()
print(report)
```

## 使用流程

### 安装
```bash
mkdir ~/rss-reader-pro && cd ~/rss-reader-pro
pip install -r requirements.txt
# ...
python migrate.py --from-free ~/rss-reader/my_config.yaml --to-pro ./config.yaml
```

### 基本使用
```bash
python main.py --once
# ...
python main.py --daemon
# ...
python main.py --report weekly
# ...
python main.py --import-feeds feeds.opml
# ...
python main.py --export-feeds --format opml --output my_feeds.opml
```

### 命令行参数
```bash
python main.py [options]
# ...
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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | rss-reader-ai处理的内容输入 |,  |
| content | string | 否 | rss-reader-ai处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "ai 相关配置参数",
    result: "ai 相关配置参数",
    result: "ai 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.8+
- **网络环境**: 需能访问订阅源URL和AI API端点
- **数据库**: 内置SQLite，无需额外安装数据库服务

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
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
export ANTHROPIC_API_KEY="your_claude_api_key"
export OPENAI_API_KEY="your_openai_api_key"
# ...
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
- **说明**: 基于Markdown的AI Skill，专业版支持定时调度、并发处理与数据分析
- **适用人群**: 企业团队、情报分析人员、产品经理、市场团队
- **兼容性**: 完全兼容免费版配置与数据库，支持无缝升级
- **支持级别**: 优先技术支持，工作日24小时内响应

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q: 专业版与免费版如何兼容？
专业版完全兼容免费版的配置文件格式与数据库结构。升级时只需运行迁移脚本，原有订阅配置与去重记录自动迁移.
### Q: 专业版支持多少个订阅源？
专业版无数量限制，实际上限取决于服务器性能与网络带宽。建议单实例配置不超过500个订阅源，超过时建议分布式部署.
### Q: 多渠道推送会不会导致重复推送？
不会。专业版采用统一的去重机制，无论推送到多少渠道，每篇内容只会被处理一次，然后分发到所有配置的渠道.
### Q: 定时调度支持哪些格式？
```bash
schedule:
  cron: "0 */2 * * *"          # 每2小时
  cron: "0 9 * * 1-5"           # 工作日每天9点
  cron: "0 0 * * 0"             # 每周日0点
"每天早上8点推送"
"工作日每2小时抓取一次"
```

### Q: 团队共享订阅如何管理权限？
```bash
python team_manager.py add-member --user "alice" --role "editor"
python team_manager.py add-member --user "bob" --role "viewer"
# ...
python team_manager.py share-feed --feed-id 12 --team "engineering"
```

### Q: 分析报告可以导出吗？
```bash
python main.py --report weekly --format pdf --output report.pdf
python main.py --report weekly --format html --output report.html
python main.py --report weekly --format json --output report.json
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

