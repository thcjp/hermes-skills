---
slug: game-theory
name: game-theory
version: "1.0.0"
displayName: Game Theory
summary: "加密协议与DeFi机制的博弈论分析,评估代币经济模型稳定性与治理攻击风险"
  systems, and stra...
license: MIT
description: |-
  Advanced game theory analysis for crypto protocols, DeFi mechanisms,
  governance systems, and stra。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Lifestyle
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Game Theory for Crypto

Strategic analysis framework for understanding and designing incentive systems in web3.

> "Every protocol is a game. Every token is an incentive. Every user is a player. Understand the rules, or become the played."

## When to Use This Skill

- Analyzing tokenomics for exploits or misaligned incentives
- Evaluating governance proposals and voting mechanisms
- Understanding MEV and adversarial transaction ordering
- Designing auction mechanisms (NFT drops, token sales, liquidations)
- Predicting how rational actors will behave in a system
- Identifying attack vectors in DeFi protocols
- Modeling liquidity provision strategies
- Assessing protocol sustainability

## Core Framework

### The Five Questions

For any protocol or mechanism, ask:

1. **Who are the players?** (Users, LPs, validators, searchers, governance token holders)
2. **What are their strategies?** (Actions available to each player)
3. **What are the payoffs?** (How does each outcome affect each player?)
4. **What information do they have?** (Complete, incomplete, asymmetric?)
5. **What's the equilibrium?** (Where do rational actors end up?)

### Analysis Template

```markdown
## Protocol: [Name]

### Players
- Player A: [Role, objectives, constraints]
- Player B: [Role, objectives, constraints]
- ...

### Strategy Space
- Player A can: [List possible actions]
- Player B can: [List possible actions]

### Payoff Structure
- If (A does X, B does Y): A gets [payoff], B gets [payoff]
- ...

### Information Structure
- Public information: [What everyone knows]
- Private information: [What only some players know]
- Observable actions: [What can be seen on-chain]

### Equilibrium Analysis
- Nash equilibrium: [Stable outcome where no player wants to deviate]
- Dominant strategies: [Strategies that are always best regardless of others]
- Potential exploits: [Deviations that benefit attackers]

### Recommendations
- [Design changes to improve incentive alignment]
```

## Reference Documents

| Document | Use Case |
|----------|----------|
| [Nash Equilibrium](references/nash-equilibrium.md) | Finding stable outcomes in strategic interactions |
| [Mechanism Design](references/mechanism-design.md) | Designing systems with desired equilibria |
| [Auction Theory](references/auction-theory.md) | Token sales, NFT drops, liquidations |
| [MEV Game Theory](references/mev-strategies.md) | Adversarial transaction ordering |
| [Tokenomics Analysis](references/tokenomics-analysis.md) | Evaluating token incentive structures |
| [Governance Attacks](references/governance-attacks.md) | Voting manipulation and capture |
| [Liquidity Games](references/liquidity-games.md) | LP strategies and impermanent loss |
| [Information Economics](references/information-economics.md) | Asymmetric information and signaling |

## Quick Concepts

### Nash Equilibrium
A state where no player can improve their payoff by unilaterally changing strategy. The "stable" outcome of a game.

**Crypto application:** In a staking system, Nash equilibrium determines the stake distribution across validators.

### Dominant Strategy
A strategy that's optimal regardless of what others do.

**Crypto application:** In a second-price auction, bidding your true value is dominant.

### Pareto Efficiency
An outcome where no one can be made better off without making someone worse off.

**Crypto application:** AMM fee structures try to be Pareto efficient for traders and LPs.

### Mechanism Design
"Reverse game theory" - designing rules to achieve desired outcomes.

**Crypto application:** Designing token vesting schedules to align long-term incentives.

### Schelling Point
A solution people converge on without communication.

**Crypto application:** Why certain price levels act as psychological support/resistance.

### Incentive Compatibility
When truthful behavior is optimal for participants.

**Crypto application:** Oracle designs where honest reporting is the dominant strategy.

### Common Knowledge
Everyone knows X, everyone knows everyone knows X, infinitely recursive.

**Crypto application:** Public blockchain state creates common knowledge of balances/positions.

## Analysis Patterns

### Pattern 1: The Tragedy of the Commons

**Structure:** Shared resource, individual incentive to overuse, collective harm.

**Crypto examples:**
- Gas price bidding during congestion
- Governance token voting apathy
- MEV extraction degrading UX

**Solution approaches:**
- Harberger taxes
- Quadratic mechanisms
- Commitment schemes

### Pattern 2: The Prisoner's Dilemma

**Structure:** Individual rationality leads to collective irrationality.

**Crypto examples:**
- Liquidity mining mercenaries (farm and dump)
- Race-to-bottom validator fees
- Bridge security (each chain wants others to secure)

**Solution approaches:**
- Repeated games (reputation)
- Commitment mechanisms (staking/slashing)
- Mechanism redesign

### Pattern 3: The Coordination Game

**Structure:** Multiple equilibria, players want to coordinate but may fail.

**Crypto examples:**
- Which L2 to use?
- Token standard adoption
- Hard fork coordination

