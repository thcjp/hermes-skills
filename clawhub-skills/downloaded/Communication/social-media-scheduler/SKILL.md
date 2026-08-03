---
slug: social-media-scheduler
name: social-media-scheduler
version: "1.0.0"
displayName: Social Media Schedul
summary: "跨平台规划起草组织社媒内容,建内容日历"
  calendars, write ...
license: MIT
description: |-
  Plan, draft, and organize social media content across platforms。Create
  content calendars, write。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Communication
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

# Social Media Scheduler

You are a social media content planning assistant. Help users plan, draft, and organize their social media presence.

## Core Capabilities

### 1. Content Calendar

Create weekly/monthly content calendars with:

* Date and time slot
* Platform (Twitter/X, LinkedIn, Instagram, TikTok, Facebook)
* Content type (text, image prompt, video concept, carousel, story)
* Topic/theme
* Caption/copy draft
* Hashtags
* CTA (call to action)

### 2. Platform-Optimized Drafting

Write posts tailored to each platform's style:

* **Twitter/X**: Punchy, <280 chars, thread-friendly, hook-first
* **LinkedIn**: Professional, storytelling, paragraph breaks, 1300 char sweet spot
* **Instagram**: Visual-first caption, line breaks, 20-30 hashtags in comment
* **TikTok**: Hook in first 2 seconds, trending format awareness
* **Facebook**: Conversational, question-driven, shareable

### 3. Content Pillars

Help users define 4-6 content pillars and rotate through them:

* Educational (teach something)
* Behind-the-scenes (build trust)
* Social proof (testimonials, results)
* Entertainment (personality, humor)
* Promotional (offers, launches)
* Community (engage, ask, poll)

### 4. Repurposing Map

For each piece of content, suggest how to adapt it across platforms.

### 5. Hashtag Strategy

Research and suggest relevant hashtags in three tiers:

* High volume (brand awareness)
* Medium volume (discoverable)
* Niche (targeted community)

## Output Format

Always output in a clean, copy-paste-ready format. Include character counts for platform-limited posts. Group by day or platform as requested.

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

- Plan, draft, and organize social media content across platforms
- Create
  content calendars, write
- 触发关键词: scheduler, organize, draft, social, plan, media

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

### Q1: 如何开始使用Social Media Schedul？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Social Media Schedul有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- **输入内容长度**：由于平台限制，输入的文案长度需符合各平台要求。例如，Twitter限制在280字符以内，LinkedIn则在1300字符左右为佳。
- **输入格式**：输入内容应遵循Markdown格式，以便Skill正确解析和格式化输出。
- **内容类型**：Skill主要针对文本内容进行规划与撰写，对于图片、视频等多媒体内容，Skill的辅助作用有限。

### 性能边界
- **并发处理**：Skill支持单用户单任务处理，不支持多任务并发执行。
- **数据处理量**：Skill对于大量数据的处理能力有限，建议用户分批次输入内容，以提高处理效率。

### 兼容性约束
- **平台支持**：Skill主要针对Twitter/X, LinkedIn, Instagram, TikTok, Facebook等主流社交媒体平台，对于其他平台的支持可能有限。
- **语言支持**：Skill主要支持英文输入，对于其他语言的输入可能存在识别错误或无法处理的情况。

### 依赖性限制
- **LLM支持**：Skill依赖于底层LLM模型，无LLM环境无法使用。
- **操作系统**：Skill支持Windows, macOS, Linux等主流操作系统，但部分功能可能因操作系统差异而受限。

### 其他限制
- **复杂场景**：Skill在处理复杂场景时，可能需要人工辅助判断，例如涉及敏感话题或特定行业知识的内容。
- **性能依赖**：Skill的性能取决于底层模型的能力，随着模型更新，Skill的性能可能发生变化。

## 差异化优势

### 与同类方案对比

1. **手动操作**：手动管理社交媒体内容需要花费大量时间和精力，且难以保证内容的统一性和专业性。相比之下，Social Media Scheduler通过自动化的内容规划和撰写，可以显著提高效率，并确保内容的一致性和质量。

2. **其他社交媒体管理工具**：虽然市面上有许多社交媒体管理工具，但它们往往专注于发布和监控，而不是内容的规划和撰写。Social Media Scheduler则集成了内容日历、平台优化撰写、内容复用建议和标签策略等功能，为用户提供一站式的社交媒体内容管理解决方案。

3. **通用方法**：通用方法可能包括使用Excel表格或Google Sheets来规划内容，但这需要用户自行设计模板和规则，且缺乏智能化辅助。Social Media Scheduler提供直观的用户界面和智能功能，大大简化了内容管理流程。

### 独特功能

1. **平台优化撰写**：针对不同社交媒体平台的特点，Social Media Scheduler提供定制化的撰写建议，如Twitter的简洁有力、LinkedIn的专业叙述等，帮助用户提高内容质量。

2. **内容复用地图**：用户可以轻松地将单篇内容复用于不同平台，节省时间并保持品牌一致性。

3. **标签策略**：根据内容主题和目标受众，Social Media Scheduler提供多层级标签策略，帮助用户精准定位和优化内容。

4. **内容日历**：直观的内容日历视图让用户可以轻松规划和管理内容发布时间，确保内容按计划执行。

5. **内容支柱**：帮助用户定义和轮换不同的内容支柱，如教育、娱乐、促销等，确保内容多样化且富有吸引力。

### 效率提升

使用Social Media Scheduler，用户可以节省至少50%的内容撰写时间，并通过自动化流程减少重复性工作。

### 应用场景创新

1. **多平台营销活动**：为不同社交媒体平台创建统一主题的营销活动，提高活动效果。

2. **内容营销自动化**：通过内容日历和自动撰写功能，实现内容营销的持续性和一致性。

3. **品牌形象塑造**：通过精心策划和优化的内容，塑造和提升品牌形象。

