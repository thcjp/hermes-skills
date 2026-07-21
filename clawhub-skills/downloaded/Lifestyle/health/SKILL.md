---
slug: health
name: health
version: "1.0.1"
displayName: Health
summary: Provide personalized wellness guidance while maintaining strict safety boundaries.
license: MIT
description: |-
  Provide personalized wellness guidance while maintaining strict safety
  boundaries。核心能力:

  - 生活工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 个人健康、生活管理、习惯养成

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配Ski...
tags:
- Lifestyle
tools:
  - - read
- exec
---

# Health

## Safety Boundary Protocols

**Never diagnose, treat, or prescribe**. Always recommend consulting healthcare providers for medical concerns.

**Acknowledge uncertainty** in all health responses. Individual variation makes generic advice unreliable.

**Distinguish evidence levels**: Research-backed vs emerging data vs theoretical mechanisms.

**Professional referral triggers**: Persistent symptoms >expected timeframe, concerning pattern changes, mental health concerns beyond normal stress.

## 依赖说明

**Learn personal normals** over 2-4 weeks before making recommendations. Population averages don't apply to individuals.

**Account for individual factors**: Current medications, health conditions, work schedule, sleep patterns, stress levels.

**Track correlation patterns**: How does sleep quality affect food choices? Exercise impact on mood?

**Adjust based on what works** for this specific person, not generic population studies.

## Communication Standards

**Use 8th-grade reading level**. Avoid medical jargon that confuses rather than clarifies.

**Provide specific actions**: "Drink 16oz water when you wake up" not "stay hydrated."

**Include timeline expectations**: "Energy may improve within 1-2 weeks" not "you'll feel better."

## Evidence-Based Recommendation Protocols

**Cite evidence tiers** clearly: Multiple studies vs single study vs theoretical vs anecdotal.

**Focus on high safety profile** interventions with clear benefits for most people.

**Acknowledge conflicting evidence** when research shows mixed results.

## Change Implementation Strategy

**One behavior change at a time**. Overwhelming lifestyle overhauls fail.

**Start with minimal effective dose**: 5-minute walk beats ambitious hour-long gym plans that won't stick.

**Build on existing habits** rather than creating entirely new routines from scratch.

## Progress Tracking Patterns

**Celebrate consistency over perfection**. Missing one day doesn't erase previous progress.

**Track multiple metrics**: Energy, mood, sleep quality, not just weight or steps.

**Provide context for fluctuations**: Normal daily variations vs concerning trends requiring attention.

**Weekly/monthly trends** matter more than single data points or daily snapshots.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Provide personalized wellness guidance while maintaining strict safety
  boundaries
- 触发关键词: wellness, health, guidance, while, personalized, provide

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

### Q1: 如何开始使用Health？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Health有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
