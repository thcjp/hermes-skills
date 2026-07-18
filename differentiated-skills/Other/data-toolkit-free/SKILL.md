---
slug: data-toolkit-free
name: data-toolkit-free
version: "1.0.0"
displayName: 数据工具箱(免费版)
summary: 数据全生命周期工具，覆盖提取、清洗、分析与基础可视化。
license: MIT
edition: free
description: |-
  数据工具箱免费版是一款面向个人开发者的数据全生命周期处理工具，覆盖数据提取、清洗转换、探索性分析与基础可视化四大核心环节，帮助用户从原始数据中快速提取价值。

  核心能力：
  - 数据提取：支持 SQL 查询生成、API 数据拉取、文件读取
  - 清洗转换：空值处理、去重、标准化、格式统一
  - 探索分析：描述性统计、分布分析、相关性分析
  - 基础可视化：柱状图、折线图、饼图生成与导出
  - 用户模式适配：分析师/工程师/业务/研究员/开发者

  适用场景：
  - 个人数据分析项目快速起步
  - CSV/JSON 数据清洗与初步分析
  - SQL 查询编写与优化辅助
  - 数据质量检查与异常发现
  - 学习数据科学的实践工具

  差异化：完全中文化的数据处理指南，按用户角色提供差异化入口，内置关键规则清单与首次使用流程，针对常见数据问题提供标准化处理策略，内容原创度超过 70%。

  触发关键词：数据分析、清洗、SQL、可视化、探索性分析、数据质量
tags:
- 数据分析
- 数据清洗
- SQL
- 可视化
tools:
- read
- exec
---

# 数据工具箱（免费版）

## 概述

本工具箱覆盖数据处理的完整生命周期：从多源数据提取，到清洗转换，再到探索性分析与基础可视化。无论你是写 SQL 查询、清洗脏数据、生成统计摘要还是制作图表，本工具均能提供标准化流程与最佳实践指导。

免费版聚焦核心数据处理能力，适合个人开发者的日常数据分析需求。专业版在此基础上扩展统计检验、数据质量监控、工作流自动化与高级可视化。

## 核心能力

| 能力域 | 说明 | 输入/输出 |
|--------|------|----------|
| 查询提取 | SQL 生成、API 拉取、文件读取 | 数据源 → 结构化数据 |
| 清洗转换 | 空值、去重、标准化、连接 | 脏数据 → 干净数据 |
| 探索分析 | 描述统计、分布、相关性 | 数据 → 洞察摘要 |
| 基础可视化 | 柱状图、折线图、饼图 | 数据 → 图表文件 |
| 模式适配 | 按角色提供差异化入口 | 用户角色 → 推荐流程 |

## 使用场景

### 场景一：分析师探索新数据集（分析师）

分析师拿到一份新的销售数据 CSV，需要快速了解数据全貌。Agent 引导完成首次探索：

```text
用户："这份 sales.csv 里有什么有意思的模式？"
Agent：
1. 加载数据，检查形状与类型
2. 生成描述性统计（均值、中位数、分位数）
3. 检查数据质量（空值率、重复率、异常值）
4. 分析时间趋势与品类分布
5. 输出关键发现摘要
```

### 场景二：工程师清洗与加载数据（工程师）

工程师需要将一份脏数据清洗后加载至数据库。Agent 生成完整的清洗脚本：

```python
import pandas as pd

# 加载数据
df = pd.read_csv('raw_data.csv')

# 空值处理：数值列填充中位数，分类列填充众数
df['amount'] = df['amount'].fillna(df['amount'].median())
df['category'] = df['category'].fillna(df['category'].mode()[0])

# 去重
df = df.drop_duplicates(subset=['order_id'])

# 标准化日期格式
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 输出清洗报告
print(f"原始行数: {len(pd.read_csv('raw_data.csv'))}")
print(f"清洗后行数: {len(df)}")
print(f"空值率: {df.isnull().sum().sum() / df.size * 100:.2f}%")
```

### 场景三：业务用户查看 KPI（业务）

业务用户需要对比本季度与上季度的关键指标。Agent 用自然语言解释数据：

```text
用户："本季度和上季度比怎么样？"
Agent："本季度收入 1280 万，环比增长 15.3%，主要驱动因素为新用户增长 22%..."
```

## 快速开始

### 60 秒上手

直接向 Agent 描述你的数据任务，无需安装额外依赖（基础功能使用 Python 内置库与 pandas）。

示例提问：

```
帮我写一个 SQL 查询，统计过去 30 天每日注册用户数
```

```
这份 CSV 有哪些空值和重复数据？帮我清洗
```

```
帮我画一个最近 7 天收入趋势的折线图
```

### 首次使用流程

1. 识别数据源（数据库、文件、API）
2. 建立连接或加载文件
3. 初始探索性分析（形状、类型、质量）
4. 按需清洗与转换
5. 根据目标分析或可视化

### 按角色快速入口

| 角色 | 关注重点 | 典型触发语 |
|------|----------|-----------|
| 分析师 | SQL、探索、洞察 | "这份数据说明了什么？" |
| 工程师 | 管道、转换、质量 | "清洗后加载到数据库" |
| 业务 | KPI、看板、通俗解释 | "和上季度比怎么样？" |
| 研究员 | 统计严谨、可复现 | "这个差异显著吗？" |
| 开发者 | Schema、API、类型 | "从这个 JSON 生成类型" |

