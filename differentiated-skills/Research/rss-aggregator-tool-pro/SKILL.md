---
slug: rss-aggregator-tool-pro
name: rss-aggregator-tool-pro
version: "1.0.0"
displayName: RSS聚合工具专业版
summary: 企业级RSS聚合平台，支持定时调度、多渠道推送、语义去重与API集成
license: MIT
edition: pro
description: |-
  RSS聚合工具专业版，面向企业用户提供定时自动调度、多渠道推送、语义级去重与API集成能力。

  核心能力:
  - 定时自动调度（cron表达式，多时段运行）
  - 多渠道推送（邮件/微信/钉钉/Webhook/Slack）
  - 语义级去重与智能聚类
  - 自定义输出模板与品牌定制
  - 多领域自动分组与标签管理
  - 历史自动归档与全文检索
  - REST API 集成与自动化工作流
  - 内容分析与趋势追踪

  适用场景:
  - 企业内部资讯简报自动推送
  - 媒体机构多源内容采编
  - 行业研究信息聚合与分发
  - 品牌舆情实时监控

  差异化:
  - PRO 版本与免费版完全兼容，支持平滑升级
  - 新增定时调度、多渠道推送、语义去重等企业级能力
  - 支持API集成与自动化工作流
  - 提供优先技术支持与定制化服务

  触发关键词: RSS定时推送, 多渠道简报, 语义去重, 企业资讯, RSS API, rss aggregator pro
tags:
- RSS
- 聚合
- 企业级
- 定时调度
- 多渠道推送
tools:
- read
- exec
---

# RSS聚合工具（专业版）

## 概述

RSS聚合工具专业版在免费版增量推送的基础上，新增定时自动调度、多渠道推送、语义级去重与智能聚类、自定义输出模板、多领域自动分组、历史自动归档与全文检索和 REST API 集成等企业级能力，满足企业资讯分发、媒体采编和行业研究的深度需求。

PRO 版本与免费版完全兼容，用户可随时从免费版平滑升级，原有 RSS 配置和历史日志均可无缝迁移。

## 核心能力

### 能力矩阵

| 能力项 | 免费版 | PRO 版本 |
|:-------|:-------|:---------|
| 定时运行 | 手动触发 | cron自动调度 |
| 推送渠道 | 终端输出 | 邮件/微信/钉钉/Webhook/Slack |
| 去重算法 | 标题匹配 | 语义级去重+聚类 |
| 输出模板 | 固定格式 | 自定义模板+品牌定制 |
| 领域分组 | 手动配置 | 自动分组+标签 |
| 历史管理 | 手动清理 | 自动归档+全文检索 |
| API 集成 | 不支持 | REST API |
| 内容分析 | 基础过滤 | 趋势分析+热点追踪 |
| 多语言 | 中文 | 中/英/日/韩 |
| 导出格式 | 纯文本 | MD/PDF/HTML/Email |
| 监控告警 | 不支持 | 源失效检测+告警 |

### PRO 专属能力详解

```text
[PRO] 定时自动调度（cron表达式，最小15分钟间隔）
[PRO] 多渠道推送（邮件/微信/钉钉/Webhook/Slack/企业微信）
[PRO] 语义级去重（向量化匹配，准确率>95%）
[PRO] 智能聚类（同主题文章自动归类）
[PRO] 自定义输出模板（品牌Logo/颜色/排版）
[PRO] 多领域自动分组与标签管理
[PRO] 历史自动归档与全文检索
[PRO] REST API 集成与自动化工作流
[PRO] 内容趋势分析与热点追踪
[PRO] RSS源健康监控与失效告警
[PRO] 多语言支持（中/英/日/韩）
[PRO] 多格式导出（Markdown/PDF/HTML/Email）
```

## 使用场景

### 场景一：企业每日资讯自动推送

企业需要每天定时向员工推送行业资讯简报，通过邮件和企业微信分发。

