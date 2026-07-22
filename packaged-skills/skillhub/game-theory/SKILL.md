---
slug: "game-theory"
name: "game-theory"
version: "1.0.0"
displayName: "加密协议博弈论分析"
summary: "面向crypto协议、DeFi机制和治理系统的博弈论分析框架，识别Nash Equilibrium与MEV风险"
license: "Proprietary"
description: |-
  面向加密协议、DeFi机制和治理系统的博弈论分析框架。
  基于Five Questions分析模型，覆盖Nash Equilibrium、Dominant Strategy、Mechanism Design等核心概念，
  支持MEV Game、Liquidity Game、Governance Game等常见crypto博弈场景分析，
  并提供Tokenomics、Governance、Mechanism三维度Red Flags检测。
  适用于协议设计审计、激励对齐评估与攻击向量识别。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 生活服务
---
# 加密协议博弈论分析

面向web3协议的激励系统设计与博弈论分析框架，用于识别Nash Equilibrium、评估MEV风险与治理攻击向量。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Bash/Shell | 运行时 | 可选 | 用于执行分析脚本 |
| Nashpy | Python库 | 可选 | `pip install nashpy` 用于Nash Equilibrium计算 |
| Gambit | 软件 | 可选 | 用于博弈论建模与求解 |

### API Key 配置
- 本Skill基于指令驱动，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行博弈论分析任务

## 核心能力

### Five Questions分析框架

对任意协议或机制，通过五个核心问题建模博弈：
1. **Who are the players?**（玩家识别：Users、LPs、validators、searchers、governance token holders）
2. **What are their strategies?**（策略空间：每个玩家可执行的动作集合）
3. **What are the payoffs?**（收益结构：每种结果对各方的影响）
4. **What information do they have?**（信息结构：Complete / Incomplete / Asymmetric Information）
5. **What's the equilibrium?**（均衡分析：理性参与者的最终收敛点）

输出标准Analysis Template包含Players、Strategy Space、Payoff Structure、Information Structure、Equilibrium Analysis、Recommendations六个章节。

### 核心博弈论概念应用
| 概念 | 定义 | Crypto应用场景 |
|:-----|:-----|:---------------|
| Nash Equilibrium | 没有玩家能通过单方面改变策略而改善收益的状态 | Staking系统中validator的stake分布均衡 |
| Dominant Strategy | 无论他人如何行动都是最优的策略 | Second-price auction中真实报价是Dominant Strategy |
| Pareto Efficiency | 无法在不损害他人的前提下使某人更好的状态 | AMM fee结构对traders和LPs的Pareto效率 |
| Mechanism Design | "逆向博弈论"——设计规则以达成期望均衡 | Token vesting schedule的长期激励对齐设计 |
| Schelling Point | 无沟通情况下人们收敛到的解 | 价格水平的心理支撑/阻力位 |
| Incentive Compatibility | 诚实行为对参与者最优的状态 | Oracle设计中诚实报告为Dominant Strategy |
| Common Knowledge | 所有人知道X，所有人知道所有人知道X，无限递归 | 公链状态创建balances/positions的Common Knowledge |

**输入**: 用户提供核心博弈论概念应用所需的指令和必要参数。
**处理**: 按照skill规范执行核心博弈论概念应用操作,遵循单一意图原则。### 六大分析模式

支持识别并分析六种经典博弈模式，每种均提供crypto实例与解决方案：

1. **Tragedy of the Commons**（公地悲剧）：Gas price竞价、governance投票冷漠、MEV提取降低UX；解决方案含Harberger taxes、Quadratic mechanisms、Commitment schemes
2. **Prisoner's Dilemma**（囚徒困境）：Liquidity mining mercenaries（farm and dump）、validator费用竞底、bridge安全搭便车；解决方案含Repeated games、Commitment mechanisms（staking/slashing）
3. **Coordination Game**（协调博弈）：L2选择、token标准采用、hard fork协调；解决方案含Focal points（Schelling points）、Sequential moves、Communication mechanisms
4. **Principal-Agent Problem**（委托代理问题）：Protocol team vs token holders、governance delegates、fund managers；解决方案含Incentive alignment、Monitoring、Bonding
5. **Adverse Selection**（逆向选择）：Token launches、insurance protocols、lending；解决方案含Signaling、Screening、Pooling equilibria
6. **Moral Hazard**（道德风险）：带保险的协议冒险、bailout预期、anonymous teams rug；解决方案含Monitoring、Incentive alignment、Reputation systems

