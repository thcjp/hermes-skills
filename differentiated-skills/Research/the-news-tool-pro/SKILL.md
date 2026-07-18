---
slug: the-news-tool-pro
name: the-news-tool-pro
version: "1.0.0"
displayName: 全球新闻情报专业版
summary: 企业级新闻情报分析平台,支持批量国家查询、长期归档、情感分析与趋势追踪
license: MIT
edition: pro
description: |-
  全球新闻情报专业版,面向企业团队和专业研究人员提供深度的全球新闻分析能力。
  支持批量国家查询、长期新闻归档、情感分析、趋势追踪、定制化报告生成等高级功能。

  核心能力:
  - 批量多国新闻并行查询,支持 20+ 国家同时获取
  - 长期新闻归档,支持数年历史数据回溯与分析
  - 新闻情感分析与主题聚类,挖掘舆论趋势
  - 跨国新闻对比分析,呈现不同视角差异
  - 定时监控与预警,自动追踪关键议题
  - 完整兼容免费版 API,平滑升级无障碍

  适用场景:
  - 企业公关与品牌舆情监控
  - 行业研究机构全球新闻追踪
  - 跨国企业多地区市场情报收集
  - 政府机构国际舆论分析

  差异化:
  - 专业版提供批量并行查询,效率提升 10 倍以上
  - 内置情感分析与趋势挖掘引擎
  - 支持长期归档与定时监控
  - 兼容免费版 API 体系,迁移成本趋近于零

  触发关键词: 新闻情报, 舆情监控, 批量新闻, 情感分析, 趋势追踪, 舆论分析, news intelligence, sentiment analysis, media monitoring
tags:
- 研究工具
- 新闻情报
- 舆情分析
- 企业级
tools:
- read
- exec
---

# 全球新闻情报专业版

## 概述

全球新闻情报专业版是企业级的新闻情报分析平台。在完整兼容免费版 API 的基础上,专业版引入了批量多国并行查询、长期新闻归档、情感分析、趋势追踪、定时监控预警等高级能力,适用于企业公关舆情监控、行业研究、跨国市场情报收集等专业场景。

专业版特别强化了数据分析能力,能够从海量新闻中提取舆论趋势、情感倾向、主题热点,并生成结构化的情报报告,帮助企业快速把握全球舆论动态。

## 核心能力

### 1. 批量多国并行查询

支持同时查询多个国家的新闻,显著提升数据采集效率。

```bash
# 批量查询配置 batch_countries.json
{
  "countries": ["us", "uk", "germany", "france", "japan", "china", "india", "brazil"],
  "mode": "parallel",
  "concurrency": 8,
  "output_format": "json"
}

# 执行批量查询
curl -s "https://www.thehear.org/api/batch-view" -d @batch_countries.json | jq

# 查看批量查询进度
news-tool batch status
```

### 2. 长期新闻归档

支持长期新闻数据归档,可回溯数年历史数据。

```bash
# 归档指定时间范围的新闻
news-tool archive create \
  --countries "us,uk,germany" \
  --from "2026-01-01" \
  --to "2026-07-17" \
  --output archive_2026_h1.json

# 查询归档数据
news-tool archive query \
  --archive archive_2026_h1.json \
  --country "us" \
  --date-range "2026-03-01:2026-03-31"

# 导出归档数据
news-tool archive export \
  --archive archive_2026_h1.json \
  --format csv \
  --output us_news_2026_h1.csv
```

### 3. 情感分析与主题聚类

从新闻标题中提取情感倾向和主题分布。

```bash
# 对指定国家的新闻进行情感分析
news-tool analyze sentiment \
  --country "us" \
  --topic "economic policy" \
  --date-range "2026-07-01:2026-07-17"

# 主题聚类分析
news-tool analyze topics \
  --countries "us,uk,germany" \
  --method "kmeans" \
  --clusters 10

# 跨国情感对比
news-tool analyze compare \
  --countries "us,uk,germany,france" \
  --topic "climate change" \
  --metric "sentiment"
```

### 4. 定时监控与预警

自动监控关键议题,触发预警。

