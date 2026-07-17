---
slug: knowledge
name: knowledge
version: "1.0.0"
displayName: Knowledge
summary: 本地知识库集成 - 文档检索、投喂、双轨模式切换
license: MIT
description: |-
  本地知识库集成 - 文档检索、投喂、双轨模式切换

  核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 投喂, 本地知识库集, knowledge, 文档检索, 双轨模式切换
tags:
- Knowledge
tools:
- read
- exec
---

# Knowledge

## 使用方法

| 命令 | 说明 |
| --- | --- |
| "查一下 xxx" | 搜索知识库 |
| "切换到本地知识库" | 使用本地检索 |
| "切换到 AnythingLLM" | 使用对话模式 |
| "知识库统计" | 查看文档数量 |

## 文件位置

* 知识库根目录：`E:/knowledge-base`
* API服务：`http://127.0.0.1:8001`

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
