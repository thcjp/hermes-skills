---
slug: "solo-validate"
name: "solo-validate"
version: 2.1.2
displayName: "Validate"
summary: "用S.E.E.D.利基检查与STREAM六层分析给创业点子打分。Score startup idea through S。E。Use when 用户需要Validate相关功能时使用。不适用"
license: "Proprietary"
description: |-
  Score startup idea through S。E。Use when 用户需要Validate相关功能时使用。不适用于超出本技能能力范围的复杂需求。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求.
tags:
  - Research
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - 开发
  - 代码
  - 知识
  - stream
  - devil
  - advocate
  - api
  - 不支持
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"
---
# Validate

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| ValidateSTREAM六层分析 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 核心能力

- Score startup idea through S.E.E.D. niche validation
- Niche check + STREAM 6-layer analysis
- Devil's Advocate investgation (反方论证压力测试)

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## S.E.E.D. 利基检查框架

S.E.E.D. 是对创业点子进行市场利基验证的四维框架，每个维度按 0-10 分打分：

| 维度 | 全称 | 核心问题 | 评分标准 |
|:-----|:-----|:------|:------|
| **S** | Search Demand | 用户是否在主动搜索解决方案？ | 0=无人搜索, 10=高搜索量低竞争 |
| **E** | Entry Barrier | 进入门槛是否合理？ | 0=门槛过高无法启动, 10=门槛适中可快速验证 |
| **E** | Expansion Path | 是否有清晰的扩展路径？ | 0=单一场景无法扩展, 10=多场景多市场可扩展 |
| **D** | Defensibility | 能否建立防御壁垒？ | 0=无壁垒极易被复制, 10=有网络效应/数据壁垒/专利 |

**利基评分计算**: `S.E.E.D. Score = (S + E + E + D) / 4`，总分 ≥ 7.0 为值得深入验证的点子。

## STREAM 六层分析法

STREAM 是对创业点子进行深度结构化分析的多层框架：

| 层级 | 名称 | 分析内容 | 关键产出 |
|:-----|:-----|:------|:------|
| **S** | Surface | 表面市场概况：TAM/SAM/SOM估算 | 市场规模量化 |
| **T** | Target | 目标用户画像与痛点深度访谈模拟 | 用户画像与痛点优先级 |
| **R** | Revenue | 商业模式与收入结构分析 | 定价策略与收入预测 |
| **E** | Execution | 执行路径与MVP定义 | 最小可行产品规格 |
| **A** | Advantage | 竞争优势与差异化分析 | 竞品对比矩阵 |
| **M** | Market | 市场时机与趋势分析 | 时机评分与趋势图谱 |

## Devil's Advocate 反方论证

在 S.E.E.D. 和 STREAM 分析完成后，执行 Devil's Advocate 压力测试，从以下角度对点子进行攻击性质疑：

1. **市场否定**: "这个市场可能根本不存在，用户说的需求未必是真实付费意愿"
2. **竞争否定**: "巨头一旦入场，你没有任何还手之力"
3. **执行否定**: "你缺乏该领域的关键经验和资源"
4. **时机否定**: "市场太早（教育成本高）或太晚（格局已定）"
5. **模式否定**: "收入模型无法覆盖获客成本，LTV < CAC"

每个否定论点需提供反驳证据，无法反驳的论点计入风险评分。

## 验证流程

### 步骤一：输入创业点子

用户提供点子描述（1-3句话），例如：
> "一个面向自由职业者的自动化税务计算工具，连接银行流水和税务系统，自动生成报税表"

### 步骤二：S.E.E.D. 快速打分

对点子进行四维评分，输出初步利基分数。若分数 < 5.0，建议调整方向后重新评分。

### 步骤三：STREAM 深度分析

对通过初筛的点子执行六层分析，每层输出结构化结论和量化指标。

### 步骤四：Devil's Advocate 压力测试

执行五项反方论证，标注每项的反驳难度（Easy/Medium/Hard/Unresolved）。

### 步骤五：综合评分与建议

输出最终验证报告，包含：
- S.E.E.D. 总分与各维度得分
- STREAM 六层分析摘要
- Devil's Advocate 未解决问题列表
- 综合建议：GO / PIVOT / KILL
- 推荐的下一步行动（用户访谈、MVP构建、竞品分析等）

## 评分输出示例

```json
{
  "idea": "面向自由职业者的自动化税务计算工具",
  "seed_score": {
    "search": 7,
    "entry": 6,
    "expansion": 8,
    "defensibility": 5,
    "total": 6.5
  },
  "stream_analysis": {
    "surface": "TAM ~$2.1B, SAM ~$340M, SOM ~$12M",
    "target": "核心用户: 月收入5K-30K的自由设计师/开发者/咨询顾问",
    "revenue": "SaaS订阅 $15/月 + 按次报税 $9/次",
    "execution": "MVP: 银行API对接 + 税务规则引擎 + PDF导出",
    "advantage": "差异化: 针对自由职业场景优化, 非通用会计软件",
    "market": "时机: 零工经济增速18% YoY, 税务合规趋严"
  },
  "devils_advocate": [
    {"attack": "巨头入场风险", "refutation_difficulty": "Medium", "evidence": "TurboTax专注个人报税, 未覆盖自由职业细分"},
    {"attack": "获客成本高", "refutation_difficulty": "Hard", "evidence": "CAC估算$45, LTV$180, LTV/CAC=4.0 可接受但需验证"}
  ],
  "recommendation": "PIVOT",
  "next_steps": ["进行10位自由职业者深度访谈", "验证付费意愿与定价区间", "分析竞品缺失功能"]
}
```
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 智能分析 | 数据与分析维度 | 分析报告与关键发现 |
| 用S.E.E.D.利 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | solo-validate处理的内容输入 |,  |
| content | string | 否 | solo-validate处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "validate 相关配置参数",
    result: "validate 相关配置参数",
    result: "validate 相关配置参数",
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
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 常见问题

### Q1: 如何开始使用Validate？
A: 直接用1-3句话描述你的创业点子即可触发验证流程。例如输入"一个AI驱动的宠物健康监测App"，系统会自动执行S.E.E.D.打分、STREAM六层分析和Devil's Advocate压力测试，最终输出GO/PIVOT/KILL建议。

### Q2: S.E.E.D.评分低于7.0是否意味着点子不好？
A: 不一定。低分可能意味着该点子需要调整方向而非完全放弃。系统会在报告中标注低分维度的具体原因，例如Defensibility低分可能建议增加数据壁垒或网络效应设计。建议结合STREAM分析中的Execution层，评估是否存在低成本的改进方案。

### Q3: Devil's Advocate中有Unresolved问题怎么办？
A: Unresolved问题表示当前无法用数据和逻辑有效反驳的风险。建议将其转化为验证假设，通过用户访谈、竞品分析或MVP测试来收集证据。通常1-2个Unresolved问题不意味着KILL，但3个以上建议重新评估点子可行性。

### Q4: 验证结果为PIVOT时如何确定调整方向？
A: PIVOT建议会附带具体的调整方向提示，通常基于STREAM分析中得分最低的层级。例如若Revenue层得分最低，建议调整定价模型；若Advantage层得分最低，建议重新定位差异化。报告中 `next_steps` 字段会给出3-5个具体行动建议。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

