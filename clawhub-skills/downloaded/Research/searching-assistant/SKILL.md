---
slug: searching-assistant
name: searching-assistant
version: "0.1.0"
displayName: Searching Assistant
summary: "搜索组组长,将搜索任务分解为独立互补子任务,协调多Agent并行搜索"
  and complemen...
license: MIT
description: |-
  You are the leader of searching group (搜索组组长)。Break down the task into
  independent and complemen。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Searching Assistant

## Overview

This skill provides specialized capabilities for searching assistant.

## Instructions

You are the leader of searching group (搜索组组长). Break down the task into independent and complementary sub-tasks. Then describe each sub-task with natural language and assign to the most suitable agent. Always use General_Search_Agent. You are strongly encouraged to additionally call other agents with different tasks specifically according to the types of user query. DO NOT call Academic_Search when the task involves date-specific requirements. You have only one chance to parallel assign tasks to agents. The upper limit of the number of sub-tasks is 8, as less as possible. Current Date: $DATE$.

## Usage Notes

* This skill is based on the Searching_Assistant agent configuration
* Template variables (if any) like $DATE$, $SESSION_GROUP_ID$ may require runtime substitution
* Follow the instructions and guidelines provided in the content above

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

This skill provides specialized capabilities for searching assistant.

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

### Q1: 如何开始使用Searching Assistant？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Searching Assistant有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 功能详解与边界条件

### 核心功能详解

1. **任务分解**：
   - **输入参数**：用户请求的搜索任务描述。
   - **处理逻辑**：将搜索任务分解为独立的子任务，如关键词提取、SEO分析、内容调研等。
   - **输出结果**：生成每个子任务的描述和分配给合适Agent的指令。

2. **任务分配**：
   - **输入参数**：分解后的子任务描述。
   - **处理逻辑**：根据子任务类型，选择合适的Agent进行执行，如General_Search_Agent、Keyword_Analyzer等。
   - **输出结果**：生成每个子任务的执行结果。

3. **并行搜索**：
   - **输入参数**：已分配的子任务列表。
   - **处理逻辑**：启动多个Agent并行执行子任务。
   - **输出结果**：收集所有子任务的执行结果。

4. **结果整合**：
   - **输入参数**：并行搜索的执行结果。
   - **处理逻辑**：将所有子任务的执行结果进行整合，生成最终的搜索结果。
   - **输出结果**：提供完整的搜索结果，包括关键词、SEO分析、内容调研等。

### 边界条件

1. **输入大小限制**：单个任务描述的字符数限制为500字符。
2. **并发限制**：最多支持8个并发子任务。
3. **字符编码要求**：输入内容需符合UTF-8编码。
4. **任务类型限制**：不适用于需要日期特定要求的任务，如使用Academic_Search Agent。
5. **Agent能力限制**：部分Agent可能无法处理特定类型的任务，如图片识别、语音识别等。
6. **网络限制**：搜索过程中可能受到网络延迟或中断的影响。
7. **性能限制**：搜索结果的质量和准确性取决于底层模型的能力。
8. **时间限制**：单个搜索任务的处理时间限制为30分钟。

### 错误处理

1. **配置错误**：检查依赖说明中的配置要求，确保环境满足需求。
2. **运行时错误**：确认运行环境符合依赖说明，检查操作系统、Agent平台等。
3. **网络错误**：检查网络连接，重试操作或参考国内替代方案。
4. **任务分解失败**：检查任务描述是否清晰，调整描述后重试。
5. **任务分配失败**：检查Agent是否可用，尝试更换其他Agent。
6. **结果整合失败**：检查子任务执行结果是否完整，确保所有子任务已完成。
7. **性能问题**：优化任务描述，尝试调整搜索参数或更换底层模型。
8. **模型能力不足**：尝试使用其他模型或工具，或寻求人工辅助。

### 性能指标

1. **搜索准确率**：搜索结果与用户请求的相关度。
2. **搜索召回率**：搜索结果中包含用户请求关键词的比例。
3. **任务处理时间**：从任务分解到结果整合的总时间。
4. **系统响应时间**：从用户请求到系统响应的总时间。
5. **并发处理能力**：系统同时处理多个任务的能力。
6. **资源消耗**：搜索过程中消耗的CPU、内存等资源。


## 差异化优势

### 与同类方案对比

1. **手动操作**：手动操作搜索任务需要大量时间和精力，且容易出错。相比之下，Searching Assistant能够自动将搜索任务分解为子任务，并分配给合适的Agent并行执行，大大提高了搜索效率，减少了人为错误。

2. **通用搜索引擎**：通用搜索引擎虽然方便，但无法针对特定搜索需求进行优化。Searching Assistant则可以根据用户的具体需求，将任务分解为多个子任务，并调用不同的Agent进行针对性搜索，从而提高搜索结果的准确性和相关性。

3. **其他自动化工具**：一些自动化工具可能能够执行部分搜索任务，但缺乏灵活性和定制性。Searching Assistant不仅能够自动执行搜索任务，还支持自定义任务分解和Agent分配，满足不同场景下的搜索需求。

### 独特功能

1. **任务分解与分配**：Searching Assistant能够将复杂的搜索任务分解为多个子任务，并根据任务类型分配给合适的Agent执行，提高了搜索效率和准确性。

2. **并行搜索**：通过并行搜索，Searching Assistant能够在短时间内获取大量搜索结果，加快了搜索速度。

3. **自定义Agent配置**：用户可以根据自己的需求，自定义Agent的配置，实现更精准的搜索结果。

4. **结果整合与分析**：Searching Assistant能够将多个子任务的执行结果进行整合，并提供详细的分析报告，帮助用户更好地理解搜索结果。

5. **实时更新**：Searching Assistant支持实时更新搜索结果，确保用户获取到最新的信息。

### 效率提升

使用Searching Assistant，用户可以将原本需要数小时甚至数天的搜索任务，缩短到几分钟内完成。例如，对于一个包含多个关键词的SEO优化任务，Searching Assistant可以在短时间内完成关键词分析、内容调研、排名提升等子任务，大大提高了工作效率。

### 应用场景创新

1. **企业市场调研**：企业可以利用Searching Assistant快速获取市场信息，了解竞争对手动态，为产品研发和营销策略提供数据支持。

2. **学术研究**：研究人员可以利用Searching Assistant进行文献检索，提高研究效率。

3. **内容创作**：内容创作者可以利用Searching Assistant进行选题、关键词分析和内容调研，提高创作效率。

