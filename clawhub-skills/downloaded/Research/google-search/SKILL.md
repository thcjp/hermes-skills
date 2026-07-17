---
slug: google-search
name: google-search
version: "1.0.0"
displayName: google-search
summary: Search the web using Google Custom Search Engine (PSE). Use this when you
  need live information, ...
license: MIT
description: |-
  Search the web using Google Custom Search Engine (PSE). Use this when
  you need live information, ...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: custom, using, google-search, search, google
tags:
- Research
tools:
- read
- exec
---

# google-search

This skill allows Skill平台 agents to perform web searches via Google's Custom Search API (PSE).

## Setup

1. **Google Cloud Console:** Create a project and enable the "Custom Search API".
2. **API Key:** Generate an API Key.
3. **Search Engine ID (CX):** Create a Programmable Search Engine at [cse.google.com](https://cse.google.com/cse/all), and get your CX ID.
4. **Environment:** Store your credentials in a `.env` file in your workspace:

   text

   ```
   GOOGLE_API_KEY=your_key_here
   GOOGLE_CSE_ID=your_cx_id_here
   ```

## Workflow

... (rest of file)

## Example Usage

```bash
GOOGLE_API_KEY=xxx GOOGLE_CSE_ID=yyy python3 skills/google-search/scripts/search.py "Skill平台 documentation"
```

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
