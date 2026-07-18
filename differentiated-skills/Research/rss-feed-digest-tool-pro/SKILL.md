---
slug: rss-feed-digest-tool-pro
name: rss-feed-digest-tool-pro
version: "1.0.0"
displayName: RSS聚合摘要专业版
summary: 企业级RSS/Atom聚合摘要系统,支持定时调度、HTML报告、邮件分发、多模板定制与团队协作
license: MIT
edition: pro
description: |-
  RSS聚合摘要专业版为企业团队提供高阶RSS/Atom订阅聚合与分发能力。

  核心能力:
  - 大规模多源并行抓取(50+源)
  - 定时调度与自动化任务管理
  - 交互式HTML报告生成
  - 多渠道分发(邮件/IM/Webhook)
  - 自定义摘要模板与品牌定制
  - 高级过滤引擎(正则/情感/语言)

  适用场景:
  - 企业竞争情报自动化监控
  - 行业研究报告定时生成
  - 团队每日资讯邮件推送
  - 多语言内容聚合分发

  差异化:专业版在免费版核心聚合流程基础上,扩展大规模并行抓取、定时调度、HTML报告、多渠道分发与模板定制能力。与免费版完全兼容,命令行参数与订阅列表文件可直接复用。

  触发关键词: RSS, Atom, 聚合, 摘要, digest, 企业, 批量, 调度, HTML, 邮件, 分发, 定时, 竞争情报
tags:
- 研究工具
- RSS
- 企业级
- 信息聚合
- 竞争情报
- 自动化
tools:
- read
- exec
---

# RSS聚合摘要专业版

## 概述

RSS聚合摘要专业版是企业级RSS/Atom订阅聚合与分发系统。在免费版多源抓取、关键词过滤、Markdown输出的基础上,专业版扩展了大规模并行抓取、定时调度引擎、交互式HTML报告、多渠道分发、自定义模板与高级过滤等企业级能力。

专业版与免费版完全兼容:免费版的命令行参数、订阅列表文件、关键词配置均可直接被专业版使用,无需修改。升级后即可享受批量调度与企业级分发功能。

## 核心能力

### 免费版 vs 专业版能力对比

| 能力模块 | 免费版 | 专业版 |
|:--------|:------|:-------|
| 多源抓取 | 支持(建议≤5源) | 支持(50+源并行) |
| 关键词过滤 | 包含/排除 | 包含/排除+正则+情感+语言 |
| 跨源去重 | URL哈希去重 | URL+标题+内容多级去重 |
| 时间筛选 | 按小时 | 按小时+自定义时间区间 |
| Markdown输出 | 支持 | 支持 |
| 纯文本输出 | 支持 | 支持 |
| HTML报告 | 不支持 | 交互式HTML(筛选/搜索/排序) |
| 定时调度 | 不支持(需手动crontab) | 内置Cron调度引擎 |
| 邮件分发 | 不支持 | SMTP邮件自动发送 |
| IM分发 | 不支持 | Webhook推送至企业IM |
| 模板定制 | 固定格式 | YAML模板引擎+品牌定制 |
| 认证源抓取 | 不支持 | Basic Auth/OAuth/API Key |
| 多语言 | 中文/英文 | 15+语言自动检测与翻译 |
| 批量操作 | 不支持 | 批量源管理+配置导入导出 |

### 专业版独有功能

1. **大规模并行抓取**:支持50+订阅源并发抓取,连接池复用,单次抓取耗时从分钟级降至秒级
2. **定时调度引擎**:内置Cron调度,支持时区配置、失败重试、任务依赖链
3. **交互式HTML报告**:生成带筛选、搜索、排序功能的静态HTML页面,可直接浏览器打开
4. **多渠道分发**:摘要自动推送至邮件、企业IM(Webhook)、文件系统、对象存储
5. **模板引擎**:YAML定义摘要结构,支持品牌头尾、自定义字段、多格式输出
6. **高级过滤**:正则表达式、情感分析、语言检测、热度评分多维过滤
7. **认证源管理**:安全存储并管理需要认证的私有RSS源的凭证

