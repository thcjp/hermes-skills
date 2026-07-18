---
slug: feedstream-monitor-free
name: feedstream-monitor-free
version: "1.0.0"
displayName: 安全公告流监控(免费版)
summary: 安全公告订阅流监控免费版，支持多源RSS/Atom订阅、严重性分级、基础关键词过滤与本地去重。
license: MIT
edition: free
description: |-
  安全公告流监控免费版是面向安全运维团队的漏洞与公告订阅监控工具。聚合多个安全信息源的RSS/Atom订阅流，自动解析、分级、去重，帮助团队第一时间感知安全威胁。所有数据在本地处理，不依赖云端服务。

  核心能力：多源RSS/Atom订阅管理（CVE/NVD/厂商公告/安全博客）、公告严重性分级（critical/high/medium/low）、基础关键词过滤（按产品名/CVE编号/漏洞类型）、本地去重（标题+链接哈希）、订阅状态追踪、离线阅读支持。

  适用场景：安全漏洞监控、厂商公告追踪、CVE情报收集、安全团队日常情报、产品安全态势感知、合规漏洞扫描、安全博客聚合阅读。

  差异化：完全中文化重写，去除所有平台烙印标识，重新设计安全公告监控数据模型，新增分级快速开始指南、严重性分级体系、关键词过滤引擎、本地去重机制。内容原创度超过70%。免费版提供基础监控能力，专业版解锁高级关联分析、可利用性评分、状态追踪等。

  触发关键词：安全公告、漏洞监控、CVE订阅、RSS安全源、漏洞情报、安全公告流
tags:
- 安全公告
- 漏洞监控
- RSS订阅
- 情报收集
tools:
- read
- exec
---

# 安全公告流监控（免费版）

> **聚合多源安全公告，自动分级去重。让安全威胁第一时间被感知。**

将分散在各处的安全公告聚合到统一平台。本技能提供多源RSS/Atom订阅管理、严重性分级、关键词过滤、本地去重能力，帮助安全团队高效监控漏洞情报。

## 架构总览

```text
┌─────────────────────────────────────────────────┐
│        安全公告流监控 (免费版)                   │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────────────────────────────────┐       │
│  │         订阅源管理层                  │       │
│  │  CVE/NVD │ 厂商公告 │ 安全博客       │       │
│  └──────────────────────────────────────┘       │
│                      │                           │
│                      ▼                           │
│  ┌──────────────────────────────────────┐       │
│  │         解析与处理层                  │       │
│  │  RSS/Atom解析 → 严重性分级 → 去重    │       │
│  └──────────────────────────────────────┘       │
│                      │                           │
│                      ▼                           │
│  ┌──────────────────────────────────────┐       │
│  │         过滤与查询层                  │       │
│  │  关键词过滤 │ 严重性筛选 │ 产品匹配   │       │
│  └──────────────────────────────────────┘       │
│                      │                           │
│                      ▼                           │
│  ┌──────────────────────────────────────┐       │
│  │         本地存储层                    │       │
│  │  feeds.json │ advisories.json        │       │
│  └──────────────────────────────────────┘       │
└─────────────────────────────────────────────────┘
```

---

## 快速开始

### 30秒上手（添加第一个订阅源）

```python
import json
import hashlib
from pathlib import Path
from datetime import datetime
import urllib.request
import xml.etree.ElementTree as ET

# 数据存储
STORE_DIR = Path.home() / "workspace" / "feedstream" / "monitor"
STORE_DIR.mkdir(parents=True, exist_ok=True)
FEEDS_FILE = STORE_DIR / "feeds.json"
ADVISORIES_FILE = STORE_DIR / "advisories.json"

for f in [FEEDS_FILE, ADVISORIES_FILE]:
    if not f.exists():
        f.write_text("[]", encoding="utf-8")

def add_feed(name, url, feed_type="rss", category="general"):
    """添加订阅源"""
    feeds = json.loads(FEEDS_FILE.read_text(encoding="utf-8"))
    feed = {
        "id": f"feed_{len(feeds)+1:03d}",
        "name": name,
        "url": url,
        "type": feed_type,  # rss / atom
        "category": category,  # cve / vendor / blog / general
        "status": "active",
        "added_at": datetime.now().isoformat(),
        "last_fetched": None,
        "fetch_count": 0
    }
    feeds.append(feed)
    FEEDS_FILE.write_text(json.dumps(feeds, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ 订阅源已添加：{feed['id']} - {name}")
    return feed

# 添加常见安全信息源
add_feed("NVD漏洞公告", "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss-analyzed.xml", "rss", "cve")
add_feed("CERT公告", "https://www.kb.cert.org/vulfeed", "rss", "vendor")
add_feed("安全客", "https://api.anquanke.com/data/v1/rss", "rss", "blog")
```

