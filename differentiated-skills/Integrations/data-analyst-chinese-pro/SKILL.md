---
slug: data-analyst-chinese-pro
name: data-analyst-chinese-pro
version: "1.0.0"
displayName: 中文数据分析(专业版)
summary: 全功能中文数据分析平台,支持时序分解、假设检验、大数据集批处理与自定义报告模板。
license: MIT
edition: pro
description: |-
  中文数据分析专业版面向专业数据分析师、BI 工程师与数据团队负责人,提供完整的数据分析生产线能力。

  核心能力:
  - 涵盖免费版全部能力,无条数与功能限制
  - 时间序列分析:重采样、滚动窗口、季节性分解、ARIMA/Prophet 预测
  - 假设检验与 A/B 测试:t 检验、卡方、方差分析、效应量与置信区间
  - 大数据集批处理:Dask/Polars 后端,千万级数据增量计算
  - 自定义报告模板:Jinja2 模板引擎,HTML/PDF/PPT 多格式输出
  - 定时分析任务与邮件分发,自动化周报/月报
  - 与企业数据库深度集成,支持 `PostgreSQL`/MySQL/ClickHouse

  适用场景:
  - 企业级数据分析团队日常工作流
  - 自动化周报/月报生产与分发
  - A/B 实验平台结论自动化判定
  - 大规模用户行为与漏斗分析

  差异化:相比免费版,专业版补齐"时序预测、假设检验、大数据、自动化"四大短板,形成完整的中文数据分析生产线。

  触发关键词:时序分解、A/B测试、假设检验、大数据、自定义报告、定时任务、`PostgreSQL`、企业集成
tags:
  - 数据分析
  - 时序预测
  - 假设检验
  - 集成工具
tools:
  - read
  - exec
---

# 中文数据分析 专业版

## 一、概述

中文数据分析专业版在免费版的日常分析能力之上,补齐"时序预测、假设检验、大数据批处理、自动化分发"四大短板,形成完整的中文数据分析生产线。面向专业数据分析师、BI 工程师、数据团队负责人与企业决策者,适合需要深度统计建模、大规模数据处理与自动化报告分发的团队场景。

专业版支持时间序列分解与预测、假设检验与 A/B 测试自动化、千万级数据集的批处理与增量计算,以及基于 Jinja2 的自定义报告模板与定时任务分发。

## 二、核心能力

### 2.1 数据读取全封装(免费版基础 + 企业级扩展)

| 数据源 | 代码片段 | 适用场景 |
|--------|----------|----------|
| CSV / Excel / JSON | `pd.read_csv` / `read_excel` / `read_json` | 文件数据 |
| SQLite | `pd.read_sql` | 本地数据库 |
| `PostgreSQL` / MySQL | `pd.read_sql` + SQLAlchemy | 企业数据库 |
| ClickHouse | `clickhouse-driver` | OLAP 分析 |
| REST API | `requests.get` | 第三方接口 |
| 数据湖 | `pyarrow` / `duckdb` | Parquet/Arrow 文件 |

### 2.2 时间序列分析

- **重采样**:`resample('D/W/M')` 按日/周/月聚合
- **滚动窗口**:`rolling(window=7).mean()` 移动平均与标准差
- **差分与百分比**:`diff()` / `pct_change()`
- **季节性分解**:`seasonal_decompose` 趋势-季节-残差分解
- **预测建模**:ARIMA、Prophet、状态空间模型

### 2.3 假设检验与 A/B 测试

| 检验类型 | 适用场景 | 关键产出 |
|----------|----------|----------|
| t 检验(独立/配对) | 均值差异 | t 值 + p 值 + 效应量 |
| 卡方检验 | 类别关联 | χ² + p 值 + Cramer's V |
| 方差分析(ANOVA) | 多组均值对比 | F 值 + p 值 + 事后检验 |
| Mann-Whitney U | 非正态分布 | U 值 + p 值 |
| 多重比较校正 | 批量检验 | Bonferroni / BH 校正后 p 值 |
| 效应量 | 业务重要性 | Cohen's d / 优势比 + 置信区间 |

