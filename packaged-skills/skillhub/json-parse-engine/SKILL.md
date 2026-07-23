---
slug: "json-parse-engine"
name: "json-parse-engine"
version: "1.0.0"
displayName: "JSON解析引擎专业版"
summary: "企业级JSON解析引擎，支持流式解析、批量处理、DataFrame转换、自定义展平策略与增量解析。"
license: "Proprietary"
edition: "pro"
description: |-
  JSON解析引擎专业版面向企业级场景，在免费版基础上扩展流式解析、批量目录处理、DataFrame表格转换、自定义展平策略、增量解析与断点续传等高级能力。核心能力：GB级JSON流式解析、目录级批量解析、JSON转DataFrame表格、可配置展平深度与分隔符、增量解析与断点续传、性能基准与多级缓存
tags:
  - 集成工具
  - JSON
  - 企业级
  - 解析
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# JSON解析引擎专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### 流式解析引擎
- GB级JSON流式解析，内存占用稳定在10MB以内
- 增量输出：边解析边输出，无需全量加载
- 路径订阅：仅提取订阅路径的数据，跳过无关部分
- 断点续传：大文件解析中断后可恢复

**输入**: 用户提供流式解析引擎所需的指令和必要参数。
### 批量目录处理
- 递归扫描指定目录的所有JSON文件
- 并行解析（默认8线程，可配置）
- 处理报告：成功/失败/记录数统计
- 增量模式：仅处理修改时间变化的文件

**输入**: 用户提供批量目录处理所需的指令和必要参数。
**输出**: 返回批量目录处理的执行结果,包含操作状态和输出数据。### DataFrame表格转换
- JSON数组转DataFrame（每元素一行）
- 嵌套对象展平后转DataFrame
- 列式数据（字典数组）转DataFrame
- 支持导出为CSV/Excel/Parquet

**输入**: 用户提供DataFrame表格转换所需的指令和必要参数。
**处理**: 按照skill规范执行DataFrame表格转换操作,遵循单一意图原则。### 自定义展平策略
| 策略参数 | 说明 | 默认值 |
|----------|------|--------|
| `max_depth` | 最大展平深度 | 无限 |
| `separator` | 键名分隔符 | `_` |
| `array_handling` | 数组处理方式 | index |
| `skip_null` | 是否跳过null值 | false |

数组处理方式：
- `index`：按索引展开（`items_0`、`items_1`）
- `concat`：拼接为字符串（`items`="a,b,c"）
- `count`：仅保留计数（`items_count`=3）
- `skip`：跳过数组字段

### 增量解析
- 基于文件哈希判断变更
- 仅解析变更的文件或字段
- 解析结果缓存，避免重复计算
- 增量日志记录变更历史

**输入**: 用户提供增量解析所需的指令和必要参数。
### 性能基准
- 解析吞吐量（MB/s）
- 内存占用峰值
- 缓存命中率
- 多线程加速比

**输入**: 用户提供性能基准所需的指令和必要参数。
**输出**: 返回性能基准的执行结果,包含操作状态和输出数据。

#
## 适用场景

| 场景 | 角色 | 价值 | 推荐能力 |
|------|------|------|----------|
| 大规模日志解析 | 数据工程师 | GB级日志结构化 | 流式解析+增量 |
| 企业数仓ETL | 数据架构师 | JSON转表格入仓 | DataFrame+批量 |
| API响应批量处理 | 后端开发者 | 批量解析API返回 | 批量+展平 |
| 数据迁移转换 | 数据库管理员 | JSON转CSV/Excel | DataFrame转换 |
| 实时数据流处理 | 流式工程师 | 增量解析实时数据 | 流式+增量 |
| BI数据预处理 | 数据分析师 | JSON转分析友好格式 | DataFrame+展平 |

## 使用流程

### 场景1：流式解析大文件

```python
from parse_engine import StreamingParser

parser = StreamingParser(
    memory_limit="10MB",
    checkpoint_interval="100MB"
)

for record in parser.parse_stream("large-log.json", path="$.events[*]"):
    process(record)  # 逐条处理，内存稳定
```

### 场景2：批量解析目录转DataFrame

```python
from parse_engine import BatchParser

parser = BatchParser(parallel=8)
result = parser.parse_dir("./data", flatten=True)

df = result.to_dataframe()
df.to_csv("output.csv", index=False)
print(f"处理 {result.file_count} 文件，{len(df)} 行")
```

### 场景3：自定义展平策略

```python
parser = JSONParser(
    flatten_config={
        "max_depth": 3,
        "separator": ".",
        "array_handling": "count",
        "skip_null": True
    }
)
flat = parser.flatten_json(data)
```

### 场景4：增量解析

```python
from parse_engine import IncrementalParser

parser = IncrementalParser(cache_dir=".parse-cache")
result = parser.parse_incremental("./data")
print(f"新增 {result.new_count}，更新 {result.updated_count}，跳过 {result.skipped_count}")
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | json-parse-engine处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "engine_result": "engine_result_value",
      "engine_metadata": "engine_metadata_value",
      "engine_status": "engine_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/json-parse-engine_template`

