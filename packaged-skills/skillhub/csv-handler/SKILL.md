---
slug: "csv-handler"
name: "csv-handler"
version: "1.0.0"
displayName: "CSV文件处理专家"
summary: "自动检测编码与分隔符，清洗、合并、拆分、转换CSV数据，支持进度计划与成本数据专用解析"
license: "Proprietary"
description: |-
  CSV文件处理专家，覆盖建筑、工程、财务等场景下的CSV全生命周期管理.
  核心能力包括：
  - 编码自动检测（utf-8、utf-8-sig、latin-1、cp1252、iso-8859-1）
  - 分隔符自动识别（逗号、分号、制表符、竖线）
  - CSV文件画像分析（行数、列数、表头判定）
  - 数据清洗（列名标准化、空行空列删除、空白裁剪）
  - 多文件合并（按列merge或纵向concat）
  - 按列值拆分CSV为多个子文件
  - 智能类型转换（数值、日期时间自动推断）
  - 进度计划CSV专用解析（日期列自动转换）
  - 成本CSV专用解析（金额列去$符号并转数值）
  - 多编码导出（utf-8-sig带BOM导出）
tags:
  - 研发工具
  - csv
  - data-processing
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# CSV文件处理专家

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | CSV文件处理专家处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| CSV文件处理专家划与成本数据专用解析 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 概述

CSV是工程与财务领域最通用的数据交换格式——从进度计划导出到成本数据库，无处不在。本技能专注于解决编码识别错误、分隔符误判、脏数据清洗等高频痛点，提供从读取到导出的完整处理链路.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 编码自动检测
通过 `chardet.detect()` 读取文件前 10000 字节进行编码推断，覆盖以下常见编码：

- `utf-8`：标准Unicode编码
- `utf-8-sig`：带BOM头的UTF-8（Excel导出常见）
- `latin-1`：西欧语言编码
- `cp1252`：Windows Latin-1扩展
- `iso-8859-1`：ISO标准西欧编码

检测失败时回退至 `utf-8`，避免抛出 `UnicodeDecodeError`.
**输入**: 用户提供编码自动检测所需的指令和必要参数.
**处理**: 解析编码自动检测的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 分隔符自动识别
读取文件前 5000 字符，统计 `COMMON_DELIMITERS = [',', ';', '\t', '|']` 各分隔符出现频次，选取频次最高者作为分隔符。支持欧式CSV（分号分隔）、TSV（制表符分隔）、管道分隔等非标准格式.
**输入**: 用户提供分隔符自动识别所需的指令和必要参数.
**处理**: 解析分隔符自动识别的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回分隔符自动识别的处理结果,包含执行状态码、结果数据和执行日志。### CSV文件画像分析

调用 `profile_csv()` 生成 `CSVProfile` 对象，包含：

| 字段 | 类型 | 说明 |
|:---:|:---:|:---:|
| `encoding` | str | 检测到的编码 |
| `delimiter` | str | 检测到的分隔符 |
| `has_header` | bool | 是否包含表头行 |
| `row_count` | int | 数据行数（不含表头） |
| `column_count` | int | 列数 |
| `columns` | List[str] | 列名列表 |

表头判定逻辑：检查首列是否为纯数字（去除 `.` 和 `-`），若非数字则判定有表头.
### 数据读取与清洗
`read_csv()` 方法封装 `pd.read_csv()`，默认参数：

- `on_bad_lines='skip'`：跳过格式错误行
- `low_memory=False`：避免大文件分块读取类型推断错误
- `nrows=10`：画像分析时仅读取前10行预览

清洗流程 `clean_dataframe()`：

1. 列名标准化：转小写、空格转下划线、横线转下划线、仅保留字母数字与下划线
2. 删除全空行：`df.dropna(how='all')`
3. 删除全空列：`df.dropna(axis=1, how='all')`
4. 字符串列空白裁剪：`df[col].str.strip()`

**输出**: 返回数据读取与清洗的处理结果,包含执行状态码、结果数据和执行日志.
### 多文件合并
`merge_csvs()` 支持两种模式：

- **按键合并**：指定 `on_column` 参数，使用 `pd.merge(how='outer')` 横向连接，自动标记 `_source_file` 来源列
- **纵向堆叠**：不指定 `on_column`，使用 `pd.concat(ignore_index=True)` 纵向拼接

**处理**: 解析多文件合并的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回多文件合并的处理结果,包含执行状态码、结果数据和执行日志。### 按列拆分
`split_csv()` 按 `group_column` 的唯一值将DataFrame拆分为多个CSV文件，输出到指定目录，文件名格式为 `{group_column}_{value}.csv`，自动创建目录 `output_path.mkdir(parents=True, exist_ok=True)`.
**输入**: 用户提供按列拆分所需的指令和必要参数.
**处理**: 解析按列拆分的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 智能类型转换
`convert_types()` 支持两种模式：

- **手动映射**：传入 `type_map={'col_name': 'float64'}` 指定列类型
- **自动推断**：依次尝试 `pd.to_numeric()` 和 `pd.to_datetime()`，转换失败保持原类型

