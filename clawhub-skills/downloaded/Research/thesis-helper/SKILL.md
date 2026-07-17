---
slug: thesis-helper
name: thesis-helper
version: "2.0.0"
displayName: Thesis Helper
summary: 论文写作助手。论文大纲生成、文献综述框架、摘要生成、引用格式转换、格式规范检查、答辩准备。Thesis helper with outline generation,
  literature re...
license: MIT-0
description: |-
  论文写作助手。论文大纲生成、文献综述框架、摘要生成、引用格式转换、格式规范检查、答辩准备。Thesis helper with outline
  generation, literature re...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: outline, 引用格式转换, 文献综述框架, thesis, 摘要生成, 论文写作助手, generation, 论文大纲生成
tags:
- Research
tools:
- read
- exec
---

# Thesis Helper

论文写作助手。论文大纲生成、文献综述框架、摘要生成、引用格式转换、格式规范检查、答辩准备。Thesis helper with outline generation, literature review, abstract writing, citation formatting, style guide, defense preparation.

## 速查表

See commands above.

## 命令速查

```text
  outline         outline
  literature      literature
  abstract        abstract
  cite            cite
  format          format
  defense         defense
```

> 💡 小技巧：先用 `help` 查看所有命令，再选择最适合的

## 专业建议

* 论文大纲**：输入研究主题，生成多级大纲结构
* 文献综述**：按时间线或主题分类组织文献框架
* 摘要生成**：
* 中文摘要：200-300字
* 英文摘要：150-250 words

---

## *thesis-helper by BytesAgain*

💬 Feedback & Feature Requests: <https://bytesagain.com/feedback>
Powered by BytesAgain | bytesagain.com

* Run `thesis-helper help` for commands
* No API keys needed

## Commands

Run `thesis-helper help` to see all available commands.

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
