---
slug: data-analyst-cn
name: data-analyst-cn
version: "1.0.23"
displayName: Data Analyst Cn
summary: 数据分析助手 - 数据清洗、统计分析、可视化建议。适合：数据分析师、产品经理、运营。
license: MIT-0
description: |-
  数据分析助手 - 数据清洗、统计分析、可视化建议。适合：数据分析师、产品经理、运营。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Data Analyst Cn

快速进行数据清洗、统计分析和可视化。

## 核心功能

| 功能 | 描述 |
| --- | --- |
| 数据清洗 | 去重、填充、格式化 |
| 统计分析 | 描述统计、相关分析 |
| 可视化 | 图表建议、代码生成 |
| 报告生成 | 自动生成分析报告 |

## 使用方法

### 分析数据

```text
分析这个 CSV 文件：sales.csv
```

### 数据清洗

```text
清洗这个数据集，处理缺失值和异常值
```

### 生成图表

```text
为这些数据生成折线图代码
```

## Python 数据分析模板

### 读取数据

```python
import pandas as pd

df = pd.read_csv('data.csv')

df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

df = pd.read_json('data.json')

import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM table', conn)

import requests
response = requests.get('https://api.example.com/data')
df = pd.DataFrame(response.json())
```

### 数据预览

```python
print(df.shape)        # 行列数
print(df.columns)      # 列名
print(df.dtypes)       # 数据类型
print(df.info())       # 详细信息

print(df.head())       # 前 5 行
print(df.tail())       # 后 5 行
print(df.sample(5))    # 随机 5 行

print(df.describe())   # 数值列统计
print(df.describe(include='all'))  # 所有列
```

### 数据清洗

```python
df.isnull().sum()                    # 统计缺失
df.dropna()                          # 删除缺失行
df.fillna(0)                         # 填充 0
df.fillna(df.mean())                 # 填充均值
df['col'].fillna(df['col'].mode()[0])  # 填充众数

df.duplicated().sum()                # 统计重复
df.drop_duplicates()                 # 删除重复
df.drop_duplicates(subset=['col'])   # 按列去重

df['date'] = pd.to_datetime(df['date'])
df['price'] = df['price'].astype(float)
df['category'] = df['category'].astype('category')

Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['col'] >= Q1 - 1.5*IQR) & (df['col'] <= Q3 + 1.5*IQR)]

df['name'] = df['name'].str.strip()
df['name'] = df['name'].str.lower()
df['name'] = df['name'].str.replace('old', 'new')
```

### 统计分析

```python
df['col'].mean()      # 均值
df['col'].median()    # 中位数
df['col'].mode()      # 众数

df['col'].std()       # 标准差
df['col'].var()       # 方差
df['col'].max() - df['col'].min()  # 极差

df['col'].skew()      # 偏度
df['col'].kurt()      # 峰度
df['col'].quantile([0.25, 0.5, 0.75])  # 分位数

df.corr()             # 相关矩阵
df.corr()['target']   # 与目标的相关性

df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count'],
    'profit': 'mean'
})

pd.crosstab(df['col1'], df['col2'])
```

### 时间序列分析

```python
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df.resample('D').sum()      # 按天
df.resample('W').mean()     # 按周
df.resample('M').sum()      # 按月

df['rolling_mean'] = df['col'].rolling(window=7).mean()
df['rolling_std'] = df['col'].rolling(window=7).std()

df['diff'] = df['col'].diff()
df['pct_change'] = df['col'].pct_change()

from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['col'], model='additive', period=12)
result.plot()
```

## 可视化代码

### 基础图表

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['value'])
plt.title('趋势图')
plt.xlabel('日期')
plt.ylabel('数值')
plt.show()

plt.bar(df['category'], df['value'])
plt.xticks(rotation=45)
plt.show()

plt.scatter(df['x'], df['y'], alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

plt.hist(df['value'], bins=20, edgecolor='black')
plt.xlabel('数值')
plt.ylabel('频数')
plt.show()

sns.boxplot(data=df, x='category', y='value')
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.show()
```

### 高级图表

```python
df_grouped = df.groupby(['category', 'type'])['value'].sum().unstack()
df_grouped.plot(kind='bar', figsize=(12, 6))
plt.legend(title='类型')
plt.show()

sns.violinplot(data=df, x='category', y='value')
plt.show()

sns.pairplot(df[['col1', 'col2', 'col3', 'category']], hue='category')
plt.show()

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df.index, df['value'], label='实际值')
ax.plot(df.index, df['rolling_mean'], label='7日均值', linestyle='--')
ax.fill_between(df.index, df['lower'], df['upper'], alpha=0.2)
ax.legend()
plt.show()
```

## 分析报告模板

```python
def generate_report(df):
    """生成数据分析报告"""
    report = f"""

## 1. 数据概览
- 数据量：{len(df)} 行 × {len(df.columns)} 列
- 时间范围：{df['date'].min()} 至 {df['date'].max()}
- 缺失值：{df.isnull().sum().sum()} 个

## 2. 关键指标
- 总销售额：¥{df['sales'].sum():,.2f}
- 平均订单：¥{df['sales'].mean():,.2f}
- 最高订单：¥{df['sales'].max():,.2f}
- 最低订单：¥{df['sales'].min():,.2f}

## 3. 分布特征
- 偏度：{df['sales'].skew():.2f}
- 峰度：{df['sales'].kurt():.2f}
- 标准差：{df['sales'].std():,.2f}

## 4. Top 5 类别
{df.groupby('category')['sales'].sum().sort_values(ascending=False).head().to_markdown()}

## 5. 趋势分析
- 环比增长：{df['sales'].pct_change().mean()*100:.2f}%
- 月均销售额：¥{df.resample('M', on='date')['sales'].sum().mean():,.2f}

## 6. 建议
1. 重点推广 Top 3 类别
2. 优化低转化品类
3. 关注季节性波动
"""
    return report
```

## 注意事项

* 大数据集注意内存使用
* 处理前备份数据
* 结果需要业务验证
* 可视化要简洁清晰

---

创建：2026-03-12
版本：1.0

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
### 分析数据

```text
分析这个 CSV 文件：sales.csv
```

### 数据清洗

```text
清洗这个数据集，处理缺失值和异常值
```

### 生成图表

```text
为这些数据生成折线图代码
```
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Data Analyst Cn？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Data Analyst Cn有什么限制？
A: 请参考已知限制章节了解具体限制。
