---
slug: "py-data-analyzer"
name: "py-data-analyzer"
version: 1.0.1
displayName: "Python数据分析(专业版)"
summary: "企业级Python数据分析方案，支持机器学习建模、时间序列预测、大数据处理与自动化报表。。Python数据分析专业版是一套面向数据科学家与企业级团队的高级数据分析解决方案，在免费版基础上扩展"
license: "Proprietary"
edition: "pro"
description: |-
  Python数据分析专业版是一套面向数据科学家与企业级团队的高级数据分析解决方案，在免费版基础上扩展出机器学习建模、时间序列预测、多维透视与交互式仪表盘、大数据处理、自动化报表与调度等能力。核心能力：提供特征工程与模型训练流程、ARIMA / Prophet 时间序列预测方案、多维数据 OLAP 透视与 Plotly 交互式可视化、Dask / Spark 大数据处理集成、定时报表自动生成与邮件分发
tags:
  - 数据分析
  - 集成工具
  - Python
  - 企业级
  - 专业版
  - 数据处理
  - 工具
tools:
  - read
  - exec
  - write
  - glob
homepage: ""
# 定价元数据
category: "Research"
---
# Python数据分析(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Python数据分析(专业版)Python数据分析 | 不支持 | 支持 |
| Python数据分析(专业版)支持机器学习建模 | 不支持 | 支持 |
| Python数据分析(专业版)大数据处理 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |

## 核心能力

### 能力一：机器学习建模
提供从特征工程到模型训练、评估、部署的完整流程。覆盖回归、分类、聚类三大任务类型，支持交叉验证、超参数调优、模型解释.
| 任务类型 | 典型算法 | 评估指标 | 适用场景 |
|:-----|:-----|:-----|:-----|
| 回归 | 线性回归、XGBoost、LightGBM | RMSE、MAE、R² | 销售预测、价格预测 |
| 分类 | 逻辑回归、随机森林、XGBoost | Accuracy、F1、AUC | 流失预测、风控识别 |
| 聚类 | K-Means、DBSCAN、层次聚类 | 轮廓系数、CH 指数 | 用户分群、异常检测 |

**处理**: 解析能力一：机器学习建模的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回能力一：机器学习建模的处理结果,包含执行状态码、结果数据和执行日志。### 能力二：时间序列预测
提供 ARIMA、Prophet、LSTM 三种主流时间序列预测方案，支持季节性分解、趋势预测、置信区间计算.
**处理**: 解析能力二：时间序列预测的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回能力二：时间序列预测的处理结果,包含执行状态码、结果数据和执行日志。### 能力三：多维数据透视与交互式可视化
基于 Plotly 与 Dash 构建交互式仪表盘，支持下钻、筛选、联动等交互操作，适合业务自助分析.
**输入**: 用户提供能力三：多维数据透视与交互式可视化所需的指令和必要参数.
**输出**: 返回能力三：多维数据透视与交互式可视化的处理结果,包含执行状态码、结果数据和执行日志。### 能力四：大数据处理集成

当 pandas 无法承载数据量时，提供 Dask（单机扩展）、PySpark（集群分布式）、DuckDB（SQL 分析）三种方案的选型建议与代码模板.
### 能力五：自动化报表生成与调度
将分析流程封装为定时任务，自动从数据源拉取数据、执行分析、生成报表、分发邮件或企业微信.
**输入**: 用户提供能力五：自动化报表生成与调度所需的指令和必要参数。### 能力六：特征工程流水线
提供特征提取、特征选择、特征变换的标准化流水线，支持缺失值处理、编码、缩放、特征交叉等操作.
**输出**: 返回能力六：特征工程流水线的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`能力五：自动化报表生成与调度`的配置文档进行参数调优
### 任务类型

针对任务类型,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供任务类型相关的配置参数、输入数据和处理选项.
**输出**: 返回任务类型的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`任务类型`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：销售预测与库存优化

基于历史销售数据训练预测模型，预测未来 30 天各品类销量，结合库存水平给出补货建议，降低库存成本.
### 场景二：用户分群与精准营销

基于用户行为数据（浏览、购买、互动）进行聚类分析，识别高价值用户群体，制定差异化营销策略.
### 场景三：金融风控建模

