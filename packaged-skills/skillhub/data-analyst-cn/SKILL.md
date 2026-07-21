---
slug: data-analyst-cn
name: data-analyst-cn
version: "1.0.0"
displayName: 数据分析师
summary: 数据清洗、统计分析、时间序列分析、可视化代码生成与分析报告自动生成
license: MIT
description: |-
  数据分析师——快速进行数据清洗、统计分析和可视化，适合数据分析师、产品经理、运营人员。
  核心能力包括：
  - 多源数据读取（CSV、Excel、JSON、SQLite、API）
  - 数据预览与质量检查（shape、dtypes、describe、缺失/重复统计）
  - 数据清洗（缺失值填充、去重、类型转换、IQR异常值剔除、字符串处理）
  - 统计分析（均值/中位数/众数/标准差/偏度/峰度/分位数/相关矩阵/分组聚合/交叉表）
  - 时间序列分析（resample重采样、rolling滚动统计、diff差分、pct_change环比、seasonal_decompose季节分解）
  - 可视化代码生成（折线/柱状/散点/直方/箱线/热力/小提琴/成对图/多轴图）
  - 分析报告自动生成（数据概览/关键指标/分布特征/Top排名/趋势分析/建议）
tags:
  - Integrations
  - data-analysis
  - visualization
tools:
  - read
  - exec
---

# 数据分析师

## 概述

快速进行数据清洗、统计分析和可视化，适合数据分析师、产品经理、运营人员。提供从数据读取到报告生成的完整Python代码模板，覆盖Pandas、Matplotlib、Seaborn、Statsmodels核心工作流。

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
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）

## 核心能力

### 多源数据读取
| 数据源 | 代码 | 说明 |
|--------|------|------|
| CSV | `pd.read_csv('data.csv')` | 读取CSV文件 |
| Excel | `pd.read_excel('data.xlsx', sheet_name='Sheet1')` | 指定Sheet读取 |
| JSON | `pd.read_json('data.json')` | 读取JSON文件 |
| SQLite | `pd.read_sql('SELECT * FROM table', conn)` | 需先 `sqlite3.connect('database.db')` |
| API | `pd.DataFrame(response.json())` | 需先 `requests.get('https://api.example.com/data')` |

**处理**: 按照skill规范执行多源数据读取操作,遵循单一意图原则。
**输出**: 返回多源数据读取的执行结果,包含操作状态和输出数据。### 数据预览与质量检查
```python
print(df.shape)        # 行列数，如 (1542, 7)
print(df.columns)      # 列名列表
print(df.dtypes)       # 数据类型
print(df.info())       # 详细信息（含内存占用）

print(df.head())       # 前 5 行
print(df.tail())       # 后 5 行
print(df.sample(5))    # 随机 5 行

print(df.describe())   # 数值列统计
print(df.describe(include='all'))  # 所有列（含分类列）
```

**输入**: 用户提供数据预览与质量检查所需的指令和必要参数。
**处理**: 按照skill规范执行数据预览与质量检查操作,遵循单一意图原则。
**输出**: 返回数据预览与质量检查的执行结果,包含操作状态和输出数据。### 数据清洗
**缺失值处理**：

```python
df.isnull().sum()                       # 统计每列缺失数
df.dropna()                             # 删除含缺失的行
df.fillna(0)                            # 填充 0
df.fillna(df.mean())                    # 填充均值
df['col'].fillna(df['col'].mode()[0])   # 填充众数
```

**去重处理**：

```python
df.duplicated().sum()                   # 统计重复行数
df.drop_duplicates()                    # 删除完全重复行
df.drop_duplicates(subset=['col'])      # 按指定列去重
```

**类型转换**：

```python
df['date'] = pd.to_datetime(df['date'])
df['price'] = df['price'].astype(float)
df['category'] = df['category'].astype('category')
```

**IQR异常值剔除**：

```python
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['col'] >= Q1 - 1.5*IQR) & (df['col'] <= Q3 + 1.5*IQR)]
```

**字符串处理**：

```python
df['name'] = df['name'].str.strip()           # 去首尾空白
df['name'] = df['name'].str.lower()           # 转小写
df['name'] = df['name'].str.replace('old', 'new')  # 替换
```

