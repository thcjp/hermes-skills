---
slug: "json-parser"
name: "json-parser"
version: "2.1.0"
displayName: "Json Parser"
summary: "解析校验建筑API/IoT/BIM的JSON并转表"
license: "Proprietary"
description: |-
  Parse and validate JSON data from construction APIs, IoT sensors, and
  BIM exports。Transform nest。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - Integrations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Json Parser

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Json Parser解析校验 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 核心能力

Construction systems increasingly use JSON for data exchange - from IoT sensors to BIM metadata exports. This skill handles parsing, validation, and flattening of JSON structures.
#
## 适用场景

### 1. BIM Metadata

```python
bim_parser = BIMJSONParser()
result = bim_parser.parse_file("revit_export.json")
elements = bim_parser.parse_bim_elements(result.data)
```

### 2. IoT Sensors

```python
iot_parser = IoTJSONParser()
readings = iot_parser.parse_sensor_batch(sensor_data)
```

### 3. API Response

```python
parser = ConstructionJSONParser()
result = parser.parse_string(api_response)
df = parser.to_dataframe(result.data)
```

## 使用流程

```python
parser = ConstructionJSONParser()
# ...
result = parser.parse_file("bim_export.json")
if result.success:
    df = parser.to_dataframe(result.data)
    print(f"Loaded {len(df)} records")
# ...
flat = parser.flatten_json(result.data)
# ...
elements = parser.extract_elements(result.data, "project.building.floors")
```

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "parser 相关配置参数",
    result: "parser 相关配置参数"
  },
  "error": null
}
```

## 异常处理

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
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

### 示例1：基础用法

```
```python
parser = ConstructionJSONParser()

result = parser.parse_file("bim_export.json")
if result.success:
    df = parser.to_dataframe(result.data)
    print(f"Loaded {len(df)} records")

flat = parser.flatten_json(result.data)

elements = parser.extract_elements(result.data, "project.building.floors")
```
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用

## 常见问题

**Q: 如何处理异常输入?**
A: 系统会自动检测并返回错误提示, 同时提供修复建议.
**Q: 支持哪些输入格式?**
A: 支持标准文本、JSON、CSV等常见格式.