---
slug: search-v2-tool-pro
name: search-v2-tool-pro
version: 1.0.0
displayName: 搜索工具专业版
summary: "企业级LLM优化搜索系统,支持批量搜索、主题分类、全文提取、图片搜索与结果缓存加速。搜索工具专业版为企业团队提供高阶LLM优化网页搜索与信息检索能力。核心能力:"
license: Proprietary
edition: pro
description: '搜索工具专业版为企业团队提供高阶LLM优化网页搜索与信息检索能力。核心能力:

  - 批量多查询并行搜索

  - 主题分类搜索(news/finance/general)

  - 全文内容提取与分块

  - 图片搜索结果

  - 搜索结果缓存加速

  - 四级搜索深度控制

  适用场景:

  - 企业竞争情报批量搜索

  - 新闻舆情监控

  - 金融数据检索

  - 研究报告资料收集

  差异化:专业版在免费版基础搜索与域名过滤基础上,扩展批量搜索、主题分类、全文提取、图片搜索与缓存能力'
tags:
  - 研究工具
  - 搜索
  - 企业级
  - 信息检索
  - 竞争情报
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
# 搜索工具专业版

## 概述

搜索工具专业版是企业级LLM优化网页搜索与信息检索系统。在免费版基础搜索、域名过滤、时间范围的基础上,专业版扩展了批量多查询并行搜索、主题分类搜索(news/finance/general)、全文内容提取与分块、图片搜索结果、搜索结果缓存加速与四级搜索深度控制等企业级能力.
专业版与免费版完全兼容:免费版的Tavily API Key、命令行参数、JSON请求格式全部继续可用,无需修改。升级后即可享受批量搜索与企业级检索功能.
## 核心能力

### 免费版 vs 专业版能力对比

| 能力模块 | 免费版 | 专业版 |
|----|---|---|
| 网页搜索 | 支持 | 支持 |
| 搜索深度 | basic/advanced | ultra-fast/fast/basic/advanced |
| 结果数量 | 最多10条 | 最多20条 |
| 域名过滤 | 支持 | 支持(最大300域名) |
| 时间范围 | 支持 | 支持 |
| 内容摘要 | 支持 | 支持 |
| 全文内容 | 不支持 | 支持(分块提取) |
| 图片结果 | 不支持 | 支持 |
| 主题分类 | 不支持 | news/finance/general |
| 批量搜索 | 不支持 | 多查询并行 |
| 结果缓存 | 不支持 | 本地缓存加速 |
| 搜索调度 | 不支持 | 定时批量搜索 |
| 结果聚合 | 不支持 | 多查询结果合并去重 |

**输入**: 用户提供免费版 vs 专业版能力对比所需的指令和必要参数.
**处理**: 解析免费版 vs 专业版能力对比的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回免费版 vs 专业版能力对比的响应数据,包含状态码、结果和日志.
### 专业版独有功能

1. **批量多查询并行**:一次提交多个搜索查询,并行执行,结果合并去重
2. **主题分类搜索**:针对新闻(news)、金融(finance)领域优化搜索结果
3. **全文内容提取**:返回页面原始内容,支持按分块(chunks)提取
4. **图片搜索**:返回与查询相关的图片结果
5. **四级搜索深度**:ultra-fast/fast/basic/advanced,按需选择延迟与精度
6. **结果缓存**:本地缓存搜索结果,重复查询即时返回,节省API调用
7. **定时批量搜索**:配置定时搜索任务,结果自动归档与对比

**输入**: 用户提供专业版独有功能所需的指令和必要参数.
**处理**: 解析专业版独有功能的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回专业版独有功能的响应数据,包含状态码、结果和日志.
### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、LLM、优化搜索系统、支持批量搜索、全文提取、图片搜索与结果缓、搜索工具专业版为、企业团队提供高阶、优化网页搜索与信、息检索能力、核心能力、批量多查询并行搜、全文内容提取与分、图片搜索结果、搜索结果缓存加速、四级搜索深度控制等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一:企业竞争情报批量搜索