```bash
# 配置监控任务 monitor_config.json
{
  "monitors": [
    {
      "name": "品牌舆情监控",
      "keywords": ["公司名称", "品牌名", "CEO姓名"],
      "countries": ["us", "uk", "china", "japan"],
      "alert_condition": "negative_sentiment > 0.3",
      "check_interval": "hourly"
    }
  ]
}

# 启动监控
news-tool monitor start monitor_config.json

# 查看监控状态
news-tool monitor status

# 查看预警记录
news-tool monitor alerts --date $(date +%Y-%m-%d)
```

### 5. 定制化报告生成

自动生成结构化的新闻情报报告。

```bash
# 生成每日新闻简报
news-tool report generate \
  --type daily_brief \
  --countries "us,uk,germany,china,japan" \
  --date $(date +%Y-%m-%d) \
  --output daily_brief.html

# 生成周度趋势报告
news-tool report generate \
  --type weekly_trend \
  --topic "technology" \
  --countries "us,china" \
  --format pdf \
  --output tech_weekly.pdf

# 生成跨国对比分析报告
news-tool report generate \
  --type comparison \
  --countries "us,china,russia" \
  --topic "trade policy" \
  --output trade_comparison.html
```

### 6. 完整兼容免费版

专业版完全兼容免费版的所有 API 调用,平滑升级。

```bash
# 免费版的所有命令在专业版中均可使用
curl -s "https://www.thehear.org/api/country-view/us" | jq
curl -s "https://www.thehear.org/api/country-view/germany?at=2026-07-01T20:00:00Z" | jq
```

## 使用场景

### 场景一:企业品牌舆情监控

某跨国企业公关团队需要每日监控全球主要市场中与公司相关的新闻报道,及时发现负面舆情。

```bash
# 步骤1:配置品牌监控关键词
cat > brand_monitor.json << 'EOF'
{
  "monitors": [
    {
      "name": "公司品牌监控",
      "keywords": ["CompanyName", "CompanyName Corp", "公司中文名"],
      "countries": ["us", "uk", "germany", "france", "china", "japan", "india"],
      "alert_condition": "negative_sentiment > 0.4 OR mention_count > 10",
      "check_interval": "hourly",
      "notification": "email + webhook"
    }
  ]
}
EOF

# 步骤2:启动监控
news-tool monitor start brand_monitor.json

# 步骤3:生成每日舆情报告
news-tool report generate \
  --type brand_daily \
  --config brand_monitor.json \
  --date $(date +%Y-%m-%d) \
  --output brand_daily_$(date +%Y%m%d).html

# 步骤4:查询历史舆情趋势
news-tool analyze trend \
  --keywords "CompanyName" \
  --countries "us,uk,germany,china" \
  --date-range "2026-01-01:2026-07-17" \
  --metric "sentiment,mention_count"
```

### 场景二:行业研究机构全球新闻追踪

某行业研究机构需要追踪全球科技行业的新闻报道,分析行业趋势和竞争格局。

```bash
# 步骤1:批量获取多国科技新闻
cat > tech_research.json << 'EOF'
{
  "countries": ["us", "uk", "germany", "france", "japan", "china", "india", "brazil"],
  "keywords": ["AI", "semiconductor", "quantum computing", "5G", "autonomous vehicle"],
  "date_range": "2026-07-01:2026-07-17",
  "output_format": "json"
}
EOF

news-tool batch research tech_research.json --output tech_news_raw.json

# 步骤2:进行主题聚类分析
news-tool analyze topics \
  --input tech_news_raw.json \
  --method "lda" \
  --clusters 15 \
  --output tech_topics.json

# 步骤3:跨国趋势对比
news-tool analyze compare \
  --input tech_news_raw.json \
  --countries "us,china,japan,germany" \
  --topic "AI" \
  --metric "sentiment,volume,trend"

# 步骤4:生成研究报告
news-tool report generate \
  --type industry_research \
  --input tech_news_raw.json \
  --template tech_industry \
  --output tech_industry_report_2026Q3.pdf
```

### 场景三:跨国企业多地区市场情报

一家跨境电商企业需要同时监控多个目标市场的政策新闻和行业动态。