```python
# enterprise_push.py - 企业推送配置
push_config = {
    "name": "每日行业资讯推送",
    "schedules": [
        {
            "name": "早间简报",
            "cron": "0 8 * * 1-5",
            "feeds": "all",
            "max_items": 15,
            "channels": ["email", "wechat_work"]
        },
        {
            "name": "午间快讯",
            "cron": "0 12 * * 1-5",
            "feeds": "tech_only",
            "max_items": 8,
            "channels": ["wechat_work"]
        },
        {
            "name": "晚间总结",
            "cron": "0 18 * * 1-5",
            "feeds": "all",
            "max_items": 20,
            "channels": ["email", "webhook"]
        }
    ],
    "recipients": {
        "email": [
            "all@company.com"
        ],
        "wechat_work": [
            "group_id_001"
        ],
        "webhook": [
            "https://hooks.company.com/news"
        ]
    }
}
```

### 场景二：多领域分组推送

企业不同部门需要接收不同领域的资讯。

```bash
# 配置多领域分组
cat > ~/rss-agg-pro/config/groups.yaml << 'EOF'
groups:
  tech:
    name: "技术资讯"
    feeds:
      - "https://feeds.example.com/ai-news.xml"
      - "https://feeds.example.com/tech-general.xml"
      - "https://feeds.example.com/devops.xml"
    schedule:
      cron: "0 8 * * 1-5"
    recipients:
      - "tech-team@company.com"
    template: "tech_template"

  finance:
    name: "财经资讯"
    feeds:
      - "https://feeds.example.com/finance.xml"
      - "https://feeds.example.com/market.xml"
    schedule:
      cron: "0 7 * * 1-5"
    recipients:
      - "finance-team@company.com"
    template: "finance_template"

  market:
    name: "市场资讯"
    feeds:
      - "https://feeds.example.com/market-research.xml"
      - "https://feeds.example.com/competitor.xml"
    schedule:
      cron: "0 9 * * 1-5"
    recipients:
      - "market-team@company.com"
    template: "market_template"
EOF
```

### 场景三：内容趋势分析

PRO 版本提供内容趋势分析，帮助发现热点话题。

```text
用户：分析本周资讯的热点趋势

Agent 执行流程：
1. 调取本周所有已推送资讯
2. 按关键词聚类分析
3. 识别热度上升趋势
4. 生成趋势分析报告
5. 推送至管理层
```

示例输出：

```markdown
## 本周资讯趋势分析 (2026-07-12 至 2026-07-18)

### 热点话题TOP5
1. AI监管政策 - 出现频次: 23次（环比+150%）
2. 新能源补贴 - 出现频次: 18次（环比+80%）
3. 半导体国产化 - 出现频次: 15次（环比+50%）
4. 量子计算 - 出现频次: 12次（环比+200%）
5. 自动驾驶 - 出现频次: 10次（环比+25%）

### 新兴话题
- 脑机接口（本周首次出现，4次报道）
- 6G通信（本周首次出现，3次报道）

### 衰退话题
- 元宇宙（环比-60%）
- NFT（环比-80%）
```

## 快速开始

### 步骤一：初始化 PRO 环境

```bash
# 创建 PRO 版本工作目录
mkdir -p ~/rss-agg-pro/{config,templates,reports,history,archives,logs}

# 初始化配置文件
cat > ~/rss-agg-pro/config.yaml << 'EOF'
edition: pro
version: "1.0.0"

feeds:
  config_path: "~/rss-agg-pro/config/feeds.yaml"
  health_check: true
  health_check_interval: "1h"

aggregation:
  deduplication: semantic
  similarity_threshold: 0.85
  clustering: true
  max_items_per_run: 30

quality_filter:
  spam_detection: true
  low_quality_filter: true
  abuse_detection: true

scheduling:
  enabled: true
  timezone: "Asia/Shanghai"
  config_path: "~/rss-agg-pro/config/schedules.yaml"
  min_interval_minutes: 15

push:
  channels:
    - email
    - wechat_work
    - webhook
    - slack
  config_path: "~/rss-agg-pro/config/channels.yaml"

templates:
  path: "~/rss-agg-pro/templates/"
  default: "pro_default"

export:
  formats: ["markdown", "pdf", "html", "email"]
  path: "~/rss-agg-pro/reports/"

history:
  auto_archive: true
  archive_after_days: 30
  retention_days: 365
  searchable: true
  path: "~/rss-agg-pro/history/"

analytics:
  enabled: true
  trend_tracking: true
  hotspot_detection: true

api:
  enabled: true
  rate_limit: "200/hour"

languages: ["zh-CN", "en-US", "ja-JP", "ko-KR"]
EOF
```