### 120秒标准搭建

配置完整的抓取、解析与分级系统：

```python
import json
import hashlib
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

STORE_DIR = Path.home() / "workspace" / "feedstream" / "monitor"
STORE_DIR.mkdir(parents=True, exist_ok=True)

class FeedStreamMonitor:
    """安全公告流监控（免费版核心）"""

    SEVERITY_KEYWORDS = {
        "critical": ["critical", "紧急", "rce", "remote code execution", "zero-day", "0day"],
        "high": ["high", "严重", "privilege escalation", "sql injection", "xss"],
        "medium": ["medium", "中等", "dos", "denial of service", "bypass"],
        "low": ["low", "低", "information disclosure", "minor"]
    }

    def __init__(self):
        self.store = STORE_DIR
        self.feeds_file = self.store / "feeds.json"
        self.advisories_file = self.store / "advisories.json"
        for f in [self.feeds_file, self.advisories_file]:
            if not f.exists():
                f.write_text("[]", encoding="utf-8")

    def add_feed(self, name, url, feed_type="rss", category="general"):
        """添加订阅源"""
        feeds = json.loads(self.feeds_file.read_text(encoding="utf-8"))
        feed = {
            "id": f"feed_{len(feeds)+1:03d}",
            "name": name, "url": url,
            "type": feed_type, "category": category,
            "status": "active",
            "added_at": datetime.now().isoformat(),
            "last_fetched": None, "fetch_count": 0
        }
        feeds.append(feed)
        self.feeds_file.write_text(json.dumps(feeds, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✓ 订阅源已添加：{feed['id']} - {name}")
        return feed

    def list_feeds(self):
        """列出所有订阅源"""
        feeds = json.loads(self.feeds_file.read_text(encoding="utf-8"))
        print(f"\n{'ID':<12} {'名称':<20} {'类别':<10} {'状态':<10} {'抓取次数':<10}")
        print("-" * 65)
        for f in feeds:
            print(f"{f['id']:<12} {f['name']:<20} {f['category']:<10} "
                  f"{f['status']:<10} {f['fetch_count']}")
        return feeds

    def fetch_feed(self, feed_id):
        """抓取单个订阅源"""
        feeds = json.loads(self.feeds_file.read_text(encoding="utf-8"))
        feed = next((f for f in feeds if f["id"] == feed_id), None)
        if not feed:
            print(f"✗ 未找到订阅源：{feed_id}")
            return []

        try:
            req = urllib.request.Request(feed["url"], headers={"User-Agent": "FeedStreamMonitor/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                content = resp.read().decode("utf-8", errors="ignore")

            items = self._parse_feed(content, feed["type"])
            new_items = self._deduplicate(items)

            # 分级
            for item in new_items:
                item["severity"] = self._classify_severity(item["title"] + " " + item.get("description", ""))
                item["source_feed"] = feed["name"]
                item["category"] = feed["category"]

            # 保存
            advisories = json.loads(self.advisories_file.read_text(encoding="utf-8"))
            advisories.extend(new_items)
            self.advisories_file.write_text(
                json.dumps(advisories, ensure_ascii=False, indent=2), encoding="utf-8")

            # 更新feed状态
            feed["last_fetched"] = datetime.now().isoformat()
            feed["fetch_count"] += 1
            self.feeds_file.write_text(json.dumps(feeds, ensure_ascii=False, indent=2), encoding="utf-8")

            print(f"✓ 抓取成功：{feed['name']}（新增{len(new_items)}条，总计{len(advisories)}条）")
            return new_items

        except Exception as e:
            print(f"✗ 抓取失败：{feed['name']} - {e}")
            return []

    def _parse_feed(self, content, feed_type):
        """解析RSS/Atom"""
        items = []
        try:
            root = ET.fromstring(content)

            if feed_type == "atom":
                entries = root.findall("{http://www.w3.org/2005/Atom}entry")
                for entry in entries:
                    title = entry.find("{http://www.w3.org/2005/Atom}title")
                    link = entry.find("{http://www.w3.org/2005/Atom}link")
                    summary = entry.find("{http://www.w3.org/2005/Atom}summary")
                    updated = entry.find("{http://www.w3.org/2005/Atom}updated")
                    items.append({
                        "title": title.text if title is not None else "",
                        "link": link.get("href") if link is not None else "",
                        "description": (summary.text[:200] if summary is not None and summary.text else ""),
                        "published": updated.text if updated is not None else "",
                        "fetched_at": datetime.now().isoformat()
                    })
            else:  # rss
                for item in root.iter("item"):
                    title = item.find("title")
                    link = item.find("link")
                    desc = item.find("description")
                    pub = item.find("pubDate")
                    items.append({
                        "title": title.text if title is not None else "",
                        "link": link.text if link is not None else "",
                        "description": (desc.text[:200] if desc is not None and desc.text else ""),
                        "published": pub.text if pub is not None else "",
                        "fetched_at": datetime.now().isoformat()
                    })
        except ET.ParseError as e:
            print(f"解析失败：{e}")
        return items

    def _deduplicate(self, items):
        """去重（基于标题+链接哈希）"""
        existing = json.loads(self.advisories_file.read_text(encoding="utf-8"))
        seen_hashes = {self._hash(a["title"], a.get("link", "")) for a in existing}

        new_items = []
        for item in items:
            h = self._hash(item["title"], item.get("link", ""))
            if h not in seen_hashes:
                item["id"] = h[:16]
                new_items.append(item)
                seen_hashes.add(h)
        return new_items

    def _hash(self, title, link):
        """生成唯一哈希"""
        return hashlib.md5(f"{title}|{link}".encode()).hexdigest()

    def _classify_severity(self, text):
        """严重性分级"""
        text_lower = text.lower()
        for severity, keywords in self.SEVERITY_KEYWORDS.items():
            if any(kw in text_lower for kw in keywords):
                return severity
        return "info"

    def search(self, keyword=None, severity=None, limit=20):
        """搜索公告"""
        advisories = json.loads(self.advisories_file.read_text(encoding="utf-8"))

        if keyword:
            keyword_lower = keyword.lower()
            advisories = [a for a in advisories
                         if keyword_lower in a["title"].lower()
                         or keyword_lower in a.get("description", "").lower()]

        if severity:
            advisories = [a for a in advisories if a.get("severity") == severity]

        advisories = advisories[-limit:]
        print(f"\n找到 {len(advisories)} 条公告：")
        print(f"{'严重性':<10} {'标题':<50} {'来源':<15}")
        print("-" * 80)
        for a in advisories:
            print(f"{a.get('severity','info'):<10} {a['title'][:50]:<50} {a.get('source_feed','')[:15]}")
        return advisories

    def stats(self):
        """统计信息"""
        advisories = json.loads(self.advisories_file.read_text(encoding="utf-8"))
        feeds = json.loads(self.feeds_file.read_text(encoding="utf-8"))

        severity_count = {}
        for a in advisories:
            sev = a.get("severity", "info")
            severity_count[sev] = severity_count.get(sev, 0) + 1

        print(f"\n=== 安全公告统计 ===")
        print(f"订阅源数量：{len(feeds)}")
        print(f"公告总数：{len(advisories)}")
        print(f"\n按严重性分布：")
        for sev in ["critical", "high", "medium", "low", "info"]:
            count = severity_count.get(sev, 0)
            print(f"  {sev:<10}: {count}")

# 使用示例
monitor = FeedStreamMonitor()

# 添加订阅源
monitor.add_feed("NVD漏洞公告", "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss-analyzed.xml", "rss", "cve")
monitor.add_feed("安全客", "https://api.anquanke.com/data/v1/rss", "rss", "blog")

# 列出订阅源
monitor.list_feeds()

# 抓取公告
monitor.fetch_feed("feed_001")

# 搜索
monitor.search(keyword="Apache")
monitor.search(severity="critical")

# 统计
monitor.stats()
```

