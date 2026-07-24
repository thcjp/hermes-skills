---

slug: "diagram-gen"
name: "diagram-gen"
version: 1.0.1
displayName: "图表生成工具-专业版"
summary: "全格式图表生成引擎，支持Draw.io/Mermaid/Excalidraw，覆盖8种图表类型与批量生成。"
license: "Proprietary"
edition: "pro"
description: |-，可自动提升工作效率
  图表生成工具专业版，面向团队的全格式图表生成与管理平台。核心能力：
  - 三大格式全覆盖：Draw。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - Creative
  - Diagram
  - Enterprise
  - Architecture
  - 工具
  - 效率
  - 自动化
  - 工作流
  - 研究
  - 分析
  - 开发
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"

---

# 图表生成工具-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 图表生成工具-专业版全格式图表生成 | 不支持 | 支持 |
| 图表生成工具-专业版种图表类型与批量生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

## 核心能力

### 格式与类型对比
| 图表类型 | 免费版 | 专业版 | 默认格式 | 默认方向 |
|:-----|:-----|:-----|:-----|:-----|
| 流程图 | 支持 | 支持 | Mermaid | 垂直 |
| 序列图 | 支持 | 支持 | Mermaid | 自动 |
| 网络拓扑 | 不支持 | 支持 | Draw.io | 垂直 |
| 系统架构 | 不支持 | 支持 | Draw.io | 垂直 |
| 泳道图 | 不支持 | 支持 | Draw.io | 水平 |
| UML（类/ER） | 不支持 | 支持 | Mermaid | 自动 |
| 思维导图 | 不支持 | 支持 | Mermaid | 自动 |
| 白板草图 | 不支持 | 支持 | Excalidraw | 自动 |

**输入**: 用户提供格式与类型对比所需的指令和必要参数.
**处理**: 解析格式与类型对比的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回格式与类型对比的处理结果,包含执行状态码、结果数据和执行日志。### 核心能力
```text
格式支持:
  - Draw.io (.drawio)     → 复杂架构与拓扑图
  - Mermaid (.mmd)         → 文档内嵌图表
  - Excalidraw (.excalidraw) → 手绘风格白板
# ...
图表类型:
  - 网络拓扑（环境→数据中心→区域→设备）
  - 系统架构（分层组件视图）
  - 流程图（决策树、流程分支）
  - 泳道图（跨团队协作流转）
  - UML（序列/类/ER图）
  - 思维导图（层级展开）
  - 白板草图（手绘风格概念图）
# ...
高级功能:
  - JSON 规范驱动生成
  - 质量门禁自动校验
  - 批量图表生成
  - 自定义模板与 Playbook
  - 配置管理与路径定制
  - MCP工具集成
```

**输入**: 用户提供核心能力所需的指令和必要参数.
**处理**: 解析核心能力的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 图表类型

针对图表类型,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供图表类型相关的配置参数、输入数据和处理选项.
**输出**: 返回图表类型的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`图表类型`的配置文档进行参数调优
### 流程图

针对流程图,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供流程图相关的配置参数、输入数据和处理选项.
**输出**: 返回流程图的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`流程图`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：企业网络拓扑设计

绘制多层级网络拓扑图，包含环境、数据中心、区域和设备的完整层级.
```json
{
  "format": "drawio",
  "diagramType": "network-topology",
  "title": "生产环境网络拓扑",
  "elements": [
    {
      "id": "env-prod",
      "type": "container",
      "name": "生产环境",
      "level": "environment",
      "geometry": {"x": 0, "y": 0, "width": 1200, "height": 800},
      "children": [
        {
          "id": "dc-primary",
          "type": "container",
          "name": "主数据中心",
          "level": "datacenter",
          "geometry": {"x": 50, "y": 50, "width": 500, "height": 600},
          "children": [
            {
              "id": "zone-dmz",
              "type": "container",
              "name": "DMZ区域",
              "level": "zone",
              "children": [
                {"id": "fw-01", "type": "node", "name": "防火墙-01"},
                {"id": "lb-01", "type": "node", "name": "负载均衡器"}
              ]
            },
            {
              "id": "zone-app",
              "type": "container",
              "name": "应用区域",
              "children": [
                {"id": "web-01", "type": "node", "name": "Web服务器-01"},
                {"id": "web-02", "type": "node", "name": "Web服务器-02"}
              ]
            }
          ]
        }
      ]
    },
    {"type": "edge", "source": "fw-01", "target": "lb-01"},
    {"type": "edge", "source": "lb-01", "target": "web-01"},
    {"type": "edge", "source": "lb-01", "target": "web-02"}
  ]
}
```

