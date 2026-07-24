---
slug: "javascript-sdk-paid"
name: "javascript-sdk-paid"
version: 1.0.1
displayName: "JS SDK工具专业版"
summary: "企业级 AI 应用 SDK 方案，支持智能体构建、流式响应、会话管理与服务器代理集成。"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业级 AI 应用开发的 JavaScript SDK 专业工具，提供智能体构建与高级调用能力。核心能力:
  - 智能体（Agent）构建与多轮对话
  - 流式响应与实时进度更新
  - 会话管理与有状态执行
  - 工具构建器 API（自定义工具/应用工具/代理工具）
  - 服务器代理集成（Next
tags:
  - 开发工具
  - JavaScript
  - AI应用
  - 智能体
  - 企业开发
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
category: "Automation"
---
# JS SDK工具专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| JS SDK工具专业版会话管理 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
|:-----|:-----|:-----|
| 应用调用 | 基础 run/getTask | 流式响应 + 进度回调 |
| 智能体 | - | Agent 构建 + 多轮对话 |
| 会话管理 | - | 有状态执行 + 会话保持 |
| 工具系统 | - | 工具构建器 API |
| 文件处理 | 基础上传 | 附件处理 + 多格式支持 |
| 代理集成 | 基础代理 | Next.js/Express/Hono/Remix/SvelteKit |
| 审批流程 | - | 人工审批工作流 |
| 类型安全 | 基础类型 | 完整类型定义 + 类型守卫 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 应用调用

针对应用调用,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供应用调用相关的配置参数、输入数据和处理选项.
**输出**: 返回应用调用的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`应用调用`的配置文档进行参数调优
### 智能体

针对智能体,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供智能体相关的配置参数、输入数据和处理选项.
**输出**: 返回智能体的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`智能体`的配置文档进行参数调优
#
## 适用场景

### 场景一：构建自定义智能体
团队需要构建一个带有自定义工具的 AI 智能体.
> 详细代码示例已移至 `references/detail.md`

### 场景二：流式响应处理
应用需要实时显示 AI 响应的生成过程.
```typescript
const agent = client.agent({
    core_app: { ref: 'claude-sonnet@latest' },
    system_prompt: '你是一个技术讲解助手。'
});
// ...
// 流式响应
const response = await agent.sendMessage('解释量子计算的基本原理', {
    onMessage: (msg) => {
        // 实时输出内容
        if (msg.content) {
            process.stdout.write(msg.content);
        }
    },
    onToolCall: async (call) => {
        // 工具调用回调
        console.log(`\n[工具调用: ${call.name}]`);
        console.log('参数:', call.args);
// ...
        // 执行工具并返回结果
        const result = await executeTool(call.name, call.args);
        agent.submitToolResult(call.id, result);
    }
});
// ...
console.log('\n\n完整响应:', response.text);
```

```typescript
// 流式应用调用（进度更新）
const stream = await client.run({
    app: 'video-generator',
    input: { prompt: '海浪日落' }
}, { stream: true });
// ...
for await (const update of stream) {
    console.log(`状态: ${update.status}`);
// ...
    if (update.logs?.length) {
        const lastLog = update.logs[update.logs.length - 1];
        console.log('日志:', lastLog);
    }
// ...
    if (update.status === 'completed') {
        console.log('输出:', update.output);
    }
}
```

### 场景三：有状态会话管理
应用需要在多次调用间保持会话状态.
```typescript
// 1. 创建新会话
const result1 = await client.run({
    app: 'my-app',
    input: { action: 'init', user_id: 'user123' },
    session: 'new',
    session_timeout: 300  // 5 分钟空闲超时
});
// ...
const sessionId = result1.session_id;
console.log('会话 ID:', sessionId);
// ...
// 2. 在同一会话中继续
const result2 = await client.run({
    app: 'my-app',
    input: { action: 'process', data: '...' },
    session: sessionId  // 复用会话
});
// ...
// 3. 会话保持工作器热度，避免冷启动
const result3 = await client.run({
    app: 'my-app',
    input: { action: 'query', question: '...' },
    session: sessionId
});
// ...
// 4. 会话超时后自动清理
// session_timeout 控制空闲超时时间（1-3600 秒）
```

## 使用流程

### 工具构建器 API

### 人工审批工作流

人工审批工作流允许在工具执行过程中插入人工审核环节，适用于高风险操作或需要多方确认的场景。通过 `approvalRequired` 配置项启用，支持自定义审批人列表、超时自动拒绝与审批回调处理。工作流执行到审批节点时暂停，等待审批人通过或拒绝后继续执行或终止.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | javascript-sdk处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Node.js 版本**: 18.0.0+（或支持 fetch 的现代浏览器）
- **包管理器**: npm / yarn / pnpm

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Node.js | 运行时 | 必需 | nodejs.org 下载 |
| @ai/sdk | npm 包 | 必需 | `npm install @ai/sdk` |
| Next.js | 框架 | 可选 | `npm install next` |
| Express | 框架 | 可选 | `npm install express` |
| Hono | 框架 | 可选 | `npm install hono` |
| TypeScript | 类型系统 | 推荐 | `npm install -D typescript` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 需要 AI 平台的 API Key，通过环境变量配置
- 前端应用必须使用代理模式，不暴露 Key
- 服务器代理通过环境变量读取 Key
- Webhook 工具需要配置对应平台的密钥

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 提供 SDK 集成建议，专业版功能依赖 Node.js、框架环境和命令行执行能力