```bash
# 步骤1:配置多地区监控
cat > market_intel.json << 'EOF'
{
  "regions": [
    {
      "name": "北美市场",
      "countries": ["us", "canada"],
      "topics": ["trade policy", "tariff", "e-commerce regulation"],
      "alert_level": "high"
    },
    {
      "name": "欧洲市场",
      "countries": ["uk", "germany", "france"],
      "topics": ["GDPR", "digital services act", "consumer protection"],
      "alert_level": "high"
    },
    {
      "name": "亚太市场",
      "countries": ["china", "japan", "india"],
      "topics": ["data security law", "cross-border e-commerce", "consumer rights"],
      "alert_level": "high"
    }
  ],
  "schedule": "0 9 * * *",
  "report_language": "zh-CN"
}
EOF

# 步骤2:执行多地区并行监控
news-tool monitor start market_intel.json

# 步骤3:生成多地区情报汇总
news-tool report generate \
  --type market_intelligence \
  --config market_intel.json \
  --output market_intel_$(date +%Y%m%d).html
```

## 快速开始

### 第一步:升级安装

```bash
# 安装专业版工具
cd ~/.skill-platform/workspace/skills/the-news-tool-pro
npm install

# 验证专业版功能
news-tool --version --edition

# 测试批量查询
news-tool batch query --countries "us,uk,germany" --limit 3
```

### 第二步:配置高级功能

```bash
# 配置专业版功能
cat > .env << 'EOF'
# 新闻 API 配置
NEWS_API_BASE=https://www.thehear.org/api
NEWS_API_KEY=your_premium_api_key

# 数据存储配置
ARCHIVE_DIR=./archives
ARCHIVE_FORMAT=json
ARCHIVE_COMPRESSION=gzip

# 分析引擎配置
SENTIMENT_MODEL=multilingual
TOPIC_MODEL=lda
LANGUAGE_DETECTION=true

# 监控配置
MONITOR_INTERVAL=3600
ALERT_WEBHOOK=https://your-webhook.example.com/alert
EOF
```

### 第三步:运行首次分析

```bash
# 执行批量新闻获取
news-tool batch query \
  --countries "us,uk,germany,france,japan,china" \
  --output news_batch.json

# 运行情感分析
news-tool analyze sentiment \
  --input news_batch.json \
  --output sentiment_report.json

# 生成分析报告
news-tool report generate \
  --type analysis \
  --input sentiment_report.json \
  --output analysis_report.html
```

## 配置示例

### 企业级监控配置

```json
{
  "edition": "pro",
  "api": {
    "base_url": "https://www.thehear.org/api",
    "rate_limit": "premium",
    "concurrent_requests": 20
  },
  "archive": {
    "enabled": true,
    "retention_days": 365,
    "compression": "gzip",
    "backup": "daily"
  },
  "analysis": {
    "sentiment": true,
    "topic_modeling": true,
    "language_detection": true,
    "trend_analysis": true
  },
  "monitoring": {
    "enabled": true,
    "check_interval": 3600,
    "alert_channels": ["email", "webhook", "slack"],
    "alert_thresholds": {
      "negative_sentiment": 0.4,
      "mention_spike": 2.0
    }
  },
  "reporting": {
    "auto_generate": true,
    "formats": ["html", "pdf"],
    "language": "zh-CN",
    "schedule": "daily"
  }
}
```

### 团队协作配置

```json
{
  "team": {
    "name": "news_intelligence_team",
    "members": [
      {"name": "alice", "role": "admin"},
      {"name": "bob", "role": "analyst"},
      {"name": "charlie", "role": "viewer"}
    ],
    "shared_archives": true,
    "shared_reports": true
  },
  "permissions": {
    "admin": ["all"],
    "analyst": ["query", "analyze", "report"],
    "viewer": ["view", "export"]
  }
}
```

## 最佳实践

### 1. 免费版到专业版的平滑迁移

```bash
# 1. 免费版的 API 调用在专业版中完全有效
curl -s "https://www.thehear.org/api/country-view/us" | jq

# 2. 专业版额外提供批量查询
news-tool batch query --countries "us,uk,germany"

# 3. 逐步引入高级分析功能
news-tool analyze sentiment --country "us" --topic "economy"
```

### 2. 批量查询的性能优化

```bash
# 根据网络情况调整并发数
news-tool batch query \
  --countries "$(cat all_countries.txt | tr '\n' ',')" \
  --concurrency 10 \
  --timeout 30

# 使用缓存避免重复查询
news-tool batch query \
  --countries "us,uk,germany" \
  --cache-dir ./cache \
  --cache-ttl 3600
```

