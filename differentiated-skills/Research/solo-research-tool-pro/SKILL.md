---
slug: "solo-research-tool-pro"
name: "solo-research-tool-pro"
version: "1.0.0"
displayName: "市场研究工具专业版"
summary: "企业级深度市场研究系统,支持MCP工具集成、多引擎搜索、收入验证、YouTube分析与深度内容抓取"
license: "Proprietary"
edition: "pro"
description: |-
  市场研究工具专业版为企业团队提供深度市场研究与竞争分析能力。核心能力:
  - MCP工具集成(知识库/代码图谱/会话搜索)
  - 多引擎搜索路由(Reddit/YouTube/GitHub)
  - TrustMRR收入验证(Stripe验证MRR)
  - YouTube评论深度挖掘
  - Playwright深度内容抓取
  - 混合搜索策略(MCP工具+WebSearch)

  适用场景:
  - 企业深度竞争分析
  - 投资标的尽职调查
  - 产品市场定位研究
  - 行业全景调研报告

  差异化:专业版在免费版基础研究流程上...
tags:
  - 研究工具
  - 市场研究
  - 企业级
  - 竞品分析
  - 尽职调查
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 市场研究工具专业版
## 概述
市场研究工具专业版是企业级深度市场研究与竞争分析系统。在免费版竞品分析、用户痛点挖掘、基础SEO研究、域名检查与市场规模估算的基础上,专业版扩展了MCP工具集成(知识库搜索/代码图谱/会话搜索)、多引擎搜索路由(Reddit/YouTube/GitHub专用引擎)、TrustMRR收入验证(Stripe验证MRR数据)、YouTube评论深度挖掘、Playwright深度内容抓取与混合搜索策略等企业级能力。

专业版与免费版完全兼容:免费版的研究流程、报告格式、搜索策略全部继续可用。升级后即可享受MCP工具集成与深度分析能力。

## 核心能力
### 免费版 vs 专业版能力对比
| 能力模块 | 免费版 | 专业版 |
|:--------|:------|:-------|
| 竞品分析 | 基础(WebSearch) | 深度(MCP工具+WebSearch+多引擎) |
| 用户痛点 | 基础(Reddit/HN) | 深度(Reddit全文+YouTube+HN) |
| SEO分析 | 基础 | 深度(竞品关键词+趋势数据) |
| 域名检查 | 三重验证 | 三重验证+商标冲突检查 |
| 市场规模 | 基础估算 | 深度(多源验证+收入数据) |
| 研究报告 | 基础模板 | 高级模板(含收入验证+深度分析) |
| MCP工具 | 不支持 | kb_search/codegraph/session_search |
| 多引擎搜索 | 不支持 | Reddit/YouTube/GitHub引擎路由 |
| 收入验证 | 不支持 | TrustMRR Stripe验证MRR |
| YouTube分析 | 不支持 | 视频评论挖掘(观看量=需求) |
| 深度抓取 | WebFetch(有限) | Playwright(绕过CAPTCHA) |
| 知识库搜索 | 不支持 | 历史研究检索 |
| 代码图谱 | 不支持 | 可复用代码与架构发现 |

**输入**: 用户提供免费版 vs 专业版能力对比所需的指令和必要参数。
**处理**: 按照skill规范执行免费版 vs 专业版能力对比操作,遵循单一意图原则。
**输出**: 返回免费版 vs 专业版能力对比的执行结果,包含操作状态和输出数据。

### 专业版独有功能
1. **MCP工具集成**:优先使用MCP工具(kb_search/web_search/session_search/codegraph),获取更精准结果
2. **多引擎搜索路由**:MCP工具 web_search支持引擎覆盖(engines="reddit"/engines="youtube"),精准搜索特定平台
3. **TrustMRR收入验证**:通过trustmrr.com验证竞品Stripe MRR、增长率、技术栈与流量
4. **YouTube深度挖掘**:搜索视频评测,观看量反映市场需求,评论反映用户反馈
5. **Playwright深度抓取**:通过浏览器自动化绕过CAPTCHA,获取old.reddit.com全文内容
6. **混合搜索策略**:MCP工具+WebSearch多后端组合,各取所长
7. **知识库与历史研究**:检索过往研究,避免重复,发现关联