**输入**: 用户提供数据清洗所需的指令和必要参数。
**输出**: 返回数据清洗的执行结果,包含操作状态和输出数据。### 统计分析
**描述统计**：

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
```

**相关分析**：

```python
df.corr()             # 完整相关矩阵
df.corr()['target']   # 与目标变量的相关性
```

**分组聚合**：

```python
df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count'],
    'profit': 'mean'
})
```

**交叉表**：

```python
pd.crosstab(df['col1'], df['col2'])
```

**输入**: 用户提供统计分析所需的指令和必要参数。
**输出**: 返回统计分析的执行结果,包含操作状态和输出数据。### 时间序列分析

```python
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df.resample('D').sum()      # 按天汇总
df.resample('W').mean()     # 按周均值
df.resample('M').sum()      # 按月汇总

df['rolling_mean'] = df['col'].rolling(window=7).mean()  # 7日滚动均值
df['rolling_std'] = df['col'].rolling(window=7).std()    # 7日滚动标准差

df['diff'] = df['col'].diff()              # 一阶差分
df['pct_change'] = df['col'].pct_change()  # 环比变化率

from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['col'], model='additive', period=12)
result.plot()
```

### 可视化代码生成
**中文字体配置**（必须先执行）：

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

**基础图表**：

| 图表类型 | 代码 | 适用场景 |
|---------|------|---------|
| 折线图 | `plt.plot(df['date'], df['value'])` | 趋势变化 |
| 柱状图 | `plt.bar(df['category'], df['value'])` | 分类对比 |
| 散点图 | `plt.scatter(df['x'], df['y'], alpha=0.5)` | 关系分布 |
| 直方图 | `plt.hist(df['value'], bins=20, edgecolor='black')` | 分布形态 |
| 箱线图 | `sns.boxplot(data=df, x='category', y='value')` | 离群值检测 |
| 热力图 | `sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)` | 相关矩阵 |

**高级图表**：

```python
# 分组柱状图
df_grouped = df.groupby(['category', 'type'])['value'].sum().unstack()
df_grouped.plot(kind='bar', figsize=(12, 6))

# 小提琴图
sns.violinplot(data=df, x='category', y='value')

# 成对关系图
sns.pairplot(df[['col1', 'col2', 'col3', 'category']], hue='category')

# 多轴趋势图（含置信区间）
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df.index, df['value'], label='实际值')
ax.plot(df.index, df['rolling_mean'], label='7日均值', linestyle='--')
ax.fill_between(df.index, df['lower'], df['upper'], alpha=0.2)
ax.legend()
```

**输出**: 返回可视化代码生成的执行结果,包含操作状态和输出数据。
### 分析报告自动生成
```python
def generate_report(df):
    report = f"""

**输入**: 用户提供分析报告自动生成所需的指令和必要参数。
**处理**: 按照skill规范执行分析报告自动生成操作,遵循单一意图原则。

### 能力覆盖范围

本skill还覆盖以下能力场景: 可视化代码生成与、数据分析师、快速进行数据清洗、统计分析和可视化、适合数据分析师、产品经理、运营人员、核心能力包括、重复统计、缺失值填充、重采样、滚动统计、季节分解、成对图、多轴图、数据概览、关键指标、分布特征、Top、趋势分析。这些能力在上述核心功能中均有对应处理逻辑。
## 1. 数据概览
- 数据量：{len(df)} 行 × {len(df.columns)} 列
- 时间范围：{df['date'].min()} 至 {df['date'].max()}
- 缺失值：{df.isnull().sum().sum()} 个

## 2. 关键指标
- 总销售额：¥{df['sales'].sum():,.2f}
- 平均订单：¥{df['sales'].mean():,.2f}

## 3. 分布特征
- 偏度：{df['sales'].skew():.2f}
- 峰度：{df['sales'].kurt():.2f}

## 4. Top 5 类别
{df.groupby('category')['sales'].sum().sort_values(ascending=False).head().to_markdown()}

## 5. 趋势分析
- 环比增长：{df['sales'].pct_change().mean()*100:.2f}%
"""
    return report
```

## 使用流程

1. **读取数据**：根据数据源选择 `pd.read_csv()` / `pd.read_excel()` / `pd.read_json()` / `pd.read_sql()`
2. **预览检查**：执行 `df.shape`、`df.dtypes`、`df.describe()` 了解数据全貌
3. **数据清洗**：处理缺失值（`fillna`）、去重（`drop_duplicates`）、类型转换（`astype`）、IQR异常值剔除
4. **统计分析**：计算描述统计量、相关矩阵、分组聚合、交叉表
5. **时间序列**：如涉及时序数据，执行 `resample`、`rolling`、`seasonal_decompose`
6. **可视化**：配置SimHei字体后生成图表代码
7. **报告生成**：调用 `generate_report()` 输出结构化分析报告

## 详细示例

### 示例1：CSV数据清洗与分析

```text
输入: 分析这个 CSV 文件：sales.csv

