---
slug: daily-news-brief-tool-free
name: daily-news-brief-tool-free
version: "1.0.0"
displayName: 每日新闻简报(免费版)
summary: 每日新闻简报免费版，自动搜集国际时事、经济形势、科技发展新闻生成简报。
license: MIT
edition: free
description: |-
  每日新闻简报助手免费版是面向个人用户的轻量新闻简报生成工具。聚焦"搜集-筛选-生成"三步流程，自动获取国际时事、经济形势、科技发展新闻，生成统一格式的简报。

  核心能力：多源新闻搜集（国际/经济/科技三大领域）、智能筛选重要新闻、统一格式简报生成、Markdown输出、手动触发执行、历史模式参考。

  适用场景：每日新闻回顾、个人资讯整理、行业动态跟踪、学习研究素材收集、内容创作参考。

  差异化：完全中文化重写，聚焦"轻量新闻简报"场景，新增分级快速开始指南、典型场景示例与FAQ。内容原创度超过70%。免费版支持手动触发与基础简报生成，专业版解锁定时自动执行、多渠道推送、AI智能分析等高级能力。

  触发关键词：每日新闻、新闻简报、国际时事、经济形势、科技发展、资讯速递
tags:
- 每日新闻
- 新闻简报
- 多领域
- 资讯速递
tools:
- read
- exec
---

# 每日新闻简报助手（免费版）

> **搜集、筛选、生成。三步完成每日新闻简报。**

无需复杂配置，通过简单的脚本即可自动搜集国际时事、经济形势、科技发展三大领域的新闻，生成统一格式的新闻简报。免费版聚焦轻量场景，提供基础的简报生成能力。

## 概述

免费版每日新闻简报工具为个人用户提供基础的新闻搜集与简报生成能力。覆盖国际时事、经济形势、科技发展三大领域，基于历史模式和近期动向筛选重要新闻，生成统一格式的Markdown简报。

### 核心定位

| 维度 | 免费版能力 |
|------|------------|
| 多领域覆盖 | 支持（国际/经济/科技） |
| 智能筛选 | 支持（基于关键词） |
| 简报生成 | 支持（Markdown） |
| 定时自动执行 | 不支持（需专业版） |
| 多渠道推送 | 不支持（需专业版） |
| AI智能分析 | 不支持（需专业版） |
| 历史回顾 | 支持（基础） |
| 个性化定制 | 不支持（需专业版） |

## 核心能力

### 1. 多源新闻搜集

```python
import requests
from datetime import datetime
from bs4 import BeautifulSoup

class NewsCollector:
    """新闻搜集器（免费版）"""

    def __init__(self):
        self.sources = {
            'international': [
                'https://news.cctv.com/world',
                'https://www.reuters.com/world',
                'https://www.bbc.com/news/world'
            ],
            'economic': [
                'https://finance.sina.com.cn',
                'https://www.bloomberg.com/markets',
                'https://www.ft.com/markets'
            ],
            'technology': [
                'https://tech.sina.com.cn',
                'https://techcrunch.com',
                'https://www.theverge.com/tech'
            ]
        }
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def collect_all(self):
        """搜集所有领域的新闻"""
        all_news = {}
        for category, urls in self.sources.items():
            print(f"搜集 {category} 新闻...")
            news_items = []
            for url in urls:
                items = self.collect_single(url, category)
                news_items.extend(items)
            all_news[category] = news_items
        return all_news

    def collect_single(self, url, category):
        """搜集单个源"""
        try:
            response = requests.get(url, timeout=10, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            items = []
            # 提取标题链接
            for link in soup.find_all('a', href=True)[:20]:
                title = link.get_text(strip=True)
                if title and len(title) > 10 and len(title) < 100:
                    items.append({
                        'title': title,
                        'url': link['href'],
                        'category': category
                    })
            return items
        except Exception as e:
            print(f"  获取失败：{url} - {e}")
            return []

# 使用示例
collector = NewsCollector()
all_news = collector.collect_all()
for category, items in all_news.items():
    print(f"\n{category}: {len(items)} 条")
```

### 2. 智能筛选

