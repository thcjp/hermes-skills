---
slug: "diagram-generator"
name: "diagram-generator"
version: "1.0.0"
displayName: "Diagram生成器"
summary: "通过MCP工具生成与编辑Draw.io/Mermaid/Excalidraw图表,支持网络拓扑/架构/流程图/UML等"
license: "Proprietary"
description: |-
  diagram-generator 图表生成客户端。通过 mcp-diagram-generator MCP 服务器将自然语言意图转换为结构化 JSON 规范,
  生成与编辑 Draw.io(.drawio)、Mermaid(.mmd)、Excalidraw(.excalidraw) 三种格式的图表。
  支持网络拓扑、系统架构、流程图、泳道、UML(时序/类/ER)、白板手绘等六类图,提供默认输出路径、自定义文件名、
  交互式采集、质量门校验、配置初始化等能力。通过 init_config 与 get_config 管理输出目录,
  通过 generate_diagram 提交 JSON 规范生成文件。适用于架构文档、流程规范、UML 设计、白板协作等场景。
tags:
  - Creative
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# Diagram Generator

通过 mcp-diagram-generator MCP 服务器将自然语言意图转换为结构化 JSON 规范,生成与编辑 Draw.io、Mermaid、Excalidraw 三种格式的图表文件。支持六类图的专属生成策略与质量校验。

**范围外**(本技能不做): 手工绘制位图、SVG 矢量编辑、PDF 排版、PPT 幻灯片、3D 建模、动画与交互式可视化。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。

## 核心能力

### 必需 MCP 工具

生成图表前,验证以下 MCP 工具可用:
- `mcp__mcp-diagram-generator__get_config`: 查看当前输出目录配置
- `mcp__mcp-diagram-generator__generate_diagram`: 提交 JSON 规范生成图表
- `mcp__mcp-diagram-generator__init_config`: 初始化默认配置

若工具缺失

**输入**: 用户提供必需 MCP 工具所需的参数和指令。
**处理**: 按照skill规范执行必需 MCP 工具操作。

### 支持的格式与图类型


**输入**: 用户提供支持的格式与图类型所需的指令和必要参数。
**处理**: 按照skill规范执行支持的格式与图类型操作,遵循单一意图原则。
**输出**: 返回支持的格式与图类型的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`支持的格式与图类型`相关配置参数进行设置
### 格式
- Draw.io: `.drawio`,适合复杂网络与架构图
- Mermaid: `.mmd` 或 markdown 内嵌,适合代码仓库文档
- Excalidraw: `.excalidraw`,适合白板手绘风格

**输入**: 用户提供格式所需的指令和必要参数。
**处理**: 按照skill规范执行格式操作,遵循单一意图原则。
**输出**: 返回格式的执行结果,包含操作状态和输出数据。
### 图类型与默认格式

| 图类型 | 默认格式 | 默认方向 |
| --- | --- | --- |
| 网络拓扑 | Draw.io | 垂直 |
| 

**输入**: 用户提供支持的格式与图类型所需的参数和指令。
**处理**: 按照skill规范执行支持的格式与图类型操作。
**输出**: 返回支持的格式与图类型的执行结果,包含操作状态和输出数据。

### 主工作流


**输入**: 用户提供主工作流所需的指令和必要参数。
**处理**: 按照skill规范执行主工作流操作,遵循单一意图原则。
**输出**: 返回主工作流的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`主工作流`相关配置参数进行设置
### 采集意图

对新建图表,在处理完整 prompt 前收集以下选项:
- 图类型(网络拓扑/架构/流程图/泳道/UML/白板)
- 输出格式(Draw.io/Mermaid/Excalidraw)
- 布局方向(垂直/水平/自动)
- 使用场景(Word/PPT/代码仓库/白板协作)
- 可选文件名或输出目录

用户已提供全部选项与完整 prompt 时跳过采集。对已有文件编辑,仅询问目标文


### 配置助手

初始化默认配置: `init_config()`

设置自定义路径:
```json
{
  "paths": {
    "drawio": "output/diagrams/drawio",
    "mermaid": "output/diagrams/mermaid",
    "excalidraw": "output/diagrams/excalidraw"
  }
}
```

查看

