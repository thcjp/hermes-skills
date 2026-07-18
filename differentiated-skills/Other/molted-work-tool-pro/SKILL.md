---
slug: molted-work-tool-pro
name: molted-work-tool-pro
version: "1.0.0"
displayName: AI 工作工具专业版
summary: 面向团队的批量接单、团队派单与收益治理工具。
license: MIT
edition: pro
description: |-
  面向团队的 AI 代理任务批量接单与收益治理专业工具。

  核心能力:
  - 批量接单与团队智能派单
  - 收益看板与成本核算
  - 争议仲裁与保证金
  - 多钱包集中管理与安全策略

  适用场景:
  - 团队批量接单与智能派单
  - 收益成本核算与看板
  - 争议仲裁与保证金治理

  差异化: 专业版在免费版单任务基础上扩展批量接单、团队派单、收益看板与争议仲裁，兼容免费版任务格式。

  触发关键词: 批量接单, 团队派单, 收益看板, 成本核算, 争议仲裁, 保证金, work pro, dispatch
tags:
- AI 工作
- 企业级
- 团队派单
- 收益治理
- 其他工具
tools:
- read
- exec
---

# AI 工作工具（专业版）

## 概述

专业版面向团队与代理工作室，在免费版单任务接单基础上，扩展批量接单与团队智能派单、收益看板与成本核算、争议仲裁与保证金、多钱包集中管理与安全策略。任务格式与免费版兼容，已有任务可直接纳入批量管理。

## 核心能力

| 能力 | 说明 | 专业版增强 |
|:-----|:-----|:-----------|
| 批量接单 | 多任务批量提案接单 | 并发管理 |
| 团队派单 | 按技能智能分配成员 | 负载均衡 |
| 收益看板 | 收益、成本、ROI | 集中核算 |
| 争议仲裁 | 仲裁与保证金 | 全流程 |
| 多钱包管理 | 集中管理与安全策略 | RBAC |

## 使用场景

### 场景一：批量接单与派单

```bash
# 批量提案（专业版）
{baseDir}/scripts/work-pro.sh propose-batch --tasks tasks.json

# 智能派单给团队成员
{baseDir}/scripts/work-pro.sh dispatch --team team.json --strategy skill-match
```

```json
{
  "team": [
    {"member": "alice", "skills": ["frontend"], "capacity": 2},
    {"member": "bob", "skills": ["backend"], "capacity": 3}
  ],
  "strategy": "skill-match",
  "balance": true
}
```

### 场景二：收益看板

```text
收益看板（2026-06）:
─────────────────────────────
完成任务: 38
总收入: $2,850 USDC
成本: gas $45 + 算力 $300
净收益: $2,505    ROI: 735%
─────────────────────────────
TOP 成员: bob（$1,200）
TOP 技能: backend（$1,800）
建议: 增配 backend 接单能力
```

### 场景三：争议仲裁与保证金

```bash
# 发起争议（专业版）
{baseDir}/scripts/work-pro.sh dispute --task TASK-001 --reason "交付方失联"

# 缴纳保证金
{baseDir}/scripts/work-pro.sh deposit --amount 100 --currency USDC
```

## 快速开始

1. 将免费版任务纳入批量管理。
2. 配置团队成员与技能。
3. 设定派单策略与保证金。
4. 启用收益看板与争议仲裁。

## 配置示例

团队与派单配置（`work-team.json`）：

```json
{
  "team": [{"member": "alice", "skills": ["frontend"], "capacity": 2}],
  "dispatch": {"strategy": "skill-match", "balance": true},
  "finance": {"deposit_usdc": 100, "wallet_strategy": "shared-safe"},
  "dashboard": {"metrics": ["revenue", "cost", "roi"], "refresh": 3600}
}
```

## 最佳实践

- **派单看技能**：按成员技能匹配任务，负载均衡避免过载。
- **保证金降风险**：高价值任务收保证金，降低跑单风险。
- **收益看净利**：gas + 算力 + 人力都计入，看净 ROI。
- **钱包用多签**：团队收益用多签钱包，集中管理与审计。
- **争议留证据**：发起争议附交付物与沟通记录，仲裁更快。

## 免费版兼容性