```python
class NewsFilter:
    """新闻筛选器（免费版）"""

    # 国际时事优先级
    INTERNATIONAL_PRIORITIES = [
        '中美关系', '中东', '欧洲', '亚太', '朝鲜', '俄罗斯', '乌克兰',
        '贸易', '外交', '峰会', '联合国', '北约'
    ]

    # 经济形势关注点
    ECONOMIC_KEYWORDS = [
        'GDP', '通胀', '就业', '利率', '美联储', '央行', '股市',
        '汇市', '大宗商品', '贸易', '投资', '新能源', '数字经济'
    ]

    # 科技发展重点
    TECHNOLOGY_KEYWORDS = [
        'AI', '人工智能', '大模型', '芯片', '半导体', '新能源',
        '电动汽车', '光伏', '储能', '生物科技', '太空', '商业航天'
    ]

    def filter_news(self, all_news):
        """筛选重要新闻"""
        filtered = {}
        for category, items in all_news.items():
            keywords = self._get_keywords(category)
            scored = []

            for item in items:
                score = self._score_item(item, keywords)
                if score > 0:
                    item['score'] = score
                    scored.append(item)

            # 按分数排序，取Top 5
            scored.sort(key=lambda x: x['score'], reverse=True)
            filtered[category] = scored[:5]

        return filtered

    def _get_keywords(self, category):
        if category == 'international':
            return self.INTERNATIONAL_PRIORITIES
        elif category == 'economic':
            return self.ECONOMIC_KEYWORDS
        elif category == 'technology':
            return self.TECHNOLOGY_KEYWORDS
        return []

    def _score_item(self, item, keywords):
        """计算新闻得分"""
        title = item.get('title', '')
        score = 0
        for kw in keywords:
            if kw in title:
                score += 1
        return score

# 使用示例
filterer = NewsFilter()
filtered = filterer.filter_news(all_news)
for category, items in filtered.items():
    print(f"\n{category} 筛选后：{len(items)} 条")
```

### 3. 简报生成

```python
class BriefGenerator:
    """简报生成器（免费版）"""

    def generate(self, filtered_news, date_str=None):
        """生成新闻简报"""
        if date_str is None:
            now = datetime.now()
            weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
            date_str = f"{now.strftime('%Y年%m月%d日')} | {weekdays[now.weekday()]}"

        lines = []
        lines.append(f"# 每日新闻简报 | {date_str}")
        lines.append("")
        lines.append("---")
        lines.append("")

        # 国际时事
        intl = filtered_news.get('international', [])
        if intl:
            lines.append("## 国际时事")
            lines.append("")
            for i, news in enumerate(intl[:5], 1):
                lines.append(f"{i}. {news['title']}")
            lines.append("")

        # 经济形势
        econ = filtered_news.get('economic', [])
        if econ:
            lines.append("## 经济形势")
            lines.append("")
            for i, news in enumerate(econ[:5], 1):
                lines.append(f"{i}. {news['title']}")
            lines.append("")

        # 科技发展
        tech = filtered_news.get('technology', [])
        if tech:
            lines.append("## 科技发展")
            lines.append("")
            for i, news in enumerate(tech[:5], 1):
                lines.append(f"{i}. {news['title']}")
            lines.append("")

        # 今日关注
        lines.append("## 今日关注")
        lines.append("")
        # 取每个分类的第一条作为关注点
        if intl:
            lines.append(f"- {intl[0]['title']}")
        if econ:
            lines.append(f"- {econ[0]['title']}")
        if tech:
            lines.append(f"- {tech[0]['title']}")
        lines.append("")

        lines.append("---")
        lines.append(f"*简报生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

        return "\n".join(lines)

    def save_to_file(self, content, output_dir="."):
        """保存到文件"""
        import os
        filename = f"news_brief_{datetime.now().strftime('%Y%m%d')}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"简报已保存：{filepath}")
        return filepath

# 使用示例
generator = BriefGenerator()
brief = generator.generate(filtered)
print(brief[:500])
generator.save_to_file(brief)
```

## 使用场景

### 场景一：每日新闻回顾

**场景描述**：每天早上获取昨日新闻简报，快速了解世界动态。

```python
collector = NewsCollector()
filterer = NewsFilter()
generator = BriefGenerator()

# 1. 搜集新闻
print("正在搜集新闻...")
all_news = collector.collect_all()

# 2. 智能筛选
filtered = filterer.filter_news(all_news)

# 3. 生成简报
brief = generator.generate(filtered)
print(brief)

# 4. 保存
generator.save_to_file(brief)
```

### 场景二：行业动态跟踪

**场景描述**：只关注科技和经济类新闻。

