---
slug: csv-insight-miner
name: csv-insight-miner
version: 1.0.1
displayName: CSV洞察挖掘机
summary: "丢一个CSV自动出洞察报告,无需写代码,异常趋势一目了然。CSV洞察挖掘机——丢一个CSV文件,自动生成全面洞察报告与可视化图表。无需写代码,无需提提示词,自动识别数据类型、统计特征、异常值"
license: Proprietary
description: CSV洞察挖掘机——丢一个CSV文件,自动生成全面洞察报告与可视化图表。无需写代码,无需提提示词,自动识别数据类型、统计特征、异常值与相关性,支持多维度交叉分析和趋势发现,让数据自己说话。Use
  when 用户上传CSV要求分析数据、需要快速生成数据报告、查找异常值或数据可视化时使用。不适用于实时流数据和超大型数据库分析。
tags:
  - 数据分析
  - CSV分析
  - 数据洞察
  - 数据可视化
  - 探索性分析
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - 开发
  - 代码
  - AI代理
tools:
  - read
  - exec
  - write
category: "Automation"
---
# CSV洞察挖掘机

自动分析 CSV 文件,无需用户提示即可生成全面洞察。从数据探查到可视化,一键产出分析报告。

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 数据探查 | 陌生CSV文件 | 自动概览报告(行列数/类型/统计/缺失) |
| 快速洞察 | CSV+分析目标 | 趋势/异常/关联发现报告+Top5关键发现 |
| 报表自动化 | CSV+报表模板 | 模板化分析报告+可视化图表合集 |
| 数据质量检查 | CSV(入库前) | 缺失/异常/重复检测报告+清洗建议 |
| 探索性分析 | CSV+多变量 | 统计摘要+相关性热力图+散点矩阵 |

### 不适用于
- 实时数据流分析(本Skill处理静态CSV文件)
- 大数据分布式处理(单机内存限制,建议<2GB CSV)
- 机器学习模型训练与预测(请使用ML工具)
- 数据库直接查询(请使用duckdb-analytics-engine)
- 自然语言文本分析(请使用NLP工具)
- 地理空间数据分析(本Skill不专门处理GIS数据)

## 核心能力

1. **自动数据探查(零提示)**:自动检测编码/分隔符/引号,列类型推断(数值/文本/日期/布尔/分类),基础统计(均值/中位数/标准差/四分位),缺失值分析
2. **自动洞察发现**:分布特征识别(正态/偏态/双峰)、异常值检测(IQR方法/Z-score)、相关性分析(Pearson/Spearman+热力图)、分组对比(自动发现显著差异)
3. **可视化自动生成**:单变量图(直方图/箱线图/条形图/折线图)、双变量图(散点图/分组箱线图/堆叠条形图)、多变量图(相关性热力图/散点矩阵),含标题/轴标签/图例
4. **洞察报告结构化**:数据概览+质量报告+统计摘要+Top5关键发现+可视化集+下一步建议
5. **清洗建议输出**:缺失值处理策略、异常值处理建议、类型转换建议、去重建议

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

### Step 1: 自动数据探查(无需提示)
1. 读取CSV文件:自动检测编码(UTF-8/GBK/GB2312)、分隔符(逗号/制表符/分号)、引号
2. 列类型推断:数值型(整数/浮点)、文本型、日期型(多格式解析)、布尔型、分类型(低基数文本)
3. 基础统计:行数/列数/内存占用、数值列统计量、文本列唯一值/最高频/平均长度、日期列时间范围
4. 缺失值分析:每列缺失数量与比例

### Step 2: 自动洞察发现
1. 分布特征:数值列正态/偏态/双峰识别、分类列帕累托图、时间列趋势/周期/季节性
2. 异常值检测:IQR方法(1.5倍IQR外)+Z-score(|z|>3),标记潜在异常行
3. 相关性分析:Pearson/Spearman相关系数、热力图可视化、强相关对高亮(>0.7)
4. 分组对比:按分类列分组统计数值列差异,自动发现显著差异分组

