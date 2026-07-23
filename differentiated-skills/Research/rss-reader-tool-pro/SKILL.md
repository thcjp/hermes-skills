---
slug: rss-reader-tool-pro
name: rss-reader-tool-pro
version: 1.0.0
displayName: RSS阅读器专业版
summary: 企业级RSS阅读与监控系统,支持定时调度、邮件推送、多用户配置、全文搜索与高级内容分析
license: Proprietary
edition: pro
description: 'RSS阅读器专业版为企业团队提供高阶RSS订阅阅读与监控能力。核心能力:

  - 大规模订阅源管理(100+源)

  - 内置Cron定时调度引擎

  - 多渠道推送(邮件/IM/Webhook)

  - 多用户配置与权限管理

  - 全文索引与搜索

  - 高级内容分析(情感/热度/趋势)


  适用场景:

  - 企业竞争情报定时监控与推送

  - 团队内容研究协作

  - 行业媒体自动化追踪

  - 多角色定制化推送


  差异化:专业版在免费版订阅管理与内容研究基础上,扩展定时调度、多渠道推送、多用户配置、全文搜索与高级分析能力'
tags:
- 研究工具
- RSS
- 企业级
- 内容监控
- 竞争情报
tools:
- - read
- exec
homepage: https://skillhub.cn
pricing_tier: L4
pricing_model: monthly
suggested_price: 99.9
---

# RSS阅读器专业版

## 概述

RSS阅读器专业版是企业级RSS订阅阅读与监控系统。在免费版订阅管理、关键词监控、内容研究模式的基础上,专业版扩展了大规模订阅源管理、内置Cron定时调度、多渠道推送、多用户配置、全文索引搜索与高级内容分析等企业级能力。

专业版与免费版完全兼容:免费版的`feeds.json`配置、命令行参数、输出格式均可直接被专业版使用,无需迁移。升级后即可享受定时自动化与企业级推送功能。

## 核心能力

### 免费版 vs 专业版能力对比

| 能力模块 | 免费版 | 专业版 |
|:--------|:------|:-------|
| 订阅管理 | 支持(建议≤20源) | 支持(100+源) |
| 分类管理 | 支持 | 支持(多级分类树) |
| 关键词监控 | 支持 | 支持(正则+词表) |
| 时间筛选 | 按小时 | 按小时+自定义区间 |
| 列表输出 | 支持 | 支持 |
| 内容研究模式 | 支持 | 支持(增强版) |
| JSON输出 | 支持 | 支持 |
| 自动摘要 | 支持 | 支持(LLM增强) |
| 定时调度 | 不支持 | 内置Cron引擎 |
| 邮件推送 | 不支持 | SMTP自动发送 |
| IM推送 | 不支持 | Webhook至企业IM |
| 多用户 | 不支持 | 用户独立配置与权限 |
| 全文搜索 | 不支持 | 全文索引引擎 |
| 内容分析 | 不支持 | 情感/热度/趋势分析 |
| 历史归档 | 不支持 | 全文归档+检索 |

**输入**: 用户提供免费版 vs 专业版能力对比所需的指令和必要参数。
**处理**: 按照skill规范执行免费版 vs 专业版能力对比操作,遵循单一意图原则。
**输出**: 返回免费版 vs 专业版能力对比的执行结果,包含操作状态和输出数据。

### 专业版独有功能

1. **大规模订阅管理**:支持100+订阅源,批量导入导出,按分类树组织
2. **内置Cron调度引擎**:无需系统crontab,内置调度支持时区、重试、任务依赖
3. **多渠道推送**:摘要自动推送至邮件、企业IM(Webhook)、文件系统
4. **多用户配置**:每个用户独立订阅列表、关键词偏好与推送渠道
5. **全文索引搜索**:对所有抓取内容建立全文索引,支持复杂查询
6. **高级内容分析**:情感分析、热度评分、趋势检测,辅助内容决策
7. **历史归档检索**:所有检查结果自动归档,支持时间线回溯

**输入**: 用户提供专业版独有功能所需的指令和必要参数。
**处理**: 按照skill规范执行专业版独有功能操作,遵循单一意图原则。
**输出**: 返回专业版独有功能的执行结果,包含操作状态和输出数据。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、RSS、阅读与监控系统、支持定时调度、全文搜索与高级内、阅读器专业版为企、业团队提供高阶、订阅阅读与监控能、核心能力、大规模订阅源管理、定时调度引擎、多用户配置与权限、全文索引与搜索等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一:企业竞争情报定时监控

