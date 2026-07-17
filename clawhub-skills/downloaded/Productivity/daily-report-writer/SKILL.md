---
slug: daily-report-writer
name: daily-report-writer
version: "1.0.0"
displayName: Daily Report Writer
summary: 根据输入生成日报 Markdown 草稿并写入 reports 目录
license: MIT
description: |-
  根据输入生成日报 Markdown 草稿并写入 reports 目录

  核心能力:

  - 商业工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 日程管理、效率提升、团队协作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 目录, report, 根据输入生成, 日报, writer, 草稿并写入, markdown, daily
tags:
- Productivity
tools:
- read
- exec
---

# Daily Report Writer

## Use when

* 用户要求生成“日报/工作总结草稿”

## Inputs

* date（必填，YYYY-MM-DD）
* highlights（必填，数组）
* blockers（可选，数组）

## Steps

1. 校验参数是否齐全。
2. 读取（或创建）`reports/{{date}}-daily-report.md`。
3. 按固定模板写入内容。
4. 返回 `status/summary/data/nextAction`。

## Failure

* 缺参数：明确指出缺哪一项，并给示例输入。
* 写文件失败：返回目录权限检查建议。

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
