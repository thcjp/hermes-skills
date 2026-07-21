---
slug: resume-assistant-free
name: resume-assistant-free
version: "1.0.0"
displayName: 简历助手免费版
summary: 免费版简历助手，支持基础评分与润色功能。
license: MIT
description: |-
  简历助手免费版，提供基础的简历评分与润色功能。
  支持100分制评分与基础检查项审查。
  适用于求职者的简历基础优化。
tools:
  - read
  - exec
---

# 简历助手（免费版）

提供基础简历评分与润色功能的AI助手。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 浏览器 | 应用 | 可选 | 操作系统自带（PDF导出） |

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行简历优化任务

## 核心能力

### Score - 简历评分
100分制基础评估，识别主要问题：

**评分维度：**
- Content Quality（内容质量）
- Structure & Formatting（结构与格式）
- Language & Grammar（语言与语法）
- ATS Optimization（ATS兼容性）

输出分数、等级与Top 3问题。

**输入**: 用户提供Score - 简历评分所需的指令和必要参数。
**处理**: 按照skill规范执行Score - 简历评分操作,遵循单一意图原则。### Polish - 简历润色

基础检查项审查与改进：

- 检查联系信息、个人简介、工作经历等基础项
- 优化动作动词与量化成果
- 返回润色后的简历

### Export - 基础导出
将简历导出为Markdown或HTML格式：

- Markdown：干净、结构化
- HTML：自包含文件，可浏览器打印为PDF

**输入**: 用户提供Export - 基础导出所需的指令和必要参数。
**处理**: 按照skill规范执行Export - 基础导出操作,遵循单一意图原则。
## 使用流程

1. 准备简历文本（纯文本或Markdown格式）
2. 选择操作：score评分 / polish润色 / export导出
3. 使用自然语言描述需求
4. Agent执行并返回结果
5. 按建议修改简历

## 示例

### 示例1：简历评分

```
用户: Score my resume
[粘贴简历]

Agent: Resume Score: 68/100 (Grade: C)
Top 3 Issues:
1. No quantified achievements
2. Weak action verbs
3. Missing keywords for target role
建议：使用polish命令进行润色
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 简历内容为空 | 未提供简历文本 | 提示用户提供简历文本 |
| 简历超长 | 超过10,000字符 | 精简内容；移除冗余经历 |
| 导出格式不支持 | format参数错误 | 免费版仅支持markdown和html格式 |

## 常见问题

### Q1: 免费版与付费版有什么区别？
A: 免费版提供基础评分与润色功能，支持Markdown和HTML导出。付费版额外提供customize岗位定制、LaTeX/Word/PDF导出、40+检查项完整审查、差距分析等高级功能。

### Q2: 支持哪些语言？
A: 支持英文（en）和中文（zh）两种语言。

### Q3: 如何导出PDF？
A: 免费版支持导出HTML，可使用浏览器的打印功能将HTML转为PDF。

## 已知限制

- 不支持customize岗位定制功能
- 不支持Word、LaTeX、PDF直接导出
- 检查项少于付费版的40+完整检查
- 不提供差距分析与关键词覆盖报告