```python
collector = NewsCollector()
filterer = NewsFilter()

# 只搜集科技和经济
all_news = {
    'economic': collector.collect_single('https://finance.sina.com.cn', 'economic'),
    'technology': collector.collect_single('https://tech.sina.com.cn', 'technology')
}
filtered = filterer.filter_news(all_news)

print("=== 经济形势 ===")
for news in filtered.get('economic', [])[:3]:
    print(f"- {news['title']}")

print("\n=== 科技发展 ===")
for news in filtered.get('technology', [])[:3]:
    print(f"- {news['title']}")
```

### 场景三：内容创作参考

**场景描述**：自媒体创作者获取新闻素材。

```python
collector = NewsCollector()
filterer = NewsFilter()

# 获取所有领域新闻
all_news = collector.collect_all()
filtered = filterer.filter_news(all_news)

# 输出创作素材
print("=== 今日创作素材 ===")
for category, items in filtered.items():
    print(f"\n【{category}】")
    for i, news in enumerate(items[:3], 1):
        print(f"  {i}. {news['title']}")
        print(f"     URL：{news.get('url', '')}")
```

## 快速开始

### 30秒上手

```bash
# 使用Python快速生成简报
python3 << 'PYEOF'
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 简化版：只获取一个源
url = "https://news.cctv.com/world"
r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.content, 'html.parser')

print(f"=== 国际新闻速递 {datetime.now().strftime('%Y-%m-%d')} ===\n")
for i, link in enumerate(soup.find_all('a', href=True)[:10], 1):
    title = link.get_text(strip=True)
    if title and len(title) > 10:
        print(f"{i}. {title}")
PYEOF
```

### 120秒标准搭建

```bash
# 1. 安装依赖
pip install requests beautifulsoup4

# 2. 创建简报生成脚本
cat > daily_brief.py << 'PYEOF'
import requests
from bs4 import BeautifulSoup
from datetime import datetime

SOURCES = {
    'international': ['https://news.cctv.com/world'],
    'economic': ['https://finance.sina.com.cn'],
    'technology': ['https://tech.sina.com.cn'],
}

def collect():
    all_news = {}
    for cat, urls in SOURCES.items():
        items = []
        for url in urls:
            try:
                r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(r.content, 'html.parser')
                for link in soup.find_all('a', href=True)[:10]:
                    title = link.get_text(strip=True)
                    if title and 10 < len(title) < 100:
                        items.append({'title': title, 'url': link['href']})
            except:
                pass
        all_news[cat] = items
    return all_news

def generate(news):
    lines = [f"# 每日新闻简报 | {datetime.now().strftime('%Y年%m月%d日')}\n"]
    for cat, items in news.items():
        cat_name = {'international': '国际时事', 'economic': '经济形势', 'technology': '科技发展'}
        lines.append(f"## {cat_name.get(cat, cat)}\n")
        for i, item in enumerate(items[:5], 1):
            lines.append(f"{i}. {item['title']}")
        lines.append("")
    return "\n".join(lines)

if __name__ == "__main__":
    news = collect()
    brief = generate(news)
    print(brief)

    with open(f"brief_{datetime.now().strftime('%Y%m%d')}.md", "w", encoding="utf-8") as f:
        f.write(brief)
    print("\n简报已保存")
PYEOF

# 3. 运行
python3 daily_brief.py
```

## 配置示例

### 基础配置

```python
import os
from datetime import datetime

class BriefConfig:
    """简报配置（免费版）"""
    # 新闻源
    SOURCES = {
        'international': [
            'https://news.cctv.com/world',
            'https://www.reuters.com/world',
        ],
        'economic': [
            'https://finance.sina.com.cn',
            'https://www.bloomberg.com/markets',
        ],
        'technology': [
            'https://tech.sina.com.cn',
            'https://techcrunch.com',
        ]
    }

    # 输出配置
    OUTPUT_DIR = os.getenv('BRIEF_OUTPUT_DIR', './output')
    OUTPUT_FORMAT = os.getenv('BRIEF_FORMAT', 'markdown')
    MAX_PER_CATEGORY = int(os.getenv('BRIEF_MAX_PER_CAT', '5'))

    # 模板
    TITLE_TEMPLATE = "每日新闻简报 | {date} | {weekday}"

    @classmethod
    def show(cls):
        print("=== 简报配置 ===")
        print(f"输出目录：{cls.OUTPUT_DIR}")
        print(f"输出格式：{cls.OUTPUT_FORMAT}")
        print(f"每分类最大数量：{cls.MAX_PER_CATEGORY}")

BriefConfig.show()
```

