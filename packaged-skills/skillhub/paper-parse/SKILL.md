---
slug: "paper-parse"
name: "paper-parse"
version: 1.0.1
displayName: "Paper Parse"
summary: "对用户提供的任何学术论文（PDF附件或URL）进行双模式深度研读。当用户请求分析、研读、解读或总结一篇学术论文时，使用此技能。一次性生成两份报告：Part"
license: "Proprietary"
description: |-
  对用户提供的任何学术论文（PDF附件或URL）进行双模式深度研读。当用户请求分析、研读、解读或总结一篇学术论文时，使用此技能。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - Knowledge
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
category: "Automation"
---
# Paper Parse

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Paper Parse当用户请求分析 | 不支持 | 支持 |
| Paper Parse一次性生成 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |

## 核心能力

- 对用户提供的任何学术论文（PDF附件或URL）进行双模式深度研读
- 当用户请求分析、研读、解读或总结一篇学术论文时，使用此技能
- 一次性生成两份报告：Part
  A 面向研究者的深度专业解析，Part
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| PDF处理 | PDF文件与操作类型 | 提取文本或生成文档 |
| 报告生成 | 数据源与报告模板 | 报告文件与摘要统计 |
| 内容生成 | 提示词与风格参数 | 生成内容与质量评分 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

论文研读分四步执行：

### Step 1: 通读论文全文

使用 `pdftotext` 命令或 `file` 工具的 `read` 动作提取论文全文。对于URL来源的论文，先尝试下载PDF再提取。必须覆盖从摘要到参考文献的所有内容。对于包含重要图表的论文，使用 `file` 工具的 `view` 动作查看关键图表页面，并将图表信息保存到文本文件中.
### Step 2: 综合分析

创建临时分析文件 `temp_analysis.md`，提取并组织以下要素：

* 研究问题、假设、方法论、数据来源
* 核心发现与关键数据
* 理论贡献与实践意义
* 论文的根本矛盾点、切入视角、方法创新

**此步骤不可跳过**，它是保证最终报告质量的思考过程.
### Step 3: 撰写双模报告

创建最终交付文件，文件名格式为 `[论文简称]_研读报告.md`.
**撰写 Part A 前**，先读取模板：`/home/ubuntu/skills/paper-parse/references/part-a-template.md`

**撰写 Part B 前**，先读取模板：`/home/ubuntu/skills/paper-parse/references/part-b-template.md`

### Step 4: 交付成果

使用 `message` 工具交付最终报告文件。消息文本中简要概括论文的核心创新、关键发现和理论价值，引导用户查看附件.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | paper-parse处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "parse_result": "parse_result_value",
      "parse_metadata": "parse_metadata_value",
      "parse_status": "parse_status_value"
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

中间产物模板参考: `assets/paper-parse_template`

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

### 示例1：基础用法

```
论文研读分四步执行：
# ...
### Step 1: 通读论文全文(补充)
# ...
使用 `pdftotext` 命令或 `file` 工具的 `read` 动作提取论文全文。对于URL来源的论文，先尝试下载PDF再提取。必须覆盖从摘要到参考文献的所有内容。对于包含重要图表的论文，使用 `file` 工具的 `view` 动作查看关键图表页面，并将图表信息保存到文本文件中.
# ...
### Step 2: 综合分析(补充)
# ...
创建临时分析文件 `temp_analysis.md`，提取并组织以下要素：
# ...
* 研究问题、假设、方法论、数据来源
* 核心发现与关键数据
* 理论贡献与实践意义
* 论文的根本矛盾点、切入视角、方法创新
# ...
**此步骤不可跳过**，它是保证最终报告质量的思考过程.
# ...
### Step 3: 撰写双模报告(补充)
# ...
创建最终交付文件，文件名格式为 `[论文简称]_研读报告.md`.
# ...
**撰写 Part A 前**，先读取模板：`/home/ubuntu/skills/paper-parse/references/part-a-template.md`
# ...
**撰写 Part B 前**，先读取模板：`/h
```

## 常见问题

### Q1: 如何开始使用Paper Parse？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