市场团队需要每小时监控竞品动态,关键信息自动推送至企业IM群,每日生成汇总邮件。

```bash
# 批量导入竞品订阅源
node scripts/rss.js sources import competitors.opml --category competitors

# 配置每小时监控(关键信息推送到IM)
node scripts/rss.js schedule add \
  --name "竞品实时监控" \
  --cron "0 * * * *" \
  --category competitors \
  --keywords "发布,融资,收购,定价,裁员,launch,funding" \
  --format ideas \
  --distribute "webhook:https://im.example.com/hook/competitive-alerts" \
  --priority high

# 配置每日汇总邮件
node scripts/rss.js schedule add \
  --name "每日竞争情报汇总" \
  --cron "0 8 * * *" \
  --timezone "Asia/Shanghai" \
  --category competitors \
  --since 24h \
  --format ideas \
  --distribute "email:market-team@corp.com" \
  --template competitive-daily
```

推送到IM的实时告警示例:

```text
[竞品告警] Competitor A 发布新功能
标题: Introducing AI-Powered Analytics
要点: 新增AI分析模块,支持自然语言查询,定价$29/seat/月
角度: 直接对标我方Analytics Pro,需评估定价策略
链接: https://competitor-a.com/blog/ai-analytics
时间: 2分钟前 | 热度: 高 | 情感: 正面
```

### 场景二:多团队内容研究协作

不同团队(产品、技术、市场)各自关注不同订阅源和关键词,专业版支持多用户独立配置。

```bash
# 创建用户并配置独立订阅
node scripts/rss.js user create product-team --config-dir /users/product/
node scripts/rss.js user create tech-team --config-dir /users/tech/
node scripts/rss.js user create market-team --config-dir /users/market/

# 产品团队:关注产品设计与用户体验
node scripts/rss.js user exec product-team -- add "https://www.smashingmagazine.com/feed/" --category design
node scripts/rss.js user exec product-team -- schedule add --cron "0 9 * * *" --format ideas --distribute "email:product@corp.com"

# 技术团队:关注技术架构与开源项目
node scripts/rss.js user exec tech-team -- add "https://news.ycombinator.com/rss" --category tech
node scripts/rss.js user exec tech-team -- schedule add --cron "0 9 * * *" --keywords "架构,性能,开源" --distribute "email:tech@corp.com"

# 市场团队:关注行业媒体与竞品
node scripts/rss.js user exec market-team -- add "https://techcrunch.com/feed/" --category news
node scripts/rss.js user exec market-team -- schedule add --cron "0 8 * * *" --distribute "email:market@corp.com"
```

### 场景三:全文搜索与趋势分析

研究团队需要检索历史归档中的特定主题,并分析关键词热度趋势。

```bash
# 全文搜索
node scripts/rss.js search "向量数据库" --since 30d --format ideas

# 关键词趋势分析
node scripts/rss.js analyze trend \
  --keywords "AI,LLM,RAG,向量数据库" \
  --since 90d \
  --interval weekly \
  --output /reports/keyword-trends.json

# 热度排行
node scripts/rss.js analyze hot \
  --since 7d \
  --top 20 \
  --by engagement
```

趋势分析输出示例:

```text
关键词趋势分析 | 最近90天(按周)

关键词        | 本周提及 | 上周提及 | 趋势   | 热度
-------------|---------|---------|--------|------
AI           |   342   |   298   | +14.8% | 极高
LLM          |   187   |   203   |  -7.9% | 高
RAG          |    89   |    62   | +43.5% | 上升
向量数据库     |    67   |    54   | +24.1% | 上升
```

## 不适用场景

以下场景RSS阅读器专业版不适合处理：

- 黑帽SEO手段
- 搜索引擎作弊
- 付费广告投放管理

## 触发条件

需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于非本工具能力范围的需求。

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
npm install xml2js node-fetch nodemailer

# 2. 验证免费版配置可用
node scripts/rss.js list
# 输出与免费版一致,确认兼容

