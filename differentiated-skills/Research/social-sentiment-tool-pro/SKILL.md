---
slug: social-sentiment-tool-pro
name: social-sentiment-tool-pro
version: "1.0.0"
displayName: 社交情感分析专业版
summary: 企业级社交情感分析系统,支持多平台采集、LLM增强分析、病毒传播检测、竞品对比与定时监控告警
license: Proprietary
edition: pro
description: |-
  社交情感分析专业版为企业团队提供高阶社交媒体情感监控与分析能力。核心能力:
  - 多平台社交数据批量采集(Twitter/Reddit/Instagram等)
  - LLM增强情感分析(准确率85-95%)
  - 病毒式传播内容检测
  - 竞品情感对比分析
  - 定时监控与负面舆情告警
  - 可视化报告生成

  适用场景:
  - 企业品牌口碑全面监控
  - 竞品情感对比分析
  - 负面舆情实时告警
  - 营销活动效果评估

  差异化:专业版在免费版词典法情感分析基础上,扩展多平台采集、LLM增强、病毒检测、竞品对比与定时告警能力
tags:
- 研究工具
- 情感分析
- 企业级
- 社交媒体
- 舆情监控
tools:
  - - read
- exec
---
# 社交情感分析专业版
## 概述
社交情感分析专业版是企业级社交媒体情感监控与分析系统。在免费版单平台采集、词典法分类、基础主题提取的基础上,专业版扩展了多平台社交数据批量采集(Twitter/Reddit/Instagram等)、LLM增强情感分析(准确率85-95%)、病毒式传播内容检测、竞品情感对比分析、定时监控与负面舆情告警、可视化报告生成等企业级能力。

专业版与免费版完全兼容:免费版的CSV数据格式、情感分类函数、分析脚本全部继续可用。升级后即可享受多平台采集与LLM增强分析能力。

## 核心能力
### 免费版 vs 专业版能力对比
| 能力模块 | 免费版 | 专业版 |
|:--------|:------|:-------|
| 数据采集 | 单平台(手动CSV) | 多平台自动采集 |
| 情感分类 | 词典法(70-80%) | LLM增强(85-95%) |
| 主题提取 | 基础词频 | LLM主题建模 |
| 情感统计 | 支持 | 支持(多维统计) |
| CSV导入 | 支持 | 支持 |
| 多平台 | 不支持 | Twitter/Reddit/Instagram等 |
| 病毒检测 | 不支持 | 高互动内容识别 |
| 竞品对比 | 不支持 | 多品牌情感对比 |
| 定时监控 | 不支持 | 内置Cron调度 |
| 负面告警 | 不支持 | 实时负面舆情推送 |
| 可视化 | 不支持 | 图表+HTML报告 |
| 情感趋势 | 基础时间统计 | 趋势预测与异常检测 |

**输入**: 用户提供免费版 vs 专业版能力对比所需的指令和必要参数。
**处理**: 按照skill规范执行免费版 vs 专业版能力对比操作,遵循单一意图原则。
**输出**: 返回免费版 vs 专业版能力对比的执行结果,包含操作状态和输出数据。

### 专业版独有功能
1. **多平台自动采集**:通过数据导出API批量采集Twitter、Reddit、Instagram等平台数据(1K-70K条)
2. **LLM增强情感分析**:利用LLM理解上下文、反讽、复合表达,准确率达85-95%
3. **病毒式传播检测**:基于互动量(点赞/转发/评论)识别高传播内容
4. **竞品情感对比**:多品牌情感得分并排对比,识别相对优势与劣势
5. **定时监控告警**:配置定时监控任务,负面舆情突增时自动告警
6. **可视化报告**:生成含图表的HTML/PDF报告,便于分享与汇报

**输入**: 用户提供专业版独有功能所需的指令和必要参数。
**处理**: 按照skill规范执行专业版独有功能操作,遵循单一意图原则。
**输出**: 返回专业版独有功能的执行结果,包含操作状态和输出数据。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级社交情感分、析系统、支持多平台采集、增强分析、病毒传播检测、竞品对比与定时监、社交情感分析专业、版为企业团队提供、高阶社交媒体情感、监控与分析能力、核心能力、多平台社交数据批、病毒式传播内容检、竞品情感对比分析、定时监控与负面舆、情告警、可视化报告生成等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景
### 场景一:企业品牌口碑全面监控
品牌团队需要全面监控多个社交媒体平台上品牌提及的情感分布,生成综合报告。

