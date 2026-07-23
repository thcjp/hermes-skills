---
slug: scrape-web-tool-pro
name: scrape-web-tool-pro
version: 1.0.0
displayName: 网页抓取工具专业版
summary: 企业级网页抓取系统,支持批量抓取、JS渲染、分页遍历、结构化输出、代理池与认证注入
license: Proprietary
edition: pro
description: '网页抓取工具专业版为企业团队提供高阶网页内容抓取与数据提取能力。核心能力:

  - 批量URL并发抓取

  - JavaScript动态渲染支持

  - 自动分页遍历

  - 结构化输出(JSON/CSV/Excel)

  - 代理池与请求头定制

  - 认证页面抓取(Cookie/Header注入)


  适用场景:

  - 竞品数据批量采集

  - 电商价格监控

  - 行业目录全量抓取

  - 需登录的内部系统数据提取


  差异化:专业版在免费版单页抓取与CSS选择器基础上,扩展批量抓取、JS渲染、分页遍历、结构化输出、代理池与认证能力'
tags:
- 研究工具
- 网页抓取
- 企业级
- 数据采集
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# 网页抓取工具专业版

## 概述

网页抓取工具专业版是企业级网页内容抓取与数据提取系统。在免费版单页抓取、CSS选择器提取、文件保存的基础上,专业版扩展了批量URL并发抓取、JavaScript动态渲染、自动分页遍历、结构化输出(JSON/CSV/Excel)、代理池轮换、请求头定制与认证页面抓取等企业级能力。

专业版与免费版完全兼容:免费版的`--url`、`--selector`、`--out`参数全部继续可用,原有命令无需修改。升级后即可享受批量抓取与企业级数据提取功能。

## 核心能力

### 免费版 vs 专业版能力对比

| 能力模块 | 免费版 | 专业版 |
|:--------|:------|:-------|
| 纯文本抓取 | 支持 | 支持 |
| CSS选择器 | 支持 | 支持(多选择器) |
| 文件保存 | 支持 | 支持(多格式) |
| 批量抓取 | 不支持 | 50+ URL并发 |
| JS渲染 | 不支持 | 支持(等待动态加载) |
| 分页遍历 | 不支持 | 自动翻页 |
| 结构化输出 | 不支持 | JSON/CSV/Excel |
| 代理支持 | 不支持 | 代理池轮换 |
| 请求头定制 | 不支持 | 完全自定义 |
| 认证抓取 | 不支持 | Cookie/Header注入 |
| 定时调度 | 不支持 | 内置Cron |
| 去重 | 不支持 | URL+内容指纹 |
| 数据清洗 | 不支持 | 自动清洗与规范化 |

**输入**: 用户提供免费版 vs 专业版能力对比所需的指令和必要参数。
**处理**: 按照skill规范执行免费版 vs 专业版能力对比操作,遵循单一意图原则。
**输出**: 返回免费版 vs 专业版能力对比的执行结果,包含操作状态和输出数据。

### 专业版独有功能

1. **批量并发抓取**:支持50+ URL并发抓取,连接池复用,自动重试与错误隔离
2. **JavaScript渲染**:等待JS动态加载完成后再抓取,支持SPA页面
3. **自动分页遍历**:配置分页规则后自动翻页,抓取全部数据
4. **结构化输出**:抓取结果输出为JSON/CSV/Excel,便于二次分析
5. **代理池轮换**:配置代理池,自动轮换IP,避免反爬封锁
6. **请求头定制**:完全自定义User-Agent、Cookie、Referer等请求头
7. **认证页面抓取**:注入Cookie或Authorization Header,抓取需登录页面
8. **数据清洗**:自动去除空白、HTML实体、广告内容,规范化输出

**输入**: 用户提供专业版独有功能所需的指令和必要参数。
**处理**: 按照skill规范执行专业版独有功能操作,遵循单一意图原则。
**输出**: 返回专业版独有功能的执行结果,包含操作状态和输出数据。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级网页抓取系、支持批量抓取、代理池与认证注入、网页抓取工具专业、版为企业团队提供、高阶网页内容抓取、与数据提取能力、核心能力、动态渲染支持、代理池与请求头定等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一:竞品数据批量采集

