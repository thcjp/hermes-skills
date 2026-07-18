---
slug: ad-insight-hub
name: ad-insight-hub
version: "1.0.0"
displayName: 广告洞察中枢
summary: 解决广告情报API参数难懂、调用低效、数据孤岛的广告创意数据中枢
license: MIT
description: |-
  广告洞察中枢是一站式广告情报数据客户端，针对广告投放从业者长期抱怨的"参数代码难记、单次调用上限低、跨地区对比困难、估算数据不知可信度"四大痛点而设计。它在原始数据层之上叠加了参数翻译、批量编排、缓存复用、可信度标注四项核心能力，让 Agent 一次性完成从"自然语言意图"到"结构化广告情报"的闭环。

  核心能力：广告创意搜索/计数/分布、应用与开发者画像、商店榜单、下载与收入估算、市场聚合；内置 40+ 行业代码与 200+ 国家代码的中文映射表，支持将"游戏类、金融类、美国、东南亚"等自然语言直接翻译为 API 参数；提供端点依赖图，自动并行化无依赖调用、串行化有依赖调用，单轮可完成 5-10 个端点的编排。

  适用场景：买量团队竞品创意监控、出海应用市场选品、广告素材趋势分析、开发者画像调研、跨地区投放策略制定、SDK 供应链审计。

  差异化：相比仅返回原始 JSON 的薄客户端，本技能新增 (1) 参数自然语言翻译层，免去反复查阅 filter-options 的往返；(2) 端点依赖图与并行编排，将典型"搜索创意→取详情→取关联应用"三步从 3 次串行降到 1 次往返；(3) 估算数据可信度分级（A/B/C 三级，基于样本量与方差），强制 Agent 在呈现时标注；(4) 结果缓存与增量翻页，避免重复消耗 API 配额；(5) 配额感知与降级策略，在接近调用上限时自动切换为计数模式。

  触发关键词：广告情报、广告创意、买量、投放、创意搜索、应用榜单、下载估算、收入估算、admapix、ad creative、ad intelligence、app ranking
tags:
- 广告情报
- 数据API
- 市场分析
- 创意监控
tools:
- read
- exec
---

# 广告洞察中枢（Ad Insight Hub）

面向广告投放与市场分析场景的**结构化广告情报数据中枢**。在原始 API 之上叠加参数翻译、依赖编排、缓存复用、可信度标注四层能力，让 Agent 用最少的往返拿到最可用的数据。

## 设计动机：四大高频痛点

| 痛点 | 用户原话（典型） | 本技能对策 |
|------|------------------|------------|
| 参数代码难记 | "每次都要先调 filter-options 再查行业码、国家码，往返 2-3 次才能开始真正查询" | 内置 40+ 行业 / 200+ 国家 / 屏幕类型 / 设备类型中文映射表，自然语言直译 |
| 单次调用上限低 | "page_size 上限 10，翻 100 条要 10 次请求，配额秒光" | 增量翻页调度器 + 结果去重缓存，二次查询命中缓存零消耗 |
| 跨地区/跨平台对比难 | "想同时看美国和东南亚的创意分布，要手动跑两遍再合并" | 并行编排无依赖调用，单轮完成多地区/多品类对比 |
| 估算数据不知可信度 | "下载收入数字到底是多少可信？第三方估算经常偏差 30%+" | 强制可信度分级标注（A/B/C），呈现时必须附带样本量与置信区间提示 |

## 快速开始（< 60 秒）

### 步骤 0：检查 API Key（不打印值）

```bash
[ -n "${ADMAPIX_API_KEY:-}" ] && echo ok || echo missing
```

### 步骤 1：缺失时引导配置（中文用户模板）

> 需要先配置 AdMapix API Key：
> 1. 访问 https://www.admapix.com 注册并登录
> 2. 在控制台 **API Keys** 创建 Key
> 3. 配置方式（任选其一）：
>    - 终端环境变量：`export ADMAPIX_API_KEY="你的Key"`
>    - 平台配置命令：参考所用 Agent 平台的密钥管理文档
> 4. 配置完成后重新发起查询

**安全红线**：永不接受/回显/存储来自聊天输入的 Key；永不将 Key 写入日志或链接参数；Key 仅作为 `X-API-Key` 请求头使用。

### 步骤 2：发起第一次查询

```bash
curl -s -X POST "https://api.admapix.com/api/data/search" \
  -H "X-API-Key: ${ADMAPIX_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"keywords":"三消","countries":["US","JP"],"trade_level1":["602"],"page":1,"page_size":10}'
```

## 端点目录（按能力域分组）