```bash
# 通过 MCP工具 生成
# 调用 mcp__mcp-diagram-generator__generate_diagram
# 传入上述 JSON 规范
# ...
# 输出: diagrams/drawio/network-topology.drawio
```

### 场景二：跨团队协作泳道图

绘制跨部门审批流程的泳道图.
```json
{
  "format": "drawio",
  "diagramType": "swimlane",
  "title": "产品上线审批流程",
  "direction": "horizontal",
  "elements": [
    {
      "id": "lane-product",
      "type": "swimlane",
      "name": "产品部",
      "children": [
        {"id": "p1", "type": "node", "name": "提交需求"},
        {"id": "p2", "type": "node", "name": "确认验收"}
      ]
    },
    {
      "id": "lane-dev",
      "type": "swimlane",
      "name": "研发部",
      "children": [
        {"id": "d1", "type": "node", "name": "技术评审"},
        {"id": "d2", "type": "node", "name": "开发实现"},
        {"id": "d3", "type": "node", "name": "提测"}
      ]
    },
    {
      "id": "lane-qa",
      "type": "swimlane",
      "name": "测试部",
      "children": [
        {"id": "q1", "type": "node", "name": "功能测试"},
        {"id": "q2", "type": "node", "name": "回归测试"}
      ]
    },
    {"type": "edge", "source": "p1", "target": "d1"},
    {"type": "edge", "source": "d1", "target": "d2"},
    {"type": "edge", "source": "d2", "target": "d3"},
    {"type": "edge", "source": "d3", "target": "q1"},
    {"type": "edge", "source": "q1", "target": "q2"},
    {"type": "edge", "source": "q2", "target": "p2"}
  ]
}
```

### 场景三：批量图表生成

为项目文档批量生成多张图表.
```python
# 批量图表生成脚本
import json
from pathlib import Path
# ...
class BatchDiagramGenerator:
    """批量图表生成器"""
# ...
    def __init__(self, output_base="diagrams"):
        self.output_base = Path(output_base)
        self.playbooks = {
            "flowchart": "references/playbook-flowchart.md",
            "architecture": "references/playbook-architecture.md",
            "network": "references/playbook-network-topology.md",
            "swimlane": "references/playbook-swimlane.md",
            "uml": "references/playbook-uml.md",
            "excalidraw": "references/playbook-excalidraw.md"
        }
# ...
    def generate_batch(self, task_list):
        """批量生成图表"""
        results = []
        for task in task_list:
            spec = self._build_spec(task)
            result = {
                "task_id": task["id"],
                "filename": f"{task['name']}.{spec['format']}",
                "output_path": str(self.output_base / spec["format"] / f"{task['name']}.{spec['format']}"),
                "spec": spec,
                "status": "ready"
            }
            results.append(result)
        return results
# ...
    def _build_spec(self, task):
        """根据任务构建JSON规范"""
        format_map = {
            "flowchart": "mermaid",
            "sequence": "mermaid",
            "architecture": "drawio",
            "network": "drawio",
            "swimlane": "drawio",
            "class": "mermaid",
            "er": "mermaid",
            "whiteboard": "excalidraw"
        }
        return {
            "format": format_map.get(task["type"], "mermaid"),
            "diagramType": task["type"],
            "title": task.get("title", task["name"]),
            "elements": task.get("elements", []),
            "direction": task.get("direction", "vertical")
        }
# ...
# 批量任务定义
tasks = [
    {"id": "D001", "name": "user-register-flow", "type": "flowchart",
     "title": "用户注册流程"},
    {"id": "D002", "name": "system-architecture", "type": "architecture",
     "title": "系统架构图"},
    {"id": "D003", "name": "network-topology", "type": "network",
     "title": "网络拓扑图"},
    {"id": "D004", "name": "approval-process", "type": "swimlane",
     "title": "审批流程泳道图"},
    {"id": "D005", "name": "data-model", "type": "er",
     "title": "数据模型ER图"},
    {"id": "D006", "name": "concept-sketch", "type": "whiteboard",
     "title": "概念白板草图"}
]
# ...
generator = BatchDiagramGenerator()
results = generator.generate_batch(tasks)
for r in results:
    print(f"[{r['task_id']}] {r['filename']} -> {r['output_path']}")
```

## 使用流程

### 优秀步：配置 MCP工具

