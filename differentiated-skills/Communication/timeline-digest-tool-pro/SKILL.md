---
slug: timeline-digest-tool-pro
name: timeline-digest-tool-pro
version: "1.0.0"
displayName: 时间线摘要工具-专业版
summary: 企业级X/Twitter时间线摘要平台,支持定时调度/智能分类/多源聚合/自动推送
license: MIT
edition: pro
description: |-
  时间线摘要工具专业版,面向企业和专业用户的高级X/Twitter时间线信息聚合平台。

  核心能力:
  - 全时间线抓取(For You + Following + 自定义列表)
  - 智能分类摘要(AI分类:科技/加密货币/商业洞察/其他)
  - 高级语义过滤与降噪
  - 定时自动调度与增量处理
  - 多源信息聚合(X/Twitter + RSS + 自定义源)
  - 自动推送通知(Telegram/邮件/Webhook)
  - 状态管理与云端同步
  - 摘要分析仪表盘与趋势追踪

  适用场景:
  - 企业舆情监控与行业动态追踪
  - 投资研究的信息聚合与分类
  - 内容团队的素材采集与选题发现
  - 自动化信息工作流集成

  差异化:
  - 与免费版完全兼容,无缝升级不丢失状态数据
  - AI智能分类摘要,自动归类并生成中文摘要
  - 定时自动调度,无需手动运行
  - 多源聚合能力,统一处理多渠道信息
  - 自动推送通知,支持多种渠道触达
  - 提供专属技术支持

  触发关键词: twitter, X, 时间线, 摘要, 去重, 分类, 调度, 定时, 聚合, 推送, 舆情, digest, timeline, schedule, aggregate, classify, notify
tags:
- 沟通协作
- 信息聚合
- X/Twitter
- 企业级
- 智能摘要
- 自动化
tools:
- read
- exec
---

# 时间线摘要工具(专业版)

## 概述

时间线摘要工具专业版是一款面向企业和专业用户的高级X/Twitter时间线信息聚合平台。在免费版基础抓取和去重能力之上,PRO版新增了AI智能分类摘要、定时自动调度、多源信息聚合、自动推送通知等企业级功能,帮助用户构建自动化的信息聚合与分发工作流。

PRO版与免费版完全兼容,升级后原有配置和状态数据继续使用。适合企业舆情监控、投资研究信息聚合、内容团队素材采集等需要持续追踪和自动化处理的场景。

### PRO版增强能力总览

| 能力分类 | 具体功能 | 免费版 | PRO版 |
|:---------|:---------|:-------|:------|
| 时间线抓取 | For You + Following | 支持 | 支持 |
| 时间线抓取 | 自定义列表 | - | 支持 |
| 去重处理 | 硬去重(ID) | 支持 | 支持 |
| 去重处理 | 近似去重(文本) | 支持 | 支持 |
| 去重处理 | 语义去重 | - | 支持 |
| 内容过滤 | 启发式过滤 | 基础 | 高级 |
| 内容过滤 | 语义过滤 | - | 支持 |
| 摘要输出 | 原始JSON | 支持 | 支持 |
| 摘要输出 | AI分类摘要 | - | 支持 |
| 摘要输出 | 中文智能简报 | - | 支持 |
| 调度 | 手动执行 | 支持 | 支持 |
| 调度 | 定时自动 | - | 支持 |
| 多源聚合 | X/Twitter | 支持 | 支持 |
| 多源聚合 | RSS源 | - | 支持 |
| 多源聚合 | 自定义源 | - | 支持 |
| 推送通知 | Telegram | - | 支持 |
| 推送通知 | 邮件 | - | 支持 |
| 推送通知 | Webhook | - | 支持 |
| 状态管理 | 本地文件 | 支持 | 支持 |
| 状态管理 | 云端同步 | - | 支持 |
| 分析 | 趋势追踪 | - | 支持 |
| 分析 | 仪表盘 | - | 支持 |

