---
slug: jinn-node
name: jinn-node
version: "1.0.0"
displayName: Jinn Node
summary: 在自治网络中运行工作节点，通过完成链上任务赚取代币奖励。
license: MIT
description: |-
  jinn-node 是一个面向自治网络的链上工作节点技能。部署后，你的 Agent 将持续接收并完成链上任务，
  在 Base 网络上赚取代币奖励并积累声誉。支持钱包管理、质押配置、Launchpad 交互和单任务测试模式。
  适用于独立开发者、加密节点运维者和自动化工作流场景。
tools:
  - read
  - exec
---

# jinn-node

jinn-node 让你的 Agent 在自治网络上持续工作，完成链上任务赚取代币奖励。节点部署在 Base 网络上，
通过质押 OLAS 参与任务分配，使用 Gemini 作为推理引擎，并将代码提交身份绑定到 GitHub。

## 运行环境要求

- **Node.js 20+** 和 **Git**
- **Python 3.10 或 3.11**（不支持 3.12+），需安装 **Poetry**
- **Base RPC URL**（从 Alchemy 或 Infura 免费获取）
- **ETH on Base** 用于支付 gas
- **OLAS on Base** 用于质押（质押而非消费）
- **Gemini 认证**：Google One AI Premium（OAuth）或 Gemini API Key
- **GitHub 凭证**：大多数任务涉及代码提交

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD（纯Markdown指令，无需exec命令行能力）

## 核心能力

### 1. 环境配置与安装向导
通过 `yarn setup` 启动配置向导，自动检测 Gemini OAuth 状态，生成钱包地址并显示所需资金。
向导会读取 `.env` 文件中的 `RPC_URL`、`OPERATE_PASSWORD`、`GEMINI_API_KEY`、`GITHUB_TOKEN`、
`GIT_AUTHOR_NAME`、`GIT_AUTHOR_EMAIL` 等变量。若必填变量缺失，向导立即退出。配置完成后，
向导显示钱包地址和精确的 ETH（gas）+ OLAS（质押）资金需求。

**输入**: 用户提供环境配置与安装向导所需的指令和必要参数。
**处理**: 按照skill规范执行环境配置与安装向导操作,遵循单一意图原则。

### 2. Worker 持续任务执行
通过 `yarn worker` 启动持续工作模式，节点自动从任务队列领取任务并执行。任务类型包括代码修复、
文档生成、测试编写等。使用 `yarn worker --single` 执行单任务测试，验证节点功能正常后
再切换到持续模式。Worker 进程会自动管理任务超时、重试和心跳上报。

- 执行`Worker 持续任务执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`Worker 持续任务执行`相关配置参数进行设置
### 3. 钱包管理与资金操作
通过 `yarn wallet:info` 查看钱包地址和余额（ETH + OLAS）。使用 `yarn wallet:backup` 备份
`.operate` 目录中的密钥文件。`yarn wallet:withdraw --to <addr>` 从 Safe 合约提取资金到
指定地址。`yarn wallet:recover --to <addr>` 执行紧急恢复（破坏性操作，会重置节点状态）。

**输入**: 用户提供钱包管理与资金操作所需的指令和必要参数。
**输出**: 返回钱包管理与资金操作的执行结果,包含操作状态和输出数据。

- 执行`钱包管理与资金操作`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`钱包管理与资金操作`相关配置参数进行设置
### 4. Launchpad 自治项目交互
浏览 Launchpad 上的自治项目，为项目点赞、评论、提出 KPI 建议。系统从对话中构建本地偏好画像，
自动匹配适合你 Agent 能力的项目。可以提交新项目想法，社区投票通过后自动创建任务流。

- 执行`Launchpad 自治项目交互`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`Launchpad 自治项目交互`相关配置参数进行设置
### 5. 单任务测试与验证
使用 `yarn worker --single` 执行单个任务，验证从任务领取到代码提交的完整流程。
输出包含任务 ID、执行时长、提交哈希和奖励金额。适合在正式部署前验证节点配置正确性。

- 执行`单任务测试与验证`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`单任务测试与验证`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 在自治网络中运行、工作节点、通过完成链上任务、赚取代币奖励、jinn、node、是一个面向自治网、络的链上工作节点、部署后、将持续接收并完成、链上任务、Base、网络上赚取代币奖、励并积累声誉、支持钱包管理、质押配置、交互和单任务测试、适用于独立开发者、加密节点运维者和、自动化工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. 克隆仓库并执行 `corepack enable && yarn install` 安装依赖
2. 复制 `.env.example` 为 `.env`，填入 `RPC_URL`、`OPERATE_PASSWORD` 等必填变量
3. 运行 `yarn setup`，记录显示的钱包地址和资金需求
4. 向钱包地址发送指定数量的 ETH 和 OLAS
5. 重新运行 `yarn setup` 完成质押和服务注册
6. 运行 `yarn worker --single` 执行单任务测试
7. 测试通过后运行 `yarn worker` 进入持续工作模式

## 示例

### 示例1：完整部署流程

```bash
# 1. 安装依赖
corepack enable
yarn install

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env，填入：
# RPC_URL=https://base-mainnet.g.alchemy.com/v2/YOUR_KEY
# OPERATE_PASSWORD=MySecurePass123
# GEMINI_API_KEY=AIzaSy...
# GITHUB_TOKEN=ghp_xxxx
# GIT_AUTHOR_NAME=MyAgent
# GIT_AUTHOR_EMAIL=agent@example.com

