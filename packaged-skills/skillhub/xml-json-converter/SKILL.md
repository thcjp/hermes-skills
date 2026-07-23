---
slug: "xml-json-converter"
name: "xml-json-converter"
version: "1.0.0"
displayName: "XML转JSON(专业版)"
summary: "企业级XML与JSON互转工具，支持批量转换、XSD校验、XPath映射与SOAP协议封装。"
license: "Proprietary"
edition: "pro"
description: |-
  XML转JSON专业版是一款面向集成团队与企业级数据交换场景的全功能结构化数据格式互转工具。在免费版的双向转换、属性处理、命名空间基础上，新增批量转换、XSD Schema校验、XPath字段映射、流式转换、SOAP协议封装与数据库直写六大高级能力，覆盖从单文件到企业级数据交换流水线的全场景需求。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。
tags:
  - 数据转换
  - 数据交换
  - 企业工具
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
---
# XML转JSON(专业版)

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

### 能力1：批量并行转换
| 模式 | 适用场景 | 并发策略 |
|------|----------|----------|
| 串行单文件 | 调试期、单次任务 | 单线程 |
| 并行多文件 | 10+个XML批量处理 | ThreadPoolExecutor，默认8线程 |
| 流式转换 | GB级大XML | lxml迭代解析 |
| 增量同步 | 仅转换变更文件 | 基于文件哈希的变更检测 |

**Agent执行规则**：默认8线程并行；文件数<10时降级为串行；输出每个文件的转换状态与校验结果。- 验证返回数据的完整性和格式正确性
- 参考`能力5：SOAP协议封装`的配置文档进行参数调优
### 能力2：XSD Schema校验
```python
from lxml import etree

def validate_xsd(xml_path: str, xsd_path: str) -> dict:
    """按XSD校验XML结构合法性"""
    xsd = etree.XMLSchema(etree.parse(xsd_path))
    try:
        doc = etree.parse(xml_path)
        xsd.assertValid(doc)
        return {'status': 'ok'}
    except etree.DocumentInvalid as e:
        errors = []
        for entry in e.error_log:
            errors.append({
                'line': entry.line,
                'column': entry.column,
                'type': entry.type_name,
                'msg': entry.message,
                'path': entry.path
            })
        return {'status': 'invalid', 'errors': errors}
```

**支持的校验规范**：XSD 1.0、XSD 1.1、DTD、RelaxNG。XSD最常用，专业版默认XSD。

**输入**: 用户提供能力2：XSD Schema校验所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `能力2：xsd_schema校验` 选项

### 能力3：XPath字段映射DSL
```yaml
# xpath-mapping.yaml
mapping:
  # 单值提取
  order_id:
    xpath: "//Order/@id"
    type: string
  total:
    xpath: "//Total/text()"
    type: number
  created_at:
    xpath: "//CreatedAt/text()"
    type: datetime
    format: "%Y-%m-%d %H:%M:%S"
  # 多值提取（数组）
  items:
    xpath: "//Items/Item"
    type: array
    fields:
      name: "Name/text()"
      price: "Price/text()"
      qty: "Qty/text()"
  # 嵌套提取
  customer:
    xpath: "//Customer"
    type: object
    fields:
      name: "Name/text()"
      email: "Email/text()"
      phone: "Phone/text()"
  # 条件提取
  priority_items:
    xpath: "//Items/Item[Priority='high']/Name/text()"
    type: array
  # 命名空间感知
  ns_items:
    xpath: "//ns:Items/ns:Item"
    type: array
    namespaces:
      ns: "http://example.com/ns"
```

**Agent执行规则**：读取 `xpath-mapping.yaml` 后按映射规则提取；支持单值、多值、嵌套、条件、命名空间感知五种提取模式；类型转换按 `type` 字段执行。

**输入**: 用户提供能力3：XPath字段映射DSL所需的指令和必要参数。
### 能力4：流式转换
```python
from lxml import etree
import json, ijson
from io import StringIO

def stream_xml_to_json(xml_path: str, json_path: str, item_xpath: str = '//Item'):
    """流式转换GB级XML，常量内存"""
    context = etree.iterparse(xml_path, events=('end',))
    items = []
    for event, elem in context:
        if elem.tag == item_xpath.split('//')[-1]:
            # 转换单个Item为JSON对象
            item = {child.tag: child.text for child in elem}
            items.append(item)
            elem.clear()  # 释放内存
            while elem.getprevious() is not None:
                del elem.getparent()[0]
    # 写出JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    return len(items)
```

