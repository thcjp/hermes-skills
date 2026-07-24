# 详细参考 - timeline-digest-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import json

class SmartDigestGenerator:
    """智能分类摘要生成器"""

    CATEGORIES = {
        "ai_tech": {"name": "AI与技术", "icon": "🤖",
                     "keywords": ["AI", "LLM", "GPT", "模型", "机器学习", "AI芯片"]},
        "crypto": {"name": "加密货币与市场", "icon": "💰",
                    "keywords": ["BTC", "ETH", "加密", "区块链", "DeFi", "NFT"]},
        "insights": {"name": "商业洞察", "icon": "💡",
                      "keywords": ["融资", "IPO", "营收", "市场", "战略", "趋势"]},
        "other": {"name": "其他要闻", "icon": "🗞️", "keywords": []}
    }

    def __init__(self, llm_client=None):
        self.llm = llm_client

    def classify_tweet(self, tweet: dict) -> str:
        """推文分类"""
        text = tweet.get("text", "").lower()
        scores = {}

        for cat_id, cat_info in self.CATEGORIES.items():
            score = sum(1 for kw in cat_info["keywords"] if kw.lower() in text)
            scores[cat_id] = score

        best_category = max(scores, key=scores.get)
        if scores[best_category] == 0:
            return "other"
        return best_category

    def generate_smart_digest(self, tweets: list) -> dict:
        """生成智能分类摘要"""
        categorized = {cat: [] for cat in self.CATEGORIES}
        for tweet in tweets:
            category = self.classify_tweet(tweet)
            categorized[category].append(tweet)

        digest_sections = []
        for cat_id, cat_tweets in categorized.items():
            if not cat_tweets:
                continue
            cat_info = self.CATEGORIES[cat_id]
            section = {
                "category": cat_id,
                "category_name": cat_info["name"],
                "icon": cat_info["icon"],
                "count": len(cat_tweets),
                "items": [
                    {
                        "author": t.get("author", ""),
                        "summary": self._summarize(t["text"]),
                        "url": t.get("url", ""),
                        "createdAt": t.get("createdAt", "")
                    }
                    for t in cat_tweets[:10]  # 每类最多10条
                ]
            }
            digest_sections.append(section)

        return {
            "digestType": "smart",
            "generatedAt": "2026-07-18T12:00:00+08:00",
            "totalCount": len(tweets),
            "sections": digest_sections,
            "digestText": self._format_digest_text(digest_sections)
        }

    def _summarize(self, text: str, max_length: int = 100) -> str:
        """摘要单条推文"""
        if len(text) <= max_length:
            return text
        return text[:max_length] + "..."

    def _format_digest_text(self, sections: list) -> str:
        """格式化摘要文本"""
        lines = ["📋 X/Twitter 时间线智能摘要\n"]
        for section in sections:
            lines.append(f"\n{section['icon']} {section['category_name']} ({section['count']}条)")
            for item in section["items"]:
                lines.append(f"  • {item['author']}: {item['summary']}")
        return "\n".join(lines)

generator = SmartDigestGenerator()

tweets = [
    {"id": "1", "text": "OpenAI发布GPT-5,支持多模态推理和长上下文处理",
     "author": "@technews", "url": "https://x.com/1"},
    {"id": "2", "text": "BTC突破10万美元,机构投资者持续涌入",
     "author": "@crypto", "url": "https://x.com/2"},
    {"id": "3", "text": "某初创公司完成5000万美元B轮融资",
     "author": "@vcnews", "url": "https://x.com/3"},
]

digest = generator.generate_smart_digest(tweets)
print(digest["digestText"])
```

## 代码示例 (python)

```python
import feedparser
import json
from datetime import datetime

class MultiSourceAggregator:
    """多源信息聚合器"""

    def __init__(self):
        self.sources = []

    def add_twitter_source(self, name: str, limit: int = 100):
        """添加X/Twitter源"""
        self.sources.append({
            "type": "twitter",
            "name": name,
            "limit": limit
        })

    def add_rss_source(self, name: str, url: str):
        """添加RSS源"""
        self.sources.append({
            "type": "rss",
            "name": name,
            "url": url
        })

    def add_custom_source(self, name: str, fetcher: str):
        """添加自定义源"""
        self.sources.append({
            "type": "custom",
            "name": name,
            "fetcher": fetcher
        })

    def fetch_all(self) -> list:
        """抓取所有源的内容"""
        all_items = []

        for source in self.sources:
            try:
                if source["type"] == "twitter":
                    items = self._fetch_twitter(source)
                elif source["type"] == "rss":
                    items = self._fetch_rss(source)
                elif source["type"] == "custom":
                    items = self._fetch_custom(source)
                else:
                    continue

                for item in items:
                    item["source_name"] = source["name"]
                    item["source_type"] = source["type"]

                all_items.extend(items)
                print(f"[{source['name']}] 抓取 {len(items)} 条")

            except Exception as e:
                print(f"[{source['name']}] 抓取失败: {e}")

        return all_items

    def _fetch_twitter(self, source: dict) -> list:
        """抓取X/Twitter"""
        return []  # 实际实现省略
    def _fetch_rss(self, source: dict) -> list:
        """抓取RSS"""
        feed = feedparser.parse(source["url"])
        items = []
        for entry in feed.entries:
            items.append({
                "id": entry.get("id", entry.get("link", "")),
                "text": entry.get("title", "") + " " + entry.get("summary", ""),
                "author": entry.get("author", source["name"]),
                "url": entry.get("link", ""),
                "createdAt": entry.get("published", "")
            })
        return items

    def _fetch_custom(self, source: dict) -> list:
        """抓取自定义源"""
        return []

