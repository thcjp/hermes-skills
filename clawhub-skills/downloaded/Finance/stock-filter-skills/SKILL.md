---
slug: stock-filter-skills
name: stock-filter-skills
version: "1.3.0"
displayName: Stock Filter Skills
summary: 股票多条件筛选、热门因子管理、Jiuyan 数据查询和抖音热点分析。提供 17 个 CLI 工具覆盖四大模块。
license: MIT-0
description: |-
  股票多条件筛选、热门因子管理、Jiuyan 数据查询和抖音热点分析。提供 17 个 CLI 工具覆盖四大模块。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- Finance
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Stock Filter Skills

股票多条件筛选、热门因子管理、Jiuyan 数据查询和抖音热点分析。

当用户提到股票筛选、股票搜索、股票详情、股票对比、批量查询、股票分析、热门因子、因子预设、jiuyan/韭研、抖音热点等话题时，使用本技能。

## Setup

安装依赖：

```bash
cd {baseDir} && npm install
```

需要配置以下环境变量（在 Skill平台 config 中设置 `skills.entries.stock-filter-skills.env`）：

* `STOCK_API_BASE_URL`: API 服务地址（必填）
* `STOCK_API_KEY`: API 认证密钥（必填，联系后端管理员申请）
* `STOCK_API_TIMEOUT`: 请求超时秒数（可选，默认 30）

## 使用方式

所有工具通过 CLI 调用，格式为：

```bash
node src/main.js <tool_name> '<JSON 参数>'
```

无参数的工具直接调用：

```bash
node src/main.js <tool_name>
```

工作目录必须为 `{baseDir}`。

## 工具列表

### 股票筛选模块

**stock_filter** — 多条件筛选股票，支持分页排序

```bash
node src/main.js stock_filter '{"filters": {"market": ["sh"]}, "page": 1, "page_size": 20, "sort_field": "pe", "sort_order": "asc"}'
```

参数: filters(object, 筛选条件), page(int, 页码), page_size(int, 每页数量), sort_field(string, 排序字段), sort_order(string, asc/desc)

**stock_filter_options** — 获取所有可用筛选维度和选项（无参数）

```bash
node src/main.js stock_filter_options
```

使用 stock_filter 前应先调用本工具了解有哪些维度可用。

**stock_search** — 按关键词搜索股票

```bash
node src/main.js stock_search '{"keyword": "贵州茅台", "limit": 10}'
```

参数: keyword(string, 必填, 搜索关键词), limit(int, 可选, 返回上限默认10)

**stock_detail** — 获取股票详细指标（PE/PB/ROE/毛利率/负债率/营收/净利润/大单/概念板块）

```bash
node src/main.js stock_detail '{"code": "600519"}'
```

参数: code(string, 必填, 股票代码)

**stock_detail_batch** — 批量获取多只股票详情，并发请求提高效率

```bash
node src/main.js stock_detail_batch '{"codes": ["600519", "000858", "000333"]}'
```

参数: codes(array, 必填, 股票代码列表)

需要同时查看多只股票时使用本工具，比逐个调用 stock_detail 更高效。单只股票失败不影响其他结果。

**stock_compare** — 对比多只股票的指标，可指定对比字段

```bash
node src/main.js stock_compare '{"codes": ["600519", "000858"], "fields": ["pe", "pb", "roe", "gross_margin"]}'
```

参数: codes(array, 必填, 股票代码列表), fields(array, 可选, 对比字段列表)

不传 fields 则返回所有指标。传入 fields 时仅返回指定字段的对比数据，结果更精简易读。

### 热门因子模块

**hot_factor_list** — 获取因子预设列表（无参数）

```bash
node src/main.js hot_factor_list
```

**hot_factor_create** — 创建因子预设

```bash
node src/main.js hot_factor_create '{"name": "成长股筛选", "factors": ["roe_high", "revenue_growth"]}'
```

