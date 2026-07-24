---
name: "tarot-free"
description: "基础版反思式塔罗抽取，支持单牌阵和基础语言校准，用于情感反思。"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "Tarot Free"
  version: "1.0.0"
  summary: "基础版反思式塔罗抽取，支持单牌阵和基础语言校准，用于情感反思。"
  tags:
    - "通用办公"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
---

# Tarot Free

tarot-free 是反思式塔罗抽取基础版。塔罗在这里是镜子，不是预言。它用于意义构建和温和的反思。

## 核心立场

- **Presence-first（临在优先）**：在提供解读前先与使用者同在
- **Non-clinical（非临床化）**：不将普通痛苦医学化

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
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 单牌阵抽取（`Single-card spread`）
用于使用者需要简单锚点的场景。通过内部随机选择 1 张大阿卡纳牌，约 35% 概率出现逆位
（`reversed`）。输出格式：Card（牌名，`upright`/`reversed`）、Keywords（3-5 个关键词）、
Reflection（5-8 行反思，温和语调）、Invitation question（1 行邀请式问题）。
反思语言使用"一种可能的视角是..."而非"你需要..."。

**输入**: 用户提供单牌阵抽取（`Single-card spread`）所需的指令和必要参数。
**处理**: 按照skill规范执行单牌阵抽取（`Single-card spread`）操作,遵循单一意图原则。

### 2. 22 张大阿卡纳牌解读库
内置 0-XXI 共 22 张 `Major Arcana`（大阿卡纳牌）的基础解读。每张牌包含：`Upright keywords`（正位关键词，4 个）、
`Reversed keywords`（逆位关键词，3-4 个）、`Reflection`（反思文本，象征性语调）。
牌号与名称：`0 The Fool`、`I The Magician`、`II The High Priestess`、`III The Empress`、
`IV The Emperor`、`V The Hierophant`、`VI The Lovers`、`VII The Chariot`、`VIII Strength`、
`IX The Hermit`、`X Wheel of Fortune`、`XI Justice`、`XII The Hanged Man`、`XIII Death`、
`XIV Temperance`、`XV The Devil`、`XVI The Tower`、`XVII The Star`、`XVIII The Moon`、
`XIX The Sun`、`XX Judgement`、`XXI The World`。

**输入**: 用户提供22 张大阿卡纳牌解读库所需的指令和必要参数。
**处理**: 按照skill规范执行22 张大阿卡纳牌解读库操作,遵循单一意图原则。
**输出**: 返回22 张大阿卡纳牌解读库的执行结果,包含操作状态和输出数据。

### 3. 基础语言校准
基础版遵循核心语言校准规则。避免使用："You need to..."、"You should..."、"This will happen..."。
偏好使用："One possible lens is..."、"It might be pointing to..."。
解读保持象征性语调，以邀请式问题结尾。基础版不包含完整的语言校准规则集。

**输入**: 用户提供基础语言校准所需的指令和必要参数。
**处理**: 按照skill规范执行基础语言校准操作,遵循单一意图原则。
**输出**: 返回基础语言校准的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`基础语言校准`相关配置参数进行设置
#
## 使用流程

1. 确认使用者意图：情感反思或自我觉察需求
2. 询问使用者是否想分享一个问题，或保持开放
3. 内部随机选择 1 张大阿卡纳牌，约 35% 概率出现逆位
4. 输出：牌名（正位/逆位）、关键词、反思（5-8 行）、邀请式问题
5. 全程使用基础语言校准规则，保持象征性语调

## 示例

### 示例1：单牌阵抽取

```text
使用者：我感觉最近很迷茫，能抽一张牌吗？

输出：
┌─────────────────────────────┐
│  Card: 0 — The Fool (正位)   │
│  Keywords: 新开始、信任、跃步、好奇 │
└─────────────────────────────┘

Reflection:
迷茫有时是新开始的序幕。`The Fool` 正位指向一种站在悬崖边的姿态——
不是无知，而是一种愿意未知道路的好奇。也许此刻的"不知道"本身就是一种准备。
如果你一直等到完全确定才行动，有些可能性可能永远不会展开。
这并不意味着你必须现在就跃步，而是也许可以允许自己"不知道"一会儿。

Invitation question:
如果在迷茫中有一个小小的、不需要确定性的好奇心在萌动，它会指向什么方向？
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 使用者请求医疗建议 | 超出技能边界（non-clinical 原则） | 温和说明塔罗不提供医疗建议，建议咨询专业医疗人员 |
| 使用者请求财务预测 | 超出技能边界（non-predictive 原则） | 说明塔罗是反思工具而非预测工具 |
| 使用者请求法律建议 | 超出技能边界 | 说明塔罗不提供法律指导 |
| 使用者要求确定性预测 | 违反 agency-first 原则 | 重新框架："塔罗不是预言，而是一面镜子。" |
| 使用者询问关于他人的解读 | 违反思辨性边界 | 说明塔罗反思聚焦于使用者自身的内在体验 |

## 常见问题

### Q1: 免费版支持三牌阵吗？
A: 免费版仅支持单牌阵（Single-card spread）。完整版支持三牌阵（Situation/Tension/Next Step），
输出 3 张牌分别对应当前情境、核心张力和可能方向，结尾包含整合段落和邀请式问题。

### Q2: 免费版有安全优先模式吗？
A: 免费版不包含安全优先模式。完整版在检测到使用者表达自伤意图时，立即暂停塔罗抽取并切换到
安全优先支持模式，提供危机资源信息。这是硬性边界，不可被使用者请求覆盖。

### Q3: 免费版的语言校准规则完整吗？
A: 免费版包含基础语言校准规则（避免"You need to..."，偏好"One possible lens is..."）。
完整版包含完整的语言校准规则集，涵盖所有避免用语和偏好用语的详细列表。

### Q4: 免费版可以使用具体问题抽牌吗？
A: 免费版支持可选询问使用者是否想分享问题。但完整版的三牌阵能更好地围绕具体问题展开
结构化反思（情境/张力/下一步），提供更深入的洞察。

### Q5: 如何升级到完整版？
A: 将技能替换为完整版 tarot 即可。完整版包含 6 项核心能力：单牌阵、三牌阵、22 张大阿卡纳
解读库、完整语言校准、边界守护与安全优先、抽牌流程与交互设计。

## 已知限制

- 仅支持单牌阵，不支持三牌阵（Situation/Tension/Next Step）
- 不包含安全优先模式（自伤意图检测和危机资源支持）
- 不包含完整语言校准规则集
- 不包含三牌阵的整合段落输出
- 仅使用 22 张大阿卡纳牌，不包含小阿卡纳牌
- 逆位概率固定为约 35%，无法调整
