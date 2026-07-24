---

slug: "openai-ai"
name: "openai-ai"
version: 1.0.7
displayName: "llm-provider"
summary: "管OpenAI文件/助手/向量库/批次/微调/模型资源。Manage llm-provider files, assistants, vector stores, batches, fine"
license: "Proprietary"
description: |-
  Manage llm-provider files, assistants, vector stores, batches, fine-tuning
  jobs, and model resources vi。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策.
tags: 工作流,llm-provider,bash,clawlink_call_tool,model,按流程执
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"

---

# llm-provider

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

- Manage llm-provider files, assistants, vector stores, batches, fine-tuning
  jobs, and model resources vi
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文件操作 | 文件路径与操作参数 | 操作结果与文件元信息 |
| 模型调用 | 输入文本与模型参数 | 模型输出与用量统计 |
| 管OpenAI文件 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

```bash
clawlink_call_tool --tool "openai_list_assistants" --params '{"limit": 10}'
# ...
clawlink_call_tool --tool "openai_create_chat_completion" --params '{"model": "gpt-4o", "messages": [{"role": "user", "content": "Hello"}]}'
# ...
clawlink_call_tool --tool "openai_list_files" --params '{"purpose": "batch"}'
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | openai-ai处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "ai_result": "ai_result_value",
      "ai_metadata": "ai_metadata_value",
      "ai_status": "ai_status_value"
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

中间产物模板参考: `assets/openai-ai_template`

## 错误处理
| Status / Error | Meaning |
|:-------------:|:-------------:|
| Tool not found | The tool name does not exist in the current catalog. Verify with `clawlink_list_tools --integration llm-provider`. |
| Missing connection | llm-provider is not connected. Direct the user to <https://claw-link.dev/dashboard?add=llm-provider>. |
| `invalid_request_error` | Invalid parameter or model not available. Verify model ID with `openai_list_models`. |
| `RateLimitError` | Too many requests. Wait and retry with exponential backoff. |
| `authentication_error` | Invalid API key. Reconnect llm-provider at the dashboard. |
| Write rejected | User did not confirm a write action. Always confirm before executing writes. |

### 错误恢复步骤
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
> **处理方式**: 参考上表中的错误场景说明,按照对应建议进行处理和恢复.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(ai-assistant Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
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
# ...
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

## 已知限制

- 需要API Key，无Key环境无法使用
- 