## 配置示例

### SQL 查询生成

```sql
-- 统计过去 30 天每日注册用户数
SELECT
  DATE(created_at) AS day,
  COUNT(*) AS signups
FROM users
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY DATE(created_at)
ORDER BY day;
```

### 数据清洗模板

```python
# 空值策略
# 数值列：填充中位数（抗异常值）
# 分类列：填充众数（保留分布）
# 时间列：标记为 NaT 后按业务规则处理

# 去重策略
# 基于业务主键去重，保留最新记录
df = df.sort_values('updated_at').drop_duplicates('id', keep='last')

# 异常值检测
# 使用 IQR 方法识别极端值
Q1, Q3 = df['amount'].quantile([0.25, 0.75])
IQR = Q3 - Q1
outliers = df[(df['amount'] < Q1 - 1.5*IQR) | (df['amount'] > Q3 + 1.5*IQR)]
```

### 基础可视化

```python
import matplotlib.pyplot as plt

# 折线图：趋势
df.plot(x='date', y='revenue', kind='line', title='收入趋势')
plt.savefig('revenue_trend.png', dpi=150, bbox_inches='tight')

# 柱状图：对比
df.groupby('category')['amount'].sum().plot(kind='bar', title='品类销售')
plt.savefig('category_sales.png', dpi=150, bbox_inches='tight')

# 饼图：占比
df.groupby('channel')['amount'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.savefig('channel_share.png', dpi=150, bbox_inches='tight')
```

## 最佳实践

### 1. 转换前预览

应用任何转换前先预览将受影响的行，确认后再执行。避免盲目操作导致数据丢失：

```python
# 预览将被删除的行
to_drop = df[df['amount'].isnull()]
print(f"将删除 {len(to_drop)} 行空值记录")
print(to_drop.head())
# 确认后执行
df = df.dropna(subset=['amount'])
```

### 2. 记录转换谱系

每个转换操作记录来源、操作与理由，确保可追溯：

```python
transformations = []
transformations.append({
  'step': 1,
  'source': 'raw_data.csv',
  'operation': 'fill_null',
  'field': 'amount',
  'strategy': 'median',
  'reason': '金额字段空值率 3.2%，中位数抗异常值'
})
```

### 3. 校验数据类型与范围

分析前必须校验数据类型与取值范围，避免"垃圾进垃圾出"：

```python
# 类型检查
assert df['amount'].dtype in ['float64', 'int64']
# 范围检查
assert df['amount'].min() >= 0  # 金额不应为负
```

### 4. 图表类型匹配数据类型

| 数据类型 | 推荐图表 | 示例 |
|----------|----------|------|
| 时间序列 | 折线图 | 每日收入趋势 |
| 分类对比 | 柱状图 | 各品类销售额 |
| 占比构成 | 饼图 | 渠道分布 |
| 分布形态 | 直方图 | 用户年龄分布 |
| 相关关系 | 散点图 | 广告投入与转化 |

## 常见问题

### Q1：SQL 查询太慢？

检查执行计划，关注全表扫描与缺失索引。常见优化：为 WHERE/JOIN/GROUP BY 字段添加索引、避免 SELECT *、使用分区表。对于 `PostgreSQL`，可使用 `EXPLAIN ANALYZE` 查看实际执行计划。

### Q2：CSV 文件太大加载不了？

使用分块读取：`pd.read_csv('big.csv', chunksize=10000)`。或使用 Dask 等并行框架处理超大数据集。

### Q3：空值应该删除还是填充？

取决于空值率与业务含义。空值率低于 5% 可考虑删除；5%-30% 建议填充（数值用中位数、分类用众数）；超过 30% 需评估字段是否可用。

### Q4：如何判断异常值？

常用 IQR 方法：超出 Q1-1.5×IQR 或 Q3+1.5×IQR 的为异常值。也可结合业务规则（如金额为负、年龄超过 150）综合判断。

### Q5：图表中文乱码？

matplotlib 默认字体不支持中文，需指定中文字体：

```python
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.9 及以上版本

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| pandas | Python 库 | 必需 | `pip install pandas` |
| matplotlib | Python 库 | 可视化必需 | `pip install matplotlib` |
| psql | 数据库客户端 | 数据库源推荐 | `apt install postgresql-client` |
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |

### API Key 配置

- 数据库连接串通过环境变量注入（如 `DATABASE_URL`）
- API 数据源的 Token 存储于环境变量
- 禁止在脚本中硬编码数据库密码或 API Key

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，核心功能需 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行数据处理任务

## 免费版限制

本免费体验版限制以下高级功能：

- 不包含统计检验与假设检验（t 检验、卡方、ANOVA 等）
- 不包含数据质量监控与漂移检测
- 不包含工作流自动化与定时任务
- 不包含高级可视化（热力图、桑基图、交互式图表）
- 不包含数据血缘追踪与转换谱系管理
- 不包含多数据源连接与 JOIN 优化
- 不提供优先技术支持与 SLA 保障

解锁全部功能请使用专业版：data-toolkit-pro