## 使用场景

### 场景一:企业竞争情报自动化

市场团队需要每日监控30+行业媒体与竞品博客,生成结构化竞争情报简报并自动邮件分发。

```bash
# 批量抓取30+源,高级过滤,生成HTML报告并发送邮件
python3 scripts/rss_digest_pro.py fetch \
  --feed-file enterprise-feeds.txt \
  --hours 24 \
  --limit 50 \
  --filter-regex "(发布|融资|收购|定价|裁员|launch|funding)" \
  --exclude-regex "(招聘|广告|sponsor)" \
  --sentiment analyze \
  --output-html /reports/daily-competitive.html \
  --output-md /reports/daily-competitive.md \
  --template competitive-intel \
  --distribute "email:market-team@corp.com" \
  --brand "企业竞争情报简报"
```

生成的HTML报告包含:

- 日期/分类/热度多维度筛选器
- 实时关键词搜索框
- 按情感倾向(正面/负面/中性)分类展示
- 每条目含标题、来源、时间、摘要、情感标签、热度评分
- 底部统计图表(来源分布、情感比例、关键词词云)

### 场景二:多语言行业研究

研究团队需要聚合中英日三语行业媒体,自动检测语言并生成双语对照摘要。

```bash
# 多语言抓取与翻译
python3 scripts/rss_digest_pro.py fetch \
  --feed-file multilingual-feeds.txt \
  --hours 168 \
  --language-detect \
  --translate-to zh \
  --output /reports/weekly-multilingual.md \
  --template bilingual-report
```

### 场景三:定时调度与任务链

内容运营团队需要配置复杂的定时任务:每日抓取->过滤->生成报告->分发->归档。

```bash
# 配置定时调度任务
python3 scripts/rss_digest_pro.py schedule add \
  --name "每日行业简报" \
  --cron "0 8 * * *" \
  --timezone "Asia/Shanghai" \
  --feed-file industry-feeds.txt \
  --hours 24 \
  --template daily-brief \
  --output-html /reports/daily/ \
  --distribute "email:team@corp.com,webhook:https://im.example.com/hook"

# 配置周度任务(依赖每日任务归档)
python3 scripts/rss_digest_pro.py schedule add \
  --name "周度趋势回顾" \
  --cron "0 9 * * 1" \
  --timezone "Asia/Shanghai" \
  --aggregate-weekly /reports/daily/ \
  --output /reports/weekly/week-$(date +%YW%V).md \
  --template weekly-trend \
  --distribute "email:c-level@corp.com"

# 查看所有调度任务
python3 scripts/rss_digest_pro.py schedule list

# 查看任务执行历史
python3 scripts/rss_digest_pro.py schedule logs "每日行业简报" --last 7
```

## 快速开始

### 从免费版升级

专业版完全兼容免费版命令,升级步骤:

```bash
# 1. 安装专业版依赖
pip3 install feedparser httpx jinja2 pyyaml

# 2. 验证免费版配置可用
python3 scripts/rss_digest_pro.py fetch \
  --feed-file my-feeds.txt \
  --hours 24 \
  --output test-upgrade.md
# 输出与免费版一致,确认兼容

# 3. 开始使用专业版功能
python3 scripts/rss_digest_pro.py fetch \
  --feed-file my-feeds.txt \
  --hours 24 \
  --output-html daily-report.html \
  --template branded-brief
```

### 首次配置定时任务

```bash
# 创建每日摘要任务
python3 scripts/rss_digest_pro.py schedule add \
  --name "每日技术简报" \
  --cron "0 8 * * *" \
  --feed-file tech-feeds.txt \
  --hours 24 \
  --template daily-brief \
  --distribute "email:dev-team@corp.com"

# 手动触发测试运行
python3 scripts/rss_digest_pro.py schedule run "每日技术简报"

# 查看运行结果
python3 scripts/rss_digest_pro.py schedule logs "每日技术简报"
```