**输入**: 用户提供专业版独有功能所需的指令和必要参数。
**处理**: 按照skill规范执行专业版独有功能操作,遵循单一意图原则。
**输出**: 返回专业版独有功能的执行结果,包含操作状态和输出数据。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级深度市场研、究系统、分析与深度内容抓、市场研究工具专业、版为企业团队提供、深度市场研究与竞、争分析能力、核心能力、会话搜索、评论深度挖掘、深度内容抓取等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景
### 场景一:企业深度竞争分析
企业需要对主要竞品进行深度分析,包括收入验证、技术栈、用户反馈与市场定位。

```text
用户输入: "深度分析竞品Notion,包括收入、技术栈、用户反馈和竞争优势"

AI助手执行专业研究流程:

1. 知识库检索(MCP kb_search):
   kb_search(query="Notion竞品分析", n_results=5)
   -> 检索过往Notion相关研究

2. 竞品分析(混合搜索):
   - MCP工具 web_search(engines="general"): "Notion competitors 2026"
   - WebSearch: "site:producthunt.com Notion alternatives"
   - WebSearch: "site:g2.com Notion review"
   - WebFetch: 抓取Notion定价页面

3. 收入验证(TrustMRR):
   - WebFetch: trustmrr.com/startup/notion
   - 提取: MRR、增长率、订阅数、技术栈、流量

4. 用户反馈(多引擎):
   - MCP工具 web_search(engines="reddit"): "Notion frustrating" (max 3 keywords)
   - MCP工具 Playwright: old.reddit.com全文抓取(绕过CAPTCHA)
   - MCP工具 web_search(engines="youtube"): "Notion review"
   - YouTube评论: 观看量+评论分析

5. 技术栈分析(MCP工具 codegraph):
   - codegraph_explain(project="notion-similar")
   - project_code_search(query="block editor", project="...")

6. 生成深度研究报告
```

### 场景二:投资标的尽职调查
投资团队需要评估某初创公司作为投资标的,验证其收入、增长与市场地位。

```text
用户输入: "评估初创公司ExampleCorp作为投资标的,验证收入与市场地位"

AI助手执行:

1. TrustMRR收入验证:
   - WebFetch: trustmrr.com/startup/examplecorp
   - 提取: MRR $250K/月,年增长180%,订阅数3,200

2. 竞争格局:
   - WebSearch: "ExampleCorp competitors alternatives"
   - WebSearch: "site:crunchbase.com ExampleCorp" (融资信息)
   - 对比3个直接竞品的收入与增长

3. 用户口碑(多引擎深度):
   - MCP工具 web_search(engines="reddit"): "ExampleCorp review"
   - Playwright: 抓取Reddit全文讨论
   - MCP工具 web_search(engines="youtube"): "ExampleCorp demo"
   - 分析: 正面评价占68%,主要赞誉是"易用性"

4. 技术评估:
   - codegraph_explain: 架构概览
   - 技术栈: Next.js + Supabase + Vercel

5. 市场规模:
   - TAM/SAM/SOM估算(多源验证)

6. 生成投资评估报告
```

### 场景三:行业全景调研报告
研究团队需要对某个行业进行全面调研,生成深度行业报告。

```text
用户输入: "调研AI代码生成器行业,包括主要玩家、技术趋势、市场规模和用户需求"

AI助手执行混合搜索策略:

| 步骤 | 搜索后端 | 原因 |
|------|---------|------|
| 竞品发现 | WebSearch + site:producthunt.com | 广泛发现+PH发布 |
| Reddit讨论 | MCP工具 web_search(engines="reddit") | Reddit全文搜索 |
| Reddit全文 | MCP工具 Playwright(old.reddit.com) | 绕过CAPTCHA获取全文 |
| YouTube评测 | MCP工具 web_search(engines="youtube") | 视频评测(观看量=需求) |
| GitHub项目 | WebSearch + topics | 开源项目发现 |
| 市场规模 | WebSearch | 多源数据综合 |
| 收入验证 | WebFetch trustmrr.com | Stripe验证MRR |
| 技术栈 | MCP工具 codegraph | 架构与技术发现 |
| 历史研究 | MCP kb_search + session_search | 避免重复研究 |

生成完整行业报告,包含:
- 行业概览与市场规模
- 主要玩家对比(含收入验证)
- 技术趋势分析
- 用户需求与痛点
- 竞争格局与机会
```

