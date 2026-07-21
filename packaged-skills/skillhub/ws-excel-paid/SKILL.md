---
slug: ws-excel-paid
name: ws-excel-paid
version: "1.0.0"
displayName: Excel工具(专业版)
summary: Excel 全能力版：多表合并、透视表、图表、大数据处理、自动化流水线与数据库联动。
license: Proprietary
edition: pro
description: |-
  Excel 工具（专业版）面向数据分析师与团队，在免费版基础读写之上新增多表合并、数据透视表、图表生成、大数据处理、自动化流水线与数据库联动六大模块。支持从 `关系型数据库` 等数据库直接导入导出，处理百万行级数据不溢出。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- 数据分析
- Excel
- 透视表
- 图表可视化
- 自动化流水线
tools:
  - - read
- exec
---
# Excel工具(专业版)

## 核心能力

| 模块 | 能力 | 性能基线 |
|------|------|---------|
| 多表合并 | JOIN/UNION/VLOOKUP | 10 文件 < 10s |
| 透视表 | 分组/聚合/交叉 | 10 万行 < 5s |
| 图表生成 | 柱/线/饼/散点 | 单图 < 1s |
| 大数据处理 | 分块/流式 | 100 万行 < 60s |
| 自动化 | 定时/批处理/邮件 | 无人值守 |
| 数据库联动 | 双向同步 | 增量同步 < 30s |
### 多表合并

执行多表合并操作,处理用户输入并返回结果。

**输入**: 用户提供多表合并所需的参数和指令。

**输出**: 返回多表合并的处理结果。
### 透视表

执行透视表操作,处理用户输入并返回结果。

**输入**: 用户提供透视表所需的参数和指令。

**输出**: 返回透视表的处理结果。
### 图表生成

执行图表生成操作,处理用户输入并返回结果。

**输入**: 用户提供图表生成所需的参数和指令。

**输出**: 返回图表生成的处理结果。


## 适用场景

### 场景一：月度销售报表自动化（运营视角）
每月初自动生成销售报表。Agent 依次：① 从 `关系型数据库` 读取当月销售数据；② 按区域做透视表；③ 生成柱状图与饼图；④ 追加合计行与格式；⑤ 邮件分发给管理层。

### 场景二：多源数据合并（分析师视角）
合并 5 个分公司的销售 Excel。Agent 用 pandas concat 合并，按 `门店 ID` 做 VLOOKUP 匹配主数据，输出合并后的总表。

### 场景三：大数据量处理（开发者视角）
处理 200 万行的交易记录。Agent 用分块读取（`chunksize=50000`），流式聚合，避免内存溢出，输出统计结果。

### 场景四：数据库双向同步（运维视角）
把 `关系型数据库` 中的客户表导出为 Excel 供业务方查看，业务方修改后再导入回数据库。Agent 用 SQLAlchemy 实现双向同步，支持增量更新。

### 场景五：自动化报表流水线（架构师视角）
搭建每日定时报表流水线。Agent 配置 cron 任务：① 凌晨拉取数据；② 生成 Excel；③ 上传到云盘；④ 邮件通知。全流程无人值守。

### 场景六：图表化分析（产品视角）
把用户增长数据可视化。Agent 生成折线图（日活趋势）、饼图（用户来源）、散点图（留存 vs 活跃），嵌入到 xlsx 中。

## 使用流程

### 120 秒上手
1. 安装依赖：`pip install openpyxl pandas matplotlib sqlalchemy psycopg2-binary`
2. 描述任务（合并/透视/图表/同步）
3. Agent 生成对应 Python 脚本并执行

### 示例

```python
import pandas as pd
import glob

# 合并多个 Excel 文件
files = glob.glob('data/sales_*.xlsx')
dfs = [pd.read_excel(f) for f in files]
merged = pd.concat(dfs, ignore_index=True)

# 去重并排序
merged = merged.drop_duplicates(subset=['订单ID'])
merged = merged.sort_values('日期')

merged.to_excel('merged_sales.xlsx', index=False)
print(f"合并完成：{len(merged)} 行，来源 {len(files)} 个文件")
```

