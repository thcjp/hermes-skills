# 详细参考 - rss-aggregator-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (bash)

```bash
mkdir -p ~/rss-agg-pro/{config,templates,reports,history,archives,logs}

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

## 代码示例 (python)

```python
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

## 代码示例 (python)

```python
class SemanticDeduplicator:
    def __init__(self):
        self.vectorizer = TextVectorizer(model="text-embedding-3")
        self.threshold = 0.85

    def deduplicate(self, articles):
        """语义级去重"""
        for article in articles:
            article['vector'] = self.vectorizer.encode(
                article['title'] + ' ' + article['summary']
            )

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
        labels = self._auto_cluster(vectors, n_clusters)
        clusters = {}
        for article, label in zip(articles, labels):
            cluster_name = f"主题{label + 1}"
            clusters.setdefault(cluster_name, []).append(article)
        return clusters
```

## 代码示例 (python)

```python
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