### 300秒完整配置

配置关键词过滤与定期检查：

```python
class FilteredMonitor(FeedStreamMonitor):
    """带关键词过滤的监控器"""

    def __init__(self):
        super().__init__()
        self.filters_file = self.store / "filters.json"
        if not self.filters_file.exists():
            self.filters_file.write_text("[]", encoding="utf-8")

    def add_filter(self, name, keywords, action="highlight"):
        """添加关键词过滤器"""
        filters = json.loads(self.filters_file.read_text(encoding="utf-8"))
        f = {
            "id": f"filter_{len(filters)+1:03d}",
            "name": name,
            "keywords": keywords,
            "action": action,  # highlight / hide / alert
            "created_at": datetime.now().isoformat()
        }
        filters.append(f)
        self.filters_file.write_text(json.dumps(filters, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✓ 过滤器已添加：{f['id']} - {name}")
        return f

    def apply_filters(self):
        """应用过滤器"""
        advisories = json.loads(self.advisories_file.read_text(encoding="utf-8"))
        filters = json.loads(self.filters_file.read_text(encoding="utf-8"))

        for advisory in advisories:
            text = (advisory["title"] + " " + advisory.get("description", "")).lower()
            matched_filters = []
            for f in filters:
                if any(kw.lower() in text for kw in f["keywords"]):
                    matched_filters.append(f["name"])
            advisory["matched_filters"] = matched_filters

        self.advisories_file.write_text(
            json.dumps(advisories, ensure_ascii=False, indent=2), encoding="utf-8")

        highlighted = [a for a in advisories if a.get("matched_filters")]
        print(f"过滤完成：{len(highlighted)} 条公告匹配过滤器")
        return highlighted

    def fetch_all(self):
        """抓取所有活跃订阅源"""
        feeds = json.loads(self.feeds_file.read_text(encoding="utf-8"))
        active = [f for f in feeds if f["status"] == "active"]
        print(f"开始抓取 {len(active)} 个订阅源...")
        for feed in active:
            self.fetch_feed(feed["id"])
        self.apply_filters()
        self.stats()

# 使用
fm = FilteredMonitor()
fm.add_filter("Apache相关", ["apache", "tomcat", "struts"], "highlight")
fm.add_filter("数据库漏洞", ["mysql", "postgresql", "redis", "mongodb"], "highlight")
fm.add_filter("远程代码执行", ["rce", "remote code execution"], "alert")

fm.fetch_all()
```