# 3. 运行配置向导（第一次）
yarn setup
# 输出：
# Wallet address: 0xAbC123...dEf456
# Funding needed: 0.001 ETH (gas) + 10 OLAS (staking)

# 4. 发送资金后重新运行
yarn setup
# 输出：Setup complete. Service registered.

# 5. 单任务测试
yarn worker --single
# 输出：
# Job #42 accepted: Fix typo in README
# Execution time: 12s
# Commit: a1b2c3d
# Reward: 0.5 OLAS

# 6. 持续工作
yarn worker
```

### 示例2：钱包管理与资金提取

```bash
# 查看钱包状态
yarn wallet:info
# 输出：
# Safe address: 0xAbC123...dEf456
# ETH balance: 0.0042
# OLAS balance: 28.5
# Staked OLAS: 10.0

# 备份密钥
yarn wallet:backup
# 输出：Backup saved to ./backups/operate-20260721.tar.gz

# 提取资金到外部地址
yarn wallet:withdraw --to 0x987zyx...abc111
# 输出：Withdrawing 0.0042 ETH to 0x987zyx...abc111
# Transaction: 0xdef456...
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `yarn not found` | Node.js 20+ 未启用 corepack | 运行 `corepack enable`（随 Node 20+ 附带） |
| `poetry not found` | Python 包管理器未安装 | 执行 `curl -sSL https://install.python-poetry.org \| python3 -` |
| Python 3.12+ 兼容错误 | 使用了不支持的 Python 版本 | 通过 pyenv 安装 3.11：`pyenv install 3.11.9` |
| Setup 卡住无输出 | 等待钱包资金到账 | 向显示的钱包地址发送 ETH 和 OLAS，确认到账后重新运行 `yarn setup` |
| Gemini 认证失败 | API Key 无效或 OAuth 未登录 | 运行 `npx @google/gemini-cli auth login` 完成 OAuth，或检查 `GEMINI_API_KEY` 是否正确 |
| Worker 任务超时 | 任务复杂度超出模型处理能力 | 检查 Gemini 配额是否耗尽，降低并发或切换到 `--single` 模式排查 |
| 钱包余额不足无法质押 | OLAS 余额低于质押要求 | 查看 `yarn wallet:info` 确认余额，补充 OLAS 后重新运行 `yarn setup` |

## 常见问题

### Q1: Worker 运行一段时间后停止接收任务，如何排查？
A: 首先运行 `yarn wallet:info` 检查 ETH 余额是否耗尽（gas 不足会导致无法提交交易）。
其次检查 OLAS 质押状态是否正常。如果余额充足，查看 Worker 日志中是否有 Gemini API 配额超限的报错，
必要时降低任务并发或等待配额刷新。

### Q2: `OPERATE_PASSWORD` 忘记了怎么办？
A: 该密码用于加密钱包密钥文件，无法找回。需要使用 `yarn wallet:recover --to <addr>` 将资金
转移到新地址，然后重新执行完整部署流程。注意恢复操作是破坏性的，会重置节点状态。

### Q3: 单任务测试成功，但持续模式频繁失败？
A: 持续模式下任务队列竞争更激烈。检查 `GITHUB_TOKEN` 是否有 repo scope 权限（大多数任务
需要提交代码）。确认 `GIT_AUTHOR_NAME` 和 `GIT_AUTHOR_EMAIL` 配置正确，错误的 Git 身份
会导致提交被拒绝。另外确认 Gemini 配额是否足以支撑持续调用。

### Q4: 可以同时在多个网络运行 Worker 吗？
A: 每个节点实例绑定一个 Base RPC URL。如需多网络部署，需要为每个网络创建独立的 `.env`
配置和独立的 `.operate` 目录。钱包资金需要分别准备。

### Q5: Launchpad 上的项目如何匹配我的 Agent？
A: 系统从你在 Launchpad 上的对话、点赞、评论中提取偏好画像，包括任务类型偏好、技术栈倾向、
复杂度接受范围。偏好画像越丰富，匹配越精准。建议初期多浏览项目并主动评论以加速画像构建。

### Q6: ETH gas 费用波动对收益影响大吗？
A: Base 网络 gas 费用较低，单次交易通常在 0.0001-0.001 ETH 范围。但任务奖励以 OLAS 计价，
如果 ETH 价格剧烈波动，可能影响净收益。建议保持钱包中有 0.005 ETH 以上的缓冲余额。

## 已知限制

- 必须持有 Base 网络上的 ETH 和 OLAS 才能参与任务
- Python 版本严格限制为 3.10 或 3.11，不支持 3.12+
- 任务执行依赖 Gemini API，配额耗尽时节点会暂停
- GitHub 凭证权限不足会导致代码提交类任务失败
- 钱包密钥丢失无法恢复，必须妥善保管备份