```json
{
  "mcpServers": {
    "协议-diagram-generator": {
      "command": "npx",
      "args": ["-y", "协议-diagram-generator"]
    }
  }
}
```

### 第二步：初始化配置

```text
# 调用 MCP工具 初始化默认配置
mcp__mcp-diagram-generator__init_config
# ...
# 查看当前配置
mcp__mcp-diagram-generator__get_config
```

### 第三步：生成优秀张图表

```json
{
  "diagram_spec": {
    "format": "drawio",
    "diagramType": "architecture",
    "title": "微服务架构",
    "elements": [
      {"id": "gateway", "type": "node", "name": "API网关"},
      {"id": "user-svc", "type": "node", "name": "用户服务"},
      {"id": "order-svc", "type": "node", "name": "订单服务"},
      {"type": "edge", "source": "gateway", "target": "user-svc"},
      {"type": "edge", "source": "gateway", "target": "order-svc"}
    ]
  },
  "filename": "microservice-arch.drawio"
}
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | diagram-gen处理的内容输入 |,  |
| content | string | 否 | diagram-gen处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
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
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+（MCP工具运行需要）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js 16+ | 运行时 | 必需 | nodejs.org 官方下载 |
| 协议-diagram-generator | MCP工具 | 必需 | `npx -y 协议-diagram-generator` |
| Draw.io Desktop | 工具 | 可选 | drawio.com 下载（查看 .drawio） |
| Excalidraw | 工具 | 可选 | excalidraw.com（查看 .excalidraw） |

### API Key 配置
- 本Skill采用纯Markdown指令驱动，无需额外API Key
- MCP工具通过本地 npx 运行，无需远程认证

### 可用性分类
- **分类**: MD+EXEC+协议（Markdown指令 + 命令行 + MCP工具集成）
- **说明**: 企业级AI Skill，支持全格式图表生成、批量操作与质量门禁
- **适用规模**: 团队与企业级，支持多格式多类型批量生成
- **兼容性**: 与免费版完全兼容，Mermaid 图表可无缝编辑扩展

## 案例展示

### 自定义输出路径

```json
{
  "paths": {
    "drawio": "output/diagrams/drawio",
    "mermaid": "output/diagrams/mermaid",
    "excalidraw": "output/diagrams/excalidraw"
  }
}
```

### 质量门禁配置

```yaml
# quality-gate.yml
quality_checks:
  - format_matches_intake: true
  - diagram_type_explicit: true
  - layout_direction_reflected: true
  - complex_geometry_provided: true    # Draw.io/Excalidraw 复杂图
  - container_hierarchy_valid: true
  - edges_top_level: true              # 边必须在顶层
  - colors_hex_format: true            # 颜色用 #RRGGBB
  - unique_ids: true                   # ID 唯一
# ...
auto_fix:
  suggest_only: true
  max_suggestions: 5
```

### Playbook 选择矩阵

```text
用户意图 → Playbook 映射:
  网络拓扑/数据中心/区域/路由器  → playbook-network-topology
  系统架构/应用架构/分层组件    → playbook-architecture
  流程图/过程/决策树            → playbook-flowchart
  泳道/跨团队/部门审批          → playbook-swimlane
  序列/类/ER/UML               → playbook-uml
  白板/手绘/非正式              → playbook-excalidraw
```

## 常见问题

### Q: MCP工具不可用怎么办？

A: 检查 MCP工具配置是否正确，重启 Agent 环境后重试。首次使用会自动创建 `.diagram-config.json` 和默认输出目录.
### Q: JSON 规范校验失败怎么办？

A: 检查以下几点：elements 是否为数组、ID 是否唯一、边的 source/target 是否指向存在的节点、边是否在顶层而非 children 内.
### Q: 如何从免费版升级？

A: 免费版的 Mermaid 图表可直接在专业版中打开编辑。专业版新增 Draw.io 和 Excalidraw 格式，无需转换已有文件.
### Q: 批量生成支持多少张图表？

A: 专业版支持单批 100+ 图表生成。建议按类型分组批量处理，便于质量管控.
### Q: 嵌套容器的坐标系如何处理？

A: 子元素坐标相对于直接父容器。容器尺寸必须容纳所有子元素边界加内边距.
### Q: 可以自定义图表样式吗？

A: 可以。Draw.io 支持 `style` 对象自定义填充色、边框、圆角等。颜色使用 `#RRGGBB` 格式，无填充用 `fillColor: "none"`.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