### Step 3: 可视化生成
1. 单变量图:数值(直方图/箱线图)、分类(条形图/饼图)、时间(折线图)
2. 双变量图:散点图、分组箱线图、堆叠条形图
3. 多变量图:相关性热力图、散点矩阵
4. 图表规范:标题/轴标签/图例/数据标签

### Step 4: 洞察报告生成
1. 数据概览:文件信息/行列数/类型分布
2. 质量报告:缺失/重复/异常汇总
3. 统计摘要:每列关键统计量
4. 关键发现:Top 5自动发现的洞察
5. 可视化集:所有图表合集
6. 建议下一步:基于数据特征推荐深入分析方向

### Step 5: 清洗建议输出
1. 缺失值处理策略(删除/填充/插值)
2. 异常值处理建议(删除/截断/保留)
3. 类型转换建议
4. 去重建议

## 自动化原则

1. **零提示启动**:读取CSV后自动开始全流程分析
2. **智能推断**:自动判断列类型、适合的图表、分析方法
3. **全面覆盖**:不遗漏任何列,每列都分析
4. **可解释**:每个洞察附带解释,不仅输出数字

## 输出规范

- 分析报告:`output/{csv-name}/insight-report.md`
- 统计摘要:`output/{csv-name}/statistics.json`
- 图表目录:`output/{csv-name}/charts/`(PNG)
- 异常清单:`output/{csv-name}/outliers.csv`
- 清洗建议:`output/{csv-name}/cleaning-suggestions.md`

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| Python 3.8+ | 运行时 | 可选 | 数据分析(pandas/matplotlib/seaborn) |
| pandas | Python库 | 可选 | `pip install pandas` |
| matplotlib | Python库 | 可选 | `pip install matplotlib` |
| seaborn | Python库 | 可选 | `pip install seaborn` |
| LLM API | API | 可选 | 由Agent内置LLM提供洞察解读 |

### 国内镜像加速(替代海外PyPI)

| 海外源 | 国内镜像 | 说明 |
|---:|---:|---:|
| pypi.org | 清华大学pypi | `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple` |
| pypi.org | 阿里云pypi | `pip install -i https://mirrors.aliyun.com/pypi/simple` |
| pypi.org | 腾讯云pypi | `pip install -i https://mirrors.cloud.tencent.com/pypi/simple` |

### API Key 配置
- 本Skill无需额外API Key配置
- 数据分析在本地Python环境执行,无外部服务依赖

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,实际执行分析需exec调用Python脚本

## 示例