### 2.4 大数据批处理

- **Dask 后端**:千万级数据集分块并行计算
- **Polars 后端**:高性能单机多线程
- **增量计算**:基于数据版本号做差量处理
- **检查点**:长任务落盘,失败可断点续跑
- **资源管理**:内存监控与自动溢写磁盘

### 2.5 自定义报告模板

- **Jinja2 引擎**:支持条件渲染、循环、宏定义
- **多格式输出**:Markdown / HTML / PDF / PPT
- **品牌化**:自定义 Logo、配色、字体
- **模板库**:内置电商/SaaS/金融/游戏/内容 5 套行业模板
- **变量插值**:动态嵌入图表、表格、结论卡片

### 2.6 定时任务与邮件分发

- **cron 调度**:标准 5 段式 cron 表达式
- **数据源自动拉取**:任务触发时拉取最新数据
- **报告自动生成**:执行分析 → 渲染模板 → 输出文件
- **多渠道分发**:邮件 / 企业 IM / Webhook / OSS
- **失败重试**:指数退避,最多 3 次
- **审计日志**:任务执行历史与结果留痕

### 2.7 企业数据库深度集成

- **`PostgreSQL`**:支持窗口函数、CTE、JSONB、物化视图
- **MySQL**:支持读写分离与连接池
- **ClickHouse**:OLAP 场景高速聚合
- **凭证安全**:统一通过环境变量传入

## 三、使用场景

### 3.1 按角色场景矩阵

| 角色 | 场景 | 关键能力 | 输出形态 |
|------|------|----------|----------|
| 数据分析师 | A/B 实验结论判定 | 假设检验 + 多重比较校正 | 结论表 + 决策建议 |
| BI 工程师 | 大屏数据底表生产 | 大数据批处理 + 增量更新 | 物化视图 + 数据集 |
| 数据团队负责人 | 周报/月报自动化 | 定时任务 + 邮件分发 | PDF 报告 + 邮件 |
| 业务决策者 | 关键指标预测 | 时序分解 + Prophet 预测 | 预测曲线 + 置信区间 |

### 3.2 典型工作流

```text
1. 每周一 09:00 定时任务触发
2. 自动从 PostgreSQL 拉取上周销售数据(增量)
3. 执行数据清洗与时序分解
4. 渲染 Jinja2 报告模板生成 PDF
5. 邮件分发至增长团队邮件组
6. 任务执行结果写入审计日志
```

## 四、快速开始

预计上手时间:**< 120 秒**(企业数据源需配置凭证)。

### 4.1 单次时序分析

```text
请对销售数据做时序分析:
- 数据源: postgres(凭证从环境变量读取)
- 表: daily_sales(2023-01-01 至 2024-12-31)
- 关注: 月度趋势 + 季节性 + 2025 年预测
- 输出: 分解图 + 预测曲线 + PDF 报告
```

### 4.2 A/B 测试结论判定

```text
请判定 A/B 测试:
- 实验组: 10000 人,转化率 5.2%
- 对照组: 9980 人,转化率 4.7%
- 要求: t 检验 + 效应量 + 95% 置信区间
- 输出: 结论 + 决策建议 + 报告卡片
```

### 4.3 定时报告任务

```text
请配置每周一定时任务:
- 数据源: PostgreSQL 销售明细表
- 分析: 上周销售汇总 + Top 10 商品 + 异动归因
- 模板: 电商行业模板 + 公司品牌
- 分发: 邮件 + 企业 IM Webhook
- 失败重试: 3 次,指数退避
```

## 五、配置示例

### 5.1 企业数据源配置

```yaml
# config/datasources.yaml
warehouse:
  type: postgres
  host: ${DB_HOST}
  port: ${DB_PORT}
  user: ${DB_USER}
  password: ${DB_PASSWORD}
  database: ${DB_NAME}
  pool_size: 10
  read_only: true

olap:
  type: clickhouse
  host: ${CH_HOST}
  user: ${CH_USER}
  password: ${CH_PASSWORD}
  database: analytics
```

