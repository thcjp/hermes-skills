---
slug: doubao-assistant
name: doubao-assistant
version: "1.0.0"
displayName: 豆包助手(专业版)
summary: 全功能豆包大模型集成平台，支持流式响应、函数调用、知识库与批量处理。
license: Proprietary
edition: pro
description: |-
  豆包助手专业版是面向团队与生产环境的全功能豆包大模型集成平台，在免费版基础上新增流式响应、函数调用、知识库检索增强、批量并发管理、系统提示词模板库、用量与会话分析六大高级模块。核心能力：提供 SSE 流式响应处理框架、Function Calling 工具集成模板、RAG 知识库检索增强方案、批量请求调度与并发控制、可复用提示词模板库、会话级用量统计与分析面板
tags:
- AI对话
- 集成工具
- 生产环境
- 专业版
tools:
  - - read
- exec
---
# 豆包助手(专业版)

## 核心能力

### 模块一：流式响应处理（专业版独有）
SSE 流式响应让用户逐字看到生成内容，大幅提升交互体验。

```javascript
// 流式响应处理框架
async function chatStream(message, onChunk) {
  const resp = await fetch('https://api.example.com/v1/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'doubao-pro',
      messages: [{ role: 'user', content: message }],
      stream: true
    })
  });

  const reader = resp.body.getReader();
  const decoder = new TextDecoder();
  let fullContent = '';

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    const lines = chunk.split('\n').filter(l => l.startsWith('data: '));
    for (const line of lines) {
      const data = line.slice(6);
      if (data === '[DONE]') return fullContent;
      const json = JSON.parse(data);
      const content = json.choices[0]?.delta?.content || '';
      if (content) {
        fullContent += content;
        onChunk(content);  // 逐字回调
      }
    }
  }
  return fullContent;
}
```

**流式响应注意事项**：
- 前端使用 EventSource 或 fetch + ReadableStream 接收
- 超时设置应长于非流式模式（建议 120 秒）
- 网络中断时展示重连提示，恢复后续接内容

- 执行`模块六：用量与会话分析（专业版独有）`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`模块六：用量与会话分析（专业版独有）`相关配置参数进行设置
### 模块二：函数调用集成（专业版独有）
通过 Function Calling 让模型调用外部工具，扩展 AI 的能力边界。

```javascript
// 函数定义
const tools = [
  {
    type: 'function',
    function: {
      name: 'search_knowledge_base',
      description: '在企业知识库中搜索相关文档',
      parameters: {
        type: 'object',
        properties: {
          query: { type: 'string', description: '搜索关键词' },
          top_k: { type: 'integer', description: '返回结果数', default: 5 }
        },
        required: ['query']
      }
    }
  },
  {
    type: 'function',
    function: {
      name: 'create_ticket',
      description: '创建工单',
      parameters: {
        type: 'object',
        properties: {
          title: { type: 'string', description: '工单标题' },
          priority: { type: 'string', enum: ['low', 'medium', 'high'] }
        },
        required: ['title']
      }
    }
  }
];

// 函数调用处理流程
async function chatWithTools(message, history) {
  const messages = [...history, { role: 'user', content: message }];

  const resp = await fetch('https://api.example.com/v1/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: 'doubao-pro', messages, tools })
  });

  const data = await resp.json();
  const toolCalls = data.choices[0].message.tool_calls;

  if (toolCalls) {
    messages.push(data.choices[0].message);
    for (const call of toolCalls) {
      const args = JSON.parse(call.function.arguments);
      const result = await executeTool(call.function.name, args);
      messages.push({
        role: 'tool',
        tool_call_id: call.id,
        content: JSON.stringify(result)
      });
    }
    // 再次请求获取最终回复
    const finalResp = await fetch('https://api.example.com/v1/chat/completions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model: 'doubao-pro', messages, tools })
    });
    return (await finalResp.json()).choices[0].message.content;
  }
  return data.choices[0].message.content;
}
```

**函数设计原则**：
- 函数描述清晰，让模型准确判断何时调用
- 参数使用 JSON Schema 严格定义类型与必填项
- 敏感操作（创建/删除/修改）需用户确认后执行
- 函数实现需设置超时与错误处理，失败时返回结构化错误

### 模块三：知识库检索增强 RAG（专业版独有）
将企业知识库与豆包对话结合，实现基于私有知识的精准问答。

```
用户提问
  ├─ 优秀步：将问题向量化，在知识库中检索相关文档片段
  ├─ 第二步：将检索结果作为上下文拼入提示词
  ├─ 第三步：调用豆包模型生成基于上下文的回答
  └─ 第四步：返回回答并标注引用来源
```