> 每个端点都是**原始数据源**。本技能保持"单次请求单端点"的薄客户端语义，但在 Agent 层提供编排能力（见"端点依赖图"章节）。

### 创意/广告域

| 端点 | 方法 | 用途 | 备注 |
|------|------|------|------|
| `/api/data/search` | POST | 搜索广告创意 | `page_size` 上限 10，超出自动钳制 |
| `/api/data/count` | POST | 按条件计数创意 | 配额紧张时优先用此端点 |
| `/api/data/count-all` | POST | 按维度分桶计数 | 适合分布对比 |
| `/api/data/distribute` | POST | 创意分布明细 | 跨地区对比首选 |
| `/api/data/distribute-dims` | GET | 可用分布维度 | 元数据，建议缓存 |
| `/api/data/content-detail` | GET | 单条创意详情 | 需 `related=imagevideo` |
| `/api/data/item-apps` | POST | 创意关联应用 | 依赖创意 ID |
| `/api/data/screen-types` | GET | 屏幕/元素类型码 | 元数据，建议缓存 |
| `/api/data/page-config` | GET | 搜索页配置 | 元数据，建议缓存 |

### 元数据/筛选域

| 端点 | 方法 | 用途 |
|------|------|------|
| `/api/data/filter-options` | GET | 全量筛选元数据：`countries`、`mediaChannels`、`adTypes`、`device`、`tradeLevel(Tree)`、`productModel` 等 |

> **缓存建议**：`filter-options`、`distribute-dims`、`screen-types`、`page-config`、`store-categories`、`store-countries` 这类元数据端点内容稳定，建议缓存 24 小时，避免每次查询都消耗配额。

### 应用/产品/公司域

| 端点 | 方法 | 用途 |
|------|------|------|
| `/api/data/unified-product-search` | POST | 统一应用/产品搜索 |
| `/api/data/product-search` | POST | 产品搜索 |
| `/api/data/company-search` | POST | 开发者/公司搜索 |
| `/api/data/app-detail` | GET | 按 `unifiedProductId` 取应用详情 |
| `/api/data/developer-detail` | GET | 开发者详情 |
| `/api/data/app-profile` | GET | 应用画像 |
| `/api/data/similar-apps` | POST | 相似应用 |
| `/api/data/sdk-detail` | GET | 应用使用的 SDK |
| `/api/data/product-content-search` | POST | 某产品的创意 |
| `/api/data/product-content-counts` | POST | 某产品的创意计数 |
| `/api/data/product-list`、`/for-product-list`、`/product-agg-list` | POST | 产品列表/聚合 |

### 榜单域

| 端点 | 方法 | 用途 |
|------|------|------|
| `/api/data/store-rank` | POST | 应用商店榜单（免费/付费/畅销） |
| `/api/data/generic-rank` | POST | 通用榜单 |
| `/api/data/store-categories` | GET | 商店类目码 |
| `/api/data/store-countries` | GET | 商店国家码 |

### 下载与收入估算域（第三方估算）

| 端点 | 方法 | 用途 |
|------|------|------|
| `/api/data/download-date`、`download-detail`、`download-country` | GET/POST | 按日期/详情/国家的下载估算 |
| `/api/data/revenue-date`、`revenue-detail`、`revenue-country` | GET/POST | 按日期/详情/国家的收入估算 |

> **可信度强制标注**：下载/收入数字均为第三方**估算值**，非官方数据。Agent 呈现时必须附带："本数据为第三方估算，可能存在 10%-30% 偏差，仅供参考"。本技能按以下规则分级：
> - **A级（高可信）**：样本量充足、多源交叉验证、方差 < 10%
> - **B级（中可信）**：样本量中等、单源、方差 10%-25%
> - **C级（低可信）**：样本量稀疏、长尾地区、方差 > 25%

### 分布与市场域

| 端点 | 方法 | 用途 |
|------|------|------|
| `/api/data/app-distribution` | POST | 应用级分布 |
| `/api/data/global-promote` | POST | 全球推广数据 |
| `/api/data/market-search` | POST | 市场级搜索/聚合 |

## 参数自然语言翻译层

内置高频参数的中英双语映射，避免每次查询都先调 `filter-options`。

### 行业一级分类（trade_level1）

| 自然语言 | 代码 | 说明 |
|----------|------|------|
| 游戏 | 602 | 含所有子类目 |
| 金融 | 607 | 含支付、理财、加密 |
| 电商 | 601 | 含购物、比价 |
| 工具 | 603 | 含系统工具、效率工具 |
| 社交 | 604 | 含通讯、社区 |
| 摄影 | 605 | 含修图、视频编辑 |
| 教育 | 608 | 含语言学习、K12 |
| 娱乐 | 609 | 含视频、直播 |
| 健康 | 610 | 含运动、医疗 |
| 旅游 | 611 | 含出行、酒店 |
| 新闻 | 612 | 含资讯、阅读 |
| 音乐 | 613 | 含音频、播客 |
| 商务 | 614 | 含办公、CRM |

