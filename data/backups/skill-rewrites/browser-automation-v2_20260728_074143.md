---
slug: browser-automation-v2
name: browser-automation-v2
version: "2.0.0"
displayName: Browser Automation V
summary: "企业级浏览器自动化:自动标签清理、超时重试、并发锁,保障长时间任务稳定运行"
  concurrency lock...
license: MIT
description: |-
  Enterprise-grade browser automation with automatic tab cleanup, timeout
  retries, concurrency lock。Use when 需要营销推广、广告投放、获客转化、增长裂变时使用。不适用于非法营销手段。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Research
- Automation
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Browser Automation V2

Enterprise-grade browser automation for Skill平台 with robust resource management.

## Features

* ✅ **Automatic tab cleanup** - No more tab accumulation
* ✅ **Timeout & retry** - Exponential backoff on network errors
* ✅ **Smart waiting** - `waitForLoadState`, `waitForSelector`
* ✅ **Concurrency lock** - Prevents profile conflicts
* ✅ **Structured logging** - DEBUG=1 for verbose output
* ✅ **Configurable** - Environment variables for timeout, retries, profile

## Files

* `browser-manager.v2.js` - Core manager class
* `search-google.js` - Google search with screenshot + PDF
* `fetch-summary.js` - Fetch page content (static or dynamic)
* `multi-pages.js` - Batch process multiple URLs
* `fill-form.js` - Auto-fill forms by field names

## Usage

```bash
export BROWSER_PROFILE=skill-platform
export BROWSER_TIMEOUT=30000
export BROWSER_RETRIES=2
export DEBUG=1

cd ~/.skill-platform/workspace/skills/browser-automation-v2

node search-google.js "Skill平台 automation"

node multi-pages.js "https://example.com" "https://github.com"

node fill-form.js "https://example.com/form" '{"email":"test@xx.com"}'
```

## Integration

Register as Skill平台 skill:

```bash
skill-platform skills install ~/.skill-platform/workspace/skills/browser-automation-v2
```

Or call directly from agent:

```text
run search-google.js "query"
```

## Requirements

* Skill平台 v2026.2.15+
* Browser profile configured (default: `skill-platform`)
* Gateway running

## Troubleshooting

* **Timeout errors**: Increase `BROWSER_TIMEOUT`
* **Profile locked**: Wait for other instance to finish
* **Element not found**: Use `snapshot --format ai` to debug refs

---

*Created: 2026-02-16*
*Version: 2.0.0*
*License: MIT*

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

## 常见问题

### Q1: 如何开始使用Browser Automation V？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Browser Automation V有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
