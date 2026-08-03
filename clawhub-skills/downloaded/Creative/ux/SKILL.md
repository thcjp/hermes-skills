---
slug: ux
name: ux
version: "1.0.0"
displayName: UX
summary: "设计分析直觉高效贴合心智模型的用户体验(社区下载版)"
  with user mental m...
license: MIT
description: |-
  Design and analyze user experiences that are intuitive, efficient, and
  aligned with user mental m。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

# UX

## Flow Analysis

* Map every step to complete key tasks—identify unnecessary steps
* Each step is a potential dropout—minimize count and friction
* Question every required field—if not essential now, defer or remove
* Identify points requiring user memory—provide recognition instead

## Mental Model Alignment

* Use vocabulary users would expect—not internal/technical terms
* Match familiar patterns before inventing—innovation has learning cost
* Consistent metaphors throughout—don't mix paradigms in same product
* Align with platform conventions—users bring expectations from other apps

## Friction Reduction

* Smart defaults reduce decisions—good default better than more options
* Pre-fill from available context—location, previous selections, account data
* Auto-save progress—never lose user work
* Don't ask for information already available—or not yet needed

## Progressive Disclosure

* Show only what's needed for current task—hide advanced options until relevant
* Reveal complexity gradually—basic path first, power features discoverable
* Empty states guide to first action—not just "Nothing here"
* Teach by doing, not explaining—inline hints over tutorials

## Feedback Design

* Every action gets acknowledgment—visual, haptic, or audible
* Progress indication for waits over 1 second
* Error messages: what happened + what to do next
* Success confirmation for significant actions

## Error Prevention

* Design to prevent errors—constraints, confirmations, smart defaults
* Confirmation dialogs only for destructive/irreversible actions
* Undo available for reversible actions—reduces fear of exploring
* Inline validation catches errors before submission

## Cognitive Load

* One primary action per screen—clear visual hierarchy
* Group related information—chunking aids comprehension
* Limit simultaneous choices—too many options cause paralysis
* Consistent patterns across product—learned once, applied everywhere

## Edge Cases to Design

* Empty state: first time, cleared, filtered with no results
* Loading state: skeleton preferred over spinner for known layouts
* Error state: what went wrong, how to recover
* Partial state: some data available, some loading/failed
* Offline state: what works, what's queued, what's unavailable

## Reversibility

* Trash over permanent delete—recovery possible
* Preview before commit—show effect of action
* Draft states for complex work—don't require completion in one session
* Settings and decisions easy to change—not buried or locked

## Task Completion

* Define what success looks like for each flow
* First value delivered quickly—quick win before complex setup
* Clear next step always visible—no dead ends
* Completion feels complete—confirmation, celebration for big tasks

## Accessibility Integration

* Keyboard/switch navigation works for all flows
* Screen reader announces what's needed—labels, states, updates
* Sufficient contrast without relying on color alone
* Respects user preferences—motion, text size, dark mode

## Copy and Labels

* Button labels describe outcome—"Save Changes" not "Submit"
* Headings scannable—user finds what they need quickly
* Error text actionable—not just "Invalid input"
* Microcopy reduces uncertainty—helper text where questions arise

## Consistency Checks

* Same words for same concepts—create glossary if needed
* Same interaction patterns—swipe/tap/long-press mean same things
* Visual similarity reflects functional similarity
* Exceptions rare and justified

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

- Design and analyze user experiences that are intuitive, efficient, and
  aligned with user mental m
- 触发关键词: analyze, design, experiences

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

### Q1: 如何开始使用UX？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: UX有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制

### 输入限制
- UX技能接受的用户请求应遵循清晰、简洁的原则，避免过长的文本或复杂的指令，以免影响处理速度和准确性。
- 用户请求中不应包含非文本元素，如图片、音频等，因为技能主要处理文本信息。

### 性能边界
- 在处理大量数据或复杂任务时，技能可能需要较长时间来生成结果，用户应耐心等待。
- 在高并发情况下，技能的响应速度可能会有所下降，建议用户合理安排请求时间。

### 兼容性约束
- UX技能主要支持Markdown格式的输入，对于其他格式（如HTML、PDF等）可能无法直接处理。
- 在不同的AI Agent平台上，技能的表现可能存在细微差异，用户在使用时应注意查看具体平台的说明。

### 功能限制
- UX技能主要关注用户体验设计分析，对于3D建模、动画制作等视觉设计领域不提供支持。
- 技能无法替代专业设计师的工作，仅作为辅助工具使用。

### 数据隐私
- UX技能在处理用户请求时，会严格保护用户隐私，不存储或泄露任何敏感信息。
- 用户请求中的个人数据仅用于技能处理，不会用于其他目的。

## 边界条件与限制

### 输入限制
- UX技能不支持处理包含特殊字符、表情符号等非标准文本的输入。
- 用户请求中不应包含代码片段或命令，以免影响技能的正常运行。

### 性能边界
- 在处理复杂任务时，技能的响应时间可能会增加，用户应耐心等待。
- 在网络环境较差的情况下，技能的响应速度可能会有所下降。

### 兼容性约束
- UX技能在不同操作系统上的表现可能存在细微差异，用户在使用时应注意查看具体平台的说明。
- 技能可能不支持某些特定平台的特殊功能。

### 功能限制
- UX技能主要关注用户体验设计分析，对于其他领域（如市场营销、数据分析等）不提供支持。
- 技能无法替代专业设计师的工作，仅作为辅助工具使用。

### 数据隐私
- UX技能在处理用户请求时，会严格保护用户隐私，不存储或泄露任何敏感信息。
- 用户请求中的个人数据仅用于技能处理，不会用于其他目的。

## 边界条件与限制

### 输入限制
- UX技能不支持处理包含敏感信息（如姓名、地址、电话号码等）的输入。
- 用户请求中不应包含非文本元素，如图片、音频等，因为技能主要处理文本信息。

### 性能边界
- 在处理大量数据或复杂任务时，技能可能需要较长时间来生成结果，用户应耐心等待。
- 在高并发情况下，技能的响应速度可能会有所下降，建议用户合理安排请求时间。

### 兼容性约束
- UX技能主要支持Markdown格式的输入，对于其他格式（如HTML、PDF等）可能无法直接处理。
- 在不同的AI Agent平台上，技能的表现可能存在细微差异，用户在使用时应注意查看具体平台的说明。

### 功能限制
- UX技能主要关注用户体验设计分析，对于3D建模、动画制作等视觉设计领域不提供支持。
- 技能无法替代专业设计师的工作，仅作为辅助工具使用。

### 数据隐私
- UX技能在处理用户请求时，会严格保护用户隐私，不存储或泄露任何敏感信息。
- 用户请求中的个人数据仅用于技能处理，不会用于其他目的。

