---
slug: agent-browser-clawdbot
name: agent-browser-clawdbot
version: "0.1.0"
displayName: Agent Browser
summary: Headless browser automation CLI optimized for AI agents with accessibility
  tree snapshots and ref...
license: MIT
description: |-
  Headless browser automation CLI optimized for AI agents with accessibility
  tree snapshots and ref...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: automation, browser, clawdbot, optimized, headless, agent, agents
tags:
- Research
- Automation
tools:
- read
- exec
---

# Agent Browser

Fast browser automation using accessibility tree snapshots with refs for deterministic element selection.

## Why Use This Over Built-in Browser Tool

**Use agent-browser when:**

* Automating multi-step workflows
* Need deterministic element selection
* Performance is critical
* Working with complex SPAs
* Need session isolation

**Use built-in browser tool when:**

* Need screenshots/PDFs for analysis
* Visual inspection required
* Browser extension integration needed

## Core Workflow

```bash
agent-browser open https://example.com
agent-browser snapshot -i --json

agent-browser click @e2
agent-browser fill @e3 "text"

agent-browser snapshot -i --json
```

## Key Commands

### Navigation

```bash
agent-browser open <url>
agent-browser back | forward | reload | close
```

### Snapshot (Always use -i --json)

```bash
agent-browser snapshot -i --json          # Interactive elements, JSON output
agent-browser snapshot -i -c -d 5 --json  # + compact, depth limit
agent-browser snapshot -s "#main" -i      # Scope to selector
```

### Interactions (Ref-based)

```bash
agent-browser click @e2
agent-browser fill @e3 "text"
agent-browser type @e3 "text"
agent-browser hover @e4
agent-browser check @e5 | uncheck @e5
agent-browser select @e6 "value"
agent-browser press "Enter"
agent-browser scroll down 500
agent-browser drag @e7 @e8
```

### Get Information

```bash
agent-browser get text @e1 --json
agent-browser get html @e2 --json
agent-browser get value @e3 --json
agent-browser get attr @e4 "href" --json
agent-browser get title --json
agent-browser get url --json
agent-browser get count ".item" --json
```

### Check State

```bash
agent-browser is visible @e2 --json
agent-browser is enabled @e3 --json
agent-browser is checked @e4 --json
```

### Wait

```bash
agent-browser wait @e2                    # Wait for element
agent-browser wait 1000                   # Wait ms
agent-browser wait --text "Welcome"       # Wait for text
agent-browser wait --url "**/dashboard"   # Wait for URL
agent-browser wait --load networkidle     # Wait for network
agent-browser wait --fn "window.ready === true"
```

### Sessions (Isolated Browsers)

```bash
agent-browser --session admin open site.com
agent-browser --session user open site.com
agent-browser session list
```

### State Persistence

```bash
agent-browser state save auth.json        # Save cookies/storage
agent-browser state load auth.json        # Load (skip login)
```

### Screenshots & PDFs

```bash
agent-browser screenshot page.png
agent-browser screenshot --full page.png
agent-browser pdf page.pdf
```

### Network Control

```bash
agent-browser network route "**/ads/*" --abort           # Block
agent-browser network route "**/api/*" --body '{"x":1}'  # Mock
agent-browser network requests --filter api              # View
```

### Cookies & Storage

```bash
agent-browser cookies                     # Get all
agent-browser cookies set name value
agent-browser storage local key           # Get localStorage
agent-browser storage local set key val
```

### Tabs & Frames

```bash
agent-browser tab new https://example.com
agent-browser tab 2                       # Switch to tab
agent-browser frame @e5                   # Switch to iframe
agent-browser frame main                  # Back to main
```

## Snapshot Output Format

```json
{
  "success": true,
  "data": {
    "snapshot": "...",
    "refs": {
      "e1": {"role": "heading", "name": "Example Domain"},
      "e2": {"role": "button", "name": "Submit"},
      "e3": {"role": "textbox", "name": "Email"}
    }
  }
}
```

## Best Practices

1. **Always use `-i` flag** - Focus on interactive elements
2. **Always use `--json`** - Easier to parse
3. **Wait for stability** - `agent-browser wait --load networkidle`
4. **Save auth state** - Skip login flows with `state save/load`
5. **Use sessions** - Isolate different browser contexts
6. **Use `--headed` for debugging** - See what's happening

## Example: Search and Extract

```bash
agent-browser open https://www.google.com
agent-browser snapshot -i --json
agent-browser fill @e1 "AI agents"
agent-browser press Enter
agent-browser wait --load networkidle
agent-browser snapshot -i --json
agent-browser get text @e3 --json
agent-browser get attr @e4 "href" --json
```

## Example: Multi-Session Testing

```bash
agent-browser --session admin open app.com
agent-browser --session admin state load admin-auth.json
agent-browser --session admin snapshot -i --json

agent-browser --session user open app.com
agent-browser --session user state load user-auth.json
agent-browser --session user snapshot -i --json
```

## Installation

```bash
npm install -g agent-browser
agent-browser install                     # Download Chromium
agent-browser install --with-deps         # Linux: + system deps
```

## Credits

Skill created by Yossi Elkrief ([@MaTriXy](https://github.com/MaTriXy))

agent-browser CLI by [Vercel Labs](https://github.com/vercel-labs/agent-browser)

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