### 步骤二：配置推送渠道

```yaml
# channels.yaml - 推送渠道配置
channels:
  email:
    enabled: true
    smtp:
      host: "smtp.company.com"
      port: 587
      username: "news@company.com"
      password: "${SMTP_PASSWORD}"
      encryption: "tls"
    from: "资讯助手 <news@company.com>"
    default_subject: "今日资讯简报 - {date}"

  wechat_work:
    enabled: true
    corp_id: "${WECHAT_CORP_ID}"
    agent_id: "${WECHAT_AGENT_ID}"
    secret: "${WECHAT_SECRET}"
    default_to: ["@all"]

  webhook:
    enabled: true
    endpoints:
      - name: "内部系统"
        url: "https://hooks.internal.local/news"
        method: "POST"
        headers:
          Authorization: "Bearer ${WEBHOOK_TOKEN}"

  slack:
    enabled: true
    webhook_url: "${SLACK_WEBHOOK_URL}"
    channel: "#news"
```

### 步骤三：从免费版迁移

```bash
# 迁移免费版配置和历史
if [ -f ~/rss-aggregator/feeds.txt ]; then
    cp ~/rss-aggregator/feeds.txt ~/rss-agg-pro/config/feeds.txt.bak
    echo "RSS链接已迁移"
fi

if [ -f ~/rss-aggregator/pushed_history.log ]; then
    cp ~/rss-aggregator/pushed_history.log ~/rss-agg-pro/history/imported_history.log
    echo "历史日志已迁移"
fi
```

### 步骤四：创建定时任务

```bash
# 配置定时推送
cat > ~/rss-agg-pro/config/schedules.yaml << 'EOF'
schedules:
  - name: "每日早间简报"
    cron: "0 8 * * 1-5"
    feeds: all
    max_items: 15
    channels: [email, wechat_work]
    template: "morning_brief"

  - name: "突发新闻推送"
    trigger: event
    condition:
      keywords: ["重大", "紧急", "突破"]
      credibility: "A"
    channels: [email, wechat_work, webhook]
    immediate: true
EOF
```

## 配置示例

### 自定义输出模板

```markdown
# {{company_name}} 资讯简报

{{date}}

---

{{#each groups}}
## {{group_name}}

{{#each items}}
标题： {{title}}

摘要： {{summary}}

链接：
{{#each links}}{{this}}
{{/each}}

{{/each}}
{{/each}}

---

本简报由 {{company_name}} 资讯助手自动生成
订阅管理：{{unsubscribe_link}}
```

### 语义去重配置

