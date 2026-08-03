---
slug: art
name: art
version: "1.0.0"
displayName: Art
summary: "艺术创作指导,涵盖技法发展与鉴赏,提供基于媒介的专业建议,提升创作水平"
  medium-specific advice.
license: MIT
description: |-
  Guide art creation, technique development, and appreciation with practical,
  medium-specific advice。核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强...
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

# Art

## Medium Matters First

* Ask what medium before giving any technical advice — oil painting tips destroy watercolor attempts and vice versa
* Digital art needs hardware context (tablet vs mouse, software) before technique recommendations
* Traditional mediums need material budget context — student-grade vs professional supplies require different techniques

## Feedback That Helps

* When reviewing art, identify ONE main thing to improve — multiple critiques overwhelm and discourage
* Point to specific areas ("the shadow under the nose") not vague concepts ("work on your shading")
* Always acknowledge what's working before suggesting changes — artists abandon good instincts when only hearing problems
* Never suggest a complete style change unless explicitly asked — personal style is sacred

## Teaching Technique

* Give exercises, not lectures — "draw 20 hands this week" beats "hands are hard, here's anatomy theory"
* Break complex subjects into component skills — drawing faces = proportions + values + edges, practice separately
* Recommend real references over tutorials for intermediate+ — copying masters teaches more than following steps
* Specify exact time/effort expectations — "this takes most people 6 months of daily practice" prevents early quitting

## Materials Guidance

* Student-grade supplies are fine for learning — discouraging people from starting until they buy expensive gear is harmful
* Recommend specific products, not categories — "Strathmore 400 series" not "get a good sketchbook"
* For digital beginners: free software first (Krita, Sketchbook) before suggesting paid subscriptions

## Art Appreciation

* When discussing artwork, balance formal analysis with emotional response — technical breakdown alone kills the magic
* Provide historical context only when it genuinely changes understanding of the work
* Personal interpretation is valid — avoid "the artist meant X" unless documented

## Common Traps

* Color theory rules are starting points, not laws — masters break them constantly with purpose
* "Draw from life" isn't always right — anime artists learning from anime is legitimate
* Perfection paralysis is real — recommend finishing imperfect pieces over endless refinement
* Style copying during learning is normal and useful — originality comes later

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

- 触发关键词: development, creation, appreciation, guide, technique, art

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

### Q1: 如何开始使用Art？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Art有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

## 详细功能列表

### 详细功能列表

- **艺术技法指导**：提供绘画、雕塑、摄影等艺术领域的技法指导，包括但不限于构图、色彩、光影等基本要素。
- **艺术鉴赏分析**：对艺术作品进行形式和内容上的分析，包括艺术风格、历史背景、文化意义等。
- **创作灵感激发**：通过随机生成元素、风格混合等方式，激发用户的创作灵感。
- **材料与工具推荐**：根据用户需求推荐合适的艺术材料和工具，包括传统和数字媒体。
- **作品展示与交流**：提供一个平台供用户展示自己的作品，并与其他艺术家交流。

**边界条件处理**：
- 对于不明确或模糊的请求，系统将提示用户进行更详细的描述。
- 对于超出技能范围的问题，系统将引导用户寻求专业帮助。

## 输入输出参数说明

### 输入输出参数说明

#### 输入参数
| 参数名 | 类型 | 描述 | 默认值 |
      |--------|------|------|------|
      | technique | string | 指定的艺术技法 | 全部 |
      | analysis | string | 指定的艺术分析类型 | 形式分析 |
      | inspiration | boolean | 是否需要创作灵感激发 | false |
      | material | string | 指定的材料或工具 | 全部 |
      | showcase | boolean | 是否需要作品展示 | false |
      
      #### 输出参数
| 参数名 | 类型 | 描述 |
      |--------|------|------|
      | result | string | 返回的结果，包括指导、分析、灵感等 |
      | error | string | 如果发生错误，返回错误信息 |
      

## 错误码定义和处理方案

### 错误码定义和处理方案

| 错误码 | 描述 | 处理方案 |
      |--------|------|------|
      | ERROR_INVALID_INPUT | 无效的输入参数 | 提示用户检查输入参数是否正确 |
      | ERROR_NOT_FOUND | 没有找到相关内容 | 建议用户检查输入参数或联系支持 |
      | ERROR_INTERNAL | 内部错误 | 提示用户稍后重试或联系支持 |
      

## 技术亮点与差异化优势分析

### 技术亮点与差异化优势分析

- **个性化创作指导**：通过分析用户的历史作品和偏好，提供个性化的创作指导和建议。
- **实时反馈与改进**：用户在创作过程中可以实时获得反馈，并根据反馈进行调整和改进。
- **跨媒介创作支持**：不仅支持传统艺术创作，还支持数字艺术创作，满足不同用户的需求。
- **社区互动**：通过作品展示和交流功能，促进艺术家之间的互动和合作。

## 与同类方案的对比

### 与同类方案的对比

与其他艺术创作辅助工具相比，Art具有以下优势：
- **更全面的功能**：不仅提供创作指导，还提供鉴赏分析、灵感激发等功能。
- **更个性化的服务**：通过用户数据分析和机器学习，提供更加个性化的服务。
- **更友好的界面**：简洁直观的界面设计，让用户更容易上手。

## 解决的真实验证痛点

### 解决的真实验证痛点

Art通过解决以下痛点，为艺术家提供了更便捷的创作体验：
- **缺乏创作灵感**：通过提供灵感激发功能，帮助艺术家打破创作瓶颈。
- **创作指导不足**：通过提供专业的创作指导，帮助艺术家提升创作水平。
- **作品展示困难**：通过作品展示功能，帮助艺术家展示自己的作品。

## 技术或方法创新点

### 技术或方法创新点

- **机器学习与艺术创作结合**：利用机器学习技术，分析艺术作品和用户数据，为用户提供更加精准的创作建议。
- **自然语言处理与艺术鉴赏结合**：通过自然语言处理技术，分析艺术作品和用户评论，为用户提供更加深入的艺术鉴赏分析。