**输入**: 用户提供智能类型转换所需的指令和必要参数.
**输出**: 返回智能类型转换的处理结果,包含执行状态码、结果数据和执行日志。### 进度计划CSV专用解析
`ScheduleCSVHandler` 继承基础处理器，`parse_schedule()` 自动识别包含 `date`、`start`、`end` 关键词的列并调用 `pd.to_datetime()` 转换。标准进度计划列：`task_id`、`task_name`、`start_date`、`end_date`、`duration`、`predecessors`、`resources`.
**输入**: 用户提供进度计划CSV专用解析所需的指令和必要参数.
**输出**: 返回进度计划CSV专用解析的处理结果,包含执行状态码、结果数据和执行日志。### 成本CSV专用解析
`CostCSVHandler` 的 `parse_costs()` 自动识别包含 `cost`、`price`、`amount`、`total`、`qty`、`quantity` 关键词的列，通过正则 `r'[\$,]'` 去除美元符号和千位分隔符后调用 `pd.to_numeric(errors='coerce')` 转换.
**输入**: 用户提供成本CSV专用解析所需的指令和必要参数.
**输出**: 返回成本CSV专用解析的处理结果,包含执行状态码、结果数据和执行日志。### 多编码导出
`export_csv()` 默认使用 `utf-8-sig` 编码导出（带BOM，确保Excel正确显示中文），支持自定义分隔符，`index=False` 不写入行索引.
**输入**: 用户提供多编码导出所需的指令和必要参数.
**处理**: 解析多编码导出的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
#
## 使用流程

1. **画像分析**：调用 `profile_csv("export.csv")` 获取文件编码、分隔符、行列数
2. **读取清洗**：调用 `read_csv("export.csv", clean=True)` 加载并自动清洗数据
3. **按需处理**：根据场景选择合并、拆分、类型转换或专用解析器
4. **结果导出**：调用 `export_csv(df, "output.csv")` 以 `utf-8-sig` 编码写出

## 详细示例

### 示例1：文件画像与基础读取

```python
handler = ConstructionCSVHandler()
# ...
profile = handler.profile_csv("p6_export.csv")
# 输出: Encoding: utf-8-sig, Delimiter: ',', Rows: 1542, Cols: 7
# ...
df = handler.read_csv("p6_export.csv")
print(f"加载 {len(df)} 行, {len(df.columns)} 列")
# 输出: 加载 1542 行, 7 列
```

### 示例2：合并季度导出文件

```python
files = ["jan_export.csv", "feb_export.csv", "mar_export.csv"]
merged = handler.merge_csvs(files, on_column="task_id")
print(f"合并后 {len(merged)} 行, 来源: {merged['_source_file'].unique()}")
```

### 示例3：按类别拆分

```python
handler.split_csv(df, group_column='category', output_dir='./split_files')
# 生成: ./split_files/category_civil.csv, ./split_files/category_electrical.csv
```

### 示例4：成本数据解析

```python
cost_handler = CostCSVHandler()
costs = cost_handler.parse_costs("estimate.csv")
print(costs['total_cost'].describe())
# 输出: mean: 45230.50, max: 185000.00, min: 120.00
```

### 示例5：进度计划导入

```python
schedule_handler = ScheduleCSVHandler()
schedule = schedule_handler.parse_schedule("p6_export.csv")
print(schedule['start_date'].dtype)
# 输出: datetime64[ns]
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| `UnicodeDecodeError` | 文件包含非声明编码字符 | 使用 `errors='replace'` 替换非法字符，或手动指定 `latin-1` 编码 |
| 分隔符误判 | 文件内逗号出现在文本字段中 | 检查是否引用了引号包裹字段，手动指定 `delimiter='\t'` |
| `ParserError: Error tokenizing data` | 行内字段数不一致 | 已通过 `on_bad_lines='skip'` 自动跳过，检查原始文件引号配对 |
| BOM残留导致列名首字符异常 | `utf-8` 读取带BOM文件 | 改用 `utf-8-sig` 编码读取，BOM会被自动移除 |
| `MemoryError` 大文件溢出 | 文件超过可用内存 | 使用 `nrows` 分批读取或 `chunksize=10000` 流式处理 |
| 合并键不匹配 | 文件间列名大小写/空格不一致 | 先执行 `clean_dataframe()` 标准化列名再合并 |
| 数值列含货币符号 | `$1,234.56` 无法直接转数值 | 使用 `replace(r'[\$,]', '', regex=True)` 清洗后转换 |
| 空文件或仅表头 | 文件无数据行 | 检查 `profile.row_count == 0`，返回空DataFrame |

## 常见问题

### Q1: Excel打开CSV中文乱码怎么办？
A: 导出时使用 `utf-8-sig` 编码（`export_csv(df, "output.csv", encoding='utf-8-sig')`），BOM头会让Excel正确识别UTF-8编码.
### Q2: 欧式CSV用分号分隔，如何正确读取？
A: `detect_delimiter()` 会自动识别分号。也可手动指定：`handler.read_csv("data.csv", delimiter=';')`.
### Q3: 合并多个CSV时列名不一致怎么处理？
A: 先对每个文件调用 `read_csv(clean=True)`，列名会自动标准化（小写、下划线连接）。再执行 `merge_csvs()`.
### Q4: 成本列含 `$` 和逗号，如何转为数值？
A: 使用 `CostCSVHandler.parse_costs()`，会自动通过正则 `r'[\$,]'` 去除符号后用 `pd.to_numeric(errors='coerce')` 转换.
### Q5: 大文件（>1GB）如何避免内存溢出？
A: 使用 `pd.read_csv(chunksize=10000)` 分块迭代处理，或仅读取需要的列 `usecols=['col1', 'col2']`.
### Q6: 如何判断CSV是否有表头行？
A: `profile_csv()` 返回的 `has_header` 字段会自动判定——检查首列是否为纯数字，非数字则判定有表头.
## 已知限制

- 编码检测基于前 10000 字节采样，极少情况下可能误判混合编码文件
- 分隔符检测基于频次统计，不处理字段内含分隔符的引号包裹场景
- `on_bad_lines='skip'` 会静默丢弃格式错误行，建议检查丢弃行数
- 不支持加密CSV文件解密

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "CSV文件处理专家处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "csv-handler"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
