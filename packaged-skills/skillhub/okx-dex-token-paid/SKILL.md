---
slug: okx-dex-token-paid
name: okx-dex-token-paid
version: "1.0.0"
displayName: DEX代币数据专业版
summary: 专业DEX代币分析与交易工具，支持多链深度分析、批量查询与限价交易。
license: Proprietary
edition: pro
description: |-
  面向专业DeFi交易者与研究员的DEX代币分析与交易工具。支持15+条链
  深度数据分析、批量代币查询、链上行为追踪、流动性监控告警与限价
  交易执行。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- Finance
- 加密货币
- DEX
- 企业级
tools:
  - - read
- exec
---
# DEX代币数据专业版

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 支持链数 | 5条 | 15+条 |
| 批量查询 | 不支持 | 支持+CSV导出 |
| 链上追踪 | 不支持 | 大户/鲸鱼监控 |
| 价格告警 | 不支持 | 多通道通知 |
| 交易执行 | 不支持 | 限价+MEV防护 |
| 套利识别 | 不支持 | 跨DEX/跨链 |
| 安全审计 | 不支持 | 合约风险评分 |
| 数据导出 | 不支持 | CSV/Excel/JSON |

### 全链支持
| 链名称 | Chain ID | 免费版 | PRO版 |
| --- | --- | --- | --- |
| Ethereum | 1 | 支持 | 支持 |
| BSC | 56 | 支持 | 支持 |
| Polygon | 137 | 支持 | 支持 |
| Arbitrum | 42161 | 支持 | 支持 |
| Optimism | 10 | 支持 | 支持 |
| Avalanche | 43114 | 不支持 | 支持 |
| Fantom | 250 | 不支持 | 支持 |
| Base | 8453 | 不支持 | 支持 |
| Linea | 59144 | 不支持 | 支持 |
| zkSync Era | 324 | 不支持 | 支持 |
| Scroll | 534352 | 不支持 | 支持 |
| Mantle | 5000 | 不支持 | 支持 |
| ... | ... | ... | 支持 |

**输入**: 用户提供全链支持所需的指令和必要参数。
**处理**: 按照skill规范执行全链支持操作,遵循单一意图原则。
**输出**: 返回全链支持的执行结果,包含操作状态和输出数据。
### 支持链数

执行支持链数操作,处理用户输入并返回结果。

**输入**: 用户提供支持链数所需的参数和指令。

**输出**: 返回支持链数的处理结果。


## 适用场景

### 场景一：批量代币研究

用户输入："分析以太坊上流动性前50的代币"

```bash
# 批量查询代币数据
python3 scripts/batch_query.py \
  --chain ethereum \
  --top 50 \
  --sort-by liquidity \
  --export \
  --output top50_tokens.xlsx

# 输出包含：
# - 代币价格与24h变化
# - 流动性池规模
# - 交易量排名
# - 合约安全评分
# - 持有者分布
```

### 场景二：鲸鱼监控

用户输入："追踪某代币大户的买卖行为"

```bash
# 设置鲸鱼监控
python3 scripts/whale_tracker.py \
  --token 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984 \
  --chain ethereum \
  --threshold 100000 \
  --alert

# 实时输出：
# [ALERT] 鲸鱼地址 0xabc... 买入 500,000 UNI
# [ALERT] 鲸鱼地址 0xdef... 卖出 200,000 UNI
```

### 场景三：限价交易

用户输入："当UNIS跌到6美元以下时自动买入"

```bash
# 设置限价单
python3 scripts/limit_order.py create \
  --token UNIS \
  --chain ethereum \
  --side buy \
  --price 6.0 \
  --amount 1000 \
  --mev-protection

# 监控执行状态
python3 scripts/limit_order.py status
```

## 使用流程

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt

# 配置钱包与API
cp config_pro_template.yaml config_pro.yaml
# 填入钱包私钥（仅本地使用）和API凭证
```

### 常用命令

```bash
# 批量查询
python3 scripts/batch_query.py --chain ethereum --top 50 --export

