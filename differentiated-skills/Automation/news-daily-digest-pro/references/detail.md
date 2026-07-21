# 详细参考 - news-daily-digest-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (json)

```json
// ~/workspace/news-digest/config.json
{
  "edition": "pro",
  "sources": {
    "x.com": {"enabled": true, "count": 10},
    "hacker_news": {"enabled": true, "count": 5},
    "reddit": {"enabled": true, "subreddits": ["technology", "AI"]},
    "rss": {"enabled": true, "feeds": [
      "https://feeds.example.com/tech",
      "https://feeds.example.com/ai"
    ]},
    "weibo_hot": {"enabled": true, "count": 5}
  },
  "search": {
    "multi_keyword": true,
    "boolean_logic": true,
    "max_keywords": 10
  },
  "analysis": {
    "sentiment": true,
    "trend_detection": true,
    "entity_extraction": true,
    "deduplication": true
  },
  "export": {
    "formats": ["png", "pdf", "html", "markdown", "json"],
    "template": "corporate"
  },
  "branding": {
    "logo_path": "~/workspace/news-digest/assets/logo.png",
    "watermark": "公司名 · 每日资讯",
    "footer": "由AI生成，仅供参考"
  },
  "scheduler": {
    "max_jobs": 50,
    "timezones": ["Asia/Shanghai", "America/New_York"]
  }
}
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│            每日新闻摘要专业版 (NEWS DAILY DIGEST PRO)             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │  多源聚合     │  │  多关键词搜索  │  │  品牌定制     │           │
│  │  Multi-Source│  │  Multi-Query │  │  Branding    │           │
│  │  ✅ 专业版    │  │  ✅ 专业版    │  │  ✅ 专业版    │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  情感分析     │  ← 正面/负面/中性 + 趋势        │
│                  │  Sentiment   │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  多格式导出   │  ← PDF/PNG/HTML/MD/JSON        │
│                  │  Export      │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  多时段调度   │  ← 无限定时任务                 │
│                  │  Scheduler   │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (json)

```json
{
  "scheduler": {
    "jobs": [
      {
        "name": "早间科技简报",
        "cron": "0 8 * * *",
        "keyword": "AI",
        "sources": ["x.com", "hacker_news", "rss"],
        "template": "tech_blue",
        "export": ["png", "pdf"]
      },
      {
        "name": "午间行业简报",
        "cron": "0 12 * * *",
        "keyword": "半导体 OR 芯片",
        "sources": ["x.com", "reddit", "weibo_hot"],
        "template": "corporate",
        "export": ["png", "html"]
      },
      {
        "name": "晚间财经简报",
        "cron": "0 18 * * 1-5",
        "keyword": "股市 OR 美股",
        "sources": ["x.com", "rss"],
        "template": "business_gray",
        "export": ["pdf", "json"]
      }
    ]
  }
}
```

## 代码示例 (json)

```json
{
  "branding": {
    "logo": {
      "path": "~/workspace/news-digest/assets/company-logo.png",
      "position": "top-right",
      "size": "120x40",
      "opacity": 1.0
    },
    "watermark": {
      "text": "公司名 · 每日资讯",
      "position": "bottom-center",
      "opacity": 0.1,
      "font_size": 48
    },
    "footer": {
      "text": "由AI生成 · 仅供参考 · © 2026 公司名称",
      "color": "#999999",
      "font_size": 14
    },
    "header": {
      "title": "每日AI资讯简报",
      "subtitle": "第 {issue_number} 期 · {date}"
    }
  }
}
```

## 代码示例 (json)

```json
{
  "meta": {
    "keyword": "AI",
    "generated_at": "2026-07-18T08:00:00+08:00",
    "sources": ["x.com", "hacker_news"],
    "total": 10
  },
  "articles": [
    {
      "title_original": "...",
      "title_translated": "...",
      "summary": "...",
      "source": "x.com",
      "url": "...",
      "engagement": {"likes": 100, "retweets": 50},
      "sentiment": {"label": "positive", "score": 0.92},
      "entities": ["OpenAI", "GPT-5"]
    }
  ],
  "analysis": {
    "sentiment_summary": {...},
    "trend": {...},
    "emerging_topics": [...]
  }
}
```

## 代码示例 (json)

```json
{
  "sentiment_analysis": {
    "overall": {
      "positive": 0.65,
      "neutral": 0.25,
      "negative": 0.10,
      "label": "偏正面"
    },
    "per_article": [
      {"title": "AI芯片需求激增", "sentiment": "positive", "score": 0.92},
      {"title": "某公司芯片良率问题", "sentiment": "negative", "score": 0.78}
    ],
    "entities": [
      {"name": "英伟达", "mentions": 8, "sentiment": "positive"},
      {"name": "AMD", "mentions": 5, "sentiment": "neutral"},
      {"name": "台积电", "mentions": 4, "sentiment": "positive"}
    ],
    "trend": {
      "vs_yesterday": "+15% 正面",
      "vs_last_week": "+8% 正面",
      "emerging_topics": ["先进封装", "HBM3", "3nm工艺"]
    }
  }
}
```

## 代码示例 (json)

```json
{
  "alerts": {
    "channels": {
      "dingtalk": {"webhook": "env:DINGTALK_WEBHOOK"},
      "email": {"to": ["pr@company.com"]}
    },
    "rules": [
      {
        "name": "负面舆情预警",
        "condition": "negative_ratio > 0.3",
        "channel": "dingtalk+email",
        "message": "检测到负面舆情激增，请立即关注"
      },
      {
        "name": "趋势异常预警",
        "condition": "sentiment_change < -20%",
        "channel": "dingtalk",
        "message": "情感趋势异常下降，请关注"
      }
    ]
  }
}
```

## 代码示例 (json)

```json
{
  "name": "品牌舆情监控",
  "cron": "0 9 * * *",
  "keyword": "公司名 OR 品牌名 OR 产品名",
  "sources": ["x.com", "weibo_hot", "zhihu_hot", "rss"],
  "analysis": {
    "sentiment": true,
    "entity_extraction": true,
    "trend_detection": true
  },
  "alerts": {
    "on_negative_spike": "dingtalk",
    "negative_threshold": 0.3
  },
  "export": ["pdf", "json"]
}
```

## 代码示例 (json)

```json
{
  "name": "品牌舆情监控",
  "cron": "0 9 * * *",
  "keyword": "公司名 OR 品牌名 OR 产品名",
  "sources": ["x.com", "weibo_hot", "zhihu_hot", "rss"],
  "analysis": {
    "sentiment": true,
    "entity_extraction": true,
    "trend_detection": true
  },
  "alerts": {
    "on_negative_spike": "dingtalk",
    "negative_threshold": 0.3
  },
  "export": ["pdf", "json"]
}
```

## 代码示例 (text)

```text
用户："生成'AI芯片'新闻简报，启用全部新闻源，附带情感分析"

