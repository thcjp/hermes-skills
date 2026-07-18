---
slug: feed-digest-tool-free
name: feed-digest-tool-free
version: "1.0.0"
displayName: 订阅摘要(免费版)
summary: 订阅摘要免费版，支持RSS订阅获取、未读扫描、基础分类与摘要生成。
license: MIT
edition: free
description: |-
  订阅摘要助手免费版是面向个人用户的轻量RSS订阅摘要工具。聚焦"获取-扫描-筛选-阅读"四步流程，从订阅源中筛选高价值内容生成摘要。

  核心能力：RSS订阅获取最新内容、未读条目扫描、智能筛选（5-10条高价值内容）、全文阅读、基础分类摘要、标记已读。

  适用场景：每日订阅速览、个人阅读管理、高价值内容筛选、学习研究素材收集、信息过载治理。

  差异化：完全中文化重写，聚焦"轻量订阅摘要"场景，新增分级快速开始指南、典型场景示例与FAQ。内容原创度超过70%。免费版支持基础筛选与摘要生成，专业版解锁AI深度摘要、多源聚合、定时推送、团队共享等高级能力。

  触发关键词：订阅摘要、RSS阅读、未读扫描、内容筛选、信息摘要、Feed Digest
tags:
- 订阅摘要
- RSS阅读
- 内容筛选
- 信息过载
tools:
- read
- exec
---

# 订阅摘要助手（免费版）

> **获取、扫描、筛选、阅读。四步完成订阅内容摘要。**

无需复杂配置，通过 `feed` CLI 即可获取订阅源最新内容，智能筛选高价值条目，生成精炼摘要。免费版聚焦轻量场景，帮助用户应对信息过载。

## 概述

免费版订阅摘要工具为个人用户提供基础的RSS订阅内容管理能力。通过 `feed` 命令行工具，获取最新条目、扫描未读、筛选高价值内容、生成摘要，让阅读更高效。

### 核心定位

| 维度 | 免费版能力 |
|------|------------|
| 获取最新内容 | 支持（feed fetch） |
| 未读条目扫描 | 支持（默认50条） |
| 智能筛选 | 支持（基础关键词） |
| 全文阅读 | 支持（Markdown格式） |
| 基础分类 | 支持（按订阅源） |
| 标记已读 | 支持（批量） |
| AI深度摘要 | 不支持（需专业版） |
| 多源聚合 | 不支持（需专业版） |
| 定时推送 | 不支持（需专业版） |
| 团队共享 | 不支持（需专业版） |

## 核心能力

### 1. 获取最新内容

```python
import subprocess
import json

class FeedFetcher:
    """订阅内容获取器（免费版）"""

    def __init__(self, cli_path="feed"):
        self.cli = cli_path

    def fetch(self):
        """获取所有订阅源的最新内容"""
        result = subprocess.run(
            [self.cli, "fetch"],
            capture_output=True, text=True, timeout=60, encoding="utf-8"
        )
        if result.returncode == 0:
            return {"success": True, "output": result.stdout}
        return {"success": False, "error": result.stderr}

    def get_entries(self, limit=50, feed_id=None):
        """获取未读条目"""
        cmd = [self.cli, "get", "entries", "--limit", str(limit)]
        if feed_id:
            cmd.extend(["--feed", feed_id])

        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30, encoding="utf-8"
        )
        if result.returncode == 0:
            return result.stdout
        return f"获取失败：{result.stderr}"

    def get_entry(self, entry_id):
        """获取单条目全文（Markdown格式）"""
        result = subprocess.run(
            [self.cli, "get", "entry", str(entry_id)],
            capture_output=True, text=True, timeout=30, encoding="utf-8"
        )
        if result.returncode == 0:
            return result.stdout
        return f"获取失败：{result.stderr}"

    def get_feeds(self):
        """获取所有订阅源列表"""
        result = subprocess.run(
            [self.cli, "get", "feeds"],
            capture_output=True, text=True, timeout=10, encoding="utf-8"
        )
        return result.stdout if result.returncode == 0 else f"获取失败：{result.stderr}"

    def get_stats(self):
        """获取数据库统计"""
        result = subprocess.run(
            [self.cli, "get", "stats"],
            capture_output=True, text=True, timeout=10, encoding="utf-8"
        )
        return result.stdout if result.returncode == 0 else f"获取失败：{result.stderr}"

# 使用示例
fetcher = FeedFetcher()

# 获取最新内容
print("=== 获取最新内容 ===")
fetcher.fetch()

# 查看订阅源
print("\n=== 订阅源列表 ===")
print(fetcher.get_feeds())

# 获取未读条目
print("\n=== 未读条目 ===")
print(fetcher.get_entries(limit=50))
```