基于用户信用数据训练分类模型，预测违约概率，结合业务规则设定审批阈值，平衡风险与通过率.
### 场景四：海量日志分析

每日 TB 级的访问日志，使用 PySpark 分布式处理，提取异常模式、性能瓶颈、用户路径等关键信息.
### 场景五：定期业务报表自动化

每周一自动生成本周业务报表，包含核心 KPI、趋势分析、异常告警，自动分发到管理层邮箱与企业微信群.
## 使用流程

本助手为知识库型 Skill，需要 Python 环境与相关库支持。直接在 Agent 对话中描述你的分析需求即可获取方案.
**典型提问模板**：

```
我有 3 年的销售数据，想预测未来 3 个月的销量，用什么模型？
```

```
我的用户行为日志每天 50GB，pandas 扛不住，有什么方案？
```

```
需要每周自动生成业务报表并分发到企业微信，如何实现？
```

Agent 会根据需求匹配对应的能力模块，输出"业务理解 → 方案设计 → 代码实现 → 评估方法 → 部署建议"五段式方案.
**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | py-data-analyzer处理的内容输入 |,  |
| content | string | 否 | py-data-analyzer处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "analyzer 相关配置参数",
    result: "analyzer 相关配置参数",
    result: "analyzer 相关配置参数",
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

| 症状 | 可能原因 | 排查方法 | 对策 |
|:---:|:---:|:---:|:---:|
| 模型过拟合 | 特征过多或树太深 | 对比训练集与测试集指标 | 减少特征、限制深度、正则化 |
| 模型欠拟合 | 特征不足或模型太简单 | 查看学习曲线 | 增加特征、换更强模型 |
| 时间序列预测偏差大 | 季节性未捕捉 | 查看残差图 | 调整季节性参数 |
| Dask 内存不足 | 分块过大 | 查看 blocksize | 减小 blocksize |
| 报表任务失败 | 数据源异常或代码报错 | 查看任务日志 | 加告警与机制 |
| 特征重要性异常 | 数据泄漏 | 检查特征来源 | 移除未来信息特征 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.9+（推荐 3.11+）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| pandas / numpy | 库 | 必需 | pip install pandas numpy |
| scikit-learn | 库 | 必需 | pip install scikit-learn |
| matplotlib / seaborn | 库 | 推荐 | pip install matplotlib seaborn |
| plotly / dash | 库 | 推荐 | pip install plotly dash |
| prophet | 库 | 可选 | pip install prophet |
| xgboost / lightgbm | 库 | 可选 | pip install xgboost lightgbm |
| dask | 库 | 可选 | pip install dask |
| pyspark | 库 | 可选 | pip install pyspark |
| duckdb | 库 | 可选 | pip install duckdb |
| apscheduler | 库 | 可选 | pip install apscheduler |

### API Key 配置
- 本专业版为知识库型 Skill，自身不需要 API Key
- 若分析涉及外部数据源 API（如数据库、云存储、第三方数据服务），相关凭据由用户自行配置于环境变量中
- 报表邮件服务的 SMTP 凭据应存储于密钥管理服务中
- 禁止在 SKILL.md 或脚本中硬编码数据源凭据或 API Token

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行Python代码）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent输出企业级数据分析方案

## 案例展示

### 机器学习建模流程

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# ...
def build_classification_model(df, features, target):
    """分类模型构建流水线"""
    X = df[features]
    y = df[target]
# ...
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
# ...
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
# ...
    # 交叉验证
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='f1')
    print(f"交叉验证 F1: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
# ...
    # 训练与评估
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    y_proba = pipeline.predict_proba(X_test)[:, 1]
# ...
    print(classification_report(y_test, y_pred))
    print(f"AUC: {roc_auc_score(y_test, y_proba):.4f}")
# ...
    return pipeline
```

### 时间序列预测（Prophet）

```python
from prophet import Prophet
import pandas as pd
# ...
def forecast_sales(df, periods=90):
    """使用 Prophet 预测销售趋势"""
    # Prophet 要求列名为 ds 和 y
    data = df.rename(columns={'date': 'ds', 'amount': 'y'})
# ...
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,
        changepoint_prior_scale=0.05
    )
    model.fit(data)