### 配置邮件分发

```yaml
# config/distribute.yaml
email:
  smtp_host: smtp.corp.com
  smtp_port: 587
  smtp_user: digest-bot@corp.com
  smtp_password: "${SMTP_PASSWORD}"  # 从环境变量读取
  from: "RSS摘要机器人 <digest-bot@corp.com>"
  default_to:
    - team@corp.com

webhook:
  im_platform:
    url: https://im.example.com/webhook/xxx
    format: card
    secret: "${WEBHOOK_SECRET}"
```

## 配置示例

### 自定义摘要模板

```yaml
# templates/competitive-intel.yaml
name: competitive-intel
displayName: 竞争情报简报
brand:
  header: |
    # {{brand_name}} | {{date}}
    > 自动生成,仅供内部参考
  footer: |
    ---
    由RSS聚合摘要专业版自动生成 | 配置: {{config_version}}
sections:
  - name: 高优先级动态
    filter:
      min_score: 0.8
      keywords: ["融资", "收购", "发布", "裁员"]
    format: detailed
    limit: 10
    fields: [title, source, time, summary, sentiment, score, suggestion]
  - name: 行业资讯
    filter:
      min_score: 0.5
    format: brief
    limit: 20
    fields: [title, source, time, summary]
  - name: 趋势信号
    filter:
      type: trend
    format: signal
    limit: 5
    fields: [keyword, count, trend_direction]
output:
  formats: [markdown, html]
  html_theme: corporate-dark
  include_charts: true
```

### 大规模订阅源管理

```bash
# 批量导入OPML
python3 scripts/rss_digest_pro.py sources import industry.opml --group "行业媒体"

# 批量健康检查
python3 scripts/rss_digest_pro.py sources health-check --all --timeout 10

# 导出当前源列表
python3 scripts/rss_digest_pro.py sources export --format opml --output backup.opml

# 按组管理
python3 scripts/rss_digest_pro.py sources list --group "行业媒体" --healthy-only
```

### 高级过滤配置

```bash
# 正则+情感+语言组合过滤
python3 scripts/rss_digest_pro.py fetch \
  --feed-file global-feeds.txt \
  --hours 24 \
  --filter-regex "(AI|LLM|GPT|大模型).*(发布|更新|评测)" \
  --exclude-regex "(招聘|广告|sponsor|casino)" \
  --sentiment analyze \
  --min-sentiment-score 0.3 \
  --language-detect \
  --languages zh,en \
  --min-score 0.6 \
  --output filtered-digest.md
```

## 最佳实践

### 1. 按业务线拆分订阅源组

不要将所有源混在一个文件中。按业务线创建独立订阅列表(如`tech-feeds.txt`、`market-feeds.txt`、`competitor-feeds.txt`),各自配置调度任务和分发渠道。

### 2. 利用HTML报告提升可读性

HTML报告支持交互式筛选与搜索,比Markdown更适合分发给非技术成员。专业版支持一键同时生成Markdown和HTML:

```bash
--output-md report.md --output-html report.html
```

### 3. 设置任务失败告警

调度任务可能因网络问题或源失效而失败。配置失败告警,确保运维及时介入:

```bash
python3 scripts/rss_digest_pro.py schedule update "每日行业简报" \
  --retry 3 \
  --retry-backoff exponential \
  --alert-on-failure "email:ops@corp.com"
```

### 4. 定期清理失效源

大规模订阅源中,部分源会随时间失效。运行定期健康检查,移除失效源,保持抓取效率:

```bash
# 每周日凌晨健康检查
python3 scripts/rss_digest_pro.py schedule add \
  --name "源健康检查" \
  --cron "0 2 * * 0" \
  --action health-check \
  --alert "email:ops@corp.com"
```