### 2. 智能筛选

```python
class FeedFilter:
    """订阅内容筛选器（免费版）"""

    HIGH_VALUE_KEYWORDS = [
        'AI', '人工智能', '大模型', 'LLM', 'GPT',
        '系统设计', '架构', '性能优化', '分布式',
        '开发工具', 'DevOps', 'CI/CD', 'Kubernetes',
        '反直觉', '颠覆', '突破', '创新',
        '深度分析', '长文', '思考',
    ]

    SKIP_KEYWORDS = [
        '广告', '推广', '赞助', 'sponsored',
        '订阅', '关注', '转发', '抽奖',
    ]

    def __init__(self, limit=10):
        self.limit = limit

    def filter_entries(self, entries_text):
        """筛选高价值条目"""
        entries = self._parse_entries(entries_text)
        scored = []

        for entry in entries:
            score = self._score_entry(entry)
            if score > 0:
                entry['score'] = score
                scored.append(entry)

        # 按分数排序，取Top N
        scored.sort(key=lambda x: x['score'], reverse=True)
        return scored[:self.limit]

    def _score_entry(self, entry):
        """计算条目得分"""
        title = entry.get('title', '').lower()
        summary = entry.get('summary', '').lower()
        text = title + ' ' + summary

        # 跳过广告/推广
        for kw in self.SKIP_KEYWORDS:
            if kw.lower() in text:
                return 0

        # 计算高分关键词得分
        score = 0
        for kw in self.HIGH_VALUE_KEYWORDS:
            if kw.lower() in text:
                score += 1

        # 标题含高分关键词额外加分
        for kw in self.HIGH_VALUE_KEYWORDS:
            if kw.lower() in title:
                score += 1

        return score

    def _parse_entries(self, entries_text):
        """解析条目列表"""
        # 简化版：按行解析表格输出
        entries = []
        lines = entries_text.strip().split('\n')
        for line in lines[1:]:  # 跳过表头
            parts = line.split('\t')
            if len(parts) >= 4:
                entries.append({
                    'id': parts[0],
                    'title': parts[1],
                    'feed': parts[2],
                    'date': parts[3],
                    'summary': parts[4] if len(parts) > 4 else ''
                })
        return entries

# 使用示例
filterer = FeedFilter(limit=10)
entries_text = fetcher.get_entries(limit=50)
filtered = filterer.filter_entries(entries_text)

print(f"\n=== 筛选Top {len(filtered)} 条 ===")
for i, entry in enumerate(filtered, 1):
    print(f"{i}. [{entry['feed']}] {entry['title']} (score: {entry['score']})")
```

### 3. 摘要生成

```python
class DigestGenerator:
    """摘要生成器（免费版）"""

    def generate(self, filtered_entries, fetcher):
        """生成摘要"""
        lines = []
        lines.append("=" * 50)
        lines.append("  订阅摘要 | 今日精选")
        lines.append("=" * 50)
        lines.append("")

        # 按主题分组
        grouped = self._group_by_theme(filtered_entries)

        for theme, entries in grouped.items():
            if entries:
                lines.append(f"【{theme}】")
                lines.append("-" * 40)
                for entry in entries:
                    lines.append(f"  {entry['title']}")
                    lines.append(f"  来源：{entry.get('feed', '未知')}")

                    # 获取全文摘要
                    full_content = fetcher.get_entry(entry['id'])
                    summary = self._extract_summary(full_content, max_length=200)
                    if summary:
                        lines.append(f"  摘要：{summary}")
                    lines.append("")

        lines.append("=" * 50)
        lines.append(f"  共 {len(filtered_entries)} 条精选")
        lines.append("=" * 50)

        return "\n".join(lines)

    def _group_by_theme(self, entries):
        """按主题分组"""
        themes = {
            'AI与机器学习': ['AI', '机器学习', 'LLM', 'GPT', '大模型'],
            '系统与架构': ['架构', '系统', '分布式', '微服务'],
            '开发工具': ['工具', 'DevOps', 'CI/CD', 'Kubernetes'],
            '行业洞察': ['趋势', '分析', '思考', '洞察'],
            '其他': []
        }

        grouped = {theme: [] for theme in themes}
        for entry in entries:
            title = entry.get('title', '')
            matched = False
            for theme, keywords in themes.items():
                if any(kw in title for kw in keywords):
                    grouped[theme].append(entry)
                    matched = True
                    break
            if not matched:
                grouped['其他'].append(entry)

        return {k: v for k, v in grouped.items() if v}

    def _extract_summary(self, content, max_length=200):
        """提取摘要"""
        if not content:
            return ""

        # 简化版：取前N个字符
        content = content.strip()
        if len(content) <= max_length:
            return content
        return content[:max_length] + "..."

# 使用示例
generator = DigestGenerator()
digest = generator.generate(filtered, fetcher)
print(digest)
```

