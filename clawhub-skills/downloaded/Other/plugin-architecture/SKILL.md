---
slug: plugin-architecture
name: plugin-architecture
version: "1.0.1"
displayName: Plugin Architecture
summary: Installs UI plugin architecture into OpenClaw, enabling plugins to register
  custom views, navigat...
license: MIT
description: |-
  Installs UI plugin architecture into OpenClaw, enabling plugins to register
  custom views, navigat。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Other
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Plugin UI Architecture

name: plugin-architecture
version: "1.1.0"
author: Charles Sears
description: Adds UI plugin registration support to Skill平台 - allows plugins to register custom tabs in the Control UI.

## Overview

This skill adds the ability for Skill平台 plugins to register custom UI views/tabs that appear in the Control dashboard sidebar.

## Installation

**This skill requires manual installation by your Skill平台 agent.**

After extracting this skill to your skills folder, give your agent this prompt:

```text
Please install the plugin-architecture skill. Read the INSTALL_INSTRUCTIONS.md file in the skill folder and follow it step by step. The skill is at: ~/clawd/skills/plugin-architecture/
```

## What It Does

Once installed, plugins can register UI tabs like this:

```typescript
// In your plugin's register() function:
if (typeof api.registerView === "function") {
  api.registerView({
    id: "my-view",
    label: "My View",
    subtitle: "Description here",
    icon: "database",  // Icon name from the icon set
    group: "Agent",    // Which nav group (Chat, Control, Agent, Settings)
    position: 5,       // Order within the group
  });
}
```

## Files Included

* `SKILL.md` - This file
* `INSTALL_INSTRUCTIONS.md` - Step-by-step instructions for the agent
* `reference/` - Reference code files showing what to add

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

This skill adds the ability for Skill平台 plugins to register custom UI views/tabs that appear in the Control dashboard sidebar.

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Plugin Architecture？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Plugin Architecture有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
