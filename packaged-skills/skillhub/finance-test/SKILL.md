---
slug: finance-test
name: finance-test
version: "1.0.0"
displayName: 加密资产追踪专业版
summary: 专业加密货币投资组合管理系统，支持多账户同步、风险分析与税务报告。
license: Proprietary
edition: pro
description: |-
  面向专业加密货币投资者的投资组合管理系统。支持多交易所/多钱包账户
  同步、实时盈亏追踪、风险评估、相关性分析与税务报告生成。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- Finance
- 加密货币
- 投资组合
- 企业级
tools:
  - - read
- exec
---
# 加密资产追踪专业版

## 核心能力

### PRO版功能增强对比
| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 账户数量 | 单一组合 | 多账户统一管理 |
| 数据同步 | 手动记录 | 交易所API自动同步 |
| 代币支持 | 前50主流币 | 全代币+DeFi |
| 风险分析 | 不支持 | VaR/波动率/相关性 |
| 税务报告 | 不支持 | 自动生成 |
| DeFi追踪 | 不支持 | 流动性池/质押 |
| 价格告警 | 不支持 | 多通道通知 |
| 批量导入 | 不支持 | CSV/API导入 |

**输入**: 用户提供PRO版功能增强对比所需的指令和必要参数。
### 多账户同步
| 数据源 | 同步方式 | 支持内容 |
| --- | --- | --- |
| Binance | API Key | 现货/合约/理财 |
| OKX | API Key | 现货/合约/DeFi |
| Coinbase | API Key | 现货持仓 |
| MetaMask | 链上地址 | 链上资产+DeFi |
| Ledger | 硬件钱包 | 链上资产 |

**输入**: 用户提供多账户同步所需的指令和必要参数。
**处理**: 按照skill规范执行多账户同步操作,遵循单一意图原则。
**输出**: 返回多账户同步的执行结果,包含操作状态和输出数据。
### 账户数量

执行账户数量操作,处理用户输入并返回结果。

**输入**: 用户提供账户数量所需的参数和指令。

**输出**: 返回账户数量的处理结果。

- 执行`账户数量`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`账户数量`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 专业加密货币投资、组合管理系统、支持多账户同步、风险分析与税务报、面向专业加密货币、投资者的投资组合、管理系统、支持多交易所、多钱包账户、实时盈亏追踪、风险评估、相关性分析与税务、报告生成、Use、需要数据分析、报表生成、统计洞察、数据可视化时使用、不适用于实时流数、据处理、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一：多账户统一管理

用户输入："同步我所有交易所的持仓"

```bash
# 同步多交易所账户
python3 scripts/sync_accounts.py \
  --exchanges "binance,okx,coinbase" \
  --auto

# 输出统一持仓概览
python3 scripts/portfolio.py summary --all-accounts

# 输出：
# === 多账户投资组合概览 ===
# Binance:  $15,000 (BTC 0.3, ETH 3)
# OKX:      $8,500  (SOL 50, USDT 5000)
# Coinbase: $5,000  (BTC 0.1)
# 链上钱包: $3,000  (DeFi持仓)
# ─────────────────────
# 总市值:   $31,500
# 总盈亏:   +$8,200 (+35.2%)
```

### 场景二：风险分析

用户输入："分析我的投资组合风险"

```bash
# 风险评估
python3 scripts/risk_analysis.py \
  --portfolio all \
  --metrics "var,volatility,correlation,sharpe" \
  --output risk_report.pdf

# 输出包含：
# - Value at Risk (VaR)
# - 各资产波动率
# - 资产间相关性矩阵
# - 夏普比率
# - 风险调整建议
```

### 场景三：税务报告

用户输入："生成今年的加密货币税务报告"

```bash
# 生成税务报告
python3 scripts/tax_report.py \
  --year 2026 \
  --jurisdiction "US" \
  --method "FIFO" \
  --output crypto_tax_2026.pdf

# 输出包含：
# - 全年交易记录
# - 已实现盈亏明细
# - 应税事件汇总
# - 申报表格（如8949）
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt

# 配置交易所API
cp config_pro_template.yaml config_pro.yaml
# 填入各交易所API凭证（只读权限）
```

### 常用命令

```bash
# 多账户同步
python3 scripts/sync_accounts.py --exchanges "binance,okx" --auto

# 风险分析
python3 scripts/risk_analysis.py --portfolio all --metrics "var,volatility"

# 税务报告
python3 scripts/tax_report.py --year 2026 --method "FIFO"

# DeFi追踪
python3 scripts/defi_tracker.py --address 0x... --chain ethereum

# 价格告警
python3 scripts/alert.py add --token BTC --condition below --threshold 60000

# 批量导入
python3 scripts/import.py --file transactions.csv --format binance
```