# 3. 启用专业版功能
node scripts/rss.js pro enable --license "YOUR-PRO-KEY"

# 4. 配置第一个定时任务
node scripts/rss.js schedule add \
  --name "每日简报" \
  --cron "0 8 * * *" \
  --format ideas \
  --distribute "email:you@corp.com"
```

### 首次配置定时调度

```bash
# 创建每日内容研究任务
node scripts/rss.js schedule add \
  --name "每日内容灵感" \
  --cron "0 8 * * *" \
  --timezone "Asia/Shanghai" \
  --since 24h \
  --format ideas \
  --distribute "email:creator@corp.com" \
  --template daily-inspiration

# 查看调度任务
node scripts/rss.js schedule list

# 手动触发测试
node scripts/rss.js schedule run "每日内容灵感"

# 查看执行历史
node scripts/rss.js schedule logs "每日内容灵感" --last 7
```

### 配置推送渠道

```yaml
# config/distribute.yaml
email:
  smtp_host: smtp.corp.com
  smtp_port: 587
  smtp_user: rss-bot@corp.com
  smtp_password: "${SMTP_PASSWORD}"
  from: "RSS阅读器 <rss-bot@corp.com>"

webhook:
  im_alerts:
    url: https://im.example.com/webhook/xxx
    format: card
    secret: "${WEBHOOK_SECRET}"
  
  slack:
    url: https://hooks.slack.com/services/xxx
    format: block
```

#
## 示例

### 定时调度配置

```yaml
# config/schedules.yaml
schedules:
  - name: "竞品实时监控"
    cron: "0 * * * *"
    category: competitors
    keywords: ["发布", "融资", "收购", "定价", "launch", "funding"]
    format: ideas
    distribute:
      - webhook:im_alerts
    priority: high
    retry: 3

  - name: "每日内容灵感"
    cron: "0 8 * * *"
    timezone: "Asia/Shanghai"
    since: 24h
    format: ideas
    distribute:
      - email:creator@corp.com
    template: daily-inspiration

  - name: "周度趋势回顾"
    cron: "0 9 * * 1"
    timezone: "Asia/Shanghai"
    action: analyze
    params:
      type: trend
      since: 7d
      keywords: ["AI", "LLM", "RAG"]
    distribute:
      - email:team@corp.com
```

### 多用户配置结构

```text
config/
├── users/
│   ├── product-team/
│   │   ├── feeds.json          # 用户订阅列表
│   │   ├── schedules.yaml      # 用户调度配置
│   │   └── preferences.json    # 用户偏好设置
│   ├── tech-team/
│   │   ├── feeds.json
│   │   ├── schedules.yaml
│   │   └── preferences.json
│   └── market-team/
│       ├── feeds.json
│       ├── schedules.yaml
│       └── preferences.json
├── global/
│   ├── distribute.yaml         # 全局推送渠道
│   └── templates/              # 全局模板
└── pro.yaml                    # 专业版授权
```

### 自定义推送模板

```yaml
# templates/competitive-daily.yaml
name: competitive-daily
displayName: 竞争情报日报
brand:
  header: "# 竞争情报日报 | {{date}}"
  footer: "---\n由RSS阅读器专业版自动生成"
sections:
  - name: 高优先级动态
    filter:
      priority: high
      keywords: ["融资", "收购", "发布"]
    format: ideas
    limit: 10
  - name: 行业资讯
    filter:
      min_hotness: 0.5
    format: list
    limit: 20
  - name: 趋势信号
    filter:
      type: trend
    format: signal
    limit: 5
analysis:
  sentiment: true
  hotness: true
  trend: weekly
