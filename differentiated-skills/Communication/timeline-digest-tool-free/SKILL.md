---
slug: timeline-digest-tool-free
name: timeline-digest-tool-free
version: "1.0.0"
displayName: 时间线摘要工具-免费版
summary: 抓取X/Twitter时间线并生成去重摘要,适合个人用户的信息聚合阅读
license: MIT
edition: free
description: |-
  时间线摘要工具免费版,从X(Twitter)时间线抓取推文并生成去重摘要。

  核心能力:
  - 抓取X/Twitter For You和Following时间线推文
  - 基于推文ID的硬去重
  - 基于文本相似度的近似去重
  - 增量过滤(避免重复处理已推送推文)
  - 生成结构化JSON摘要输出
  - 基础启发式过滤(去除广告、垃圾内容)

  适用场景:
  - 个人用户的信息聚合阅读
  - 关注领域的动态追踪
  - 减少信息噪音,提取高价值内容

  差异化:
  - 免费版聚焦单次摘要生成,操作简洁
  - 内置增量过滤,避免重复推送
  - 与PRO版完全兼容,可升级获得定时调度和智能分类摘要

  触发关键词: twitter, X, 时间线, 摘要, 去重, digest, timeline, 推文, 聚合, 信息流
tags:
- 沟通协作
- 信息聚合
- X/Twitter
- 内容摘要
tools:
- read
- exec
---

# 时间线摘要工具(免费版)

## 概述

时间线摘要工具免费版是一款X(Twitter)时间线信息聚合工具。通过命令行工具抓取For You和Following两个时间线的最新推文,进行增量过滤、硬去重和近似去重处理,最终生成结构化的JSON摘要数据,帮助用户快速了解关注领域的最新动态,减少信息噪音。

本版本聚焦单次摘要生成能力,内置增量过滤机制避免重复处理。适合个人用户的日常信息聚合阅读需求。如需定时自动调度、智能分类摘要、多源聚合等高级功能,请升级至PRO版。

### 免费版与PRO版能力对比

| 能力维度 | 免费版 | PRO版 |
|:---------|:-------|:------|
| 时间线抓取 | For You + Following | For You + Following + 自定义列表 |
| 硬去重(ID) | 支持 | 支持 |
| 近似去重(文本相似度) | 支持 | 支持(可调阈值) |
| 增量过滤 | 支持 | 支持 |
| 启发式过滤 | 基础(去广告/垃圾) | 高级(语义过滤) |
| 摘要输出 | 原始JSON | JSON + 智能分类摘要 |
| 定时调度 | 手动执行 | 自动定时 |
| 分类标注 | 不支持 | AI分类(科技/加密/洞察/其他) |
| 多源聚合 | 不支持 | 支持 |
| 状态管理 | 本地文件 | 本地+云端同步 |
| 推送通知 | 不支持 | 支持(Telegram/邮件等) |

## 核心能力

### 1. 时间线抓取

从X/Twitter的For You和Following两个时间线抓取最新推文。

```bash
# 抓取For You时间线(推荐流)
bird home -n 100 --json > for_you_raw.json

# 抓取Following时间线(关注流)
bird home --following -n 60 --json > following_raw.json
```

**参数说明:**
- `-n`: 抓取推文数量
- `--json`: 以JSON格式输出
- `--following`: 抓取Following时间线(不加此参数默认For You)

### 2. 增量过滤

基于上次运行时间戳,只处理新增推文,避免重复处理。

