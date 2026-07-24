---
slug: "data-analysis-toolkit"
name: "data-analysis-toolkit"
version: "1.0.1"
displayName: "Python Data Analysis"
summary: "提供Python数据清洗、统计分析及可视化建议，辅助业务和科研数据的快速处理与分析。。提供Python数据清洗、统计分析及可视化建议，辅助业务和科研数据的快速处理与分析. 核心能力:数据清洗"
license: "MIT"
description: |-
  提供Python数据清洗、统计分析及可视化建议，辅助业务和科研数据的快速处理与分析.
  核心能力:数据清洗预处理、统计分析支持、数据可视化建议、常见分析模式指导.
  适用场景:业务数据分析、科研数据处理、报表生成辅助、数据探索性分析.
tags:
  - Integrations
  - 数据处理
  - 数据分析
  - 工具
  - llm
  - agent
  - 运行环境
tools:
  - read
  - write
  - exec
  - glob
homepage: ""
category: "Research"
---
# Python Data Analysis

## 核心能力

### 一、数据清洗和预处理
- **缺失值处理**: 识别数据中的缺失值(NaN/Null/空字符串),支持删除、均值填充、中位数填充、前后向填充等策略
- **异常值检测**: 基于Z-Score、IQR(四分位距)方法识别离群点,支持标记、剔除或平滑处理
- **数据类型转换**: 自动推断字段类型,将字符串日期转为datetime、文本数字转为数值类型
- **重复数据处理**: 基于全部列或指定列识别并去除重复记录
- **数据标准化**: Min-Max归一化、Z-Score标准化,消除量纲差异影响

### 二、统计分析支持
- **描述性统计**: 计算均值、中位数、标准差、方差、偏度、峰度等统计量
- **相关性分析**: Pearson/Spearman相关系数矩阵,识别变量间线性与非线性关系
- **假设检验**: T检验、卡方检验、方差分析(ANOVA),支持p值计算与显著性判断
- **分组聚合**: 按类别字段分组计算统计量,支持多级分组与自定义聚合函数

### 三、数据可视化建议
- **图表类型推荐**: 根据数据特征和分析目标自动推荐合适图表(柱状图/折线图/散点图/箱线图/热力图)
- **可视化代码生成**: 输出matplotlib/seaborn/plotly代码片段,可直接执行生成图表
- **配色与样式优化**: 建议专业配色方案,优化图表标签、标题、图例等元素

### 四、常见分析模式指导
- **时间序列分析**: 趋势分解、季节性识别、移动平均、ARIMA建模建议
- **分群与聚类**: K-Means/DBSCAN聚类建议与轮廓系数评估
- **回归分析**: 线性回归/逻辑回归建模建议与残差分析
- **探索性数据分析(EDA)**: 自动生成数据概览报告,包含分布、相关性、异常值摘要
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景
- 不适用: 需要人工判断的复杂决策场景

* 业务数据分析
* 科研数据处理
* 报表生成辅助
* 数据探索性分析

## 使用流程

1. 描述你的数据结构
2. 说明分析目标
3. 获取代码和分析建议

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 处理的输入数据或指令,支持文本/JSON/CSV格式 |
| options | object | 否 | 附加配置选项,如清洗策略、统计方法等 |
| callback_url | string | 否 | 异步回调通知URL |

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "数据分析结果",
    "execution_time": "0.8s",
    "metadata": {
      "version": "1.0",
      "processor": "data-analysis-toolkit"
    }
  },
  "execution_log": ["解析输入参数", "数据清洗预处理", "执行统计分析", "格式化输出结果"],
  "error": null
}
```

## 异常处理

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

## 案例展示

以下是Python Data Analysis在实际场景中的应用案例，展示完整的输入处理输出流程.

### 销售数据探索性分析（Python）

对CSV格式的销售数据进行清洗、描述性统计与可视化:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 加载数据
df = pd.read_csv('sales_data.csv')

# 2. 数据清洗：处理缺失值与异常值
df['revenue'] = df['revenue'].fillna(df['revenue'].median())  # 中位数填充
q1, q3 = df['revenue'].quantile([0.25, 0.75])
iqr = q3 - q1
df = df[(df['revenue'] >= q1 - 1.5 * iqr) & (df['revenue'] <= q3 + 1.5 * iqr)]  # IQR去离群

# 3. 描述性统计
print("=== 描述性统计 ===")
print(df.describe())
print(f"偏度: {df['revenue'].skew():.2f}, 峰度: {df['revenue'].kurtosis():.2f}")

# 4. 相关性分析
corr_matrix = df[['revenue', 'quantity', 'discount']].corr()
print("\n=== 相关系数矩阵 ===")
print(corr_matrix)

# 5. 分组聚合：按产品类别统计
category_stats = df.groupby('category')['revenue'].agg(['mean', 'sum', 'count'])
print("\n=== 按类别统计 ===")
print(category_stats)

# 6. 可视化：收入分布与类别对比
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(df['revenue'], bins=30, kde=True, ax=axes[0])
axes[0].set_title('Revenue Distribution')
sns.boxplot(x='category', y='revenue', data=df, ax=axes[1])
axes[1].set_title('Revenue by Category')
plt.tight_layout()
plt.savefig('sales_eda.png', dpi=150)
print("\n可视化图表已保存: sales_eda.png")
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 数据处理能力受限于本地硬件资源
- 大数据量时分析性能可能显著下降
- 数据准确性依赖输入质量，无法自动修正脏数据

## 常见问题

**Q: 如何处理异常输入?**
A: 系统会自动检测并返回错误提示, 同时提供修复建议.
**Q: 支持哪些输入格式?**
A: 支持标准文本、JSON、CSV等常见格式.