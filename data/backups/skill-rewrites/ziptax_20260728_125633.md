---
slug: ziptax
name: ziptax
version: "1.0.0"
displayName: Ziptax Sales Tax
summary: "销售税查询(其脚本可本地运行需谨慎)(社区下载版)"
  script can run local...
license: MIT
description: |-
  This sales-tax lookup skill is legitimate in purpose, but its bundled
  lookup script can run local。Use when 用户需要Ziptax Sales Tax相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags:
- Development
tools:
  - - read
- exec
pricing_tier: "L2"
pricing_model: "per_use"
suggested_price: 19.9
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

- This sales-tax lookup skill is legitimate in purpose, but its bundled
  lookup script can run local
- 触发关键词: tax, ziptax, legitimate, sales, lookup, skill

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
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
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Ziptax Sales Tax？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Ziptax Sales Tax有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 本地运行，不支持多设备同步
