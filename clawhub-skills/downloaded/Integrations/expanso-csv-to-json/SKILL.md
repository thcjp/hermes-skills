---
slug: expanso-csv-to-json
name: expanso-csv-to-json
version: "1.0.0"
displayName: Expanso csv-to-json
summary: Convert CSV input into a JSON array of objects using Expanso Edge CLI or
  MCP pipelines.
license: MIT
description: |-
  Convert CSV input into a JSON array of objects using Expanso Edge CLI
  or MCP pipelines.

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: convert, json, array, csv, csv-to-json, expanso, input
tags:
- Integrations
tools:
- read
- exec
---

# Expanso csv-to-json

"Convert CSV data to JSON array of objects"

## Requirements

* Expanso Edge installed (`expanso-edge` binary in PATH)
* Install via: `* 安装此Skill请参考SkillHub平台指南

## Usage

### CLI Pipeline

```bash
echo '<input>' | expanso-edge run pipeline-cli.yaml
```

### MCP Pipeline

```bash
expanso-edge run pipeline-mcp.yaml
```

### Deploy to Expanso Cloud

```bash
expanso-cli job deploy https://skills.expanso.io/csv-to-json/pipeline-cli.yaml
```

## Files

| File | Purpose |
| --- | --- |
| `skill.yaml` | Skill metadata (inputs, outputs, credentials) |
| `pipeline-cli.yaml` | Standalone CLI pipeline |
| `pipeline-mcp.yaml` | MCP server pipeline |

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
