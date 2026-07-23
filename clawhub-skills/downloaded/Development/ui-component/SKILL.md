---
slug: ui-component
name: ui-component
version: "2.0.0"
displayName: Ui Component
summary: "UI组件HTML/CSS代码生成。表单、表格、卡片、模态框、导航栏，输出完整可运行HTML文件。UI component generator:
  form, table, card, modal."
license: MIT-0
description: |-
  UI组件HTML/CSS代码生成。表单、表格、卡片、模态框、导航栏，输出完整可运行HTML文件。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
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

## 示例

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

🎯 **精准** — 针对具体场景定制化输出
📋 **全面** — 多个命令覆盖完整工作流
🇨🇳 **本土化** — 完全适配中文用户习惯

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Ui Component？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Ui Component有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
