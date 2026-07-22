---
slug: "learn-cog-free"
name: "learn-cog-free"
version: "1.0.0"
displayName: "个性化学习助手免费版"
summary: "免费版AI学习助手，支持概念解释、语言学习与学习指南生成。"
license: "MIT"
description: |-
  个性化学习助手免费版，提供基础AI辅导功能。
  支持概念解释、语言学习基础与学习指南生成。
  适用于学生的日常学习与知识获取。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
---
# 个性化学习助手（免费版）

AI驱动的学习助手，支持概念解释、语言学习与学习指南生成。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 概念解释（Concept Explanations）
多角度解释概念，适配不同理解水平：

- **概念拆解**：如"Explain quantum entanglement like I'm 10 years old"
- **多角度解释**：如"Explain recursion using 3 different analogies"
- **作业辅导**：逐步解答数学、物理等问题并解释每步
- **代码调试**：解释代码问题并帮助修复

**处理**: 按照skill规范执行概念解释（Concept Explanations）操作,遵循单一意图原则。
**输出**: 返回概念解释（Concept Explanations）的执行结果,包含操作状态和输出数据。### 语言学习（Language Learning）

基础语言学习辅导：

- **语法讲解**：如"Explain Japanese particles with examples"
- **词汇构建**：如"Teach me 20 essential business Chinese phrases"
- **写作反馈**：检查语言学习写作并提供修改建议

### 学习指南（Study Guides）
生成基础学习材料：

- **学习指南**：如"Create a study guide for AP Chemistry exam"
- **摘要笔记**：如"Summarize Chapter 5 of my biology textbook"
- **速查表**：如"Create a one-page reference for Python syntax"

**输入**: 用户提供学习指南（Study Guides）所需的指令和必要参数。
**处理**: 按照skill规范执行学习指南（Study Guides）操作,遵循单一意图原则。
### 概念拆解

执行概念拆解操作,处理用户输入并返回结果。

**输入**: 用户提供概念拆解所需的参数和指令。

**输出**: 返回概念拆解的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`概念拆解`相关配置参数进行设置
#
## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 明确学习目标与当前水平
3. 使用自然语言描述学习需求
4. Agent生成个性化学习内容
5. 通过练习巩固学习成果

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 示例

### 示例1：学习递归概念

```
用户: Explain recursion using 3 different analogies, I'm a beginner

Agent: 递归的三种类比解释：
1. 镜中镜 - 一面镜子映照另一面镜子，层层深入
2. 俄罗斯套娃 - 打开一个娃娃里面还有更小的娃娃
3. 楼梯攀登 - 每步只上一级，重复直到顶层
[附Python代码示例]
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 学习内容过浅/过深 | 未说明当前水平 | 明确说明：Complete beginner / Intermediate / Advanced |
| 概念解释不清楚 | 学习风格不匹配 | 尝试不同学习风格：Analogies / Step-by-Step |
| 代码示例无法运行 | 环境依赖缺失 | 检查Python/Node版本；安装所需依赖 |

## 常见问题

### Q1: 免费版与付费版有什么区别？
A: 免费版提供概念解释、基础语言学习与学习指南功能。付费版额外提供项目教程、视觉学习、对话练习、闪卡生成、模拟测试等高级功能。

### Q2: 支持哪些学科？
A: 支持STEM、人文、技术技能等基础学科的辅导，覆盖数学、物理、编程、语言等常见领域。

### Q3: 如何获得更好的学习效果？
A: 说明当前水平、多问为什么、请求练习题、承认困惑点，并基于已理解内容构建新知识。

## 已知限制

- 不支持项目教程与实战项目驱动学习
- 不支持视觉学习的图表生成
- 不支持闪卡与模拟测试生成
- 语言学习口语练习需配合TTS工具