市场团队需要批量抓取多个竞品官网的产品页面,提取产品名称、价格、功能列表,生成对比表。

```bash
# 批量抓取竞品页面,结构化输出
python （请参考skill目录中的脚本文件） batch \
  --urls-file competitors-urls.txt \
  --selectors "name:h1.product-title::text" \
              "price:span.price::text" \
              "features:ul.features li::text" \
  --format json \
  --output /reports/competitor-data.json \
  --workers 20 \
  --clean

# 导出为CSV
python （请参考skill目录中的脚本文件） batch \
  --urls-file competitors-urls.txt \
  --selectors "name:h1.product-title::text" "price:span.price::text" \
  --format csv \
  --output /reports/competitor-pricing.csv
```

URL列表文件格式:

```text
# competitors-urls.txt
https://competitor-a.com/products
https://competitor-b.com/pricing
https://competitor-c.com/features
```

输出JSON示例:

```json
[
  {
    "url": "https://competitor-a.com/products",
    "name": "AI Assistant Pro",
    "price": "$49/月",
    "features": ["GPT-5支持", "128K上下文", "私有化部署", "SSO集成"],
    "fetched_at": "2026-07-18T10:30:00"
  },
  {
    "url": "https://competitor-b.com/pricing",
    "name": "ChatBot Enterprise",
    "price": "$99/月",
    "features": ["多模型支持", "API接入", "团队协作"],
    "fetched_at": "2026-07-18T10:30:01"
  }
]
```

### 场景二:电商价格动态监控

电商运营团队需要每日抓取竞品电商平台的价格,监控价格变动。

```bash
# 配置抓取规则(支持JS渲染)
python （请参考skill目录中的脚本文件） scrape \
  --url "https://ecommerce-site.com/product/123" \
  --selector "span.price::text" \
  --render-js \
  --wait-for "span.price" \
  --wait-time 3000 \
  --output /reports/price-snapshots/$(date +%Y%m%d)-product-123.json

# 定时调度(每日3次)
python （请参考skill目录中的脚本文件） schedule add \
  --name "价格监控" \
  --cron "0 9,13,18 * * *" \
  --urls-file price-watch-urls.txt \
  --selectors "name:h1::text" "price:span.price::text" "stock:div.availability::text" \
  --render-js \
  --output /reports/price-watch/ \
  --format json
```

### 场景三:需登录的内部系统数据提取

企业需要从需登录的内部系统中批量提取数据。

```bash
# 注入Cookie抓取认证页面
python （请参考skill目录中的脚本文件） scrape \
  --url "https://internal-system.com/dashboard" \
  --selector "table.data tr::text" \
  --header "Cookie: session_id=abc123; auth_token=xyz789" \
  --header "Authorization: Bearer eyJhb..." \
  --output /reports/internal-data.csv

# 批量抓取多个认证页面
python （请参考skill目录中的脚本文件） batch \
  --urls-file internal-urls.txt \
  --selectors "title:h2::text" "data:table.results td::text" \
  --header "Cookie: session_id=abc123" \
  --format csv \
  --output /reports/internal-batch.csv \
  --workers 10
```

## 不适用场景

以下场景网页抓取工具专业版不适合处理：

- 加密文件破解
- 损坏文件修复
- 物理介质数据恢复

## 触发条件

需要文件处理、文档转换、格式互转、内容提取时使用。不适用于非本工具能力范围的需求。

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
pip install "scrapling[all]" httpx openpyxl

# 2. 验证免费版命令可用
python （请参考skill目录中的脚本文件） --url "https://example.com"
# 输出与免费版一致,确认兼容

# 3. 使用专业版功能
python （请参考skill目录中的脚本文件） scrape \
  --url "https://example.com" \
  --render-js \
  --selector "div.content::text" \
  --format json
```

### 首次批量抓取

```bash
# 准备URL列表文件
cat > urls.txt << 'EOF'
https://example.com/page1
https://example.com/page2
https://example.com/page3
EOF

# 批量抓取
python （请参考skill目录中的脚本文件） batch \
  --urls-file urls.txt \
  --selector "h1::text" \
  --format json \
  --output results.json \
  --workers 10
