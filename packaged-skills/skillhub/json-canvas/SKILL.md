---
slug: "json-canvas"
name: "json-canvas"
version: "1.0.0"
displayName: "Json Canvas"
summary: "创建编辑JSON Canvas文件,含节点/边/分组/连接"
license: "Proprietary"
description: |-
  Create and edit JSON Canvas files (。canvas) with nodes, edges, groups,
  and connections。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Integrations
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# Json Canvas

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Create and edit JSON Canvas files ( | 支持 | 支持 |
| canvas) with nodes, edges, groups, | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Create and edit JSON Canvas files (
- canvas) with nodes, edges, groups,
  and connections
#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 画布创建 | 节点类型和连接关系 | JSON Canvas格式文件 |
| 画布编辑 | 现有.canvas文件和修改 | 编辑后的画布和节点结构 |
| 节点管理 | 节点ID和属性 | 节点增删改和边连接 |

**不适用于**：非Canvas格式的可视化文件编辑(如SVG/PSD)

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| canvas_path | string | 否 | Canvas文件路径, 新建时留空 |
| node_type | string | 否 | 节点类型, 可选: text/group/file/link, 默认: text |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 工具依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

See [references/EXAMPLES.md](/api/v1/skills/json-canvas/file?path=references%2FEXAMPLES.md&ownerHandle=sadlay) for full canvas examples including mind maps, project boards, research canvases, and flowcharts.

## 常见问题

### Q1: 如何开始使用Json Canvas？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Json Canvas有什么限制？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
