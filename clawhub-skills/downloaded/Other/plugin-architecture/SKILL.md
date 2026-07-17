---
slug: plugin-architecture
name: plugin-architecture
version: "1.0.1"
displayName: Plugin UI Architecture
summary: Installs UI plugin architecture into OpenClaw, enabling plugins to register
  custom views, navigat...
license: MIT
description: |-
  Installs UI plugin architecture into OpenClaw, enabling plugins to register
  custom views, navigat...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: architecture, installs, openclaw, plugin
tags:
- Other
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
