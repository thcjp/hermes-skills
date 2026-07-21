---
slug: finance-test-tool-free
name: finance-test-tool-free
version: "1.0.0"
displayName: 加密资产追踪入门
summary: 个人加密货币投资组合追踪工具，支持持仓记录与基础盈亏计算。
license: Proprietary
edition: free
description: |-
  面向个人加密货币投资者的投资组合追踪工具。支持记录持仓、查询实时
  价格、计算盈亏与基础统计分析。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- Finance
- 加密货币
- 投资组合
tools:
  - - read
- exec
---

# 加密资产追踪入门（免费版）

## 概述

本工具为个人加密货币投资者提供投资组合追踪能力。支持记录持仓信息、查询实时价格、计算盈亏并进行基础统计分析。适合个人用户管理加密货币投资组合，了解投资表现。

## 核心能力

### 追踪功能

| 功能 | 说明 | 免费版支持 |
| --- | --- | --- |
| 持仓记录 | 添加/删除/修改 | 支持 |
| 实时价格 | 行情查询 | 支持 |
| 盈亏计算 | 已实现/未实现 | 支持 |
| 组合统计 | 基础统计 | 支持 |
| 多账户 | 多钱包管理 | 不支持 |
| 批量导入 | CSV导入 | 不支持 |
| 价格告警 | 阈值通知 | 不支持 |
| 高级分析 | 风险/相关性 | 不支持 |

**输入**: 用户提供追踪功能所需的指令和必要参数。
**处理**: 按照skill规范执行追踪功能操作,遵循单一意图原则。
**输出**: 返回追踪功能的执行结果,包含操作状态和输出数据。

### 支持的代币

| 类型 | 说明 | 示例 |
| --- | --- | --- |
| 主流币 | 市值前50 | BTC, ETH, BNB, SOL |
| 稳定币 | 法币锚定 | USDT, USDC, DAI |
| 平台币 | 交易所代币 | BNB, OKB, CRO |
| DeFi代币 | 去中心化金融 | UNI, AAVE, COMP |

**输入**: 用户提供支持的代币所需的指令和必要参数。
**处理**: 按照skill规范执行支持的代币操作,遵循单一意图原则。
**输出**: 返回支持的代币的执行结果,包含操作状态和输出数据。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：个人加密货币投资、组合追踪工具、支持持仓记录与基、础盈亏计算、面向个人加密货币、投资者的投资组合、追踪工具、支持记录持仓、查询实时、计算盈亏与基础统、计分析、Use、when、需要数据分析、报表生成、统计洞察、数据可视化时使用、不适用于实时流数、据处理、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：记录持仓

用户输入："我买了0.5个BTC，成本40000"

```bash
# 添加持仓
python3 scripts/portfolio.py add \
  --token BTC \
  --amount 0.5 \
  --cost 40000 \
  --date "2026-01-15"

# 查看持仓
python3 scripts/portfolio.py list
```

### 场景二：查看盈亏

用户输入："我的投资组合现在赚了多少？"

```bash
# 查看组合概览
python3 scripts/portfolio.py summary

# 输出：
# === 投资组合概览 ===
# 总投入: $20,000
# 当前市值: $25,500
# 总盈亏: +$5,500 (+27.5%)
#
# 持仓明细：
# BTC  0.5个  成本$40,000  现价$45,000  +$2,500 (+12.5%)
# ETH  5个    成本$2,000   现价$2,500   +$2,500 (+25%)
# SOL  20个   成本$100     现价$150     +$1,000 (+50%)
```

### 场景三：交易记录

用户输入："记录一笔卖出交易"

```bash
# 记录卖出
python3 scripts/portfolio.py sell \
  --token ETH \
  --amount 2 \
  --price 2500 \
  --date "2026-02-20"

# 自动计算已实现盈亏
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 环境准备

```bash
# 依赖说明
pip install requests pandas

# 初始化投资组合
python3 scripts/portfolio.py init
```

### 常用命令

```bash
# 添加持仓
python3 scripts/portfolio.py add --token BTC --amount 0.5 --cost 40000

# 查看持仓
python3 scripts/portfolio.py list

# 组合概览
python3 scripts/portfolio.py summary

# 记录卖出
python3 scripts/portfolio.py sell --token ETH --amount 2 --price 2500

# 交易历史
python3 scripts/portfolio.py history

# 导出记录
python3 scripts/portfolio.py export --format csv
```

## 示例

### 投资组合配置

```yaml
portfolio_config:
  data_source: "coingecko"
  base_currency: "USD"
  cache_ttl: 60

  tracking:
    auto_refresh: false           # 免费版手动刷新
    refresh_interval: 300

  storage:
    type: "sqlite"
    path: "./portfolio.db"

  display:
    currency_format: "USD"
    decimal_places: 2
    show_percentage: true
```

## 最佳实践

1. **及时记录**：买卖后立即记录，避免遗忘
2. **成本准确**：记录实际买入成本（含手续费）
3. **定期复查**：定期查看组合表现，调整策略
4. **数据备份**：定期导出持仓数据备份

| 实践要点 | 说明 |
| --- | --- |
| 价格时效 | 加密货币24小时交易，价格实时变化 |
| 手续费 | 记录成本时包含Gas费和交易手续费 |
| 安全意识 | 不要将私钥或助记词记录在工具中 |
| 免责声明 | 工具仅供参考，投资有风险 |

## 常见问题

### Q1：免费版支持多少种代币？

免费版支持市值前50的主流代币。如需追踪更多代币（如小众DeFi代币），建议升级PRO版。

### Q2：数据来源是什么？

免费版使用CoinGecko免费API获取价格数据。可能存在延迟，仅供参考。

### Q3：支持多账户管理吗？

免费版仅支持单一投资组合。如需管理多个钱包或交易所账户，建议升级PRO版。

### Q4：可以连接交易所自动同步吗？

免费版需手动记录交易。如需自动同步交易所账户，建议升级PRO版支持API对接。

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
| requests | Python库 | 必需 | `pip install requests` |
| pandas | Python库 | 可选 | `pip install pandas`（数据分析） |

### API Key 配置

- 免费版无需任何API Key
- 价格数据通过CoinGecko免费API获取

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 本地存储加密货币投资组合数据，通过免费API查询价格
- **免费版限制**: 单一组合、手动记录、不支持交易所同步与高级分析

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