### 5. 利用模板引擎实现多角色分发

不同角色关注不同粒度。为管理层配置精简模板,为执行层配置详尽模板,通过同一数据源生成不同报告:

```bash
# 同一批次生成两种报告
python3 scripts/rss_digest_pro.py fetch \
  --feed-file industry-feeds.txt \
  --hours 24 \
  --template executive-brief \
  --distribute "email:c-level@corp.com"

python3 scripts/rss_digest_pro.py fetch \
  --feed-file industry-feeds.txt \
  --hours 24 \
  --template detailed-report \
  --distribute "email:team@corp.com"
```

## 常见问题

### Q: 如何从免费版迁移到专业版?

A: 专业版完全兼容免费版。安装专业版依赖后,免费版的`--feeds`、`--feed-file`、`--keywords`、`--hours`、`--limit`、`--output`、`--format`参数全部继续可用。原有订阅列表文件无需修改,直接使用专业版脚本即可。

### Q: 大规模抓取(50+源)时性能如何?

A: 专业版使用`httpx`异步连接池,50+源并行抓取通常在10-15秒内完成(取决于网络与源响应速度)。连接池大小可配置(`--workers 50`),默认并发数为20。单源超时默认30秒,可通过`--timeout`调整。

### Q: HTML报告可以在内网环境使用吗?

A: 可以。HTML报告是完全自包含的静态文件,所有CSS/JS内联,无外部CDN依赖。生成后可直接在任意浏览器打开,也适合内网分发或归档至对象存储。

### Q: 邮件分发支持附件吗?

A: 支持。摘要Markdown/HTML作为邮件正文发送,同时可将完整HTML报告作为附件。配置示例:`--distribute "email:team@corp.com" --attach-html report.html`。

### Q: 情感分析的准确率如何?

A: 专业版内置基于词典的情感分析,对中英文准确率约75-85%。如需更高准确率,可接入外部NLP API(如LLM API),通过`--sentiment-engine llm`配置。情感分析结果用于分类展示与过滤,不作为唯一决策依据。

### Q: 定时调度任务如何查看执行历史?

A: 运行`schedule logs <task-name>`查看任务执行历史,包含每次运行的时间、耗时、抓取条目数、分发状态。日志默认保留30天,可通过`--log-retention`调整。

### Q: 多语言翻译使用什么引擎?

A: 专业版默认使用Agent内置LLM进行翻译,无需额外API。如需更高翻译质量,可配置外部翻译API(如DeepL、Google Translate),通过`config/translate.yaml`设置。

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
| feedparser | Python库 | 必需 | `pip3 install feedparser` |
| httpx | HTTP客户端 | 必需 | `pip3 install httpx` |
| jinja2 | 模板引擎 | 必需 | `pip3 install jinja2` |
| pyyaml | 配置解析 | 必需 | `pip3 install pyyaml` |
| SMTP服务 | 邮件服务 | 条件必需(邮件分发时) | 企业SMTP服务器 |
| Webhook端点 | IM集成 | 条件必需(IM分发时) | 企业IM平台Webhook URL |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置

- **SMTP凭证**: 通过环境变量`SMTP_PASSWORD`配置,或写入`config/distribute.yaml`
- **Webhook密钥**: 通过环境变量`WEBHOOK_SECRET`配置
- **翻译API Key**: 条件必需,使用外部翻译引擎时配置于`config/translate.yaml`
- **LLM API**: 由Agent平台内置提供,用于情感分析与翻译,无需额外配置

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行Python脚本)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent调用Python脚本完成企业级RSS聚合摘要与分发任务。专业版在免费版基础上扩展大规模并行抓取、定时调度、HTML报告、多渠道分发与模板定制能力,适合企业竞争情报自动化、行业研究定时生成与多角色内容分发场景。