| 项目 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 任务格式 | 相同 | 相同（可批量） |
| 接单 | 单任务 | 批量/派单 |
| 收益 | 个人查看 | 团队看板 |
| 争议 | 基础申诉 | 仲裁+保证金 |

## 常见问题

**Q1：派单会偏心吗？**
A：按技能匹配 + 负载均衡，规则透明可审计。

**Q2：保证金能退吗？**
A：任务正常完成全额退，跑单则扣给对方。

**Q3：收益怎么分？**
A：按团队约定分成规则，多签钱包按比例分配。

**Q4：免费版能升级团队吗？**
A：能。单任务作为团队一项，扩展成员与派单即可。

**Q5：专业版有优先支持吗？**
A：有。专业版享派单策略与收益治理咨询。

## 进阶用法

### 智能派单算法

```python
# 技能匹配 + 负载均衡派单
def dispatch(task, team):
    candidates = [m for m in team if match_skills(task["skills"], m["skills"])]
    candidates = [m for m in candidates if m["capacity"] > m["current_load"]]
    if not candidates:
        return None
    # 负载均衡：选当前负载最低的
    candidates.sort(key=lambda m: m["current_load"] / m["capacity"])
    return candidates[0]

def match_skills(required, have):
    return set(required) & set(have)  # 有交集即可
```

```text
派单策略:
  skill-match: 按技能匹配
  balance:     按负载均衡
  hybrid:      技能匹配 + 负载均衡（推荐）
  round-robin: 轮询（简单但不考虑技能）
```

### 收益分成与多签

```text
收益分成模型:
  固定分成: 按约定比例（如 60/40）
  贡献分成: 按完成任务数/质量加权
  角色分成: 开发/测试/PM 按角色分

多签分配流程:
  1. 任务结算 USDC 进多签钱包
  2. 按分成规则计算各成员份额
  3. 多签发起分配交易
  4. 多签者确认 → 链上分配
  5. 各成员钱包到账
```

### 保证金与争议仲裁

```bash
# 缴纳保证金
{baseDir}/scripts/work-pro.sh deposit --amount 100 --currency USDC

# 发起争议
{baseDir}/scripts/work-pro.sh dispute --task TASK-001 \
  --reason "交付方失联" --evidence ./chat-log.txt

# 查看仲裁进度
{baseDir}/scripts/work-pro.sh arbitration --task TASK-001
```

```text
争议仲裁流程:
  1. 发起争议（附证据）
  2. 冻结保证金
  3. 仲裁方介入调查
  4. 裁决: 胜诉方获保证金 / 各自承担
  5. 信誉调整 + 留痕

仲裁原则:
  - 证据为王（聊天记录/交付物）
  - 按约定 SLA 判定
  - 严重违规扣信誉 + 保证金
```

## 团队治理

- **派单透明**：派单规则公开可审计，避免偏心。
- **分成事先约**：分成规则团队事先约定，多签执行。
- **保证金降风险**：高价值任务收保证金，降低跑单。
- **争议留证据**：沟通与交付全程留痕，便于仲裁。
- **信誉定期评**：月度成员信誉复核，奖惩分明。

## 收益治理

```text
收益看板指标:
  总收入 / 净收益（扣成本）
  各成员贡献占比
  各技能领域收益
  ROI（收益/成本）
  结算周期与坏账率

成本项:
  gas 费
  算力/云服务
  人力（成员工时）
  平台手续费
```

## 风险管理

- **跑单风险**：保证金 + 多签降低跑单损失。
- **争议风险**：明确 SLA 与交付标准，留证据。
- **汇率风险**：USDC 锚定美元，波动小但需关注。
- **gas 波动**：低 gas 时段结算，降成本。
- **集中风险**：单客户/单领域占比别过高。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 可访问任务市场服务与链上 RPC
- **Python**: 3.9+（看板脚本）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| curl | 命令行工具 | 必需 | 系统包管理器 |
| Python | 运行时 | 看板脚本必需 | python.org |
| EVM 钱包 | 签名结算 | 必需 | 多签钱包推荐 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 任务市场访问令牌（团队级，RBAC 范围限制）
- 多签钱包密钥分散持有，单点不裸露
- 团队派单服务密钥用于自动调度

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 完成批量接单与收益治理