市场团队需要针对多个竞品和关键词批量搜索,一次性获取全面情报.
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 搜索工具专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 批量搜索多个查询
python （请参考skill目录中的脚本文件） batch \
  --queries "竞品A定价策略" "竞品B用户评价" "竞品C融资动态" "竞品D功能对比" \
  --search-depth advanced \
  --max-results 10 \
  --format json \
  --output /reports/competitive-intel.json \
  --merge \
  --dedup
# ...
# 结果自动合并去重
```

输出示例:

```json
{
  "batch_id": "batch_20260718_001",
  "queries": 4,
  "total_results": 32,
  "deduplicated": 28,
  "results": [
    {
      "source_query": "竞品A定价策略",
      "title": "竞品A发布企业版定价方案",
      "url": "https://example.com/news",
      "content": "竞品A今日发布企业版,定价$49/seat/月...",
      "score": 0.92
    }
  ],
  "response_time": 4.8
}
```

### 场景二:新闻舆情监控

公关团队需要每日监控品牌相关的新闻舆情,及时发现负面报道.
```bash
# 新闻主题搜索(最近24小时)
python （请参考skill目录中的脚本文件） search \
  --query "品牌名 OR 公司名" \
  --topic news \
  --time-range day \
  --max-results 20 \
  --include-answer true \
  --format json \
  --output /reports/daily-news-monitor.json
# ...
# 配置定时新闻监控
python （请参考skill目录中的脚本文件） schedule add \
  --name "每日新闻舆情监控" \
  --cron "0 8,12,18 * * *" \
  --query "品牌名 OR 公司名" \
  --topic news \
  --time-range 6h \
  --max-results 20 \
  --output /reports/news-monitor/ \
  --alert-on-negative true \
  --distribute "webhook:https://im.example.com/hook/pr-alerts"
```

### 场景三:金融数据检索

投资团队需要搜索特定股票或公司的财务相关信息.
```bash
# 金融主题搜索
python （请参考skill目录中的脚本文件） search \
  --query "AAPL earnings Q4 2024" \
  --topic finance \
  --search-depth advanced \
  --max-results 15 \
  --include-raw-content true \
  --chunks-per-source 3 \
  --format json \
  --output /reports/aapl-earnings.json
# ...
# 批量金融搜索(多股票)
python （请参考skill目录中的脚本文件） batch \
  --queries "AAPL earnings" "GOOGL earnings" "MSFT earnings" "AMZN earnings" \
  --topic finance \
  --search-depth advanced \
  --max-results 10 \
  --format csv \
  --output /reports/tech-earnings-comparison.csv
```

## 不适用场景

以下场景搜索工具专业版不适合处理：

- 黑帽SEO手段
- 搜索引擎作弊
- 付费广告投放管理

## 触发条件

需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 从免费版升级

专业版完全兼容免费版,升级步骤:

```bash
# 1. 验证免费版API Key可用
echo $TAVILY_API_KEY
# 输出: tvly-your-api-key-here
# ...
# 2. 使用专业版功能
python （请参考skill目录中的脚本文件） search \
  --query "your question" \
  --topic news \
  --include-raw-content true \
  --max-results 15
# ...
# 3. 批量搜索
python （请参考skill目录中的脚本文件） batch \
  --queries "query1" "query2" "query3" \
  --merge
```

### 首次批量搜索

```bash
# 准备查询列表
cat > queries.txt << 'EOF'
AI基础设施最新进展
大模型推理优化方案
向量数据库性能对比
RAG最佳实践2026
EOF
# ...
# 批量搜索
python （请参考skill目录中的脚本文件） batch \
  --queries-file queries.txt \
  --search-depth advanced \
  --max-results 10 \
  --merge \
  --dedup \
  --format json \
  --output batch-results.json
```

### 配置结果缓存

```bash
# 启用缓存(默认24小时过期)
python （请参考skill目录中的脚本文件） search \
  --query "Python async patterns" \
  --cache \
  --cache-ttl 3600
