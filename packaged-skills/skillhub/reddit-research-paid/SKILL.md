---

slug: "reddit-research-paid"
name: "reddit-research-paid"
version: 1.0.1
displayName: "Reddit调研(专业版)"
summary: "企业级Reddit社区调研方案，支持多平台聚合、自动化定时调研、情感分析与团队协作。。Reddit调研专业版是一套面向市场研究团队与内容机构的企业级社区调研解决方案，在免费版基础上扩展出多"
license: "Proprietary"
edition: "pro"
description: |-，可自动提升工作效率
  Reddit调研专业版是一套面向市场研究团队与内容机构的企业级社区调研解决方案，在免费版基础上扩展出多 Subreddit 并行扫描、自动化定时调研、跨平台舆情对比、情感分析与热度预测、团队协作与报告分发等能力。核心能力：提供多社区并行扫描与聚合分析、定时调研任务调度与趋势追踪、Reddit 与其他平台舆情对比、基于 NLP 的情感分析与话题热度预测、团队协作调研与报告自动分发
tags:
  - 调研
  - 集成工具
  - 内容创作
  - 企业级
  - 专业版
  - 搜索
  - 检索
  - 工具
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Knowledge"

---

# Reddit调研(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Reddit调研(专业版)情感分析 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 核心能力

### 能力一：多 Subreddit 并行扫描与聚合

支持同时扫描数十个 Subreddit，按主题、地域、语言等维度聚合分析，输出跨社区的综合洞察.
| 聚合维度 | 分析方法 | 输出形式 |
|:-----|:-----|:-----|
| 主题聚合 | 按关键词聚类 | 主题热度排行 |
| 地域聚合 | 按用户语言/地区 | 地域差异对比 |
| 时间聚合 | 按周/月趋势 | 趋势变化曲线 |
| 情感聚合 | 正负面分类 | 情感分布图 |
| 影响力聚合 | 按互动量加权 | 高影响力话题 |

### 能力二：自动化定时调研与趋势追踪
配置定时任务自动执行调研流程，追踪话题热度随时间的变化，识别上升期与衰退期话题.
**输入**: 用户提供能力二：自动化定时调研与趋势追踪所需的指令和必要参数.
**输出**: 返回能力二：自动化定时调研与趋势追踪的处理结果,包含执行状态码、结果数据和执行日志。### 能力三：跨平台舆情对比
将 Reddit 调研结果与 Twitter、Hacker News、Discord 等其他平台对比，识别跨平台共鸣话题与平台特异性话题.
**输入**: 用户提供能力三：跨平台舆情对比所需的指令和必要参数.
**处理**: 解析能力三：跨平台舆情对比的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 能力四：情感分析与话题热度预测
基于 NLP 模型对评论进行情感分类（正/负/中），结合历史数据预测话题热度走势.
**输入**: 用户提供能力四：情感分析与话题热度预测所需的指令和必要参数.
**处理**: 解析能力四：情感分析与话题热度预测的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回能力四：情感分析与话题热度预测的处理结果,包含执行状态码、结果数据和执行日志。### 能力五：团队协作调研与报告分发
支持多人协作调研，按角色分配社区与任务，调研报告自动分发到指定渠道.
**输入**: 用户提供能力五：团队协作调研与报告分发所需的指令和必要参数.
**处理**: 解析能力五：团队协作调研与报告分发的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回能力五：团队协作调研与报告分发的处理结果,包含执行状态码、结果数据和执行日志。### 能力六：品牌舆情监控与危机预警
监控品牌相关 mentions，识别负面舆情爆发早期信号，触发危机预警通知.
**处理**: 解析能力六：品牌舆情监控与危机预警的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回能力六：品牌舆情监控与危机预警的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`能力二：自动化定时调研与趋势追踪`的配置文档进行参数调优
### 聚合维度

针对聚合维度,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供聚合维度相关的配置参数、输入数据和处理选项.
**输出**: 返回聚合维度的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`聚合维度`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：品牌舆情监控

品牌团队持续监控 Reddit 上对本品牌的讨论，每日生成舆情简报，负面舆情爆发时立即告警.
### 场景二：竞品动态追踪

产品团队定期调研竞品相关 Subreddit，了解用户对竞品新功能的真实反馈，作为产品迭代参考.
### 场景三：行业趋势研究

市场研究团队对行业相关 20+ Subreddit 进行季度调研，输出行业趋势报告，支撑战略决策.
### 场景四：内容矩阵选题

内容机构管理多个垂直账号，通过多社区扫描为每个账号匹配最相关的话题，规划内容矩阵.
### 场景五：市场进入验证

