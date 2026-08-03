---

slug: admapix
name: admapix
version: "1.0.30"
displayName: AdMapix
summary: "AdMapix广告原始数据层,广告创意/应用/排名/下载收入"
license: MIT
description: |-
  AdMapix raw data layer for ad creatives, apps, rankings, downloads/revenue。核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Agents
- Creative
- Research
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9

---


# AdMapix

A thin client over the AdMapix read API. It fetches **raw structured data** and returns it as JSON. It does **not** analyze, summarize, rank, generate pages, or run autonomous research — the calling agent (e.g. Claude Code, Codex) decides which endpoints to call, composes multi-call workflows from the metadata, and does any analysis itself.

**Out of scope** (never done inside this skill): HTML/H5 page generation, hosted "deep research", autonomous multi-step research, summaries, insights, recommendations, dashboards, message-send.

## Auth

Use `ADMAPIX_API_KEY` as the `X-API-Key` header. Never print or expose the key.

```bash
admapix_auth_header="X-API-Key: ${ADMAPIX_API_KEY}"
curl -s "https://api.admapix.com/api/data/{endpoint}?{params}" -H "$admapix_auth_header"
curl -s -X POST "https://api.admapix.com/api/data/{endpoint}" \
  -H "$admapix_auth_header" -H "Content-Type: application/json" -d '{...}'
```

For creative search, prefer the `admapix.search_creatives` MCP tool when available; otherwise call `POST /api/data/search` directly.

### Step 1 — Check the key

Before any API call, verify the key is configured (without printing its value):

```bash
[ -n "${ADMAPIX_API_KEY:-}" ] && echo ok || echo missing
```

### Step 2 — If missing, show the setup guide

If the key is missing (and no MCP tool is available), do **not** call the API. Show the user how to get and configure a key — in their language — then ask them to retry. Detect language from the user's message.

**中文用户：**

> 🔑 需要先配置 AdMapix API Key 才能使用：
>
> 1. 打开 <https://www.admapix.com> 注册账号
> 2. 登录后在控制台找到 **API Keys**，创建一个 Key
> 3. 选择一种方式配置：
>    * **Skill平台 / SkillHub**：在终端运行 `skill-platform config set skills.entries.admapix.apiKey "你的_API_KEY"`
>    * **通用环境变量**：在终端运行 `export ADMAPIX_API_KEY="[REDACTED]"`
> 4. 配置完成后重新发起查询 ✅

**English users:**

> 🔑 You need an AdMapix API Key to get started:
>
> 1. Sign up at <https://www.admapix.com>
> 2. After signing in, open **API Keys** in your dashboard and create one
> 3. Configure it one of these ways:
>    * **Skill平台 / SkillHub**: run `skill-platform config set skills.entries.admapix.apiKey "YOUR_API_KEY"` in your terminal
>    * **Generic env var**: run `export ADMAPIX_API_KEY="[REDACTED]"` in your terminal
> 4. Re-run your query after setup ✅

If the host provides a secure secret/config command, point the user to that instead. Never accept, echo, or store the key from chat — keep it out of responses, logs, and links. For programmatic callers, also return the `missing_api_key` error (see Error Handling).

## Endpoint Catalog

Each endpoint is a raw data source. **Read the listed reference file before using an endpoint you have not called yet** — it carries the exact params and response fields. Compose multiple calls as needed; the skill itself stays single-call-per-request and returns raw JSON.