### 5.2 时序分析代码

```python
from statsmodels.tsa.seasonal import seasonal_decompose

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# 重采样与滚动
daily = df.resample('D').sum()
daily['rolling_mean'] = daily['sales'].rolling(window=7).mean()
daily['rolling_std'] = daily['sales'].rolling(window=7).std()

# 季节性分解
result = seasonal_decompose(daily['sales'], model='additive', period=365)
result.plot()

# Prophet 预测
from prophet import Prophet
m = Prophet(yearly_seasonality=True)
m.fit(df_prophet)
future = m.make_future_dataframe(periods=90)
forecast = m.predict(future)
```

### 5.3 假设检验代码

```python
from scipy import stats

# 独立样本 t 检验
t_stat, p_val = stats.ttest_ind(exp_group, ctrl_group)

# 效应量(Cohen's d)
pooled_std = ((len(exp) - 1) * exp.std()**2 + (len(ctrl) - 1) * ctrl.std()**2) / (len(exp) + len(ctrl) - 2)
pooled_std = pooled_std ** 0.5
cohens_d = (exp.mean() - ctrl.mean()) / pooled_std

# 95% 置信区间
import statsmodels.api as sm
cm = sm.stats.CompareMeans(sm.stats.DescrStatsW(exp), sm.stats.DescrStatsW(ctrl))
ci = cm.tconfint_diff(usevar='pooled')
```

### 5.4 报告模板配置

```yaml
report:
  format: pdf
  template: ecommerce_brand
  variables:
    company_name: "示例电商"
    logo_path: assets/logo.png
    primary_color: "#E11D48"
  output_dir: reports/
  naming: "{year}{week}_{title}.pdf"
```

### 5.5 定时任务配置

```yaml
schedule:
  weekly_report:
    cron: "0 9 * * 1"  # 每周一 09:00
    analysis: weekly_sales_summary
    datasource: warehouse
    report: ecommerce_brand
    distribute:
      email: [growth@example.com]
      webhook: ${IM_WEBHOOK_URL}
    retry:
      max: 3
      backoff: exponential
```

## 六、最佳实践

- **数据源隔离**:OLTP 与 OLAP 分库,避免分析查询影响业务
- **增量优先**:大数据集优先增量计算,避免全量重算
- **检查点策略**:长任务必须落盘,异常可断点续跑
- **多重比较校正**:批量 A/B 检验必须做 BH 校正,避免假阳性
- **报告品牌化**:统一模板与配色,提升专业感
- **告警分级**:定时任务失败分 P0/P1/P2,避免告警风暴
- **凭证安全**:数据库密码、SMTP 凭证一律走环境变量
- **审计留痕**:任务执行历史与结果留痕,便于合规追溯

## 七、常见问题

### Q1: 专业版支持多大的数据集?

A: 单机模式支持千万级行(Dask/Polars 后端),集群模式可处理亿级。增量计算可显著降低重复成本。

### Q2: 时序预测准确度如何?

A: 短期(7-30 天)预测准确度较高(MAPE < 10%);中长期(>90 天)建议结合业务判断。Prophet 适合有季节性的数据,ARIMA 适合平稳数据。

### Q3: A/B 测试如何处理多重比较?

A: 专业版自动应用 BH 校正控制 FDR。严格场景(医疗/金融)可切换 Bonferroni。

### Q4: 报告模板支持哪些变量?

A: 支持 `{{ company_name }}`、`{{ date_range }}`、`{{ charts }}`、`{{ tables }}`、`{{ conclusions }}` 等变量,详见模板文档。

### Q5: 定时任务失败如何排查?

A: 查看审计日志中的执行历史,关注数据源连接、SQL 执行、模板渲染三阶段。失败自动重试 3 次,仍失败则告警。

### Q6: 是否支持与 BI 工具集成?

