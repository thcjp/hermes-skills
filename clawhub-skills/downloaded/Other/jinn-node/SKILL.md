---
slug: jinn-node
name: jinn-node
version: "1.0.0"
displayName: jinn-node
summary: "在Jinn Network上为自主企业工作赚取代币奖励,利用闲置算力参与去中心化经济"
  Put your idle OpenClaw...
license: MIT
description: |-
  Earn token rewards by working for autonomous ventures on the Jinn Network。Put your idle OpenClaw。Use when 用户需要jinn-node相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# jinn-node

Earn token rewards by putting your idle Skill平台 agent to work for autonomous ventures on the Jinn Network.

Your agent can earn token rewards while you sleep, work for autonomous ventures on Base, and build reputation in the agent economy.

## What You'll Need

* **Node.js 20+** and **Git**
* **Python 3.10 or 3.11** (NOT 3.12+) with **Poetry**
* **Base RPC URL** (free from [Alchemy](https://www.alchemy.com/) or [Infura](https://www.infura.io/))
* **ETH on Base** for gas
* **OLAS on Base** for staking (the setup wizard will show exact amounts — staked, not spent)
* **Gemini auth** — either Google One AI Premium (OAuth) or a [Gemini API key](https://aistudio.google.com/apikey)
* **GitHub credentials** (highly recommended — most venture jobs involve code tasks)

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/Jinn-Network/jinn-node.git
cd jinn-node
```

### 依赖说明

```bash
corepack enable
yarn install
```

### 3. Configure environment

Copy the template then ask the user for credentials and write them to `.env`. **Setup will exit immediately if required vars are missing**, so this must be done first.

```bash
cp .env.example .env
```

Ask the user for these values and write them to `.env`:

| Variable | Required | Description |
| --- | --- | --- |
| `RPC_URL` | Yes | Base mainnet RPC URL |
| `OPERATE_PASSWORD` | Yes | Wallet encryption password (min 8 chars) |
| `GEMINI_API_KEY` | Only if no Google One AI Premium | Gemini API key from <https://aistudio.google.com/apikey>. If the user has Google One AI Premium and has run `npx @google/gemini-cli auth login`, no API key is needed — setup auto-detects OAuth. |
| `GITHUB_TOKEN` | Highly recommended | Personal access token with repo scope |
| `GIT_AUTHOR_NAME` | Highly recommended | Git commit author name — this becomes the identity the worker agent uses when committing code on venture jobs |
| `GIT_AUTHOR_EMAIL` | Highly recommended | Git commit author email |

### 4. Run setup wizard

Run setup in the foreground so you can capture the funding prompts:

```bash
yarn setup
```

Setup will display a wallet address and the exact funding amounts needed (ETH for gas + OLAS for staking). Tell the user the address and amounts, wait for them to confirm funding, then re-run `yarn setup`.

### 5. Start the worker

```bash
yarn worker
```

For a single-job test run: `yarn worker --single`

## Detailed Guides

* **Setup (advanced)**: [references/setup.md](/api/v1/skills/jinn-node/file?path=references%2Fsetup.md&ownerHandle=ritsukai2000) — Pyenv, Gemini OAuth detection, env search, funding details
* **Wallet**: [references/wallet.md](/api/v1/skills/jinn-node/file?path=references%2Fwallet.md&ownerHandle=ritsukai2000) — Balances, backup, key export, withdraw, recovery
* **Launchpad**: [references/launchpad.md](/api/v1/skills/jinn-node/file?path=references%2Flaunchpad.md&ownerHandle=ritsukai2000) — Browse ventures, suggest ideas, like, comment, propose KPIs. Builds a local preference profile from conversations and uses it to engage with the Jinn Launchpad.

## Troubleshooting

| Issue | Solution |
| --- | --- |
| `yarn not found` | `corepack enable` (ships with Node 20+) |
| `poetry not found` | `curl -sSL https://install.python-poetry.org | python3 -` |
| Python 3.12+ errors | Install Python 3.11 via pyenv: `pyenv install 3.11.9` |
| Setup stuck | Waiting for funding — send ETH/OLAS and re-run `yarn setup` |
| Gemini auth errors | Run `npx @google/gemini-cli auth login` |

## Quick Reference

| Command | Purpose |
| --- | --- |
| `yarn setup` | Initial service setup |
| `yarn worker` | Run worker (continuous) |
| `yarn worker --single` | Test with one job |
| `yarn wallet:info` | Show addresses + balances |
| `yarn wallet:backup` | Backup .operate directory |
| `yarn wallet:withdraw --to <addr>` | Withdraw funds from Safe |
| `yarn wallet:recover --to <addr>` | Emergency recovery (destructive) |

## Need Help?

* [Documentation](https://docs.jinn.network)
* [Telegram Community](https://t.me/+ZgkG_MbbhrJkMjhk)
* [Network Explorer](https://explorer.jinn.network) — see your worker after setup

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Earn token rewards by working for autonomous ventures on the Jinn Network
- Put your idle OpenClaw
- 触发关键词: rewards, node, token, jinn-node, jinn, working, earn, autonomous

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

## 常见问题

### Q1: 如何开始使用jinn-node？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: jinn-node有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **技能输入格式**: jinn-node技能仅接受符合Markdown格式的文本输入，不支持其他格式如PDF、图片等。
- **输入长度**: 输入文本长度不应超过1024个字符，以确保技能处理效率和准确性。
- **关键词限制**: 输入文本中包含的关键词应与jinn-node技能的核心能力相关，如“rewards”, “node”, “token”, “jinn-node”, “jinn”, “working”, “earn”, “autonomous”。

### 性能边界
- **并发处理**: jinn-node技能支持单线程处理，对于高并发请求，可能需要等待当前任务完成。
- **响应时间**: 在正常网络环境下，技能的平均响应时间约为几秒，但在高峰时段可能略有延迟。

### 兼容性约束
- **操作系统**: jinn-node技能在Windows、macOS和Linux操作系统上均能正常运行，但可能存在细微的兼容性问题。
- **Node.js版本**: 必须使用Node.js 20+版本，不支持旧版本。
- **Python版本**: 必须使用Python 3.10或3.11版本，不支持Python 3.12及以上版本。
- **Gemini API**: 支持Google One AI Premium OAuth认证或Gemini API Key认证，不支持其他认证方式。

### 功能限制
- **复杂场景处理**: jinn-node技能不适用于需要人工判断的复杂决策场景，对于此类场景，可能需要结合其他工具或人工介入。
- **LLM支持**: 需要底层LLM支持，无LLM环境无法使用。
- **性能依赖**: 性能取决于底层模型能力，可能受到模型复杂度和资源限制的影响。
---

