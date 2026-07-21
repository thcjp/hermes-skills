---
slug: data-format-converter
name: data-format-converter
version: "1.0.0"
displayName: 数据格式转换器
summary: 在CSV、JSON、XML、YAML、TOML格式间高效互转，支持批量处理与嵌套结构处理
license: MIT
description: |-
  数据格式转换器——在CSV、JSON、XML、YAML、TOML等主流数据格式间高效转换。
  核心能力包括：
  - CSV与JSON互转（支持嵌套结构展开与扁平化）
  - JSON与YAML互转（保留注释与锚点引用）
  - XML与JSON互转（处理属性与子元素映射）
  - TOML与JSON互转（支持表数组与嵌套表）
  - 批量转换（目录级批量处理，保持文件名映射）
  - 编码处理（utf-8、utf-8-sig自动识别与输出）
  - 格式美化（indent缩进、sort_keys排序、ensure_ascii中文输出）
tags:
  - Integrations
  - data-format
  - converter
tools:
  - read
  - exec
---

# 数据格式转换器

## 概述

在不同数据格式间高效转换：CSV、JSON、XML、YAML、TOML。支持单文件转换与目录级批量处理，自动处理编码、嵌套结构、特殊字符等常见问题。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD（纯Markdown指令，无需exec命令行能力）

## 核心能力

### CSV与JSON互转
**CSV转JSON**：使用 `csv.DictReader()` 逐行读取为字典，通过 `json.dumps(ensure_ascii=False, indent=2)` 输出UTF-8中文JSON。

```python
import csv, json

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

json_str = json.dumps(rows, ensure_ascii=False, indent=2)
```

**JSON转CSV**：使用 `csv.DictWriter()` 写入，需指定 `fieldnames`。嵌套JSON需先扁平化（如 `{"a": {"b": 1}}` → `{"a.b": 1}`）。

```python
import csv, json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

fieldnames = list(data[0].keys())
with open('output.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

**输入**: 用户提供CSV与JSON互转所需的指令和必要参数。
**处理**: 按照skill规范执行CSV与JSON互转操作,遵循单一意图原则。### JSON与YAML互转

**JSON转YAML**：使用 `yaml.safe_dump()` 输出，`default_flow_style=False` 使用块样式（更易读），`allow_unicode=True` 保留中文。

```python
import yaml, json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

yaml_str = yaml.safe_dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
```

**YAML转JSON**：使用 `yaml.safe_load()` 解析（安全加载，不执行任意Python对象）。

```python
import yaml, json

