---
slug: "finance-radar-paid"
name: "finance-radar-paid"
version: "1.0.0"
displayName: "股票分析雷达专业版"
summary: "专业股票与加密货币分析平台，支持批量分析、组合追踪、价格告警与传闻检测。"
license: "Proprietary"
edition: "pro"
description: |-
  面向专业投资者与机构的股票与加密货币分析平台。支持批量标的分析、
  投资组合追踪、价格告警、热门趋势检测、传闻与早期信号识别。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标。
tags:
  - Finance
  - 股票分析
  - 投资组合
  - 企业级
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "金融,财务,数据"
---
# 股票分析雷达专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 股票分析雷达专业版业股票与加密货币分析 | 不支持 | 支持 |
| 股票分析雷达专业版支持批量分析 | 不支持 | 支持 |
| DCF估值建模与敏感性分析 | 不支持 | 支持 |
| 财务舞弊识别(Beneish M-Score) | 不支持 | 支持 |
| 批量财报处理与自动化报告 | 不支持 | 支持 |

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
|:-----|:-----|:-----|
| 综合分析 | 单标的 | 批量并行 |
| 评分模型 | 固定8维度 | 可自定义权重 |
| 批量分析 | 不支持 | 支持+CSV导出 |
| 组合追踪 | 不支持 | 完整P&L |
| 价格告警 | 不支持 | 多通道通知 |
| 热门扫描 | 基础版 | 病毒传播检测 |
| 传闻检测 | 不支持 | 早期信号识别 |
| 数据导出 | 不支持 | CSV/Excel/JSON |- 验证返回数据的完整性和格式正确性
- 参考`投资组合追踪`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`批量分析与导出`的配置文档进行参数调优
### 批量分析与导出
```bash
# 批量分析多只标的
python3 （请参考skill目录中的脚本文件） --tickers AAPL,GOOG,MSFT,AMZN,TSLA
# ...
# 导出CSV对比矩阵
python3 （请参考skill目录中的脚本文件） --tickers AAPL,GOOG,MSFT --export --output comparison.csv
```

**输入**: 用户提供批量分析与导出所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量分析与导出` 选项
- 处理流程: 接收输入 -> 执行批量分析与导出 -> 返回结果
- 输入: 用户提供批量分析与导出所需的参数和指令
- 输出: 返回批量分析与导出的处理结果,包含执行状态码、结果数据和执行日志

### 投资组合追踪
```bash
# 导入组合
python3 （请参考skill目录中的脚本文件） import --file holdings.csv
# ...
# 查看组合P&L
python3 （请参考skill目录中的脚本文件） summary
# ...
# 风险分析
python3 （请参考skill目录中的脚本文件） risk-analysis --output risk_report.pdf
```

#
## 适用场景

### 场景一：批量筛选股票

用户输入："帮我分析科技板块的20只股票"

```bash
# 批量分析并导出
python3 （请参考skill目录中的脚本文件） \
  --tickers "AAPL,MSFT,GOOG,AMZN,META,NVDA,TSLA,AMD,INTC,...,AVGO" \
  --skills "analyze,score" \
  --export \
  --output tech_sector_analysis.xlsx \
  --sort-by "score" \
  --descending
# ...
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
python3 （请参考skill目录中的脚本文件） summary
# ...
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
python3 （请参考skill目录中的脚本文件） --scan
# ...
# 输出：
# === 市场传闻扫描 ===
# 1. [高可信] NVDA AI芯片需求超预期 - 来源3处
# 2. [中可信] 某医药公司FDA审批在即 - 来源2处
# 3. [低可信] 某能源公司并购传闻 - 来源1处
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt
# ...
# 配置数据源与通知
cp config_pro_template.yaml config_pro.yaml
```

### 常用命令

```bash
# 批量分析
python3 （请参考skill目录中的脚本文件） --tickers AAPL,GOOG,MSFT --export
# ...
# 组合管理
python3 （请参考skill目录中的脚本文件） import --file holdings.csv
python3 （请参考skill目录中的脚本文件） summary
python3 （请参考skill目录中的脚本文件） risk-analysis
# ...
# 价格告警
python3 （请参考skill目录中的脚本文件） add AAPL --alert-above 180 --alert-below 170
python3 （请参考skill目录中的脚本文件） monitor
# ...
# 传闻扫描
python3 （请参考skill目录中的脚本文件） --scan
python3 （请参考skill目录中的脚本文件） --viral
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | finance-radar处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| yfinance | Python库 | 必需 | `pip install yfinance` |
| pandas | Python库 | 必需 | `pip install pandas` |
| numpy | Python库 | 必需 | `pip install numpy` |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |
| requests | Python库 | 必需 | `pip install requests`（API调用） |

### API Key 配置

| 服务 | 环境变量 | 用途 |
|---:|:---|---:|
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

## 案例展示

### PRO高级配置

```yaml
pro_config:
  data_sources:
    primary: "yahoo_finance"
    secondary: "alpha_vantage"
    cache_ttl: 60
# ...
  batch:
    max_parallel: 10             # 最大并行数
    timeout: 300                 # 超时（秒）
    export_formats: ["csv", "excel", "json"]
# ...
  portfolio:
    auto_refresh: true
    refresh_interval: 60         # 刷新间隔（秒）
    benchmark: "SPY"             # 基准标的
    risk_model: "var"            # 风险模型
# ...
  alerts:
    channels:
      - console
      - webhook
      - email
    webhook_url: "${WEBHOOK_URL}"
    email_config:
      smtp_host: "${SMTP_HOST}"
      smtp_port: 587
# ...
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
# ...
  rumor_detection:
    sources: ["news", "social_media", "sec_filings"]
    min_credibility: 0.5
    scan_interval: 3600
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

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

