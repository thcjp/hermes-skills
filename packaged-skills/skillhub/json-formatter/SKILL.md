---

slug: "json-formatter"
name: "json-formatter"
version: 1.0.1
displayName: "JSON Formatter"
summary: "格式化/校验/压缩JSON并提取路径,提升可读性。Format, validate, compress JSON data, and extract JSON paths for impro"
license: "Proprietary"
description: |-，可自动提升工作效率
  Format, validate, compress JSON data, and extract JSON paths for improved
  readability and structu。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - Integrations
  - 工具
  - 效率
  - 自动化
  - 研究
  - 分析
  - 创意
  - 图像
  - 开发
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"

---

# JSON Formatter

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |
| 数据质量检测与清洗规则 | 不支持 | 支持 |

## 核心能力

* JSON 格式化（缩进）：将紧凑或混乱的JSON字符串按层级缩进，生成2空格或4空格缩进的可读结构
* JSON 验证：检测语法错误（未闭合括号、尾逗号、单引号、注释等）并精确定位行号与列号
* JSON 压缩：移除所有空白字符与换行，生成单行紧凑JSON，适用于网络传输与存储优化
* 路径提取：基于JSONPath语法（`$.store.book[0].title`）提取所有键路径，用于数据映射与字段定位
* 类型推断：自动识别字符串、数字、布尔值、null、数组、对象，并标注叶子节点类型
* 深度统计：计算最大嵌套深度、数组元素数、键值对总数，辅助复杂度评估

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| API响应调试 | 紧凑JSON响应体 | 缩进格式化JSON + 高亮错误位置 |
| 配置文件压缩 | 多行JSON配置文件 | 单行压缩JSON + 体积缩减百分比 |
| 数据字段定位 | 嵌套JSON对象 | JSONPath路径列表 + 叶子节点值 |
| 语法错误修复 | 含错误的JSON字符串 | 错误类型 + 行列号 + 修复建议 |
| 批量数据处理 | JSON数组 | 每个元素的路径提取 + 类型标注 |

**不适用于**：实时流数据处理（如WebSocket、SSE）、二进制数据序列化、超10GB单文件处理

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 确定处理目标：格式化、验证、压缩还是路径提取
3. 将JSON内容作为输入传入，指定操作类型与缩进参数
4. 检查输出结果中的 `valid` 字段确认语法正确性
5. 如遇错误，参考错误处理章节中的行列号定位问题
6. 对于路径提取，使用输出的JSONPath表达式进行后续数据操作

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 是 | 待处理的JSON字符串或文件内容 |
| operation | string | 否 | 操作类型，可选值: `format`/`validate`/`compress`/`extract_paths`，默认 `format` |
| indent | integer | 否 | 缩进空格数，可选值: `2`/`4`/`0`(压缩)，默认 `2` |
| sort_keys | boolean | 否 | 是否按键名字典序排序，默认 `false` |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "formatted": "{\n  \"a\": 1,\n  \"b\": 2\n}",
  "valid": true,
  "size": 1024,
  "compressed_size": 456,
  "paths": ["$.a", "$.b"],
  "errors": [],
  "metadata": {
    "operation": "format",
    "indent": 2,
    "depth": 3,
    "key_count": 12
  }
}
```

## 详细使用示例

### 示例1：格式化紧凑JSON

```text
输入(content): {"name":"JSON Formatter","version":"1.0.0","features":["format","validate","compress"],"config":{"indent":2,"sort":false}}
操作(operation): format
缩进(indent): 2

输出:
{
  "name": "JSON Formatter",
  "version": "1.0.0",
  "features": [
    "format",
    "validate",
    "compress"
  ],
  "config": {
    "indent": 2,
    "sort": false
  }
}
```

### 示例2：验证含错误的JSON

```text
输入(content): {"name": "test", "value": 123,}  ← 尾逗号错误
操作(operation): validate

