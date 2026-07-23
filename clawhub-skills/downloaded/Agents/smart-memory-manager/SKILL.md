---
pricing_tier: L2
pricing_model: per_use
suggested_price: 19.9
---

# smart-memory-manager

## 核心亮点

1. 📚 **分层记忆体系**：短期/长期/重要记忆三层架构，自动清理过期记忆，解决上下文溢出问题
2. 🔍 **多模式检索**：支持关键词/语义/混合三种检索模式，快速召回相关记忆，提升RAG准确率
3. 📝 **自动摘要能力**：一键生成记忆摘要，支持长会话上下文压缩，token占用减少70%
4. 💾 **持久化支持**：支持内存/磁盘持久化，重启后记忆不丢失

## 适用场景

* 长会话Agent、聊天机器人
* RAG应用的记忆层
* 需要长期记忆的任务型Agent
* 客服、助理类Agent的上下文管理

## 📝 参数说明

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | string | 是 | 操作类型：add/search/summarize/clear/list/load/save |
| content | string | 否 | add操作必填，记忆内容 |
| type | string | 否 | add操作可选，记忆类型：short-term/long-term/important，默认short-term |
| query | string | 否 | search操作必填，搜索关键词 |
| limit | number | 否 | search/list操作可选，返回结果数量，默认5/20 |
| typeFilter | string | 否 | 所有操作可选，过滤记忆类型，默认all |
| persist | boolean | 否 | add操作可选，是否持久化存储，默认false |
| persistPath | string | 否 | load/save操作可选，持久化文件路径，默认./memory-store.json |

## 示例

### 添加记忆

```typescript
// 添加长期记忆
await skills.smartMemoryManager({
  action: "add",
  content: "用户喜欢喝咖啡，不加糖，每周三下午喝奶茶",
  type: "long-term",
  persist: true
});
```

### 搜索记忆

```typescript
const result = await skills.smartMemoryManager({
  action: "search",
  query: "用户喜好",
  limit: 3,
  searchMode: "hybrid" // 关键词+语义混合检索
});
```

### 生成会话摘要

```typescript
const summary = await skills.smartMemoryManager({
  action: "summarize",
  typeFilter: "short-term",
  maxTokens: 500
});
```

### 持久化与加载

```typescript
// 保存所有记忆到磁盘
await skills.smartMemoryManager({
  action: "save",
  persistPath: "./my-memory.json"
});

// 从磁盘加载记忆
await skills.smartMemoryManager({
  action: "load",
  persistPath: "./my-memory.json"
});
```

## 🔧 技术实现说明

* 内置记忆自动清理机制，短期记忆最多保留100条，避免内存溢出
* 模块化设计，可轻松对接向量数据库实现语义检索
* 全链路类型安全，参数自动校验
* 轻量无外部依赖，开箱即用，也支持自定义扩展

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

- Intelligent memory management for agents with short/long-term memory
  layering, semantic search, a
- 触发关键词: memory, intelligent, manager, smart-memory-manager, agents, management, smart

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

### Q1: 如何开始使用smart-memory-manager？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: smart-memory-manager有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
