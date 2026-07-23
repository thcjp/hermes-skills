---
slug: "data-analysis-litiao"
name: "data-analysis-litiao"
version: "1.0.0"
displayName: "数据分析理调"
summary: "数据分析方法论框架，覆盖统计严谨性、陷阱识别、方法选择与输出规范"
license: "Proprietary"
description: |-
  数据分析理调是数据分析的方法论守护框架，覆盖 Methodology First（方法论优先）、
  Statistical Rigor Checklist（统计严谨性检查清单）、Analytical Pitfalls（分析陷阱识别：
  p-hacking、Survivorship bias、Simpson's Paradox 等）、Approach Selection（分析方法选择）、
  Output Standards（输出规范）、Red Flags to Escalate（风险升级机制）.
tags:
  - 信息检索
tools:
  - read
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# 数据分析理调

数据分析方法论守护框架，确保分析过程的统计严谨性、陷阱识别和方法论正确性.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 数据分析理调处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 数据分析理调数据分析 | 不支持 | 支持 |
| 数据分析理调陷阱识别 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

### Methodology First（方法论优先框架）

在任何数据分析开始前，先回答四个方法论问题：

1. **What decision** is this analysis supporting? — 这项分析支持什么决策？明确决策目标再选方法.
2. **What would change your mind?** — 什么结果会改变你的判断？预先定义证伪条件和 stop condition.
3. **What data do you actually have** vs what you wish you had? — 实际有什么数据 vs 希望有什么数据？识别数据缺口.
4. **What timeframe** is relevant? — 什么时间范围相关？避免 cherry-picking 有利时段.
核心原则：方法论决定分析路径，数据只是输入。先定 hypothesis 和 testing 框架，再收集数据.
### Statistical Rigor Checklist（统计严谨性检查清单）

分析结果输出前必须通过的统计检查：

- **Sample size adequacy**：样本量是否足够？小样本（n<30）的 inference 不可靠，需标注 effect size 和 confidence interval
- **Multiple comparison correction**：多次比较是否做了校正？用 Bonferroni correction 或 FDR 控制 false positive
- **p-value interpretation**：p-value 是否被正确理解？p<0.05 不等于"有效"，需报告 effect size 和 practical significance
- **Confounding variables**：是否有未控制的 confounder？cohort 对比时检查 baseline 差异
- **Regression assumptions**：回归模型假设是否满足？检查残差独立性、homoscedasticity、multicollinearity
- **Confidence interval reporting**：是否报告了 confidence interval 而非仅点估计？

### Analytical Pitfalls（分析陷阱识别）
7 个常见分析陷阱及其识别方法：

| 陷阱 | 英文 | 识别方法 |
|---:|---:|---:|
| p值操纵 | p-hacking | 检查是否多次跑测试直到 p<0.05，报告所有跑过的测试而非只报告显著的 |
| 时期不可比 | Comparing unequal periods | 对比周期天数是否一致？节假日、季节性是否对齐？ |
| 幸存者偏差 | Survivorship bias | 样本是否只包含"存活"对象？退出用户、失败案例是否被排除？ |
| 辛普森悖论 | Simpson's Paradox | 分组和整体趋势是否一致？分层分析后再下结论 |
| 时间序列伪相关 | Correlation in time series | 两个时间序列的相关可能是 trend 导致的，需差分或去趋势后再算相关 |
| 百分比聚合错误 | Aggregating percentages | 各组百分比不能直接平均，需用加权平均或回到原始计数 |
| 摘樱桃 | Cherry-picking | 是否只展示有利数据？检查完整时间范围和所有分组 |

**输出**: 返回Analytical Pitfalls（分析陷阱识别）的处理结果,包含执行状态码、结果数据和执行日志.
### Approach Selection（分析方法选择）
根据分析目标选择正确的分析方法：

- **描述性分析（Descriptive）**：均值、中位数、分布 — 回答"发生了什么"
- **诊断性分析（Diagnostic）**：cohort analysis、segmentation、funnel analysis — 回答"为什么发生"
- **因果推断（Causal inference）**：A/B testing、difference-in-differences、propensity score matching — 回答"X 是否导致 Y"
- **预测性分析（Predictive）**：regression、time series forecasting、anomaly detection — 回答"未来会怎样"
- **规范性分析（Prescriptive）**：optimization、simulation — 回答"应该怎么做"

