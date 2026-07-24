---
slug: "xml-parser-tool"
name: "xml-parser-tool"
version: "2.1.1"
displayName: "Xml Reader"
summary: "读解析建筑系统XML,P6进度/BSDD/IFC-XML/COBie-XML。Read and parse XML from construction systems - P6 schedu"
license: "MIT"
description: |-
  Read and parse XML from construction systems - P6 schedules, BSDD exports,
  IFC-XML, COBie-XML. This skill parses XML and converts to structured DataFrames.
tags:
  - Other
  - 工具
  - 效率
  - 写作
  - activities
  - reader
  - xml
  - root
tools:
  - read
  - write
  - exec
homepage: ""
category: "Automation"
---
# Xml Reader

## 核心能力

XML is used in construction for P6 schedules (XER), IFC-XML, COBie-XML, and buildingSMART Data Dictionary exports. This skill parses XML and converts to structured DataFrames.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 1. P6 Schedule Import

```python
p6_reader = P6XMLReader()
schedule = p6_reader.parse_full_schedule("p6_export.xml")
# ...
activities = schedule['activities']
print(f"Activities: {len(activities)}")
```

### 2. COBie Data

```python
cobie_reader = COBieXMLReader()
cobie_data = cobie_reader.parse_cobie("facility_cobie.xml")
# ...
components = cobie_data.get('Component', pd.DataFrame())
```

### 3. IFC-XML Analysis

```python
ifc_reader = IFCXMLReader()
root = ifc_reader.parse_file("model.ifcxml")
# ...
types = ifc_reader.get_entity_types(root)
for entity_type, count in sorted(types.items(), key=lambda x: -x[1])[:10]:
    print(f"{entity_type}: {count}")
```

## 使用流程

```python
reader = ConstructionXMLReader()
# ...
root = reader.parse_file("schedule.xml")
# ...
activities = reader.find_elements(root, "Activity")
print(f"Found {len(activities)} activities")
# ...
df = reader.elements_to_dataframe(activities)
```

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
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
    result: "tool 相关配置参数",
    result: "tool 相关配置参数"
  },
  "error": null
}
```

## 异常处理

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

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

## 案例展示

### 示例1：基础用法

```
```python
reader = ConstructionXMLReader()

root = reader.parse_file("schedule.xml")

activities = reader.find_elements(root, "Activity")
print(f"Found {len(activities)} activities")

df = reader.elements_to_dataframe(activities)
```
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪.
### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界.