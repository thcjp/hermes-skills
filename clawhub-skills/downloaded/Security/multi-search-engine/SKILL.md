---
slug: multi-search-engine
name: multi-search-engine
version: "2.1.3"
displayName: Multi Search Engine
summary: Multi search engine integration with 16 engines (7 CN + 9 Global).
license: MIT
description: |-
  Multi search engine integration with 16 engines (7 CN + 9 Global).

  核心能力:

  - 安全工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 安全审计、漏洞扫描、加密保护

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: integration, multi, engine, search
tags:
- Security
- Integrations
tools:
- read
- exec
---

# Multi Search Engine

Integration of 16 search engines for web crawling without API keys.

## Workflow

1. **Preparation**: AI Agent initializes an empty in-memory cookie store. Cookies are only acquired dynamically during search operations when access is denied
2. **Language Evaluation**: Detect the language attribute of the search query. If the query is in Chinese, use Domestic search engines (Baidu, Bing CN, Bing INT, 360, Sogou, WeChat, Shenma). If the query is non-Chinese, use International search engines (Google, Google HK, DuckDuckGo, Yahoo, Startpage, Brave, Ecosia, Qwant, WolframAlpha). Select engines based on query relevance and availability.
3. **Controlled Search**: Use web_fetch to execute search requests with rate limiting:

   * Add 1-2 second delay between requests to respect server load
   * Batch requests in groups of 3-4 engines with sequential execution between batches
   * Include standard browser headers to identify as legitimate user agent
   * If access is denied (403/429), fetch engine homepage to obtain fresh session cookies
4. **Cookie Management**:

   * Cookies are stored ONLY in memory during runtime
   * Cookies are acquired on-demand when search requests fail
   * No cookies are read from or written to config.json or any file
   * Cookies are cleared after search session completes
   * Only session cookies from search engine domains are captured
5. **Retry Mechanism**: If a search fails due to cookie/session issues, retry once with freshly acquired cookies after a 2-second delay
6. **Result Aggregation**: Consolidate successful results from search engines, organize and summarize them to output a core search report

## Search Engines

### Domestic (7)

* **Baidu**: `https://www.baidu.com/s?wd={keyword}`
* **Bing CN**: `https://cn.bing.com/search?q={keyword}&ensearch=0`
* **Bing INT**: `https://cn.bing.com/search?q={keyword}&ensearch=1`
* **360**: `https://www.so.com/s?q={keyword}`
* **Sogou**: `https://sogou.com/web?query={keyword}`
* **WeChat**: `https://wx.sogou.com/weixin?type=2&query={keyword}`
* **Shenma**: `https://m.sm.cn/s?q={keyword}`

### International (9)

* **Google**: `https://www.google.com/search?q={keyword}`
* **Google HK**: `https://www.google.com.hk/search?q={keyword}`
* **DuckDuckGo**: `https://duckduckgo.com/html/?q={keyword}`
* **Yahoo**: `https://search.yahoo.com/search?p={keyword}`
* **Startpage**: `https://www.startpage.com/sp/search?query={keyword}`
* **Brave**: `https://search.brave.com/search?q={keyword}`
* **Ecosia**: `https://www.ecosia.org/search?q={keyword}`
* **Qwant**: `https://www.qwant.com/?q={keyword}`
* **WolframAlpha**: `https://www.wolframalpha.com/input?i={keyword}`

## Quick Examples

```javascript
// Basic search
web_fetch({"url": "https://www.google.com/search?q=python+tutorial"})

// Site-specific
web_fetch({"url": "https://www.google.com/search?q=site:github.com+react"})

// File type
web_fetch({"url": "https://www.google.com/search?q=machine+learning+filetype:pdf"})

// Time filter (past week)
web_fetch({"url": "https://www.google.com/search?q=ai+news&tbs=qdr:w"})

// Privacy search
web_fetch({"url": "https://duckduckgo.com/html/?q=privacy+tools"})

// DuckDuckGo Bangs
web_fetch({"url": "https://duckduckgo.com/html/?q=!gh+tensorflow"})

// Knowledge calculation
web_fetch({"url": "https://www.wolframalpha.com/input?i=100+USD+to+CNY"})
```

## Advanced Operators

| Operator | Example | Description |
| --- | --- | --- |
| `site:` | `site:github.com python` | Search within site |
| `filetype:` | `filetype:pdf report` | Specific file type |
| `""` | `"machine learning"` | Exact match |
| `-` | `python -snake` | Exclude term |
| `OR` | `cat OR dog` | Either term |

## Time Filters

| Parameter | Description |
| --- | --- |
| `tbs=qdr:h` | Past hour |
| `tbs=qdr:d` | Past day |
| `tbs=qdr:w` | Past week |
| `tbs=qdr:m` | Past month |
| `tbs=qdr:y` | Past year |

## Privacy Engines

* **DuckDuckGo**: No tracking
* **Startpage**: Google results + privacy
* **Brave**: Independent index
* **Qwant**: EU GDPR compliant

## Bangs Shortcuts (DuckDuckGo)

| Bang | Destination |
| --- | --- |
| `!g` | Google |
| `!gh` | GitHub |
| `!so` | Stack Overflow |
| `!w` | Wikipedia |
| `!yt` | YouTube |

## WolframAlpha Queries

* Math: `integrate x^2 dx`
* Conversion: `100 USD to CNY`
* Stocks: `AAPL stock`
* Weather: `weather in Beijing`

## Documentation

* `references/advanced-search.md` - Domestic search guide
* `references/international-search.md` - International search guide
* `CHANGELOG.md` - Version history

## License

MIT

## Security & Privacy Notice

### Cookie Handling

* **Purpose**: Cookies are used ONLY to maintain search session state when access is denied (403/429 errors)
* **Storage**: Cookies are kept STRICTLY in memory during runtime - NEVER persisted to disk or config files
* **Acquisition**: Cookies are acquired on-demand from search engine homepages only when search requests fail
* **Scope**: Only session cookies from the specific search engine domain are captured
* **Lifecycle**: Cookies are cleared immediately after the search session completes
* **No Pre-configuration**: No cookies are loaded from config.json or any external file at startup
* **No API Keys**: This tool uses standard web search URLs, no authentication required

### Crawling Ethics

* **Rate Limiting**: Implement reasonable delays between requests (recommend 1-2 seconds)
* **Respect robots.txt**: Honor search engine crawling policies
* **Terms of Service**: Users are responsible for complying with search engine ToS
* **Purpose**: Designed for legitimate search aggregation, not mass data scraping

### Data Handling

* **No Personal Data**: Tool does not collect or transmit user personal information
* **Local Execution**: All operations run locally, no external data transmission
* **Session Isolation**: Cookies are session-specific and cleared after use

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
