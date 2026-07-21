---
slug: diagram-tools
name: diagram-tools
version: "1.0.2"
displayName: Diagram Tools
summary: 图表工具技能 - 支持 Mermaid、Graphviz、流程图、思维导图等多种图表生成
license: MIT-0
description: |-
  图表工具技能 - 支持 Mermaid、Graphviz、流程图、思维导图等多种图表生成\n\n核心能力:\n- 商业工具领域的专业化AI辅助工具\n\
  - 基于高人气开源Skill深度优化升级\n- 移除风险代码,增强安全性和稳定性\n\n适用场景:\n- 日程管理、效率提升、团队协作\n- 独立开发者与一人公司效率提升\n\
  - 自动化工作流与智能决策辅助\n\n差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags: '[''Productivity'']'
tools:
  - read
  - exec
---
# Diagram Tools å¾è¡¨å·¥å·æè½

强大的图表生成工具集，支持多种图表格式和渲染引擎。

## 适用场景

* 📊 流程图设计
* 🧠 思维导图
* 📈 数据可视化
* 🔄 架构图
* 📑 UML 图
* 📅 时间线图

## 不适用场景

以下场景Diagram Tools不适合处理：

- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析


## 触发条件

需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于非本工具能力范围的需求。


## 核心功能

### 1. Mermaid 图表

使用 Mermaid 语法生成各类图表：

* Flowchart 流程图
* Sequence 时序图
* Class 类图
* State 状态图
* ER 数据库图
* Gantt 甘特图
* Pie 饼图
* Mindmap 思维导图
* Timeline 时间线

### 2. Graphviz 图表

使用 DOT 语言生成：

* 有向图/无向图
* 层级图
* 树形图

### 3. 数据图表

* 柱状图
* 折线图
* 饼图

## 示例

### 流程图

Rendering diagram...

### 思维导图

Rendering diagram...

### 时序图

Rendering diagram...

## Graphviz 示例

```python
from graphviz import Digraph
dot = Digraph()
dot.node('A', '节点A')
dot.node('B', '节点B')
dot.edge('A', 'B')
dot.render('output', format='png')
```

## 支持的图表类型

| 类型 | Mermaid 语法 |
| --- | --- |
| 流程图 | `graph TD` / `graph LR` |
| 时序图 | `sequenceDiagram` |
| 类图 | `classDiagram` |
| 状态图 | `stateDiagram-v2` |
| ER图 | `erDiagram` |
| 甘特图 | `gantt` |
| 饼图 | `pie` |
| 思维导图 | `mindmap` |
| 时间线 | `timeline` |
| 四象限 | `quadrantChart` |

## 主题配置

自定义颜色主题：

```json
{
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#1976d2",
    "lineColor": "#666666",
    "secondaryColor": "#4caf50"
  }
}
```

## 使用技巧

* 使用 `graph LR` 表示从左到右
* 使用 `graph TD` 表示从上到下
* 保持节点标签简短
* 使用子图分组相关组件
* 高清输出使用 `-s 2` 或 `-s 3`

## 相关技能

* `mermaid` - Mermaid 图表
* `markdown-tools` - Markdown 处理
* `meeting-notes` - Word 文档

## 更新日志

* v1.0.0 - 初始版本，整合 Mermaid 和 Graphviz

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Diagram Tools？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Diagram Tools有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
