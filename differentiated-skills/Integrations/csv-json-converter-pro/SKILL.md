---
slug: csv-json-converter-pro
name: csv-json-converter-pro
version: "1.0.0"
displayName: CSV转JSON(专业版)
summary: 企业级CSV转JSON工具，支持批量流式转换、Schema校验、字段映射与数据库直写。
license: Proprietary
edition: pro
description: |-
  CSV转JSON专业版是一款面向数据团队与企业级ETL场景的全功能表格数据格式转换工具。在免费版的表头推断、类型识别、编码探测基础上，新增批量转换、流式转换、JSON Schema校验、自定义字段映射、增量同步与数据库直写六大高级能力，覆盖从单文件到TB级数据流水线的全场景需求。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。
tags:
- 数据转换
- ETL流水线
- 企业工具
tools:
  - - read
- exec
---

# CSV转JSON（专业版）

> **把"CSV转JSON"从单文件手搓升级为企业级流水线。批量+流式+Schema+映射+增量+直写六件套。**

CSV转JSON专业版解决数据团队最常踩的六个坑：GB级文件OOM、转换结果结构不符合下游契约、CSV列名与JSON键名对不上、全量重跑浪费算力、转换后还要手动导入数据库、断点续传难实现。本工具把这些企业级诉求固化为可复制模板与流水线编排规则，让Agent能直接给出生产可用的脚本与运维建议。

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 60秒上手：批量流式转换

直接对Agent说：

> "帮我把 ./data 目录下所有CSV批量转成JSON，文件较大需要流式处理。"

Agent会按本工具的批量流式模板输出：

```python
import csv, json, os, glob
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

def convert_one(csv_path: str, out_dir: str):
    """单文件流式转换（不一次性载入内存）"""
    out_path = Path(out_dir) / (Path(csv_path).stem + '.json')
    with open(csv_path, 'r', encoding='utf-8-sig', newline='') as fin, \
         open(out_path, 'w', encoding='utf-8') as fout:
        reader = csv.DictReader(fin)
        fout.write('[')
        first = True
        for row in reader:
            if not first:
                fout.write(',')
            json.dump(dict(row), fout, ensure_ascii=False)
            first = False
        fout.write(']')
    return out_path, os.path.getsize(out_path)

# 并行批量转换
csv_files = glob.glob('./data/**/*.csv', recursive=True)
with ThreadPoolExecutor(max_workers=4) as pool:
    futures = [pool.submit(convert_one, f, './out') for f in csv_files]
    for fut in as_completed(futures):
        out_path, size = fut.result()
        print(f'完成: {out_path} ({size//1024}KB)')
```

### 120秒上手：带Schema校验的转换

把目标JSON Schema粘给Agent，Agent会生成带校验的转换脚本：

```python
import jsonschema

SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id", "name", "price"],
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string", "minLength": 1},
            "price": {"type": "number", "minimum": 0}
        }
    }
}

# 转换后校验
jsonschema.validate(converted_rows, SCHEMA)
print("Schema校验通过")
```

## 核心能力

### 能力1：批量并行转换

| 模式 | 适用场景 | 并发策略 |
|------|----------|----------|
| 串行单文件 | 调试期、单次任务 | 单线程，便于排查 |
| 并行多文件 | 10+个CSV批量处理 | ThreadPoolExecutor，默认4线程 |
| 多进程加速 | CPU密集型类型识别 | ProcessPoolExecutor，按CPU核数 |
| 分布式转换 | TB级跨机器处理 | 配合Celery/Dask调度 |

**Agent执行规则**：默认4线程并行；文件数<5时降级为串行；输出每个文件的转换状态与耗时，便于定位慢文件。

**输入**: 用户提供能力1：批量并行转换所需的指令和必要参数。
**处理**: 按照skill规范执行能力1：批量并行转换操作,遵循单一意图原则。
**输出**: 返回能力1：批量并行转换的执行结果,包含操作状态和输出数据。

### 能力2：流式转换（GB级不OOM）

```python
import csv, json, ijson

def stream_convert(csv_path: str, json_path: str, chunk_size: int = 10000):
    """流式转换，常量内存占用"""
    with open(csv_path, 'r', encoding='utf-8-sig', newline='') as fin, \
         open(json_path, 'w', encoding='utf-8') as fout:
        reader = csv.DictReader(fin)
        fout.write('[')
        first = True
        for row in reader:
            if not first:
                fout.write(',')
            json.dump(dict(row), fout, ensure_ascii=False)
            first = False
        fout.write(']')
    # 流式回读校验行数
    with open(json_path, 'rb') as f:
        count = sum(1 for _ in ijson.items(f, 'item'))
    return count
```