```python
import json
from datetime import datetime, timezone

class IncrementalFilter:
    """增量过滤器"""

    def __init__(self, state: dict):
        self.last_run_at = state.get("lastRunAt")
        self.sent_ids = state.get("sentTweetIds", {})

    def filter_new(self, tweets: list) -> list:
        """过滤出未处理过的新推文"""
        if not self.last_run_at:
            return tweets  # 首次运行,全部处理

        last_time = datetime.fromisoformat(self.last_run_at)
        new_tweets = []

        for tweet in tweets:
            # 检查ID是否已处理
            if tweet["id"] in self.sent_ids:
                continue
            # 检查时间是否在上次运行之后
            tweet_time = datetime.fromisoformat(
                tweet["createdAt"].replace("Z", "+00:00")
            )
            if tweet_time > last_time:
                new_tweets.append(tweet)

        return new_tweets

    def update_state(self, tweets: list) -> dict:
        """更新状态文件"""
        now = datetime.now(timezone.utc).isoformat()
        for tweet in tweets:
            self.sent_ids[tweet["id"]] = now
        return {
            "lastRunAt": now,
            "sentTweetIds": self.sent_ids
        }
```

### 3. 去重处理

#### 硬去重(基于推文ID)

```python
class Deduplicator:
    """推文去重器"""

    def dedup_by_id(self, tweets: list) -> list:
        """基于推文ID去重"""
        seen_ids = set()
        unique = []
        for tweet in tweets:
            if tweet["id"] not in seen_ids:
                seen_ids.add(tweet["id"])
                unique.append(tweet)
        return unique

    def dedup_near_duplicate(self, tweets: list, threshold: float = 0.9) -> list:
        """基于文本相似度的近似去重"""
        from difflib import SequenceMatcher

        unique = []
        for tweet in tweets:
            is_duplicate = False
            for existing in unique:
                similarity = SequenceMatcher(
                    None,
                    tweet["text"][:200],
                    existing["text"][:200]
                ).ratio()
                if similarity >= threshold:
                    is_duplicate = True
                    # 合并来源
                    if "sources" in existing:
                        existing["sources"] = list(
                            set(existing["sources"] + tweet.get("sources", []))
                        )
                    break
            if not is_duplicate:
                unique.append(tweet)
        return unique
```

### 4. 启发式过滤

自动过滤广告、垃圾内容和低价值推文。

```python
class HeuristicFilter:
    """启发式内容过滤器"""

    # 过滤规则
    SPAM_PATTERNS = [
        r'^(gm|good morning)\s*$',           # 纯问候
        r'^(gn|good night)\s*$',             # 纯晚安
        r'https?://\S+\s*$',                 # 纯链接
        r'^(liked|retweeted)\b',             # 系统通知
    ]

    SPAM_KEYWORDS = [
        "giveaway", "follow me", "check out",
        "limited time", "click here", "free crypto",
    ]

    def filter(self, tweets: list) -> list:
        """过滤低价值内容"""
        import re
        filtered = []

        for tweet in tweets:
            text = tweet["text"].strip().lower()

            # 跳过过短内容
            if len(text) < 10:
                continue

            # 跳过匹配垃圾模式的
            if any(re.match(p, text, re.IGNORECASE) for p in self.SPAM_PATTERNS):
                continue

            # 跳过包含垃圾关键词的
            if any(kw in text for kw in self.SPAM_KEYWORDS):
                continue

            filtered.append(tweet)

        return filtered
```

### 5. 结构化输出

```python
import json
from datetime import datetime, timezone, timedelta

class DigestGenerator:
    """摘要生成器"""

    def __init__(self, config: dict):
        self.interval_hours = config.get("intervalHours", 6)
        self.max_items = config.get("maxItemsPerDigest", 25)

    def generate(self, tweets: list) -> dict:
        """生成结构化摘要"""
        now = datetime.now(timezone.utc)
        window_start = now - timedelta(hours=self.interval_hours)

        # 排序并截取
        sorted_tweets = sorted(
            tweets,
            key=lambda t: t.get("createdAt", ""),
            reverse=True
        )[:self.max_items]

        return {
            "window": {
                "start": window_start.isoformat(),
                "end": now.isoformat(),
                "intervalHours": self.interval_hours
            },
            "counts": {
                "fetched": len(tweets),
                "final": len(sorted_tweets)
            },
            "items": [
                {
                    "id": t["id"],
                    "author": t.get("author", ""),
                    "createdAt": t.get("createdAt", ""),
                    "text": t["text"],
                    "url": t.get("url", f"https://x.com/i/web/status/{t['id']}"),
                    "sources": t.get("sources", [])
                }
                for t in sorted_tweets
            ]
        }


# 使用示例
config = {"intervalHours": 6, "maxItemsPerDigest": 25}
generator = DigestGenerator(config)

# 假设已处理好的推文列表
tweets = [
    {"id": "123", "text": "AI最新进展...", "author": "@technews",
     "createdAt": "2026-07-18T10:00:00+08:00", "sources": ["forYou"]}
]

digest = generator.generate(tweets)
print(json.dumps(digest, indent=2, ensure_ascii=False))
```