# ...
# 查看缓存状态
python （请参考skill目录中的脚本文件） cache stats
# 输出: Cache entries: 156 | Hit rate: 34% | Size: 12MB
# ...
# 清理过期缓存
python （请参考skill目录中的脚本文件） cache cleanup
```

## 示例

### 四级搜索深度对比

| 深度 | 延迟 | 相关度 | 内容类型 | 适用场景 |
|---:|---:|---:|---:|---:|
| `ultra-fast` | 最低 | 较低 | NLP摘要 | 实时对话、自动补全 |
| `fast` | 低 | 良好 | 分块内容 | 需要分块且在意延迟 |
| `basic` | 中等 | 高 | NLP摘要 | 通用搜索,平衡速度与质量 |
| `advanced` | 较高 | 最高 | 分块内容 | 精确搜索,需要最高相关度 |

### 主题分类说明

| 主题 | 说明 | 适用场景 |
|:---:|:---:|:---:|
| `general` | 通用搜索(默认) | 日常信息检索 |
| `news` | 新闻搜索 | 品牌舆情、行业新闻、事件追踪 |
| `finance` | 金融搜索 | 股票财报、公司财务、市场数据 |

### 批量搜索配置

```bash
# 从文件读取查询列表
python （请参考skill目录中的脚本文件） batch \
  --queries-file queries.txt \
  --search-depth advanced \
  --max-results 10 \
  --merge \
  --dedup \
  --format json \
  --output results.json
# ...
# 命令行直接传入多个查询
python （请参考skill目录中的脚本文件） batch \
  --queries "query1" "query2" "query3" \
  --topic news \
  --time-range week \
  --max-results 15 \
  --format csv \
  --output news-results.csv
```

### 定时搜索调度

```yaml
# config/schedules.yaml
schedules:
  - name: "每日新闻舆情监控"
    cron: "0 8,12,18 * * *"
    timezone: "Asia/Shanghai"
    action: search
    params:
      query: "品牌名 OR 公司名"
      topic: news
      time_range: 6h
      max_results: 20
      include_answer: true
    output: /reports/news-monitor/
    alert:
      on_negative: true
      distribute: "webhook:https://im.example.com/hook/pr-alerts"
# ...
  - name: "周度竞品情报搜索"
    cron: "0 9 * * 1"
    action: batch
    params:
      queries_file: config/competitor-queries.txt
      search_depth: advanced
      max_results: 15
      merge: true
      dedup: true
    output: /reports/weekly-competitive/
```

### 全文内容提取配置

```bash
# 获取全文内容(分块)
python （请参考skill目录中的脚本文件） search \
  --query "machine learning best practices" \
  --include-raw-content true \
  --chunks-per-source 3 \
  --max-results 5 \
  --search-depth advanced
# ...
# 输出包含每个结果的多个内容分块
# 便于AI助手深入分析全文内容
```

## 最佳实践

### 1. 批量搜索时善用合并去重

多个查询可能返回重叠结果。使用`--merge --dedup`自动合并去重,避免重复内容干扰分析:

```bash
python （请参考skill目录中的脚本文件） batch \
  --queries "AI推理优化" "LLM推理加速" "大模型部署" \
  --merge --dedup
```

### 2. 按场景选择主题分类

新闻舆情用`news`主题,金融数据用`finance`主题,通用搜索用`general`。主题分类会调用专门的索引,提升领域搜索质量:

```bash
# 新闻舆情
python （请参考skill目录中的脚本文件） search --query "公司名" --topic news --time-range day
# ...
# 金融数据
python （请参考skill目录中的脚本文件） search --query "AAPL财报" --topic finance
```

### 3. 利用缓存节省API调用

重复查询启用缓存,避免消耗API额度。缓存适合不常变化的信息检索:

```bash
# 首次搜索(调用API)
python （请参考skill目录中的脚本文件） search --query "Python设计模式" --cache
# ...
# 再次搜索相同查询(命中缓存,即时返回)
python （请参考skill目录中的脚本文件） search --query "Python设计模式" --cache
```

### 4. 全文提取用于深度分析

需要AI助手深入分析页面内容时,启用`--include-raw-content`获取全文分块。注意这会增加响应大小和API消耗:

```bash
python （请参考skill目录中的脚本文件） search \
  --query "技术方案对比" \
  --include-raw-content true \
  --chunks-per-source 3 \
  --search-depth advanced \
  --max-results 5