# 鲸鱼追踪
python3 scripts/whale_tracker.py --token 0x... --chain ethereum --threshold 100000

# 限价交易
python3 scripts/limit_order.py create --token UNIS --side buy --price 6.0 --amount 1000

# 套利扫描
python3 scripts/arb_scanner.py --chains ethereum,bsc,arbitrum

# 安全审计
python3 scripts/security_audit.py --token 0x... --chain ethereum
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+
- **Node.js**: 16+（部分链交互需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| requests | Python库 | 必需 | `pip install requests` |
| web3 | Python库 | 必需 | `pip install web3` |
| eth-account | Python库 | 必需 | `pip install eth-account`（交易签名） |
| pandas | Python库 | 可选 | `pip install pandas`（数据导出） |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| OKX API | `OKX_API_KEY` | 必需 | DEX聚合器接口 |
| OKX Secret | `OKX_API_SECRET` | 必需 | API签名 |
| OKX Passphrase | `OKX_PASSPHRASE` | 必需 | API验证 |
| 钱包私钥 | `WALLET_PRIVATE_KEY` | 交易必需 | 本地签名（不上传） |
| RPC节点 | `ETH_RPC_URL`等 | 推荐 | 自定义RPC节点 |

- 私钥仅存储在本地，用于交易签名，不会上传任何服务器
- API凭证加密存储在本地配置文件

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+链上交互执行）
- **说明**: 专业DEX代币分析与交易工具，支持全链数据与交易执行
- **PRO版特性**: 15+链支持、批量查询、鲸鱼追踪、限价交易、MEV防护、套利识别
- **兼容性**: 完全兼容免费版全部命令与查询接口
- **风险提示**: DeFi交易存在固有风险，请充分了解后再使用交易功能

## 案例展示

### PRO交易配置

```yaml
pro_config:
  api:
    endpoint: "https://www.okx.com/dex-api"
    api_key: "${OKX_API_KEY}"
    api_secret: "${OKX_API_SECRET}"
    passphrase: "${OKX_PASSPHRASE}"

  chains:
    supported: "all"               # 全链支持
    default: ethereum

  trading:
    enabled: true
    wallet:
      private_key: "${WALLET_PRIVATE_KEY}"   # 仅本地存储
      rpc_endpoints:
        ethereum: "${ETH_RPC_URL}"
        bsc: "${BSC_RPC_URL}"
    mev_protection:
      enabled: true
      service: "flashbots"
    slippage:
      default: 0.5%
      max: 3%

  monitoring:
    whale_tracking: true
    min_whale_amount: 100000
    liquidity_alert: true
    alert_channels:
      - console
      - webhook
      - telegram

  batch:
    max_parallel: 10
    export_formats: ["csv", "excel", "json"]
```

## 常见问题

### Q1：交易功能安全吗？

PRO版交易通过本地钱包私钥签名，私钥不会上传任何服务器。同时开启MEV防护（Flashbots）防止抢跑攻击。但DeFi交易固有风险（如智能合约漏洞）无法完全消除。

### Q2：鲸鱼监控如何工作？

PRO版监控链上大额交易，当指定代币出现超过阈值的买卖行为时触发告警。数据来自链上公开交易记录，可追踪任何公开地址的行为。

### Q3：套利扫描支持哪些类型？

支持同一链上不同DEX间的套利（如Uniswap vs SushiSwap）和跨链套利（如以太坊vs Arbitrum）。扫描结果包含预估利润、Gas费用和执行路径。

### Q4：私钥如何存储？

私钥存储在本地配置文件中，建议设置文件权限为600（仅所有者可读写）。PRO版不会将私钥传输至任何外部服务器，所有交易在本地签名后广播。

### Q5：支持多少条链？

PRO版支持15+条主流区块链，包括所有EVM兼容链。新增链支持会通过更新包发布，无需重新安装。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