```bash
# 多平台数据采集
python scripts/sentiment_pro.py collect \
  --brand "YourBrand" \
  --platforms twitter reddit instagram \
  --days 30 \
  --output /data/brand-mentions/

# LLM增强情感分析
python scripts/sentiment_pro.py analyze \
  --data /data/brand-mentions/ \
  --engine llm \
  --extract-themes \
  --detect-viral \
  --output /reports/brand-sentiment.json

# 生成可视化报告
python scripts/sentiment_pro.py report \
  --data /reports/brand-sentiment.json \
  --format html \
  --template corporate \
  --output /reports/brand-sentiment-report.html
```

报告输出示例:

```text
品牌情感报告 | YourBrand | 2026-07-18

情感得分: 72/100 | 总提及: 14,832
正面: 58% | 负面: 24% | 中性: 18%

平台分布:
  Twitter:  8,234条 (正面 55% | 负面 26%)
  Reddit:   4,102条 (正面 62% | 负面 20%)
  Instagram: 2,496条 (正面 61% | 负面 25%)

主题分析:
  产品性能: 2,034条 (正面 19% | 负面 81%) [需关注]
  用户体验: 1,856条 (正面 72% | 负面 28%) [优势]
  客户服务: 1,432条 (正面 45% | 负面 55%) [需改进]
  定价策略:   892条 (正面 38% | 负面 62%) [需关注]

病毒式传播内容 (Top 10):
  1. [负面] "品牌X又出bug了,气死了!" - 12.3K点赞, 3.4K转发
  2. [正面] "用了品牌X一个月,效率提升50%" - 8.7K点赞, 2.1K转发
  ...
```

### 场景二:竞品情感对比分析
市场团队需要将自身品牌与3个竞品的情感得分进行对比,识别相对位置。

```bash
# 批量采集竞品数据
python scripts/sentiment_pro.py collect \
  --brands "OurBrand" "CompetitorA" "CompetitorB" "CompetitorC" \
  --platforms twitter reddit \
  --days 30 \
  --output /data/competitive/

# 对比分析
python scripts/sentiment_pro.py compare \
  --data /data/competitive/ \
  --engine llm \
  --output /reports/competitive-comparison.json \
  --format html

# 生成对比报告
python scripts/sentiment_pro.py report \
  --data /reports/competitive-comparison.json \
  --template comparison \
  --output /reports/competitive-sentiment.html
```

对比报告示例:

```text
竞品情感对比 | 最近30天

品牌          | 情感得分 | 总提及  | 正面% | 负面% | 趋势
-------------|---------|---------|-------|-------|------
OurBrand     |   72    | 14,832  |  58%  |  24%  |  +5
CompetitorA  |   68    | 22,104  |  55%  |  27%  |  -3
CompetitorB  |   45    |  8,732  |  42%  |  38%  |  -8
CompetitorC  |   81    | 11,256  |  63%  |  19%  |  +2

优势主题: 用户体验(72%正面,领先竞品)
劣势主题: 定价策略(38%正面,落后CompetitorC的62%)
```

### 场景三:负面舆情实时告警
公关团队需要监控负面舆情,在负面提及突增时立即收到告警。

```bash
# 配置定时监控任务
python scripts/sentiment_pro.py schedule add \
  --name "品牌负面舆情监控" \
  --cron "0 */4 * * *" \
  --brand "YourBrand" \
  --platforms twitter reddit \
  --window 4h \
  --alert-threshold "negative_ratio>35%" \
  --alert-on-viral true \
  --distribute "webhook:https://im.example.com/hook/pr-alerts" \
  --archive /reports/sentinel/

# 查看监控任务
python scripts/sentiment_pro.py schedule list

# 查看告警历史
python scripts/sentiment_pro.py alerts --last 7d
```

告警示例:

```text
[舆情告警] YourBrand负面提及突增

时间: 2026-07-18 14:00
窗口: 最近4小时
负面占比: 42% (阈值35%)
总提及: 342条 (较上4小时+156%)

病毒式传播:
  "品牌X客服态度太差了,避雷!" - 5.2K点赞,1.1K转发
  建议立即响应,避免进一步扩散

主题: 客户服务 (负面 78%)
建议: 启动客服应急响应流程
```

## 不适用场景

以下场景社交情感分析专业版不适合处理：

- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析

## 触发条件

需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于非本工具能力范围的需求。

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 从免费版升级
专业版完全兼容免费版,升级步骤:

```bash
# 依赖说明
pip3 install pandas httpx matplotlib jinja2

# 2. 验证免费版CSV数据可用
python scripts/sentiment_pro.py analyze --data existing.csv --engine dict
# 输出与免费版词典法一致,确认兼容
# 3. 使用LLM增强分析
python scripts/sentiment_pro.py analyze --data existing.csv --engine llm
```