处理:
- df = pd.read_csv('sales.csv')
- 缺失值: df['sales'].fillna(df['sales'].mean())
- 异常值: Q1=120, Q3=450, IQR=330, 保留 [Q1-1.5*IQR, Q3+1.5*IQR] 范围
- 统计: 均值¥45,230, 中位数¥38,500, 偏度1.2

输出: 清洗后 1485 行（原 1542 行），销售额右偏分布
```

### 示例2：生成折线图代码

```text
输入: 为这些数据生成折线图代码

输出:
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['value'])
plt.title('趋势图')
plt.xlabel('日期')
plt.ylabel('数值')
plt.show()
```

### 示例3：时间序列季节分解

```text
输入: 对月度销售数据做季节性分解

处理:
- df['date'] = pd.to_datetime(df['date'])
- df = df.set_index('date')
- result = seasonal_decompose(df['sales'], model='additive', period=12)
- 趋势组件: 稳定上升
- 季节组件: 12月峰值，6月谷值
- 残差: 无明显模式

输出: 分解图含趋势/季节/残差三子图
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 中文图表显示方框 | 未配置SimHei字体 | 执行 `plt.rcParams['font.sans-serif'] = ['SimHei']` 和 `plt.rcParams['axes.unicode_minus'] = False` |
| `KeyError` 列名不存在 | 列名含空格或大小写不一致 | 先 `print(df.columns)` 检查实际列名，用 `df.columns = df.columns.str.strip()` 清洗 |
| `fillna(df.mean())` 报错 | 含非数值列无法求均值 | 仅对数值列填充：`df.select_dtypes(include='number').fillna(df.mean())` |
| IQR剔除后数据量骤减 | 异常值阈值过严（1.5*IQR） | 检查数据分布是否极度偏斜，考虑用 3*IQR 放宽阈值或先做对数变换 |
| `seasonal_decompose` 报错 | 数据含缺失值或频率不固定 | 先 `df = df.asfreq('M').fillna(method='ffill')` 补齐频率与缺失 |
| `resample` 结果全NaN | 未将日期列设为索引 | 先 `df['date'] = pd.to_datetime(df['date'])` 再 `df = df.set_index('date')` |
| `astype(float)` 转换失败 | 列中含非数字字符串（如"N/A"） | 使用 `pd.to_numeric(df['col'], errors='coerce')` 将非法值转为NaN |
| 大数据集内存溢出 | DataFrame超过可用内存 | 使用 `dtype` 参数指定类型，或分块读取 `pd.read_csv(chunksize=10000)` |

## 常见问题

### Q1: 图表中中文显示为方框怎么解决？
A: 在绘图前配置字体：`plt.rcParams['font.sans-serif'] = ['SimHei']`（Windows）或 `['Arial Unicode MS']`（macOS），同时设置 `plt.rcParams['axes.unicode_minus'] = False` 避免负号显示异常。

### Q2: IQR异常值剔除后数据量减少太多怎么办？
A: 检查数据分布的偏度（`df['col'].skew()`），若偏度>2说明极度右偏。可先做对数变换 `np.log1p(df['col'])` 再用IQR，或将阈值从1.5*IQR放宽至3*IQR。

### Q3: `rolling(window=7)` 前几行为NaN正常吗？
A: 正常。7日滚动窗口需要至少7个数据点才能计算，前6行无足够数据故为NaN。绘图时可用 `df.dropna()` 去掉或保留以显示真实情况。

### Q4: `seasonal_decompose` 的 period 参数怎么选？
A: period是季节周期长度。月度数据通常 period=12（一年12个月），季度数据 period=4，日数据如有周季节性则 period=7。需确保数据长度至少为 period 的2倍。

### Q5: `df.corr()` 中有非数值列怎么办？
A: `df.corr()` 默认仅计算数值列，非数值列自动忽略。如需包含分类列，先转为哑变量：`pd.get_dummies(df, columns=['category'])` 后再计算相关矩阵。

### Q6: 分组聚合后结果有多级索引怎么处理？
A: 使用 `reset_index()` 展平：`df.groupby('category').agg({'sales': 'sum'}).reset_index()`，或用 `as_index=False`：`df.groupby('category', as_index=False).agg({'sales': 'sum'})`。

## 已知限制

- 大数据集需注意内存使用，建议超过1GB时分块处理
- 处理前务必备份原始数据，清洗操作不可逆
- 统计结果需要业务验证，避免数据驱动偏差
- 可视化要简洁清晰，单图不宜超过5个系列
- 不适用于实时流数据处理