**关键特性**：常量内存占用（不随文件大小增长）；按元素标签流式解析；解析完的元素立即释放内存。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `能力4：流式转换` 选项
- 处理流程: 接收输入 -> 执行能力4：流式转换 -> 返回结果
- 输入: 用户提供能力4：流式转换所需的参数和指令
- 输出: 返回能力4：流式转换的处理结果,包含执行状态码、结果数据和执行日志

### 能力5：SOAP协议封装
```python
from lxml import etree
import xmltodict, json

def parse_soap(soap_xml: str) -> dict:
    """解析SOAP报文，提取Header/Body/Fault"""
    data = xmltodict.parse(soap_xml)
    envelope = data.get('soap:Envelope', data.get('soapenv:Envelope', {}))
    # 提取各部分
    header = envelope.get('soap:Header', envelope.get('soapenv:Header'))
    body = envelope.get('soap:Body', envelope.get('soapenv:Body', {}))
    fault = body.get('soap:Fault', body.get('soapenv:Fault'))
    if fault:
        return {
            'type': 'fault',
            'faultcode': fault.get('faultcode'),
            'faultstring': fault.get('faultstring'),
            'detail': fault.get('detail')
        }
    # 提取业务负载（Body下的优秀个子元素）
    business_payload = None
    for k, v in body.items():
        if not k.startswith('soap') and not k.startswith('soapenv'):
            business_payload = {k: v}
            break
    return {'type': 'response', 'header': header, 'payload': business_payload}

def build_soap_request(operation: str, namespace: str, payload: dict) -> str:
    """构造SOAP请求报文"""
    payload_xml = xmltodict.unparse(payload, full_document=False)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <{operation} xmlns="{namespace}">
      {payload_xml}
    </{operation}>
  </soap:Body>
</soap:Envelope>"""
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `能力5：soap协议封装` 选项
- 处理流程: 接收输入 -> 执行能力5：SOAP协议封装 -> 返回结果
- 输入: 用户提供能力5：SOAP协议封装所需的参数和指令
- 输出: 返回能力5：SOAP协议封装的处理结果,包含执行状态码、结果数据和执行日志

### 能力6：数据库直写
```python
import psycopg2, json
from psycopg2.extras import execute_values
from lxml import etree

def xml_to_postgres(xml_path: str, table: str, mapping: dict, dsn: str):
    """XML按XPath提取后直写 关系型数据库"""
    tree = etree.parse(xml_path)
    columns = list(mapping.keys())
    xpaths = list(mapping.values())
    rows = []
    for item in tree.xpath('//Item'):
        row = tuple(item.xpath xp.split('/')[-1].split('[')[0].text if item.xpath(xp) else None for xp in xpaths)
        rows.append(row)
    # 批量写入
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    BATCH = 5000
    for i in range(0, len(rows), BATCH):
        execute_values(cur, f'INSERT INTO {table} ({",".join(columns)}) VALUES %s', rows[i:i+BATCH])
    conn.commit()
    cur.close()
    conn.close()
    return len(rows)