```javascript
// RAG 检索增强方案
async function ragChat(question, knowledgeBase) {
  // 1. 检索相关知识片段
  const relevantDocs = await knowledgeBase.search(question, { topK: 5 });

  // 2. 构造增强提示词
  const context = relevantDocs
    .map((doc, i) => `[文档${i+1}] ${doc.content}`)
    .join('\n\n');

  const systemPrompt = `你是一个企业知识助手。请基于以下参考文档回答问题。
如果参考文档中没有相关信息，请说明"知识库中未找到相关内容"。

参考文档：
${context}`;

  // 3. 调用模型生成回答
  const messages = [
    { role: 'system', content: systemPrompt },
    { role: 'user', content: question }
  ];

  const resp = await fetch('https://api.example.com/v1/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: 'doubao-pro', messages })
  });

  const data = await resp.json();
  return {
    answer: data.choices[0].message.content,
    sources: relevantDocs.map(d => ({ title: d.title, score: d.score }))
  };
}
```

| RAG 组件 | 推荐方案 | 说明 |
|:---------|:---------|:-----|
| 文档切分 | 按段落/固定长度 | 每块 200-500 字，保留上下文 |
| 向量化 | Embedding 模型 | 将文本转为向量表示 |
| 向量存储 | 向量数据库 | 支持 ANN 近似最近邻检索 |
| 检索策略 | 语义相似度 + 关键词混合 | 兼顾语义匹配与精确匹配 |
| 重排序 | Cross-encoder 重排 | 提升 Top-K 结果相关性 |

### 模块四：批量并发管理（专业版独有）
| 策略 | 适用场景 | 实现方式 |
|:-----|:---------|:---------|
| 串行队列 | 有序依赖任务 | 逐个执行，结果按序收集 |
| 并发池 | 独立批量任务 | 固定并发数 + 队列调度 |
| 分批处理 | 超大批量 | 按批次分组，批次间间隔 |

```javascript
// 并发池实现
async function batchProcess(tasks, concurrency = 5) {
  const results = new Array(tasks.length);
  let index = 0;

  async function worker() {
    while (index < tasks.length) {
      const current = index++;
      try {
        results[current] = await tasks[current]();
      } catch (e) {
        results[current] = { error: e.message };
      }
    }
  }

  await Promise.all(Array.from({ length: concurrency }, () => worker()));
  return results;
}
```

### 模块五：系统提示词模板库（专业版独有）
| 模板名称 | 系统提示词要点 | 适用场景 |
|:---------|:---------------|:---------|
| 知识助手 | 基于上下文回答、标注来源、不编造 | 企业知识库问答 |
| 客服代表 | 友好专业、不超过权限承诺、引导转人工 | 智能客服 |
| 内容摘要 | 提取要点、保留关键数据、结构化输出 | 文档总结 |
| 翻译专家 | 保留术语、适配文化、自然流畅 | 多语言翻译 |
| 数据分析 | 输出结论与建议、标注数据来源 | 报表解读 |

### 模块六：用量与会话分析（专业版独有）
```javascript
// 会话级用量统计
class SessionAnalytics {
  constructor() {
    this.sessions = new Map();
  }

  record(sessionId, { inputTokens, outputTokens, duration, toolCalls }) {
    if (!this.sessions.has(sessionId)) {
      this.sessions.set(sessionId, {
        totalInput: 0,
        totalOutput: 0,
        totalDuration: 0,
        totalToolCalls: 0,
        messageCount: 0
      });
    }
    const stats = this.sessions.get(sessionId);
    stats.totalInput += inputTokens;
    stats.totalOutput += outputTokens;
    stats.totalDuration += duration;
    stats.totalToolCalls += toolCalls || 0;
    stats.messageCount++;
  }

  getReport(sessionId) {
    const stats = this.sessions.get(sessionId);
    if (!stats) return null;
    return {
      ...stats,
      avgInputPerMessage: Math.round(stats.totalInput / stats.messageCount),
      avgOutputPerMessage: Math.round(stats.totalOutput / stats.messageCount),
      avgDurationMs: Math.round(stats.totalDuration / stats.messageCount)
    };
  }

  getTopSessions(metric = 'totalInput', limit = 10) {
    return [...this.sessions.entries()]
      .sort((a, b) => b[1][metric] - a[1][metric])
      .slice(0, limit)
      .map(([id, stats]) => ({ sessionId: id, ...stats }));
  }
}
```

- 执行`模块六：用量与会话分析（专业版独有）`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`模块六：用量与会话分析（专业版独有）`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 全功能豆包大模型、集成平台、支持流式响应、知识库与批量处理、豆包助手专业版是、面向团队与生产环、境的全功能豆包大、模型集成平台、在免费版基础上新、增流式响应、用量与会话分析六、大高级模块、核心能力、工具集成模板、知识库检索增强方、批量请求调度与并、发控制、可复用提示词模板、会话级用量统计与、分析面板。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一：企业知识库智能检索
将企业文档导入知识库，员工通过自然语言提问，系统基于 RAG 返回精准答案并标注来源。