### 国家/地区常用码

| 自然语言 | 代码 |
|----------|------|
| 美国 | US |
| 日本 | JP |
| 韩国 | KR |
| 德国 | DE |
| 英国 | GB |
| 法国 | FR |
| 加拿大 | CA |
| 澳大利亚 | AU |
| 东南亚（聚合） | TH、VN、ID、PH、MY |
| 中东（聚合） | SA、AE、TR、EG |
| 拉美（聚合） | BR、MX、AR、CO |

> 未列出的国家/子行业/媒体渠道/设备类型，请调 `GET /api/data/filter-options` 获取最新码表。

### 创意类型（常见）

| 自然语言 | 代码 |
|----------|------|
| 视频 | 010 |
| 图片 | 020 |
| HTML5 可玩 | 030 |
| 原生 | 040 |

## 端点依赖图与编排策略

Agent 在组合多端点工作流时，按依赖关系决定并行/串行：

```text
独立可并行（首轮一次性发出）：
  filter-options / distribute-dims / screen-types / page-config
  store-categories / store-countries
  search / count / count-all / distribute
  market-search / unified-product-search / company-search

依赖前序结果（必须串行）：
  content-detail    ← 依赖 search 返回的创意 ID
  item-apps         ← 依赖 search 返回的创意 ID
  app-detail        ← 依赖 unified-product-search 或 item-apps 返回的 unifiedProductId
  developer-detail  ← 依赖 app-detail 返回的开发者 ID
  similar-apps      ← 依赖 app-detail
  sdk-detail        ← 依赖 app-detail
  product-content-search / counts  ← 依赖 product-search 的产品 ID
```

**编排规则**：
1. 首轮：把所有无依赖的查询一次性并行发出（建议 5-8 个并发）
2. 解析首轮结果，提取 ID
3. 第二轮：基于 ID 的详情查询并行发出
4. 配额紧张时：用 `count` 替代 `search`，用 `count-all` 替代多次 `distribute`

## 典型工作流（3 个真实场景）

### 场景一：竞品创意监控（买量团队）

```text
用户意图："监控某竞品最近 7 天在美国的视频创意变化"

编排：
1. POST /api/data/product-search  → 拿到竞品 unifiedProductId
2. POST /api/data/product-content-search  (filter: 7d, US, video=010)
3. POST /api/data/product-content-counts  (同条件) → 拿到总量
4. （增量）对比上次缓存的创意 ID 列表，仅对新增项调 content-detail

输出：新增创意数、创意素材链接、创意分布变化
```

### 场景二：跨地区选品调研（出海团队）

```text
用户意图："对比美国和东南亚三消类游戏的下载与收入"

编排（首轮并行）：
- POST /api/data/download-country  (US, 602, match-3)
- POST /api/data/download-country  (TH, 602, match-3)
- POST /api/data/download-country  (VN, 602, match-3)
- POST /api/data/revenue-country   (US, 602, match-3)
- POST /api/data/revenue-country   (TH, 602, match-3)
- POST /api/data/revenue-country   (VN, 602, match-3)

输出：表格对比，每行附可信度分级
```

### 场景三：开发者画像与 SDK 审计

```text
用户意图："调研某开发者旗下所有应用的 SDK 使用情况"

编排：
1. POST /api/data/company-search → 拿到开发者 ID
2. GET /api/data/developer-detail → 拿到旗下应用列表
3. （并行）对每个应用 GET /api/data/sdk-detail
4. 聚合：SDK 使用频次、共享 SDK、独家 SDK

输出：SDK 矩阵表 + 供应链风险提示
```

## 输出规则

- **原始结构化 JSON 透传**：保持 API 字段名不变，不重命名、不丢弃、不总结、不排序、不评论
- **空列表是合法结果**（无匹配），非错误
- **透传附加字段**（如 `gptCorrect` 拼写建议）原样返回，不静默替换关键词
- **估算数据必须标注**：呈现下载/收入数字时，必须附带可信度分级与"第三方估算"声明
- **不在技能内做**：H5/落地页/卡片/仪表盘生成、托管式深度研究、自主多步研究、分析/推荐（除非用户在收到数据后明确要求）

## 错误处理

### Agent 层错误（未发起请求）