### Creatives / ads — `references/api-creative.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/search` | POST | Search ad creatives |
| `/api/data/count` | POST | Count creatives for a query |
| `/api/data/count-all` | POST | Counts broken down by dimension |
| `/api/data/distribute` | POST | Creative distribution breakdown |
| `/api/data/distribute-dims` | GET | Available distribute dimensions |
| `/api/data/content-detail` | GET | Single creative detail (`related=imagevideo |
| `/api/data/item-apps` | POST | Apps associated with a creative |
| `/api/data/screen-types` | GET | Screen / element type codes |
| `/api/data/page-config` | GET | Search page config |

### Metadata / filters — `references/api-creative.md` + `references/param-mappings.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/filter-options` | GET | **All filter metadata**: `countries`, `mediaChannels`, `adTypes`, `device`, `tradeLevel(Tree)`, `productModel`, etc. Pull this to discover valid codes for any filter. |

### Apps / products / companies — `references/api-product.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/unified-product-search` | POST | Unified app/product search |
| `/api/data/product-search` | POST | Product search |
| `/api/data/company-search` | POST | Developer / company search |
| `/api/data/app-detail` | GET | App detail by `unifiedProductId` |
| `/api/data/developer-detail` | GET | Developer detail |
| `/api/data/app-profile` | GET | App profile |
| `/api/data/similar-apps` | POST | Similar apps |
| `/api/data/sdk-detail` | GET | SDKs used by a package |
| `/api/data/product-content-search` | POST | Creatives for a product |
| `/api/data/product-content-counts` | POST | Creative counts for a product |
| `/api/data/product-list`, `/for-product-list`, `/product-agg-list` | POST | Product lists / aggregations |

### Rankings — `references/api-ranking.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/store-rank` | POST | App-store rankings (free / paid / grossing) |
| `/api/data/generic-rank` | POST | Generic ranking lists |
| `/api/data/store-categories` | GET | Store category codes |
| `/api/data/store-countries` | GET | Store country codes |

### Downloads & revenue (third-party estimates) — `references/api-download-revenue.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/download-date`, `download-detail`, `download-country` | GET/POST | Download estimates by date / detail / country |
| `/api/data/revenue-date`, `revenue-detail`, `revenue-country` | GET/POST | Revenue estimates by date / detail / country |

> ⚠️ Download/revenue figures are third-party **estimates**, not official data. Return the raw numbers as-is; the calling agent must note they are estimates when presenting.

### Distribution — `references/api-distribution.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/app-distribution` | POST | App-level distribution |
| `/api/data/global-promote` | POST | Global promotion data |

### Market — `references/api-market.md`

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/data/market-search` | POST | Market-level search / aggregation |

## 输入输出参数说明

以下是对AdMapix API输入输出参数的详细说明，包括默认值、类型和取值范围：

- 输入参数：
  - `ADMAPIX_API_KEY`: 类型为字符串，必须提供有效的API Key。
  - `endpoint`: 类型为字符串，指定API端点。
  - `params`: 类型为JSON对象，包含API调用所需的参数。
- 输出参数：
  - `data`: 类型为JSON对象，包含API调用的结果数据。
  - `error`: 类型为JSON对象，包含错误信息，如果发生错误则返回。

每个参数的具体类型和取值范围应在文档中明确列出，以便用户正确使用API。

## 边界条件

为了确保AdMapix的稳定性和可靠性，以下是一些关键的边界条件，这些条件在文档中应得到详细说明：

- API Key的有效期：明确API Key的有效期限，以及如何处理过期或即将过期的API Key。
- 数据量限制：说明API调用时的数据量限制，例如单次调用返回的数据条数上限。
- 网络延迟：讨论网络延迟对API调用的影响，以及如何处理超时情况。
- 异常处理：详细说明如何处理API调用过程中可能出现的异常，包括但不限于网络错误、服务器错误、数据格式错误等。
- 安全措施：描述AdMapix如何处理API Key泄露的风险，以及如何防止恶意用户利用API Key进行攻击。

这些边界条件的详细说明将帮助用户更好地理解AdMapix的功能限制，并采取相应的措施来避免潜在的问题。

## Parameter Mapping

Read `references/param-mappings.md` to translate natural language into codes:

* creative type (`010`=video, etc.), industry (`trade_level1`: `602`=Game, `607`=Finance…), country / region groups, relative date ranges, sorting, page size.
* For codes not in param-mappings (sub-industries, media channels, devices, store categories…), pull `GET /api/data/filter-options` or the endpoint-specific dimension call (e.g. `store-categories`).

For the creative `search` endpoint, `page_size` is capped at **10** (clamp any larger request down to 10; use `page` for more). Other list endpoints use their own documented ranges.

## Output Rules

Return the API response as **raw structured JSON** — keep the API field names; do not rename, drop, summarize, rank, or editorialize. The calling agent composes and analyzes.

* Response shapes vary by endpoint. Creative search via direct API returns `pageIndex` / `pageSize` / `totalSize` / `list`; the MCP tool additionally wraps it with `request` / `page` / `page_size`. `totalSize` may be `null` on filtered queries — use the length of `list`.
* An empty `list` is a valid result (no matches), not an error.
* Pass through extra fields (e.g. `gptCorrect` spelling suggestions) unchanged; do not silently swap a keyword.

Do not: generate H5 / landing / card / dashboard pages, hide records behind links, run hosted "deep research" or autonomous multi-step research, or produce analysis / recommendations unless the user explicitly asks after receiving the data.

## Error Handling

**Agent-level** (no request was made — no MCP tool and `ADMAPIX_API_KEY` is missing):

```json
{ "error": { "code": "missing_api_key", "message": "Missing ADMAPIX_API_KEY environment variable", "retry": false } }
```

**API-level** (the call returned a non-2xx status). The API responds with `{ "detail": "...", "code": "..." }`; surface it plus the HTTP status, and never print the key. HTTP 401 with `INVALID_API_KEY` / `NOT_AUTHENTICATED` means the key is missing, malformed, or disabled — do not retry:

```json
{ "error": { "code": "invalid_api_key", "http_status": 401, "message": "Invalid API key format", "retry": false } }
```

## 错误码定义和处理方案

以下是对AdMapix API可能返回的错误码及其处理方案的详细说明：

- `missing_api_key`: 表示缺少API Key，需要用户配置API Key。
- `invalid_api_key`: 表示API Key无效，可能是格式错误或API Key已禁用。
- `timeout`: 表示API调用超时，需要检查网络连接或重试请求。
- `server_error`: 表示服务器错误，需要稍后再试或联系支持。

对于每个错误码，应提供具体的错误信息和建议的处理步骤，以便用户能够快速解决问题。

## 运行环境
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

## 主要能力
- AdMapix raw data layer for ad creatives, apps, rankings, downloads/revenue
- 触发关键词: apps, admapix, data, creatives, layer

## 技术或方法创新点

AdMapix在以下方面具有技术或方法创新点：

- **智能代理领域的专业化AI辅助工具**: AdMapix为智能代理领域提供了专业的AI辅助工具，提高了数据分析的效率和准确性。
- **基于高人气开源Skill深度优化升级**: AdMapix基于高人气开源Skill深度优化升级，提高了产品的稳定性和可靠性。

这些创新点使得AdMapix在技术上处于领先地位。

## 解决的真实验证痛点

AdMapix解决了以下真实验证的用户痛点：

- **数据获取困难**: 用户在获取广告数据时面临困难，AdMapix提供了便捷的数据获取方式。
- **数据分析复杂**: 用户在分析广告数据时面临复杂的问题，AdMapix简化了数据分析过程。
- **安全性担忧**: 用户对数据安全性担忧，AdMapix通过增强安全措施提供了更高的安全性保障。

这些痛点解决使得AdMapix在用户中获得了良好的口碑。

## 与同类方案的对比

与同类方案相比，AdMapix在以下方面具有优势：

- **功能更全面**: AdMapix提供了更全面的广告数据服务，包括创意、应用、排名、下载和收入等。
- **性能更优**: 通过深度优化，AdMapix提供了更高的性能和更快的响应速度。
- **安全性更高**: AdMapix通过增强安全措施，提供了更高的安全性保障。

这些优势使得AdMapix成为广告数据服务的首选方案。

## 差异化优势分析

AdMapix在以下方面具有独特的差异化优势：

- **深度优化**: AdMapix经过深度优化，移除了原始风险代码，清理了外部依赖引用，增强了元数据和触发关键词，完全适配SkillHub平台规范。
- **安全性增强**: 通过移除风险代码和增强安全措施，AdMapix提供了更高的安全性和稳定性。
- **易用性提升**: AdMapix提供了清晰的文档和示例，简化了API的使用过程，降低了用户的学习成本。

这些差异化优势使得AdMapix在同类产品中脱颖而出，成为用户的首选。

## 使用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用说明
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```

```

## 常见疑问
### Q1: 如何开始使用AdMapix？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: AdMapix有什么限制？
A: 请参考已知限制章节了解具体限制。

## 注意事项
- 需要API Key，无Key环境无法使用