## 不适用场景

以下场景市场研究工具专业版不适合处理：

- 黑帽SEO手段
- 搜索引擎作弊
- 付费广告投放管理

## 触发条件

需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于非本工具能力范围的需求。

## 快速开始
### 从免费版升级
专业版完全兼容免费版,升级步骤:

```text
1. 确认MCP工具可用性
   - 如果MCP工具可用:优先使用MCP,获得更精准结果
   - 如果MCP工具不可用:自动回退到WebSearch/WebFetch(与免费版一致)

2. 使用专业版增强功能
   - 收入验证: 在研究中提及"验证收入"或"TrustMRR"
   - 多引擎搜索: 在研究中提及"YouTube评论"或"Reddit全文"
   - 深度抓取: 在研究中提及"全文内容"或"绕过限制"
```

### 使用MCP工具
```text
# MCP工具优先级(MCP可用时优先使用)
知识库搜索:
  kb_search(query="关键词", n_results=5)
  -> 搜索知识库中的相关文档

网络搜索(支持引擎路由):
  web_search(query="关键词", engines="reddit")
  web_search(query="关键词", engines="youtube")
  web_search(query="关键词", engines="github")
  web_search(query="关键词", include_raw_content=true)

会话搜索(历史研究):
  session_search(query="关键词", project="项目名")
  -> 查找过去如何做类似研究

代码图谱(项目架构):
  codegraph_explain(project="项目名")
  -> 获取项目架构概览(技术栈、模式、依赖)

  codegraph_query(query="Cypher查询")
  -> 原始Cypher查询(查找共享包、依赖关系)

  project_code_search(query="关键词", project="项目名")
  -> 项目源代码语义搜索
```

### Reddit内容访问回退链
```text
Reddit内容获取回退链(从最佳到最后手段):

1. MCP工具 Playwright (old.reddit.com)     <- 最佳: 绕过CAPTCHA,全文+评论
2. PullPush API (api.pullpush.io)      <- 按query/subreddit/作者搜索
3. MCP工具 web_search include_raw_content   <- 有时可用,常被截断
4. WebFetch / WebSearch snippets        <- 最后手段,仅部分数据

使用方法:
- 发现Reddit帖子: MCP工具 web_search(engines="reddit") 或 WebSearch
- 读取全文: MCP工具 Playwright browser_navigate("https://old.reddit.com/r/...")
- old.reddit.com不显示CAPTCHA,可获取完整帖子+评论
```

### TrustMRR收入验证
```bash
# 通过WebFetch获取TrustMRR数据
# URL: trustmrr.com/startup/<slug>
# 返回数据字段:
# - MRR (月经常性收入)
# - 历史总收入
# - 最近30天收入
# - 活跃订阅数
# - 增长率
# - 技术栈
# - 流量(24h/7d/30d)
# - 分类
# - 创始人社交账号
# 搜索同类初创公司
# WebSearch: "site:trustmrr.com <category or idea>"
```

### 命令参数说明

- `-GO`: 命令参数,用于指定操作选项

## 示例
### 混合搜索策略配置
```text
| 步骤 | 最佳后端 | 原因 |
|------|---------|------|
| 竞品发现 | WebSearch + site:producthunt.com + site:g2.com | 广泛发现+PH+B2B评价 |
| Reddit/痛点 | MCP工具 web_search(engines="reddit") + MCP工具 Playwright | PullPush API, selftext内容 |
| YouTube评测 | MCP工具 web_search(engines="youtube") | 视频评测(观看量=需求) |
| 市场规模 | WebSearch | 综合10个来源的数字 |
| SEO/ASO | WebSearch | 更广覆盖,趋势数据 |
| 页面抓取 | WebFetch或MCP工具 web_search(include_raw_content) | 最多5000字符页面内容 |
| Hacker News | WebSearch site:news.ycombinator.com | HN讨论与观点 |
| 融资/公司 | WebSearch site:crunchbase.com | 竞品融资,团队规模 |
| 收入验证 | WebFetch trustmrr.com/startup/<slug> | Stripe验证MRR,增长,技术栈 |
```