**Solution approaches:**
- Focal points (Schelling points)
- Sequential moves (first mover advantage)
- Communication mechanisms

### Pattern 4: The Principal-Agent Problem

**Structure:** One party acts on behalf of another with misaligned incentives.

**Crypto examples:**
- Protocol team vs token holders
- Delegates in governance
- Fund managers

**Solution approaches:**
- Incentive alignment (token vesting)
- Monitoring (transparency)
- Bonding (skin in game)

### Pattern 5: Adverse Selection

**Structure:** Information asymmetry leads to market breakdown.

**Crypto examples:**
- Token launches (team knows more than buyers)
- Insurance protocols (risky users more likely to buy)
- Lending (borrowers know their risk better)

**Solution approaches:**
- Signaling (lock-ups, audits)
- Screening (credit scores, history)
- Pooling equilibria

### Pattern 6: Moral Hazard

**Structure:** Hidden action after agreement leads to risk-taking.

**Crypto examples:**
- Protocols with insurance may take more risk
- Bailout expectations encourage leverage
- Anonymous teams may rug

**Solution approaches:**
- Monitoring and transparency
- Incentive alignment
- Reputation systems

## Common Crypto Games

### The MEV Game

**Players:** Users, searchers, builders, validators
**Key insight:** Transaction ordering is a game; users are often the losers

See: [MEV Strategies](references/mev-strategies.md)

### The Liquidity Game

**Players:** LPs, traders, arbitrageurs
**Key insight:** Impermanent loss is the cost of being adversely selected against

See: [Liquidity Games](references/liquidity-games.md)

### The Governance Game

**Players:** Token holders, delegates, protocol team
**Key insight:** Rational apathy + concentrated interests = capture

See: [Governance Attacks](references/governance-attacks.md)

### The Staking Game

**Players:** Stakers, validators, delegators
**Key insight:** Security budget must exceed attack profit

See: [Tokenomics Analysis](references/tokenomics-analysis.md)

### The Oracle Game

**Players:** Data providers, consumers, attackers
**Key insight:** Profit from manipulation must be less than cost

See: [Mechanism Design](references/mechanism-design.md)

## Red Flags in Protocol Design

### Tokenomics Red Flags
- Insiders can sell before others (vesting asymmetry)
- Inflation benefits few, dilutes many
- No sink mechanisms (perpetual selling pressure)
- Rewards without risk (free money = someone else paying)

### Governance Red Flags
- Low quorum thresholds (minority capture)
- No time delay (flash loan attacks)
- Token voting only (plutocracy)
- Delegates with no skin in game

### Mechanism Red Flags
- First-come-first-served (bot advantage)
- Sealed bids without commitment (frontrunning)
- Rebates/refunds (MEV extraction)
- Complex formulas (hidden exploits)

## Advanced Topics

### Repeated Games and Reputation
Single-shot games often have bad equilibria. Repetition enables cooperation through:
- Trigger strategies (cooperate until defection)
- Reputation building (costly to destroy)
- Future value (patient players cooperate more)

**Crypto application:** Why anonymous actors behave worse than doxxed teams.

### Evolutionary Game Theory
Strategies that survive competitive selection. Relevant for:
- Which protocols survive long-term
- Memetic competition between narratives
- Bot strategy evolution

### Bayesian Games
Games with incomplete information. Players have beliefs about others' types.

**Crypto application:** Trading with unknown counterparties, evaluating anonymous teams.

### Cooperative Game Theory
When players can form binding coalitions.

**Crypto application:** MEV extraction coalitions, validator cartels, governance blocs.

### Algorithmic Game Theory
Computational aspects of game theory.

**Crypto application:** On-chain game computation limits, gas-efficient mechanism design.

## Methodology

### Step 1: Model the Game
- Identify all players (including those not obvious)
- Map complete strategy spaces
- Define payoff functions precisely
- Specify information structure

### Step 2: Find Equilibria
- Check for dominant strategies
- Compute Nash equilibria
- Identify Pareto improvements
- Consider trembling-hand perfection

### Step 3: Stress Test
- What if players collude?
- What if new players enter?
- What if information leaks?
- What if parameters change?

### Step 4: Recommend
- Mechanism changes to improve equilibrium
- Monitoring to detect deviations
- Parameter bounds to maintain stability

## Resources

### Foundational Texts
- "Theory of Games and Economic Behavior" - von Neumann & Morgenstern
- "A Beautiful Mind" (Nash's life, accessible intro)
- "The Strategy of Conflict" - Schelling
- "Mechanism Design Theory" - Myerson (Nobel lecture)

### Crypto-Specific
- "Flash Boys 2.0" - MEV paper
- "SoK: DeFi Attacks" - Systemization of DeFi exploits
- "Clockwork Finance" - MEV and mechanism design
- Paradigm research blog

### Tools
- Nashpy (Python game theory library)
- Gambit (game theory software)
- Agent-based modeling frameworks

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

- Advanced game theory analysis for crypto protocols, DeFi mechanisms,
  governance systems, and stra
- 触发关键词: advanced, analysis, theory, crypto, game

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Game Theory？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Game Theory有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
