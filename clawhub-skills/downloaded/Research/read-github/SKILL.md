---
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
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

- This skill is mostly transparent about reading GitHub through gitmcp
- io,
  but it exposes broader r
- 触发关键词: read, about, transparent, github, mostly, skill

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

### Q1: 如何开始使用Read GitHub？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Read GitHub有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