输出:
{
  "valid": false,
  "errors": [
    {
      "type": "trailing_comma",
      "message": "Unexpected token } after comma",
      "line": 1,
      "column": 28,
      "suggestion": "删除最后一个键值对后的逗号"
    }
  ]
}
```

### 示例3：提取JSONPath

```text
输入(content): {"store":{"book":[{"title":"A","price":10},{"title":"B","price":20}],"bike":{"color":"red"}}
操作(operation): extract_paths

输出 paths:
$.store.book[0].title      → "A"
$.store.book[0].price      → 10
$.store.book[1].title      → "B"
$.store.book[1].price      → 20
$.store.bike.color         → "red"
```

### 示例4：压缩JSON

```text
输入(content): {"a": 1, "b": [2, 3]}
操作(operation): compress

输出: {"a":1,"b":[2,3]}
压缩率: 40%
```

## 最佳实践

### 缩进选择
- 开发调试阶段使用 `indent: 2`，兼顾可读性与屏幕空间
- 生产环境日志输出使用 `compress`（`indent: 0`），减少存储与带宽
- 配置文件审查使用 `indent: 4`，层级清晰便于人工核对

### 验证流程
- 任何JSON在写入文件或发送API前，先执行 `validate` 操作
- 验证失败时优先检查错误输出中的 `line` 和 `column` 字段定位问题
- 常见错误模式：尾逗号（trailing comma）、单引号代替双引号、键名缺少引号、注释（JSON不支持注释）

### 路径提取应用
- 提取路径后可用于JSON Schema生成，为每个叶子节点定义类型约束
- 在数据映射场景中，路径列表可作为字段对照表，指导ETL流程
- 配合 `jq` 工具使用路径进行数据查询：`echo '$json' | jq '$.store.book[0].title'`

## 与其他工具集成

### 配合 jq 进行高级查询
```bash
# 先用本工具格式化，再用jq提取特定字段
cat raw.json | python -m json.tool | jq '.store.book[] | .title'
```

### 配合 Python json 模块
```python
import json

# 格式化
formatted = json.dumps(data, indent=2, ensure_ascii=False)

# 验证
try:
    json.loads(json_string)
    print("Valid JSON")
except json.JSONDecodeError as e:
    print(f"Error at line {e.lineno}, column {e.colno}: {e.msg}")
```

### 配合 curl 调试API响应
```bash
# 获取API响应并自动格式化
curl -s https://api.example.com/data | python -m json.tool
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接与代理设置 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.

## 案例展示

```text
输入: {"a":1,"b":2}
输出: {
  "a": 1,
  "b": 2
}
```

## 常见问题

### Q1: 如何开始使用JSON Formatter？
A: 将待处理的JSON字符串作为 `content` 参数传入，指定 `operation` 为 `format`（格式化）、`validate`（验证）、`compress`（压缩）或 `extract_paths`（路径提取）。默认操作为格式化，缩进2空格。例如输入 `{"a":1}` 并选择格式化，输出为缩进后的多行JSON。

### Q2: JSON验证失败时如何定位错误？
A: 查看输出中 `errors` 数组的每个元素，其中包含 `type`（错误类型）、`message`（错误描述）、`line`（行号）、`column`（列号）和 `suggestion`（修复建议）。常见错误类型包括 `trailing_comma`（尾逗号）、`single_quote`（单引号）、`missing_key_quotes`（键名缺引号）、`unexpected_token`（意外字符）。

### Q3: 路径提取支持哪些JSONPath语法？
A: 支持标准JSONPath语法：`$` 根对象、`.` 子键访问、`[]` 数组索引、`[*]` 数组通配符。例如 `$.store.book[0].title` 提取第一个书名，`$.store.book[*].price` 提取所有价格。不支持过滤表达式（如 `$[?(@.price>10)]`）和递归下降（`$..`）。

### Q4: 压缩后的JSON如何还原？
A: 压缩是可逆操作。将压缩后的单行JSON作为 `content` 传入，`operation` 设为 `format`，即可还原为多行缩进格式。压缩不会丢失任何数据，仅移除空白字符。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
| JSON解析深度超限 | 嵌套层级超过100层 | 检查数据结构是否合理，考虑扁平化深层嵌套 |
| 输入包含BOM头 | 文件以UTF-8 BOM开头 | 移除BOM头后再处理，或使用工具自动剥离 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 单次处理JSON大小上限为10MB，超出需分批处理
- 不支持JSON5、JSONC等扩展语法（如注释、尾逗号、单引号）
- 路径提取不支持过滤表达式与递归下降语法
- 无法处理循环引用的JSON对象（如序列化DOM节点）
