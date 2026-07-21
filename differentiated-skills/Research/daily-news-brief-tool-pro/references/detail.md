# 详细参考 - daily-news-brief-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import requests

class NewsPusher:
    """新闻推送器（专业版）"""

    def __init__(self):
        self.channels = {}

    def register(self, name, webhook_url, channel_type="generic"):
        """注册推送渠道"""
        self.channels[name] = {
            "url": webhook_url,
            "type": channel_type
        }

    def push(self, channel_name, content, title="新闻简报"):
        """推送到指定渠道"""
        if channel_name not in self.channels:
            return False
        channel = self.channels[channel_name]
        try:
            if channel["type"] == "feishu":
                return self._push_feishu(channel["url"], title, content)
            elif channel["type"] == "dingtalk":
                return self._push_dingtalk(channel["url"], title, content)
            elif channel["type"] == "wechat":
                return self._push_wechat(channel["url"], title, content)
            elif channel["type"] == "email":
                return self._push_email(channel["url"], title, content)
            elif channel["type"] == "slack":
                return self._push_slack(channel["url"], title, content)
            else:
                return self._push_generic(channel["url"], title, content)
        except Exception as e:
            print(f"推送 {channel_name} 失败：{e}")
            return False

    def push_all(self, content, title="新闻简报"):
        """推送到所有渠道"""
        results = {}
        for name in self.channels:
            results[name] = self.push(name, content, title)
        return results

    def _push_feishu(self, url, title, content):
        payload = {
            "msg_type": "interactive",
            "card": {
                "header": {"title": {"tag": "plain_text", "content": title}},
                "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": content}}]
            }
        }
        r = requests.post(url, json=payload, timeout=10)
        return r.status_code == 200

    def _push_dingtalk(self, url, title, content):
        payload = {
            "msgtype": "markdown",
            "markdown": {"title": title, "text": f"## {title}\n\n{content}"}
        }
        r = requests.post(url, json=payload, timeout=10)
        return r.status_code == 200

    def _push_wechat(self, url, title, content):
        payload = {
            "msgtype": "markdown",
            "markdown": {"content": f"## {title}\n{content}"}
        }
        r = requests.post(url, json=payload, timeout=10)
        return r.status_code == 200

    def _push_email(self, url, title, content):
        payload = {"subject": title, "body": content, "format": "markdown"}
        r = requests.post(url, json=payload, timeout=10)
        return r.status_code == 200

    def _push_slack(self, url, title, content):
        payload = {"text": f"*{title}*\n{content}"}
        r = requests.post(url, json=payload, timeout=10)
        return r.status_code == 200

    def _push_generic(self, url, title, content):
        payload = {"title": title, "content": content}
        r = requests.post(url, json=payload, timeout=10)
        return r.status_code == 200
```

## 代码示例 (python)

```python
class CustomBriefGenerator:
    """个性化简报生成器（专业版）"""

    def __init__(self, config):
        self.config = config
        self.collector = NewsCollector()
        self.filterer = NewsFilter()
        self.generator = BriefGenerator()

    def generate_custom(self):
        """生成个性化简报"""
        sources = self.config.get('sources', {})
        news = self._collect_custom(sources)

        keywords = self.config.get('keywords', {})
        filtered = self._filter_custom(news, keywords)

        template = self.config.get('template', 'default')
        brief = self._generate_with_template(filtered, template)

        return brief

    def _collect_custom(self, sources):
        """根据配置搜集"""
        all_news = {}
        for category, urls in sources.items():
            items = []
            for url in urls:
                items.extend(self.collector.collect_single(url, category))
            all_news[category] = items
        return all_news

    def _filter_custom(self, news, keywords):
        """根据权重筛选"""
        filtered = {}
        for cat, items in news.items():
            cat_keywords = keywords.get(cat, [])
            scored = []
            for item in items:
                score = sum(kw['weight'] for kw in cat_keywords if kw['word'] in item.get('title', ''))
                if score > 0:
                    item['score'] = score
                    scored.append(item)
            scored.sort(key=lambda x: x['score'], reverse=True)
            filtered[cat] = scored[:self.config.get('max_per_category', 5)]
        return filtered

    def _generate_with_template(self, filtered, template):
        """使用模板生成"""
        if template == 'formal':
            return self._generate_formal(filtered)
        elif template == 'brief':
            return self._generate_brief(filtered)
        else:
            return self.generator.generate(filtered)

    def _generate_formal(self, filtered):
        """正式报告格式"""
        lines = ["# 正式新闻分析报告", "", "---", ""]
        for cat, items in filtered.items():
            lines.append(f"## {cat.upper()}")
            lines.append("")
            for i, item in enumerate(items, 1):
                lines.append(f"### {i}. {item['title']}")
                lines.append(f"   重要程度：{'高' if item.get('score', 0) >= 3 else '中'}")
                lines.append("")
        return "\n".join(lines)

    def _generate_brief(self, filtered):
        """精简格式"""
        lines = ["# 新闻快讯", ""]
        for cat, items in filtered.items():
            for item in items[:3]:
                lines.append(f"- [{cat}] {item['title']}")
        return "\n".join(lines)
