---
slug: ollama-integration
name: ollama-integration
version: "1.0.0"
displayName: Ollama Integration
summary: "集成运行本地Ollama AI模型,自定义提示与自动模式(社区下载版)"
  and automatic mode...
license: MIT
description: |-
  Integrate and run local Ollama AI models with custom prompts for AI
  assistance and automatic mode。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Ollama Integration

---\nname: ollama-integration\ndescription: Ollama local model integration for AI assistance\ntype: skill\nversion: 1.0.0\nauthor: Skill平台\nlicense: MIT\n---\n\n# Ollama Integration\n\nThis skill provides integration with local Ollama models for AI assistance.\n\n## Features\n\n- List available Ollama models\n- Run models with custom prompts\n- Automatic model discovery\n- Local AI processing\n\n## Usage\n\n

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

## 核心能力

- Integrate and run local Ollama AI models with custom prompts for AI
  assistance and automatic mode
- 触发关键词: local, ollama, models, integration, integrate

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Ollama Integration？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Ollama Integration有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 性能取决于底层模型能力
- 本地运行，不支持多设备同步

---
## 边界条件与限制 (Boundary Conditions)

### 输入限制
- **模型兼容性**: 本技能仅支持与Ollama AI模型兼容的本地模型。若尝试使用不兼容的模型，技能可能无法正常运行。
- **数据格式**: 输入数据应遵循Ollama模型要求的格式。不正确或不符合格式的数据可能导致模型无法处理或错误输出。
- **字符限制**: 对于自定义提示，存在字符数限制，超过限制的提示可能导致技能无法正确解析或执行。

### 性能边界
- **并发处理**: 单个Agent实例在同一时间只能处理一个Ollama模型的请求。若需要同时处理多个请求，需启动多个Agent实例。
- **计算资源**: Ollama模型的运行依赖于底层计算资源。在资源受限的环境下，模型处理速度可能会受到影响。

### 兼容性约束
- **操作系统**: 目前，Ollama Integration仅在Windows、macOS和Linux操作系统上提供支持。
- **Agent平台**: 仅支持与SKILL.md兼容的AI Agent，如Claude Code、Cursor、Codex、Gemini CLI等。
- **LLM API**: 必须由Agent内置的LLM提供LLM API，否则技能无法正常工作。

### 其他限制
- **API Key**: 虽然本Skill基于Markdown指令，无需额外API Key，但在某些情况下，外部API的访问可能需要API Key。
- **多设备同步**: 本地运行的模型不支持多设备同步，即同一模型在同一时间只能在一个设备上运行。


## 示例 (Examples)

### 示例2：模型兼容性检查

```
输入: 用户请求使用一个不兼容的模型
处理: 报告错误信息，说明模型不兼容
输出: 错误信息提示
```

### 示例3：数据格式错误

```
输入: 用户提供不符合格式的数据
处理: 报告错误信息，说明数据格式错误
输出: 错误信息提示
```

### 示例4：资源受限

```
输入: 用户请求处理大量数据
处理: 报告资源受限，请求减少数据量或等待资源释放
输出: 资源受限提示
```


## 注意事项 (Important Notes)

- 在使用Ollama Integration时，请确保遵循所有模型的使用指南和最佳实践。
- 在处理敏感或机密数据时，请确保数据的安全性，并遵守相关法律法规。
- 若遇到未在文档中描述的问题，请通过官方渠道寻求技术支持。