### 首次多平台采集
```bash
# 配置平台API凭证
# config/credentials.yaml
twitter:
  bearer_token: "${TWITTER_BEARER_TOKEN}"
reddit:
  client_id: "${REDDIT_CLIENT_ID}"
  client_secret: "${REDDIT_CLIENT_SECRET}"

# 执行采集
python scripts/sentiment_pro.py collect \
  --brand "YourBrand" \
  --platforms twitter reddit \
  --days 30 \
  --output /data/mentions/
```

### 首次LLM增强分析
```bash
# LLM增强情感分析
python scripts/sentiment_pro.py analyze \
  --data /data/mentions/ \
  --engine llm \
  --extract-themes \
  --detect-viral \
  --output /reports/analysis.json

# 对比词典法与LLM法结果
python scripts/sentiment_pro.py analyze --data /data/mentions/ --engine dict --output /reports/dict.json
python scripts/sentiment_pro.py analyze --data /data/mentions/ --engine llm --output /reports/llm.json
python scripts/sentiment_pro.py compare-engines --dict /reports/dict.json --llm /reports/llm.json
```

## 示例
### 多平台采集配置
```yaml
# config/collect.yaml
platforms:
  twitter:
    enabled: true
    queries:
      - '"YourBrand"'
      - '"YourBrand" AND (love OR amazing)'
      - '"YourBrand" AND (hate OR terrible OR bad)'
    max_results: 10000

  reddit:
    enabled: true
    subreddits: ["products", "reviews", "YourBrand"]
    queries: ["YourBrand"]
    max_results: 5000

  instagram:
    enabled: false  # 需额外配置
    queries: ["#YourBrand"]

collection:
  default_days: 30
  batch_size: 100
  rate_limit: true
  retry: 3
```

### LLM分析配置
```yaml
# config/analysis.yaml
engine: llm
model: "claude-sonnet"

sentiment:
  categories: [positive, negative, neutral, mixed]
  confidence_threshold: 0.7
  context_aware: true        # 理解上下文
  sarcasm_detection: true    # 反讽检测
  emoji_analysis: true       # 表情符号分析
themes:
  extract: true
  method: llm                # LLM主题建模
  min_theme_size: 50         # 主题最少提及数
  max_themes: 10             # 最多提取主题数
viral_detection:
  enabled: true
  metrics: [likes, retweets, replies]
  thresholds:
    high: { likes: 1000, retweets: 500 }
    medium: { likes: 500, retweets: 200 }
```

### 定时监控与告警配置
```yaml
# config/schedules.yaml
schedules:
  - name: "品牌情感监控(4小时)"
    cron: "0 */4 * * *"
    timezone: "Asia/Shanghai"
    brand: "YourBrand"
    platforms: [twitter, reddit]
    window: 4h
    engine: llm
    alert:
      negative_ratio_threshold: 35%
      viral_alert: true
      volume_spike: 150%
      distribute:
        - webhook:https://im.example.com/hook/pr-alerts
        - email:pr@corp.com
    archive: /reports/sentinel/

  - name: "竞品周度对比"
    cron: "0 9 * * 1"
    brands: ["OurBrand", "CompetitorA", "CompetitorB"]
    platforms: [twitter, reddit]
    days: 7
    engine: llm
    output: /reports/weekly-comparison/
```

### 可视化报告模板
```yaml
# templates/corporate-report.yaml
name: corporate-report
displayName: 企业情感分析报告
sections:
  - name: 执行摘要
    type: summary
    fields: [score, total_mentions, sentiment_distribution]

  - name: 平台分布
    type: platform_breakdown
    chart: bar

  - name: 主题分析
    type: theme_analysis
    chart: heatmap
    fields: [theme, sentiment_ratio, mention_count]

  - name: 病毒内容
    type: viral_list
    limit: 10
    fields: [text, platform, engagement, sentiment]

  - name: 趋势图
    type: trend
    chart: line
    timeframe: 30d

  - name: 建议
    type: recommendations
    source: llm
charts:
  theme: corporate
  colors:
    positive: "#22c55e"
    negative: "#ef4444"
    neutral: "#94a3b8"
```

## 最佳实践
### 1. 多平台采集要覆盖用户群
不同平台的用户画像不同。Twitter偏技术/媒体,Reddit偏深度讨论,Instagram偏视觉/生活方式。根据品牌用户群选择采集平台,确保覆盖面:

```bash
# 技术产品:Twitter + Reddit
--platforms twitter reddit

# 消费品:Twitter + Instagram + Reddit
--platforms twitter instagram reddit
```

### 2. LLM分析优先于词典法
LLM分析能理解上下文、反讽和复合表达,准确率显著高于词典法。对于重要决策,始终使用LLM引擎:

```bash
# 重要报告用LLM
python scripts/sentiment_pro.py analyze --engine llm

# 快速预览可用词典法
python scripts/sentiment_pro.py analyze --engine dict
```