```

### 配置JS渲染抓取

```bash
# 抓取SPA页面(等待JS加载)
python （请参考skill目录中的脚本文件） scrape \
  --url "https://spa-app.com/dashboard" \
  --render-js \
  --wait-for "div.dashboard-content" \
  --wait-time 5000 \
  --selector "div.dashboard-content::text"
```

### 配置代理池

```yaml
# config/proxies.yaml
proxies:
  - url: "http://proxy1.example.com:8080"
    username: "user1"
    password: "${PROXY1_PASSWORD}"
  - url: "http://proxy2.example.com:8080"
    username: "user2"
    password: "${PROXY2_PASSWORD}"
  - url: "socks5://proxy3.example.com:1080"

rotation:
  strategy: round-robin  # 轮换策略: round-robin / random / least-used
  retry_on_fail: true
  max_retries: 3
```

```bash
# 使用代理池抓取
python （请参考skill目录中的脚本文件） batch \
  --urls-file urls.txt \
  --selector "div.content::text" \
  --proxy-pool config/proxies.yaml \
  --workers 20
```

## 示例

### 批量抓取配置

```bash
# 基本批量抓取
python （请参考skill目录中的脚本文件） batch \
  --urls-file urls.txt \
  --selector "h1::text" \
  --format json \
  --output results.json

# 多选择器结构化抓取
python （请参考skill目录中的脚本文件） batch \
  --urls-file urls.txt \
  --selectors "title:h1::text" "price:span.price::text" "desc:div.description::text" \
  --format csv \
  --output products.csv \
  --workers 20 \
  --clean

# 带JS渲染的批量抓取
python （请参考skill目录中的脚本文件） batch \
  --urls-file urls.txt \
  --selectors "title:h1::text" "data:div.dynamic-data::text" \
  --render-js \
  --wait-for "div.dynamic-data" \
  --format json \
  --output rendered-data.json \
  --workers 5
```

### 分页遍历配置

```bash
# 自动分页抓取
python （请参考skill目录中的脚本文件） paginate \
  --url "https://example.com/list?page=1" \
  --next-page "a.next-page::attr(href)" \
  --max-pages 20 \
  --selector "div.item h3::text" \
  --format json \
  --output all-items.json
```

### 定时调度配置

```yaml
# config/schedules.yaml
schedules:
  - name: "每日竞品价格监控"
    cron: "0 9,13,18 * * *"
    timezone: "Asia/Shanghai"
    action: batch
    params:
      urls_file: config/competitor-urls.txt
      selectors:
        name: "h1.product-title::text"
        price: "span.price::text"
      format: json
      output: /reports/price-watch/
      render_js: true
      workers: 10

  - name: "周度全量数据抓取"
    cron: "0 2 * * 1"
    action: batch
    params:
      urls_file: config/all-urls.txt
      selectors:
        title: "h1::text"
        content: "div.content::text"
      format: csv
      output: /reports/weekly-scrape.csv
      workers: 30
```

### 数据清洗规则

```yaml
# config/clean_rules.yaml
clean:
  trim_whitespace: true          # 去除首尾空白
  collapse_spaces: true           # 合并多余空格
  remove_html_entities: true      # 解码HTML实体
  remove_ads: true                # 去除广告内容
  remove_navigation: true         # 去除导航文本
  normalize_encoding: utf-8       # 统一编码
  date_format: "%Y-%m-%d"        # 日期格式化
  price_normalize: true           # 价格格式化(去除货币符号)