**输入**: 用户提供配置助手所需的参数和指令。
**处理**: 按照skill规范执行配置助手操作。

#
## 必需 MCP 工具

生成图表前,验证以下 MCP 工具可用:
- `mcp__mcp-diagram-generator__get_config`: 查看当前输出目录配置
- `mcp__mcp-diagram-generator__generate_diagram`: 提交 JSON 规范生成图表
- `mcp__mcp-diagram-generator__init_config`: 初始化默认配置

若工具缺失,需配置 MCP 服务器并重启 Agent 环境。推荐远程配置:
```json
{
  "mcpServers": {
    "mcp-diagram-generator": {
      "command": "npx",
      "args": ["-y", "mcp-diagram-generator"]
    }
  }
}
```

首次使用时服务器会创建 `.diagram-config.json` 与默认输出目录 `diagrams/{format}/`。

## 支持的格式与图类型

### 格式
- Draw.io: `.drawio`,适合复杂网络与架构图
- Mermaid: `.mmd` 或 markdown 内嵌,适合代码仓库文档
- Excalidraw: `.excalidraw`,适合白板手绘风格

### 图类型与默认格式

| 图类型 | 默认格式 | 默认方向 |
| --- | --- | --- |
| 网络拓扑 | Draw.io | 垂直 |
| 系统架构 | Draw.io | 垂直或自动 |
| 流程图 | Mermaid | 垂直 |
| 泳道 | Draw.io | 水平 |
| 时序/类/ER | Mermaid | 自动 |
| 白板手绘 | Excalidraw | 自动 |

使用场景可覆盖默认值: Word 文档优先纵向、PPT 横向可读性优先、代码仓库优先 Mermaid、白板协作优先 Excalidraw、复杂网络或架构优先 Draw.io。

## 主工作流

### 采集意图

对新建图表,在处理完整 prompt 前收集以下选项:
- 图类型(网络拓扑/架构/流程图/泳道/UML/白板)
- 输出格式(Draw.io/Mermaid/Excalidraw)
- 布局方向(垂直/水平/自动)
- 使用场景(Word/PPT/代码仓库/白板协作)
- 可选文件名或输出目录

用户已提供全部选项与完整 prompt 时跳过采集。对已有文件编辑,仅询问目标文件路径与变更内容(若缺失)。

### 分派 Playbook

按图类型选择单一主 playbook:
- 网络拓扑(数据中心/区域/路由/交换机/防火墙): `references/playbook-network-topology.md`
- 系统架构(分层组件图): `references/playbook-architecture.md`
- 流程图(决策树): `references/playbook-flowchart.md`
- 泳道(跨团队交接/审批): `references/playbook-swimlane.md`
- UML(时序/类/ER): `references/playbook-uml.md`
- 白板手绘(Excalidraw 非正式): `references/playbook-excalidraw.md`
- 格式不确定: 先读 `references/format-selection-guide.md`,再读对应 playbook

仅读取当前图所需的 playbook。涉及显式几何坐标时,额外读 `references/layout-quality-guide.md`。

### 构建 JSON 规范

遵循 `references/json-schema-guide.md` 的 schema,核心结构:
```json
{
  "format": "drawio",
  "diagramType": "architecture",
  "title": "图表标题",
  "elements": [
    {
      "id": "unique-id",
      "type": "container",
      "name": "显示名",
      "level": "environment",
      "geometry": { "x": 0, "y": 0, "width": 800, "height": 600 },
      "children": []
    },
    {
      "type": "edge",
      "source": "source-id",
      "target": "target-id"
    }
  ]
}
```

通用规则:
- `elements` 必须是数组
- ID 必须唯一
- 边必须为顶层元素,不能放在 `children` 内
- 边的 `source` 与 `target` 必须指向已存在的节点或容器
- `style` 必须是对象
- 颜色使用 `#RRGGBB`
- Draw.io 无填充节点使用 `fillColor: "none"`

### 质量门校验

调用 MCP 服务器前验证:
- 格式与采集答案和 playbook 一致
- `diagramType` 在支持时显式声明
- 布局方向反映在坐标或生成器专属字段
- 复杂 Draw.io 与 Excalidraw 图表提供显式 `geometry`
- 容器层级合法
- 边为顶层元素
- 文本与连接器规则符合所选格式

