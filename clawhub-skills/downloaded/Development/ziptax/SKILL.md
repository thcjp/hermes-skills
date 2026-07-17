---
slug: ziptax
name: ziptax
version: "1.0.0"
displayName: Ziptax Sales Tax
summary: This sales-tax lookup skill is legitimate in purpose, but its bundled lookup
  script can run local...
license: MIT
description: |-
  This sales-tax lookup skill is legitimate in purpose, but its bundled
  lookup script can run local...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: tax, ziptax, legitimate, sales, lookup, skill
tags:
- Development
tools:
- read
- exec
---

# Ziptax Sales Tax

## Setup

Set `ZIPTAX_API_KEY` env variable with your API key from <https://platform.zip.tax> (DEVELOP > API Keys).
Free tier gives 100 calls/month. **Never share your API key publicly.**

## Quick Start

### Address Lookup (most accurate)

```bash
curl -s "https://api.zip-tax.com/request/v60?address=200+Spectrum+Center+Drive+Irvine+CA+92618" \
  -H "X-API-KEY: $ZIPTAX_API_KEY"
```

### Postal Code Lookup

```bash
curl -s "https://api.zip-tax.com/request/v60?postalcode=92618" \
  -H "X-API-KEY: $ZIPTAX_API_KEY"
```

### Lat/Lng Lookup

```bash
curl -s "https://api.zip-tax.com/request/v60?lat=33.6525&lng=-117.7479" \
  -H "X-API-KEY: $ZIPTAX_API_KEY"
```

## Workflow

1. Determine lookup type: address (best), lat/lng, or postal code
2. Use **v60** (latest) for full jurisdiction breakdowns; use v10 for simple combined rate
3. Make GET request to `https://api.zip-tax.com/request/v60` with auth header
4. Check `metadata.response.code` — 100 means success
5. Read `taxSummaries[0].rate` for total sales tax rate
6. Read `baseRates` array for state/county/city/district breakdown
7. Check `service.taxable` and `shipping.taxable` for service/freight taxability

## Key Points

* **Address > Postal code**: Address gives one exact result; postal code returns all rates in that ZIP
* **Auth**: Header `X-API-KEY` or query param `key`
* **Rate format**: Decimal (0.0775 = 7.75%)
* **Response code 100** = success; check `metadata.response.code`
* **Metrics endpoint** (`/account/metrics`) does not count against quota

## Bundled Resources

* **`scripts/lookup.sh`** — CLI wrapper for quick lookups. Run with `--address`, `--lat`/`--lng`, `--postalcode`, or `--metrics`
* **`references/api-reference.md`** — Full API reference with all endpoints, response schemas, code samples, response codes, and SDK links. Read when you need endpoint details or response field definitions.

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