### Common Crypto Games分析
针对五种crypto原生博弈提供专门分析能力：

- **MEV Game**：玩家为Users、searchers、builders、validators；核心洞察为transaction ordering是博弈，users常为输家
- **Liquidity Game**：玩家为LPs、traders、arbitrageurs；核心洞察为impermanent loss是adverse selection的代价
- **Governance Game**：玩家为token holders、delegates、protocol team；核心洞察为rational apathy + concentrated interests = capture
- **Staking Game**：玩家为stakers、validators、delegators；核心洞察为security budget必须超过attack profit
- **Oracle Game**：玩家为data providers、consumers、attackers；核心洞察为操纵收益必须小于操纵成本

**输出**: 返回Common Crypto Games分析的执行结果,包含操作状态和输出数据。
### Red Flags检测
提供三维度协议设计风险检测：

- **Tokenomics Red Flags**：insiders vesting不对称、inflation稀释、无sink机制、reward无risk
- **Governance Red Flags**：quorum过低、无timelock（flash loan攻击）、token voting only（plutocracy）、delegates无skin in game
- **Mechanism Red Flags**：first-come-first-served（bot优势）、sealed bid无commitment（frontrunning）、rebates（MEV提取）、复杂公式（隐藏漏洞）

**输出**: 返回Red Flags检测的执行结果,包含操作状态和输出数据。
### 高级分析能力
支持四类高级博弈论主题的深入分析：

- **Repeated Games and Reputation**：单次博弈均衡差，重复博弈通过Trigger strategies、Reputation building、Future value促成合作；解释anonymous actors行为更差
- **Evolutionary Game Theory**：策略竞争选择；分析哪些协议长期存活、narrative竞争、bot策略进化
- **Bayesian Games**：不完全信息博弈；分析未知对手方交易、anonymous team评估
- **Cooperative Game Theory**：可形成binding coalitions的博弈；分析MEV extraction coalitions、validator cartels、governance blocs

#
## 使用流程

1. **确定分析目标**：明确要分析的协议或机制（DeFi协议、governance提案、tokenomics设计等）
2. **应用Five Questions框架**：识别players、strategies、payoffs、information、equilibrium
3. **选择分析模式**：从六大Pattern中匹配最贴切的博弈结构
4. **识别Common Crypto Games**：判断属于MEV / Liquidity / Governance / Staking / Oracle哪类博弈
5. **运行Red Flags检测**：对Tokenomics、Governance、Mechanism三维度进行风险扫描
6. **进行高级分析**：按需调用Repeated Games、Bayesian Games等高级分析能力
7. **输出Recommendations**：给出mechanism改进、monitoring建议、parameter bounds

#
## 示例

### 示例1：DeFi借贷协议的Principal-Agent分析

```
分析目标: 某 lending protocol 的清算机制
Step 1 - Players:
  - Borrowers（目标：最小化清算损失）
  - Liquidators（目标：最大化清算利润）
  - Protocol（目标：维持偿付能力）
Step 2 - 分析模式匹配: Principal-Agent Problem
  - Principal = Protocol，Agent = Liquidators
  - 信息不对称：Liquidators比Protocol更早感知抵押率变化
Step 3 - Red Flags检测:
  - Mechanism Red Flag: first-come-first-served清算 → bot优势
  - 无commitment机制 → 可frontrunning
Step 4 - Recommendations:
  - 引入Dutch auction清算机制
  - 添加清算延迟（timelock）
  - 设置清算奖励上限
```