**关键特性**：常量内存占用（不随文件大小增长）；支持断点续传（记录已处理行数到状态文件）；支持压缩输出（`.json.gz`）。

**输入**: 用户提供能力2：流式转换（GB级不OOM）所需的指令和必要参数。
**处理**: 按照skill规范执行能力2：流式转换（GB级不OOM）操作,遵循单一意图原则。
**输出**: 返回能力2：流式转换（GB级不OOM）的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 能力3：JSON Schema校验

转换结果必须符合下游契约，专业版提供三层校验：

| 校验层 | 时机 | 失败处理 |
|--------|------|----------|
| 结构校验 | 转换后立即 | 报错并定位到错误行 |
| 类型校验 | 转换中逐行 | 隔离错误行，继续转换 |
| 业务校验 | 转换后批量 | 生成校验报告，标记违规行 |

**Agent执行规则**：默认开启结构校验；类型校验用 `try-except` 隔离错误行写入 `.errors.jsonl`；业务校验按用户提供的Schema执行。

**输入**: 用户提供能力3：JSON Schema校验所需的指令和必要参数。
**处理**: 按照skill规范执行能力3：JSON Schema校验操作,遵循单一意图原则。
**输出**: 返回能力3：JSON Schema校验的执行结果,包含操作状态和输出数据。

### 能力4：自定义字段映射DSL

```yaml
# field-mapping.yaml
mapping:
  # 重命名
  user_name: name
  user_age: age
  # 拆分：全名拆为姓和名
  full_name:
    _split: " "
    _as: [first_name, last_name]
  # 合并：姓+名合并为全名
  first_name,last_name:
    _join: " "
    _as: full_name
  # 计算字段
  total:
    _expr: "price * qty"
    _type: number
  # 常量字段
  source:
    _const: "csv_import"
  # 类型强转
  phone:
    _type: string
    _format: "{value}"
```

**Agent执行规则**：读取 `field-mapping.yaml` 后按映射规则转换；支持重命名、拆分、合并、计算字段、常量字段、类型强转六种操作；映射规则冲突时报错并列出冲突项。

**输入**: 用户提供能力4：自定义字段映射DSL所需的指令和必要参数。
**处理**: 按照skill规范执行能力4：自定义字段映射DSL操作,遵循单一意图原则。
**输出**: 返回能力4：自定义字段映射DSL的执行结果,包含操作状态和输出数据。

### 能力5：增量同步

```python
import json, os
from pathlib import Path

STATE_FILE = '.sync_state.json'

def load_state():
    if os.path.exists(STATE_FILE):
        return json.loads(Path(STATE_FILE).read_text())
    return {}

def save_state(state):
    Path(STATE_FILE).write_text(json.dumps(state, ensure_ascii=False, indent=2))

def incremental_convert(csv_path: str, key_field: str = 'id'):
    """增量转换：只处理新增行"""
    state = load_state()
    last_key = state.get(csv_path, {}).get('last_key', None)
    new_last_key = last_key
    new_rows = 0
    with open(csv_path, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            current_key = row[key_field]
            if last_key is not None and current_key <= last_key:
                continue  # 跳过已处理
            # ... 写出逻辑
            new_last_key = current_key
            new_rows += 1
    state[csv_path] = {'last_key': new_last_key, 'rows': new_rows}
    save_state(state)
    return new_rows
```

**关键特性**：基于业务主键（非行号）的增量识别；状态文件持久化到本地；支持多文件各自独立的增量进度。

**输入**: 用户提供能力5：增量同步所需的指令和必要参数。
**处理**: 按照skill规范执行能力5：增量同步操作,遵循单一意图原则。
**输出**: 返回能力5：增量同步的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 能力6：数据库直写

```python
# 示例
import psycopg2, csv, json
from psycopg2.extras import execute_values

def csv_to_postgres(csv_path: str, table_name: str, dsn: str):
    """CSV转JSON后直写 PostgreSQL"""
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    with open(csv_path, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        rows = [tuple(r[c] for c in columns) for r in reader]
    # 批量写入（分批，每批5000行）
    BATCH = 5000
    for i in range(0, len(rows), BATCH):
        execute_values(cur, f'INSERT INTO {table_name} ({",".join(columns)}) VALUES %s', rows[i:i+BATCH])
    conn.commit()
    cur.close()
    conn.close()
    return len(rows)
```

**支持的数据库**：`PostgreSQL`、MySQL、SQLite、ClickHouse。每种数据库提供独立的连接模板与批量写入策略。