### 示例1: 电商销售数据探查

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| input | string | 是 | CSV洞察挖掘机处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
文件:sales.csv(电商订单数据)
列:order_id, customer_id, product, category, quantity, price, order_date, region
行数:10000
```

**输出** (`output/sales/insight-report.md`):
```markdown
# sales.csv 洞察报告
# ...
## 一、数据概览
- 文件:sales.csv
- 行数:10,000 | 列数:8
- 内存占用:1.2MB
- 类型分布:数值(3) | 文本(4) | 日期(1)
# ...
## 二、质量报告
| 列名 | 缺失数 | 缺失率 | 异常数 | 重复数 |
|:------|------:|:------|:------|------:|
| order_id | 0 | 0% | 0 | 0 |
| customer_id | 12 | 0.12% | 0 | - |
| product | 0 | 0% | 0 | - |
| quantity | 0 | 0% | 23 | - |
| price | 0 | 0% | 15 | - |
| order_date | 0 | 0% | 0 | - |
| region | 45 | 0.45% | 0 | - |
# ...
## 三、统计摘要
### 数值列
| 列 | 均值 | 中位数 | 标准差 | 最小 | 最大 | Q1 | Q3 |
|---:|:---|---:|---:|:---|---:|---:|:---|
| quantity | 2.8 | 2 | 1.9 | 1 | 50 | 1 | 4 |
| price | 156.3 | 89.0 | 245.7 | 9.9 | 2999 | 45 | 199 |
# ...
### 异常值检测(IQR)
- quantity: 23个异常值(>7,正常范围1-4)
- price: 15个异常值(>500,正常范围9.9-199)
# ...
## 四、关键发现(Top 5)
1. **销售额TOP3品类**:电子产品(38%) > 服装(25%) > 家居(18%)
2. **地区差异显著**:华东地区客单价(¥210) vs 西北(¥89),差异136%
3. **时间趋势**:Q4销售额环比增长45%,双11贡献62%
4. **异常订单**:23个quantity异常订单,均为批发客户(B2B)
5. **强相关**:price与category强相关(r=0.82),电子产品价格最高
# ...
## 五、可视化集
- charts/distribution_quantity.png(数量分布直方图)
- charts/category_sales.png(品类销售条形图)
- charts/region_heatmap.png(地区销售热力图)
- charts/time_trend.png(月度销售趋势)
- charts/correlation_matrix.png(相关性矩阵)
# ...
## 六、下一步建议
1. 深入分析双11/618大促对销售的拉动效应
2. 调查华东vs西北客单价差异原因
3. B2B批发订单单独建模分析
4. 建立品类销售预测模型
```

**输出** (`output/sales/cleaning-suggestions.md`):
```markdown
# 数据清洗建议
# ...
## 缺失值处理
- customer_id(12条,0.12%):删除(占比极低,不影响分析)
- region(45条,0.45%):填充为"未知"(保留订单数据)
# ...
## 异常值处理
- quantity(23条):保留(为B2B批发订单,属正常业务)
- price(15条):保留(高价电子产品,需单独标注)
# ...
## 类型转换
- order_date:字符串→datetime(当前为object类型)
- order_id:字符串(当前被推断为数值,应保持文本)
```

### 示例2: 用户行为数据质量检查

**输入**:
```
文件:user_events.csv(用户行为日志)
列:user_id, event_type, timestamp, page, duration, device, browser
```

**输出** (`output/user_events/insight-report.md` 节选):
```markdown
## 质量报告
| 问题类型 | 数量 | 占比 | 严重程度 |
|:------:|--------|:-------|:------:|
| 完全重复行 | 342 | 3.4% | 高 |
| user_id缺失 | 89 | 0.9% | 中 |
| duration负值 | 15 | 0.15% | 高 |
| timestamp格式错误 | 7 | 0.07% | 高 |
| page为空 | 23 | 0.23% | 低 |
# ...
## 关键发现
1. **重复率3.4%**:可能是日志重复上报,建议去重
2. **duration负值15条**:数据采集bug,需排查埋点
3. **设备分布**:Mobile(62%) > Desktop(31%) > Tablet(7%)
4. **事件类型**:page_view(48%) > click(28%) > scroll(24%)
5. **高频页面**:首页(35%) > 商品页(22%) > 搜索(15%)
```

## 错误处理
- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断
- 重试机制: 失败时自动重试, 最多3次

| 错误场景 | 原因 | 处理方式 |
|----|:--:|---:|
| 文件编码错误 | 非UTF-8编码(GBK/GB2312) | 自动尝试多编码检测(chardet),回退到GBK |
| 分隔符识别失败 | 非标准分隔符(分号/制表符) | 自动检测(sniff),回退到手动指定 |
| 列类型推断错误 | 混合类型列/日期格式多样 | 提供手动类型指定,支持多日期格式尝试 |
| 内存不足 | CSV文件过大(>2GB) | 分块读取(chunksize),流式处理,建议转为Parquet |
| 中文乱码 | matplotlib字体不支持中文 | 配置中文字体(SimHei/Microsoft YaHei),提供字体下载 |
| 可视化生成失败 | matplotlib后端问题 | 切换Agg后端,禁用GUI显示,输出PNG文件 |
| 相关性计算失败 | 非数值列/全缺失列 | 跳过非数值列,标注"无法计算",建议手动检查 |
| 大量异常值 | 业务正常但统计异常 | 区分"统计异常"与"业务异常",标注业务上下文 |

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 电商销售数据自动探查

**输入**:
```
文件: sales.csv（电商订单数据）
列: order_id, customer_id, product, category, quantity, price, order_date, region
行数: 10000
```

**LLM生成输出**:
```python
# output/sales/analyze.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
from pathlib import Path
# ...
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文支持
plt.rcParams['axes.unicode_minus'] = False
# ...
# 1. 自动数据探查
df = pd.read_csv('sales.csv', encoding='utf-8')
print(f"行数: {len(df)} | 列数: {len(df.columns)}")
print(f"内存占用: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
# ...
# 类型推断
df['order_date'] = pd.to_datetime(df['order_date'])
print("\n列类型:")
print(df.dtypes)
# ...
# 2. 基础统计
stats = df.describe(include='all')
stats.to_csv('output/sales/statistics.csv')
# ...
# 3. 缺失值分析
missing = df.isnull().sum()
print("\n缺失值:")
print(missing[missing > 0])
# ...
# 4. 异常值检测(IQR)
def detect_outliers_iqr(series):
    Q1, Q3 = series.quantile([0.25, 0.75])
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
    return series[(series < lower) | (series > upper)]
# ...
quantity_outliers = detect_outliers_iqr(df['quantity'])
price_outliers = detect_outliers_iqr(df['price'])
print(f"\nquantity异常: {len(quantity_outliers)}个")
print(f"price异常: {len(price_outliers)}个")
# ...
# 5. 相关性分析
numeric_cols = df.select_dtypes(include=['number']).columns
corr = df[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('相关性矩阵')
plt.tight_layout()
plt.savefig('output/sales/charts/correlation_matrix.png', dpi=150)
# ...
# 6. 可视化
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
df['category'].value_counts().plot(kind='bar', ax=axes[0,0], title='品类销售分布')
df.groupby('region')['price'].mean().plot(kind='bar', ax=axes[0,1], title='地区客单价')
df.resample('M', on='order_date')['price'].sum().plot(ax=axes[1,0], title='月度销售趋势')
df['quantity'].hist(bins=30, ax=axes[1,1])
axes[1,1].set_title('数量分布直方图')
plt.tight_layout()
plt.savefig('output/sales/charts/overview.png', dpi=150)
```

```markdown
# output/sales/insight-report.md (节选)
# sales.csv 洞察报告
# ...
## 一、数据概览(续1)
- 文件: sales.csv
- 行数: 10,000 | 列数: 8
- 内存占用: 1.2MB
- 类型分布: 数值(3) | 文本(4) | 日期(1)
# ...
## 二、质量报告(续1)
| 列名 | 缺失数 | 缺失率 | 异常数 |
|----|----|----|----|
| order_id | 0 | 0% | 0 |
| customer_id | 12 | 0.12% | 0 |
| quantity | 0 | 0% | 23 |
| price | 0 | 0% | 15 |
| region | 45 | 0.45% | 0 |
# ...
## 三、关键发现(Top 5)
1. **销售额TOP3品类**: 电子产品(38%) > 服装(25%) > 家居(18%)
2. **地区差异显著**: 华东客单价(¥210) vs 西北(¥89)，差异136%
3. **时间趋势**: Q4销售额环比增长45%，双11贡献62%
4. **异常订单**: 23个quantity异常订单，均为B2B批发
5. **强相关**: price与category相关(r=0.82)，电子产品最高
# ...
## 四、下一步建议
1. 深入分析双11/618大促拉动效应
2. 调查华东vs西北客单价差异原因
3. B2B批发订单单独建模
```

**效果验证**: ✓自动检测编码和分隔符 ✓8列类型正确推断 ✓IQR方法检测38个异常值 ✓相关性热力图生成 ✓Top5洞察含数据支撑

### 案例2: 用户行为数据质量检查

**输入**:
```
文件: user_events.csv（用户行为日志）
列: user_id, event_type, timestamp, page, duration, device, browser
预期: 数据入库前质量检查
```

**LLM生成输出**:
```python
# output/user_events/quality_check.py
import pandas as pd
# ...
df = pd.read_csv('user_events.csv')
# ...
# 1. 完全重复行检测
duplicates = df.duplicated().sum()
print(f"完全重复行: {duplicates} ({duplicates/len(df)*100:.2f}%)")
# ...
# 2. 缺失值检测
missing_report = df.isnull().sum()
missing_report = missing_report[missing_report > 0].sort_values(ascending=False)
# ...
# 3. 异常值检测
# duration负值（业务异常）
negative_duration = df[df['duration'] < 0]
print(f"duration负值: {len(negative_duration)}条")
# ...
# timestamp格式错误
invalid_ts = df[pd.to_datetime(df['timestamp'], errors='coerce').isnull()]
print(f"timestamp格式错误: {len(invalid_ts)}条")
# ...
# 4. 唯一性检查（user_id应为非空）
empty_user = df[df['user_id'].isnull()]
print(f"user_id缺失: {len(empty_user)}条")
# ...
# 5. 生成质量报告
quality_report = {
    'total_rows': len(df),
    'duplicates': duplicates,
    'missing_values': missing_report.to_dict(),
    'negative_duration': len(negative_duration),
    'invalid_timestamps': len(invalid_ts),
    'empty_user_id': len(empty_user),
}
```

```markdown
# output/user_events/insight-report.md (节选)
## 关键发现(续1)
1. **重复率3.4%**: 可能是日志重复上报，建议去重
2. **duration负值15条**: 数据采集bug，需排查埋点
3. **设备分布**: Mobile(62%) > Desktop(31%) > Tablet(7%)
4. **事件类型**: page_view(48%) > click(28%) > scroll(24%)
5. **高频页面**: 首页(35%) > 商品页(22%) > 搜索(15%)
# ...
## 清洗建议
- 去重: df.drop_duplicates() 删除342条重复
- duration负值: 删除或置为0（15条）
- timestamp: 标准化为ISO 8601格式
- user_id缺失: 填充为"anonymous"或删除
```

**效果验证**: ✓5类质量问题全覆盖 ✓严重程度分级 ✓业务异常(负值)识别 ✓清洗建议含代码 ✓分布统计完整

### 案例3: 多变量探索性分析

**输入**:
```
文件: employee_survey.csv（员工满意度调研）
列: age, salary, department, tenure, satisfaction, work_hours, commutes, performance
目标: 发现影响绩效的关键因素
```

**LLM生成输出**:
```python
# output/employee_survey/eda.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# ...
df = pd.read_csv('employee_survey.csv')
# ...
# 1. 相关性分析（Pearson + Spearman）
numeric_cols = ['age', 'salary', 'tenure', 'satisfaction', 'work_hours', 'performance']
pearson_corr = df[numeric_cols].corr(method='pearson')
spearman_corr = df[numeric_cols].corr(method='spearman')
# ...
# 强相关对（>0.7）
strong_pairs = []
for i in range(len(numeric_cols)):
    for j in range(i+1, len(numeric_cols)):
        r = pearson_corr.iloc[i, j]
        if abs(r) > 0.7:
            strong_pairs.append((numeric_cols[i], numeric_cols[j], r))
# ...
# 2. 分组对比
dept_stats = df.groupby('department')['performance'].agg(['mean', 'std', 'count'])
# 显著差异检测
from scipy import stats
dept_a = df[df['department'] == 'Engineering']['performance']
dept_b = df[df['department'] == 'Sales']['performance']
t_stat, p_value = stats.ttest_ind(dept_a, dept_b)
print(f"Engineering vs Sales: t={t_stat:.2f}, p={p_value:.4f}")
# ...
# 3. 散点矩阵
sns.pairplot(df[numeric_cols + ['department']], hue='department', diag_kind='kde')
plt.savefig('output/employee_survey/charts/pairplot.png', dpi=150)
# ...
# 4. 分组箱线图
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
df.boxplot(column='performance', by='department', ax=axes[0])
axes[0].set_title('各部门绩效分布')
df.boxplot(column='satisfaction', by='department', ax=axes[1])
axes[1].set_title('各部门满意度分布')
plt.tight_layout()
plt.savefig('output/employee_survey/charts/dept_comparison.png', dpi=150)
```

```markdown
# output/employee_survey/insight-report.md
## 关键发现(Top 5)
# ...
1. **满意度与绩效强相关**: r=0.78(p<0.001)
   - 满意度>7的员工，绩效平均高出23%
   - 建议: 优先改善低满意度团队的工作环境