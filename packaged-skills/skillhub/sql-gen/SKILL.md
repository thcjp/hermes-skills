---

slug: "sql-gen"
name: "sql-gen"
version: 1.0.1
displayName: "SQL生成器(专业版)"
summary: "面向团队的自然语言转SQL专业版，含Schema感知、多表JOIN生成、性能优化建议、迁移脚本与优先支持。"
license: "Proprietary"
edition: "pro"
description: |-，可自动提升工作效率
  面向团队、企业与专业开发者的SQL生成器专业版。在免费版基础上新增Schema智能感知自动补全、复杂多表JOIN自动生成、SQL性能优化建议、数据库迁移脚本自动生成、批量SQL生成与版本管理、生成质量回归测试等高级能力，配套面向产品、开发、DBA的多角色场景指南。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策.
tags:
  - 集成工具
  - 数据库
  - SQL生成
  - 高级特性
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - 写作
  - 电商
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"

---

# SQL生成器(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| SQL生成器(专业版)多表JOIN生成 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 核心能力

| 能力分类 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 单次生成上限 | 1条 | 无上限批量生成 |
| Schema感知 | 手动提供 | 自动读取补全 |
| 多表JOIN | 不支持 | 支持复杂关联 |
| 性能优化建议 | 无 | 索引建议+重写提示 |
| 迁移脚本 | 不支持 | up/down自动生成 |
| 版本管理 | 无 | 生成历史+回归测试 |
| 优先支持 | 社区 | 工单优先响应 |
### 能力分类

针对能力分类,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力分类相关的配置参数、输入数据和处理选项.
**输出**: 返回能力分类的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力分类`的配置文档进行参数调优
### 单次生成上限

针对单次生成上限,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供单次生成上限相关的配置参数、输入数据和处理选项.
**输出**: 返回单次生成上限的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`单次生成上限`的配置文档进行参数调优
### Schema感知

针对Schema感知,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Schema感知相关的配置参数、输入数据和处理选项.
**输出**: 返回Schema感知的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Schema感知`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：Schema感知生成（开发者视角）

生成前自动连接数据库读取表结构，生成时自动补全真实字段名与类型，杜绝幻觉字段.
```python
from sql_gen_tool import ProFeatures
# ...
pro = ProFeatures(db_url="postgresql://user:pass@localhost/mydb")
pro.connect_schema()  # 自动读取所有表结构
# ...
sql = pro.generate("查询最近30天消费超1000元的用户及其订单明细")
# 自动感知 users、orders 表结构，生成含真实字段名的多表JOIN
```

### 场景二：复杂多表JOIN生成（数据工程师视角）

支持3表以上复杂关联查询的自动生成，自动选择JOIN类型与连接条件.
```text
输入：查询每个用户的最近3笔订单及对应商品名称，按用户名排序
# ...
输出：
WITH recent_orders AS (
    SELECT o.*, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn
    FROM orders o
)
SELECT u.name, ro.total, p.product_name, ro.created_at
FROM users u
INNER JOIN recent_orders ro ON ro.user_id = u.id AND ro.rn <= 3
INNER JOIN order_items oi ON oi.order_id = ro.id
INNER JOIN products p ON p.id = oi.product_id
ORDER BY u.name;
```

### 场景三：性能优化建议（DBA视角）

生成SQL后自动分析执行计划，给出索引建议与重写提示.
```python
result = pro.generate_with_advice("查询上月销售额Top10商品")
# 返回：SQL + 优化建议
# 建议1：products表缺少(sales, created_at)复合索引，预计提升5倍
# 建议2：子查询可改写为JOIN，减少中间结果集
```

### 场景四：迁移脚本生成（架构师视角）

根据Schema变更需求自动生成up/down双向迁移脚本，支持版本化管理.
```python
pro.generate_migration(
    change="为orders表增加shipping_address字段，并创建按状态分组的部分索引",
    version="005_add_orders_shipping"
)
# 生成 005_add_orders_shipping_up.sql 和 005_add_orders_shipping_down.sql
```

### 场景五：批量生成与回归（团队视角）

批量生成一组业务SQL并纳入版本管理，每次Schema变更后跑回归测试，确保已有SQL不失效.
```python
pro.batch_generate(
    prompts_file="business_queries.yaml",
    output_dir="generated_sql/"
)
pro.regression_test(baseline_dir="generated_sql/v1.2/")
```

