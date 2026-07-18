---
slug: finance-radar-tool-pro
name: finance-radar-tool-pro
version: "1.0.0"
displayName: 股票分析雷达专业版
summary: 专业股票与加密货币分析平台，支持批量分析、组合追踪、价格告警与传闻检测。
license: MIT
edition: pro
description: |-
  面向专业投资者与机构的股票与加密货币分析平台。支持批量标的分析、
  投资组合追踪、价格告警、热门趋势检测、传闻与早期信号识别。内置
  高级评分模型与CSV导出功能，全面满足专业投研需求。

  核心能力:
  - 批量分析：多标的并行分析并导出CSV对比矩阵
  - 投资组合追踪：持仓P&L与组合风险评估
  - 价格告警：自定义阈值与多通道通知
  - 热门趋势检测：病毒式传播信号识别
  - 传闻检测：早期信号与市场传闻监控
  - 自定义评分模型：可调整维度权重与阈值

  适用场景:
  - 专业投研团队批量筛选
  - 投资组合实时监控
  - 量化策略标的筛选
  - 市场热点追踪
  - 早期投资机会发现

  差异化:
  - 兼容免费版全部功能，无缝升级
  - 新增批量分析与CSV导出
  - 投资组合追踪与P&L计算
  - 价格告警与多通道推送
  - 传闻检测与早期信号识别

  触发关键词: 股票分析, 批量分析, 组合追踪, 价格告警, 热门, 传闻, 早期信号, 雷达, stock, crypto, batch, portfolio, alert
tags:
- Finance
- 股票分析
- 投资组合
- 企业级
tools:
- read
- exec
---

# 股票分析雷达专业版（PRO版）

## 概述

本平台为专业投资者和投研团队提供全功能的股票与加密货币分析能力。相比免费版，PRO版新增批量分析、组合追踪、价格告警、传闻检测等高级功能，内置可自定义的评分模型，全面满足专业投研与投资管理的复杂需求。

PRO版完全兼容免费版全部命令与评分模型，升级后原有分析工作流可直接使用。

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 综合分析 | 单标的 | 批量并行 |
| 评分模型 | 固定8维度 | 可自定义权重 |
| 批量分析 | 不支持 | 支持+CSV导出 |
| 组合追踪 | 不支持 | 完整P&L |
| 价格告警 | 不支持 | 多通道通知 |
| 热门扫描 | 基础版 | 病毒传播检测 |
| 传闻检测 | 不支持 | 早期信号识别 |
| 数据导出 | 不支持 | CSV/Excel/JSON |

### 批量分析与导出

```bash
# 批量分析多只标的
python3 scripts/batch.py --tickers AAPL,GOOG,MSFT,AMZN,TSLA

# 导出CSV对比矩阵
python3 scripts/batch.py --tickers AAPL,GOOG,MSFT --export --output comparison.csv
```

### 投资组合追踪

```bash
# 导入组合
python3 scripts/portfolio.py import --file holdings.csv

# 查看组合P&L
python3 scripts/portfolio.py summary

# 风险分析
python3 scripts/portfolio.py risk-analysis --output risk_report.pdf
```

## 使用场景

### 场景一：批量筛选股票

用户输入："帮我分析科技板块的20只股票"

```bash
# 批量分析并导出
python3 scripts/batch.py \
  --tickers "AAPL,MSFT,GOOG,AMZN,META,NVDA,TSLA,AMD,INTC,...,AVGO" \
  --skills "analyze,score" \
  --export \
  --output tech_sector_analysis.xlsx \
  --sort-by "score" \
  --descending

# 输出包含：
# - 各标的8维度评分排名
# - 关键财务指标对比矩阵
# - 估值水平分布图
# - 综合推荐列表
```

### 场景二：投资组合监控

用户输入："看看我的投资组合今天表现如何"

```bash
# 组合P&L汇总
python3 scripts/portfolio.py summary

# 输出：
# === 投资组合日报 2026-07-18 ===
# 总市值: $125,000 | 日P&L: +$1,250 (+1.0%)
# 持仓数: 12 | 胜率: 8/12
# 最大盈利: AAPL +$500
# 最大亏损: TSLA -$200
# 行业分布: 科技45% 消费25% 金融20% 其他10%
```

### 场景三：传闻与早期信号

用户输入："最近有什么市场传闻值得关注？"

```bash
# 传闻检测
python3 scripts/rumor.py --scan

# 输出：
# === 市场传闻扫描 ===
# 1. [高可信] NVDA AI芯片需求超预期 - 来源3处
# 2. [中可信] 某医药公司FDA审批在即 - 来源2处
# 3. [低可信] 某能源公司并购传闻 - 来源1处
```