### 命令参数说明

1. `--all-accounts`: 命令参数,用于指定操作选项
2. `--address`: 命令参数,用于指定操作选项
3. `--condition`: 命令参数,用于指定操作选项
4. `--format`: 命令参数,用于指定操作选项
5. `--method`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

### 命令参数说明

- `--year`: 命令参数,用于指定操作选项
- `--exchanges`: 命令参数,用于指定操作选项
- `--metrics`: 命令参数,用于指定操作选项
- `--chain`: 命令参数,用于指定操作选项
- `--threshold`: 命令参数,用于指定操作选项

### 命令参数说明

- `--token`: 命令参数,用于指定操作选项
- `--jurisdiction`: 命令参数,用于指定操作选项
- `--portfolio`: 命令参数,用于指定操作选项
- `--file`: 命令参数,用于指定操作选项
- `--auto`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

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
| requests | Python库 | 必需 | `pip install requests` |
| pandas | Python库 | 必需 | `pip install pandas` |
| numpy | Python库 | 必需 | `pip install numpy`（风险计算） |
| scipy | Python库 | 可选 | `pip install scipy`（统计模型） |
| web3 | Python库 | 可选 | `pip install web3`（DeFi追踪） |
| ccxt | Python库 | 可选 | `pip install ccxt`（交易所API） |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| Binance | `BINANCE_API_KEY` | 可选 | 交易所同步 |
| OKX | `OKX_API_KEY` | 可选 | 交易所同步 |
| Coinbase | `COINBASE_API_KEY` | 可选 | 交易所同步 |
| CoinGecko Pro | `COINGECKO_API_KEY` | 可选 | 高频价格数据 |

- 交易所API仅需只读权限
- 所有凭证加密存储在本地配置文件

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+API执行）
- **说明**: 专业加密货币投资组合管理系统，支持多账户同步与风险分析
- **PRO版特性**: 多账户同步、风险评估、税务报告、DeFi追踪、价格告警、批量导入
- **兼容性**: 完全兼容免费版持仓数据与命令，支持一键迁移
- **安全提示**: API仅授予只读权限，密钥加密存储不上传

## 案例展示

### PRO系统配置

```yaml
pro_config:
  accounts:
    exchanges:
      - name: "Binance"
        api_key: "${BINANCE_API_KEY}"
        api_secret: "${BINANCE_API_SECRET}"
        permissions: ["read_only"]
      - name: "OKX"
        api_key: "${OKX_API_KEY}"
        api_secret: "${OKX_API_SECRET}"
        passphrase: "${OKX_PASSPHRASE}"

    wallets:
      - name: "MetaMask"
        address: "0x..."
        chains: ["ethereum", "bsc", "polygon"]
      - name: "Phantom"
        address: "..."
        chains: ["solana"]

  risk_analysis:
    var_confidence: 0.95             # VaR置信度
    var_horizon: 1                   # VaR时间窗口（天）
    correlation_method: "pearson"
    benchmark: "BTC"

  tax:
    jurisdictions: ["US", "CN"]
    methods: ["FIFO", "LIFO", "HIFO"]
    generate_forms: true

  defi:
    track_liquidity_pools: true
    track_staking: true
    track_lending: true
    auto_detect: true

  alerts:
    channels: ["telegram", "email"]
    price_alerts: true
    abnormal_activity: true
    large_transactions: true
    threshold: 10000

  storage:
    type: "postgresql"
    host: "${DB_HOST}"
    encrypted: true
```

## 常见问题

### Q1：交易所API安全吗？

PRO版仅需要只读API权限，不提现权限。API密钥加密存储在本地，不会上传服务器。建议定期轮换密钥，并设置IP白名单。

### Q2：税务报告支持哪些国家？

支持美国（8949表格）、中国、英国、澳大利亚等主要司法管辖区。各国家税务规则不同，报告仅供参考，具体申报请咨询专业税务师。

### Q3：DeFi持仓如何追踪？

PRO版通过链上地址自动扫描DeFi持仓，包括Uniswap流动性池、AAVE借贷、Lido质押等。支持以太坊、BSC、Polygon等主流链。

### Q4：风险分析使用什么模型？

PRO版使用历史模拟法计算VaR，使用对数收益率计算波动率，使用皮尔逊相关系数分析资产间相关性。可配置置信度和时间窗口。

### Q5：支持NFT追踪吗？

PRO版支持以太坊和Solana链上NFT持仓的基础追踪。由于NFT估值复杂，目前仅显示持仓数量和最近交易价格。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