## 案例展示

### 服务器代理集成

### 文件附件处理
```typescript
import { readFileSync } from 'fs';
// ...
// 1. 从文件路径发送（Node.js）
const response1 = await agent.sendMessage('分析这张图片', {
    files: [readFileSync('image.png')]
});
// ...
// 2. 从 base64 发送
const response2 = await agent.sendMessage('分析这个文件', {
    files: ['data:image/png;base64,iVBORw0KGgo...']
});
// ...
// 3. 从浏览器 File 对象发送
const input = document.querySelector('input[type="file"]');
const response3 = await agent.sendMessage('描述这张图片', {
    files: [input.files[0]]
});
// ...
// 4. 多文件发送
const response4 = await agent.sendMessage('比较这两张图片', {
    files: [file1, file2]
});
```

### 技能（Skills）配置
```typescript
const agent = client.agent({
    core_app: { ref: 'claude-sonnet@latest' },
    skills: [
        {
            name: 'code-review',
            description: '代码审查指南',
            content: `# 代码审查规范
1. 检查安全性
2. 检查性能
3. 检查可读性`
        },
        {
            name: 'api-docs',
            description: 'API 文档',
            url: 'https://example.com/docs/api.md'
        }
    ]
});
// ...
// 智能体会自动参考技能内容进行回答
const response = await agent.sendMessage('帮我审查这段代码');
```

### 完整类型定义

## 常见问题

### Q1：如何在 React 中使用？
```typescript
// React Hook 封装
import { useState, useCallback } from 'react';
import { createClient } from '@ai/sdk';
// ...
const client = createClient({ proxyUrl: '/api/proxy' });
// ...
function useAgent() {
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);
// ...
    const send = useCallback(async (text: string) => {
        setLoading(true);
        try {
            const agent = client.agent({
                core_app: { ref: 'claude-sonnet@latest' }
            });
// ...
            const response = await agent.sendMessage(text, {
                onMessage: (msg) => {
                    if (msg.content) {
                        setMessages(prev => [...prev, {
                            role: 'assistant',
                            content: msg.content
                        }]);
                    }
                }
            });
        } finally {
            setLoading(false);
        }
    }, []);
// ...
    return { messages, send, loading };
}
```

### Q2：如何处理工具执行错误？
```typescript
const response = await agent.sendMessage('执行任务', {
    onToolCall: async (call) => {
        try {
            const result = await executeTool(call.name, call.args);
            agent.submitToolResult(call.id, result);
        } catch (error) {
            // 工具执行失败也返回结果
            agent.submitToolResult(call.id, {
                error: `工具执行失败: ${error.message}`
            });
        }
    }
});
```

### Q3：如何实现多智能体协作？
```typescript
import { agentTool } from '@ai/sdk';
// ...
// 主智能体可以委托给子智能体
const researcher = agentTool('research', 'research-agent@v1')
    .describe('研究指定主题')
    .param('topic', string('研究主题'))
    .build();
// ...
const writer = agentTool('write', 'writer-agent@v1')
    .describe('根据研究结果撰写文章')
    .param('research_data', string('研究数据'))
    .build();
// ...
const coordinator = client.agent({
    core_app: { ref: 'claude-sonnet@latest' },
    system_prompt: '你是协调者，负责分配任务给研究者和撰写者。',
    tools: [researcher, writer]
});
// ...
const response = await coordinator.sendMessage(
    '研究量子计算并写一篇科普文章'
);
```

### Q4：如何控制会话超时？
```typescript
// 创建会话时指定超时（秒）
const result = await client.run({
    app: 'my-app',
    input: { action: 'init' },
    session: 'new',
    session_timeout: 600  // 10 分钟
});
// ...
// 范围: 1-3600 秒
// 超时后会话自动清理
```

### 错误恢复步骤
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制
```typescript
// 简单的速率限制器
class RateLimiter {
    private queue: Array<() => void> = [];
    private running = 0;
    constructor(private maxConcurrent: number = 5) {}
// ...
    async execute<T>(fn: () => Promise<T>): Promise<T> {
        if (this.running >= this.maxConcurrent) {
            await new Promise<void>(resolve => this.queue.push(resolve));
        }
        this.running++;
        try {
            return await fn();
        } finally {
            this.running--;
            if (this.queue.length > 0) {
                this.queue.shift()!();
            }
        }
    }
}
// ...
const limiter = new RateLimiter(5);
// ...
// 使用
const result = await limiter.execute(() =>
    client.run({ app: 'my-app', input: {...} })
);
```

### Q6：支持哪些框架的代理？
| 框架 | 支持 | 配置方式 |
|:------:|--------|:-------|
| Next.js (App Router) | 完整支持 | `createRouteHandler` |
| Next.js (Pages Router) | 完整支持 | 中间件配置 |
| Express | 完整支持 | `createProxyMiddleware` |
| Hono | 完整支持 | `createHonoProxy` |
| Remix | 完整支持 | Action 函数 |
| SvelteKit | 完整支持 | Endpoint 配置 |

## 错误处理

| 错误场景(续)(续)| 原因 | 处理方式 |
|-------|:-----:|------:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 依赖Agent平台的LLM能力与运行环境配置
- 免费版功能受限，高级能力需升级专业版
