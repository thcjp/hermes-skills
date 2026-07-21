---
slug: auto-workflow
name: auto-workflow
version: "1.0.0"
displayName: Auto Workflow
summary: Builds automation workflows from repetitive tasks. Use when user mentions
  \
license: MIT
description: |-
  Builds automation workflows from repetitive tasks。Use when user mentions
  \

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillH...
tags: '[''Automation'']'
tools:
  - read
  - exec
---

# Auto Workflow

把重复任务自动化的能力。

## 能力轮廓

* **输入**：重复性任务/手动操作
* **输出**：自动化工作流 + 执行脚本
* **核心逻辑**：识别 → 抽象 → 自动化 → 测试

## 工作流

```text
1. 观察 - 用户在重复做什么？
2. 抽象 - 这个任务的模式是什么？
3. 设计 - 怎么自动完成？
4. 实现 - 写脚本/配置
5. 测试 - 小范围验证
6. 优化 - 迭代改进
```

## 示例

用户每周手动发周报：

1. 收集数据（系统状态）
2. 整理成模板
3. 发送邮件

自动化后：

* 每周五自动执行
* 收集本周数据
* 生成报告
* 自动发送

## 思维模式

不是"回答问题"，而是"看到重复→立刻构建自动化"

遇到重复操作时：

* 问自己：能否写成脚本？
* 问自己：下次能否自动跑？
* 直接做，不等用户要求

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

- Builds automation workflows from repetitive tasks
- 触发关键词: workflows, repetitive, auto, automation, workflow, builds

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

### Q1: 如何开始使用Auto Workflow？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Auto Workflow有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
