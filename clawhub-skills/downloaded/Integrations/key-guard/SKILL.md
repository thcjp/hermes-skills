---
slug: key-guard
name: key-guard
version: "1.0.1"
displayName: "# key-guard  A local MCP server that keeps API keys off Claude's servers.\
  \  ## Why This Exists  When Claude reads a file containing an API key, the raw key\
  \ content gets sent to Claude's servers. key-guard prevents this by acting as a\
  \ local middleman â\x80\x94 Claude calls a tool, the tool reads the key and makes\
  \ the API call locally, and only the result is returned to Claude."
summary: "Security guardrail: prevents API keys from being sent to Claude. Triggers
  when user asks to call"
license: MIT-0
description: |-
  Security guardrail: prevents API keys from being sent to Claude. Triggers
  when user asks to call ...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: exists, local, mcp, claude, raw, why, when, sent
tags: '[''Integrations'']'
tools: '[read, exec]'
---

# # key-guard  A local MCP server that keeps API keys off Claude's servers.  ## Why This Exists  When Claude reads a file containing an API key, the raw key content gets sent to Claude's servers. key-guard prevents this by acting as a local middleman â Claude calls a tool, the tool reads the key and makes the API call locally, and only the result is returned to Claude.

A security skill that ensures API keys stay local and are never sent to Claude.

## When This Skill Applies

Activate whenever the user wants to:

* Call an external API (OpenAI, DeepL, Oxford Dictionary, etc.)
* Check if an API key is configured
* Read `.env`, `*.key`, `secrets.*`, or any credentials file
* View or edit a script (`.sh`, `.bash`, curl commands, config files) that may contain a hardcoded API key
* Debug why an API call is failing

## Rules (ALWAYS follow these)

1. **NEVER read `.env` or key files directly** — do not use bash `cat .env` or file read tools on any file containing keys
2. **NEVER read script or config files directly** if they might contain hardcoded API keys — use `read_file_masked` instead
3. **NEVER include a key value in your response**, even partially
4. **ALWAYS use the `key-guard` MCP server** for anything key-related

## How to Use the MCP Server

The `key-guard` MCP server exposes five tools:

### Tool 1: `list_keys`

Discover all available key names — never values.

```text
Call: list_keys()
Returns: { keys: ["KEY_A", "KEY_B", "KEY_C"] }
```

### Tool 2: `validate_key`

Check if a key is configured without seeing it.

```text
Call: validate_key({ key_name: "OPENAI_API_KEY" })
Returns: { exists: true, length: 51, preview: "sk-a****", message: "Key is set" }
```

### Tool 2: `call_api`

Make an authenticated HTTP request locally. The key is injected by the MCP server — Claude only sees the API response.

```text
Call: call_api({
  key_name: "OPENAI_API_KEY",
  url: "https://api.openai.com/v1/models",
  method: "GET"
})
Returns: { status: 200, data: { ... API response ... } }
```

### Tool 3: `read_file_masked`

Read a script or config file with all key values replaced by `{{KEY_NAME}}` placeholders. Use this instead of reading files directly.

```text
Call: read_file_masked({ file_path: "./call.sh" })
Returns: {
  content: "curl -H 'Authorization: Bearer {{OPENAI_API_KEY}}' https://..."
}
```

You can now safely view and suggest edits to the non-key parts.

### Tool 4: `write_file_with_keys`

Write a file back after editing, with `{{KEY_NAME}}` placeholders substituted with real key values locally.

```text
Call: write_file_with_keys({
  file_path: "./call.sh",
  content: "curl -H 'Authorization: Bearer {{OPENAI_API_KEY}}' https://api.openai.com/v1/chat/completions ..."
})
Returns: { success: true, message: "File written with keys substituted locally" }
```

## Setup Instructions (tell the user if MCP is not running)

If the MCP server hasn't been registered yet:

```bash
git clone https://github.com/your-username/key-guard.git

cp .env.example .env

/mcp add key-guard node /path/to/key-guard/key-guard.js

```

## Example Workflows

### User: "Is my OpenAI key set up?"

```text
1. Call validate_key({ key_name: "OPENAI_API_KEY" })
2. Report back: "Yes, your key is set (51 chars, starts with sk-a****)"
```

### User: "Call the OpenAI API to get word definitions"

```text
1. Call call_api({
     key_name: "OPENAI_API_KEY",
     url: "https://api.openai.com/v1/chat/completions",
     method: "POST",
     body: { model: "gpt-4o-mini", messages: [...] }
   })
2. Use the returned response — never the key itself
```

### User: "Show me my .env file"

```text
Do NOT read .env directly.
Instead, call validate_key for each expected key name and show:
- Which keys are configured
- Approximate length (as a sanity check)
Never show actual values.
```

### User: "Edit my curl script to add a header"

```text
1. Call read_file_masked({ file_path: "./call.sh" })
   → Claude sees "curl -H 'Authorization: Bearer {{OPENAI_API_KEY}}' ..."
2. Make the requested edit to the non-key parts
3. Call write_file_with_keys({ file_path: "./call.sh", content: "<edited content with {{OPENAI_API_KEY}} still in place>" })
   → MCP substitutes the real key before writing to disk
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