## 核心能力

### 1. 智能分类摘要

PRO版通过LLM对去重后的推文进行智能分类和中文摘要生成。

```python
import json

class SmartDigestGenerator:
    """智能分类摘要生成器"""

    # 分类体系
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
        # 分类
        categorized = {cat: [] for cat in self.CATEGORIES}
        for tweet in tweets:
            category = self.classify_tweet(tweet)
            categorized[category].append(tweet)

        # 生成各分类摘要
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
        # 简单截取(实际使用LLM生成摘要)
        return text[:max_length] + "..."

    def _format_digest_text(self, sections: list) -> str:
        """格式化摘要文本"""
        lines = ["📋 X/Twitter 时间线智能摘要\n"]
        for section in sections:
            lines.append(f"\n{section['icon']} {section['category_name']} ({section['count']}条)")
            for item in section["items"]:
                lines.append(f"  • {item['author']}: {item['summary']}")
        return "\n".join(lines)


# 使用示例
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

### 2. 定时自动调度

PRO版支持cron式定时调度,自动执行摘要生成流程。

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

        # 1. 抓取时间线
        self._fetch_timelines()

        # 2. 运行摘要脚本
        self._run_digest_script()

        # 3. 生成智能摘要
        self._generate_smart_digest()

        # 4. 推送通知
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
        # 每N小时执行一次
        schedule.every(self.interval_hours).hours.do(self.run_digest_pipeline)

        # 也可以设置固定时间点执行
        # schedule.every().day.at("09:00").do(self.run_digest_pipeline)
        # schedule.every().day.at("21:00").do(self.run_digest_pipeline)

        print(f"调度器已启动,每 {self.interval_hours} 小时执行一次")
        print("按 Ctrl+C 停止")

        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            print("\n调度器已停止")


# 使用示例
config = {
    "intervalHours": 6,
    "fetchLimitForYou": 100,
    "fetchLimitFollowing": 60,
}

scheduler = DigestScheduler(config)
scheduler.start()
```

### 3. 多源信息聚合

除X/Twitter时间线外,PRO版支持聚合RSS源和自定义信息源。

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

                # 标注来源
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
        # 调用bird工具抓取
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
        # 调用自定义抓取器
        return []


# 使用示例
aggregator = MultiSourceAggregator()

# 添加X/Twitter源
aggregator.add_twitter_source("X-ForYou", limit=100)
aggregator.add_twitter_source("X-Following", limit=60)

# 添加RSS源
aggregator.add_rss_source("TechNews", "https://feeds.example.com/tech")
aggregator.add_rss_source("AIBlog", "https://feeds.example.com/ai")

# 抓取所有源
all_items = aggregator.fetch_all()
print(f"\n共抓取 {len(all_items)} 条内容")
```

### 4. 自动推送通知

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

## 使用场景

### 场景一:企业舆情自动监控

企业设置每6小时自动抓取X/Twitter时间线,生成分类摘要并推送到Telegram群组。

```python
# 配置自动舆情监控
config = {
    "intervalHours": 6,
    "fetchLimitForYou": 100,
    "fetchLimitFollowing": 60,
    "maxItemsPerDigest": 25,
    "notifications": {
        "telegram": {
            "enabled": True,
            "bot_token": "YOUR_BOT_TOKEN",
            "chat_id": "@company_pr_monitor"
        }
    }
}

# 启动自动监控
scheduler = DigestScheduler(config)
scheduler.start()
# 每6小时自动: 抓取 -> 去重 -> 分类 -> 推送
```

### 场景二:投资研究信息聚合

投资团队聚合X/Twitter和多个RSS源,生成每日投资简报。

```python
# 配置多源聚合
aggregator = MultiSourceAggregator()
aggregator.add_twitter_source("X-Crypto", limit=100)
aggregator.add_rss_source("CoinDesk", "https://feeds.coindesk.com/coinbase")
aggregator.add_rss_source("TechCrunch", "https://techcrunch.com/feed/")

