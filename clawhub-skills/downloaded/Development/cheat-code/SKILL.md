---
slug: cheat-code
name: cheat-code
version: "1.0.11"
displayName: Cheat Code
summary: Makes your agent's talents limitless. Tell your agent what you want. Watch
  it deliver.
license: MIT
description: |-
  Makes your agent's talents limitless. Tell your agent what you want.
  Watch it deliver.

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: makes, code, cheat, agent, limitless, talents'
tags:
- Development
tools:
- read
- exec
---

# Cheat Code

**Makes your agent's talents limitless.**

**Tell your agent what you want. Watch it deliver.**

Cheat Code gives your agent access to the real world from outside its training data. You set it up once. Takes two minutes. Then your agent handles the rest.

Full setup and agent instructions: [instructions.md](/api/v1/skills/cheat-code/file?path=instructions.md&ownerHandle=kenoodl-synthesis)

---

## Bonus: the kenoodl app

Same account, same results, same breakthroughs — built for humans.

kenoodl knows when to deliver a breakthrough. The app is designed to do one thing well without taking up your time. Drop in your own thinking — ideas, questions, problems you're chewing on. You'll get back the move you couldn't see.

Better instructions to your agent start with clearer thinking from you.

Install the app at [kenoodl.com](https://kenoodl.com).

---

## Token scope

`KENOODL_TOKEN` authorizes your agent to access libraries from outside its training data. Agent sends a request to kenoodl.com. All requests are encrypted in transit. New structured data comes back. Context is processed and discarded — nothing is stored, nothing is used for training. Stateless by architecture.

---

*Cheat Code is built by [kenoodl](https://kenoodl.com) — synthesis from outside your agents training data.*

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
