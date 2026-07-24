---
slug: "notion"
name: "notion"
version: 1.0.1
displayName: "Notion"
summary: "Notion API创建管理页面/数据库/块。Notion API for creating and managing pages, databases, and blocks。核心能力:"
license: "Proprietary"
description: |-
  Notion API for creating and managing pages, databases, and blocks。核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Productivity
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"
---
# Notion

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| NotionAPI创建管理 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 核心能力

- **页面管理**：通过Notion API创建、读取、更新、删除页面，支持设置页面属性、标题、图标、封面
- **数据库操作**：创建数据库、查询数据库条目、按属性筛选与排序、批量插入与更新记录
- **块内容编辑**：向页面追加文本块、标题块、列表块、代码块、引用块、分割线等Block类型
- **属性类型支持**：处理标题、文本、数字、选择(Select)、多选(Multi-select)、日期、人员、文件、复选框、URL、邮箱、公式、关联(Relation)等属性
- **搜索功能**：按标题和内容搜索用户有权限访问的页面和数据库
- **批量操作**：支持单次请求批量创建最多100个块、批量查询数据库条目（分页获取）

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 项目管理 | 项目名称与任务列表 | Notion数据库 + 任务页面 + 属性配置 |
| 知识库构建 | 文档分类与内容 | 结构化页面树 + 数据库索引 + 关联关系 |
| 会议记录 | 会议时间与参会人 | 会议笔记页面 + 任务分配数据库 + 关联页面 |
| 数据导入 | CSV/JSON数据 | Notion数据库条目 + 属性映射 + 批量创建 |
| 自动化工作流 | 触发条件与操作 | 定时创建页面 + 属性更新 + 状态流转 |

**不适用于**：Notion页面实时协作编辑、Notion评论管理、Notion工作区设置管理、文件上传（需配合files API）

## 使用流程