with open('data.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

json_str = json.dumps(data, ensure_ascii=False, indent=2)
```

### XML与JSON互转

**XML转JSON**：使用 `xmltodict.parse()` 将XML解析为有序字典，属性以 `@` 前缀标记。

```python
import xmltodict, json

with open('data.xml', 'r', encoding='utf-8') as f:
    xml_str = f.read()

data = xmltodict.parse(xml_str)
json_str = json.dumps(data, ensure_ascii=False, indent=2)
```

**JSON转XML**：使用 `xmltodict.unparse()` 将字典转回XML，`pretty=True` 格式化输出。

```python
import xmltodict, json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

xml_str = xmltodict.unparse(data, pretty=True)
```

### TOML与JSON互转

**TOML转JSON**：使用 `toml.load()` 解析TOML文件，支持表数组和嵌套表。

```python
import toml, json

with open('data.toml', 'r', encoding='utf-8') as f:
    data = toml.load(f)

json_str = json.dumps(data, ensure_ascii=False, indent=2)
```

**JSON转TOML**：使用 `toml.dumps()` 输出TOML格式字符串。

```python
import toml, json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

toml_str = toml.dumps(data)
```

### 批量转换

支持目录级批量处理，遍历源格式文件并批量转换为目标格式：

```python
from pathlib import Path

def batch_convert(input_dir, output_dir, from_fmt, to_fmt):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for file in input_path.glob(f'*.{from_fmt}'):
        # 读取源文件 -> 转换 -> 写入目标文件
        output_file = output_path / f'{file.stem}.{to_fmt}'
        # 转换逻辑...
```

## 支持格式矩阵

| 输入\输出 | CSV | JSON | YAML | XML | TOML |
|----------|-----|------|------|-----|------|
| CSV | - | 支持 | 间接 | 间接 | 间接 |
| JSON | 支持 | - | 支持 | 支持 | 支持 |
| YAML | 间接 | 支持 | - | 间接 | 间接 |
| XML | 间接 | 支持 | 间接 | - | 间接 |
| TOML | 间接 | 支持 | 间接 | 间接 | - |

> "间接"表示先转为JSON再转为目标格式。JSON是所有转换的中心枢纽。

## 使用流程

1. **识别源格式**：根据文件扩展名（`.csv`/`.json`/`.yaml`/`.xml`/`.toml`）确定输入格式
2. **选择目标格式**：确认用户需要转换为何种格式
3. **加载源数据**：使用对应解析器读取文件（注意 `encoding='utf-8'`）
4. **执行转换**：通过JSON作为中间格式，或直接调用对应转换函数
5. **输出结果**：写入目标文件，注意 `ensure_ascii=False` 保留中文，`indent=2` 格式化

## 详细示例

### 示例1：CSV转JSON

```text
输入 (CSV):
name,age,city
张三,30,北京
李四,25,上海

输出 (JSON):
[
  {"name": "张三", "age": "30", "city": "北京"},
  {"name": "李四", "age": "25", "city": "上海"}
]
```

### 示例2：JSON转YAML

```text
输入 (JSON):
{"database": {"host": "localhost", "port": 5432}, "debug": true}

输出 (YAML):
database:
  host: localhost
  port: 5432
debug: true
```

### 示例3：XML转JSON

```text
输入 (XML):
<user id="101"><name>张三</name><age>30</age></user>

输出 (JSON):
{"user": {"@id": "101", "name": "张三", "age": "30"}}
```

### 示例4：TOML转JSON

```text
输入 (TOML):
[server]
host = "127.0.0.1"
port = 8080

[[users]]
name = "admin"

输出 (JSON):
{"server": {"host": "127.0.0.1", "port": 8080}, "users": [{"name": "admin"}]}
```

### 示例5：批量CSV转JSON

```text
输入: ./csv_files/ 目录下 3 个CSV文件
处理: 遍历 *.csv，逐个用 csv.DictReader 读取，json.dumps 输出
输出: ./json_files/ 目录下 3 个对应JSON文件，文件名保持一致
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `json.JSONDecodeError` | JSON格式错误（如尾随逗号、单引号） | 使用 `json.loads()` 严格解析，报告出错行号与列位置 |
| CSV含嵌套数据无法扁平化 | CSV单元格内含JSON字符串 | 先用 `json.loads()` 解析单元格内容，再展开为多列 |
| XML属性与子元素同名冲突 | `xmltodict` 属性加 `@` 前缀，但子元素同名 | 自定义 `attr_prefix` 参数，如 `attr_prefix='_'` |
| YAML含特殊字符未加引号 | 值含 `:` `#` `&` 等保留字符 | 输出时用 `default_style='"'` 强制引号包裹 |
| TOML不支持嵌套数组中的数组 | TOML规范限制：表数组 `[[x]]` 内不能有数组值 | 将嵌套数组转为JSON字符串存储，或改用JSON格式 |
| `UnicodeDecodeError` 编码错误 | 文件非UTF-8编码（如GBK、Latin-1） | 先用 `chardet.detect()` 检测编码，再以正确编码读取 |
| JSON转CSV时值含逗号或换行 | CSV字段需引号包裹 | `csv.DictWriter` 自动处理引号转义，确保 `newline=''` |
| YAML锚点与别名引用丢失 | `yaml.safe_dump` 不保留锚点 | 使用 `yaml.dump(Dumper=yaml.Dumper)` 保留引用关系 |

## 常见问题

### Q1: JSON转CSV时，JSON值是数组或对象怎么办？
A: CSV是扁平格式，无法直接表示嵌套结构。需先将嵌套值扁平化（如 `{"a": {"b": 1}}` → `{"a.b": 1}`），或将数组/对象转为JSON字符串存入单元格。

### Q2: 转换后中文变成 `\u5f20\u4e09` 怎么办？
A: 输出JSON时设置 `ensure_ascii=False`，如 `json.dumps(data, ensure_ascii=False, indent=2)`。YAML设置 `allow_unicode=True`。

### Q3: XML的属性和子元素在JSON中如何区分？
A: `xmltodict.parse()` 默认将XML属性加 `@` 前缀。如 `<user id="1"><name>张三</name></user>` 转为 `{"user": {"@id": "1", "name": "张三"}}`。

### Q4: YAML转JSON时遇到 `!!python/object` 标签怎么办？
A: 这是非安全YAML标签，可能含恶意代码。务必使用 `yaml.safe_load()` 而非 `yaml.load()`，`safe_load` 会拒绝执行任意Python对象。

### Q5: TOML文件中的表数组 `[[users]]` 转JSON后是什么结构？
A: 转为JSON数组。多个 `[[users]]` 块合并为 `"users": [{"name": "admin"}, {"name": "guest"}]`。

### Q6: 批量转换时如何保持文件名一致？
A: 使用 `Path.stem` 获取文件名（不含扩展名），拼接目标扩展名：`output_file = output_path / f'{file.stem}.{to_fmt}'`。

## 已知限制

- CSV是扁平格式，无法无损表示JSON的嵌套结构，需扁平化或字符串化处理
- TOML不支持数组中的数组（如 `[[a]] [[a.b]]` 内含数组值），复杂嵌套建议用JSON
- YAML的锚点与别名在 `safe_dump` 下会展开为独立副本，不保留引用关系
- XML与JSON的转换中，XML文本节点与属性节点的映射需自定义规则
- 批量转换不支持递归子目录，仅处理顶层文件
