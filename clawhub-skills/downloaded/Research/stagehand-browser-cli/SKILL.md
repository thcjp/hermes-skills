---
slug: stagehand-browser-cli
name: stagehand-browser-cli
version: "1.0.0"
displayName: Stagehand Browser CLI
summary: Automate web browser interactions using natural language via CLI commands.
  Use when the user asks...
license: MIT
description: |-
  Automate web browser interactions using natural language via CLI commands.
  Use when the user asks...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: interactions, using, browser, stagehand, natural, automate, cli
tags:
- Research
- Automation
tools:
- read
- exec
---

# Stagehand Browser CLI

Automate browser interactions using Stagehand CLI with Claude.

### First: Environment Selection (Local vs Remote)

The skill automatically selects between local and remote browser environments:

* **If Browserbase API keys exist** (BROWSERBASE_API_KEY and BROWSERBASE_PROJECT_ID in .env file): Uses remote Browserbase environment
* **If no Browserbase API keys**: Falls back to local Chrome browser
* **No user prompting**: The selection happens automatically based on available configuration

## Setup (First Time Only)

Check `setup.json` in this directory. If `setupComplete: false`:

```bash
npm install    # Install dependencies
npm link       # Create global 'browser' command
```

## Commands

All commands work identically in both modes:

```bash
browser navigate <url>                    # Go to URL
browser act "<action>"                    # Natural language action
browser extract "<instruction>" ['{}']    # Extract data (optional schema)
browser observe "<query>"                 # Discover elements
browser screenshot                        # Take screenshot
browser close                             # Close browser
```

## Quick Example

```bash
browser navigate https://example.com
browser act "click the Sign In button"
browser extract "get the page title"
browser close
```

## Mode Comparison

| Feature | Local | Browserbase |
| --- | --- | --- |
| Speed | Faster | Slightly slower |
| Setup | Chrome required | API key required |
| Stealth mode | No | Yes |
| Proxy/CAPTCHA | No | Yes |
| Best for | Development | Production/scraping |

## Best Practices

1. **Always navigate first** before interacting
2. **View screenshots** after each command to verify
3. **Be specific** in action descriptions
4. **Close browser** when done

## Troubleshooting

* **Chrome not found**: Install Chrome or use Browserbase mode
* **Action fails**: Use `browser observe` to discover available elements
* **Browserbase fails**: Verify API key and project ID are set

For detailed examples, see [EXAMPLES.md](/api/v1/skills/stagehand-browser-cli/file?path=EXAMPLES.md&ownerHandle=peytoncasper).
For API reference, see [REFERENCE.md](/api/v1/skills/stagehand-browser-cli/file?path=REFERENCE.md&ownerHandle=peytoncasper).

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
