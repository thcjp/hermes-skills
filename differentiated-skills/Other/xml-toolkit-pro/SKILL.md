---
slug: xml-toolkit-pro
name: xml-toolkit-pro
version: "1.0.0"
displayName: XML处理工具专业版
summary: 流式解析、XSD验证、格式互转与批量处理，适合数据团队与企业级XML数据治理。
license: Proprietary
edition: pro
description: |-
  XML处理工具专业版，面向数据团队与企业的高阶XML处理平台。核心能力:
  - 流式解析大文件（SAX/StAX）
  - XSD/RelaxNG 模式验证
  - XML/JSON/YAML/CSV 互转
  - 批量处理与目录递归
  - XPath 2。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
- XML
- 企业数据处理
- 格式转换
- 专业版
tools:
  - - read
- exec
---

# XML处理工具（专业版）

## 概述

专业版在免费版的命名空间处理、编码规范、转义与 XPath 查询之上，扩展为面向数据团队与企业的完整 XML 处理平台。新增流式解析、XSD 验证、格式互转、批量处理与高级查询，同时与免费版的解析规则保持向后兼容。

## 核心能力

| 能力 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 解析模式 | DOM（全加载） | DOM + SAX/StAX（流式） |
| 模式验证 | 良构检查 | DTD + XSD + RelaxNG |
| 格式互转 | 不支持 | XML/JSON/YAML/CSV 互转 |
| 批量处理 | 单文件 | 批量 + 目录递归 |
| XPath | 1.0 子集 | XPath 2.0+ |
| 大文件支持 | 受内存限制 | 流式处理 GB 级文件 |
| 报告 | 不支持 | 处理报告 + 验证报告 |
| 自定义映射 | 不支持 | XML↔对象映射 |

## 使用场景

### 场景一：流式解析大文件

处理 GB 级的 XML 文件，避免内存溢出。

```python
import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ""
        self.count = 0

    def startElement(self, name, attrs):
        self.current = name

    def characters(self, content):
        if self.current == "record":
            self.count += 1
            if self.count % 10000 == 0:
                print(f"已处理 {self.count} 条记录")

# 流式解析大文件
parser = xml.sax.make_parser()
parser.setContentHandler(MyHandler())
parser.parse("large-data.xml")  # 可处理 GB 级文件
```

### 场景二：XSD 模式验证

验证 XML 是否符合 XSD 模式。

```bash
# 批量验证
xml-pro validate \
  --input ./xml-files/ \
  --schema ./schemas/config.xsd \
  --recursive \
  --report validation-report.md

# 输出
# 📊 验证报告
# 总文件: 45
# 有效: 42 ✅
# 无效: 3 ❌
#   - config-12.xml: 元素 'port' 类型不匹配（期望整数，得到字符串）
#   - config-23.xml: 缺少必需属性 'name'
#   - config-34.xml: 未知元素 'unknown-tag'
```

### 场景三：XML 与 JSON 互转

将 XML 转换为 JSON 供 API 消费。

```bash
# XML 转 JSON
xml-pro convert xml-to-json \
  --input config.xml \
  --output config.json \
  --preserve-namespaces \
  --pretty

# JSON 转 XML
xml-pro convert json-to-xml \
  --input data.json \
  --output data.xml \
  --root "data" \
  --encoding utf-8

# 批量转换
xml-pro convert batch \
  --input ./xml/ \
  --output ./json/ \
  --to json \
  --recursive
```

## 快速开始

```bash
# 1. 初始化专业版工作区
xml-pro init --workspace ~/xml-pro

# 2. 解析（兼容免费版）
xml-pro parse --file input.xml --format pretty

# 3. 流式解析大文件
xml-pro parse --file large.xml --mode stream --handler record-counter

# 4. XSD 验证
xml-pro validate --file config.xml --schema config.xsd

# 5. 格式转换
xml-pro convert xml-to-json --file config.xml --output config.json

# 6. 批量处理
xml-pro batch convert --input ./xml/ --to json --output ./json/
```

## 示例

```yaml
# ~/xml-pro/config.yaml
edition: pro
parse:
  default_mode: dom
  large_file_threshold: 100MB
  stream_handler: default
validate:
  schemas:
    - name: config
      path: ~/xml-pro/schemas/config.xsd
    - name: data
      path: ~/xml-pro/schemas/data.xsd
  strict: false
convert:
  xml_to_json:
    preserve_namespaces: true
    pretty: true
    array_detection: true
  json_to_xml:
    root: root
    encoding: utf-8
    namespace: ""
batch:
  max_concurrent: 5
  recursive: true
  backup: true
xpath:
  version: "2.0"
  namespaces_support: true
report:
  formats: [markdown, json]
  include_diff: true
```

## 格式互转对照

| 源格式 | 目标格式 | 说明 |
|:-------|:---------|:-----|
| XML | JSON | 保留命名空间前缀 |
| XML | YAML | 简化结构表示 |
| XML | CSV | 提取重复元素为行 |
| JSON | XML | 添加根元素 |
| YAML | XML | 保持顺序 |
| CSV | XML | 每行一个记录元素 |

## 最佳实践

* 大文件（>100MB）使用流式解析，避免内存溢出。
* XSD 验证在生产环境前置执行，确保数据合规。
* 格式互转时注意命名空间与属性的保留策略。
* 批量处理启用并发控制，避免 IO 瓶颈。
* XML 转 JSON 时启用数组检测，避免单元素被解析为对象。
* 验证失败时查看详细错误报告，定位具体位置。
* 定期导出处理报告，作为数据治理依据。
* 编码统一使用 UTF-8，避免多编码混乱。

## 常见问题

**Q：专业版与免费版的解析规则兼容吗？**
A：兼容。免费版的所有解析规则在专业版中默认遵循，专业版额外支持流式、验证、互转等能力。

**Q：流式解析支持哪些 handler？**
A：内置记录计数、字段提取、过滤等 handler。支持自定义 handler。

**Q：XSD 验证支持哪些版本？**
A：支持 XSD 1.0 与 1.1。同时支持 DTD 与 RelaxNG。

**Q：格式互转会丢失信息吗？**
A：XML 转 JSON 时命名空间与属性会保留为特殊字段。CDATA 会转为普通文本。建议启用 `preserve_namespaces`。

**Q：批量处理有文件数量上限吗？**
A：无硬性上限，建议单批不超过 1000 个文件。可通过 `--max-concurrent` 控制并发。

**Q：可以与数据库集成吗？**
A：专业版支持将 XML 解析结果导出为 SQL 插入语句，便于导入各类数据库。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.9+
- **Node.js**: 18+（批量与转换功能需要）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 官方站点下载 |
| lxml | 库 | 推荐 | pip 安装 |
| Node.js | 运行时 | 可选 | 官方站点下载 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 脚本执行能力）
- **说明**: 专业版在 Markdown 指令基础上，提供流式解析、XSD 验证与格式互转能力

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