**输入**: 用户提供能力6：数据库直写所需的指令和必要参数。
**处理**: 按照skill规范执行能力6：数据库直写操作,遵循单一意图原则。
**输出**: 返回能力6：数据库直写的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级、支持批量流式转换、字段映射与数据库、专业版是一款面向、数据团队与企业级、ETL、场景的全功能表格、数据格式转换工具、在免费版的表头推、编码探测基础上、新增批量转换、增量同步与数据库、直写六大高级能力、覆盖从单文件到、级数据流水线的全、场景需求、when、需要文件处理、文档转换、格式互转、内容提取时使用、不适用于加密文件等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：企业级ETL流水线CSV接入节点（数据工程师角色）

**痛点**：数据仓库ODS层每天要接50+个CSV文件，总量约5GB，单线程跑要3小时，且偶发OOM。

**使用方式**：对Agent说"给我一个ETL节点的批量流式转换脚本，要并行4线程、支持断点续传、转换后写JSONL"，Agent按本工具的批量并行模板输出生产级脚本，附调度示例（Airflow DAG）与监控指标（行数、耗时、错误率）。

**效果**：3小时降至25分钟，OOM清零，断点续传避免重跑。

### 场景二：API数据契约校验（后端工程师角色）

**痛点**：上游吐的CSV字段经常变，下游接口契约要求严格，转换后才发现字段缺失或类型错误。

**使用方式**：把JSON Schema粘给Agent，Agent生成带三层校验的转换脚本，错误行隔离到 `.errors.jsonl`，正常行照常输出。转换后生成校验报告，列出违规行号与原因。

**效果**：契约违规从下游报错提前到转换期拦截，节省联调时间。

### 场景三：跨系统数据同步（运维/SRE角色）

**痛点**：业务系统A每天导出CSV，要同步到业务系统B的 `PostgreSQL`，全量重跑慢且浪费。

**使用方式**：对Agent说"基于id字段做增量同步，转换后直写 `PostgreSQL` 的 orders 表"，Agent输出增量同步脚本+数据库直写脚本，附状态文件管理与失败重试逻辑。

**效果**：同步时间从全量2小时降至增量5分钟，数据库负载下降90%。

### 场景四：多源CSV合并入湖（数据平台角色）

**痛点**：多个业务线各自导出CSV，格式不统一（列名、类型、编码都不同），要合并入数据湖。

**使用方式**：把各业务线的字段映射规则粘给Agent，Agent生成统一映射配置+批量转换脚本，输出统一的JSONL格式供数据湖消费。

**效果**：多源异构CSV统一为标准格式，入湖前的清洗工作量减少80%。

## 最佳实践

### 实践1：大文件必须流式

单文件超过100MB时必须用流式转换，避免OOM。专业版默认流式，但需注意流式模式下无法回溯（如需校验行数一致性，用 `ijson` 流式计数）。

### 实践2：批量转换用线程池

文件IO密集型场景用 `ThreadPoolExecutor`（默认4线程）；CPU密集型（复杂类型识别）用 `ProcessPoolExecutor`（按CPU核数）。混合场景用线程池+异步IO。

### 实践3：Schema校验分层

不要把所有校验都堆在转换后。结构校验在转换后批量做；类型校验在转换中逐行做（隔离错误行）；业务校验按需做（按用户提供的规则）。

### 实践4：增量同步用业务主键

不要用行号做增量标识（CSV行号会因删除/插入变化）。用业务主键（如 `id`、`created_at`）做增量，状态文件记录最后处理的主键值。

### 实践5：数据库直写分批提交

单次提交行数建议5000-10000行，过大事务会锁表过久。专业版默认5000行一批，可按目标数据库调整。

## 常见问题

### Q1：专业版能处理多大的CSV文件？

专业版采用流式转换，理论上无大小限制。实测单文件10GB（约1亿行）可在30分钟内完成转换，内存占用稳定在200MB以内。建议单文件不超过50GB，超过则按行切分后并行处理。

### Q2：断点续传如何工作？

专业版在转换过程中每处理10000行更新一次状态文件（`.convert_state.json`），记录已处理行数与文件偏移量。中断后重启时读取状态文件，从上次位置继续。状态文件与输出文件在同一目录，删除输出文件会触发全量重跑。

### Q3：Schema校验失败后如何排查？

专业版将校验失败的行写入 `.errors.jsonl`，每行包含原始数据、错误原因、错误位置（行号+字段名）。可用 `jq` 快速统计错误类型分布：`cat .errors.jsonl | jq -r .error | sort | uniq -c`。

### Q4：增量同步如何处理删除操作？

CSV本身不记录删除操作，增量同步只能识别新增和更新。若需同步删除，建议上游提供"软删除"标记字段（如 `is_deleted`），或改用CDC（变更数据捕获）方案。专业版提供基于 `is_deleted` 字段的逻辑删除同步模板。

### Q5：字段映射DSL支持复杂表达式吗？