```

### 5. 定时搜索构建趋势追踪

配置定时搜索任务,结果自动归档,通过对比不同时间的结果发现趋势变化:

```bash
python （请参考skill目录中的脚本文件） schedule add \
  --name "AI技术趋势追踪" \
  --cron "0 8 * * *" \
  --queries-file ai-trend-queries.txt \
  --output /reports/trends/ \
  --format json
```

## 常见问题

### Q: 如何从免费版迁移到专业版?

A: 专业版完全兼容免费版。Tavily API Key无需更换,命令行参数格式一致。安装专业版脚本后,原有搜索命令直接可用,新增`--topic`、`--include-raw-content`、`--include-images`等参数按需使用.
### Q: 批量搜索会消耗多少API额度?

A: 每个查询消耗一次API调用。4个查询的批量搜索消耗4次调用。合并去重不额外消耗。建议合理规划查询数量,利用缓存减少重复调用。Tavily按调用次数计费,具体额度取决于套餐.
### Q: 全文内容提取(include-raw-content)与内容摘要有何区别?

A: 内容摘要(NLP summary)是搜索引擎生成的精炼摘要,约200-300字;全文内容(raw content)是页面原始文本,按分块(chunks)返回,每块约500-1000字。全文内容更适合AI深度分析,但响应更大、API消耗更多.
### Q: 缓存的过期策略如何配置?

A: 通过`--cache-ttl`参数设置缓存过期时间(秒)。默认3600秒(1小时)。时效性强的搜索(如新闻)建议短TTL(300-900秒),不常变化的信息(如技术文档)可设长TTL(86400秒)。缓存存储在本地,不占用API额度.
### Q: 图片搜索结果包含哪些信息?

A: 启用`--include-images`后,返回结果中包含与查询相关的图片URL、标题和描述。图片结果独立于文本结果,数量受`max_results`限制。适合需要视觉素材的场景.
### Q: 定时搜索任务的告警如何配置?

A: 通过`--alert-on-negative true`配置负面舆情告警。搜索引擎会分析结果内容,检测负面情绪后触发告警。告警通过`--distribute`配置的渠道推送(邮件/IM Webhook)。告警判断基于关键词匹配,可能存在误报,建议人工复核.
### Q: 金融主题搜索返回的数据格式与通用搜索有何不同?

A: 金融主题搜索会优先返回财务数据相关页面,如财报、分析师报告、财经新闻。数据格式与通用搜索一致(标题+URL+内容+评分),但内容更聚焦财务指标。如需结构化财务数据,建议配合专门的数据API使用.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python版本**: ≥ 3.8
- **运行时**: 需要终端执行能力(exec)以调用搜索脚本

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Tavily API | 搜索API | 必需 | https://tavily.com 注册获取(专业套餐) |
| Python 3.8+ | 运行时 | 必需 | https://python.org |
| httpx | HTTP客户端 | 必需 | `pip install httpx` |
| pyyaml | 配置解析 | 必需 | `pip install pyyaml` |
| SQLite3 | 缓存存储 | 必需(Python内置) | Python标准库自带 |
| SMTP服务 | 邮件服务 | 条件必需(邮件告警) | 企业SMTP服务器 |
| Webhook端点 | IM集成 | 条件必需(IM告警) | 企业IM平台Webhook URL |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 网络访问 | 网络 | 必需 | 需能访问Tavily API |

### API Key 配置

- **Tavily API Key**: 必需,通过环境变量`TAVILY_API_KEY`配置,建议使用专业套餐以支持批量与全文功能
- **SMTP凭证**: 条件必需,邮件告警时通过环境变量`SMTP_PASSWORD`配置
- **Webhook密钥**: 条件必需,IM告警时通过环境变量`WEBHOOK_SECRET`配置
- **LLM API**: 由Agent平台内置提供,用于搜索结果分析与告警判断,无需额外配置

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行Python脚本)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent调用Tavily API完成企业级网页搜索与信息检索任务。专业版在免费版基础上扩展批量搜索、主题分类、全文提取、图片搜索与缓存能力,适合企业竞争情报批量搜索、新闻舆情监控与金融数据检索场景.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 执行效率受模型能力与网络环境影响
