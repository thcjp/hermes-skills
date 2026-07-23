---
slug: "feishu-doc"
name: "feishu-doc"
version: "1.2.7"
displayName: "Feishu Doc"
summary: "抓取飞书Wiki/文档/表格/多维表格内容,自动解析URL"
license: "Proprietary"
description: |-
  Fetch content from Feishu (Lark) Wiki, Docs, Sheets, and Bitable。Automatically
  resolves Wiki URL。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写.
tags:
  - Knowledge
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Feishu Doc

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Feishu Doc自动解析 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |

## 核心能力

- 抓取飞书 Wiki（知识库）、Docx（云文档）、Sheet（电子表格）、Bitable（多维表格）内容
- 自动解析飞书文档 URL，识别文档类型并提取 token，支持短链展开与重定向跟踪
- 将飞书文档块结构转换为 Markdown / 纯文本 / JSON 格式输出
- 支持批量抓取知识库下所有子文档，保留目录层级结构
- 提取电子表格数据为结构化 JSON，支持指定工作表、单元格范围与格式选项
- 解析多维表格记录，支持按视图筛选、字段映射与关联记录展开

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文档抓取 | 飞书文档 URL 或 token | Markdown 格式正文与元信息 |
| 知识库导出 | Wiki 空间 ID 与节点路径 | 完整目录树与各节点内容 |
| 表格数据提取 | 电子表格 URL 与工作表名 | 结构化 JSON 数据 |
| 多维表格查询 | Bitable URL 与筛选条件 | 记录列表与字段值 |
| 短链解析 | 飞书短链 URL | 展开后的完整 URL 与文档 token |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

### 流程详解：文档内容抓取

**步骤 1：识别 URL 类型**

飞书文档 URL 有多种格式，需要先识别类型再调用对应接口：

| URL 格式 | 文档类型 | 提取 token |
|:---------|:---------|:-----------|
| `https://xxx.feishu.cn/wiki/AAbbCCdd` | Wiki 知识库节点 | 需调用接口获取真实 doc_token |
| `https://xxx.feishu.cn/docx/AAbbCCdd` | Docx 云文档 | 路径中直接提取 `AAbbCCdd` |
| `https://xxx.feishu.cn/sheets/AAbbCCdd` | 电子表格 | 路径中直接提取 `AAbbCCdd` |
| `https://xxx.feishu.cn/base/AAbbCCdd` | 多维表格 | 路径中直接提取 `AAbbCCdd` |
| `https://xxx.feishu.cn/short/~/AAbbCCdd` | 短链 | 需请求获取重定向目标 |

**步骤 2：Wiki URL 解析**

Wiki 节点的 URL 中的 token 并非真实文档 token，需要通过 API 转换：

```
请求: GET /open-apis/wiki/v2/spaces/get_node?token=AAbbCCdd
响应: {
  "data": {
    "node": {
      "node_token": "AAbbCCdd",
      "obj_token": "真实文档token",
      "obj_type": "docx"  // 文档类型: docx/doc/wiki/bitable
    }
  }
}
```

**步骤 3：抓取文档内容**

根据文档类型调用不同接口获取内容：

- **Docx 文档**：调用 `GET /open-apis/docx/v1/documents/{document_id}/blocks` 获取文档块树，然后递归遍历转换为 Markdown
- **电子表格**：调用 `GET /open-apis/sheets/v3/spreadsheets/{spreadsheet_token}/sheets` 获取工作表列表，再按 sheet_id 获取单元格数据
- **多维表格**：调用 `GET /open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records` 获取记录列表

## URL 解析与内容提取示例

### 示例 1：抓取 Wiki 文档并转为 Markdown

```
输入 URL: https://example.feishu.cn/wiki/WkIbslDkNiNbGHnlpABCDj

处理流程:
1. 从 URL 提取 node_token: WkIbslDkNiNbGHnlpABCDj
2. 调用 wiki API 获取 obj_token 和 obj_type
3. obj_type=docx, obj_token=DOCNabcdef123456
4. 调用 docx API 获取文档块列表
5. 遍历块结构，转换规则:
   - block_type=2 (文本) -> 普通段落
   - block_type=3 (标题1) -> # 标题
   - block_type=4 (标题2) -> ## 标题
   - block_type=12 (无序列表) -> - 列表项
   - block_type=15 (代码块) -> ```lang ... ```
   - block_type=27 (表格) -> | a | b | 表格语法
6. 输出完整 Markdown 文本
```

### 示例 2：提取电子表格数据

```
输入 URL: https://example.feishu.cn/sheets/Iow7sNbNeabcdef123

查询参数:
- sheet_id: "sheetA1B2C3"  (工作表 ID)
- range: "A1:Z1000"        (单元格范围，可选)
- value_render_option: "ToString"  (值格式: ToString/Formula/FormattedValue)

输出 JSON:
{
  "spreadsheet_token": "Iow7sNbNeabcdef123",
  "sheets": [
    {
      "sheet_id": "sheetA1B2C3",
      "title": "销售数据",
      "rows": 150,
      "data": [
        {"日期": "2024-01-01", "产品": "商品A", "销量": 320, "金额": 9600},
        {"日期": "2024-01-02", "产品": "商品B", "销量": 215, "金额": 6450}
      ]
    }
  ]
}
```

