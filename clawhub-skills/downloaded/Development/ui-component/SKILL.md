---
slug: ui-component
name: ui-component
version: "2.0.0"
displayName: Ui Component
summary: "UI组件HTML/CSS代码生成。表单、表格、卡片、模态框、导航栏，输出完整可运行HTML文件。UI component generator:
  form, table, card, modal."
license: MIT-0
description: |-
  UI组件HTML/CSS代码生成。表单、表格、卡片、模态框、导航栏，输出完整可运行HTML文件。UI component generator:
  form, table, card, modal.

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: generator, 代码生成, component, form, 卡片, html, 组件, 表格
tags:
- Development
tools:
- read
- exec
---

# Ui Component

UI组件HTML/CSS代码生成。表单、表格、卡片、模态框、导航栏，输出完整可运行HTML文件。UI component generator: form, table, card, modal, navbar as standalone HTML files.

## 核心特点

🎯 **精准** — 针对具体场景定制化输出
📋 **全面** — 多个命令覆盖完整工作流
🇨🇳 **本土化** — 完全适配中文用户习惯

## 可用命令

* **generate** — generate
* **form** — form
* **table** — table
* **card** — card
* **modal** — modal
* **navbar** — navbar

## 专业建议

* 一致性** — 同一项目使用统一的圆角、间距、配色
* 可访问性** — 表单加label，按钮有焦点样式，对比度达标
* 响应式** — 移动端优先，用相对单位(rem/%)
* 简洁** — 少即是多，不加无意义装饰
* | 需求 | 推荐命令 |

---

## *ui-component by BytesAgain*

💬 Feedback & Feature Requests: <https://bytesagain.com/feedback>
Powered by BytesAgain | bytesagain.com

## Examples

```bash
ui-component help

ui-component run
```

* Run `ui-component help` for all commands

## Commands

Run `ui-component help` to see all available commands.

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