```python
# semantic_dedup.py - 语义去重配置
class SemanticDeduplicator:
    def __init__(self):
        self.vectorizer = TextVectorizer(model="text-embedding-3")
        self.threshold = 0.85

    def deduplicate(self, articles):
        """语义级去重"""
        # 1. 文本向量化
        for article in articles:
            article['vector'] = self.vectorizer.encode(
                article['title'] + ' ' + article['summary']
            )

        # 2. 余弦相似度去重
        unique = []
        for article in articles:
            is_dup = False
            for existing in unique:
                similarity = self._cosine_similarity(
                    article['vector'],
                    existing['vector']
                )
                if similarity > self.threshold:
                    is_dup = True
                    # 合并信息
                    existing['links'].extend(article['links'])
                    existing['sources'].append(article['source'])
                    break
            if not is_dup:
                article['links'] = article.get('links', [article['url']])
                article['sources'] = [article['source']]
                unique.append(article)

        return unique

    def cluster(self, articles, n_clusters=None):
        """智能聚类"""
        vectors = [a['vector'] for a in articles]
        # 自动聚类
        labels = self._auto_cluster(vectors, n_clusters)
        # 组织聚类结果
        clusters = {}
        for article, label in zip(articles, labels):
            cluster_name = f"主题{label + 1}"
            clusters.setdefault(cluster_name, []).append(article)
        return clusters
```

### REST API 集成

```python
# api_client.py - PRO 版本 API 客户端
import requests

class RSSAggregatorProClient:
    def __init__(self, api_key, base_url="https://api.rss-agg-pro.local"):
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.base_url = base_url

    def trigger_aggregation(self, feeds=None, max_items=20):
        """手动触发聚合"""
        resp = requests.post(
            f"{self.base_url}/v1/aggregate",
            headers=self.headers,
            json={"feeds": feeds or "all", "max_items": max_items}
        )
        return resp.json()

    def create_schedule(self, config):
        """创建定时任务"""
        resp = requests.post(
            f"{self.base_url}/v1/schedules",
            headers=self.headers,
            json=config
        )
        return resp.json()

    def add_feed(self, name, url, group=None):
        """添加RSS源"""
        resp = requests.post(
            f"{self.base_url}/v1/feeds",
            headers=self.headers,
            json={"name": name, "url": url, "group": group}
        )
        return resp.json()

    def get_history(self, query=None, days=30):
        """搜索历史资讯"""
        params = {"days": days}
        if query:
            params["q"] = query
        resp = requests.get(
            f"{self.base_url}/v1/history",
            headers=self.headers,
            params=params
        )
        return resp.json()

    def get_trends(self, period="7d"):
        """获取趋势分析"""
        resp = requests.get(
            f"{self.base_url}/v1/trends",
            headers=self.headers,
            params={"period": period}
        )
        return resp.json()

    def check_feed_health(self):
        """检查RSS源健康状态"""
        resp = requests.get(
            f"{self.base_url}/v1/feeds/health",
            headers=self.headers
        )
        return resp.json()
```

## 最佳实践

### 1. 按部门配置推送组

```python
# 推荐的部门推送配置
DEPARTMENT_FEEDS = {
    "技术部": {
        "feeds": ["ai-news", "tech-general", "devops"],
        "schedule": "0 8 * * 1-5",
        "channels": ["email", "wechat_work"]
    },
    "市场部": {
        "feeds": ["market-research", "competitor", "industry"],
        "schedule": "0 9 * * 1-5",
        "channels": ["email"]
    },
    "高管层": {
        "feeds": "all",
        "schedule": "0 7 * * 1-5",
        "channels": ["email", "wechat_work"],
        "max_items": 10  # 高管精简版
    }
}
```

### 2. 利用语义去重提升质量

```text
用户：对本周所有资讯执行语义去重，合并重复报道

Agent：
1. 加载本周历史资讯
2. 使用向量化模型计算内容相似度
3. 合并语义相同的报道
4. 重新聚类组织
5. 生成精简版周报
```

### 3. 设置 RSS 源健康监控

```bash
# 配置源健康监控
cat > ~/rss-agg-pro/config/health_check.yaml << 'EOF'
health_check:
  interval: "1h"
  timeout: 30
  retries: 3

  alerts:
    - condition: "consecutive_failures >= 3"
      action: "disable_feed"
      notify: ["admin@company.com"]

    - condition: "response_time > 10s"
      action: "log_warning"
      notify: []

    - condition: "feed_empty_days >= 7"
      action: "flag_inactive"
      notify: ["admin@company.com"]
EOF
```