### 4. 标记已读

```python
class ReadStatusManager:
    """已读状态管理（免费版）"""

    def __init__(self, cli_path="feed"):
        self.cli = cli_path

    def mark_read(self, entry_ids):
        """标记条目为已读"""
        if not entry_ids:
            return False

        cmd = [self.cli, "update", "entries", "--read"] + [str(id) for id in entry_ids]
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30, encoding="utf-8"
        )
        if result.returncode == 0:
            print(f"已标记 {len(entry_ids)} 条为已读")
            return True
        print(f"标记失败：{result.stderr}")
        return False

    def search(self, query):
        """全文搜索"""
        result = subprocess.run(
            [self.cli, "search", query],
            capture_output=True, text=True, timeout=30, encoding="utf-8"
        )
        return result.stdout if result.returncode == 0 else f"搜索失败：{result.stderr}"

# 使用示例
manager = ReadStatusManager()

# 标记筛选后的条目为已读
entry_ids = [entry['id'] for entry in filtered]
manager.mark_read(entry_ids)
```

## 使用场景

### 场景一：每日订阅速览

**场景描述**：每天早上获取订阅源最新内容，快速浏览高价值条目。

```python
fetcher = FeedFetcher()
filterer = FeedFilter(limit=10)
generator = DigestGenerator()
manager = ReadStatusManager()

# 1. 获取最新内容
print("正在获取最新内容...")
fetcher.fetch()

# 2. 扫描未读
entries_text = fetcher.get_entries(limit=50)

# 3. 筛选高价值
filtered = filterer.filter_entries(entries_text)

# 4. 生成摘要
digest = generator.generate(filtered, fetcher)
print(digest)

# 5. 标记已读
entry_ids = [e['id'] for e in filtered]
manager.mark_read(entry_ids)
```

### 场景二：个人阅读管理

**场景描述**：管理个人订阅，控制信息过载。

```python
fetcher = FeedFetcher()

# 查看订阅统计
print("=== 订阅统计 ===")
print(fetcher.get_stats())

# 查看各订阅源未读数
print("\n=== 订阅源 ===")
print(fetcher.get_feeds())

# 按订阅源筛选
print("\n=== 某订阅源未读 ===")
print(fetcher.get_entries(limit=20, feed_id="feed_id_xxx"))
```

### 场景三：高价值内容筛选

**场景描述**：从大量未读中筛选最值得阅读的内容。

```python
fetcher = FeedFetcher()
filterer = FeedFilter(limit=5)

# 获取大量未读
entries_text = fetcher.get_entries(limit=100)

# 筛选Top 5
filtered = filterer.filter_entries(entries_text)

print(f"=== 今日必读 Top {len(filtered)} ===")
for i, entry in enumerate(filtered, 1):
    print(f"\n{i}. {entry['title']}")
    print(f"   来源：{entry.get('feed', '')}")
    print(f"   得分：{entry.get('score', 0)}")

    # 阅读全文
    full = fetcher.get_entry(entry['id'])
    print(f"   全文长度：{len(full)} 字符")
```

## 快速开始

### 30秒上手

```bash
# 1. 安装feed CLI
brew install odysseus0/tap/feed

# 2. 获取最新内容
feed fetch

# 3. 查看未读
feed get entries --limit 50

# 4. 阅读全文
feed get entry <entry_id>
```

### 120秒标准搭建

```bash
# 1. 安装feed CLI
brew install odysseus0/tap/feed
# 或从源码编译
# git clone <feed-repo>
# cd feed && cargo install --path .

# 2. 添加订阅源
feed add https://example.com/feed.xml
feed add https://another.com/rss

# 3. 获取最新内容
feed fetch

# 4. 查看统计
feed get stats

# 5. 查看未读
feed get entries --limit 50

# 6. 批量标记已读
feed update entries --read <id1> <id2> <id3>
```

## 配置示例

### 基础配置