进入新市场前，调研目标市场相关的 Subreddit，验证用户需求与竞争格局，降低市场进入风险.
## 使用流程

本助手为指令型 Skill，需要配合定时任务与团队配置使用。请确保已配置专业版授权与相关 API 凭据.
**典型提问模板**：

```
帮我监控品牌 ACME 在 Reddit 上的舆情，每日生成简报
```

```
对比 r/programming 与 Hacker News 上关于 Rust 的讨论差异
```

```
为 5 人团队配置 20 个 Subreddit 的协作调研方案
```

Agent 会根据需求匹配对应的能力模块，输出"策略配置 → 自动采集 → 深度分析 → 报告分发 → 趋势追踪"五段式方案.
#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | reddit-research处理的内容输入 |,  |
| content | string | 否 | reddit-research处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "research 相关配置参数",
    result: "research 相关配置参数",
    result: "research 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 症状 | 可能原因 | 排查方法 | 对策 |
|:---:|:---:|:---:|:---:|
| 扫描任务未执行 | 调度器故障或配置错误 | 查看调度器日志 | 修复配置或重启调度器 |
| 告警未触发 | 阈值设置不合理 | 查看告警规则 | 调整阈值并测试 |
| 情感分析准确率低 | 模型不适应领域 | 抽样人工对比 | 微调模型或更换 |
| 跨平台对比失败 | 平台 API 限流 | 查看请求日志 | 降低频率或换备用源 |
| 报告分发失败 | 通道配置错误 | 检查 Webhook 与邮箱 | 修复配置并重发 |
| 团队协作卡住 | 流程定义不清 | 查看任务状态 | 明确角色与职责 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 需能访问 reddit.com 及其他平台 API
- **Python**: 3.9+（用于调度脚本与情感分析）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| WebFetch 工具 | Agent工具 | 推荐 | Agent 内置工具 |
| curl | 命令行工具 | 必需 | 系统自带或安装 |
| apscheduler | 库 | 推荐 | pip install apscheduler |
| transformers | 库 | 可选 | pip install transformers（情感分析） |
| Reddit API 凭据 | 凭据 | 可选 | 申请 Reddit API 开发者账号 |
| Slack Webhook | 集成 | 可选 | Slack 工作区配置 |

### API Key 配置
- 本专业版使用 /.json 公开端点为基础，不需要 API Key
- 若使用 Reddit 官方 API（更高频率），需配置凭据于环境变量 `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET`
- Slack/钉钉 Webhook URL 等敏感配置应存储于密钥管理服务
- 禁止在 SKILL.md 或脚本中硬编码 API Token 或 Webhook URL

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，需要exec命令行执行扫描、调度与分析脚本）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行企业级社区调研流程

## 案例展示

### 多 Subreddit 并行扫描配置

```yaml
# multi-subreddit-scan.yaml
scan_groups:
  - name: brand_monitoring
    subreddits:
      - r/brandname
      - r/competitor1
      - r/competitor2
    schedule: daily
    depth: full_thread
# ...
  - name: industry_trends
    subreddits:
      - r/industry_main
      - r/industry_discussion
      - r/industry_news
    schedule: weekly
    depth: top_posts
# ...
  - name: market_research
    subreddits:
      - r/target_audience_1
      - r/target_audience_2
    schedule: monthly
    depth: deep_analysis
# ...
aggregation:
  dimensions: [topic, sentiment, influence]
  output_format: [markdown, pdf, dashboard]
```

### 自动化定时调研配置

```python
from apscheduler.schedulers.blocking import BlockingScheduler
import json
from datetime import datetime
# ...
def daily_brand_monitoring():
    """每日品牌舆情监控"""
    subreddits = ['brandname', 'competitor1', 'competitor2']
    results = []
# ...
    for sub in subreddits:
        # 获取最新与热帖
        new_posts = fetch_json(f"https://www.reddit.com/r/{sub}/new/.json?limit=25")
        hot_posts = fetch_json(f"https://www.reddit.com/r/{sub}/hot/.json?limit=25")
# ...
        # 情感分析
        analyzed = analyze_sentiment(new_posts + hot_posts)
# ...
        # 识别品牌 mentions
        brand_mentions = filter_brand_mentions(analyzed, brand='ACME')
# ...
        results.append({
            'subreddit': sub,
            'mentions': brand_mentions,
            'sentiment_summary': summarize_sentiment(brand_mentions)
        })
# ...
    # 生成报告并分发
    report = generate_report(results, date=datetime.today())
    distribute_report(report, channels=['email', 'slack'])
# ...
# 每日 8 点执行
scheduler = BlockingScheduler()
scheduler.add_job(daily_brand_monitoring, 'cron', hour=8)
scheduler.start()
```