### 场景二：智能客服系统
集成函数调用让模型查询订单、提交工单、查询物流，实现端到端自动化客服。

### 场景三：批量内容处理
运营团队批量生成商品描述、营销文案，使用并发池管理吞吐量，用量分析追踪消耗。

### 场景四：流式对话服务
面向用户的对话服务使用流式响应提升体验，前端逐字展示生成内容。

### 场景五：AI Agent 工具链
构建具备工具调用能力的 AI Agent，通过 Function Calling 连接数据库、搜索引擎、内部系统。

## 使用流程

**角色化集成方案模板**：

```
【开发者】我需要搭建一个企业知识库问答系统，文档约 5000 篇，请给出 RAG 方案。
```

```
【运维】我需要监控各会话的 Token 消耗，找出成本最高的会话。
```

```
【产品经理】我想做一个能查询订单和提交工单的智能客服，需要哪些工具函数？
```

Agent 会输出包含架构设计、代码模板、配置参数、监控指标的完整集成方案。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **运行时**: Node.js 18+ 或 Python 3.8+
- **向量数据库**: Chroma / Pinecone / Weaviate（RAG 场景必需）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| 豆包会话凭据 | 凭据 | 必需 | 豆包平台获取 |
| Node.js / Python | 运行时 | 必需 | 官方网站下载 |
| 向量数据库 | 数据库 | 推荐 | 对应官方下载或云服务 |
| Embedding 模型 | 模型 | 推荐 | 开源模型或 API 服务 |
| Redis | 缓存 | 可选 | 官方下载（会话存储） |

### API Key 配置
- **豆包会话凭据**: 通过环境变量 `DOUBAO_SESSIONID` 注入
- **向量数据库密钥**: 通过环境变量注入
- **Embedding API Key**: 通过环境变量注入
- **禁止**: 在代码、脚本、SKILL.md 中硬编码任何密钥
- **推荐**: 生产环境使用密钥管理服务

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，高级功能需要exec执行脚本与HTTP请求）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent实现豆包大模型的工程化集成

## 案例展示

### 生产环境配置清单
```yaml
# 生产环境配置
doubao:
  session_id: ${DOUBAO_SESSIONID}
  base_url: https://api.example.com/v1
  default_model: doubao-pro
  timeout_ms: 60000
  max_retries: 3

streaming:
  enabled: true
  chunk_timeout_ms: 30000      # 单 chunk 超时
rag:
  enabled: true
  vector_db:
    type: chroma                # chroma / pinecone / weaviate
    collection: knowledge_base
  chunk_size: 300               # 文档切分大小
  chunk_overlap: 50             # 切分重叠
  top_k: 5                      # 检索返回数
  rerank: true                  # 是否重排序
concurrency:
  max_pool_size: 10
  queue_timeout_ms: 30000

analytics:
  session_tracking: true
  cost_tracking: true
  report_schedule: "0 8 * * *"  # 每日8点生成报表
```

## 常见问题

### Q1：RAG 检索结果不相关怎么办？
检查文档切分质量、向量模型选择、检索 top_k 设置。引入重排序（Cross-encoder）提升相关性。优化查询改写，将用户问题转换为更适合检索的形式。

### Q2：函数调用失败如何处理？
向模型返回结构化错误信息，模型会基于错误调整回复。不要对用户直接暴露原始错误，转换为用户友好的提示。

### Q3：流式响应中途断开怎么办？
记录已接收内容位置，断开后重新请求时通过对话历史续接。前端展示"连接中断，正在重连"提示。

### Q4：知识库文档量大时检索慢？
使用向量数据库的 ANN 索引加速检索。文档按类别分区，查询时先过滤再检索。定期优化索引。

### Q5：如何实现多轮对话的上下文压缩？
当对话轮数超过阈值（如 10 轮）时，将早期对话用模型生成摘要，用摘要替代原始历史。

### Q6：批量任务如何保证不丢数据？
使用检查点机制：每完成一批将结果持久化，失败时从最后检查点恢复。任务设计为幂等。

### Q7：用量分析发现某会话消耗异常高怎么办？
检查该会话的对话历史是否过长、是否频繁调用工具函数。设置单会话 Token 上限，超限提示用户开启新会话。

### Q8：如何评估 RAG 系统质量？
构建评测集（问题-标准答案），统计检索命中率、回答准确率、来源引用正确率。定期回归测试确保质量不退化。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