### 3. 监控预警的精细化配置

```bash
# 多维度预警条件
{
  "alert_conditions": [
    {"metric": "negative_sentiment", "threshold": 0.4, "action": "immediate"},
    {"metric": "mention_count", "threshold": 10, "action": "summary"},
    {"metric": "trend_change", "threshold": 0.2, "action": "trend_report"}
  ],
  "alert_channels": {
    "immediate": ["webhook", "slack", "email"],
    "summary": ["email"],
    "trend_report": ["email"]
  }
}
```

## 免费版与专业版对比

| 功能特性 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 基础新闻查询 | 支持 | 支持 |
| 国家覆盖 | 20 个 | 20+(含扩展) |
| 批量并行查询 | 不支持 | 支持 |
| 历史数据回溯 | 7 天 | 数年归档 |
| 情感分析 | 不支持 | 支持 |
| 主题聚类 | 不支持 | 支持 |
| 跨国对比分析 | 不支持 | 支持 |
| 定时监控预警 | 不支持 | 支持 |
| 定制化报告 | 不支持 | 支持 |
| 调用频率限制 | 60 次/小时 | 无限制 |
| 团队协作 | 不支持 | 支持 |
| 适用场景 | 个人资讯 | 企业情报 |
| 技术支持 | 社区支持 | 优先支持 |

## 常见问题

### Q1: 专业版是否兼容免费版的 API 调用?

**A:** 完全兼容。专业版是免费版的超集,所有免费版的 API 调用和脚本在专业版中均可直接使用,无需修改。

### Q2: 情感分析支持哪些语言?

**A:** 专业版使用多语言情感分析模型,支持中、英、日、法、德、西、俄、阿拉伯等主要语种。对于小语种,会先进行语言检测,再调用对应模型分析。

### Q3: 监控预警如何配置通知渠道?

**A:** 支持多种通知渠道:

```bash
# 配置通知渠道
news-tool config set alert_channels \
  --email "alerts@example.com" \
  --webhook "https://hooks.example.com/news" \
  --slack "#news-alerts"
```

### Q4: 归档数据如何备份和迁移?

**A:** 专业版支持归档数据的备份和迁移:

```bash
# 导出归档数据
news-tool archive export --archive my_archive.json --format csv

# 备份到云存储
news-tool archive backup --destination s3://my-bucket/news-archives/

# 从备份恢复
news-tool archive restore --source s3://my-bucket/news-archives/
```

### Q5: 如何限制团队成员的访问权限?

**A:** 通过角色权限配置实现细粒度访问控制:

```bash
# 配置角色权限
news-tool team config set --role analyst --permissions "query,analyze,report"
news-tool team config set --role viewer --permissions "view,export"
```

## 依赖说明

### 运行环境

- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 需要稳定的互联网连接
- **存储**: 归档功能需要本地或云端存储空间

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | 官方网站下载安装 |
| curl | HTTP 工具 | 必需 | 系统自带 |
| jq | JSON 解析 | 推荐 | 包管理器安装 |
| thehear API | 新闻数据 | 必需 | 公共 API,专业版可注册获取更高配额 |
| Python | 分析引擎 | 分析功能必需 | 官方网站下载安装(3.9+) |
| 分析模型库 | 库 | 分析功能必需 | 通过 `pip install` 安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

专业版推荐配置以下 API Key 以获得更高配额:

```bash
# .env 文件配置
# 新闻 API(可选,注册获取更高配额)
NEWS_API_KEY=your_premium_news_api_key

# 分析引擎(可选,本地运行无需)
SENTIMENT_API_KEY=your_sentiment_api_key

# 通知渠道(可选)
SLACK_WEBHOOK=your_slack_webhook_url
ALERT_EMAIL=alerts@example.com
```

### 可用性分类

- **分类**: MD+EXEC+API(综合型,支持 API 调用、批量执行、数据分析和报告生成)
- **说明**: 企业级新闻情报分析平台,支持批量查询、长期归档、情感分析、趋势追踪等高级功能
- **适用规模**: 多用户、多地区、大规模数据采集与分析
- **兼容性**: 完全兼容免费版,支持平滑升级
