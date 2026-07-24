---
slug: "csv-analyzer"
name: "csv-analyzer"
version: 1.0.1
displayName: "CSV数据分析器"
summary: "用简单命令分析CSV文件，获取统计、筛选行、检测异常、分组聚合，零外部依赖。。CSV数据分析器用简单命令分析CSV文件，即时获取统计、筛选数据、检测异常并导出结果. 仅依赖Python标准库"
license: "Proprietary"
description: |-
  CSV数据分析器用简单命令分析CSV文件，即时获取统计、筛选数据、检测异常并导出结果.
  仅依赖Python标准库（csv模块），无需pandas或重型依赖，在2GB内存服务器上运行无压力.
  核心能力：
  - 快速统计：stats命令返回行数、列类型、数值列min/max/mean、文本列unique计数
  - 灵活筛选：filter命令支持比较运算符，可导出筛选结果
  - Top/Bottom N：top/bottom命令按指定列取前N/后N
  - 异常检测：anomalies命令基于z-score检测超出2σ的值
  - 分组聚合：group命令支持sum/count等多种聚合函数
  - 自动列类型检测：数值、日期、文本自动识别
  - 结果导出：筛选/处理结果可导出为CSV
  适用场景：数据探索、快速统计、异常排查、报表预处理、ETL质检.
  不适用于：超过100MB的大文件（需pandas流式处理）、加密文件破解.
tags:
  - 信息检索
  - 数据分析
  - CSV
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - AI代理
  - agent
  - 开发
  - csv
  - python3
  - 请参考
  - 目录中的
  - 脚本文件
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Csv Analyzer — CSV数据分析器

用简单命令分析CSV文件，即时获取统计、筛选数据、检测异常并导出结果——无需pandas或重型依赖.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | CSV数据分析器处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| CSV数据分析器用简单命令分析 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 核心能力

### 1. 快速统计（stats）
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） stats data.csv
```

返回行数、列类型、数值列的min/max/mean、文本列的unique计数.
**输入**: 用户提供快速统计（stats）所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `快速统计（stats）` 选项

### 2. 灵活筛选（filter）
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） filter data.csv --where "amount>1000" --output big_orders.csv
```

支持比较运算符（`>`、`<`、`>=`、`<=`、`==`、`!=`），可将筛选结果导出为CSV.
**输入**: 用户提供灵活筛选（filter）所需的指令和必要参数.
### 3. Top/Bottom N
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） top data.csv --column revenue --n 10
python3 {baseDir}/（请参考skill目录中的脚本文件） bottom data.csv --column revenue --n 5
```

按指定列取前N或后N行.
**输入**: 用户提供Top/Bottom N所需的指令和必要参数.
**输出**: 返回Top/Bottom N的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 异常检测（anomalies）
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） anomalies data.csv --column price
```

基于z-score检测超出2σ（2倍标准差）的值.
**输入**: 用户提供异常检测（anomalies）所需的指令和必要参数.
**输出**: 返回异常检测（anomalies）的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 分组聚合（group）
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） group data.csv --by category --agg "sum:amount" "count:id"
```

按指定列分组，支持 `sum`、`count` 等多种聚合函数，可同时指定多个聚合.
**输入**: 用户提供分组聚合（group）所需的指令和必要参数.
**输出**: 返回分组聚合（group）的处理结果,包含执行状态码、结果数据和执行日志.
### 6. 自动列类型检测
自动识别列类型：数值（numeric）、日期（date）、文本（text）。数值列做统计计算，文本列做unique计数.
**输入**: 用户提供自动列类型检测所需的指令和必要参数.
**处理**: 解析自动列类型检测的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回自动列类型检测的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`自动列类型检测`的配置文档进行参数调优
### 7. 结果导出

`filter` 等命令支持 `--output` 参数，将处理结果导出为CSV，便于后续分析或报表使用.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 为何不用pandas？

pandas很强大，但：

- 仅导入就占100MB+内存
- 对快速分析任务过于重型
- 本技能在2GB内存服务器上运行无压力
- 对真正的大数据集，Agent可建议安装pandas

## 使用流程

1. **确认环境**：检查 `python3` 可用（无需安装任何外部包）.
2. **快速统计**：用 `stats` 命令获取数据概况（行数、列类型、min/max/mean）.
3. **按需分析**：根据统计结果选择 `filter`/`top`/`bottom`/`anomalies`/`group` 命令.
4. **导出结果**：用 `--output` 参数将筛选/处理结果导出为CSV.
5. **验证输出**：检查导出文件的行数与内容是否符合预期.
6. **大数据集建议**：若文件接近100MB或分析慢，考虑安装pandas.
#
## 示例

### 示例1：快速统计

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） stats orders.csv
# 输出：
# 行数: 1500
# 列: order_id(text, 1500 unique), amount(numeric, min=10.5, max=9999.0, mean=456.78),
#     category(text, 12 unique), order_date(date)
```