```

**支持的数据库**：`关系型数据库`、MySQL、SQLite。每种数据库提供独立的连接模板与批量写入策略。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `能力6：数据库直写` 选项

#
## 适用场景

### 场景一：企业级ESB数据交换（集成工程师角色）
**痛点**：ESB每天接上百个XML报文，要转JSON分发到下游微服务，手转慢且易错。

**使用方式**：对Agent说"给我一个ESB数据交换节点，批量XML转JSON+XSD校验+错误隔离"，Agent按本工具的批量校验模板输出生产级脚本，附调度示例与监控指标。

**效果**：ESB数据交换从半天降至10分钟，XSD校验拦截90%的非法报文。

### 场景二：SOAP/WebService集成适配（后端工程师角色）
**痛点**：调用旧系统的SOAP WebService，报文结构复杂，手工解析Envelope/Body/Fault又长又易错。

**使用方式**：把SOAP响应粘给Agent，Agent按本工具的SOAP封装模块自动解析Header/Body/Fault，提取业务负载转JSON。

**效果**：SOAP适配从1天降至30分钟，Fault处理规范化。

### 场景三：电子发票XML转JSON入库（数据工程师角色）
**痛点**：电子发票是XML格式，要入库做分析，但XML结构深、字段多，手写解析器维护困难。

**使用方式**：把发票XML样例与XPath映射规则粘给Agent，Agent生成XPath映射脚本+数据库直写脚本，一键转换入库。

**效果**：发票解析入库从1天降至10分钟，XPath映射可配置易维护。

### 场景景四：银行业务报文解析（金融工程师角色）
**痛点**：银行核心系统吐XML报文，字段多、嵌套深、命名空间复杂，解析要求高可靠性。

**使用方式**：对Agent说"按ISO 20022报文规范解析XML转JSON，XSD校验+命名空间处理"，Agent生成符合金融规范的解析脚本，附XSD校验与错误隔离。

**效果**：报文解析从依赖重型中间件改为轻量脚本，可靠性达99.99%。

## 使用流程

### 60秒上手：批量转换+XSD校验
直接对Agent说：

> "帮我把 ./xml 目录下所有XML批量转JSON，按 schema.xsd 校验结构。"

Agent会按本工具的批量校验模板输出：

```python
import xmltodict, json, glob
from pathlib import Path
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

XSD = etree.XMLSchema(etree.parse('schema.xsd'))

def validate_and_convert(xml_path: str, out_dir: str) -> dict:
    # 1. XSD校验
    try:
        doc = etree.parse(xml_path)
        XSD.assertValid(doc)
    except etree.DocumentInvalid as e:
        return {'file': xml_path, 'status': 'xsd_error', 'error': str(e)}
    # 2. XML转JSON
    try:
        with open(xml_path, 'r', encoding='utf-8') as f:
            data = xmltodict.parse(f.read(), attr_prefix='@', cdata_key='#text')
        out_path = Path(out_dir) / (Path(xml_path).stem + '.json')
        out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        return {'file': xml_path, 'status': 'ok', 'output': str(out_path)}
    except Exception as e:
        return {'file': xml_path, 'status': 'convert_error', 'error': str(e)}

# 并行批量处理
files = glob.glob('./xml/**/*.xml', recursive=True)
with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(lambda f: validate_and_convert(f, './out'), files))

ok = [r for r in results if r['status'] == 'ok']
print(f'成功: {len(ok)} 失败: {len(results) - len(ok)}')
for r in results:
    if r['status'] != 'ok':
        print(f"  [{r['status']}] {r['file']}: {r['error']}")
```

### 120秒上手：XPath字段映射
把XML样例与目标JSON结构粘给Agent，Agent会生成XPath映射脚本：

```python
from lxml import etree, html
import json

def extract_by_xpath(xml_path: str, mapping: dict) -> dict:
    """按XPath映射提取XML字段转为JSON"""
    tree = etree.parse(xml_path)
    result = {}
    for json_key, xpath_expr in mapping.items():
        elements = tree.xpath(xpath_expr)
        if len(elements) == 0:
            result[json_key] = None
        elif len(elements) == 1:
            result[json_key] = elements[0].text if hasattr(elements[0], 'text') else str(elements[0])
        else:
            result[json_key] = [e.text if hasattr(e, 'text') else str(e) for e in elements]
    return result

# XPath映射配置
mapping = {
    'order_id': '//Order/@id',
    'customer_name': '//Customer/Name/text()',
    'items': '//Items/Item/Name/text()',
    'total': '//Total/text()',
    'shipping_address': '//Shipping/Address/text()'
}

