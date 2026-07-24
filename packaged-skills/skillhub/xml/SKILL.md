---
slug: "xml"
name: "xml"
version: 1.0.1
displayName: "XML"
summary: "解析生成转换XML,命名空间与编码处理正确。Parse, generate, and transform XML with correct namespace handling and en"
license: "Proprietary"
description: |-
  Parse, generate, and transform XML with correct namespace handling and
  encoding。核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Other
  - 工具
  - 效率
  - 自动化
  - 知识
  - 文档
  - 创意
  - 图像
  - 安全
  - xml
  - book
  - title
  - xsl
  - python
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"
---
# XML

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| XML解析生成转换 | 不支持 | 支持 |
| XML命名空间与编码处理 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |

## 核心能力

- Parse, generate, and transform XML with correct namespace handling and encoding
- XML Schema (XSD) 验证与文档类型定义 (DTD) 校验
- XSLT 转换与 XPath 查询
- XML 与 JSON/CSV/YAML 互转
- XXE 防护与安全 XML 处理

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## XML 解析方式对比

| 解析方式 | 特点 | 内存占用 | 适用场景 |
|:-----|:------|:------|:------|
| DOM | 加载整个文档到内存树结构 | 高 | 需要随机访问、修改文档 |
| SAX | 事件驱动，逐元素回调 | 低 | 大文件流式读取，只读场景 |
| StAX | 拉取式流解析，游标控制 | 低 | 需要流式处理且控制解析进度 |
| XPath | 路径表达式查询节点 | 中 | 快速定位特定节点 |

### DOM 解析示例（Python）

```python
import xml.etree.ElementTree as ET

# 解析XML
tree = ET.parse('catalog.xml')
root = tree.getroot()

# 遍历所有book节点
for book in root.findall('.//book'):
    title = book.find('title').text
    author = book.find('author').text
    price = book.get('price')  # 属性访问
    print(f"{title} by {author} - ${price}")

# 修改节点
book = root.find('.//book[@id="b001"]')
book.find('price').text = '39.99'

# 写回文件
tree.write('catalog.xml', encoding='UTF-8', xml_declaration=True)
```

### XPath 查询示例

| 查询需求 | XPath 表达式 | 说明 |
|:------|:------|:------|
| 所有book节点 | `//book` | 任意层级的book |
| 指定ID的book | `//book[@id='b001']` | 属性过滤 |
| 价格大于30的书 | `//book[number(@price) > 30]` | 数值比较 |
| 第一个book的title | `(//book)[1]/title/text()` | 索引取值 |
| 包含特定关键词 | `//title[contains(text(), 'Python')]` | 文本包含 |

## 命名空间处理

### 带命名空间的XML示例

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root xmlns="http://example.com/default"
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:media="http://search.yahoo.com/mrss/">
  <item id="001">
    <dc:title>XML进阶指南</dc:title>
    <dc:creator>张三</dc:creator>
    <media:content url="https://example.com/cover.jpg" type="image/jpeg"/>
  </item>
</root>
```

### 命名空间查询（Python）

```python
ns = {
    'def': 'http://example.com/default',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'media': 'http://search.yahoo.com/mrss/'
}

# 查询带命名空间的节点
title = root.find('.//def:item/dc:title', ns)
creator = root.find('.//def:item/dc:creator', ns)
content_url = root.find('.//def:item/media:content', ns).get('url')
```

**命名空间常见陷阱**：
- 默认命名空间（无前缀）在XPath中必须显式指定前缀，不能省略
- 不同命名空间下可以有同名元素，不会冲突
- 命名空间URI区分大小写，必须完全匹配

## XSLT 转换示例

### XML 转 HTML

```xml
<!-- transform.xsl -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <table border="1">
          <tr><th>标题</th><th>作者</th><th>价格</th></tr>
          <xsl:for-each select="//book">
            <tr>
              <td><xsl:value-of select="title"/></td>
              <td><xsl:value-of select="author"/></td>
              <td><xsl:value-of select="@price"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```

## 编码处理

### 常见编码问题与解决方案

| 问题 | 原因 | 解决方案 |
|:------|:------|:------|
| 中文乱码 | 声明编码与实际编码不一致 | 确保XML声明 `<?xml version="1.0" encoding="UTF-8"?>` 与文件实际编码一致 |
| BOM导致解析失败 | UTF-8 BOM头被误认为内容 | 使用 `utf-8-sig` 编码读取，或移除BOM |
| 特殊字符报错 | `<`, `>`, `&`, `'`, `"` 未转义 | 使用实体引用: `&lt;` `&gt;` `&amp;` `&apos;` `&quot;` |
| CDATA未闭合 | CDATA段内含 `]]>` | 分割为两段CDATA: `]]]]><![CDATA[>` |

