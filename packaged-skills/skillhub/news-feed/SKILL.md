---
slug: "news-feed"
name: "news-feed"
version: 1.0.1
displayName: "News Feed"
summary: "从BBC/Reuters/AP等主流RSS抓最新新闻标题"
license: "Proprietary"
description: |-
  Fetch latest news headlines from major RSS feeds (BBC, Reuters, AP,
  Al Jazeera, NPR, The Guardian。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求.
tags:
  - Research
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
tools: ["read", "exec"]
tags: "新闻,信息,资讯"
category: "Knowledge"
---
# News Feed

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多源数据聚合与去重 | 不支持 | 支持 |
| 语义搜索与智能摘要 | 不支持 | 支持 |
| 定时监控与变化推送 | 不支持 | 支持 |
| 研究结论结构化导出 | 不支持 | 支持 |
| 知识图谱构建与关系推理 | 不支持 | 支持 |

## 核心能力

- **多源RSS抓取**：从BBC、Reuters、AP、Al Jazeera、NPR、The Guardian等主流新闻源RSS Feed获取最新标题与摘要
- **关键词过滤**：基于关键词、正则表达式或主题分类筛选新闻条目，支持包含/排除规则
- **时间范围筛选**：按发布时间范围（最近1小时/24小时/7天/自定义）过滤新闻
- **内容去重**：基于标题相似度与URL指纹检测重复新闻，跨源合并同一事件报道
- **摘要生成**：对多条相关新闻自动生成事件摘要，提取关键人物、地点、时间要素
- **多语言支持**：支持中英文新闻源，自动检测语言并可选翻译摘要

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 行业资讯追踪 | 行业关键词 + 新闻源 | 相关新闻列表 + 事件摘要 |
| 竞品动态监控 | 竞品名称 + 时间范围 | 竞品相关新闻 + 舆情趋势 |
| 主题研究 | 研究主题 + 多源配置 | 聚合新闻 + 去重 + 结构化报告 |
| 每日新闻简报 | 订阅源列表 + 时间范围 | 排序新闻列表 + 摘要 + 来源标注 |
| 事件追踪 | 事件关键词 + 时间窗口 | 事件发展时间线 + 多源报道对比 |

**不适用于**：实时推文抓取（需Twitter API）、付费墙内容全文获取、视频新闻转录、社交媒体舆情分析

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 指定新闻源（预设源或自定义RSS URL）和获取数量
3. 设置关键词过滤和时间范围（可选）
4. 执行抓取并查看返回的新闻条目列表
5. 如需摘要，指定相关条目进行摘要生成
6. 导出结果为结构化格式（JSON/Markdown）用于后续分析

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | 搜索关键词或主题描述 |
| sources | array | 否 | 新闻源列表，可选值: `bbc`/`reuters`/`ap`/`aljazeera`/`npr`/`guardian`/`all`，默认 `all` |
| count | integer | 否 | 每个源获取的条目数，默认 `10`，最大 `50` |
| time_range | string | 否 | 时间范围，可选值: `1h`/`24h`/`7d`/`30d`/`all`，默认 `24h` |
| keywords | array | 否 | 关键词过滤列表，仅返回包含任一关键词的条目 |
| dedup | boolean | 否 | 是否跨源去重，默认 `true` |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "total_items": 25,
    "items": [
      {
        "title": "Breaking: Major tech announcement",
        "source": "BBC",
        "url": "https://bbc.com/news/...",
        "published": "2024-01-15T10:30:00Z",
        "summary": "Summary of the news article...",
        "categories": ["Technology", "Business"]
      }
    ],
    "deduplicated": 3,
    "metadata": {
      "template_used": "reviewer",
      "sources_queried": 6,
      "sources_responded": 6,
      "time_range": "24h",
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 详细使用示例

### 示例1：获取BBC最新科技新闻

```text
输入(content): technology
输入(sources): ["bbc"]
输入(count): 5
输入(time_range): 24h

输出(items):
1. [BBC] AI breakthrough announced by leading lab
   URL: https://bbc.com/news/technology-...
   发布时间: 2024-01-15 08:30 UTC
   摘要: Researchers at a leading AI lab announced...

2. [BBC] New cybersecurity guidelines published
   URL: https://bbc.com/news/technology-...
   发布时间: 2024-01-15 06:15 UTC
   摘要: The government has published new guidelines...
```

### 示例2：多源聚合并去重

```text
输入(content): climate change
输入(sources): ["bbc", "reuters", "ap", "guardian"]
输入(count): 10
输入(dedup): true

输出:
总条目: 40 → 去重后: 28
去重的3条重复报道:
- "Global climate summit reaches agreement" (BBC + Reuters + AP 报道同一事件)
- "New renewable energy record set" (BBC + Guardian 报道同一事件)
- "Sea level rise study published" (Reuters + AP 报道同一事件)
```

### 示例3：关键词过滤追踪竞品

```text
输入(content): 竞品动态
输入(sources): ["all"]
输入(keywords): ["OpenAI", "Anthropic", "Google AI"]
输入(time_range): 7d

输出: 仅返回标题或摘要中包含上述关键词的新闻条目
匹配条目: 12
- [Reuters] OpenAI launches new model...
- [BBC] Google AI announces partnership...
- [AP] Anthropic publishes safety research...
```

## 支持的新闻源

| 源标识 | 名称 | RSS Feed URL | 语言 | 更新频率 |
|:-------|:-----|:-------------|:-----|:---------|
| bbc | BBC News | http://feeds.bbci.co.uk/news/rss.xml | English | 每5分钟 |
| reuters | Reuters | https://feeds.reuters.com/reuters/topNews | English | 每10分钟 |
| ap | Associated Press | https://feeds.apnews.com/rss/apf-topnews | English | 每15分钟 |
| aljazeera | Al Jazeera | https://www.aljazeera.com/xml/rss/all.xml | English | 每10分钟 |
| npr | NPR | https://feeds.npr.org/1001/rss.xml | English | 每10分钟 |
| guardian | The Guardian | https://www.theguardian.com/world/rss | English | 每5分钟 |

### 添加自定义RSS源
```json
{
  "custom_source": {
    "name": "TechCrunch",
    "url": "https://techcrunch.com/feed/",
    "language": "en",
    "category": "technology"
  }
}
```

## 最佳实践

### 获取策略
- 突发新闻追踪：使用 `time_range: "1h"` + `sources: ["bbc", "reuters"]` 获取最快更新源
- 深度研究：使用 `time_range: "7d"` + `sources: ["all"]` + `dedup: true` 获取多视角报道
- 主题监控：配合关键词过滤，定期执行以追踪特定话题发展

### 去重配置
- 默认开启去重（`dedup: true`），基于标题Jaccard相似度 >0.7 判定为重复
- 去重后保留最早发布的条目，其他标记为 `duplicates`
- 如需查看所有原始条目，设置 `dedup: false`

### 数据导出
```bash
# 导出为JSON
news-feed --export json --output news.json

# 导出为Markdown简报
news-feed --export markdown --output daily-brief.md
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接与代理设置 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 网络连接 | 网络 | 必需 | 需访问RSS Feed URL |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.

## 常见问题

### Q1: 如何开始使用News Feed？
A: 指定 `sources`（如 `["bbc", "reuters"]` 或 `["all"]`）、`count`（每个源条目数）和 `time_range`（时间范围）即可开始抓取。默认抓取所有源最近24小时的各10条新闻，自动去重。可使用 `content` 参数传入关键词进一步筛选，或使用 `keywords` 数组进行精确关键词匹配。

### Q2: RSS源无法访问怎么办？
A: 部分RSS源可能因网络限制或源服务器问题暂时不可达。输出中的 `sources_responded` 字段显示实际响应的源数量。如某些源持续不可达，可尝试：1）检查网络代理设置；2）使用 `custom_source` 添加镜像RSS URL；3）仅使用可用的源子集。单个源失败不影响其他源的抓取。

### Q3: 去重算法如何工作？
A: 去重基于标题文本的Jaccard相似度（分词后交集/并集 >0.7）和URL指纹（去除查询参数后的URL哈希匹配）。当两条新闻被判定为重复时，保留发布时间最早的条目，其余条目的URL记录在 `duplicates` 字段中。跨语言去重（如中英文同一事件）需要启用翻译后比较，默认不开启。

### Q4: 如何获取新闻全文而非仅摘要？
A: RSS Feed通常仅提供标题和简短摘要（200-500字符）。如需全文，需使用返回的 `url` 字段配合网页抓取工具（如WebFetch或curl）获取完整文章。注意部分新闻源有付费墙（如部分Reuters、AP文章），全文可能需要订阅。本工具不绕过付费墙，仅提供RSS中公开的摘要内容。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
| RSS Feed返回空 | 源暂时无更新或Feed地址变更 | 检查源是否正常更新，尝试更换备用Feed URL |
| 抓取超时 | 网络延迟或源服务器响应慢 | 减少 `count` 数量，或增加超时时间配置 |

## 已知限制

- 仅支持RSS/Atom Feed格式，不支持Twitter、Facebook等社交媒体API
- RSS摘要通常为200-500字符，不包含文章全文
- 去重基于标题相似度，对内容相同但标题差异大的新闻可能漏判
- 不支持需要认证的付费RSS源
- 单次请求最多抓取6个源 x 50条 = 300条新闻

