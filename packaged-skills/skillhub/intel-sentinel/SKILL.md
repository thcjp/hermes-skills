---
slug: intel-sentinel
name: intel-sentinel
version: "1.0.0"
displayName: "情报哨兵"
summary: "信息过载克星,50+平台聚合+四级分级+决策简报一键送达"
license: MIT
description: |-
  情报哨兵——信息太多看不过来?它替你盯50+平台,AI按S/A/B/C四级分级,语义去重不推重复新闻,只把值得看的S/A级情报整理成决策简报推送给你。共享缓存架构,多主题订阅扫描量降低83%。

  核心能力:
  - 50+平台聚合:热点聚合/RSS/趋势雷达/搜索引擎多源采集
  - SABC四级分级:S级立即推送/A级纳入简报/B级存档/C级过滤
  - 语义去重:相似报道自动合并,不重复推送
  - 决策简报:AI生成结构化简报,辅助快速判断
  - 定时扫描:每天3次(8:00/12:00/18:00)自动巡检
  - 主题订阅:科技/AI/教育默认订阅,支持自定义
  - 多渠道推送:S/A级情报自动推送到指定渠道
  - 内容矩阵联动:图文/短视频/数字人内容生产分支

  适用场景:
  - 行业资讯订阅者:不用每天刷50个平台,简报直接送到手
  - 媒体号运营者:自动化新闻采集→AI处理→内容分发
  - 内容矩阵操盘手:热点情报驱动内容生产,抢占首发
  - 企业情报监控:竞品动态/行业风向自动追踪
  - 副业达人追热点:S级情报第一时间推送,抢流量窗口

  输入要求:订阅主题+数据源偏好+推送渠道(可选)

  差异化:不是简单的RSS聚合器,而是AI四级分级+语义去重+决策简报,只推值得看的,共享缓存架构让多主题订阅成本降低83%。

  触发关键词:新闻监控、热点订阅、新闻推送、新闻播报、每日简报、行业资讯、情报监控、情报简报、新闻雷达、热点追踪
homepage: "https://skillhub.cn"
tags: [情报监控, 新闻聚合, 信息分级, 决策简报, 自动化]
tools: [read, exec]
---

# 情报哨兵 - 多源新闻情报监控雷达

> 定位: 多源新闻情报的采集、分级、去重、简报与分发一体化雷达
> 设计: 主题订阅 + 定时扫描 + AI四级分级(S/A/B/C) + 语义去重 + 决策简报 + 多渠道推送

## 使用场景

- 每日新闻简报生成与推送(定时触发,每天3次:8:00/12:00/18:00)
- 行业资讯订阅: 科技/AI/教育三方向默认订阅,支持自定义主题
- 媒体号运营: 自动化新闻采集→AI处理→内容分发
- 情报简报推送: S/A级情报自动推送到指定渠道,辅助决策
- 内容矩阵联动: 图文新闻→多平台分发,数字人播报,短视频

## 缓存架构说明

**架构原理**:
- 新闻条目按主题(topic)缓存到本地JSON文件,所有订阅共享同一份新闻缓存
- 主题订阅配置记录用户关注的topic,控制可见性
- 定时扫描时扫描所有订阅的不同主题(去重后),写入共享缓存
- 查看时只返回用户关注主题的缓存新闻

**效率提升**:
- 多主题订阅场景下,同一topic只扫描一次,所有关注该topic的订阅共享缓存
- 例如订阅5个主题,每天3次扫描只需15次,而非按订阅重复扫描(约83%降幅)

## 工作流

1. 初始化订阅配置
   - 读取订阅方向(默认: 科技/AI/教育)
   - 调用主题订阅接口: subscribe_topic(topic, sources, push_channels, matrix_enabled, seo_geo_enabled, product_link_enabled)
   - 自动写入订阅配置JSON文件
   - 检查点: 验证订阅配置写入成功

2. 多源新闻采集(定时扫描模式)
   - 调用 scan_all_topics() - 扫描所有订阅的不同主题
   - 内部流程: 查询订阅主题获取所有不同topic → 对每个topic调用数据源采集 → 写入共享缓存 → 更新主题缓存状态
   - 聚合多源数据: 热点聚合(50+平台) + RSS + 趋势雷达 + 搜索引擎
   - 检查点: 验证采集条目数

3. AI处理(在scan_all_topics内部完成)
   - 调用 score_news(news_items, threshold=6.0) - AI评分,按S/A/B/C四级分级
     - S级: score ≥ 9.0(重大情报,立即推送)
     - A级: 7.0 ≤ score < 9.0(重要情报,纳入简报)
     - B级: 6.0 ≤ score < 7.0(一般情报,存档备查)
     - C级: score < 6.0(低价值,过滤)
   - 调用 deduplicate_news(scored_news) - 语义去重,合并相似报道
   - 调用 generate_digest(deduped_news, language="zh") - 生成决策简报
   - 调用 fact_check(digest) - 事实核查
   - 检查点: 验证简报生成成功

