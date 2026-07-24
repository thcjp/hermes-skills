---
slug: "figma"
name: "figma"
version: 2.1.1
displayName: "Figma"
summary: "读Figma数据/导出资产/写回请求,设计交付闭环"MIT。This skill does what it advertises: reads Figma data, exp"
description: |-
  This skill does what it advertises: reads Figma data, exports assets,
  and writes user-requested r。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - Knowledge
  - 工具
  - 效率
  - api
  - figma
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
license: "MIT"
category: "Automation"
---
# Figma

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 核心能力

### API Rate Limiting
Built-in rate limiting and retry logic to handle Figma's API constraints gracefully.

**输入**: 用户提供API Rate Limiting所需的指令和必要参数.
**处理**: 解析API Rate Limiting的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回API Rate Limiting的处理结果,包含执行状态码、结果数据和执行日志。### Error Handling
Comprehensive error handling with detailed logging and recovery suggestions.

**输入**: 用户提供Error Handling所需的指令和必要参数.
**处理**: 解析Error Handling的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Error Handling的处理结果,包含执行状态码、结果数据和执行日志。### Multi-Format Support

Export assets in PNG, SVG, PDF, and WEBP with platform-specific sizing.- 验证返回数据的完整性和格式正确性
- 参考`API Rate Limiting`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 数据处理 | 数据源与处理规则 | 清洗结果与统计摘要 |
| 读Figma数据 | 目标数据与配置参数 | 处理结果与执行状态 |
| 导出资产 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Authentication Setup

```bash
export FIGMA_ACCESS_TOKEN="[REDACTED]"
# ...
echo "FIGMA_ACCESS_TOKEN=your-token" >> .env
```

### Basic Operations

```bash
python （请参考skill目录中的脚本文件） get-file "your-file-key"
# ...
python （请参考skill目录中的脚本文件） export-frames "file-key" --formats png,svg
# ...
python （请参考skill目录中的脚本文件） audit-file "file-key" --generate-html
# ...
python （请参考skill目录中的脚本文件） "file-key" --level AA --format html
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | figma处理的内容输入 |,  |
| content | string | 否 | figma处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "figma 相关配置参数",
    result: "figma 相关配置参数",
    result: "figma 相关配置参数",
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

### With Development Workflows

```bash
python （请参考skill目录中的脚本文件） export-tokens "file-key" --format css
# ...
python （请参考skill目录中的脚本文件） document-components "file-key" --output docs/
```

### With Brand Management

```bash
python （请参考skill目录中的脚本文件） audit-file "file-key" --brand-colors "#FF0000,#00FF00,#0000FF"
# ...
python （请参考skill目录中的脚本文件） extract-colors "file-key" --output brand-colors.json
```

### With Client Deliverables

```bash
python （请参考skill目录中的脚本文件） client-package "file-key" --template presentation
# ...
python （请参考skill目录中的脚本文件） dev-handoff "file-key" --include-specs
```

## 常见问题

### Q1: 如何开始使用Figma？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

This skill has the following known limitations due to Figma API constraints. Please review carefully before use:

### Read-Only Operations

This skill provides **read-only access** to Figma files through the REST API. It can:

* ✅ Extract data, components, and styles
* ✅ Export assets in multiple formats
* ✅ Analyze and audit design files
* ✅ Generate comprehensive reports

### What It Cannot Do

* ❌ **Modify existing files** (colors, text, components)
* ❌ **Create new designs** or components
* ❌ **Batch update** multiple files
* ❌ **Real-time collaboration** features

For file modifications, you would need to develop a **Figma plugin** using the Plugin API.
