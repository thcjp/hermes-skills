---
slug: design
name: design
version: "1.0.0"
displayName: Design
summary: "自动学习视觉偏好,适配UI/图形/视频等创意工作"
  creative work.
license: MIT
description: |-
  Auto-learns your visual preferences。Adapts to UI, graphics, video,
  and any creative work。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Design

## Auto-Adaptive Design Preferences

This skill auto-evolves. Edit sections below as you learn user's visual taste.

**Rules:**

* Detect patterns from choices, feedback, and reactions
* Support all design types (UI, graphics, video, print, any visual)
* Confirm after 2+ consistent preferences
* Keep entries ultra-compact
* Check `dimensions.md` for categories, `criteria.md` for format

---

### Aesthetic

### By Medium

### Brands

### Never

---

*Empty sections = no preference yet. Observe and fill.*

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

- Auto-learns your visual preferences
- Adapts to UI, graphics, video,
  and any creative work
- 触发关键词: design, learns, visual, preferences

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

### Q1: 如何开始使用Design？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Design有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制

* **数据量限制**：Design技能在处理大量数据时可能会遇到性能瓶颈，建议每次处理的数据量不超过1000条。
* **数据格式限制**：输入数据需符合Markdown格式，否则技能可能无法正确解析。
* **关键词限制**：输入内容中包含的关键词数量不宜过多，过多可能导致技能无法准确识别用户意图。

### 性能边界

* **响应时间**：Design技能的响应时间取决于输入数据的复杂度和当前系统负载，通常在几秒到几十秒之间。
* **并发处理**：Design技能支持并发处理，但受限于系统资源，并发数量不宜过多。

### 兼容性约束

* **操作系统**：Design技能支持Windows、macOS和Linux操作系统。
* **Agent平台**：Design技能支持SKILL.md的任意AI Agent，如Claude Code、Cursor、Codex、Gemini CLI等。
* **LLM支持**：Design技能需要LLM支持，无LLM环境无法使用。

### 其他限制

* **复杂场景**：Design技能在处理复杂场景时可能需要人工辅助判断，如涉及敏感信息或需要深度理解用户意图的场景。
* **模型能力**：Design技能的性能取决于底层模型能力，随着模型能力的提升，技能性能有望得到改善。