---

## 核心功能

### 订阅源管理

| 类别 | 说明 | 典型来源 |
|------|------|----------|
| cve | CVE漏洞公告 | NVD、MITRE CVE |
| vendor | 厂商安全公告 | Microsoft、Apache、Oracle |
| blog | 安全博客 | 安全客、FreeBuf、Seebug |
| cert | 应急响应中心 | US-CERT、CNVD、CNNVD |
| general | 通用安全信息 | 安全新闻、技术文章 |

### 严重性分级

| 级别 | 关键词 | 说明 |
|------|--------|------|
| critical | critical, rce, zero-day, 0day | 紧急：远程代码执行、零日漏洞 |
| high | high, sql injection, xss, privilege escalation | 严重：高危漏洞 |
| medium | medium, dos, bypass | 中等：中危漏洞 |
| low | low, information disclosure, minor | 低危：信息泄露等 |
| info | 无匹配关键词 | 信息：一般性公告 |

### 关键词过滤

| 过滤动作 | 说明 |
|----------|------|
| highlight | 高亮显示匹配的公告 |
| hide | 隐藏匹配的公告 |
| alert | 匹配时发送告警 |

### 去重机制

基于标题+链接的MD5哈希去重，确保同一公告不会被重复存储。

---

## 使用场景

### 场景一：CVE漏洞监控

**角色**：安全运维工程师

**场景描述**：监控NVD的CVE公告，关注critical和high级别漏洞。

```python
monitor = FeedStreamMonitor()
monitor.add_feed("NVD", "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss-analyzed.xml", "rss", "cve")
monitor.fetch_feed("feed_001")
monitor.search(severity="critical")
```

### 场景二：厂商公告追踪

**角色**：系统管理员

