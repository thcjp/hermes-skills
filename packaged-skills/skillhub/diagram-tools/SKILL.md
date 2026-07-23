---
slug: "diagram-tools"
name: "diagram-tools"
version: "1.0.2"
displayName: "Diagram Tools"
summary: "图表工具技能 - 支持 Mermaid、Graphviz、流程图、思维导图等多种图表生成"
license: "Proprietary"
description: |-
  图表工具技能 - 支持 Mermaid、Graphviz、流程图、思维导图等多种图表生成\n\n核心能力:\n- 商业工具领域的专业化AI辅助工具\n\
  - 基于高人气开源Skill深度优化升级\n- 移除风险代码,增强安全性和稳定性\n\n适用场景:\n- 日程管理、效率提升、团队协作\n- 独立开发者与一人公司效率提升\n\
tags:
  - Productivity
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Diagram Tools

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Diagram Tools维导图等多种图表生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

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

**输入**: 用户提供Mermaid 图表所需的指令和必要参数.
**处理**: 解析Mermaid 图表的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 2. Graphviz 图表
使用 DOT 语言生成：

* 有向图/无向图
* 层级图
* 树形图

**输入**: 用户提供Graphviz 图表所需的指令和必要参数.
**处理**: 解析Graphviz 图表的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 3. 数据图表
* 柱状图
* 折线图
* 饼图

**输入**: 用户提供数据图表所需的指令和必要参数.
**处理**: 解析数据图表的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回数据图表的处理结果,包含执行状态码、结果数据和执行日志.
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
|:-----|:-----|:-----|:-----|
| content | string | 否 | diagram-tools处理的内容输入 |,  |
| content | string | 否 | diagram-tools处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "tools 相关配置参数",
    result: "tools 相关配置参数",
    result: "tools 相关配置参数",
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
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
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

### 流程图

Rendering diagram...

### 思维导图

### 时序图

## 常见问题

### Q1: 如何开始使用Diagram Tools？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

