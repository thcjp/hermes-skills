---
slug: key-guard
name: key-guard
version: "1.0.1"
displayName: Key Guard
  \  ## Why This Exists  When Claude reads a file containing an API key, the raw key\
  \ content gets sent to Claude's servers. key-guard prevents this by acting as a\
  \ local middleman â\x80\x94 Claude calls a tool, the tool reads the key and makes\
  \ the API call locally, and only the result is returned to Claude."
summary: "Security guardrail: prevents API keys from being sent to ai-assistant. Triggers
  when user asks to call"
license: MIT-0
description: |-
  Security guardrail: prevents API keys from being sent to ai-assistant。Triggers
  when user asks to call。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags: '[''Integrations'']'
tools:
  - read
  - exec
---

# # key-guard  A local MCP server that keeps API keys off ai-assistant's servers.  ## Why This Exists  When ai-assistant reads a file containing an API key, the raw key content gets sent to ai-assistant's servers. key-guard prevents this by acting as a local middleman â ai-assistant calls a tool, the tool reads the key and makes the API call locally, and only the result is returned to ai-assistant.

A security skill that ensures API keys stay local and are never sent to ai-assistant.

## When This Skill Applies

Activate whenever the user wants to:

* Call an external API (llm-provider, DeepL, Oxford Dictionary, etc.)
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

Make an authenticated HTTP request locally. The key is injected by the MCP server — ai-assistant only sees the API response.

```text
Call: call_api({
  key_name: "OPENAI_API_KEY",
  url: "https://api.llm-provider.com/v1/models",
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
  content: "curl -H 'Authorization: Bearer {{OPENAI_API_KEY}}' https://api.llm-provider.com/v1/chat/completions ..."
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

## 示例

### User: "Is my llm-provider key set up?"

```text
1. Call validate_key({ key_name: "OPENAI_API_KEY" })
2. Report back: "Yes, your key is set (51 chars, starts with sk-a****)"
```

### User: "Call the llm-provider API to get word definitions"

```text
1. Call call_api({
     key_name: "OPENAI_API_KEY",
     url: "https://api.llm-provider.com/v1/chat/completions",
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
   → ai-assistant sees "curl -H 'Authorization: Bearer {{OPENAI_API_KEY}}' ..."
2. Make the requested edit to the non-key parts
3. Call write_file_with_keys({ file_path: "./call.sh", content: "<edited content with {{OPENAI_API_KEY}} still in place>" })
   → MCP substitutes the real key before writing to disk
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
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

- Security guardrail: prevents API keys from being sent to ai-assistant
- Triggers
  when user asks to call
- 触发关键词: exists, local, mcp, ai-assistant, raw, why, when, sent

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Key Guard？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Key Guard有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