### 跨平台舆情对比

```python
def cross_platform_comparison(topic):
    """跨平台话题对比"""
    platforms = {
        'reddit': fetch_reddit_mentions(topic),
        'hackernews': fetch_hn_mentions(topic),
        'twitter': fetch_twitter_mentions(topic)
    }
# ...
    comparison = {
        'topic': topic,
        'volume': {p: len(m) for p, m in platforms.items()},
        'sentiment': {p: analyze_sentiment(m) for p, m in platforms.items()},
        'unique_to_platform': find_unique_discussions(platforms),
        'cross_platform_resonance': find_resonance(platforms)
    }
# ...
    return comparison
```

### 情感分析配置

```yaml
# sentiment-analysis.yaml
model:
  type: finetuned_bert
  path: ./models/sentiment-v2
  labels: [positive, negative, neutral, mixed]
# ...
rules:
  - condition: negative_ratio > 0.4
    action: alert
    severity: warning
# ...
  - condition: negative_ratio > 0.6
    action: alert
    severity: critical
    notify: [brand_team, pr_team]
# ...
  - condition: mention_volume > historical_avg * 2
    action: alert
    severity: info
    message: "讨论量异常增长，可能存在热点事件"
```

### 团队协作配置

```yaml
# team-collaboration.yaml
team:
  - name: Alice
    role: lead
    assigned_subs: [r/brandname, r/competitor1]
    responsibilities: [strategy, final_review]
# ...
  - name: Bob
    role: analyst
    assigned_subs: [r/industry_main, r/industry_news]
    responsibilities: [scanning, deep_analysis]
# ...
  - name: Carol
    role: writer
    assigned_subs: [r/target_audience_1]
    responsibilities: [report_drafting]
# ...
workflow:
  - step: scan
    owner: analyst
    output: raw_findings
  - step: analyze
    owner: analyst
    output: structured_insights
  - step: draft_report
    owner: writer
    output: report_draft
  - step: review
    owner: lead
    output: final_report
# ...
distribution:
  - channel: email
    recipients: [stakeholders@company.com]
  - channel: slack
    webhook: ${SLACK_WEBHOOK_URL}
  - channel: notion
    database_id: ${NOTION_DB_ID}
```

## 常见问题

### Q1：多 Subreddit 并行扫描会触发限流吗？

会。Reddit 对未认证请求有较严格的限流。建议每秒不超过 1 次请求，并使用指数退避重试。专业版内置限流控制与队列调度.
### Q2：情感分析模型如何选择？

通用场景可用 VADER 或 TextBlob；垂直领域建议微调 BERT 模型；高准确率要求可接入商业 NLP API。模型选择需平衡准确率、成本、延迟.
### Q3：跨平台对比如何对齐数据？

不同平台的数据结构差异大。建议先抽取统一字段（如内容、时间、互动量、情感），再按主题或时间对齐分析.
### Q4：危机预警的阈值怎么定？

初期可参考行业基准（如负面 mention 占比 >30% 触发预警），积累历史数据后调整为基于自身基线的动态阈值.
### Q5：报告分发支持哪些渠道？

支持邮件、Slack/钉钉/企业微信 Webhook、Notion 数据库、飞书文档等。新增渠道可通过扩展分发适配器实现.
### Q6：团队协作如何避免重复劳动？

通过任务分配明确每人负责的 Subreddit 与职责，调研结果统一存储于共享空间，避免多人扫描同一社区.
### Q7：如何评估调研效果？

关键指标：话题发现数量、机会转化率（发现的 topic 中实际产出的内容占比）、舆情响应时长、报告阅读率。季度 review 这些指标.
### Q8：如何处理多语言社区？

配置语言检测与翻译流水线。扫描时自动识别帖子语言，非目标语言的帖子可选择跳过或翻译后分析。翻译质量会影响分析准确率，关键结论需人工校验.
### Q9：私有 Subreddit 如何调研？

私有 Subreddit 需要登录态与会员资格。可配置 Reddit API 凭据并加入该社区后访问，或委托社区成员代为调研.
### Q10：如何与现有 BI 工具集成？

调研结果可导出为 JSON/CSV 供 Tableau、Power BI 等工具消费，或直接写入数据仓库供 SQL 查询。建议建立标准化数据 schema 便于集成.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