# ...
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
# ...
    # 可视化
    fig = model.plot(forecast)
    fig2 = model.plot_components(forecast)
# ...
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
```

### 大数据处理（Dask）

```python
import dask.dataframe as dd
# ...
def process_large_csv(filepath):
    """使用 Dask 处理超大 CSV"""
    ddf = dd.read_csv(filepath, blocksize='64MB')
# ...
    # 惰性计算，调用 compute 才真正执行
    result = (
        ddf[ddf['amount'] > 0]
        .groupby('category')
        .agg({
            'amount': ['mean', 'sum', 'count'],
            'user_id': 'nunique'
        })
        .compute()
    )
# ...
    return result
```

### 自动化报表调度

```python
from apscheduler.schedulers.blocking import BlockingScheduler
import smtplib
from email.mime.text import MIMEText
import pandas as pd
# ...
def generate_weekly_report():
    """生成周报表并发送邮件"""
    # 1. 拉取数据
    df = pd.read_sql("SELECT * FROM sales WHERE date >= CURRENT_DATE - 7", con)
# ...
    # 2. 计算指标
    summary = df.groupby('category').agg(
        revenue=('amount', 'sum'),
        orders=('order_id', 'count')
    )
# ...
    # 3. 生成 HTML 报表
    html = summary.to_html()
# ...
    # 4. 发送邮件
    msg = MIMEText(html, 'html')
    msg['Subject'] = '周业务报表'
    msg['From'] = 'analytics@company.com'
    msg['To'] = 'management@company.com'
# ...
    with smtplib.SMTP('smtp.company.com') as server:
        server.send_message(msg)
# ...
# 每周一早上 8 点执行
scheduler = BlockingScheduler()
scheduler.add_job(generate_weekly_report, 'cron', day_of_week='mon', hour=8)
scheduler.start()
```

## 常见问题

### Q1：如何选择机器学习算法？

优先从简单模型开始：线性回归/逻辑回归 → 随机森林 → XGBoost/LightGBM。简单模型可解释性好，效果不够再换复杂模型。避免一上来就用深度学习.
### Q2：特征工程有哪些常用技巧？

数值特征：对数变换、分箱、标准化；分类特征：One-Hot 编码、目标编码；时间特征：提取年月日、是否节假日；交叉特征：组合两个特征生成新特征.
### Q3：模型评估指标怎么选？

回归看 RMSE（关注大误差）或 MAE（关注平均误差）；分类看业务目标，关注准确率选 Accuracy，关注少数类选 F1 或 AUC；聚类看轮廓系数或业务可解释性.
### Q4：Prophet 和 ARIMA 怎么选？

Prophet 适合有强季节性、节假日效应、缺失值多的数据，配置简单；ARIMA 适合平稳序列，需要调参但理论严谨。不确定时两个都试，对比效果.
### Q5：Dask 和 PySpark 怎么选？

单机扩展选 Dask，API 与 pandas 几乎一致，迁移成本低；集群分布式选 PySpark，适合 TB 级以上数据与多节点并行。数据量在 10-100GB 优先考虑 DuckDB.
### Q6：报表自动化如何保证数据质量？

在报表生成流程中加入数据质量检查：行数是否在合理范围、关键指标是否为空、同比环比是否异常。检查不通过则告警并暂停报表发送.
### Q7：模型上线后效果下降怎么办？

可能是数据漂移（data drift）导致。定期监控特征分布与预测分布的变化，超过阈值时触发模型重训练。建议每月 review 一次模型效果.
### Q8：如何处理类别不平衡？

常用方法：过采样少数类（SMOTE）、欠采样多数类、调整类别权重、使用 F1/AUC 等不平衡友好指标。避免只看 Accuracy.
### Q9：特征数量多少合适？

经验法则：样本数应为特征数的 10 倍以上。特征过多时使用特征选择（基于重要性、相关性、方差）或降维（PCA）减少维度.
### Q10：如何向业务方解释模型结果？

使用 SHAP 或 LIME 等模型解释工具，展示特征对预测结果的贡献度。避免用业务方听不懂的术语，用具体案例说明模型如何决策.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

