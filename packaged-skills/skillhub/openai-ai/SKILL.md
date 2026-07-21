---
slug: openai-ai
name: openai-ai
version: "1.0.6"
displayName: llm-provider
summary: Manage llm-provider files, assistants, vector stores, batches, fine-tuning jobs,
  and model resources vi...
license: MIT-0
description: |-
  Manage llm-provider files, assistants, vector stores, batches, fine-tuning
  jobs, and model resources vi。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Creative
tools:
  - - read
- exec
---
# llm-provider

## 核心能力

- Manage llm-provider files, assistants, vector stores, batches, fine-tuning
  jobs, and model resources vi
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Use、模型调用、智能对话、Agent、应用时使用、不适用于需要、确定性的关键决策。这些能力在上述核心功能中均有对应处理逻辑。
### 领域术语

本skill涉及以下领域术语: `english`, `asynchronous`, `jsonl`, `permissions`, `openai_create_fine_tuning_job`, `safedefaults`, `pair`, `openai_get_eval`, `openai_list_vector_stores`, `openai_list_run_steps`, `edit`, `responses`, `openai_delete_assistant`, `overview`, `openai_create_embeddings`

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

```bash
clawlink_call_tool --tool "openai_list_assistants" --params '{"limit": 10}'

clawlink_call_tool --tool "openai_create_chat_completion" --params '{"model": "gpt-4o", "messages": [{"role": "user", "content": "Hello"}]}'

clawlink_call_tool --tool "openai_list_files" --params '{"purpose": "batch"}'
```

### 命令参数说明

1. `-e-3`: 命令参数,用于指定操作选项
2. `--strict-json`: 命令参数,用于指定操作选项
3. `--params`: 命令参数,用于指定操作选项
4. `-platform`: 命令参数,用于指定操作选项

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| mode | string | 否 | 处理模式, 可选: json/text/markdown, 默认: 默认值 |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明",
      （根据实际场景填充）: "相关说明"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/（根据实际场景填充）`

## 异常处理

| Status / Error | Meaning |
| --- | --- |
| Tool not found | The tool name does not exist in the current catalog. Verify with `clawlink_list_tools --integration llm-provider`. |
| Missing connection | llm-provider is not connected. Direct the user to <https://claw-link.dev/dashboard?add=llm-provider>. |
| `invalid_request_error` | Invalid parameter or model not available. Verify model ID with `openai_list_models`. |
| `RateLimitError` | Too many requests. Wait and retry with exponential backoff. |
| `authentication_error` | Invalid API key. Reconnect llm-provider at the dashboard. |
| Write rejected | User did not confirm a write action. Always confirm before executing writes. |

### 错误处理

1. Check that the ClawLink plugin is installed:

   bash

   ```
   skill-platform plugins list
   ```
2. If the plugin is installed but tools are missing, tell the user to send `/new` as a standalone message to reload the catalog.
3. If a fresh chat does not help, run:

   bash

   ```
   skill-platform config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
   skill-platform gateway restart
   ```
4. After restart, tell the user to send `/new` again and retry.

### Troubleshooting: Invalid Tool Call

1. Ensure the integration slug is exactly `llm-provider`.
2. Use `clawlink_describe_tool` to verify parameter names and types before calling.
3. For write operations, always call `clawlink_preview_tool` first.

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### Create a chat completion

```bash
clawlink_call_tool --tool "openai_create_chat_completion" \
  --params '{
    "model": "gpt-4o",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Explain quantum computing in simple terms."}
    ],
    "max_tokens": 500
  }'
```

### Create an assistant

```bash
clawlink_call_tool --tool "openai_create_assistant" \
  --params '{
    "name": "Code Reviewer",
    "model": "gpt-4o",
    "instructions": "You review code and suggest improvements.",
    "tools": [{"type": "code_interpreter"}]
  }'
```

### Upload a file and create a vector store

```bash
clawlink_call_tool --tool "openai_upload_file" \
  --params '{
    "file": "@./knowledge.pdf",
    "purpose": "assistants"
  }'

clawlink_call_tool --tool "openai_create_vector_store_file" \
  --params '{
    "vector_store_id": "VS_ID",
    "file_id": "FILE_ID"
  }'
```

### Create a batch job

```bash
clawlink_call_tool --tool "openai_create_batch" \
  --params '{
    "input_file_id": "FILE_ID",
    "endpoint": "chat/completions",
    "model": "gpt-4o-mini",
    "completion_window": "24h"
  }'
```

### Generate an image

```bash
clawlink_call_tool --tool "openai_create_image" \
  --params '{
    "model": "dall-e-3",
    "prompt": "A minimalist diagram showing the Skill平台 to ClawLink to Provider flow",
    "size": "1024x1024",
    "n": 1
  }'
```

## 常见问题

### Q1: 如何开始使用OpenAI？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: OpenAI有什么限制？
A: 

## 已知限制

- 需要API Key，无Key环境无法使用
- 