A: 支持输出物化视图供 Tableau / Power BI / Metabase 消费,也可输出 Parquet 文件供数据湖使用。

### Q7: 如何保障数据安全?

A: 凭证统一走环境变量,**禁止**硬编码;数据库账号最小权限原则;报告可加水印与访问控制;审计日志完整保留。

### Q8: 是否支持 MCP工具扩展?

A: 专业版支持通过 MCP工具协议接入外部数据源与计算后端,可在 `mcp_servers` 配置块中注册 MCP server 与 MCP端点,融入 MCP生态共享分析能力。

### Q9: 多个数据源如何联合分析?

A: 通过 `duckdb` 或 ETL 工具将多源数据归一至统一 Arrow/Parquet 格式后,可使用 SQL 联表查询。

### Q10: 企业级部署如何授权?

A: 企业版支持团队席位授权与 SSO 集成,具体联系销售团队。

## 八、专业版特性

本专业版相比免费版新增以下能力:

- 时间序列分析:重采样、滚动窗口、季节性分解、ARIMA/Prophet 预测
- 假设检验与 A/B 测试:t 检验、卡方、ANOVA、效应量、多重比较校正
- 大数据批处理:Dask/Polars 后端,千万级数据增量计算
- 自定义报告模板:Jinja2 引擎,Markdown/HTML/PDF/PPT 多格式
- 定时任务与邮件分发:cron 调度,多渠道分发,失败重试
- 企业数据库深度集成:`PostgreSQL`/MySQL/ClickHouse
- MCP工具集成:通过 MCP server 接入外部能力,融入 MCP生态

## 九、定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 核心清洗 + 基础统计 + 中文图表 | 个人试用 |
| 收费专业版 | ¥199/月 | 全功能 + 时序预测 + 大数据 + 自动化 | 团队/企业 |

专业版通过 SkillHub SkillPay 发布。

## 十、依赖说明

### 运行环境

- **Agent 平台**: 任意支持 SKILL.md 的 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.9+(时序与大数据需要)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| pandas | Python 库 | 必需 | `pip install pandas` |
| numpy | Python 库 | 必需 | `pip install numpy` |
| scipy | Python 库 | 必需 | `pip install scipy`(假设检验) |
| statsmodels | Python 库 | 必需 | `pip install statsmodels`(时序分解) |
| prophet | Python 库 | 可选 | `pip install prophet`(预测) |
| matplotlib | Python 库 | 必需 | `pip install matplotlib`(可视化) |
| seaborn | Python 库 | 可选 | `pip install seaborn` |
| sqlalchemy | Python 库 | 必需 | `pip install sqlalchemy`(数据库) |
| psycopg2 | Python 库 | 可选 | `pip install psycopg2-binary`(`PostgreSQL`) |
| clickhouse-driver | Python 库 | 可选 | `pip install clickhouse-driver`(ClickHouse) |
| dask | Python 库 | 可选 | `pip install dask`(大数据) |
| polars | Python 库 | 可选 | `pip install polars`(高性能) |
| jinja2 | Python 库 | 必需 | `pip install jinja2`(报告模板) |
| pyarrow | Python 库 | 可选 | `pip install pyarrow`(Parquet) |
| duckdb | Python 库 | 可选 | `pip install duckdb`(多源联表) |

### API Key 配置

- **数据库凭证**: 通过 `DB_HOST`/`DB_USER`/`DB_PASSWORD` 等环境变量传入
- **邮件 SMTP**: 通过 `SMTP_HOST`/`SMTP_USER`/`SMTP_PASSWORD` 等环境变量传入
- **Webhook**: 通过 `IM_WEBHOOK_URL` 等环境变量传入
- **禁止**: 在 SKILL.md、脚本、配置文件中硬编码任何凭证
- **推荐路径**: 凭证统一存放在 `d:\skills\.skill-credentials\` 目录(已 gitignore)

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言驱动的 AI Skill,集成时序预测、假设检验、大数据与自动化分发的完整生产线