### 安全处理：XXE防护

XML外部实体（XXE）攻击通过DOCTYPE声明读取系统文件。安全处理应禁用外部实体：

```python
# Python安全解析（防御XXE）
from defusedxml import ElementTree as ET
tree = ET.parse('input.xml')  # defusedxml自动禁用外部实体

# 或使用标准库时手动禁用
import xml.etree.ElementTree as ET
parser = ET.XMLParser()
# Python 3.8+ 默认禁用外部实体，但仍建议使用defusedxml
```

## XSD 验证示例

### Schema 定义

```xml
<!-- schema.xsd -->
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="book">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="title" type="xs:string" minOccurs="1"/>
        <xs:element name="author" type="xs:string" maxOccurs="unbounded"/>
        <xs:element name="price" type="xs:decimal"/>
        <xs:element name="published" type="xs:date"/>
      </xs:sequence>
      <xs:attribute name="id" type="xs:string" use="required"/>
      <xs:attribute name="category" type="xs:string"/>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### 常用数据类型

| XSD类型 | 说明 | 示例值 |
|:------|:------|:------|
| xs:string | 字符串 | "Hello" |
| xs:integer | 整数 | 42 |
| xs:decimal | 十进制数 | 19.99 |
| xs:boolean | 布尔值 | true / false |
| xs:date | 日期 | 2026-07-24 |
| xs:dateTime | 日期时间 | 2026-07-24T10:30:00 |
| xs:email | 邮箱（需pattern） | user@example.com |
| xs:anyURI | URI | https://example.com |

## XML 与其他格式互转

### XML 转 JSON

```python
import xmltodict
import json

# XML → JSON
with open('data.xml', 'r', encoding='utf-8') as f:
    xml_str = f.read()
json_data = xmltodict.parse(xml_str)
print(json.dumps(json_data, indent=2, ensure_ascii=False))

# JSON → XML
xml_output = xmltodict.unparse(json_data, pretty=True)
```

**互转注意事项**：
- XML属性在JSON中以 `@` 前缀表示（如 `@id` → `"@id": "b001"`）
- XML文本内容在JSON中以 `#text` 键表示
- 多个同名元素在JSON中自动转为数组
- XML命名空间信息在转换中可能丢失，需额外处理
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 数据解析 | 原始内容与格式 | 结构化字段与提取结果 |
| 编码执行 | 需求描述与约束条件 | 代码文件与测试结果 |
| 内容生成 | 提示词与风格参数 | 生成内容与质量评分 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | xml处理的内容输入 |,  |
| content | string | 否 | xml处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "xml 相关配置参数",
    result: "xml 相关配置参数",
    result: "xml 相关配置参数",
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
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

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
## 常见问题

### Q1: 如何开始使用XML？
A: 提供你的XML处理需求即可，例如"解析这个XML文件并提取所有book节点的title"、"将这个JSON转换为XML"、"验证这个XML是否符合给定的XSD Schema"。系统会根据需求选择合适的解析方式（DOM/SAX/StAX），生成可执行的代码并解释每一步操作。

### Q2: XML命名空间查询为什么返回空结果？
A: 最常见的原因是默认命名空间（xmlns="..."无前缀）在XPath中被忽略。标准XPath 1.0不支持空前缀匹配默认命名空间。解决方法：在查询时为默认命名空间显式分配一个前缀（如 `def`），然后用 `//def:element` 查询。系统会自动处理命名空间映射，无需手动维护前缀对照表。

### Q3: 如何处理超大XML文件（>100MB）？
A: 对于大文件，应避免使用DOM解析（会将整个文件加载到内存）。推荐使用SAX或StAX流式解析：SAX适合只读遍历场景，通过事件回调处理每个元素；StAX适合需要控制解析进度的场景，通过游标按需拉取元素。系统会根据文件大小自动推荐合适的解析方式，大文件默认使用流式解析。

### Q4: XML转JSON后属性和文本内容如何区分？
A: 使用xmltodict等库转换时，XML属性以 `@` 前缀表示（如 `@price`），元素文本内容以 `#text` 键表示。例如 `<book id="b001" price="29.99">Python指南</book>` 转为 `{"book": {"@id": "b001", "@price": "29.99", "#text": "Python指南"}}`。系统在转换时会自动处理这些约定，并在输出中添加注释说明。

### Q5: 如何防止XXE攻击？
A: XXE（XML外部实体）攻击通过DOCTYPE中的实体定义读取系统文件或发起SSRF请求。防护措施：（1）使用defusedxml库替代标准xml.etree；（2）禁用DOCTYPE声明；（3）禁用外部实体解析。系统生成的所有XML解析代码默认采用安全配置，已禁用外部实体和DOCTYPE处理。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