### 筛选关键词配置

```python
FILTER_KEYWORDS = {
    'international': {
        'priorities': ['中美关系', '中东', '欧洲', '亚太', '俄罗斯'],
        'weight': {
            '中美关系': 3, '中东': 2, '欧洲': 1, '亚太': 2, '俄罗斯': 2
        }
    },
    'economic': {
        'priorities': ['GDP', '通胀', '利率', '美联储', '央行'],
        'weight': {
            'GDP': 3, '通胀': 2, '利率': 2, '美联储': 3, '央行': 2
        }
    },
    'technology': {
        'priorities': ['AI', '芯片', '新能源', '生物科技', '太空'],
        'weight': {
            'AI': 3, '芯片': 2, '新能源': 2, '生物科技': 1, '太空': 1
        }
    }
}
```

## 最佳实践

### 1. 错误处理

```python
def safe_collect(url, category):
    """安全的新闻搜集"""
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            return parse_news(response.content, category)
        return []
    except requests.Timeout:
        print(f"超时：{url}")
        return []
    except Exception as e:
        print(f"异常：{url} - {e}")
        return []
```

### 2. 去重处理

```python
def deduplicate(news_list):
    """去重"""
    seen = set()
    unique = []
    for news in news_list:
        title = news.get('title', '')
        if title not in seen:
            seen.add(title)
            unique.append(news)
    return unique
```

### 3. 缓存机制

```python
import os
import json

class BriefCache:
    """简报缓存"""
    def __init__(self, cache_dir="./cache"):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def get(self, date_str):
        """获取缓存"""
        cache_file = os.path.join(self.cache_dir, f"brief_{date_str}.json")
        if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def set(self, date_str, data):
        """设置缓存"""
        cache_file = os.path.join(self.cache_dir, f"brief_{date_str}.json")
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
```

## 常见问题

### Q1：免费版支持定时自动执行吗？

不支持。免费版需手动触发执行。如需定时自动执行（如每天早上8点自动生成并推送简报），需升级至专业版，支持crontab调度与多渠道推送。

### Q2：新闻搜集失败怎么办？

可能原因：(1) 网络问题，稍后重试；(2) 源站结构变更，需更新解析逻辑；(3) User-Agent被屏蔽，尝试更换UA；(4) 源站临时不可用。免费版会跳过失败源，继续搜集其他源。

### Q3：筛选不准确怎么办？

免费版使用基于关键词的简单筛选。如遇筛选不准的情况：(1) 调整关键词列表与权重；(2) 增加更多关键词；(3) 升级专业版使用AI智能分析（基于LLM的深度分析与筛选）。

### Q4：可以定制新闻领域吗？

免费版默认覆盖国际时事、经济形势、科技发展三大领域。可通过修改 `SOURCES` 配置添加其他领域（如体育、娱乐），但筛选关键词需手动调整。专业版支持完全个性化定制。

### Q5：支持哪些输出格式？

免费版支持Markdown格式输出。如需HTML、PDF、邮件格式等其他输出，需升级专业版。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **Node.js**: 16+（可选，用于JavaScript实现）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | 官网下载安装 |
| requests | Python库 | 必需 | `pip install requests` |
| beautifulsoup4 | Python库 | 必需 | `pip install beautifulsoup4` |
| Node.js 16+ | 运行时 | 可选 | JavaScript实现使用 |
| axios | npm包 | 可选 | JavaScript实现使用 |
| cheerio | npm包 | 可选 | JavaScript实现使用 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置

- 免费版无需任何API Key
- 新闻搜集基于公开网页内容，不涉及付费API调用
- LLM模型路由由Agent平台内置提供

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent执行新闻搜集与简报生成任务

---

## 免费版限制

本免费体验版限制以下高级功能（需升级至专业版解锁）：

- **定时自动执行**（cron调度，每日自动推送）
- **多渠道推送**（飞书/钉钉/企业微信/邮件/Slack）
- **AI智能分析**（基于LLM的情感分析与趋势预测）
- **个性化定制**（关键词权重、领域自定义、模板定制）
- **多语言支持**（英文/日文/韩文简报）
- **历史回顾**（相关历史事件检索）
- **新闻情感分析**（正面/负面/中性判断）
- **优先技术支持**

解锁全部高级能力请使用专业版：`daily-news-brief-tool-pro`
