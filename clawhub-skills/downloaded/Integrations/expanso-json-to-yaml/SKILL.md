---
slug: expanso-json-to-yaml
name: expanso-json-to-yaml
version: "1.0.0"
displayName: Expanso json-to-yaml
summary: Convert JSON input into YAML format using Expanso Edge pipelines for CLI
  or MCP server integration.
license: MIT
description: |-
  Convert JSON input into YAML format using Expanso Edge pipelines for
  CLI or MCP server integration.

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: yaml, json-to-yaml, convert, input, expanso, json
tags:
- Integrations
tools:
- read
- exec
---

# Expanso json-to-yaml

Convert JSON to YAML format

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
expanso-cli job deploy https://skills.expanso.io/json-to-yaml/pipeline-cli.yaml
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