## 快速开始

### PRO版初始化

```bash
# 安装PRO版依赖
pip install -r requirements_pro.txt

# 配置数据源与通知
cp config_pro_template.yaml config_pro.yaml
```

### 常用命令

```bash
# 批量分析
python3 scripts/batch.py --tickers AAPL,GOOG,MSFT --export

# 组合管理
python3 scripts/portfolio.py import --file holdings.csv
python3 scripts/portfolio.py summary
python3 scripts/portfolio.py risk-analysis

# 价格告警
python3 scripts/watchlist.py add AAPL --alert-above 180 --alert-below 170
python3 scripts/watchlist.py monitor

# 传闻扫描
python3 scripts/rumor.py --scan
python3 scripts/hot_scan.py --viral
```

## 配置示例

### PRO高级配置

```yaml
pro_config:
  data_sources:
    primary: "yahoo_finance"
    secondary: "alpha_vantage"
    cache_ttl: 60

  batch:
    max_parallel: 10             # 最大并行数
    timeout: 300                 # 超时（秒）
    export_formats: ["csv", "excel", "json"]

  portfolio:
    auto_refresh: true
    refresh_interval: 60         # 刷新间隔（秒）
    benchmark: "SPY"             # 基准标的
    risk_model: "var"            # 风险模型

  alerts:
    channels:
      - console
      - webhook
      - email
    webhook_url: "${WEBHOOK_URL}"
    email_config:
      smtp_host: "${SMTP_HOST}"
      smtp_port: 587

  scoring:
    model: "custom"              # custom | 8-dimension
    weights:
      profitability: 0.20        # 自定义权重
      growth: 0.20
      valuation: 0.15
      financial_health: 0.15
      cashflow: 0.10
      dividend: 0.05
      technical: 0.10
      sentiment: 0.05

  rumor_detection:
    sources: ["news", "social_media", "sec_filings"]
    min_credibility: 0.5
    scan_interval: 3600
```

## 最佳实践

### PRO版高级实践

| 实践领域 | 建议做法 |
| --- | --- |
| 批量筛选 | 先用热门扫描缩小范围，再批量深度分析 |
| 组合监控 | 设置每日自动刷新，关注行业集中度 |
| 告警策略 | 设置多级阈值（预警/警告/紧急） |
| 传闻验证 | 传闻仅供参考，需交叉验证后决策 |
| 评分调优 | 根据投资风格调整维度权重 |

### 免费版兼容性

```text
免费版命令 → PRO版命令（增强）：
analyze.py --ticker AAPL  → batch.py --tickers AAPL,MSFT,...
score.py --ticker TSLA    → 自定义权重评分
dividend.py --ticker KO   → 批量股息对比
hot_scan.py               → +病毒传播检测
```

## 常见问题

### Q1：批量分析支持多少只标的？

PRO版单批次支持最多50只标的的并行分析。建议根据数据源API限额调整并行度。结果自动导出为CSV/Excel对比矩阵。

### Q2：投资组合支持哪些格式导入？

支持CSV和Excel格式。CSV需包含ticker、shares、cost_basis字段。也支持从券商账户API直接同步（需额外配置）。

### Q3：价格告警如何通知？

支持控制台、Webhook和邮件三种通知方式。Webhook可集成企业微信、钉钉等IM工具。告警触发后自动记录历史，避免重复通知。

### Q4：传闻检测的数据来源是什么？

PRO版从新闻媒体、社交媒体和SEC公开文件中扫描潜在信号。通过多源交叉验证评估可信度。所有传闻仅供参考，不构成投资建议。

### Q5：自定义评分模型如何配置？

在config_pro.yaml的scoring部分修改weights字段即可。各维度权重之和需为1.0。修改后立即生效，无需重启。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| yfinance | Python库 | 必需 | `pip install yfinance` |
| pandas | Python库 | 必需 | `pip install pandas` |
| numpy | Python库 | 必需 | `pip install numpy` |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |
| requests | Python库 | 必需 | `pip install requests`（API调用） |

### API Key 配置

| 服务 | 环境变量 | 用途 |
|:-------|:---------|:-----|
| Alpha Vantage | `ALPHA_VANTAGE_API_KEY` | 备选数据源 |
| News API | `NEWS_API_KEY` | 传闻检测新闻源 |
| Webhook | `WEBHOOK_URL` | 告警推送 |

- 未配置的API会自动跳过，不影响核心功能
- 所有API Key存储在本地配置文件

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 专业级股票与加密货币分析平台，支持批量处理与组合追踪
- **PRO版特性**: 批量分析、组合追踪、价格告警、传闻检测、自定义评分
- **兼容性**: 完全兼容免费版全部命令与评分模型