### 示例2：筛选大额订单并导出

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） filter orders.csv --where "amount>1000" --output big_orders.csv
# 输出：筛选出87行，已导出到 big_orders.csv
```

### 示例3：取销售额前10

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） top orders.csv --column amount --n 10
# 输出：amount最大的10行记录
```

### 示例4：检测价格异常

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） anomalies orders.csv --column amount
# 输出：超出2σ的异常值，共23行
# 例如：amount=9999.0（z-score=3.8），amount=5.0（z-score=-2.5）
```

### 示例5：按类别分组聚合

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） group orders.csv --by category --agg "sum:amount" "count:order_id"
# 输出：
# category=electronics, sum:amount=125000.50, count:order_id=320
# category=clothing, sum:amount=45000.20, count:order_id=180
# ...
```

### 示例6：多条件组合（先filter再stats）

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） filter orders.csv --where "amount>500" --output high_value.csv
python3 {baseDir}/（请参考skill目录中的脚本文件） stats high_value.csv
# 输出：高价值订单的统计概况
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| `FileNotFoundError` | 文件路径错误或不存在 | 校验文件路径与扩展名（.csv） |
| `python3: command not found` | 系统未安装Python 3 | 安装Python 3.x并确保 `python3` 在PATH中 |
| `--column` 列名不存在 | 列名拼写错误或大小写不匹配 | 先用 `stats` 查看实际列名，再传入 |
| `--where` 表达式无效 | 比较运算符或列名错误 | 使用合法运算符（`>`/`<`/`>=`/`<=`/`==`/`!=`）与正确列名 |
| `--agg` 聚合函数不支持 | 传入了非sum/count的函数 | 仅支持 `sum`/`count`，按 `func:column` 格式传入 |
| 数值列含非数值 | 数据中有空值或字符串 | 清洗数据或确认列类型识别正确 |
| 日期解析失败 | 非ISO格式 | 优先使用ISO 8601（`2024-01-15`），其他格式可能无法识别 |
| 文件过大导致内存不足 | 超过约100MB | 改用pandas流式处理，或拆分文件 |
| `--n` 值非法 | 传入0或负数 | 传入正整数，如 `--n 10` |
| `--output` 路径不可写 | 目录权限不足 | 检查目标目录权限或更换输出路径 |
| 导出文件空 | 筛选条件无匹配行 | 放宽 `--where` 条件或检查数据 |

## 常见问题

### Q1：为何不用pandas？
pandas仅导入就占100MB+内存，对快速分析任务过于重型。本技能仅用Python标准库（csv模块），在2GB内存服务器上运行无压力。对真正的大数据集，Agent可建议安装pandas.
### Q2：支持多大的文件？
设计支持约100MB以内的文件（载入内存）。超过此规模建议安装pandas或使用流式处理。2GB内存服务器可稳定运行.
### Q3：如何检测异常？
`anomalies` 命令基于z-score检测超出2σ（2倍标准差）的值。这些值在统计上偏离均值较远，可能是数据错误或值得关注的异常点.
### Q4：支持哪些聚合函数？
目前支持 `sum`（求和）与 `count`（计数）两种聚合函数，按 `func:column` 格式传入，可同时指定多个（如 `"sum:amount" "count:id"`）.
### Q5：如何导出筛选结果？
`filter` 命令支持 `--output` 参数，将筛选结果导出为CSV文件。例如 `--output big_orders.csv`.
### Q6：列类型如何识别？
自动识别：数值列做min/max/mean统计，文本列做unique计数，日期列尝试ISO格式解析。非ISO日期可能无法识别.
### Q7：支持哪些比较运算符？
`filter` 的 `--where` 支持 `>`、`<`、`>=`、`<=`、`==`、`!=` 六种比较运算符，如 `"amount>1000"`.
### Q8：能在2GB内存服务器上运行吗？
能。本技能零外部依赖，仅用Python标准库，内存占用远低于pandas。2GB内存服务器可稳定运行100MB以内的文件分析.
## 已知限制

- 设计支持约100MB以内的文件（载入内存），更大文件需pandas流式处理.
- 日期解析为基础级，优先支持ISO 8601格式，其他格式可能无法识别.
- 聚合函数仅支持 `sum` 与 `count`，暂不支持 `avg`/`min`/`max`/`median`.
- 仅依赖Python标准库，无pandas的向量化加速，大文件分析较慢.
- 不支持加密CSV文件的破解.
- 不支持多表JOIN与跨文件关联分析.
- `--where` 仅支持单条件，不支持 AND/OR 组合条件.