生成后检查保存文件,确认格式专属属性存在。MCP 服务器代码变更时,运行 `npm run test:diagrams`。

### 调用 MCP 工具生成

调用 `generate_diagram`,传入 `diagram_spec` 与可选 `filename` 或 `output_path`:
```json
{
  "diagram_spec": "<规范对象>",
  "filename": "architecture-overview.drawio"
}
```

服务器校验 schema、创建缺失目录、未提供输出路径时写入配置的默认目录。

## 配置助手

初始化默认配置: `init_config()`

设置自定义路径:
```json
{
  "paths": {
    "drawio": "output/diagrams/drawio",
    "mermaid": "output/diagrams/mermaid",
    "excalidraw": "output/diagrams/excalidraw"
  }
}
```

查看配置: `get_config()`

更新单格式路径:
```json
{
  "format": "drawio",
  "path": "custom/drawio-path"
}
```

## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及 playbook |
| --- | --- | --- | --- |
| 系统架构文档化 | 为微服务系统画分层架构图 | Draw.io 架构图,含网关/服务/数据层 | architecture |
| 网络拓扑规划 | 画三个数据中心的双活拓扑 | Draw.io 拓扑图,含环境/数据中心/区域/设备四级层级 | network-topology |
| 流程规范输出 | 为报销审批流程画泳道图 | Draw.io 泳道图,跨部门交接与审批节点 | swimlane |
| 代码仓库文档 | 为用户登录流程画时序图 | Mermaid 时序图,可直接嵌入 markdown | uml |

**不适用于**: 位图绘制、SVG 矢量编辑、PDF 排版、PPT 制作、3D 建模、动画与交互式可视化。

## 使用流程

### 检查 MCP 工具可用性
确认 `mcp__mcp-diagram-generator__generate_diagram` 等三个工具已注册。若缺失,按"必需 MCP 工具"章节配置服务器并重启 Agent 环境。

### 采集意图或读取已有文件
1. 新建: 收集图类型/格式/方向/场景/文件名
2. 编辑: 读取目标 `.drawio`/`.mmd`/`.excalidraw` 文件,解析现有结构

### 分派对应 playbook
仅读取当前图类型所需的 playbook 与(如需)`json-schema-guide.md` 或 `layout-quality-guide.md`。

### 构建与校验 JSON 规范
按 schema 构建 `elements` 数组,执行质量门检查。

### 调用 MCP 工具生成
传入 `diagram_spec` 与可选 `filename` 或 `output_path`,服务器返回保存文件路径。

#
## 案例展示

### 案例一： 微服务系统架构图
**场景**: 后端团队需要为新上线的电商系统绘制分层架构图,用于内部技术评审

意图采集后确定: 图类型=系统架构,格式=Draw.io,方向=垂直,场景=PPT,文件名=`ecommerce-arch.drawio`。

读取 `references/playbook-architecture.md` 与 `references/json-schema-guide.md`,构建规范:
```json
{
  "format": "drawio",
  "diagramType": "architecture",
  "title": "电商系统架构",
  "elements": [
    {
      "id": "gateway-tier",
      "type": "container",
      "name": "接入层",
      "geometry": { "x": 0, "y": 0, "width": 800, "height": 120 },
      "children": [
        { "id": "api-gw", "type": "node", "name": "API Gateway" },
        { "id": "lb", "type": "node", "name": "Load Balancer" }
      ]
    },
    {
      "id": "service-tier",
      "type": "container",
      "name": "服务层",
      "geometry": { "x": 0, "y": 140, "width": 800, "height": 200 },
      "children": [
        { "id": "user-svc", "type": "node", "name": "用户服务" },
        { "id": "order-svc", "type": "node", "name": "订单服务" },
        { "id": "payment-svc", "type": "node", "name": "支付服务" }
      ]
    },
    { "type": "edge", "source": "api-gw", "target": "user-svc" },
    { "type": "edge", "source": "api-gw", "target": "order-svc" },
    { "type": "edge", "source": "order-svc", "target": "payment-svc" }
  ]
}
```

