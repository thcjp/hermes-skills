---
slug: javascript-sdk
name: javascript-sdk
version: "0.1.5"
displayName: Javascript Sdk
summary: "inference.sh的JS/TS SDK,跑AI应用/建Agent/集成150+模型(社区下载版)"
  150+ models. Pa...
license: MIT
description: |-
  JavaScript/TypeScript SDK for inference。sh - run AI apps, build agents,
  integrate 150+ models。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Development
tools:
  - - read
- exec
# Javascript Sdk
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

Build AI applications with the [inference.sh](https://inference.sh) JavaScript/TypeScript SDK.

## Quick Start
```bash
npm install @inferencesh/sdk
```

```typescript
import { inference } from '@inferencesh/sdk';

const client = inference({ apiKey: 'inf_your_key' });

// Run an AI app
const result = await client.run({
  app: 'infsh/flux-schnell',
  input: { prompt: 'A sunset over mountains' }
});
console.log(result.output);
```

## Installation
```bash
npm install @inferencesh/sdk
yarn add @inferencesh/sdk
pnpm add @inferencesh/sdk
```

**Requirements:** Node.js 18.0.0+ (or modern browser with fetch)

## Authentication
```typescript
import { inference } from '@inferencesh/sdk';

// Direct API key
const client = inference({ apiKey: 'inf_your_key' });

// From environment variable (recommended)
const client = inference({ apiKey: process.env.INFERENCE_API_KEY });

// For frontend apps (use proxy)
const client = inference({ proxyUrl: '/api/inference/proxy' });
```

Get your API key: Settings → API Keys → Create API Key

## Running Apps
### Basic Execution
```typescript
const result = await client.run({
  app: 'infsh/flux-schnell',
  input: { prompt: 'A cat astronaut' }
});

console.log(result.status);  // "completed"
console.log(result.output);  // Output data
```

### Fire and Forget
```typescript
const task = await client.run({
  app: 'google/veo-3-1-fast',
  input: { prompt: 'Drone flying over mountains' }
}, { wait: false });

console.log(`Task ID: ${task.id}`);
// Check later with client.getTask(task.id)
```

### Streaming Progress
```typescript
const stream = await client.run({
  app: 'google/veo-3-1-fast',
  input: { prompt: 'Ocean waves at sunset' }
}, { stream: true });

for await (const update of stream) {
  console.log(`Status: ${update.status}`);
  if (update.logs?.length) {
    console.log(update.logs.at(-1));
  }
}
```

### Run Parameters
| Parameter | Type | Description |
| --- | --- | --- |
| `app` | string | App ID (namespace/name@version) |
| `input` | object | Input matching app schema |
| `setup` | object | Hidden setup configuration |
| `infra` | string | 'cloud' or 'private' |
| `session` | string | Session ID for stateful execution |
| `session_timeout` | number | Idle timeout (1-3600 seconds) |

## File Handling
### Automatic Upload
```typescript
const result = await client.run({
  app: 'image-processor',
  input: {
    image: '/path/to/image.png'  // Auto-uploaded
  }
});
```

### Manual Upload

> 详细代码示例已移至 `references/detail.md`

### Browser File Upload
```typescript
const input = document.querySelector('input[type="file"]');
const file = await client.uploadFile(input.files[0]);
```

## Sessions (Stateful Execution)
Keep workers warm across multiple calls:

> 详细代码示例已移至 `references/detail.md`

## Agent SDK
### Template Agents
Use pre-built agents from your workspace:

> 详细代码示例已移至 `references/detail.md`

### Ad-hoc Agents
Create custom agents programmatically:

> 详细代码示例已移至 `references/detail.md`

### Available Core Apps
| Model | App Reference |
| --- | --- |
| Claude Sonnet 4 | `infsh/claude-sonnet-4@latest` |
| Claude 3.5 Haiku | `infsh/claude-haiku-35@latest` |
| GPT-4o | `infsh/gpt-4o@latest` |
| GPT-4o Mini | `infsh/gpt-4o-mini@latest` |

## Tool Builder API
### Parameter Types

> 详细代码示例已移至 `references/detail.md`

### Client Tools (Run in Your Code)
```typescript
const greet = tool('greet')
  .display('Greet User')
  .describe('Greets a user by name')
  .param('name', string('Name to greet'))
  .requireApproval()
  .build();
```

### App Tools (Call AI Apps)
```typescript
const generate = appTool('generate_image', 'infsh/flux-schnell@latest')
  .describe('Generate an image from text')
  .param('prompt', string('Image description'))
  .setup({ model: 'schnell' })
  .input({ steps: 20 })
  .requireApproval()
  .build();
```

### Agent Tools (Delegate to Sub-agents)
```typescript
import { agentTool } from '@inferencesh/sdk';

const researcher = agentTool('research', 'my-org/researcher@v1')
  .describe('Research a topic')
  .param('topic', string('Topic to research'))
  .build();
```

### Webhook Tools (Call External APIs)
```typescript
import { webhookTool } from '@inferencesh/sdk';

const notify = webhookTool('slack', 'https://hooks.slack.com/...')
  .describe('Send Slack notification')
  .secret('SLACK_SECRET')
  .param('channel', string('Channel'))
  .param('message', string('Message'))
  .build();
```

### Internal Tools (Built-in Capabilities)

> 详细代码示例已移至 `references/detail.md`

## Streaming Agent Responses
```typescript
const response = await agent.sendMessage('Explain quantum computing', {
  onMessage: (msg) => {
    if (msg.content) {
      process.stdout.write(msg.content);
    }
  },
  onToolCall: async (call) => {
    console.log(`\n[Tool: ${call.name}]`);
    const result = await executeTool(call.name, call.args);
    agent.submitToolResult(call.id, result);
  }
});
```

## File Attachments

> 详细代码示例已移至 `references/detail.md`

## Skills (Reusable Context)

> 详细代码示例已移至 `references/detail.md`

## Server Proxy (Frontend Apps)
For browser apps, proxy through your backend to keep API keys secure:

### Client Setup
```typescript
const client = inference({
  proxyUrl: '/api/inference/proxy'
  // No apiKey needed on frontend
});
```

### Next.js Proxy (App Router)
```typescript
// app/api/inference/proxy/route.ts
import { createRouteHandler } from '@inferencesh/sdk/proxy/nextjs';

const route = createRouteHandler({
  apiKey: process.env.INFERENCE_API_KEY
});

export const POST = route.POST;
```

### Express Proxy
```typescript
import express from 'express';
import { createProxyMiddleware } from '@inferencesh/sdk/proxy/express';

const app = express();
app.use('/api/inference/proxy', createProxyMiddleware({
  apiKey: process.env.INFERENCE_API_KEY
}));
```

### Supported Frameworks
* Next.js (App Router & Pages Router)
* Express
* Hono
* Remix
* SvelteKit

## TypeScript Support
Full type definitions included:

> 详细代码示例已移至 `references/detail.md`

## Error Handling

> 详细代码示例已移至 `references/detail.md`

## Human Approval Workflows
```typescript
const response = await agent.sendMessage('Delete all temp files', {
  onToolCall: async (call) => {
    if (call.requiresApproval) {
      const approved = await promptUser(`Allow ${call.name}?`);
      if (approved) {
        const result = await executeTool(call.name, call.args);
        agent.submitToolResult(call.id, result);
      } else {
        agent.submitToolResult(call.id, { error: 'Denied by user' });
      }
    }
  }
});
```

## CommonJS Support
```javascript
const { inference, tool, string } = require('@inferencesh/sdk');

const client = inference({ apiKey: 'inf_...' });
const result = await client.run({...});
```

## Reference Files
* [Agent Patterns](/api/v1/skills/javascript-sdk/file?path=references%2Fagent-patterns.md&ownerHandle=okaris) - Multi-agent, RAG, batch processing patterns
* [Tool Builder](/api/v1/skills/javascript-sdk/file?path=references%2Ftool-builder.md&ownerHandle=okaris) - Complete tool builder API reference
* [Server Proxy](/api/v1/skills/javascript-sdk/file?path=references%2Fserver-proxy.md&ownerHandle=okaris) - Next.js, Express, Hono, Remix, SvelteKit setup
* [Streaming](/api/v1/skills/javascript-sdk/file?path=references%2Fstreaming.md&ownerHandle=okaris) - Real-time progress updates and SSE handling
* [File Handling](/api/v1/skills/javascript-sdk/file?path=references%2Ffiles.md&ownerHandle=okaris) - Upload, download, and manage files
* [Sessions](/api/v1/skills/javascript-sdk/file?path=references%2Fsessions.md&ownerHandle=okaris) - Stateful execution with warm workers
* [TypeScript](/api/v1/skills/javascript-sdk/file?path=references%2Ftypescript.md&ownerHandle=okaris) - Type definitions and type-safe patterns
* [React Integration](/api/v1/skills/javascript-sdk/file?path=references%2Freact-integration.md&ownerHandle=okaris) - Hooks, components, and patterns

## Related Skills
```bash
* 安装此Skill请参考SkillHub平台指南

* 安装此Skill请参考SkillHub平台指南

* 安装此Skill请参考SkillHub平台指南

* 安装此Skill请参考SkillHub平台指南
```

## Documentation
* [JavaScript SDK Reference](https://inference.sh/docs/api/sdk-javascript) - Full API documentation
* [Agent SDK Overview](https://inference.sh/docs/api/agent-sdk) - Building agents
* [Tool Builder Reference](https://inference.sh/docs/api/agent-tools) - Creating tools
* [Server Proxy Setup](https://inference.sh/docs/api/sdk/server-proxy) - Frontend integration
* [Authentication](https://inference.sh/docs/api/authentication) - API key setup
* [Streaming](https://inference.sh/docs/api/sdk/streaming) - Real-time updates
* [File Uploads](https://inference.sh/docs/api/sdk/files) - File handling

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
- JavaScript/TypeScript SDK for inference
- sh - run AI apps, build agents,
  integrate 150+ models
- 触发关键词: apps, inference, typescript, sdk, build, javascript

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例
### 示例1：基础用法
```
```bash
npm install @inferencesh/sdk
```

```typescript
import { inference } from '@inferencesh/sdk';

const client = inference({ apiKey: 'inf_your_key' });

// Run an AI app
const result = await client.run({
  app: 'infsh/flux-schnell',
  input: { prompt: 'A sunset over mountains' }
});
console.log(result.output);
```
```

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Javascript Sdk？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Javascript Sdk有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 性能取决于底层模型能力
