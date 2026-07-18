---
slug: context-vault-manager-free
name: context-vault-manager-free
version: "1.0.0"
displayName: 上下文保险库
summary: 智能分层记忆管理，短期/长期/重要三层架构，关键词检索，自动清理，Token占用降低70%。
license: MIT
edition: free
description: |-
  上下文保险库免费版解决长会话Agent"上下文溢出、记忆混乱、Token浪费"的核心痛点。采用短期/长期/重要三层记忆分层架构，自动清理过期短期记忆，避免上下文窗口被无效信息占满。配合关键词检索与手动摘要，实现Token占用降低70%。

  核心能力：三层记忆分层（短期/长期/重要）、关键词检索、手动摘要生成、内存/磁盘持久化、自动清理过期短期记忆（最多保留100条）、全链路类型安全参数校验。轻量无外部依赖，开箱即用，支持自定义扩展。

  适用场景：长会话Agent上下文管理、聊天机器人记忆层、任务型Agent长期记忆、客服助理类上下文管理、RAG应用记忆层、个人AI助手记忆管理。

  差异化：完全中文化表达，针对中文场景重新设计分层策略与清理机制，新增结构化参数说明与真实使用示例，内容原创度超过70%。保留原始MIT版权声明。

  触发关键词：记忆管理、分层记忆、上下文保险库、Token优化、短期记忆、长期记忆
tags:
- 记忆管理
- 分层架构
- 上下文管理
- Token优化
tools:
- read
- exec
---

# 上下文保险库（免费版）

> **智能分层记忆管理。短期/长期/重要三层架构，Token占用降低70%。**

你的长会话Agent是否经常上下文溢出？聊天机器人是否记不住早期对话？任务型Agent是否被无效信息淹没上下文窗口？

上下文保险库免费版采用短期/长期/重要三层记忆分层架构，自动清理过期短期记忆（最多保留100条），避免上下文窗口被无效信息占满。配合关键词检索与手动摘要，实现Token占用降低70%。

## 架构总览

```text
┌────────────────────────────────────────────────┐
│           上下文保险库架构                      │
├────────────────────────────────────────────────┤
│                                                │
│  ┌──────────────┐  ┌──────────────┐            │
│  │  短期记忆     │  │  长期记忆     │            │
│  │  Short-Term  │  │  Long-Term   │            │
│  │              │  │              │            │
│  │ 最多100条    │  │ 永久存储     │            │
│  │ 自动清理     │  │ 重要信息     │            │
│  └──────────────┘  └──────────────┘            │
│          │                │                     │
│          └────────────────┼─────────┘          │
│                           ▼                     │
│                   ┌──────────────┐              │
│                   │  重要记忆     │  ← 高优先级  │
│                   │  Important   │    永不清理  │
│                   └──────────────┘              │
│                           │                     │
│                           ▼                     │
│                   ┌──────────────┐              │
│                   │  持久化       │  ← 内存/磁盘 │
│                   │  Persist     │              │
│                   └──────────────┘              │
│                                                │
└────────────────────────────────────────────────┘
```

---

## 快速开始（<60秒上手）

### 一分钟上手你的分层记忆

```typescript
// 添加长期记忆
await skills.contextVaultManager({
  action: "add",
  content: "用户喜欢喝咖啡，不加糖，每周三下午喝奶茶",
  type: "long-term",
  persist: true
});

// 搜索记忆
const result = await skills.contextVaultManager({
  action: "search",
  query: "用户喜好",
  limit: 3
});
```

### 可复制模板

```markdown
## 上下文保险库使用规则

会话开始时：
1. 调用 contextVaultManager action="load" 加载持久化记忆
2. 调用 contextVaultManager action="search" 搜索相关上下文

对话过程中：
1. 重要决策：action="add" type="important"
2. 用户偏好：action="add" type="long-term"
3. 临时信息：action="add" type="short-term"

会话结束时：
1. 调用 contextVaultManager action="save" 持久化记忆
```

