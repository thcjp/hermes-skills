---
slug: knowledge-capture
name: knowledge-capture
version: "0.1.0"
displayName: Knowledge Capture
summary: Transform conversations and discussions into structured Notion documentation
license: MIT
description: |-
  Transform conversations and discussions into structured Notion documentation

  核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: knowledge, conversations, transform, discussions, structured, capture
tags:
- Knowledge
- Productivity
tools:
- read
- exec
---

# Knowledge Capture

## Overview

The Knowledge Capture skill transforms conversations, discussions, and unstructured information into organized, structured documentation in Notion. It helps you preserve institutional knowledge by capturing important conversations and converting them into actionable, well-formatted documentation.

## When to Use

Use this skill when you need to:

* Convert transcripts or conversation notes into structured documentation
* Create meeting summaries with action items
* Build knowledge base articles from discussions
* Archive important conversations for future reference
* Extract key insights and decisions from discussions

## Features

* **Smart Content Extraction**: Automatically identifies key points, decisions, and action items from conversations
* **Structured Organization**: Creates well-organized Notion documents with proper hierarchy
* **Metadata Capture**: Preserves participants, dates, and context information
* **Action Item Tracking**: Extracts and formats action items with ownership and deadlines
* **Cross-linking**: Automatically creates links to related documentation and team members

## Requirements

* **Notion API Access**: Integration token with appropriate permissions
* **Target Workspace**: Notion workspace where documentation will be stored
* **Template (Optional)**: Pre-defined Notion template for consistent structure

## Implementation Details

This skill uses the Notion API to:

1. Parse input content (text, transcripts, or discussion notes)
2. Extract key information using structural analysis
3. Format content according to Notion document standards
4. Create or update Notion pages with captured knowledge
5. Maintain cross-references and relationships

### Typical Workflow

```text
Input: Conversation/Discussion
  ↓
Parse & Extract
  ↓
Identify: Key Points, Decisions, Action Items
  ↓
Format for Notion
  ↓
Create/Update Notion Document
  ↓
Output: Structured Documentation
```

## Example Use Cases

1. **Team Meeting Notes**

   * Input: Meeting transcript
   * Output: Organized meeting summary with decisions and next steps
2. **Customer Call Documentation**

   * Input: Call notes and transcript
   * Output: Customer interaction record with key requirements
3. **Architecture Discussion**

   * Input: Design discussion notes
   * Output: Architectural decision record with alternatives and rationale
4. **Interview Notes**

   * Input: Interview transcript
   * Output: Structured candidate or user research documentation

## Configuration

Set up these environment variables or Notion settings:

env

```
NOTION_API_TOKEN=your_token_here
NOTION_DATABASE_ID=your_database_id
```

## See Also

* [Research Documentation](/skills/research-documentation) - For research-focused documentation
* [Meeting Intelligence](/skills/meeting-intelligence) - For meeting preparation and follow-up
* [Notion API Documentation](https://developers.notion.com)

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
