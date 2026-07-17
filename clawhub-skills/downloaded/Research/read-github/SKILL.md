---
slug: read-github
name: read-github
version: "1.0.1"
displayName: Read GitHub
summary: This skill is mostly transparent about reading GitHub through gitmcp.io,
  but it exposes broader r...
license: MIT
description: |-
  This skill is mostly transparent about reading GitHub through gitmcp.io,
  but it exposes broader r...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: read, about, transparent, github, mostly, skill
tags:
- Research
- Development
tools:
- read
- exec
---

# Read GitHub

Access GitHub repository documentation and code via the gitmcp.io MCP service.

## URL Conversion

Convert GitHub URLs to gitmcp.io:

* `github.com/owner/repo` → `gitmcp.io/owner/repo`
* `https://github.com/karpathy/llm-council` → `https://gitmcp.io/karpathy/llm-council`

## CLI Usage

The `scripts/gitmcp.py` script provides CLI access to repository docs.

### List Available Tools

```bash
python3 scripts/gitmcp.py list-tools owner/repo
```

### Fetch Documentation

Retrieves the full documentation file (README, docs, etc.):

```bash
python3 scripts/gitmcp.py fetch-docs owner/repo
```

### Search Documentation

Semantic search within repository documentation:

```bash
python3 scripts/gitmcp.py search-docs owner/repo "query"
```

### Search Code

Search code using GitHub Search API (exact match):

```bash
python3 scripts/gitmcp.py search-code owner/repo "function_name"
```

### Fetch Referenced URL

Fetch content from URLs mentioned in documentation:

```bash
python3 scripts/gitmcp.py fetch-url owner/repo "https://example.com/doc"
```

### Direct Tool Call

Call any MCP tool directly:

```bash
python3 scripts/gitmcp.py call owner/repo tool_name '{"arg": "value"}'
```

## Tool Names

Tool names are dynamically prefixed with the repo name (underscored):

* `karpathy/llm-council` → `fetch_llm_council_documentation`
* `facebook/react` → `fetch_react_documentation`
* `my-org/my-repo` → `fetch_my_repo_documentation`

## Available MCP Tools

For any repository, these tools are available:

1. **fetch_{repo}_documentation** - Fetch entire documentation. Call first for general questions.
2. **search_{repo}_documentation** - Semantic search within docs. Use for specific queries.
3. **search_{repo}_code** - Search code via GitHub API (exact match). Returns matching files.
4. **fetch_generic_url_content** - Fetch any URL referenced in docs, respecting robots.txt.

## Workflow

1. When given a GitHub repo, first fetch documentation to understand the project
2. Use search-docs for specific questions about usage or features
3. Use search-code to find implementations or specific functions
4. Use fetch-url to retrieve external references mentioned in docs

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