### 示例 3：查询多维表格记录

```
输入 URL: https://example.feishu.cn/base/bascnabcdef123

筛选条件:
- filter: AND(CurrentValue.[状态] = "进行中")
- page_size: 100
- field_names: ["任务名称", "负责人", "截止日期"]

输出:
{
  "app_token": "bascnabcdef123",
  "table_id": "tbl123456",
  "total": 42,
  "records": [
    {
      "record_id": "rec001",
      "fields": {
        "任务名称": "API 接口开发",
        "负责人": {"text": "张三", "id": "ou_abc123"},
        "截止日期": 1700000000000
      }
    }
  ]
}
```

## 文档块类型转换对照表

| 块类型 (block_type) | 飞书名称 | Markdown 映射 |
|:---:|:---------|:-------------|
| 1 | 页面 Page | 文档标题 |
| 2 | 文本 Text | 普通段落 |
| 3 | 标题1 Heading1 | `# 标题` |
| 4 | 标题2 Heading2 | `## 标题` |
| 5 | 标题3 Heading3 | `### 标题` |
| 9 | 有序列表 | `1. 列表项` |
| 12 | 无序列表 | `- 列表项` |
| 13 | 代码块 | ` ```lang ... ``` ` |
| 14 | 引用 | `> 引用文本` |
| 15 | 等式 | `$$ 公式 $$` |
| 22 | 分隔线 | `---` |
| 27 | 表格 | `\| a \| b \|` |

## 最佳实践

### 批量抓取知识库

当需要导出整个知识空间时，建议采用递归方式遍历目录树：

1. 调用 `GET /open-apis/wiki/v2/spaces/{space_id}/nodes` 获取根节点列表
2. 对每个节点判断是否有子节点，递归获取子节点
3. 根据 `obj_type` 分别调用对应文档接口获取内容
4. 按目录层级保存文件，保留原有组织结构

**注意事项**：
- 每次请求间隔建议 > 200ms，避免触发 API 频率限制
- 文档块数量超过 500 时需分页获取，使用 `page_token` 参数
- 部分文档可能因权限不足无法访问，需捕获错误并记录跳过

### 处理富文本内联元素

飞书文档的文本块中可能包含多种内联元素，转换时需特殊处理：

| 元素类型 | 处理方式 |
|:---------|:---------|
| 加粗 | `**文本**` |
| 斜体 | `*文本*` |
| 删除线 | `~~文本~~` |
| 行内代码 | `` `代码` `` |
| 链接 | `[文本](URL)` |
| @人名 | `@用户名` |
| 公式 | `$公式$` |

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| url | string | 是 | 飞书文档 URL，支持 wiki/docx/sheets/base/短链 |
| doc_type | string | 否 | 文档类型: `wiki`/`docx`/`sheets`/`bitable`，未指定时自动识别 |
| output_format | string | 否 | 输出格式: `markdown`/`text`/`json`，默认 `markdown` |
| content | string | 否 | feishu-doc处理的内容输入，可选值: json/text/markdown |
| sheet_id | string | 否 | 电子表格工作表 ID（仅 sheets 类型） |
| filter | string | 否 | 多维表格筛选条件（仅 bitable 类型） |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "doc_type": "docx",
    "doc_token": "DOCNabcdef123456",
    "title": "产品需求文档 - v2.0",
    "content": "# 产品需求文档 - v2.0\n\n## 背景\n\n...",
    "blocks_count": 156,
    "metadata": {
      "template_used": "feishu-doc-parser",
      "word_count": 3200,
      "style": "专业",
      "source_url": "https://example.feishu.cn/wiki/WkIbslDkNiNbGHnlpABCDj",
      "resolved_url": "https://example.feishu.cn/docx/DOCNabcdef123456"
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

### Q1: 如何开始使用Feishu Doc？
A: 提供飞书文档 URL 即可。系统会自动识别 URL 类型（Wiki/Docx/Sheets/Bitable），解析 token 并抓取内容。对于 Wiki 链接，会先调用 API 获取真实文档 token，再抓取对应内容。输出默认为 Markdown 格式，也可指定输出为 JSON 或纯文本。

### Q2: Wiki URL 和 Docx URL 有什么区别？
A: Wiki URL（路径含 `/wiki/`）是知识库节点链接，其 token 是 node_token，需要通过 API 转换为真实的 obj_token 才能获取文档内容。Docx URL（路径含 `/docx/`）是直接文档链接，其 token 可直接用于调用文档接口。本 Skill 会自动处理这个转换过程。

### Q3: 抓取文档时提示权限不足怎么办？
A: 确认应用已被添加为文档协作者，或文档已对应用开启"云文档全部权限"。对于知识库文档，需在知识库设置中添加应用为成员并授予"可阅读"权限。若文档属于其他部门创建，可能需要联系文档所有者手动授权。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