### VLOOKUP 跨表匹配

```python
import pandas as pd

# 主表与从表
main = pd.read_excel('orders.xlsx')
lookup = pd.read_excel('customers.xlsx')

# 类似 VLOOKUP 的左连接
result = main.merge(
    lookup[['客户ID', '客户名称', '区域']],
    on='客户ID',
    how='left'
)

result.to_excel('orders_with_customer.xlsx', index=False)
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（推荐 3.10+）
- **内存**：建议 ≥ 8GB（大数据处理时）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| openpyxl | Python 库 | 必需 | `pip install openpyxl` |
| pandas | Python 库 | 必需 | `pip install pandas` |
| matplotlib | Python 库 | 图表必需 | `pip install matplotlib` |
| SQLAlchemy | Python 库 | 数据库联动必需 | `pip install sqlalchemy` |
| psycopg2-binary | Python 库 | `关系型数据库` 必需 | `pip install psycopg2-binary` |
| PyMySQL | Python 库 | MySQL 可选 | `pip install pymysql` |
| schedule | Python 库 | 自动化可选 | `pip install schedule` |

### API Key 配置
- **数据库连接串**：`关系型数据库` 通过环境变量 `DATABASE_URL` 注入（格式：`关系型数据库://user:pass@host:5432/dbname`）
- **SMTP 凭证**：邮件分发需要 SMTP 用户名与密码，通过环境变量 `SMTP_USER`/`SMTP_PASS` 注入
- **禁止**：在 SKILL.md 或脚本中硬编码数据库密码或 SMTP 凭证
- **数据文件路径**：由用户提供，Agent 通过 exec 执行 Python 脚本处理

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：专业版推荐使用 GPT-4o / Claude Sonnet 以处理复杂的数据分析与脚本生成
- **数据安全**：处理敏感数据时建议在本地执行，数据库连接走内网或 VPN

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1：合并多个 Excel 时列名不一致？
A：用 `rename` 统一列名后再合并。建议建立列名映射表：`df.rename(columns={'销售额': 'amount'})`。

### Q2：透视表聚合后出现 NaN？
A：某些分组无数据时会返回 NaN。用 `fill_value=0` 填充，或后续 `fillna(0)`。

### Q3：图表中文显示乱码？
A：matplotlib 默认字体不支持中文。设置中文字体：`plt.rcParams['font.sans-serif'] = ['SimHei']`（Windows）或 `['Arial Unicode MS']`（macOS）。

### Q4：200 万行 Excel 读取太慢？
A：① 用 `read_only=True` 模式；② 用 `chunksize` 分块；③ 考虑先转为 CSV 或 Parquet 再处理；④ 优秀方案：直接从 `关系型数据库` 读取，跳过 Excel。

### Q5：`关系型数据库` 导入 Excel 数据报类型错误？
A：检查 Excel 列的数据类型是否与数据库 schema 一致。日期用 `pd.to_datetime` 转换，数字用 `astype` 转换，空值用 `fillna` 或 `None`。

### Q6：自动化流水线如何定时执行？
A：Linux 用 cron，Windows 用任务计划器，或 Python 用 `schedule`/`APScheduler` 库。建议配合日志与告警。

### Q7：图表嵌入后位置错乱？
A：`ws.add_image(img, 'H2')` 的锚点是单元格。调整锚点到合适位置，或用 `img.anchor = 'H2'` 明确指定。

### Q8：增量同步怎么实现？
A：维护一个 `last_sync_id` 或 `last_sync_time`，每次只读取大于该值的数据。同步完成后更新游标。`关系型数据库` 可用 `WHERE id > :last_id` 或 `WHERE updated_at > :last_time`。

### Q9：邮件发送附件失败？
A：检查：① SMTP 服务器与端口；② 发件人凭证；③ 附件路径正确；④ 文件未被打占用。建议用 `with open` 确保文件句柄释放。

### Q10：如何保证数据一致性？
A：① 同步前做行数校验；② 关键字段做 checksum；③ 用事务（`关系型数据库` 的 BEGIN/COMMIT）；④ 保留同步日志便于回溯。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