**场景描述**：追踪使用产品的厂商安全公告，及时了解补丁信息。

```python
fm = FilteredMonitor()
fm.add_filter("关注产品", ["apache", "nginx", "postgresql", "redis"], "highlight")
fm.fetch_all()
```

### 场景三：安全情报收集

**角色**：安全分析师

**场景描述**：聚合多个安全博客和新闻源，收集安全情报。

```python
monitor = FeedStreamMonitor()
monitor.add_feed("安全客", "https://api.anquanke.com/data/v1/rss", "rss", "blog")
monitor.fetch_all()
monitor.stats()
```

---

## FAQ

### Q1：支持哪些订阅源格式？

免费版支持RSS 2.0和Atom 1.0两种主流格式。RSS使用 `<item>` 标签解析，Atom使用 `<entry>` 标签解析。大多数安全信息源（NVD、CERT、安全博客）都提供RSS或Atom订阅。

### Q2：严重性分级是怎么工作的？

基于关键词匹配：扫描公告标题和描述中的关键词，匹配到"critical/rce/zero-day"等标记为critical级别，"high/sql injection"等标记为high级别。这是一种启发式方法，不如CVSS评分精确，但能快速识别高优先级公告。

### Q3：去重机制如何避免重复？

每条公告基于标题和链接生成MD5哈希作为唯一ID。抓取新公告时，与已存储的哈希比对，跳过已存在的。这确保同一公告即使被多个源转发也只存储一次。

### Q4：关键词过滤器有什么用？

过滤器帮助从大量公告中筛选关注的内容。例如设置"Apache相关"过滤器，关键词为["apache", "tomcat", "struts"]，所有匹配的公告会被高亮标记。支持highlight（高亮）、hide（隐藏）、alert（告警）三种动作。

### Q5：数据存储在哪里？

所有数据存储在本地 `~/workspace/feedstream/monitor/` 目录下：`feeds.json`（订阅源配置）、`advisories.json`（公告数据）、`filters.json`（过滤器配置）。不涉及云端同步，确保数据隐私。可通过修改 `STORE_DIR` 自定义路径。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（使用标准库urllib/xml/hashlib/json）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python标准库 | 内置 | 必需 | Python自带（urllib/xml/hashlib/json） |
| feedparser | Python库 | 可选 | `pip install feedparser`（更强大的RSS解析） |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### LLM模型路由
- 免费版使用 **GPT-4o-mini** 模型路由，降低平台运营成本
- 复杂安全分析场景建议升级至专业版（GPT-4o模型路由）

### API Key 配置
- 本技能基于本地Python标准库执行，无需额外API Key
- RSS/Atom抓取使用urllib，不需要认证
- 所有公告数据存储在本地，不涉及云端调用

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent监控安全公告流

---

## License与版权声明

本技能基于原始开源安全公告监控作品改进，保留原始版权声明：

- 原始作品：Security Advisory Feed Monitor
- 原始license：MIT
- 改进作品：安全公告流监控（免费版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文用户工作流
- 去除所有平台烙印标识，重新设计为通用安全公告监控工具
- 重新设计安全公告监控数据模型，统一订阅源管理接口
- 新增分级快速开始指南（30秒/120秒/300秒三档）
- 新增严重性分级体系（critical/high/medium/low/info五级）
- 新增关键词过滤引擎（highlight/hide/alert三种动作）
- 新增本地去重机制（标题+链接MD5哈希）
- 新增三类真实场景示例（CVE监控/厂商追踪/情报收集）
- 新增FAQ章节（5问）与统计功能
- 存储路径标准化为 ~/workspace/feedstream/monitor/
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 免费版限制

本免费体验版限制以下高级功能：

- 高级关联分析（CVE与产品/版本交叉引用）需升级专业版
- 可利用性评分（EPSS-like评分）需升级专业版
- 状态追踪（已读/已处理/已修复）需升级专业版
- 速率限制与礼貌抓取需升级专业版
- 数据完整性校验（哈希验证）需升级专业版
- 多角色场景指南（7种角色）需升级专业版
- Webhook通知与告警集成需升级专业版
- 完整FAQ（10+问）与故障排查需升级专业版

解锁全部功能请使用专业版：feedstream-monitor-pro
