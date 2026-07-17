---
slug: ai-agent-helper
name: ai-agent-helper
version: "1.0.0"
displayName: AI Agent Helper
summary: AI Agent 設定同優化助手 - Prompt Engineering、Task Decomposition、Agent Loop設計
license: MIT
description: |-
  AI Agent 設定同優化助手 - Prompt Engineering、Task Decomposition、Agent Loop設計

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: task, prompt, decomposition, agent, 設定同優化助, engineering, 設計, helper
tags:
- Agents
- Productivity
tools:
- read
- exec
---

# AI Agent Helper

幫你setup同優化AI Agents既技能。

## 功能

* 📝 Prompt Engineering - 整高質量system prompts
* 🔄 Task Decomposition - 將複雜任務拆解
* ⚙️ Agent Loop設計 - ReAct/ReAct/Chain-of-Thought
* 🎯 Tool Selection - 最佳化agent既tool usage

## 使用場景

"帮我整prompt" / "點樣set AI agent" / "優化agent response"

## 技術

* System Prompt優化
* Few-shot examples
* Output parsing (JSON/structured)
* Error handling patterns
* Token優化

## 範例

```python
system = """你係{role}。
目標：{goal}
限制：{constraints}
Output格式：{format}"""
```

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