### 4. 利用趋势分析发现热点

```text
用户：生成本月资讯趋势分析报告

Agent：
1. 调取30天内所有已推送资讯
2. 按关键词聚类分析
3. 计算各话题频次与环比变化
4. 识别新兴话题与衰退话题
5. 生成趋势分析报告并推送
```

## 常见问题

### Q1：PRO 版本支持多少个 RSS 源？

PRO 版本不限制 RSS 源数量，支持通过配置文件或 API 动态添加和管理。

### Q2：定时推送最小间隔是多少？

定时推送最小间隔为 15 分钟，突发新闻触发推送为实时（延迟 < 1 分钟）。

### Q3：语义去重的准确率如何？

PRO 版本使用向量化模型进行语义匹配，去重准确率超过 95%，显著高于免费版的标题匹配。

### Q4：支持哪些推送渠道？

支持邮件（SMTP）、企业微信、钉钉、Slack、Webhook 五种推送渠道，可多渠道同时推送。

### Q5：历史资讯保留多久？

默认保留 365 天，超过 30 天的记录自动归档。归档记录支持全文检索。

### Q6：免费版如何升级至 PRO 版本？

PRO 版本初始化时会自动检测免费版配置，RSS 链接和历史日志可一键迁移。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.10 及以上（推荐 3.12）
- **网络连接**: 稳定的互联网连接
- **存储空间**: 至少 1GB 用于历史资讯与归档存储

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| 网络访问 | 服务 | 必需 | 互联网连接 |
| Python 3.10+ | 运行时 | 必需 | 系统包管理器安装 |
| requests | Python 包 | 可选 | `pip install requests` |
| PyYAML | Python 包 | 可选 | `pip install pyyaml` |
| 向量化模型 | 模型 | 可选 | API调用或本地部署（语义去重） |
| SMTP服务 | 服务 | 可选 | 邮件推送所需 |
| pandoc | 工具 | 可选 | 系统包管理器安装（PDF导出） |

### API Key 配置

PRO 版本支持 API 集成与多渠道推送，需配置相关密钥：

```bash
# 配置 API 认证
export RSS_AGG_PRO_API_KEY="your_api_key"

# 邮件服务配置
export SMTP_HOST="smtp.company.com"
export SMTP_PORT="587"
export SMTP_USER="news@company.com"
export SMTP_PASS="your_smtp_password"

# 企业微信配置
export WECHAT_CORP_ID="your_corp_id"
export WECHAT_AGENT_ID="your_agent_id"
export WECHAT_SECRET="your_secret"

# Webhook配置
export WEBHOOK_TOKEN="your_webhook_token"

# 向量化模型（语义去重）
export EMBEDDING_API_KEY="your_embedding_key"

# 或写入配置文件
cat > ~/rss-agg-pro/.env << 'EOF'
RSS_AGG_PRO_API_KEY=your_api_key
SMTP_HOST=smtp.company.com
SMTP_PORT=587
SMTP_USER=news@company.com
SMTP_PASS=your_smtp_password
WECHAT_CORP_ID=your_corp_id
WECHAT_AGENT_ID=your_agent_id
WECHAT_SECRET=your_secret
WEBHOOK_TOKEN=your_webhook_token
EMBEDDING_API_KEY=your_embedding_key
EOF
```

### 可用性分类

- **分类**: MD+EXEC+API（Markdown 指令 + 命令行执行 + API 集成）
- **说明**: PRO 版本支持定时调度、多渠道推送、语义去重、趋势分析与 REST API 集成
- **适用规模**: 企业资讯部门、媒体机构、行业研究团队
- **兼容性**: 与 rss-aggregator-tool-free 完全兼容，支持配置迁移与平滑升级
- **核心优势**: 增量推送 + 语义去重 + 多渠道分发 + 趋势分析的一站式企业资讯解决方案
- **支持级别**: 优先技术支持，提供自定义输出模板与推送渠道定制服务
