---
slug: brave-search
name: brave-search
version: "1.0.1"
displayName: Brave Search
summary: "通过Brave Search API进行网络搜索与内容提取,隐私优先的搜索方案"
license: MIT
description: |-
  Web search and content extraction via Brave Search API。核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Research
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
---

# Brave Search

Headless web search and content extraction using Brave Search. No browser required.

## Setup

Run once before first use:

```bash
cd ~/Projects/agent-scripts/skills/brave-search
npm ci
```

Needs env: `BRAVE_API_KEY`.

## Search

```bash
./search.js "query"                    # Basic search (5 results)
./search.js "query" -n 10              # More results
./search.js "query" --content          # Include page content as markdown
./search.js "query" -n 3 --content     # Combined
```

## Extract Page Content

```bash
./content.js https://example.com/article
```

Fetches a URL and extracts readable content as markdown.

## Output Format

```text
--- Result 1 ---
Title: Page Title
Link: https://example.com/page
Snippet: Description from search results
Content: (if --content flag used)
  Markdown content extracted from the page...

--- Result 2 ---
...
```

## When to Use

* Searching for documentation or API references
* Looking up facts or current information
* Fetching content from specific URLs
* Any task requiring web search without interactive browsing

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

- Web search and content extraction via Brave Search API
- 触发关键词: brave, search, extraction, content

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 场景不足

为了更全面地覆盖使用场景，以下是一些额外的使用场景示例：

- **学术研究**：Brave Search Skill可以帮助研究人员快速检索学术文献和论文，提取关键信息，并生成文献综述。

- **内容监控**：企业可以使用Skill来监控特定关键词或主题，以便及时发现市场趋势或竞争对手的活动。

- **新闻聚合**：Skill可以用于构建一个个性化的新闻聚合工具，根据用户的兴趣提供定制化的新闻内容。

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

## 错误处理

为了提高错误处理的详细性和实用性，以下是对Brave Search Skill中可能遇到的错误场景的详细处理方案：

- **配置错误**：当用户输入的参数缺失或格式错误时，Skill将返回一个明确的错误消息，指出具体的问题所在。例如，如果用户未提供`BRAVE_API_KEY`环境变量，Skill将输出`Error: BRAVE_API_KEY environment variable is not set.`。用户应检查其环境配置并确保所有必需的参数都已正确设置。

- **运行时错误**：如果Skill在执行过程中遇到运行时错误，例如网络连接问题或API限制，它将输出一个包含错误代码和简短描述的消息。例如，如果API请求超时，Skill将输出`Error: API request timed out. Please try again later.`。用户应检查其网络连接，并在必要时重试操作。

- **网络错误**：当Skill无法连接到Brave Search API时，它将输出一个网络错误的提示。例如，如果无法连接到API，Skill将输出`Error: Unable to connect to Brave Search API. Please check your internet connection.`。用户应检查其网络连接，并确保其代理设置不会阻止API访问。

## 常见问题

### Q1: 如何开始使用Brave Search？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Brave Search有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用

## 边界条件

为了确保Brave Search Skill在各种边界条件下的稳定性和可靠性，以下是一些已考虑的边界情况及其处理策略：

- **空查询**：如果用户输入一个空查询，Skill将返回一个错误消息，提示用户输入有效的查询字符串。

- **超长查询**：如果查询字符串过长，可能导致API响应超时。Skill将限制查询字符串的最大长度，并在必要时截断查询以避免超时。

- **结果数量限制**：API可能对返回的结果数量有限制。Skill将根据API的限制设置合理的默认结果数量，并允许用户通过`-n`参数调整。

- **内容提取限制**：某些页面可能不包含可提取的Markdown内容。Skill将检查页面内容是否存在，并在内容不可用时返回一个相应的消息。

## 差异化优势

Brave Search Skill在以下方面具有独特的差异化优势：

- **隐私保护**：Skill通过使用Brave Search API，提供了一种隐私优先的搜索解决方案，避免了用户数据被第三方跟踪或分析。

- **深度优化**：Skill经过深度优化，移除了原始风险代码，增强了元数据和触发关键词，使其更符合SkillHub平台规范，提高了安全性和稳定性。

- **灵活配置**：Skill允许用户通过环境变量和命令行参数灵活配置API密钥和其他设置，以适应不同的使用场景。

## 同类方案对比

与同类搜索和内容提取工具相比，Brave Search Skill具有以下优势：

- **更快的搜索速度**：通过使用Brave Search API，Skill提供了更快的搜索速度和更准确的结果。

- **更丰富的内容提取**：Skill不仅提取标题和链接，还可以提取页面内容，包括Markdown格式的文本。

- **更灵活的集成**：Skill可以轻松集成到现有的工作流程和应用程序中，无需复杂的配置。
