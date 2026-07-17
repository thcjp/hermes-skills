---
slug: browser-automation-v2
name: browser-automation-v2
version: "2.0.0"
displayName: Browser Automation V2
summary: Enterprise-grade browser automation with automatic tab cleanup, timeout retries,
  concurrency lock...
license: MIT
description: |-
  Enterprise-grade browser automation with automatic tab cleanup, timeout
  retries, concurrency lock...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: grade, automation, enterprise, browser
tags:
- Research
- Automation
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