参数: name(string, 必填, 预设名称), factors(array, 必填, 因子ID列表)

**hot_factor_update** — 更新因子预设

```bash
node src/main.js hot_factor_update '{"preset_id": "xxx", "name": "新名称"}'
```

参数: preset_id(string, 必填), name(string, 可选), factors(array, 可选)

**hot_factor_delete** — 删除因子预设（不可恢复）

```bash
node src/main.js hot_factor_delete '{"preset_id": "xxx"}'
```

参数: preset_id(string, 必填)

**hot_factor_use** — 使用预设并增加计数

```bash
node src/main.js hot_factor_use '{"preset_id": "xxx"}'
```

参数: preset_id(string, 必填)

**hot_factor_sort** — 调整预设排序

```bash
node src/main.js hot_factor_sort '{"preset_ids": ["id1", "id2", "id3"]}'
```

参数: preset_ids(array, 必填, 按期望顺序排列的ID列表)

### Jiuyan 数据模块

**jiuyan_stock_analysis** — 获取股票综合分析

```bash
node src/main.js jiuyan_stock_analysis '{"stock_code": "300236"}'
```

参数: stock_code(string, 必填, 股票代码)

**jiuyan_stock_theme** — 获取股票主题/题材数据

```bash
node src/main.js jiuyan_stock_theme '{"stock_code": "300236"}'
```

参数: stock_code(string, 必填, 股票代码)

**jiuyan_articles** — 批量获取文章详情

```bash
node src/main.js jiuyan_articles '{"article_ids": "id1,id2,id3"}'
```

参数: article_ids(string, 必填, 逗号分隔的文章ID)

### 抖音热点模块

**douyin_hotspot_list** — 获取抖音热点列表

```bash
node src/main.js douyin_hotspot_list '{"page": 1, "page_size": 20}'
```

参数: page(int, 可选, 默认1), page_size(int, 可选, 默认20)

**douyin_hotspot_detail** — 获取热点详情

```bash
node src/main.js douyin_hotspot_detail '{"aweme_id": "xxx"}'
```

参数: aweme_id(string, 必填, 热点ID)

## 错误处理

所有工具返回 JSON。错误时格式为 `{"error": "描述"}`。常见错误：认证失败（检查 API Key）、连接失败（检查服务是否启动）、参数错误。

## 使用流程

1. 筛选股票：先 stock_filter_options 获取维度 → 再 stock_filter 执行筛选
2. 查股票：stock_search 搜索 → stock_detail 查详情
3. 批量查询：stock_detail_batch 一次获取多只股票详情
4. 对比股票：stock_compare 对比多只股票的关键指标
5. 分析股票：jiuyan_stock_analysis 获取分析 → jiuyan_stock_theme 查看主题
6. 管理预设：hot_factor_list 查看 → hot_factor_create/update/delete 操作
7. 看热点：douyin_hotspot_list 浏览 → douyin_hotspot_detail 查详情

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 股票多条件筛选、热门因子管理、Jiuyan 数据查询和抖音热点分析
- 提供 17 个 CLI 工具覆盖四大模块
- 触发关键词: 音热点分析, 热门因子管理, 股票多条件筛, jiuyan, skills, 提供, 数据查询和抖, filter

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
1. 筛选股票：先 stock_filter_options 获取维度 → 再 stock_filter 执行筛选
2. 查股票：stock_search 搜索 → stock_detail 查详情
3. 批量查询：stock_detail_batch 一次获取多只股票详情
4. 对比股票：stock_compare 对比多只股票的关键指标
5. 分析股票：jiuyan_stock_analysis 获取分析 → jiuyan_stock_theme 查看主题
6. 管理预设：hot_factor_list 查看 → hot_factor_create/update/delete 操作
7. 看热点：douyin_hotspot_list 浏览 → douyin_hotspot_detail 查详情
```

## 常见问题

### Q1: 如何开始使用Stock Filter Skills？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Stock Filter Skills有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
