---
slug: "feishu-doc-write"
name: "feishu-doc-write"
version: 1.0.1
displayName: "feishu-doc-write"
summary: "飞书文档API写入规范,把Markdown转飞书Block结构。Feishu (Lark) Document API writing spec。Converts Markdown conte"
license: "MIT"
description: |-
  Feishu (Lark) Document API writing spec。Converts Markdown content to
  Feishu Block structures and。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解.
tags:
  - Knowledge
  - 工具
  - 效率
  - 创意
  - block_type
  - content
  - api
  - json
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# feishu-doc-write

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |
| 消息频控与智能排队 | 不支持 | 支持 |

## 核心能力

- Feishu (Lark) Document API writing spec
- Converts Markdown content to
  Feishu Block structures and
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文档处理 | 文件路径与格式选项 | 转换结果与页面信息 |
| 飞书文档API写入规 | 目标数据与配置参数 | 处理结果与执行状态 |
| 把Markdown转 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | feishu-doc-write处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "write_result": "write_result_value",
      "write_metadata": "write_metadata_value",
      "write_status": "write_status_value"
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

中间产物模板参考: `assets/feishu-doc-write_template`

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
## 案例展示

### Text

```json
{
  "block_type": 2,
  "text": {
    "elements": [{
      "text_run": {
        "content": "Paragraph text here",
        "text_element_style": { "bold": false, "italic": false }
      }
    }]
  }
}
```

### Heading

```json
{ "block_type": 3, "heading1": { "elements": [{ "text_run": { "content": "H1 Title" } }] } }
{ "block_type": 4, "heading2": { "elements": [{ "text_run": { "content": "H2 Title" } }] } }
```

### Bullet / Ordered List

```json
{ "block_type": 12, "bullet": { "elements": [{ "text_run": { "content": "List item" } }] } }
{ "block_type": 13, "ordered": { "elements": [{ "text_run": { "content": "Numbered item" } }] } }
```

Each list item is a **separate Block**.

### Code Block

```json
{
  "block_type": 14,
  "code": {
    "elements": [{ "text_run": { "content": "console.log('hello');" } }],
    "style": { "language": 23, "wrap": false }
  }
}
```

Common language enums: PlainText=1, JavaScript=23, Python=40, TypeScript=49, Go=20, Shell=46, SQL=47, Java=22, Rust=44, C=12, CSS=17, HTML=21, Docker=19.

### Callout (Feishu-specific highlight box)

Callout is a **container block** — create it first, then add child blocks inside.

```json
// Step 1: Create callout as document child
{ "block_type": 19, "callout": { "background_color": 3, "border_color": 3, "emoji_id": "star" } }
# ...
// Step 2: POST .../blocks/{callout_block_id}/children
{ "children": [{ "block_type": 2, "text": { "elements": [{ "text_run": { "content": "Highlight text" } }] } }] }
```

Color enums: Red=1, Orange=2, Yellow=3, Green=4, Blue=5, Purple=6, Grey=7.

### Divider

```json
{ "block_type": 22, "divider": {} }
```

### Image (two-step)

```text
Step 1: Create placeholder block { "block_type": 27, "image": {} }
Step 2: Upload via POST /open-apis/drive/v1/medias/upload_all
  - multipart/form-data: file, file_name, parent_type="docx_image", parent_node=<image_block_id>
```

## 常见问题

### Q1: 如何开始使用feishu-doc-write？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
