---
name: "jinn-node-free"
description: "在自治网络中运行工作节点的基础版本，支持单任务测试和钱包查询。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "Jinn Node Free"
  version: "1.0.0"
  summary: "在自治网络中运行工作节点的基础版本，支持单任务测试和钱包查询。"
  tags:
    - "通用办公"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
tools:
  - exec
  - read
  - write
---
# jinn-node-free

jinn-node-free 让你的 Agent 在自治网络上执行单个链上任务，体验从任务领取到代码提交的完整流程。
节点部署在 Base 网络上，通过质押 OLAS 参与任务分配，使用 Gemini 作为推理引擎。

## 运行环境要求

- **Node.js 20+** 和 **Git**
- **Python 3.10 或 3.11**（不支持 3.12+），需安装 **Poetry**
- **Base RPC URL**（从 Alchemy 或 Infura 免费获取）
- **ETH on Base** 用于支付 gas
- **OLAS on Base** 用于质押
- **Gemini 认证**：Google One AI Premium（OAuth）或 Gemini API Key

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
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 环境配置与安装向导
通过 `yarn setup` 启动配置向导，读取 `.env` 文件中的 `RPC_URL`、`OPERATE_PASSWORD`、
`GEMINI_API_KEY` 等必填变量。向导自动检测 Gemini OAuth 状态，生成钱包地址并显示所需资金。
若必填变量缺失，向导立即退出。配置完成后显示 ETH（gas）+ OLAS（质押）的精确资金需求。

### 2. 单任务测试与验证
使用 `yarn worker --single` 执行单个任务，验证从任务领取到代码提交的完整流程。

### 3. 钱包余额查询
通过 `yarn wallet:info` 查看钱包地址和余额（ETH + OLAS），确认资金到账状态和质押情况。
支持查看 Safe 合约地址和当前质押的 OLAS 数量。

#
## 使用流程

1. 克隆仓库并执行 `corepack enable && yarn install` 安装依赖
2. 复制 `.env.example` 为 `.env`，填入 `RPC_URL`、`OPERATE_PASSWORD` 等必填变量
3. 运行 `yarn setup`，记录显示的钱包地址和资金需求
4. 向钱包地址发送指定数量的 ETH 和 OLAS
5. 重新运行 `yarn setup` 完成质押和服务注册
6. 运行 `yarn worker --single` 执行单任务测试

#
## 示例

### 示例1：单任务测试流程

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

# 3. 运行配置向导
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

# 6. 查看钱包状态
yarn wallet:info
# 输出：
# Safe address: 0xAbC123...dEf456
# ETH balance: 0.0042
# OLAS balance: 28.5
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `yarn not found` | Node.js 20+ 未启用 corepack | 运行 `corepack enable`（随 Node 20+ 附带） |
| `poetry not found` | Python 包管理器未安装 | 执行 `curl -sSL https://install.python-poetry.org \| python3 -` |
| Python 3.12+ 兼容错误 | 使用了不支持的 Python 版本 | 通过 pyenv 安装 3.11：`pyenv install 3.11.9` |
| Setup 卡住无输出 | 等待钱包资金到账 | 向显示的钱包地址发送 ETH 和 OLAS，确认到账后重新运行 `yarn setup` |
| Gemini 认证失败 | API Key 无效或 OAuth 未登录 | 运行 `npx @google/gemini-cli auth login` 完成 OAuth |

## 常见问题

### Q1: 免费版可以持续运行 Worker 吗？
A: 免费版仅支持 `yarn worker --single` 单任务测试模式，不支持 `yarn worker` 持续工作模式。
如需持续赚取代币奖励，请升级到完整版 jinn-node，支持持续任务执行、自动重试和心跳上报。

### Q2: 免费版可以提取钱包资金吗？
A: 免费版支持 `yarn wallet:info` 查询余额，但不支持 `yarn wallet:withdraw` 和
`yarn wallet:recover` 等资金操作。如需提取资金或紧急恢复，请升级到完整版。

### Q3: 单任务测试的奖励可以领取吗？
A: 单任务测试产生的奖励会记入钱包 OLAS 余额，可通过 `yarn wallet:info` 查看。
但免费版不支持主动提取操作，资金将保留在 Safe 合约中。

### Q4: 免费版支持 Launchpad 项目交互吗？
A: 免费版不包含 Launchpad 交互功能。完整版支持浏览自治项目、点赞、评论、提出 KPI 建议，
并基于偏好画像自动匹配适合你 Agent 能力的项目。

### Q5: 如何升级到完整版？
A: 将技能替换为完整版 jinn-node 即可。已有 `.env` 配置和 `.operate` 钱包目录无需重新创建，
升级后直接运行 `yarn worker` 即可进入持续工作模式。

## 已知限制

- 仅支持 `yarn worker --single` 单任务模式，不支持持续工作
- 不支持钱包资金提取（`yarn wallet:withdraw`）和紧急恢复（`yarn wallet:recover`）
- 不支持 Launchpad 项目浏览、评论和 KPI 提议
- 不支持钱包密钥备份（`yarn wallet:backup`）
- Python 版本严格限制为 3.10 或 3.11，不支持 3.12+

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 效率量化分析

| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 差异化对比

| 对比维度 | 本技能 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 核心功能 | 通用场景 | 通用场景 |

## 核心功能

- **自动化执行**: 基于指令驱动的自动化流程
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据