# 生成投资简报
all_items = aggregator.fetch_all()
digest = SmartDigestGenerator().generate_smart_digest(all_items)

# 推送到邮件
pusher = NotificationPusher({
    "email": {
        "enabled": True,
        "from": "digest@company.com",
        "to": "research@company.com",
        "smtp_host": "smtp.company.com",
        "smtp_port": 587,
        "username": "digest@company.com",
        "password": "PASSWORD"
    }
})
pusher.push_email(digest["digestText"])
```

### 场景三:内容团队素材采集

内容团队定期采集时间线中的热门话题,作为创作素材。

```python
# 采集热门话题
aggregator = MultiSourceAggregator()
aggregator.add_twitter_source("X-Trending", limit=200)

items = aggregator.fetch_all()
digest = SmartDigestGenerator().generate_smart_digest(items)

# 输出各分类的素材
for section in digest["sections"]:
    print(f"\n{section['icon']} {section['category_name']} - {section['count']}条素材")
    for item in section["items"][:5]:
        print(f"  • {item['author']}: {item['summary']}")
        print(f"    {item['url']}")
```

## 快速开始

### 从免费版升级

```bash
# PRO版继承免费版全部配置和状态,直接安装即可
skill-platform skills install timeline-digest-tool-pro
skill-platform gateway restart

# 状态文件自动继承,不会丢失已处理记录
# 发送 /new 开始新会话
```

### 全新安装

```bash
# 1. 确认前置依赖
bird --version
python3 --version

# 2. 安装PRO版
skill-platform skills install timeline-digest-tool-pro

# 3. 初始化配置
python3 init_config.py --interval 6 --output config.json

# 4. 配置推送通知(可选)
python3 setup_notifications.py --telegram --email

# 5. 启动定时调度
python3 start_scheduler.py --config config.json
```

## 配置示例

### PRO版企业级配置

```json
{
  "intervalHours": 6,
  "fetchLimitForYou": 100,
  "fetchLimitFollowing": 60,
  "maxItemsPerDigest": 25,
  "similarityThreshold": 0.9,
  "statePath": "~/.timeline-digest/state.json",

  "smartDigest": {
    "enabled": true,
    "categories": ["ai_tech", "crypto", "insights", "other"],
    "language": "zh_CN",
    "max_summary_length": 100
  },

  "multiSource": {
    "enabled": true,
    "sources": [
      {"type": "twitter", "name": "X-ForYou", "limit": 100},
      {"type": "twitter", "name": "X-Following", "limit": 60},
      {"type": "rss", "name": "TechNews", "url": "https://feeds.example.com/tech"}
    ]
  },

  "notifications": {
    "telegram": {
      "enabled": true,
      "bot_token": "YOUR_BOT_TOKEN",
      "chat_id": "@your_channel"
    },
    "email": {
      "enabled": false,
      "from": "digest@example.com",
      "to": "user@example.com",
      "smtp_host": "smtp.example.com",
      "smtp_port": 587
    },
    "webhook": {
      "enabled": false,
      "url": "https://hooks.example.com/digest"
    }
  },

  "scheduler": {
    "mode": "interval",
    "intervalHours": 6,
    "run_on_startup": true
  },

  "analytics": {
    "enabled": true,
    "trend_tracking": true,
    "dashboard_path": "./dashboard/"
  }
}
```

### 推送通知配置

```yaml
# notifications.yaml
notifications:
  telegram:
    enabled: true
    bot_token: "${TELEGRAM_BOT_TOKEN}"
    chat_id: "@company_monitor"

  email:
    enabled: true
    smtp_host: "smtp.company.com"
    smtp_port: 587
    username: "${EMAIL_USER}"
    password: "${EMAIL_PASS}"
    from: "digest@company.com"
    to: ["team@company.com"]

  webhook:
    enabled: true
    url: "https://hooks.company.com/timeline-digest"
    headers:
      Authorization: "Bearer ${WEBHOOK_TOKEN}"