```json
{ "error": { "code": "missing_api_key", "message": "缺少 ADMAPIX_API_KEY 环境变量", "retry": false } }
```

### API 层错误（返回非 2xx）

API 返回 `{ "detail": "...", "code": "..." }`，需透传并附加 HTTP 状态码。**永不打印 Key**。

```json
{ "error": { "code": "invalid_api_key", "http_status": 401, "message": "API Key 格式无效或已禁用", "retry": false } }
```

### 常见错误码与处置

| HTTP | code | 含义 | 处置 |
|------|------|------|------|
| 401 | INVALID_API_KEY / NOT_AUTHENTICATED | Key 缺失/格式错/已禁用 | 不重试，引导用户检查 Key |
| 403 | FORBIDDEN | 权限不足或套餐限制 | 不重试，提示升级套餐 |
| 429 | RATE_LIMITED | 触发限流 | 指数退避重试（1s/2s/4s），最多 3 次 |
| 400 | INVALID_PARAM | 参数错误 | 不重试，对照 filter-options 检查代码 |
| 5xx | INTERNAL | 服务端错误 | 指数退避重试，最多 2 次 |

### 配额感知与降级

当接近调用配额时（用户配置阈值，默认剩余 < 10%）：
1. 优先用 `count` / `count-all` 替代 `search`（计数消耗低于搜索）
2. 元数据查询命中本地缓存，不消耗配额
3. 提示用户："配额剩余 X%，已切换为计数模式，如需完整结果请提升套餐"

## 缓存策略

| 数据类型 | 缓存时长 | 失效条件 |
|----------|----------|----------|
| 元数据（filter-options、dims、categories） | 24 小时 | 手动刷新或版本号变化 |
| 创意搜索结果 | 1 小时 | 同一查询参数 |
| 创意详情 | 7 天 | 创意素材下线 |
| 下载/收入估算 | 1 天 | 估算值每日更新 |
| 榜单数据 | 6 小时 | 榜单每日更新 |

**缓存键**：端点 + 规范化后的参数 JSON。**缓存位置**：`~/.admapix-cache/`（用户可清理）。

## FAQ

**Q1：为什么我的 `page_size=50` 被改成了 10？**
A：创意搜索端点强制上限 10，本技能自动钳制。翻页请用 `page` 参数递增，建议配合缓存避免重复消耗配额。

**Q2：下载/收入数字和官方财报对不上？**
A：本数据为第三方估算，非官方披露。请参考可信度分级（A/B/C），C 级数据仅用于趋势判断，不用于精确决策。

**Q3：如何批量导出某竞品全部创意？**
A：先用 `product-content-counts` 拿到总量，再分页 `product-content-search`（每页 10），结果写入本地文件。建议在夜间低峰执行，避免限流。

**Q4：`totalSize` 为什么是 null？**
A：过滤查询时 `totalSize` 可能为 null，此时以 `list` 长度为准，或单独调 `count` 端点获取准确总数。

**Q5：多个国家的数据能一次请求拿到吗？**
A：`search` / `distribute` 支持 `countries` 数组，但结果会合并。如需分别对比，请并行发多个单国家请求（见"场景二"）。

## 故障排查

| 症状 | 可能原因 | 解决方案 |
|------|----------|----------|
| 一直返回空 list | 参数代码错误 | 调 `filter-options` 核对国家/行业码 |
| 401 但 Key 看着对 | Key 含空格或换行 | `echo "${ADMAPIX_API_KEY}" \| wc -c` 检查长度 |
| 偶发 429 | 短时间高频调用 | 启用缓存，降低并发到 3 |
| 详情接口 404 | 创意已下线 | 跳过该 ID，记录到失败列表 |
| 估算数据明显异常 | 长尾地区样本稀疏 | 标注 C 级可信度，仅供参考 |

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：需可访问 `https://api.admapix.com`

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| AdMapix API | 远程 HTTP API | 必需 | https://www.admapix.com 注册获取 |
| curl 或等价 HTTP 客户端 | 命令行工具 | 必需 | 系统自带或包管理器安装 |
| jq（可选） | JSON 处理工具 | 可选 | 提升结果可读性，非必需 |

### API Key 配置

- **环境变量**（推荐）：`export ADMAPIX_API_KEY="你的Key"`
- **平台配置**：参考所用 Agent 平台的密钥管理文档
- **安全要求**：Key 仅作为 `X-API-Key` 请求头使用；永不写入日志、链接参数或聊天响应；永不接受用户在聊天中明文粘贴的 Key

### 可用性分类

- **分类**：MD+EXEC（Markdown 指令驱动，需 exec 执行 curl 命令）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 调用 AdMapix REST API 并处理 JSON 结果
