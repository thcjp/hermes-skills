---
slug: figma-2
name: figma-2
version: "0.1.1"
displayName: Figma
summary: Figma 集成。浏览团队项目与文件，读取设计结构、页面、节点，导出图片，管理评论，查看版本历史，检查组件/组件集/样式，获取设计变量（Token）。通过
  MorphixAI 代理安全访问 Fi...
license: MIT
description: |-
  Figma 集成。浏览团队项目与文件，读取设计结构、页面、节点，导出图片，管理评论，查看版本历史，检查组件/组件集/样式，获取设计变量（Token）。通过
  MorphixAI 代理安全访问 Fi...

  核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 页面, 读取设计结构, 浏览团队项目, token, figma, 集成, morphixai, 与文件
tags:
- Creative
tools:
- read
- exec
---

# Figma

通过 `mx_figma` 工具访问 Figma 工作区：浏览项目文件、读取设计结构、导出图片、管理评论、查看组件库/组件集/样式、获取设计变量（Design Token）。

## 前置条件

1. **安装插件**: `skill-platform plugins install skill-platform-morphixai`
2. **获取 API Key**: 访问 [morphix.app/api-keys](https://morphix.app/api-keys) 生成 `mk_xxxxxx` 密钥
3. **配置环境变量**: `export MORPHIXAI_API_KEY="[REDACTED]"`
4. **链接账号**: 访问 [morphix.app/connections](https://morphix.app/connections) 链接 Figma 账号，或通过 `mx_link` 工具链接（app: `figma`）

## 核心操作

### 查看当前用户

```text
mx_figma:
  action: get_me
```

### 浏览团队项目

```text
mx_figma:
  action: list_team_projects
  team_id: "123456789"
```

### 列出项目中的文件

```text
mx_figma:
  action: list_project_files
  project_id: "987654321"
```

### 获取文件结构

```text
mx_figma:
  action: get_file
  file_key: "abc123DEF456"
  depth: 2  # 1=仅页面, 2=页面+Frame, 省略=完整树
```

> `file_key` 从 Figma URL 中提取：`figma.com/design/{file_key}/...`

### 获取指定节点

```text
mx_figma:
  action: get_file_nodes
  file_key: "abc123DEF456"
  node_ids: ["1:2", "3:4"]
  depth: 1
```

### 导出图片

```text
mx_figma:
  action: export_images
  file_key: "abc123DEF456"
  node_ids: ["1:2"]
  format: "png"   # jpg / png / svg / pdf
  scale: 2        # 0.01–4, 默认 1
```

> 返回 node_id → 图片 URL 的映射。

### 评论操作

**列出评论：**

```text
mx_figma:
  action: list_comments
  file_key: "abc123DEF456"
```

**发表评论：**

```text
mx_figma:
  action: post_comment
  file_key: "abc123DEF456"
  message: "这个按钮的圆角需要改为 8px"
```

**回复评论：**

```text
mx_figma:
  action: post_comment
  file_key: "abc123DEF456"
  message: "已修改，请确认"
  comment_id: "12345"
```

**删除评论：**

```text
mx_figma:
  action: delete_comment
  file_key: "abc123DEF456"
  comment_id: "12345"
```

### 版本历史

```text
mx_figma:
  action: list_versions
  file_key: "abc123DEF456"
```

### 组件

**文件内组件：**

```text
mx_figma:
  action: get_file_components
  file_key: "abc123DEF456"
```

**团队组件库：**

```text
mx_figma:
  action: get_team_components
  team_id: "123456789"
  page_size: 30
```

### 组件集（变体）

组件集是包含多个变体的容器，例如 `Button` 组件集包含 Primary、Secondary 等变体。

**文件内组件集：**

```text
mx_figma:
  action: get_file_component_sets
  file_key: "abc123DEF456"
```

**团队组件集：**

```text
mx_figma:
  action: get_team_component_sets
  team_id: "123456789"
```

### 样式

**文件内样式：**

```text
mx_figma:
  action: get_file_styles
  file_key: "abc123DEF456"
```

**团队样式库：**

```text
mx_figma:
  action: get_team_styles
  team_id: "123456789"
```

### 设计变量（Design Token）

获取文件中定义的变量（颜色、数值、字符串、布尔值），对应 MCP 的 `get_variable_defs` 功能。

**本地变量：**

```text
mx_figma:
  action: get_local_variables
  file_key: "abc123DEF456"
```

> 返回 `variables`（变量定义）和 `variableCollections`（变量集合/分组）。
> 变量包含 `resolvedType`（COLOR/FLOAT/STRING/BOOLEAN）和 `valuesByMode`（各模式下的值）。

**发布的变量（跨文件共享）：**

```text
mx_figma:
  action: get_published_variables
  file_key: "abc123DEF456"
```

## 常见工作流

### 设计走查

```text
1. mx_figma: get_file, file_key: "xxx", depth: 1  → 查看页面列表
2. mx_figma: get_file_nodes, file_key: "xxx", node_ids: ["page_id"]  → 查看页面详情
3. mx_figma: list_comments, file_key: "xxx"  → 查看设计评论
4. mx_figma: post_comment  → 添加走查反馈
```

### 设计资产导出

```text
1. mx_figma: get_file, file_key: "xxx", depth: 2  → 找到目标 Frame
2. mx_figma: export_images, node_ids: ["frame_id"], format: "svg", scale: 2  → 导出 SVG
```

### 设计系统检查

```text
1. mx_figma: get_file_components, file_key: "xxx"  → 查看文件组件
2. mx_figma: get_file_component_sets, file_key: "xxx"  → 查看组件变体
3. mx_figma: get_file_styles, file_key: "xxx"  → 查看文件样式
4. mx_figma: get_local_variables, file_key: "xxx"  → 查看设计变量/Token
5. mx_figma: get_team_components, team_id: "xxx"  → 查看团队组件库
```

### 开发阶段：获取图层和组件信息

```text
1. mx_figma: get_file, file_key: "xxx", depth: 2  → 获取页面和 Frame 结构
2. mx_figma: get_file_nodes, file_key: "xxx", node_ids: ["target_node"]  → 获取指定节点详细属性
3. mx_figma: get_file_components, file_key: "xxx"  → 获取可复用组件列表
4. mx_figma: get_file_component_sets, file_key: "xxx"  → 获取组件变体（Primary/Secondary 等）
5. mx_figma: get_local_variables, file_key: "xxx"  → 获取颜色/间距/字体等设计 Token
6. mx_figma: export_images, file_key: "xxx", node_ids: ["icon_id"], format: "svg"  → 导出图标资源
```

### 版本对比

```text
1. mx_figma: list_versions, file_key: "xxx"  → 查看历史版本
2. mx_figma: list_comments, file_key: "xxx"  → 查看相关讨论
```

## 注意事项

* `file_key` 从 Figma URL 获取：`https://figma.com/design/{file_key}/...`
* `node_id` 格式为 `"1:2"`（冒号分隔），从 Figma URL 的 `node-id` 参数获取（URL 中用 `-` 分隔，需转为 `:`）
* `get_file` 不带 `depth` 参数会返回完整文件树，大文件可能很慢，建议使用 `depth: 1` 或 `depth: 2`
* 导出图片返回的是临时 URL，有效期有限
* `account_id` 参数通常省略，工具自动检测已链接的 Figma 账号
* 变量 API 可能需要 Figma Enterprise 计划才能完整使用

## 与 Figma MCP 的关系

Figma 官方 MCP 提供了一些本 skill 无法通过 REST API 实现的功能：

| MCP 专有功能 | 说明 |
| --- | --- |
| `get_design_context` | 返回参考代码 + 截图 + 上下文（设计转代码核心） |
| `get_code_connect_map` | 设计节点→代码组件映射 |
| `generate_figma_design` | 网页截图导入 Figma |
| `generate_diagram` | FigJam 中生成 Mermaid 图表 |

本 skill 覆盖了 Figma REST API 的全部核心能力，适用于项目管理、设计系统检查和开发资源获取。对于设计转代码等高级工作流，建议配合 Figma MCP 使用。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
