---
slug: art
name: art
version: "1.0.0"
displayName: Art
summary: Guide art creation, technique development, and appreciation with practical,
  medium-specific advice.
license: MIT
description: |-
  Guide art creation, technique development, and appreciation with practical,
  medium-specific advice.

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: development, creation, appreciation, guide, technique, art
tags:
- Other
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