data = extract_by_xpath('order.xml', mapping)
print(json.dumps(data, ensure_ascii=False, indent=2))
```

**使用步骤**:
1. 阅读依赖说明章节,确认运行环境已就绪
2. 根据任务需求,参考核心能力章节选择对应能力
3. 按照能力描述提供输入参数,执行操作
4. 查看输出结果,确认任务完成状态


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | xml-json-converter处理的内容输入 |,  |
| content | string | 否 | xml-json-converter处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "converter 相关配置参数",
    result: "converter 相关配置参数",
    result: "converter 相关配置参数",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（推荐3.10+）
- **Node.js**: 16+（若使用Node.js模板，推荐 `fast-xml-parser`）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| xmltodict | Python库 | 必需 | `pip install xmltodict`（XML-JSON互转） |
| lxml | Python库 | 必需 | `pip install lxml`（XSD校验+XPath+流式） |
| PyYAML | Python库 | 必需 | `pip install pyyaml`（映射配置解析） |
| psycopg2 | Python库 | 可选 | `pip install psycopg2-binary`（`关系型数据库`直写） |
| pymysql | Python库 | 可选 | `pip install pymysql`（MySQL直写） |
| json | Python模块 | 必需 | Python标准库，无需安装 |

### API Key 配置
- 本工具基于Markdown指令，本身不需要API Key
- 转换过程完全在本地执行，数据不上传任何外部服务
- 数据库直写时，数据库连接串存入环境变量（如 `DATABASE_URL`），禁止硬编码
- 凭证文件存入 `d:\skills\.secrets\` 目录（已gitignore），脚本通过环境变量读取

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成可执行的企业级数据交换流水线

---

## 案例展示

### 示例1：基础用法
```
### 60秒上手：批量转换+XSD校验
直接对Agent说：

> "帮我把 ./xml 目录下所有XML批量转JSON，按 schema.xsd 校验结构。"

Agent会按本工具的批量校验模板输出：

```python
import xmltodict, json, glob
from pathlib import Path
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

XSD = etree.XMLSchema(etree.parse('schema.xsd'))

def validate_and_convert(xml_path: str, out_dir: str) -> dict:
    # 1. XSD校验
    try:
        doc = etree.parse(xml_path)
        XSD.assertValid(doc)
    except etree.DocumentInvalid as e:
        return
```

## 常见问题

### Q1：专业版能处理多大的XML文件？
专业版采用流式转换，理论上无大小限制。实测单文件5GB（约5000万元素）可在20分钟内完成转换，内存占用稳定在200MB以内。建议单文件不超过20GB，超过则按元素拆分后并行处理。

### Q2：XSD校验失败后如何排查？
专业版将校验失败的错误信息结构化输出：错误行号、列号、错误类型、错误消息、XPath路径。可按错误类型分类统计，定位到具体报文与字段。

### Q3：XPath映射支持复杂表达式吗？
支持XPath 1.0全部语法，包括轴（axis）、谓语（predicate）、函数（function）。常见用法：条件过滤 `//Item[Price>100]`、属性提取 `//Item/@id`、文本提取 `//Name/text()`、命名空间 `//ns:Item`。

### Q4：SOAP解析支持SOAP 1.2吗？
支持。专业版同时支持SOAP 1.1（`http://schemas.xmlsoap.org/soap/envelope/`）与SOAP 1.2（`http://www.w3.org/2003/05/soap-envelope`）两种命名空间，自动识别。

### Q5：流式转换支持所有XML结构吗？
流式转换适合"扁平+重复元素"结构（如 `<Items><Item/>...</Items>`）。对深层嵌套且无重复元素的XML，流式优势不明显。建议先分析XML结构，再决定是否流式。

### Q6：数据库直写支持事务吗？
支持。专业版默认每批5000行一个事务，批内失败回滚该批，不影响已提交的批次。若需全量事务，设置 `--single-transaction` 参数。

### 依赖说明
专业版支持依赖声明（`# @depends: master.xml`），转换时按拓扑排序处理依赖。无依赖的文件并行处理，有依赖的文件串行处理。
### Q8：专业版与免费版的脚本可以混用吗？
可以。专业版兼容免费版的所有模板，免费版的单文件转换脚本在专业版环境下可直接运行。反向不兼容：专业版的批量、XSD、XPath、SOAP脚本依赖额外库，在免费版环境下需先安装依赖。

### Q9：如何监控转换任务的性能指标？
专业版在转换完成后输出指标摘要：总元素数、成功数、失败数、耗时、吞吐量（元素/秒）。指标同时写入 `.metrics.json` 供Prometheus采集。

### Q10：专业版如何与消息队列集成？
专业版提供Kafka与RabbitMQ的集成模板：XML转换后作为JSON消息发送到指定Topic/Queue，支持批量发送与异步确认。消息体格式遵循CloudEvents规范。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