Agent："正在聚合AI芯片新闻...
  ✅ X.com：抓取8条热门
  ✅ Hacker News：抓取3条
  ✅ Reddit r/technology：抓取2条
  ✅ RSS源（5个）：抓取4条
  ✅ 去重后共10条
  ✅ 情感分析完成：
     正面：7条（70%）
     中性：2条（20%）
     负面：1条（10%）
  ✅ 趋势：相比昨日，正面情绪上升15%
  📸 海报已生成（含情感分析图表）
  📤 已导出PNG + PDF + JSON"
```

### 300秒上手（完整企业配置）
```json
// ~/workspace/news-digest/config.json
{
  "edition": "pro",
  "sources": {
    "x.com": {"enabled": true, "count": 10},
    "hacker_news": {"enabled": true, "count": 5},
    "reddit": {"enabled": true, "subreddits": ["technology", "AI"]},
    "rss": {"enabled": true, "feeds": [
      "https://feeds.example.com/tech",
      "https://feeds.example.com/ai"
    ]},
    "weibo_hot": {"enabled": true, "count": 5}
  },
  "search": {
    "multi_keyword": true,
    "boolean_logic": true,
    "max_keywords": 10
  },
  "analysis": {
    "sentiment": true,
    "trend_detection": true,
    "entity_extraction": true,
    "deduplication": true
  },
  "export": {
    "formats": ["png", "pdf", "html", "markdown", "json"],
    "template": "corporate"
  },
  "branding": {
    "logo_path": "~/workspace/news-digest/assets/logo.png",
    "watermark": "公司名 · 每日资讯",
    "footer": "由AI生成，仅供参考"
  },
  "scheduler": {
    "max_jobs": 50,
    "timezones": ["Asia/Shanghai", "America/New_York"]
  }
}
```



## 架构总览
```text
┌─────────────────────────────────────────────────────────────────┐
│            每日新闻摘要专业版 (NEWS DAILY DIGEST PRO)             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │  多源聚合     │  │  多关键词搜索  │  │  品牌定制     │           │
│  │  Multi-Source│  │  Multi-Query │  │  Branding    │           │
│  │  ✅ 专业版    │  │  ✅ 专业版    │  │  ✅ 专业版    │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  情感分析     │  ← 正面/负面/中性 + 趋势        │
│                  │  Sentiment   │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  多格式导出   │  ← PDF/PNG/HTML/MD/JSON        │
│                  │  Export      │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                          │                                       │
│                          ▼                                       │
│                  ┌──────────────┐                                │
│                  │  多时段调度   │  ← 无限定时任务                 │
│                  │  Scheduler   │    ✅ 专业版                    │
│                  └──────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```