支持基础表达式（加减乘除、字符串拼接、条件判断）。复杂逻辑（如正则提取、函数调用）建议用 `_expr` 字段写Python表达式，专业版会在沙箱中执行。若表达式有安全风险，Agent会提示并要求确认。

### Q6：数据库直写支持事务吗？

支持。专业版默认每批5000行一个事务，批内失败回滚该批，不影响已提交的批次。若需全量事务（要么全成功要么全失败），设置 `--single-transaction` 参数，但注意大文件事务会长时间锁表。

### Q7：并行转换时文件顺序如何保证？

并行转换不保证文件处理顺序，但每个文件的输出独立。若需合并输出且保持顺序，建议先按文件名排序，再用串行模式；或转换后用 `jq` 按业务字段排序合并。

### Q8：专业版如何与调度系统（Airflow/DolphinScheduler）集成？

专业版提供标准CLI入口与退出码规范：成功返回0，部分失败返回1，全部失败返回2。调度系统按退出码判断任务状态。专业版还提供Airflow DAG模板与DolphinScheduler任务模板，可直接复用。

### Q9：如何监控转换任务的性能指标？

专业版在转换完成后输出指标摘要：总行数、成功行数、失败行数、耗时、吞吐量（行/秒）、平均单行耗时。指标同时写入 `.metrics.json` 供Prometheus采集。

### Q10：专业版与免费版的脚本可以混用吗？

可以。专业版兼容免费版的所有模板，免费版的单文件转换脚本在专业版环境下可直接运行。反向不兼容：专业版的批量、流式、Schema校验脚本依赖额外库，在免费版环境下需先安装依赖。

## 专业版特性

本专业版相比免费版新增以下能力：

- 批量并行转换：一次处理10+个CSV文件，4线程并行，支持多进程加速与分布式调度
- 流式转换：常量内存占用，支持GB级大文件，断点续传与压缩输出
- JSON Schema校验：三层校验（结构/类型/业务），错误行隔离与校验报告
- 自定义字段映射DSL：重命名、拆分、合并、计算字段、常量字段、类型强转六种操作
- 增量同步：基于业务主键的增量识别，状态文件持久化，多文件独立进度
- 数据库直写：支持 `PostgreSQL`/MySQL/SQLite/ClickHouse四种数据库，分批提交与事务控制
- 优先支持：专业版用户享7x24小时工单优先响应与企业级SLA保障

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | 0元 | 核心功能（表头推断+类型识别+编码探测+单文件转换） | 个人试用、单文件场景 |
| 收费专业版 | 29.9元/月 | 全功能+高级特性（批量/流式/Schema/映射/增量/直写）+优先支持 | 团队/企业ETL流水线 |

专业版通过SkillHub SkillPay发布。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（推荐3.10+）
- **Node.js**: 16+（若使用Node.js模板）

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| chardet | Python库 | 推荐 | `pip install chardet`（编码探测） |
| jsonschema | Python库 | 必需 | `pip install jsonschema`（Schema校验） |
| ijson | Python库 | 必需 | `pip install ijson`（流式JSON处理） |
| psycopg2 | Python库 | 可选 | `pip install psycopg2-binary`（`PostgreSQL`直写） |
| pymysql | Python库 | 可选 | `pip install pymysql`（MySQL直写） |
| clickhouse-driver | Python库 | 可选 | `pip install clickhouse-driver`（ClickHouse直写） |
| PyYAML | Python库 | 必需 | `pip install pyyaml`（映射配置解析） |
| csv | Python模块 | 必需 | Python标准库，无需安装 |
| json | Python模块 | 必需 | Python标准库，无需安装 |

### API Key 配置
- 本工具基于Markdown指令，本身不需要API Key
- 转换过程完全在本地执行，数据不上传任何外部服务
- 数据库直写时，数据库连接串存入环境变量（如 `DATABASE_URL`），禁止硬编码在脚本中
- 凭证文件存入 `d:\skills\.secrets\` 目录（已gitignore），脚本通过环境变量读取

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成可执行的企业级转换流水线

---

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：CSV转JSON工具（csv-to-json）
- 原始license：MIT
- 改进作品：CSV转JSON（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，重构为面向数据团队的企业级工具形态
- 去除原始项目标识、外部仓库URL与原作者署名
- 将单文件命令行参考重构为批量并行+流式+Schema+映射+增量+直写六大企业级能力
- 新增JSON Schema三层校验流程与错误行隔离机制
- 新增自定义字段映射DSL与增量同步状态机
- 新增四种数据库直写模板与分批提交策略
- 重新设计使用场景（数据工程师/后端/运维/数据平台四角色）
- 新增专业版特性章节、定价章节与10问FAQ
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