## 使用场景

### 场景一:每日信息聚合

个人用户每天运行一次,获取关注领域的最新动态摘要。

```bash
# 完整流程:抓取 -> 过滤 -> 去重 -> 输出
# 步骤1:抓取两个时间线
bird home -n 100 --json > for_you.json
bird home --following -n 60 --json > following.json

# 步骤2:运行摘要生成脚本
python3 generate_digest.py --for-you for_you.json --following following.json > digest.json

# 步骤3:查看摘要
python3 format_digest.py --input digest.json
```

**输出示例:**
```json
{
  "window": {
    "start": "2026-07-18T00:00:00+08:00",
    "end": "2026-07-18T06:00:00+08:00",
    "intervalHours": 6
  },
  "counts": {
    "forYouFetched": 100,
    "followingFetched": 60,
    "afterIncremental": 34,
    "afterDedup": 26,
    "final": 20
  },
  "items": [
    {
      "id": "123456789",
      "author": "@technews",
      "createdAt": "2026-07-18T02:15:00+08:00",
      "text": "OpenAI发布GPT-5模型,支持多模态推理...",
      "url": "https://x.com/technews/status/123456789",
      "sources": ["forYou", "following"]
    }
  ]
}
```

### 场景二:关注领域追踪

追踪特定领域的最新推文动态。

```bash
# 抓取后按关键词筛选
python3 generate_digest.py --filter "AI,LLM,GPT,大模型" > ai_digest.json

# 输出筛选后的摘要
python3 format_digest.py --input ai_digest.json --format text
```

### 场景三:减少信息过载

通过去重和过滤,将大量推文压缩为高价值摘要。

```bash
# 查看处理统计
python3 generate_digest.py --stats-only

# 输出示例:
# 抓取统计:
#   For You: 100条
#   Following: 60条
#   增量过滤后: 34条
#   去重后: 26条
#   启发式过滤后: 20条
#   最终输出: 20条
#   压缩率: 87.5%
```

## 快速开始

### 前置条件

1. 安装bird命令行工具并完成认证(cookie登录)
2. 安装Python 3.8+

### 安装与配置

```bash
# 1. 确认bird已安装并认证
bird --version
bird auth status

# 2. 创建配置文件
cat > config.json << 'EOF'
{
  "intervalHours": 6,
  "fetchLimitForYou": 100,
  "fetchLimitFollowing": 60,
  "maxItemsPerDigest": 25,
  "similarityThreshold": 0.9,
  "statePath": "~/.timeline-digest/state.json"
}
EOF

# 3. 创建状态目录
mkdir -p ~/.timeline-digest
```

### 首次运行

```bash
# 运行摘要生成
python3 generate_digest.py --config config.json

# 首次运行会处理全部推文(无增量过滤)
# 后续运行只处理新增推文
```

## 配置示例

### 基础配置

```json
{
  "intervalHours": 6,
  "fetchLimitForYou": 100,
  "fetchLimitFollowing": 60,
  "maxItemsPerDigest": 25,
  "similarityThreshold": 0.9,
  "statePath": "~/.timeline-digest/state.json"
}
```

### 配置项说明

