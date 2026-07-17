---
slug: web-browsing
name: web-browsing
version: "1.0.0"
displayName: Web Browsing
summary: Browse and summarize websites, extract content from URLs, search the web
  for information. Use whe...
license: MIT-0
description: |-
  Browse and summarize websites, extract content from URLs, search the
  web for information. Use whe...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: web, websites, browsing, summarize, content, browse, extract
tags:
- Research
tools:
- read
- exec
---

# Web Browsing

This skill enables browsing websites, extracting content from URLs, and searching the web for information.

## When to Use

**Use this skill when:**

* User asks you to visit a website (e.g., "Check out example.com")
* User wants webpage content summarized
* User needs current information that requires internet search
* User provides a URL and wants it analyzed
* User asks to search for something online

## How It Works

### 1. Direct URL Access

When given a specific URL:

```markdown
User: "What's on https://example.com?"
→ Visit the page, extract main content, summarize key points
```

### 2. Web Search

When user asks to search:

```markdown
User: "Find information about climate change"
→ Perform web search, present top results with summaries
```

### 3. Content Extraction

For specific data extraction:

```markdown
User: "Get the latest news from techcrunch.com"
→ Navigate to site, extract relevant articles/headlines
```

## Tools Available

* **web_search**: Search the web for information
* **fetch_url**: Visit and retrieve webpage content
* **extract_content**: Parse HTML and extract structured data

## Best Practices

1. **Be specific** - Tell me what you want from the page (summary, specific data, latest news)
2. **Provide URLs** - If you have a specific page, share the URL directly
3. **Clarify intent** - Let me know if you need:
   * Quick summary
   * Detailed analysis
   * Specific data points
   * Latest updates

## Examples

```markdown
✅ "Visit https://news.ycombinator.com and summarize today's top stories"
✅ "Search for the latest React.js tutorial"
✅ "Check what's on Wikipedia's page about quantum computing"
✅ "Find pricing information from apple.com/iphone"
❌ Just say "browse the web" - be more specific!
```

## Limitations

* Cannot interact with JavaScript-heavy sites (may miss dynamic content)
* Some sites block automated access
* Video/audio content cannot be played, only described if available
* Login-required pages won't work without credentials

---

**Ready to browse!** Just give me a URL or tell me what to search for. 🌐

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