```

## 最佳实践

### 1. 按团队拆分订阅配置

不要让所有团队共享一个订阅列表。为每个团队创建独立用户配置,各自管理订阅源、关键词和推送渠道,避免信息过载和相互干扰。

### 2. 实时告警与每日汇总分离

高频监控(每小时)使用IM Webhook推送关键信息,低频汇总(每日)使用邮件发送完整报告。这样既保证关键信息及时触达,又不至于频繁邮件打扰。

### 3. 利用全文索引避免信息遗漏

专业版对所有检查结果自动建立全文索引。定期使用`search`命令检索特定主题,确保没有遗漏重要信息:

```bash
# 检索最近30天关于某主题的所有文章
node scripts/rss.js search "竞品A定价策略" --since 30d
```

### 4. 趋势分析辅助内容决策

定期运行趋势分析,发现上升中的关键词,提前布局内容创作:

```bash
# 每周趋势分析
node scripts/rss.js analyze trend --since 7d --top 10 --output weekly-trends.json
```

### 5. 推送模板按角色定制

不同角色关注不同粒度。为管理层配置精简模板(只看高优先级),为执行层配置详尽模板(包含分析数据):

```bash
# 管理层:精简版
node scripts/rss.js schedule add --name "管理层简报" --template executive-brief --distribute "email:c-level@corp.com"

# 执行层:详尽版
node scripts/rss.js schedule add --name "执行层详报" --template detailed-report --distribute "email:team@corp.com"
```

## 常见问题

### Q: 如何从免费版迁移到专业版?

A: 专业版完全兼容免费版。安装专业版依赖后,免费版的`feeds.json`、命令行参数、输出格式全部继续可用。运行`node scripts/rss.js pro enable`激活专业版功能,原有订阅配置自动识别。

### Q: 多用户模式下如何保证配置隔离?

A: 每个用户拥有独立的配置目录(`config/users/<user_id>/`),包含各自的`feeds.json`、`schedules.yaml`和`preferences.json`。调度任务按用户独立执行,推送渠道按用户配置路由,用户间配置互不影响。

### Q: 全文索引会占用多少存储空间?

A: 全文索引基于本地嵌入式搜索引擎,每1000篇文章约占用5-10MB存储空间。索引在检查时自动增量构建,无需额外维护。支持通过`search reindex`命令重建索引。

### Q: 定时调度任务失败如何排查?

A: 运行`schedule logs <task-name>`查看执行日志。常见原因:订阅源URL失效、网络超时、推送渠道配置错误。专业版提供失败重试(默认3次,指数退避),重试耗尽后发送告警。

### Q: IM Webhook推送支持哪些平台?

A: 专业版支持所有提供Webhook URL的IM平台,包括企业通讯工具、Slack、Discord等。通过`config/distribute.yaml`配置Webhook URL和消息格式(card/block/text)。不同平台的格式适配通过模板自动处理。

### Q: 趋势分析的数据来源是什么?

A: 趋势分析数据来源于专业版自动归档的历史检查结果。每次`check`执行的结果(含文章元数据)都会归档,趋势分析基于这些历史数据统计关键词提及频率变化。数据保留默认90天,可通过配置调整。

### Q: 高级内容分析的情感分析准确率如何?

A: 专业版内置基于词典的情感分析,中英文准确率约75-85%。情感分析结果用于分类展示与告警过滤,不作为唯一决策依据。如需更高准确率,可启用LLM增强模式(消耗额外Token)。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: ≥ 14
- **运行时**: 需要终端执行能力(exec)以调用Node.js脚本

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js 14+ | 运行时 | 必需 | https://nodejs.org |
| xml2js | npm包 | 必需 | `npm install xml2js` |
| node-fetch | npm包 | 必需 | `npm install node-fetch` |
| nodemailer | npm包 | 条件必需(邮件推送) | `npm install nodemailer` |
| SMTP服务 | 邮件服务 | 条件必需(邮件推送) | 企业SMTP服务器 |
| Webhook端点 | IM集成 | 条件必需(IM推送) | 企业IM平台Webhook URL |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 网络访问 | 网络 | 必需 | 需能访问目标RSS源URL |

### API Key 配置

- **专业版授权Key**: 运行`node scripts/rss.js pro enable --license "YOUR-KEY"`激活
- **SMTP凭证**: 通过环境变量`SMTP_PASSWORD`配置,或写入`config/distribute.yaml`
- **Webhook密钥**: 通过环境变量`WEBHOOK_SECRET`配置
- **LLM API**: 由Agent平台内置提供,用于增强摘要与情感分析,无需额外配置

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行Node.js脚本)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent调用Node.js脚本完成企业级RSS阅读与监控任务。专业版在免费版基础上扩展定时调度、多渠道推送、多用户配置、全文搜索与高级分析能力,适合企业竞争情报监控、团队内容研究协作与多角色定制化推送场景。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