aggregator = MultiSourceAggregator()

aggregator.add_twitter_source("X-ForYou", limit=100)
aggregator.add_twitter_source("X-Following", limit=60)

aggregator.add_rss_source("TechNews", "https://feeds.example.com/tech")
aggregator.add_rss_source("AIBlog", "https://feeds.example.com/ai")

all_items = aggregator.fetch_all()
print(f"\n共抓取 {len(all_items)} 条内容")
```

## 代码示例 (python)

```python
import schedule
import time
import subprocess
import json
from datetime import datetime

class DigestScheduler:
    """摘要定时调度器"""

    def __init__(self, config: dict):
        self.config = config
        self.interval_hours = config.get("intervalHours", 6)

    def run_digest_pipeline(self):
        """执行完整的摘要生成流程"""
        print(f"[{datetime.now()}] 开始执行摘要生成流程...")

        self._fetch_timelines()

        self._run_digest_script()

        self._generate_smart_digest()

        self._push_notifications()

        print(f"[{datetime.now()}] 摘要生成流程完成")

    def _fetch_timelines(self):
        """抓取时间线"""
        subprocess.run([
            "bird", "home", "-n", str(self.config.get("fetchLimitForYou", 100)),
            "--json"
        ], stdout=open("for_you.json", "w"))

        subprocess.run([
            "bird", "home", "--following", "-n",
            str(self.config.get("fetchLimitFollowing", 60)), "--json"
        ], stdout=open("following.json", "w"))

    def _run_digest_script(self):
        """运行去重和过滤脚本"""
        subprocess.run([
            "python3", "generate_digest.py",
            "--for-you", "for_you.json",
            "--following", "following.json",
            "--output", "digest.json"
        ])

    def _generate_smart_digest(self):
        """生成智能摘要"""
        subprocess.run([
            "python3", "smart_digest.py",
            "--input", "digest.json",
            "--output", "smart_digest.json"
        ])

    def _push_notifications(self):
        """推送通知"""
        subprocess.run([
            "python3", "push_notify.py",
            "--input", "smart_digest.json"
        ])

    def start(self):
        """启动定时调度"""
        schedule.every(self.interval_hours).hours.do(self.run_digest_pipeline)

        print(f"调度器已启动,每 {self.interval_hours} 小时执行一次")
        print("按 Ctrl+C 停止")

        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            print("\n调度器已停止")

config = {
    "intervalHours": 6,
    "fetchLimitForYou": 100,
    "fetchLimitFollowing": 60,
}

scheduler = DigestScheduler(config)
scheduler.start()
```

## 代码示例 (python)

```python
import requests
import smtplib
from email.mime.text import MIMEText
import json

class NotificationPusher:
    """推送通知器"""

    def __init__(self, config: dict):
        self.config = config

    def push_telegram(self, digest_text: str) -> bool:
        """推送到Telegram"""
        tg_config = self.config.get("telegram", {})
        if not tg_config.get("enabled"):
            return False

        url = f"https://api.telegram.org/bot{tg_config['bot_token']}/sendMessage"
        data = {
            "chat_id": tg_config["chat_id"],
            "text": digest_text,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, json=data)
        return response.status_code == 200

    def push_email(self, digest_text: str) -> bool:
        """推送到邮件"""
        email_config = self.config.get("email", {})
        if not email_config.get("enabled"):
            return False

        msg = MIMEText(digest_text, "plain", "utf-8")
        msg["Subject"] = f"X/Twitter时间线摘要 - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        msg["From"] = email_config["from"]
        msg["To"] = email_config["to"]

        try:
            with smtplib.SMTP(email_config["smtp_host"], email_config["smtp_port"]) as server:
                server.starttls()
                server.login(email_config["username"], email_config["password"])
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"邮件发送失败: {e}")
            return False

    def push_webhook(self, digest_data: dict) -> bool:
        """推送到Webhook"""
        webhook_config = self.config.get("webhook", {})
        if not webhook_config.get("enabled"):
            return False

        response = requests.post(
            webhook_config["url"],
            json=digest_data,
            headers={"Content-Type": "application/json"}
        )
        return response.status_code == 200

    def push_all(self, digest_text: str, digest_data: dict):
        """推送到所有已配置的渠道"""
        results = {}
        results["telegram"] = self.push_telegram(digest_text)
        results["email"] = self.push_email(digest_text)
        results["webhook"] = self.push_webhook(digest_data)

        for channel, success in results.items():
            status = "成功" if success else "失败/未配置"
            print(f"  [{channel}] {status}")

        return results
```