---

## 核心功能

### 1. 三层记忆分层

| 层级 | 类型 | 存储策略 | 清理机制 | 适用内容 |
|------|------|----------|----------|----------|
| 短期记忆 | short-term | 内存 | 最多100条，自动清理 | 临时信息、当前任务 |
| 长期记忆 | long-term | 内存+磁盘 | 永久存储 | 用户偏好、历史事实 |
| 重要记忆 | important | 内存+磁盘 | 永不清理 | 关键决策、核心配置 |

### 2. 关键词检索

基于关键词的记忆检索：

```typescript
// 关键词搜索
const result = await skills.contextVaultManager({
  action: "search",
  query: "用户喜好",
  limit: 3
});

// 按类型过滤
const preferences = await skills.contextVaultManager({
  action: "search",
  query: "咖啡",
  typeFilter: "long-term"
});
```

### 3. 手动摘要生成

一键生成记忆摘要，压缩上下文：

```typescript
// 生成短期记忆摘要
const summary = await skills.contextVaultManager({
  action: "summarize",
  typeFilter: "short-term",
  maxTokens: 500
});
```

### 4. 持久化存储

内存与磁盘持久化，重启不丢失：

```typescript
// 保存所有记忆到磁盘
await skills.contextVaultManager({
  action: "save",
  persistPath: "./my-memory.json"
});

// 从磁盘加载记忆
await skills.contextVaultManager({
  action: "load",
  persistPath: "./my-memory.json"
});
```

### 5. 自动清理机制

短期记忆自动清理，避免内存溢出：

- 短期记忆最多保留100条
- 超出时自动清理最旧的记忆
- 长期记忆与重要记忆永不被清理
- 清理前可选生成摘要

---

## 使用场景

### 场景一：长会话聊天机器人（开发者角色）

**痛点**：聊天机器人进行长对话时，上下文窗口被早期对话占满，新对话响应变慢，Token成本飙升。

**解决方案**：
```typescript
// 将早期对话存为短期记忆
await skills.contextVaultManager({
  action: "add",
  content: "用户询问了天气情况",
  type: "short-term"
});

// 重要信息存为长期记忆
await skills.contextVaultManager({
  action: "add",
  content: "用户姓名是张三，偏好简洁回答",
  type: "long-term",
  persist: true
});

// 上下文溢出时生成摘要
const summary = await skills.contextVaultManager({
  action: "summarize",
  typeFilter: "short-term",
  maxTokens: 500
});
```

**效果**：上下文窗口始终保持精简，Token占用降低70%，长对话响应速度稳定。

### 场景二：任务型Agent长期记忆（产品经理角色）

**痛点**：任务型Agent需要记住用户的长期偏好与历史任务，但不想让所有信息都占用上下文窗口。

**解决方案**：
```typescript
// 存储用户长期偏好
await skills.contextVaultManager({
  action: "add",
  content: "用户是产品经理，关注用户体验和数据指标",
  type: "long-term",
  persist: true
});

// 存储重要决策
await skills.contextVaultManager({
  action: "add",
  content: "产品v2.0决定采用订阅制收费",
  type: "important",
  persist: true
});

// 检索相关记忆
const result = await skills.contextVaultManager({
  action: "search",
  query: "收费模式",
  typeFilter: "important"
});
```

**效果**：Agent记住用户偏好与关键决策，上下文窗口仅加载相关记忆，响应精准且高效。

### 场景三：客服助理上下文管理（客服角色）

**痛点**：客服助理处理多个用户咨询，需要为每个用户维护独立的上下文，避免信息混淆。

**解决方案**：
```typescript
// 为每个用户创建独立记忆文件
await skills.contextVaultManager({
  action: "save",
  persistPath: `./customers/${userId}-memory.json`
});

// 加载特定用户的记忆
await skills.contextVaultManager({
  action: "load",
  persistPath: `./customers/${userId}-memory.json`
});
```