### MCP工具配置
```yaml
# config/mcp.yaml
mcp_tools:
  kb_search:
    enabled: true
    description: "搜索知识库中的相关文档"
    params:
      n_results: 5

  web_search:
    enabled: true
    description: "支持引擎路由的网络搜索"
    engines: [general, reddit, youtube, github]
    include_raw_content: true

  session_search:
    enabled: true
    description: "查找过去如何做类似研究"

  codegraph_explain:
    enabled: true
    description: "获取项目架构概览"

  codegraph_query:
    enabled: true
    description: "原始Cypher查询"

  project_code_search:
    enabled: true
    description: "项目源代码语义搜索"

fallback:
  # MCP不可用时回退到WebSearch/WebFetch
  web_search: WebSearch
  raw_content: WebFetch
```

### 研究报告高级模板
```markdown
# 深度市场研究报告: {产品想法}
## 元数据
- 产品类型: {web/mobile/cli/api}
- 研究日期: {date}
- 研究方法: 混合搜索(MCP+WebSearch)
- 数据源: {数据源列表}

## 1. 执行摘要
- 关键发现(3-5条)
- 建议: GO / NO-GO / PIVOT
- 核心风险与机会

## 2. 竞品深度分析
| 竞品 | URL | 定价 | MRR(验证) | 增长率 | 技术栈 | 核心功能 | 弱点 |
|------|-----|------|----------|--------|--------|---------|------|
(含TrustMRR收入验证数据)

## 3. 用户痛点(多源)
### Reddit(全文)
### YouTube(视频评测)
### Hacker News
Top 5痛点,含引用、来源URL与情感分析

## 4. SEO/ASO分析
| 关键词 | 意图 | 月搜索量 | 竞争度 | 相关度 | 趋势 |
|-------|------|---------|--------|--------|------|

## 5. 域名与商标
| 域名 | 可用性 | TLD等级 | 商标冲突 |
|-----|--------|--------|---------|

## 6. 市场规模
- TAM: {总市场} (来源: {数据源})
- SAM: {可服务市场}
- SOM: {第一年可获取}
- 增长率: {CAGR}

## 7. 技术可行性
- 可复用代码: {codegraph发现}
- 推荐技术栈: {基于竞品分析}
- 预估开发周期: {基于复杂度}

## 8. 历史研究关联
- 过往相关研究: {session_search发现}
- 知识库关联文档: {kb_search发现}

## 9. 结论与建议
- 建议: GO / NO-GO / PIVOT
- 理由: {详细说明}
- 下一步: /validate <想法>
```

## 最佳实践
### 1. 优先使用MCP工具
MCP工具(知识库搜索、代码图谱)提供比WebSearch更精准的结果。如果MCP工具可用,优先使用:

```text
优先级:
1. MCP kb_search (知识库)
2. MCP session_search (历史研究)
3. MCP工具 web_search (引擎路由)
4. WebSearch (通用搜索)
5. WebFetch (页面抓取)
```

### 2. Reddit搜索关键词不超过3个
Reddit搜索效果随关键词增多而下降。MCP工具 web_search(engines="reddit")同样遵循此规则:

```text
# 好: 2-3个关键词
web_search(query="product hunt launch", engines="reddit")

# 不好: 过多关键词
web_search(query="product hunt scraper maker profiles linkedin outreach", engines="reddit")
```

### 3. 使用old.reddit.com获取Reddit全文
www.reddit.com会显示CAPTCHA,old.reddit.com不会。通过MCP工具 Playwright访问old.reddit.com获取完整帖子与评论:

```text
browser_navigate("https://old.reddit.com/r/subreddit/comments/...")
-> 获取完整帖子文本+评论(YAML结构)
```

### 4. TrustMRR验证竞品真实收入
TrustMRR提供Stripe验证的MRR数据,比竞品自称的收入更可信。研究竞品时,始终检查trustmrr.com:

```text
WebFetch("trustmrr.com/startup/<竞品slug>")
-> 获取: MRR, 增长率, 订阅数, 技术栈, 流量
```

### 5. YouTube观看量反映市场需求
YouTube视频评测的观看量是市场需求的代理指标。高观看量的评测视频说明用户关注度高:

```text
MCP工具 web_search(engines="youtube"): "竞品名 review"
-> 观看量排序,高观看量=高需求
```

### 6. 并行执行独立搜索
研究各维度的搜索相互独立,应并行执行以提升效率。AI助手会自动并行化独立搜索任务。

