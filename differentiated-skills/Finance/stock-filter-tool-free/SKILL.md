---
slug: stock-filter-tool-free
name: stock-filter-tool-free
version: "1.0.0"
displayName: 股票筛选入门工具
summary: A股股票筛选工具，支持基本面与技术面过滤，单策略逐只分析。
license: MIT
edition: free
description: |-
  面向个人投资者的A股股票筛选工具。支持按基本面（PE/PB/ROE等）和
  技术面（均线/RSI等）条件筛选股票。适合个人投资者进行简单的选股
  分析与初步筛选。

  核心能力:
  - 基本面筛选（PE/PB/ROE/营收增长等）
  - 技术面筛选（均线/RSI/MACD等）
  - 单策略逐只分析
  - 结果列表展示

  适用场景:
  - 个人投资者选股
  - 基本面初步筛选
  - 技术面信号扫描
  - 学习研究用途

  差异化:
  - 免费版聚焦单策略筛选
  - 适合个人用户低频使用
  - 不支持多策略组合
  - 不支持批量导出

  触发关键词: 股票筛选, 选股, 基本面, 技术面, PE, PB, ROE, 均线, RSI, stock filter, screener
tags:
- Finance
- 股票筛选
- 选股工具
tools:
- read
- exec
---

# 股票筛选入门工具（免费版）

## 概述

本工具为个人投资者提供A股股票筛选能力。支持按基本面和技术面条件筛选股票，帮助用户从大量股票中快速找到符合条件的标的。适合个人投资者进行简单的选股分析与初步筛选。

## 核心能力

### 筛选功能

| 功能 | 说明 | 免费版支持 |
| --- | --- | --- |
| 基本面筛选 | PE/PB/ROE等 | 支持 |
| 技术面筛选 | 均线/RSI等 | 支持 |
| 策略组合 | 多策略叠加 | 不支持 |
| 批量导出 | CSV/Excel | 不支持 |
| 自定义公式 | 复杂条件 | 不支持 |
| 历史回测 | 策略验证 | 不支持 |
| 行业筛选 | 按行业过滤 | 支持 |
| 市值筛选 | 按市值范围 | 支持 |

### 基本面筛选条件

| 条件 | 说明 | 示例 |
| --- | --- | --- |
| PE | 市盈率范围 | 0 < PE < 30 |
| PB | 市净率范围 | 0 < PB < 5 |
| ROE | 净资产收益率 | ROE > 15% |
| 营收增长 | 营收同比增长率 | 增长 > 20% |
| 净利增长 | 净利润同比增长率 | 增长 > 25% |
| 股息率 | 年度股息率 | 股息率 > 3% |
| 市值 | 总市值范围 | 100亿-1000亿 |
| 负债率 | 资产负债率 | < 60% |

## 使用场景

### 场景一：基本面筛选

用户输入："帮我找PE小于20、ROE大于15%的股票"

```bash
# 基本面筛选
python3 scripts/filter.py \
  --market a-share \
  --conditions "pe<20,roe>15" \
  --sort-by roe \
  --descending

# 输出：
# 代码    名称      PE    ROE    市值
# 600519  贵州茅台  25.3  30.2   2.1万亿
# 000858  五粮液    22.1  25.6   6500亿
# ...
```

### 场景二：技术面筛选

用户输入："找出MACD金叉的股票"

```bash
# 技术面筛选
python3 scripts/filter.py \
  --market a-share \
  --conditions "macd_cross=golden" \
  --sort-by volume
```

### 场景三：行业筛选

用户输入："筛选白酒行业的股票"

```bash
# 行业筛选
python3 scripts/filter.py \
  --market a-share \
  --industry "白酒" \
  --conditions "pe<30,roe>20"
```

## 快速开始

### 环境准备

```bash
# 安装依赖
pip install akshare pandas

# 运行筛选
python3 scripts/filter.py --conditions "pe<20,roe>15"
```

### 常用命令

```bash
# 基本面筛选
python3 scripts/filter.py --conditions "pe<20,roe>15,debt_ratio<0.6"

# 技术面筛选
python3 scripts/filter.py --conditions "macd_cross=golden,rsi<30"

# 行业+基本面
python3 scripts/filter.py --industry "白酒" --conditions "pe<30,roe>20"

# 市值筛选
python3 scripts/filter.py --market-cap "100亿-1000亿" --conditions "pe<25"
```

## 配置示例

### 筛选配置

```yaml
filter_config:
  market: a-share                # a-share | us-stock | hk-stock
  data_source: "akshare"

  defaults:
    sort_by: "roe"
    descending: true
    max_results: 50

  conditions:
    fundamentals:
      pe: { min: 0, max: 30 }
      pb: { min: 0, max: 5 }
      roe: { min: 15 }
      revenue_growth: { min: 0.1 }
      debt_ratio: { max: 0.6 }

    technical:
      ma_periods: [5, 10, 20, 60]
      rsi_period: 14
      macd: { fast: 12, slow: 26, signal: 9 }

  cache:
    ttl: 3600                   # 数据缓存1小时
```

## 最佳实践

1. **先粗后细**：先用宽松条件大范围筛选，再逐步收紧
2. **多维度交叉**：基本面与技术面结合，提高筛选质量
3. **行业对比**：同行业内筛选更有可比性
4. **定期复查**：市场变化快，建议定期重新筛选

| 实践要点 | 说明 |
| --- | --- |
| 数据时效 | 基本面数据可能滞后，注意财报日期 |
| 筛选范围 | 免费版建议单次筛选条件不超过5个 |
| 结果验证 | 筛选结果需进一步人工分析 |
| 免责声明 | 筛选结果仅供参考，不构成投资建议 |

## 常见问题

### Q1：免费版支持多策略组合吗？

免费版仅支持单策略筛选（多个条件AND组合）。如需多策略OR组合或复杂逻辑，建议升级PRO版。

### Q2：数据来源是什么？

免费版使用AkShare开源数据接口，数据来源包括东方财富、同花顺等公开数据。可能有延迟，仅供参考。

### Q3：支持港股和美股吗？

免费版主要支持A股筛选。美股和港股支持有限，如需完整覆盖，建议升级PRO版。

### Q4：筛选结果可以导出吗？

免费版仅支持终端展示。如需导出CSV/Excel，建议升级PRO版。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| akshare | Python库 | 必需 | `pip install akshare` |
| pandas | Python库 | 必需 | `pip install pandas` |

### API Key 配置

- 免费版无需任何API Key
- 数据通过AkShare开源接口免费获取

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 通过AkShare获取A股数据进行筛选
- **免费版限制**: 单策略、不支持导出、主要支持A股