### 示例2：治理提案的Governance Game分析

```
分析目标: 某 DAO 的治理投票提案是否易被capture
Step 1 - Players:
  - Token holders（rational apathy，参与率低）
  - Large delegates（concentrated interests）
  - Protocol team（信息优势）
Step 2 - Common Crypto Game: Governance Game
  - 核心洞察: rational apathy + concentrated interests = capture
Step 3 - Red Flags检测:
  - Governance Red Flags:
    * Quorum threshold 仅 5% → minority capture风险
    * 无timelock → flash loan攻击可能
    * Token voting only → plutocracy
Step 4 - 高级分析:
  - Bayesian Games: 分析delegate与voter间的信息不对称
  - Cooperative Game Theory: 识别voting blocs形成的可能
Step 5 - Recommendations:
  - 提高quorum至15-20%
  - 添加timelock（至少48小时）
  - 引入quadratic voting或conviction voting
  - 要求delegates bonding（skin in game）
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 无法识别players | 协议参与者角色不清晰 | 检查on-chain合约与文档，补充隐式参与者（如searchers、arbitrageurs） |
| Nash Equilibrium不收敛 | 策略空间连续或博弈无限重复 | 使用Nashpy库进行数值求解，或转为离散策略空间近似 |
| 误判博弈模式 | 协议同时具有多种博弈特征 | 优先识别dominant特征，对次要特征单独分析后综合 |
| Red Flags漏报 | 仅检查单维度风险 | 强制对Tokenomics、Governance、Mechanism三维度逐一扫描 |
| MEV分析偏差 | 未考虑builder-validator关系 | 补充Proposer-Builder Separation（PBS）视角，分析searcher-builder纵向关系 |
| Incentive Compatibility验证失败 | 诚实行为非最优策略 | 重新设计reward/penalty结构，引入slashing或bonding机制 |

## 常见问题

### Q1: 这个Skill适用于分析哪些类型的协议？
A: 适用于所有web3协议的博弈论分析，包括DeFi借贷、AMM、staking、governance、oracle、MEV相关协议。特别适合分析tokenomics设计、激励对齐、攻击向量识别与机制设计审计。

### Q2: 如何判断一个协议是否存在MEV风险？
A: 通过MEV Game分析框架，检查transaction ordering是否可被操纵、是否存在first-come-first-served机制、sealed bid是否有commitment。若存在rebates/refunds机制，通常伴随MEV提取。

### Q3: Nash Equilibrium在实际协议分析中如何应用？
A: 先建模players和strategies，定义payoff functions，然后检查是否存在Dominant Strategy。若无dominant strategy，计算Nash Equilibrium。对于staking系统，Nash Equilibrium决定validator的stake分布。

### Q4: Red Flags检测发现多个风险点如何优先级排序？
A: 按攻击成本与影响排序：governance capture（flash loan攻击）> tokenomics vesting不对称 > mechanism的frontrunning风险。优先修复攻击成本最低、影响最大的风险点。

### Q5: 是否需要Nashpy或Gambit等外部工具？
A: 基础分析无需外部工具，Agent可通过Markdown指令完成定性分析。涉及复杂数值求解（如连续策略空间的Nash Equilibrium计算）时，可选用Nashpy（`pip install nashpy`）或Gambit进行辅助计算。

### Q6: 如何分析anonymous team的协议风险？
A: 使用Bayesian Games框架分析信息不对称，结合Repeated Games理论——anonymous actors因无reputation成本，行为通常比doxxed teams更差。重点检查Moral Hazard风险与rug可能性。

## 已知限制

- 定性分析为主，复杂博弈的精确数值求解需依赖Nashpy/Gambit等外部工具
- 无法实时获取on-chain数据，需用户提供协议参数与合约信息
- Evolutionary Game Theory的长期预测具有不确定性，narrative竞争难以精确建模
- Bayesian Games的belief建模依赖用户输入，无法自动推断对手方类型分布
- 不替代正式的安全审计，仅提供博弈论视角的风险评估