## 使用流程

### 优秀步：连接数据库感知Schema

```python
from sql_gen_tool import ProFeatures
# ...
pro = ProFeatures(db_url="postgresql://user:pass@localhost/mydb")
pro.connect_schema()  # 自动读取表结构
```

### 第二步：生成带优化建议的SQL

```python
result = pro.generate_with_advice("查询用户消费排行前10")
print(result.sql)
print(result.advice)  # 优化建议
```

### 第三步：生成迁移脚本

```python
pro.generate_migration(change="为users表增加phone字段", version="006_add_phone")
```

完整上手时间约120秒.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | sql-gen处理的内容输入 |,  |
| content | string | 否 | sql-gen处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
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
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| psycopg2 | Python包 | 可选 | `pip install psycopg2`（`PostgreSQL`驱动） |
| pymysql | Python包 | 可选 | `pip install pymysql`（MySQL驱动） |
| pyodbc | Python包 | 可选 | `pip install pyodbc`（SQL Server驱动） |
| sqlparse | Python包 | 可选 | `pip install sqlparse`（SQL格式化） |

### API Key 配置
- **数据库连接凭证**: 通过环境变量或配置文件注入，禁止硬编码
- **LLM API Key**: 由Agent平台内置提供，无需额外配置

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### Schema感知配置

```python
pro.configure(
    schema_refresh="on-demand",      # 按需刷新Schema
    include_views=True,              # 包含视图
    include_indexes=True,            # 包含索引信息
    dialect="postgresql"             # 指定数据库方言
)
```

### 批量生成配置

```python
pro.batch_config(
    prompts_file="queries.yaml",     # 自然语言需求清单
    output_dir="generated/",         # 输出目录
    naming="snake_case",             # 文件命名规范
    include_advice=True,             # 附带优化建议
    parallel=4                       # 并发生成数
)
```

### 回归测试配置

```python
pro.regression_config(
    baseline_dir="generated/v1.0/",  # 基线版本
    check_syntax=True,               # 语法校验
    check_plan=True,                 # 执行计划对比
    regression_threshold=0.1         # 性能回归阈值10%
)
```

## 常见问题

### Q1：Schema感知连接失败怎么办？

A：(1) 检查数据库连接字符串与网络连通性；(2) 确认账号有`information_schema`读取权限；(3) 对 `PostgreSQL` 需要访问`pg_catalog`。可降级为手动提供Schema.
### Q2：多表JOIN生成准确率如何保证？

A：专业版通过Schema感知获取真实外键关系与字段语义，对有显式外键约束的表JOIN准确率可达95%+；对无外键约束的表需在描述中指明关联字段.
### Q3：优化建议的索引会影响写入性能吗？

A：会。每个索引都会增加写入开销。专业版优化建议会标注"读写比"评估，对写多读少的表会谨慎推荐索引，建议结合业务负载综合决策.
### Q4：迁移脚本支持哪些数据库？

A：支持 `PostgreSQL`、MySQL、SQL Server、SQLite四类数据库的迁移脚本生成。不同方言的ALTER TABLE语法差异已内置适配.
### Q5：批量生成的SQL如何版本管理？

A：专业版自动为每次批量生成创建版本快照，支持`pro.version_diff(v1, v2)`对比两个版本的差异，便于追踪变更.
### Q6：回归测试的"性能回归"如何度量？

A：通过对比基线与当前版本的执行计划耗时。若某查询耗时增加超过阈值（默认10%），标记为回归。建议在稳定环境运行测试，避免硬件波动干扰.
### Q7：生成的SQL可以自动执行吗？

A：可以，但建议先dry-run。专业版支持`pro.generate_and_explain()`生成后自动EXPLAIN但不执行，确认计划合理后再真正执行.
### Q8：Schema感知缓存如何失效？

A：默认按需刷新（`on-demand`），也可配置`on-change`监听数据库变更事件自动刷新，或`scheduled`定时刷新.
### Q9：支持生成存储过程吗？

A：不支持自动生成存储过程。存储过程逻辑复杂且方言差异大，专业版聚焦标准SQL生成，存储过程建议人工编写.
### Q10：团队多人如何协作？

A：专业版支持将生成历史与迁移脚本纳入Git管理，团队成员共享同一套基线。批量生成配置文件`queries.yaml`可作为团队SQL需求清单统一维护.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

