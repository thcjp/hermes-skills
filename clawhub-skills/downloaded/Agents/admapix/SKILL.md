---
slug: admapix
name: admapix
version: "1.0.30"
displayName: AdMapix
summary: AdMapix raw data layer for ad creatives, apps, rankings, downloads/revenue.
license: MIT
description: |-
  AdMapix raw data layer for ad creatives, apps, rankings, downloads/revenue.

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: apps, admapix, data, creatives, layer
tags:
- Agents
- Creative
- Research
tools:
- read
- exec
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
