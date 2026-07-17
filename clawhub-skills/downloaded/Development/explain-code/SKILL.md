---
slug: explain-code
name: explain-code
version: "1.0.0"
displayName: explain-code
summary: 用可视化图表和类比解释代码。在解释代码如何工作、教授代码库或用户询问如何工作时使用
license: MIT
description: |-
  用可视化图表和类比解释代码。在解释代码如何工作、教授代码库或用户询问如何工作时使用

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: explain-code, explain, code, 在解释代码如, 用可视化图表, 何工作, 教授代码库或, 和类比解释代
tags:
- Development
tools:
- read
- exec
---

# explain-code

在解释代码时，总是包含:

1. **先打比方做类比**: 将代码与日常生活中的事物进行比较
2. **画图表**: 使用ASCII art来展示流程、结构或关系
3. **遍历代码**: 一步一步地解释发生了什么
4. **Highlight突出问题**: 常见的错误或误解是什么？

保持解释自然。对于复杂的概念，可以用多个类比。

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