调用生成: `{ "diagram_spec": "<上述规范>", "filename": "ecommerce-arch.drawio" }`

**输出**: `diagrams/drawio/ecommerce-arch.drawio` 文件路径

**说明**: 容器分层反映接入层与服务层,边为顶层元素连接跨层节点。垂直布局适合 PPT 横屏展示,显式 `geometry` 确保层级间距可控。

### 案例二： 跨部门报销审批泳道图
**场景**: 财务团队需要规范报销审批流程,涉及员工、直属主管、财务、出纳四个角色

读取 `references/playbook-swimlane.md`,确定: 图类型=泳道,格式=Draw.io,方向=水平。

构建规范(节选):
```json
{
  "format": "drawio",
  "diagramType": "swimlane",
  "title": "报销审批流程",
  "elements": [
    { "id": "lane-employee", "type": "swimlane", "name": "员工", "geometry": { "x": 0, "y": 0, "width": 1200, "height": 150 } },
    { "id": "lane-manager", "type": "swimlane", "name": "主管", "geometry": { "x": 0, "y": 150, "width": 1200, "height": 150 } },
    { "id": "lane-finance", "type": "swimlane", "name": "财务", "geometry": { "x": 0, "y": 300, "width": 1200, "height": 150 } },
    { "id": "lane-cashier", "type": "swimlane", "name": "出纳", "geometry": { "x": 0, "y": 450, "width": 1200, "height": 150 } },
    { "id": "submit", "type": "node", "name": "提交报销单", "parent": "lane-employee" },
    { "id": "approve-1", "type": "node", "name": "主管审批", "parent": "lane-manager" },
    { "id": "approve-2", "type": "node", "name": "财务复核", "parent": "lane-finance" },
    { "id": "pay", "type": "node", "name": "打款", "parent": "lane-cashier" },
    { "type": "edge", "source": "submit", "target": "approve-1" },
    { "type": "edge", "source": "approve-1", "target": "approve-2" },
    { "type": "edge", "source": "approve-2", "target": "pay" }
  ]
}
```

**输出**: `diagrams/drawio/expense-approval.drawio` 文件路径

**说明**: 水平泳道清晰呈现跨部门交接,每条 lane 的 `geometry` 控制纵向位置,边跨 lane 连接体现流转方向。

### 案例三： 用户登录时序图嵌入文档
**场景**: 文档团队需要在 markdown 文档中嵌入用户登录时序图,要求可直接在代码仓库渲染

读取 `references/playbook-uml.md`,确定: 图类型=时序,格式=Mermaid,方向=自动。

构建规范:
```json
{
  "format": "mermaid",
  "diagramType": "sequence",
  "title": "用户登录时序",
  "elements": [
    { "id": "user", "type": "actor", "name": "用户" },
    { "id": "client", "type": "participant", "name": "前端" },
    { "id": "auth", "type": "participant", "name": "鉴权服务" },
    { "id": "db", "type": "participant", "name": "数据库" },
    { "type": "message", "source": "user", "target": "client", "label": "输入账号密码" },
    { "type": "message", "source": "client", "target": "auth", "label": "POST /login" },
    { "type": "message", "source": "auth", "target": "db", "label": "查询用户" },
    { "type": "message", "source": "db", "target": "auth", "label": "返回用户记录" },
    { "type": "message", "source": "auth", "target": "client", "label": "返回 JWT" }
  ]
}
```

**输出**: `diagrams/mermaid/user-login.mmd` 文件路径,内容可直接复制到 markdown 代码块渲染

**说明**: Mermaid 时序图代码仓库友好,`actor`/`participant`/`message` 类型映射 Mermaid 语法,生成后可直接嵌入 markdown 代码块。

## 错误处理

| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
| --- | --- | --- | --- |
| mcp_tool_missing | `mcp__mcp-diagram-generator__*` 未注册 | MCP 服务器未配置或未启动 | 按"必需 MCP 工具"章节配置并重启 Agent 环境 |
| schema_validation_failed | `Error: schema validation failed` | 必填字段缺失、ID 重复、边 source/target 无效 | 读 `references/json-schema-guide.md`,检查必填字段与 ID 唯一性 |
| directory_error | `EACCES: permission denied` | 输出目录无写权限 | 检查目录权限,运行 `get_config()` 查看路径,必要时 `init_config()` 重置 |
| wrong_extension | `File saved as .md` | `filename` 扩展名与 `format` 不匹配 | Draw.io 用 `.drawio`、Mermaid 用 `.mmd`、Excalidraw 用 `.excalidraw` |
| nested_container_invalid | `Child out of parent bounds` | 子节点坐标超出父容器尺寸 | 子坐标相对直接父级,容器尺寸需容纳子节点加 padding |
| edge_target_not_found | `Edge target "x" not found` | 边的 source/target 指向不存在的 ID | 检查 ID 拼写,确保 source/target 指向已定义的节点或容器 |
| topology_hierarchy_violation | `Invalid environment datacenter zone device nesting` | 网络拓扑层级顺序错误 | 网络拓扑必须遵循环境、数据中心、区域、设备四级嵌套 |
| file_not_found_on_edit | `ENOENT: no such file` | 编辑模式目标文件路径错误 | 确认文件路径与扩展名,读取已有文件前用 Read 工具校验存在性 |

## 常见问题

### Q1: 新建图表时如何选择格式?
A: 按图类型与使用场景选择。网络拓扑与复杂架构优先 Draw.io;流程图、时序、类图、ER 图嵌入代码仓库优先 Mermaid;白板协作与非正式草图优先 Excalidraw。Word 文档优先纵向布局,PPT 横屏展示可接受水平布局。不确定时先读 `references/format-selection-guide.md`。

### Q2: 如何配置 mcp-diagram-generator 服务器?
A: 在 Agent 的 MCP 配置中添加 `mcp-diagram-generator` 条目,`command` 设为 `npx`,`args` 设为 `["-y", "mcp-diagram-generator"]`。本地开发可用 `node /absolute/path/to/mcp-diagram-generator/dist/index.js`。配置后重启 Agent 环境。首次调用会创建 `.diagram-config.json` 与默认输出目录。

### Q3: 如何编辑已有的 .drawio 或 .mmd 文件?
A: 用 Read 工具读取目标文件,解析现有结构为 JSON 规范,在此基础上应用用户请求的变更(增删节点/边、调整坐标、修改样式),重新构建规范并调用 `generate_diagram` 覆盖输出。编辑模式仅需询问目标文件路径与变更内容。

### Q4: JSON 规范中边为什么必须放在顶层?
A: 边表示节点间的关系,逻辑上不属于任何容器。若把边放入 `children`,会导致容器语义混乱与 schema 校验失败。`elements` 数组中,节点/容器与边平级存在,边的 `source` 与 `target` 通过 ID 引用任意层级的节点。

### Q5: 如何处理复杂的网络拓扑?
A: 严格遵循 `references/playbook-network-topology.md` 的四级层级: 环境、数据中心、区域、设备。每级用 `container` 类型,`level` 字段标识层级。子坐标相对直接父级,容器尺寸需容纳所有子节点加 padding。参考 `references/network-topology-examples.md` 的 JSON 模式。

### Q6: 如何自定义输出路径?
A: 调用 `generate_diagram` 时传入 `output_path` 参数指定完整路径(含扩展名),或传入 `filename` 仅指定文件名(写入配置的默认目录)。也可通过 `init_config` 或 `get_config` 修改默认目录配置。服务器会自动创建不存在的目录。

## 已知限制

1. **依赖 MCP 服务器**: 必须配置 `mcp-diagram-generator` MCP 服务器,无 MCP 环境无法使用
2. **三种格式限定**: 仅支持 Draw.io、Mermaid、Excalidraw,不支持 Visio、Lucidchart、PlantUML 等其他格式
3. **JSON 规范需符合 schema**: ID 重复、边 source/target 无效、容器嵌套违规等会触发 schema 校验失败
4. **复杂图需显式几何坐标**: Draw.io 与 Excalidraw 复杂图必须提供 `geometry`,否则布局可能不可读
5. **编辑模式需读取原文件**: 无法直接修改未读取的文件,需先解析现有结构
6. **生成质量取决于 prompt 与规范描述**: 节点命名、层级划分、边连接描述越具体,结果越符合预期