选择原则：correlation 不等于 causation。观察数据只能发现关联，因果需实验或准实验方法.
**输出**: 返回Approach Selection（分析方法选择）的处理结果,包含执行状态码、结果数据和执行日志.
### Output Standards（输出规范）
分析输出的标准化要求：

- **结论先行**：1-2 句话总结核心发现，附 confidence level（高/中/低）
- **数据来源**：标注数据来源、时间范围、样本量、缺失值处理方式
- **可视化规范**：图表标题自解释，坐标轴有标签和单位，避免误导性 scale
- **不确定性量化**：报告 confidence interval、margin of error，不使用确定性表述
- **方法论说明**：使用的统计方法、假设检验类型、校正方法
- **局限性声明**：数据局限性、未控制的 confounder、generalizability 限制

**输入**: 用户提供Output Standards（输出规范）所需的指令和必要参数.
### Red Flags to Escalate（风险升级机制）

遇到以下情况时必须升级到资深分析师或暂停分析：

- 用户想"证明"预设结论而非探索发现 — 这是 p-hacking 的起点
- 样本量太小无法做可靠 inference（如 n<10 做统计检验）
- 数据质量问题导致分析无效（缺失率 >30%、系统性偏差）
- 存在无法控制的 confounder 且影响方向未知
- Simpson's Paradox 出现（分组和整体结论矛盾）
- 时间序列的 correlation 可能是 spurious（伪相关）
- 结果依赖于特定时间段或特定子集（Cherry-picking 风险）

#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`data-analysis-litiao`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 示例

### 基本用法

向Agent发送指令:

```
使用 数据分析理调 处理以下任务:
[具体任务描述]
```

### 输出说明

Agent将根据指令调用对应能力,返回响应数据。响应格式取决于具体能力点的输出定义.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD（纯Markdown指令，无需exec命令行能力）

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| p-hacking 风险 | 多次测试直到显著 | 预设假设和测试数量，用 Bonferroni 校正，报告所有测试 |
| 样本量不足 | n<30 做统计推断 | 标注为探索性分析，报告 effect size，建议增加样本量 |
| Simpson's Paradox | 分组与整体趋势矛盾 | 分层分析并报告各组结果，不依赖整体汇总结论 |
| 幸存者偏差 | 样本只含成功案例 | 检查样本选择机制，纳入失败/退出案例 |
| 时间序列伪相关 | trend 导致虚假 correlation | 差分去趋势后再计算相关，检查 Granger causality |
| 百分比聚合错误 | 直接平均各组百分比 | 回到原始计数重新计算，使用加权平均 |
| 数据缺失率过高 | 缺失率 >30% | 评估缺失机制（MCAR/MAR/MNAR），多重插补或标注局限性 |
| Cherry-picking 嫌疑 | 只展示有利数据 | 展示完整时间范围和所有分组，透明报告所有分析结果 |

## 常见问题

### Q1: p-value < 0.05 就意味着结果显著吗？
A: 不完全。p-value 只是在零假设下观察到当前或更极端结果的概率。还需检查 effect size（实际效应量）、confidence interval、样本量和 practical significance。小样本下的 p<0.05 可能是 false positive.
### Q2: 如何识别 Simpson's Paradox？
A: 对比分组分析和整体汇总分析的趋势方向。如果分组结论和整体结论相反（如各组都显示 A>B，但整体显示 B>A），就是 Simpson's Paradox。此时应以分层分析为准.
### Q3: 观察数据能做因果推断吗？
A: 观察数据只能发现 correlation（关联），不能直接做 causal inference（因果推断）。需要用 difference-in-differences、propensity score matching、instrumental variable 等准实验方法，并明确假设前提.
## 已知限制

- 不替代专业统计学家做复杂建模决策
- 无法自动检测所有类型的数据质量问题
- 因果推断方法的有效性依赖假设前提是否满足
- 高维数据的 multiple comparison 问题需要领域知识判断
