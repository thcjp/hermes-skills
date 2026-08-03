---
slug: plugin-architecture
name: plugin-architecture
version: "1.0.1"
displayName: Plugin Architecture
summary: "为Agent安装UI插件架构,支持注册自定义视图、导航、命令,扩展Agent界面能力"
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

---
## 边界条件与限制

### 输入限制
- **数据格式**: 插件注册视图时，传入的数据格式必须符合API定义，否则可能导致注册失败。
- **ID唯一性**: 视图ID必须全局唯一，重复的ID会导致注册失败。
- **资源限制**: 由于Control UI的侧边栏空间有限，过多的自定义视图可能会导致界面拥挤，影响用户体验。

### 性能边界
- **并发处理**: 当大量用户同时访问自定义视图时，可能对Agent的性能造成影响，建议优化插件代码，减少资源消耗。
- **加载时间**: 自定义视图的加载时间不应过长，否则会影响用户体验，建议优化视图的加载逻辑。

### 兼容性约束
- **Agent版本**: 该技能需要与特定版本的Agent平台兼容，不兼容的版本可能导致技能无法正常工作。
- **浏览器兼容性**: 如果自定义视图依赖于前端技术，需要确保其在目标浏览器上具有良好的兼容性。
- **插件依赖**: 自定义视图可能依赖于其他插件或Skill，需要确保这些依赖项在Agent中正确安装和配置。