## 异常处理

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|----------|----------|--------|
| 流式解析内存溢出 | 缓冲区过大/单行过长 | 降低buffer_size，使用大行解析器 | 高 |
| 批量解析卡住 | 目录过大/IO瓶颈 | 启用增量模式，增加并行线程 | 中 |
| DataFrame转换失败 | 类型推断错误 | 显式指定dtypes，统一列类型 | 高 |
| 展平后字段爆炸 | 数组展开过多 | 限制max_depth，改用count/skip | 中 |
| 增量解析遗漏 | 修改时间不准 | 切换哈希模式，清理缓存 | 中 |
| 缓存命中率低 | 文件频繁变更 | 调整缓存策略，全量重建 | 低 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于解析引擎与DataFrame转换）
- **Node.js**: 16+（用于流式解析命令行工具，可选）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| JSON解析器 | 运行时 | 必需 | Python内置json模块 |
| pandas | pip包 | 必需 | `pip install pandas` |
| pyarrow | pip包 | 可选 | `pip install pyarrow`（Parquet导出） |
| 流式解析库 | pip包 | 必需 | `pip install ijson` |

### API Key 配置
- 本Skill基于指令驱动，无需额外API Key
- 流式解析与批量处理为本地执行，不依赖外部API
- 若需对接企业版数据仓库，按对应服务文档配置

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，解析与转换功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行企业级JSON解析与转换任务，高级功能通过命令行工具实现

## 案例展示

### 流式解析参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `memory_limit` | string | 10MB | 内存上限 |
| `checkpoint_interval` | string | 100MB | 检查点间隔 |
| `buffer_size` | string | 64KB | 读写缓冲区 |
| `path_subscription` | array | [] | 订阅路径列表 |

### 批量解析参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `parallel` | integer | 8 | 并行线程数 |
| `recursive` | boolean | true | 是否递归 |
| `incremental` | boolean | false | 增量模式 |
| `exclude` | array | [] | 排除模式 |

### DataFrame转换参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `flatten` | boolean | true | 是否展平 |
| `export_format` | string | csv | csv/excel/parquet |
| `encoding` | string | utf-8 | 输出编码 |
| `dtypes` | object | {} | 列类型指定 |

### 展平策略参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `max_depth` | integer | -1 | 最大深度（-1无限） |
| `separator` | string | _ | 键名分隔符 |
| `array_handling` | string | index | index/concat/count/skip |
| `skip_null` | boolean | false | 跳过null |
| `rename` | object | {} | 字段重命名映射 |

## 常见问题

### Q1：流式解析内存仍超10MB？
A：检查缓冲区大小（buffer_size），过大可能突破内存上限。若JSON单行过长（如几MB的数组），需要专用的大行解析器。订阅路径过多也会增加内存，建议精确订阅。

### Q2：批量解析结果不一致？
A：并行解析不保证顺序，结果合并时按文件名排序。若业务要求顺序，设置`parallel=1`。DataFrame合并按文件处理顺序追加，如需特定顺序，解析后排序。

### Q3：DataFrame转换类型错误？
A：JSON的类型推断可能不准确（如数字字符串被识别为object）。通过`dtypes`参数显式指定列类型。混合类型列（如既有数字又有字符串）建议统一为字符串。

### Q4：展平后字段太多？
A：限制`max_depth`减少展平层级。数组字段选择`count`或`skip`处理方式，避免索引展开。展平后字段数过多影响可读性，建议按需提取。

### Q5：增量解析遗漏文件？
A：基于修改时间的增量可能遗漏（编辑器保存方式问题）。切换为基于文件哈希的增量（`incremental=hash`），确保准确性。缓存目录被清理后，首次运行会全量解析。

### Q6：流式解析的订阅路径如何写？
A：使用JSONPath语法，如`$.events[*]`订阅events数组的所有元素，`$.user.name`订阅用户名。订阅路径精确指定可显著减少解析量，提升性能。

### Q7：如何导出为Parquet格式？
A：设置`export_format=parquet`。Parquet是列式存储，适合大数据分析。需要安装`pyarrow`或`fastparquet`库。Parquet支持压缩，体积比CSV小3-10倍。

### Q8：多级缓存如何工作？
A：L1缓存解析结果（避免重复解析），L2缓存展平结果（避免重复展平），L3缓存DataFrame（避免重复转换）。缓存键基于文件哈希，文件变更自动失效。

### Q9：如何集成到ETL流水线？
A：专业版提供命令行接口与Python API。命令行接口支持`--stream`/`--batch`/`--export`等参数，适合脚本化。Python API提供更细粒度控制，适合嵌入ETL框架。

### Q10：解析过程中断如何恢复？
A：流式解析的检查点机制支持恢复。检查点文件位于`.parse-checkpoints/`目录，包含已解析的偏移量。恢复时从最近检查点继续，避免重头解析。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