1. 确认运行环境满足依赖说明中的要求，已配置Notion Integration Token
2. 在Notion中将目标页面/数据库与Integration共享（添加连接）
3. 确定操作类型：创建页面、查询数据库、追加块内容等
4. 构造API请求参数（页面ID、数据库ID、块内容JSON）
5. 执行操作并检查返回的页面ID或块ID
6. 验证结果：在Notion中打开对应页面确认内容正确

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | 操作描述或JSON格式的页面/块内容 |
| operation | string | 否 | 操作类型，可选值: `create_page`/`query_db`/`append_blocks`/`search`/`update_page`，默认 `search` |
| database_id | string | 否 | 目标数据库ID（查询/创建数据库条目时使用） |
| page_id | string | 否 | 目标页面ID（追加块/更新页面时使用） |
| token | string | 否 | Notion Integration Token，也可通过环境变量 `NOTION_TOKEN` 配置 |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "page": {
      "id": "page-uuid-string",
      "url": "https://notion.so/page-uuid-string",
      "properties": {
        "Name": {
          "title": [{"text": {"content": "新任务"}}]
        },
        "Status": {
          "select": {"name": "进行中", "color": "blue"}
        }
      }
    },
    "metadata": {
      "template_used": "reviewer",
      "operation": "create_page",
      "blocks_created": 3,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 详细使用示例

### 示例1：创建数据库条目

```json
{
  "operation": "create_page",
  "database_id": "abc123def456",
  "content": {
    "Name": {"title": [{"text": {"content": "修复登录Bug"}}]},
    "Status": {"select": {"name": "待处理"}},
    "Priority": {"select": {"name": "高"}},
    "Due Date": {"date": {"start": "2024-01-20"}},
    "Tags": {"multi_select": [{"name": "前端"}, {"name": "紧急"}]}
  }
}
```

### 示例2：查询数据库并筛选

```json
{
  "operation": "query_db",
  "database_id": "abc123def456",
  "content": {
    "filter": {
      "and": [
        {"property": "Status", "select": {"equals": "待处理"}},
        {"property": "Priority", "select": {"equals": "高"}}
      ]
    },
    "sorts": [
      {"property": "Due Date", "direction": "ascending"}
    ],
    "page_size": 10
  }
}
```

### 示例3：向页面追加内容块

```json
{
  "operation": "append_blocks",
  "page_id": "page-uuid-string",
  "content": {
    "children": [
      {
        "object": "block",
        "type": "heading_2",
        "heading_2": {"rich_text": [{"type": "text", "text": {"content": "会议纪要"}}]}
      },
      {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "讨论了Q1路线图"}}]}
      },
      {
        "object": "block",
        "type": "to_do",
        "to_do": {"rich_text": [{"type": "text", "text": {"content": "完成API文档"}}], "checked": false}
      },
      {
        "object": "block",
        "type": "code",
        "code": {"rich_text": [{"type": "text", "text": {"content": "npm install"}}], "language": "bash"}
      }
    ]
  }
}
```

### 示例4：搜索页面

```json
{
  "operation": "search",
  "content": {
    "query": "项目计划",
    "filter": {"property": "object", "value": "page"},
    "page_size": 5
  }
}
```

## 支持的块类型

| 块类型 | API字段名 | 说明 |
|:-------|:----------|:-----|
| 段落 | `paragraph` | 普通文本段落 |
| 一级标题 | `heading_1` | H1标题 |
| 二级标题 | `heading_2` | H2标题 |
| 三级标题 | `heading_3` | H3标题 |
| 无序列表项 | `bulleted_list_item` | 圆点列表 |
| 有序列表项 | `numbered_list_item` | 数字列表 |
| 待办事项 | `to_do` | 复选框，支持checked属性 |
| 代码块 | `code` | 支持language属性 |
| 引用 | `quote` | 引用块 |
| 分割线 | `divider` | 水平分割线 |
| 切换块 | `toggle` | 可折叠内容块 |
| 呼叫块 | `callout` | 高亮提示框 |

## 最佳实践

### Integration配置
- 在 https://notion.so/my-integrations 创建Internal Integration获取Token
- Token格式为 `secret_xxxxxxxxxxxx`，以环境变量 `NOTION_TOKEN` 存储
- 必须在目标页面/数据库点击"..." → "Connections" → 添加Integration才能访问

### 数据库属性映射
- 标题属性使用 `title` 类型，每个数据库只能有一个标题属性
- Select/Multi-select的选项需预先在Notion中创建，或通过API自动创建
- 日期属性使用ISO 8601格式：`{"start": "2024-01-20", "end": "2024-01-21"}`
- Relation属性需提供目标数据库ID和关联页面ID

### 批量操作
- 单次 `append_blocks` 最多创建100个块，超出需分批请求
- `query_db` 默认返回10条，最大100条，通过 `start_cursor` 分页获取
- 避免频繁API调用，Notion API限制每秒3次请求

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
| Notion Integration Token | API | 必需 | https://notion.so/my-integrations |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export NOTION_TOKEN="secret_your_integration_token_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.

## 常见问题

### Q1: 如何开始使用Notion API？
A: 首先在 https://notion.so/my-integrations 创建Internal Integration，获取Token（`secret_` 开头）。然后在Notion中打开要操作的页面或数据库，点击右上角"..." → "Connections" → 搜索并添加你的Integration。最后将Token设置为环境变量 `NOTION_TOKEN`，即可通过 `create_page`、`query_db`、`append_blocks` 等操作管理Notion内容。

### Q2: 为什么API返回"object not found"错误？
A: 此错误表示Integration没有访问目标资源的权限。Notion的权限模型要求每个页面/数据库单独授权。解决方法：打开目标页面 → "..." → "Connections" → 添加Integration。注意：如果页面在子页面中，需要对父页面授权，子页面会继承权限。

### Q3: 如何处理富文本格式（加粗、斜体、链接）？
A: Notion的富文本通过 `rich_text` 数组实现，每个元素可指定不同样式。例如加粗文本：`{"type": "text", "text": {"content": "重要"}, "annotations": {"bold": true}}`。链接文本：`{"type": "text", "text": {"content": "点击这里", "link": {"url": "https://example.com"}}}`。一个 `rich_text` 数组可包含多个不同样式的文本段。

### Q4: 数据库查询的筛选语法是怎样的？
A: 筛选使用 `filter` 对象，支持 `and`/`or` 组合条件。单属性筛选：`{"property": "Status", "select": {"equals": "进行中"}}`。多属性组合：`{"and": [{"property": "Status", "select": {"equals": "进行中"}}, {"property": "Priority", "select": {"equals": "高"}}]}`。每种属性类型有不同的筛选操作符：select支持 `equals`/`does_not_equal`，date支持 `before`/`after`/`on_or_before`，text支持 `contains`/`starts_with`。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
| 401 Unauthorized | Token无效或过期 | 重新生成Integration Token，更新环境变量 |
| 404 object_not_found | Integration未授权访问目标资源 | 在Notion页面中添加Integration连接 |
| 429 rate_limited | API请求频率超限（3次/秒） | 降低请求频率，添加请求间隔延迟 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 不支持Notion评论API（comments）
- 不支持文件上传到Notion（需使用files API单独处理）
- 不支持页面导出为PDF/Markdown（需使用Notion内置导出功能）
- API请求限制为每秒3次，大批量操作需分批并加延迟
- 块内容单次最多追加100个块，超出需分批请求
