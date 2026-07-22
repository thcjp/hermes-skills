---
slug: "diagram-tools"
name: "diagram-tools"
version: "1.0.2"
displayName: "Diagram Tools"
summary: "图表工具技能 - 支持 Mermaid、Graphviz、流程图、思维导图等多种图表生成"
license: "MIT-0"
description: |-
  图表工具技能 - 支持 Mermaid、Graphviz、流程图、思维导图等多种图表生成\n\n核心能力:\n- 商业工具领域的专业化AI辅助工具\n\
  - 基于高人气开源Skill深度优化升级\n- 移除风险代码,增强安全性和稳定性\n\n适用场景:\n- 日程管理、效率提升、团队协作\n- 独立开发者与一人公司效率提升\n\
tags: "'[''Productivity'']'"
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
---
# Diagram Tools

## 核心能力

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

**输入**: 用户提供Mermaid 图表所需的指令和必要参数。
**处理**: 按照skill规范执行Mermaid 图表操作,遵循单一意图原则。

### 2. Graphviz 图表
使用 DOT 语言生成：

* 有向图/无向图
* 层级图
* 树形图

**输入**: 用户提供Graphviz 图表所需的指令和必要参数。
**处理**: 按照skill规范执行Graphviz 图表操作,遵循单一意图原则。

### 3. 数据图表
* 柱状图
* 折线图
* 饼图

**输入**: 用户提供数据图表所需的指令和必要参数。
**处理**: 按照skill规范执行数据图表操作,遵循单一意图原则。
**输出**: 返回数据图表的执行结果,包含操作状态和输出数据。

#
## 适用场景

* 📊 流程图设计
* 🧠 思维导图
* 📈 数据可视化
* 🔄 架构图
* 📑 UML 图
* 📅 时间线图

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
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

### 流程图

Rendering diagram...

### 思维导图

Rendering diagram...

### 时序图

Rendering diagram...

## 常见问题

### Q1: 如何开始使用Diagram Tools？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Diagram Tools有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