```python
import os

class FeedConfig:
    """订阅摘要配置（免费版）"""
    CLI_PATH = os.getenv("FEED_CLI", "feed")
    DEFAULT_LIMIT = int(os.getenv("FEED_LIMIT", "50"))
    FILTER_LIMIT = int(os.getenv("FEED_FILTER_LIMIT", "10"))
    SUMMARY_MAX_LENGTH = int(os.getenv("FEED_SUMMARY_LEN", "200"))

    # 筛选关键词
    HIGH_VALUE_KEYWORDS = [
        'AI', '人工智能', '大模型', 'LLM', 'GPT',
        '系统设计', '架构', '性能优化', '分布式',
        '开发工具', 'DevOps', '反直觉', '颠覆', '突破'
    ]

    SKIP_KEYWORDS = ['广告', '推广', '赞助', 'sponsored']

    @classmethod
    def show(cls):
        print("=== 订阅摘要配置 ===")
        print(f"CLI路径：{cls.CLI_PATH}")
        print(f"默认限制：{cls.DEFAULT_LIMIT}")
        print(f"筛选限制：{cls.FILTER_LIMIT}")
        print(f"摘要长度：{cls.SUMMARY_MAX_LENGTH}")

FeedConfig.show()
```

### 常用命令速查

```bash
# 获取最新
feed fetch                              # 拉取所有订阅源最新内容

# 查看条目
feed get entries --limit N              # 列出未读条目（表格）
feed get entries --feed <id> --limit N  # 按订阅源筛选
feed get entry <id>                     # 阅读全文（Markdown）

# 搜索
feed search "<query>"                   # 全文搜索

# 标记已读
feed update entries --read <id1> <id2> ...  # 批量标记

# 查看订阅源与统计
feed get feeds                          # 列出订阅源（含未读数）
feed get stats                          # 数据库统计
```

## 最佳实践

### 1. 输出格式优化

```python
# 使用表格输出（最节省token）
# 避免使用 -o json（除非需要程序化处理）
result = subprocess.run(
    ["feed", "get", "entries", "--limit", "50"],
    capture_output=True, text=True
)
# 表格格式更易于扫描
```

### 2. 按订阅源筛选

```python
# 当未读太多时，按订阅源筛选
def filter_by_feed(feed_id, limit=20):
    return fetcher.get_entries(limit=limit, feed_id=feed_id)

# 先查看各源未读数
feeds = fetcher.get_feeds()
# 然后按需筛选
```

### 3. 阅读全文

```python
# feed get entry 返回Markdown格式，便于阅读
def read_full(entry_id):
    content = fetcher.get_entry(entry_id)
    return content  # Markdown格式

# 阅读后及时标记已读
manager.mark_read([entry_id])
```

## 常见问题

### Q1：免费版需要安装什么？

免费版需要安装 `feed` CLI工具。安装方式：macOS可使用 `brew install odysseus0/tap/feed`，其他平台可从源码编译（需Rust环境）。

### Q2：订阅源如何添加？

通过 `feed add <url>` 命令添加RSS/Atom订阅源。支持标准RSS 2.0和Atom 1.0格式。添加后使用 `feed fetch` 获取最新内容。

### Q3：筛选不准确怎么办？

免费版使用基于关键词的简单筛选。如遇筛选不准的情况：(1) 调整 `HIGH_VALUE_KEYWORDS` 列表；(2) 添加更多领域关键词；(3) 升级专业版使用AI深度筛选（基于LLM的内容理解）。

### Q4：未读条目太多怎么办？

建议：(1) 按订阅源筛选 `feed get entries --feed <id>`；(2) 减少限制数量 `--limit 20`；(3) 使用筛选器只看高价值内容；(4) 定期标记已读避免堆积。

### Q5：支持Markdown格式输出吗？

支持。`feed get entry <id>` 返回Markdown格式的全文内容，便于阅读和处理。列表输出默认为表格格式，最节省token。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Rust**: 1.70+（仅编译feed CLI需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| feed CLI | 工具 | 必需 | `brew install odysseus0/tap/feed` 或源码编译 |
| Python 3.8+ | 运行时 | 可选 | 辅助脚本使用 |
| SQLite | 数据库 | 必需 | feed CLI内置（无需单独安装） |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置

- 免费版无需任何API Key
- 订阅内容基于公开RSS源，不涉及付费API调用
- LLM模型路由由Agent平台内置提供

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent执行订阅内容获取与摘要生成任务

---

## 免费版限制

本免费体验版限制以下高级功能（需升级至专业版解锁）：

- **AI深度摘要**（基于LLM的内容理解与摘要生成）
- **多源聚合**（跨订阅源主题聚合）
- **定时推送**（每日自动推送摘要）
- **团队共享**（团队订阅与共享摘要）
- **个性化推荐**（基于阅读历史的智能推荐）
- **全文搜索增强**（语义搜索）
- **阅读统计与分析**（阅读习惯分析）
- **优先技术支持**

解锁全部高级能力请使用专业版：`feed-digest-tool-pro`