```

## 最佳实践

### 1. 合理设置并发数

`--workers`参数控制并发抓取数。建议:(1)普通网站设10-20;(2)有反爬机制的网站设5-10;(3)使用代理池可设20-50。过高并发可能触发反爬封锁或本地资源耗尽。

### 2. JS渲染抓取要设置等待

JS渲染抓取需要等待动态内容加载。使用`--wait-for`指定等待元素,`--wait-time`设置最大等待时间。不设等待可能导致抓取到加载前的空页面。

### 3. 代理池配置要多样化

代理池中的IP应来自不同地域和运营商,避免单一IP段被封锁。轮换策略推荐`round-robin`(均匀分配),配合`retry_on_fail`自动切换失败代理。

### 4. 结构化输出便于二次分析

批量抓取优先使用JSON或CSV格式输出,便于在Excel、数据库或分析工具中二次处理。多选择器抓取时,每个选择器对应一个字段,形成结构化表格。

### 5. 遵守抓取礼仪

控制抓取频率(并发数与间隔),遵守`robots.txt`规则,不在高峰时段大规模抓取。专业版支持`--delay`参数设置请求间隔:

```bash
python （请参考skill目录中的脚本文件） batch --urls-file urls.txt --delay 2 --workers 5
```

## 常见问题

### Q: 如何从免费版迁移到专业版?

A: 专业版完全兼容免费版。安装专业版依赖后,免费版的`--url`、`--selector`、`--out`参数全部继续可用。直接使用专业版脚本即可享受批量抓取与JS渲染等高级功能,原有命令无需修改。

### Q: JS渲染抓取很慢怎么办?

A: JS渲染需要启动浏览器引擎加载页面,天然比纯HTML抓取慢。优化方法:(1)设置合理的`--wait-time`(3000-5000ms通常足够);(2)使用`--wait-for`精确等待目标元素而非超时;(3)降低JS渲染抓取的并发数(--workers 5);(4)非必要不启用JS渲染,先测试纯HTML抓取是否够用。

### Q: 批量抓取时部分URL失败怎么办?

A: 专业版自动重试失败URL(默认3次)。抓取结束后查看日志确认失败URL,可单独重试:`python （请参考skill目录中的脚本文件） batch --urls-file failed-urls.txt --retry 5`。持续失败的URL可能是目标页面不可访问或反爬封锁。

### Q: 代理池中的代理失效怎么办?

A: 专业版代理池支持自动健康检查。配置`retry_on_fail: true`后,失败代理会被临时移出轮换队列。建议定期运行代理健康检查更新代理列表,移除永久失效的代理。

### Q: 认证抓取的Cookie如何获取?

A: 在浏览器中登录目标系统,打开开发者工具(F12)->Network->任一请求->Headers,复制Cookie值。将Cookie注入请求头:`--header "Cookie: session_id=xxx; auth_token=yyy"`。注意Cookie有有效期,过期后需重新获取。

### Q: 分页抓取如何判断是否到最后一页?

A: 专业版通过`--next-page`选择器判断。如果该选择器未命中任何元素(没有"下一页"链接),则认为已到最后一页,停止遍历。也可通过`--max-pages`强制限制最大翻页数,避免无限翻页。

### Q: 结构化输出的CSV包含特殊字符导致格式错乱怎么办?

A: 专业版CSV输出遵循RFC 4180标准,自动处理逗号、引号、换行等特殊字符(用双引号包裹)。如仍有问题,尝试使用JSON格式输出,再通过脚本转换为CSV。

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
| Scrapling | Python库 | 必需 | `pip install "scrapling[all]"` |
| httpx | HTTP客户端 | 必需 | `pip install httpx` |
| openpyxl | Excel导出 | 条件必需(Excel输出) | `pip install openpyxl` |
| pyyaml | 配置解析 | 必需 | `pip install pyyaml` |
| 浏览器引擎 | 系统组件 | 条件必需(JS渲染) | `scrapling install` |
| 代理服务 | 网络 | 条件必需(代理抓取) | 代理服务提供商 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 网络访问 | 网络 | 必需 | 需能访问目标网页URL |

### API Key 配置

- **代理认证**: 代理池用户名密码通过环境变量配置,参考`config/proxies.yaml`
- **认证Cookie/Header**: 通过命令行`--header`参数注入,敏感凭证建议使用环境变量
- **LLM API**: 由Agent平台内置提供,无需额外配置
- 无外部付费API强制依赖(代理服务费用取决于代理提供商)

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行Python脚本)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent调用Python脚本完成企业级网页抓取与数据提取任务。专业版在免费版基础上扩展批量抓取、JS渲染、分页遍历、结构化输出、代理池与认证能力,适合竞品数据批量采集、电商价格监控与需登录系统数据提取场景。

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