4. 查看与分发
   - 调用 get_news(time_range, limit) 获取关注主题的缓存新闻
   - 推送简报: 调用 push_digest(digest, channel) 推送到指定渠道
   - 接口暴露: 写入简报JSON文件供第三方调用(原子写入)
   - 内容矩阵: 触发图文/短视频/数字人内容生产分支(由matrix_enabled配置触发)
   - 检查点: 验证推送状态

5. 内容矩阵联动(1+3分支,由matrix_enabled配置触发)
   - 主管道: 采集+AI处理+推送(8步)
   - 子分支-图文: 新闻→SEO/GEO优化→敏感词过滤→电商关联→图文发布(6步)
     - 触发条件: matrix_types包含'graphic'且matrix_enabled=true
     - 默认平台: 微信公众号/今日头条/知乎/百家号/微博
   - 子分支-短视频: 新闻→脚本→TTS配音→视频生成→发布(7步)
     - 触发条件: matrix_types包含'short_video'且matrix_enabled=true
   - 子分支-数字人: 新闻→脚本→数字人→口型同步→SEO→发布(8步)
     - 触发条件: matrix_types包含'digital_human'且matrix_enabled=true
   - 检查点: 验证矩阵分支触发状态

6. 状态持久化
   - JSON文件持久化: 订阅配置/新闻条目/主题缓存/推送日志/主题订阅
   - 文件结构: state.json(订阅状态) + items.json(新闻缓存) + digest.json(简报)
   - 记录审计日志
   - 验证: 校验数据完整性
   - 检查点: 验证持久化成功

## 输入格式

### 定时扫描输入(scan_all_topics)
```json
{
  "sources": ["hot_aggregator", "rss"],
  "time_range": "24h",
  "limit_per_topic": 50
}
```

### 主题订阅输入(subscribe_topic)
```json
{
  "topic": "科技",
  "sources": ["hot_aggregator", "rss"],
  "push_channels": ["qqbot"],
  "matrix_enabled": false,
  "seo_geo_enabled": false,
  "product_link_enabled": false
}
```

### 查看新闻输入(get_news)
```json
{
  "time_range": "24h",
  "limit": 50,
  "min_score": 6.0
}
```

## 输出格式

```json
{
  "success": true,
  "data": {
    "total": 25,
    "digest": "今日AI领域重要动态...",
    "items": [
      {
        "id": "...",
        "title": "...",
        "ai_score": 7.5,
        "grade": "A",
        "content_type": "news",
        "topic": "科技"
      }
    ],
    "digest_path": "digest/20260712/digest.json",
    "pushed": true,
    "persisted": true
  },
  "error": null,
  "code": null
}
```

## 异常处理

- **数据源不可用**: 采集内部熔断+降级(热点聚合失败→RSS兜底), 返回success=true+部分数据
- **AI调用失败**: score_news降级为默认5分(C级), generate_digest返回空摘要, 不阻塞流程
- **订阅主题为空**: scan_all_topics查询所有不同topic,若为空返回 `{"success": false, "error": "无订阅主题", "code": "NO_TOPIC"}`
- **limit超限**: 自动截断为100(边界保护)
- **推送通道不可用**: push_digest降级到文件持久化, 记录错误日志
- **JSON写入失败**: 降级到内存缓存, persisted=false, 记录告警
- **无订阅**: get_news返回空列表,success=true

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 |
| 新闻数据源 | API | 可选 | 热点聚合/RSS/搜索引擎(可手动输入新闻) |
| JSON文件存储 | 文件系统 | 必需 | exec工具创建state.json/items.json/digest.json |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - AI评分分级/语义去重/简报生成
- **NEWS_API_KEY**: 可选 - 新闻数据源API(可使用免费RSS)
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
新闻源支持RSS(免费)和热点聚合。AI评分降级为默认5分(C级)不阻塞流程。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

```bash
# 定时每日3次扫描(8:00/12:00/18:00) - 扫描所有订阅的不同主题
intel-sentinel scan --mode scan-all --sources "hot_aggregator,rss" --time-range 24h --limit 50

# 订阅主题
intel-sentinel subscribe --topic "科技" --sources "hot_aggregator,rss"

# 查看缓存新闻
intel-sentinel view --time-range 24h --limit 50

# 推送简报到指定渠道
intel-sentinel push --digest-path digest/20260712/digest.json --channel qqbot
```

## 时政新闻资质校验

非资质用户不得发布时政类新闻。校验逻辑:
1. 检查用户profile.political_news_qualified字段
2. 若topics包含"时政"/"政治"/"政策"且用户未获资质, 拒绝采集并返回 `{"success": false, "error": "无时政新闻资质", "code": "NO_QUAL"}`
3. 默认订阅方向(科技/AI/教育)不涉及时政, 无需校验

## 数据生命周期管理

- 新闻条目保留90天
- 推送日志保留30天
- scan_all_topics每次执行时自动清理过期数据
- 主题缓存记录每个主题的扫描状态和条目数