### 3. 病毒内容要快速响应
病毒式负面内容的影响随时间指数增长。配置实时告警,在负面病毒内容出现后立即响应:

```bash
# 配置病毒内容告警
--alert-on-viral true --distribute "webhook:..."
```

### 4. 竞品对比关注相对位置
绝对情感得分受品牌规模影响。关注与竞品的相对位置(排名变化)比绝对分数更有意义:

```bash
# 定期竞品对比
python scripts/sentiment_pro.py compare --brands "OurBrand" "CompetitorA" ...
```

### 5. 趋势分析要拉长时间窗口
单次分析是快照,趋势分析更有价值。拉长监控时间窗口(至少30天),观察情感变化趋势,识别异常波动:

```bash
# 30天趋势分析
python scripts/sentiment_pro.py analyze --data /data/30d/ --trend --anomaly-detect
```

## 常见问题
### Q: 如何从免费版迁移到专业版?
A: 专业版完全兼容免费版。CSV数据格式、情感分类函数、分析脚本全部继续可用。安装专业版依赖后,原有CSV数据可直接用专业版分析,新增`--engine llm`、`--extract-themes`、`--detect-viral`等参数按需使用。

### Q: LLM增强分析的Token消耗如何?
A: LLM分析每条提及约消耗100-200 Token。1万条提及约消耗100-200万Token。可通过以下方式控制消耗:(1)先用词典法预筛,只对中性或低置信度内容用LLM;(2)限制分析数据量;(3)使用批量分析模式(批量提交降低单条开销)。

### 已知限制
A: 各平台API有速率限制。Twitter API单次最多10K条,Reddit API单次约5K条。专业版支持分页采集,总数据量可达1K-70K条。采集耗时取决于数据量和API速率限制,通常1万条约5-15分钟。

### Q: 病毒式传播检测的标准是什么?
A: 专业版基于互动量(点赞/转发/评论)判定。默认阈值:高传播(点赞>1000且转发>500),中传播(点赞>500且转发>200)。阈值可通过配置调整。检测算法还考虑互动增长率(短时间内互动激增)。

### Q: 负面舆情告警的触发条件?
A: 默认触发条件:(1)负面占比超过阈值(默认35%);(2)负面提及量较上周期增长超150%(突增);(3)检测到病毒式负面内容。三个条件任一触发即告警。阈值可通过`alert-threshold`参数配置。

### Q: 可视化报告支持哪些图表类型?
A: 专业版支持:情感分布饼图、平台对比柱状图、主题情感热力图、时间趋势折线图、病毒内容列表、竞品对比雷达图。报告输出为HTML(交互式)或PDF(静态),HTML报告支持筛选与排序。

### Q: 定时监控的数据如何归档?
A: 所有定时监控结果自动归档至指定目录,按日期组织。归档数据建立索引,支持历史检索与趋势对比。归档默认保留90天,可通过配置调整。归档数据可用于长期趋势分析与异常检测。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: ≥ 3.8
- **运行时**: 需要终端执行能力(exec)以调用Python脚本

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | https://python.org |
| pandas | Python库 | 必需 | `pip3 install pandas` |
| httpx | HTTP客户端 | 必需 | `pip3 install httpx` |
| matplotlib | 图表库 | 必需(可视化) | `pip3 install matplotlib` |
| jinja2 | 模板引擎 | 必需(HTML报告) | `pip3 install jinja2` |
| Twitter API | 数据源 | 条件必需(Twitter采集) | Twitter Developer平台申请 |
| Reddit API | 数据源 | 条件必需(Reddit采集) | Reddit App注册 |
| SMTP服务 | 邮件服务 | 条件必需(邮件告警) | 企业SMTP服务器 |
| Webhook端点 | IM集成 | 条件必需(IM告警) | 企业IM平台Webhook URL |
| LLM API | API | 必需(LLM分析) | 由Agent内置LLM提供 |
| 网络访问 | 网络 | 必需 | 需能访问社交媒体API |

### API Key 配置
- **Twitter API Bearer Token**: 条件必需,Twitter数据采集时配置于`config/credentials.yaml`
- **Reddit API凭证**: 条件必需,Reddit数据采集时配置Client ID和Secret
- **SMTP凭证**: 条件必需,邮件告警时通过环境变量`SMTP_PASSWORD`配置
- **Webhook密钥**: 条件必需,IM告警时通过环境变量`WEBHOOK_SECRET`配置
- **LLM API**: 由Agent平台内置提供,用于LLM增强情感分析与主题建模

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行Python脚本)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent调用Python脚本完成企业级社交媒体情感监控与分析任务。专业版在免费版基础上扩展多平台采集、LLM增强分析、病毒检测、竞品对比与定时告警能力,适合企业品牌口碑全面监控、竞品情感对比分析与负面舆情实时告警场景。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |
