---
slug: thesis-helper
name: thesis-helper
version: "2.0.0"
displayName: Thesis Helper
summary: 论文写作助手。论文大纲生成、文献综述框架、摘要生成、引用格式转换、格式规范检查、答辩准备。Thesis helper with outline generation,
  literature re...
license: MIT-0
description: |-
  论文写作助手。论文大纲生成、文献综述框架、摘要生成、引用格式转换、格式规范检查、答辩准备。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Thesis Helper

论文写作助手。论文大纲生成、文献综述框架、摘要生成、引用格式转换、格式规范检查、答辩准备。Thesis helper with outline generation, literature review, abstract writing, citation formatting, style guide, defense preparation.

## 速查表

See commands above.

## 命令速查

```text
  outline         outline
  literature      literature
  abstract        abstract
  cite            cite
  format          format
  defense         defense
```

> 💡 小技巧：先用 `help` 查看所有命令，再选择最适合的

## 专业建议

* 论文大纲**：输入研究主题，生成多级大纲结构
* 文献综述**：按时间线或主题分类组织文献框架
* 摘要生成**：
* 中文摘要：200-300字
* 英文摘要：150-250 words

---

## *thesis-helper by BytesAgain*

💬 Feedback & Feature Requests: <https://bytesagain.com/feedback>
Powered by BytesAgain | bytesagain.com

* Run `thesis-helper help` for commands
* No API keys needed

## Commands

Run `thesis-helper help` to see all available commands.

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

- 论文大纲生成、文献综述框架、摘要生成、引用格式转换、格式规范检查、答辩准备
- Thesis helper with outline
  generation, literature re
- 触发关键词: outline, 引用格式转换, 文献综述框架, thesis, 摘要生成, 论文写作助手, generation, 论文大纲生成

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

### Q1: 如何开始使用Thesis Helper？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Thesis Helper有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **主题明确性**：Thesis Helper要求用户输入明确的研究主题，模糊或不具体的研究领域可能导致无法生成有效的大纲或摘要。
- **文献数据量**：对于大量文献的综述，系统可能需要较长时间来处理和生成框架，且可能无法完全覆盖所有文献。
- **格式规范**：用户输入的文本格式必须符合系统要求，如段落分隔、引用格式等，否则可能影响输出结果。

### 性能边界
- **处理速度**：在处理大量数据或复杂任务时，如文献综述和格式转换，系统可能需要较长时间来完成操作。
- **资源消耗**：使用Thesis Helper可能对Agent的资源消耗有一定影响，特别是在处理高负载任务时。

### 兼容性约束
- **LLM支持**：Thesis Helper依赖于LLM API，因此必须在支持LLM的Agent平台上运行。
- **操作系统兼容**：虽然理论上支持Windows、macOS和Linux，但实际使用中可能存在兼容性问题，需要根据具体操作系统调整配置。

### 其他限制
- **人工辅助**：对于一些需要人工判断的复杂场景，如特定领域的专业知识判断，系统可能无法完全依赖自动生成。
- **语言限制**：目前系统主要支持中英文，对于其他语言的论文写作支持有限。