| 配置项 | 类型 | 默认值 | 说明 |
|:-------|:-----|:-------|:-----|
| intervalHours | number | 6 | 时间窗口(小时) |
| fetchLimitForYou | number | 100 | For You抓取数量 |
| fetchLimitFollowing | number | 60 | Following抓取数量 |
| maxItemsPerDigest | number | 25 | 摘要最大推文数 |
| similarityThreshold | number | 0.9 | 近似去重相似度阈值 |
| statePath | string | ~/.timeline-digest/state.json | 状态文件路径 |

## 最佳实践

### 1. 合理设置抓取数量

```text
抓取数量建议:
- 高频用户(每天多次运行): For You 50, Following 30
- 中频用户(每天1-2次): For You 100, Following 60
- 低频用户(每周1-2次): For You 200, Following 100
```

### 2. 调整相似度阈值

```python
# 相似度阈值调整建议
THRESHOLD_GUIDE = {
    0.95: "严格去重 - 仅去除几乎完全相同的内容",
    0.90: "标准去重 - 去除高度相似的内容(推荐)",
    0.85: "宽松去重 - 去除主题相似的内容",
    0.80: "激进去重 - 可能误删不同视角的同类内容",
}
```

### 3. 状态文件管理

```python
# 状态文件定期清理(保留30天)
import os
import json
from datetime import datetime, timedelta

def cleanup_state(state_path: str, retain_days: int = 30):
    """清理过期的状态记录"""
    with open(state_path, 'r') as f:
        state = json.load(f)

    cutoff = datetime.now() - timedelta(days=retain_days)
    sent_ids = state.get("sentTweetIds", {})

    cleaned = {
        tid: ts for tid, ts in sent_ids.items()
        if datetime.fromisoformat(ts) > cutoff
    }

    state["sentTweetIds"] = cleaned
    with open(state_path, 'w') as f:
        json.dump(state, f, indent=2)

    removed = len(sent_ids) - len(cleaned)
    print(f"清理完成: 移除 {removed} 条过期记录")
```

## 常见问题

### Q1: bird工具是什么?如何安装?

**A:** bird是一个X/Twitter命令行工具,用于读取时间线推文。安装后需要通过cookie方式完成认证登录。请参考bird工具的官方文档进行安装和认证。

### Q2: 首次运行时为什么处理了全部推文?

**A:** 首次运行时没有状态记录,无法进行增量过滤,因此会处理全部抓取到的推文。从第二次运行开始,只会处理上次运行之后的新增推文。

### Q3: 近似去重的阈值应该设多少?

**A:** 推荐使用默认值0.9(标准去重)。如果发现摘要中有太多相似内容,可降低到0.85;如果发现去重过于激进导致内容丢失,可提高到0.95。

### Q4: 免费版支持定时自动运行吗?

**A:** 免费版需要手动执行。如需定时自动调度运行,请升级至PRO版,PRO版支持cron定时任务和自动推送通知。

### Q5: 如何生成中文分类摘要?

**A:** 免费版输出原始JSON数据。生成中文分类摘要(科技/加密/洞察等分类)需要结合LLM处理,这是PRO版的智能摘要功能。

### Q6: 如何升级到PRO版?

**A:** PRO版与免费版完全兼容,升级后原有配置和状态文件继续使用,同时获得定时调度、智能分类摘要、多源聚合等高级功能。直接安装PRO版Skill即可完成升级。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **网络环境**: 需可访问X/Twitter服务

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| bird | CLI工具 | 必需 | 参考bird工具文档安装 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 可选 | 仅JS脚本执行时需要 |

### API Key 配置

- bird工具的认证(cookie)由bird工具自行管理
- 本Skill基于Markdown指令,无需额外API Key
- 如需LLM智能摘要功能,由Agent内置LLM提供

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行时间线摘要任务
- **运行模式**: 本地脚本执行,需bird工具已认证
- **安全等级**: 只读操作,不修改X/Twitter账户数据;状态文件存储在本地
