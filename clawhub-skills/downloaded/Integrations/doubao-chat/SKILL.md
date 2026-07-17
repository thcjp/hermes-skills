---
slug: doubao-chat
name: doubao-chat
version: "1.0.0"
displayName: Doubao Chat
summary: 豆包大模型对话（免费 API，支持联网搜索）
license: MIT
description: |-
  豆包大模型对话（免费 API，支持联网搜索）

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 支持联网搜索, 免费, doubao, chat, 豆包大模型对
tags:
- Integrations
tools:
- read
- exec
---

# Doubao Chat

使用豆包免费 API 进行对话，支持联网搜索。

## 环境变量

```bash
DOUBAO_SESSIONID=your_sessionid
```

## 使用方法

```bash
node scripts/chat.js "你好"
```

## API 端点

对话补全：POST <https://doubao-free-api.vercel.app/v1/chat/completions>

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