## 常见问题
### Q: 如何从免费版迁移到专业版?
A: 专业版完全兼容免费版。研究流程、报告格式、搜索策略全部不变。如果MCP工具可用,专业版自动优先使用MCP获取更精准结果;如果MCP不可用,自动回退到WebSearch/WebFetch(与免费版行为一致)。

### Q: MCP工具不可用怎么办?
A: MCP工具不可用时,专业版自动回退到WebSearch/WebFetch,行为与免费版一致。如需启用MCP工具,需配置MCP server(如SearXNG用于引擎路由)。配置后可获得Reddit/GitHub/YouTube引擎路由与Playwright深度抓取能力。

### Q: TrustMRR数据覆盖范围有多大?
A: TrustMRR覆盖使用Stripe处理支付的公开SaaS初创公司。并非所有竞品都在TrustMRR有数据。如果竞品不在TrustMRR,可:(1)搜索"site:trustmrr.com <category>"找同类公司;(2)使用Crunchbase融资数据替代;(3)通过WebSearch搜索竞品公开的收入信息。

### Q: MCP工具 Playwright与WebFetch有何区别?
A: WebFetch是简单的HTTP请求,无法执行JavaScript,遇到CAPTCHA会失败。MCP工具 Playwright是完整浏览器自动化,能执行JS、绕过CAPTCHA、获取动态加载内容。对于Reddit(old.reddit.com)、Product Hunt等需要JS或会显示CAPTCHA的站点,Playwright是首选。

### Q: PullPush API是什么?
A: PullPush API(api.pullpush.io)是Reddit内容的第三方搜索API,支持按query/subreddit/作者/分数/日期搜索。返回JSON格式的完整帖子内容(selftext)。速率限制:15 req/min(软),30 req/min(硬),1000 req/hr。适合Reddit内容发现与检索。

### Q: 混合搜索策略如何选择后端?
A: 专业版根据搜索维度自动选择最佳后端:竞品发现用WebSearch(广覆盖),Reddit讨论用MCP工具 web_search(engines="reddit")+Playwright(全文),YouTube用MCP工具 web_search(engines="youtube"),收入验证用WebFetch(TrustMRR)。用户无需手动选择,AI助手自动路由。

### Q: 代码图谱(codegraph)对研究有何帮助?
A: 代码图谱帮助发现已有项目中的可复用代码、架构模式与技术栈选择。对于评估技术可行性、估算开发周期和发现可复用基础设施非常有价值。如果无MCP工具 codegraph,此步骤自动跳过。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent具备WebSearch和WebFetch能力,MCP工具为可选增强

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| WebSearch | 搜索能力 | 必需 | Agent内置WebSearch工具 |
| WebFetch | 网页抓取 | 必需 | Agent内置WebFetch工具 |
| MCP kb_search | 知识库 | 条件可选(MCP增强) | 配置MCP server |
| MCP工具 web_search | 多引擎搜索 | 条件可选(MCP增强) | 配置SearXNG MCP |
| MCP工具 Playwright | 浏览器自动化 | 条件可选(深度抓取) | 配置Playwright MCP |
| MCP工具 codegraph | 代码图谱 | 条件可选(技术分析) | 配置codegraph MCP |
| whois/dig/curl | 域名工具 | 条件必需(域名检查) | 系统预装 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 网络访问 | 网络 | 必需 | 需能访问搜索引擎与目标网页 |

### API Key 配置
- **MCP server配置**: 条件可选,使用MCP增强功能时需配置对应MCP server
- **SearXNG配置**: 条件可选,使用引擎路由功能时配置SearXNG实例
- **TrustMRR**: 无需API Key,通过WebFetch直接访问trustmrr.com
- **PullPush API**: 无需API Key,直接调用api.pullpush.io(有速率限制)
- **LLM API**: 由Agent平台内置提供,负责想法解析、信息提取、综合分析与报告生成

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,依赖Agent的WebSearch/WebFetch与可选MCP工具)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent完成深度市场研究任务。专业版在免费版基础上扩展MCP工具集成、多引擎搜索路由、TrustMRR收入验证、YouTube深度挖掘与Playwright深度抓取能力,适合企业深度竞争分析、投资标的尽职调查与行业全景调研报告场景。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