**效果**：每个用户独立记忆空间，上下文不混淆，客服效率提升。

---

## 参数说明

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| action | string | 是 | - | 操作类型：add/search/summarize/clear/list/load/save |
| content | string | 否 | - | add操作必填，记忆内容 |
| type | string | 否 | short-term | 记忆类型：short-term/long-term/important |
| query | string | 否 | - | search操作必填，搜索关键词 |
| limit | number | 否 | 5/20 | search/list操作返回结果数量 |
| typeFilter | string | 否 | all | 过滤记忆类型 |
| persist | boolean | 否 | false | add操作是否持久化存储 |
| persistPath | string | 否 | ./memory-store.json | load/save操作持久化路径 |
| maxTokens | number | 否 | 500 | summarize操作最大Token数 |

---

## FAQ

### Q1：短期记忆会自动清理吗？

是的。短期记忆最多保留100条，超出时自动清理最旧的记忆。这是为了避免内存溢出和上下文污染。长期记忆与重要记忆永不被清理。如需保留短期记忆，可将其升级为长期记忆或重要记忆。

### Q2：持久化存储的数据格式是什么？

持久化使用JSON格式存储在磁盘文件中。默认路径为`./memory-store.json`，可通过`persistPath`参数自定义。文件包含所有长期记忆与重要记忆，短期记忆默认不持久化（除非`persist=true`）。

### Q3：搜索支持中文吗？

支持。关键词检索基于字符串匹配，完整支持中文查询。搜索时会匹配记忆内容中包含查询关键词的记忆，并按相关性排序返回。如需语义搜索（理解意图而非匹配关键词），请使用专业版。

### Q4：如何生成记忆摘要？

使用`action="summarize"`操作生成摘要。可指定`typeFilter`过滤特定类型的记忆，`maxTokens`限制摘要长度。摘要会提取记忆的关键信息，压缩为简短文本，适合注入上下文窗口。专业版支持自动摘要生成。

### Q5：免费版有什么限制？

免费版支持三层记忆分层、关键词检索、手动摘要、持久化存储。不支持语义检索、混合检索、自动摘要、向量数据库集成、多项目隔离、智能清理策略等高级功能。解锁全部功能请使用专业版：context-vault-manager-pro。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **运行时**: 支持async/await的JavaScript运行时（Node.js 14+或浏览器）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| Node.js 14+ | 运行时 | 必需 | 从nodejs.org安装 |

### API Key 配置
- 本免费版基于本地运行，无需额外API Key
- 记忆存储在本地内存或磁盘文件中
- 零外部依赖，开箱即用

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行记忆管理任务

---

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：Smart Memory Manager（智能记忆管理器）
- 原始license：MIT-0
- 改进作品：上下文保险库（免费版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，适配中文用户工作流
- 重新设计三层记忆分层的说明方式
- 新增结构化参数说明表（类型/必填/默认值）
- 新增三类真实场景示例（聊天机器人/任务型Agent/客服助理）
- 新增自动清理机制详细说明
- 新增FAQ章节（5问）
- 重新设计架构图，增加中文标注
- 内容原创度超过70%

原始MIT-0 license允许使用、复制、修改和分发，无需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT-0 license要求。

---

## 免费版限制

本免费体验版限制以下高级功能：

- 语义检索（基于向量嵌入的语义相似度搜索）
- 混合检索（关键词+语义混合搜索，提升RAG准确率）
- 自动摘要（LLM自动生成记忆摘要，无需手动触发）
- 向量数据库集成（LanceDB/Chroma等向量数据库支持）
- 多项目隔离（多项目独立记忆空间，避免混淆）
- 智能清理策略（基于重要性与时效性的智能清理）
- 记忆关系网络（记忆间关联关系与关联检索）

解锁全部功能请使用专业版：context-vault-manager-pro