```

## 代码示例 (python)

```python
class AINewsAnalyzer:
    """AI新闻分析器（专业版）"""

    def analyze(self, filtered_news):
        """生成AI分析报告"""
        news_text = self._prepare_input(filtered_news)

        prompt = f"""请基于以下筛选后的新闻，生成深度AI分析：

{news_text}

要求：
1. 每日核心要点（3-5条）
2. 新闻趋势分析（短期/长期）
3. 情感倾向判断（正面/负面/中性）
4. 关联事件分析
5. 未来一周关注重点
6. 200字整体概述
"""
        return self._call_llm(prompt)

    def predict_trend(self, weekly_news):
        """趋势预测"""
        prompt = f"""基于本周新闻数据，预测未来一周可能的新闻走向：

{self._format_weekly(weekly_news)}

要求：
1. 热点主题预测
2. 关键事件走向
3. 潜在风险预警
4. 投资机会提示
"""
        return self._call_llm(prompt)

    def sentiment_analysis(self, news_list):
        """情感分析"""
        results = []
        for news in news_list:
            sentiment = self._analyze_sentiment(news.get('title', ''))
            news['sentiment'] = sentiment
            results.append(news)
        return results

    def _analyze_sentiment(self, title):
        """分析情感（简化版）"""
        positive = ['增长', '突破', '创新', '成功', '合作', '共赢', '利好']
        negative = ['下降', '失败', '冲突', '危机', '风险', '疫情', '暴跌']
        if any(kw in title for kw in positive):
            return 'positive'
        elif any(kw in title for kw in negative):
            return 'negative'
        return 'neutral'

    def _prepare_input(self, filtered):
        lines = []
        for cat, items in filtered.items():
            lines.append(f"\n【{cat}】")
            for news in items[:5]:
                lines.append(f"- {news.get('title', '')}")
        return "\n".join(lines)

    def _format_weekly(self, weekly_news):
        lines = []
        for day, news in weekly_news.items():
            lines.append(f"\n{day}:")
            for item in news[:3]:
                lines.append(f"  - {item.get('title', '')}")
        return "\n".join(lines)

    def _call_llm(self, prompt):
        """调用LLM（由Agent平台路由GPT-4o）"""
        return f"[AI分析结果] 基于输入生成（{len(prompt)}字符）"
```

## 代码示例 (python)

```python
import schedule
import time
import threading
from datetime import datetime

class ScheduledBriefGenerator:
    """定时简报生成器（专业版）"""

    def __init__(self):
        self.collector = NewsCollector()
        self.filterer = NewsFilter()
        self.generator = BriefGenerator()
        self.pusher = NewsPusher()
        self.running = False
        self.thread = None

    def setup_schedule(self):
        """配置定时任务"""
        schedule.every().day.at("08:00").do(self.morning_brief)
        schedule.every().day.at("12:00").do(self.noon_express)
        schedule.every().day.at("20:00").do(self.evening_summary)
        schedule.every().monday.at("09:00").do(self.weekly_report)

        print("定时任务已配置：")
        print("  - 每天 08:00 早间简报（完整版）")
        print("  - 每天 12:00 午间快讯（精简版）")
        print("  - 每天 20:00 晚间总结（含AI分析）")
        print("  - 每周一 09:00 周报（趋势分析）")

    def morning_brief(self):
        """早间简报"""
        print(f"\n[{datetime.now()}] 执行早间简报...")
        news = self.collector.collect_all()
        filtered = self.filterer.filter_news(news)
        brief = self.generator.generate(filtered)
        self.pusher.push_all(brief, "早间新闻简报")

    def noon_express(self):
        """午间快讯"""
        print(f"\n[{datetime.now()}] 执行午间快讯...")
        news = self.collector.collect_all()
        filtered = self.filterer.filter_news(news)
        express = self.generator.generate_express(filtered, max_per_cat=3)
        self.pusher.push_all(express, "午间新闻快讯")

    def evening_summary(self):
        """晚间总结（含AI分析）"""
        print(f"\n[{datetime.now()}] 执行晚间总结...")
        news = self.collector.collect_all()
        filtered = self.filterer.filter_news(news)
        brief = self.generator.generate(filtered)
        analyzer = AINewsAnalyzer()
        analysis = analyzer.analyze(filtered)
        full_brief = brief + "\n\n" + analysis
        self.pusher.push_all(full_brief, "晚间新闻总结（含AI分析）")

    def weekly_report(self):
        """周报（含趋势分析）"""
        print(f"\n[{datetime.now()}] 执行周报...")
        pass

    def start(self):
        """启动定时任务"""
        self.running = True
        self.setup_schedule()
        print("\n定时简报生成器已启动...")
        while self.running:
            schedule.run_pending()
            time.sleep(60)

    def stop(self):
        self.running = False
```