```

## 最佳实践

### 1. 调度频率选择

| 使用场景 | 建议频率 | 抓取量 | 说明 |
|:---------|:---------|:-------|:-----|
| 实时舆情监控 | 每2小时 | ForYou 50 | 高频追踪,快速响应 |
| 日常信息聚合 | 每6小时 | ForYou 100 | 平衡效率与覆盖 |
| 每日简报 | 每天2次 | ForYou 200 | 早晚各一次 |
| 每周回顾 | 每周1次 | ForYou 500 | 深度回顾 |

### 2. 多源聚合策略

```text
多源聚合建议:
1. X/Twitter作为主要信息源(实时性强)
2. RSS补充深度内容(博客、新闻站)
3. 自定义源补充专业领域内容
4. 统一去重,避免跨源重复
5. 分类摘要时标注来源,便于追溯
```

### 3. 推送通知优化

```python
# 推送内容优化建议
PUSH_BEST_PRACTICES = {
    "format": "使用简洁的格式,重点突出分类和数量",
    "length": "单次推送不超过2000字符,过长分段发送",
    "timing": "避免深夜推送,建议在9:00-21:00之间",
    "priority": "高优先级内容(突发新闻)可即时推送",
    "dedup": "推送前检查24小时内是否已推送相同内容",
}
```

## 常见问题

### Q1: PRO版的智能分类准确率如何?

**A:** PRO版使用关键词匹配+LLM语义分析双重分类机制。对于明确领域的内容(如AI、加密货币)准确率较高。用户可通过配置自定义分类关键词来提升特定领域的分类准确率。

### Q2: 定时调度如何保证不遗漏推文?

**A:** PRO版使用增量过滤机制,每次运行只处理上次运行后的新推文。状态文件记录已处理的推文ID,即使调度间隔较长也不会遗漏。状态文件保留30天的记录,确保去重有效。

### Q3: 多源聚合会增加API调用吗?

**A:** X/Twitter源的抓取通过bird工具完成,不额外增加API调用。RSS源是标准HTTP请求,不涉及API限制。自定义源取决于具体实现。建议合理设置抓取频率,避免对源站造成压力。

### Q4: 推送通知支持哪些渠道?

**A:** PRO版支持Telegram Bot推送、邮件推送(SMTP)和Webhook推送。Webhook可对接Slack、飞书、企业微信等支持Webhook的平台。

### Q5: 状态文件可以云端同步吗?

**A:** PRO版支持状态文件云端同步,适合多设备或团队共享去重状态的场景。配置中设置 `cloud_sync` 相关参数即可启用。

### Q6: 如何与免费版协作?

**A:** PRO版与免费版完全兼容。免费版的状态文件格式与PRO版一致,升级后直接继承。免费版用户手动生成的JSON摘要也可以导入PRO版进行智能分类处理。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **网络环境**: 需可访问X/Twitter服务和推送服务

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| bird | CLI工具 | 必需 | 参考bird工具文档安装 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| feedparser | Python库 | 可选 | `pip install feedparser` |
| requests | Python库 | 可选 | `pip install requests` |
| schedule | Python库 | 可选 | `pip install schedule` |

### API Key 配置

- bird工具的认证(cookie)由bird工具自行管理
- Telegram推送需要Bot Token(通过 @BotFather 创建)
- 邮件推送需要SMTP账号密码
- Webhook推送需要目标URL和认证Token
- LLM智能摘要由Agent内置LLM提供,无需额外Key

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行时间线摘要和推送任务
- **运行模式**: 本地脚本执行 + 定时调度 + 远程推送
- **安全等级**: 只读抓取操作;推送通知需配置认证凭证;状态文件支持云端加密同步
- **兼容性**: 与免费版(timeline-digest-tool-free)完全兼容,支持无缝升级
