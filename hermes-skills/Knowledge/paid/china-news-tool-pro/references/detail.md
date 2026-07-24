# 详细参考 - china-news-tool-pro

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
        payload = {"subject": title, "body": content}
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
import schedule
import time
import threading

class ScheduledNewsAggregator:
    """定时新闻聚合器（专业版）"""

    def __init__(self):
        self.fetcher = RSSFetcher()
        self.browser_fetcher = BrowserNewsFetcher()
        self.categorizer = NewsCategorizer()
        self.summarizer = AINewsSummarizer()
        self.pusher = NewsPusher()
        self.running = False

    def setup_schedule(self):
        """配置定时任务"""
        schedule.every().day.at("08:00").do(self.morning_brief)
        schedule.every().day.at("12:00").do(self.noon_express)
        schedule.every().day.at("20:00").do(self.evening_summary)
        schedule.every().monday.at("09:00").do(self.weekly_report)

        print("定时任务已配置：")
        print("  - 每天 08:00 早间简报")
        print("  - 每天 12:00 午间快讯")
        print("  - 每天 20:00 晚间总结")
        print("  - 每周一 09:00 周报")

    def morning_brief(self):
        """早间简报"""
        print("\n=== 执行早间简报 ===")
        rss_news = self.fetcher.fetch_all()
        browser_news = self.browser_fetcher.fetch_all_browser()
        all_news = rss_news + browser_news

        categorized = self.categorizer.categorize(all_news)

        summary = self.summarizer.generate_summary(categorized)

        self.pusher.push_all(summary, "早间新闻简报")

    def noon_express(self):
        """午间快讯"""
        print("\n=== 执行午间快讯 ===")
        news = self.fetcher.fetch_all()
        categorized = self.categorizer.categorize(news)
        hot_news = "\n".join([
            f"【{cat}】{items[0]['title']}"
            for cat, items in categorized.items() if items
        ])
        self.pusher.push_all(hot_news, "午间新闻快讯")

    def evening_summary(self):
        """晚间总结"""
        print("\n=== 执行晚间总结 ===")
        news = self.fetcher.fetch_all()
        categorized = self.categorizer.categorize(news)
        summary = self.summarizer.generate_summary(categorized)
        self.pusher.push_all(summary, "晚间新闻总结")

    def weekly_report(self):
        """周报"""
        print("\n=== 执行周报 ===")
        pass

    def start(self):
        """启动定时任务"""
        self.running = True
        self.setup_schedule()
        print("\n定时新闻聚合器已启动...")
        while self.running:
            schedule.run_pending()
            time.sleep(60)

    def stop(self):
        self.running = False
```

## 代码示例 (python)

```python
class AINewsSummarizer:
    """AI新闻摘要生成器（专业版）"""

    def __init__(self):
        self.llm_available = True  # 由Agent平台内置提供
    def generate_summary(self, categorized_news):
        """生成AI新闻摘要"""
        news_text = self._prepare_input(categorized_news)

        prompt = f"""请基于以下分类新闻生成结构化AI摘要：

{news_text}

要求：
1. 每个分类生成3条核心要点
2. 标注重要程度（高/中/低）
3. 分析新闻趋势与关联
4. 生成200字以内的整体概述
5. 标注需重点关注的事件
"""
        return self._call_llm(prompt)

    def generate_topic_report(self, news_list, topic):
        """生成专题报告"""
        filtered = [n for n in news_list if topic in n.get('title', '')]
        if not filtered:
            return f"未找到与'{topic}'相关的新闻"

        prompt = f"""请基于以下关于'{topic}'的新闻生成专题报告：

{self._format_news(filtered)}

要求：
1. 事件背景与时间线
2. 各方观点汇总
3. 影响分析（短期/长期）
4. 趋势预判
"""
        return self._call_llm(prompt)

    def _prepare_input(self, categorized):
        lines = []
        for cat, news_list in categorized.items():
            lines.append(f"\n【{cat}】")
            for news in news_list[:5]:
                lines.append(f"- {news.get('title', '')}")
        return "\n".join(lines)

    def _format_news(self, news_list):
        lines = []
        for i, news in enumerate(news_list, 1):
            lines.append(f"{i}. {news.get('title', '')}")
            if news.get('desc'):
                lines.append(f"   摘要：{news['desc'][:100]}")
        return "\n".join(lines)

    def _call_llm(self, prompt):
        """调用LLM"""
        return f"[AI摘要] 基于输入生成（{len(prompt)}字符）"

summarizer = AINewsSummarizer()
summary = summarizer.generate_summary(categorized)
print(summary)
```

## 代码示例 (python)

```python
import subprocess
import json

class BrowserNewsFetcher:
    """浏览器新闻获取器（专业版）"""

    def __init__(self):
        self.sources = {
            '网易新闻': 'https://news.163.com',
            '腾讯新闻': 'https://news.qq.com',
            '人民网': 'http://www.people.com.cn',
            '新华网': 'http://www.xinhuanet.com',
            '央视网': 'http://www.cctv.com',
        }

    def fetch_with_browser(self, source_name, max_items=20):
        """使用浏览器获取新闻"""
        if source_name not in self.sources:
            return []

        url = self.sources[source_name]
        try:
            cmd = [
                "node", "browser-news.js",
                "--url", url,
                "--max-items", str(max_items),
                "--format", "json"
            ]
            result = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=30, encoding="utf-8"
            )

            if result.returncode == 0:
                news = json.loads(result.stdout)
                for item in news:
                    item['source'] = source_name
                return news
            return []
        except Exception as e:
            print(f"浏览器获取 {source_name} 失败：{e}")
            return []

    def fetch_all_browser(self):
        """使用浏览器获取所有源"""
        all_news = []
        for source in self.sources:
            print(f"  浏览器获取 {source}...")
            news = self.fetch_with_browser(source)
            all_news.extend(news)
        return all_news

browser_fetcher = BrowserNewsFetcher()
browser_news = browser_fetcher.fetch_all_browser()
print(f"浏览器获取 {len(browser_news)} 条新闻")
```

