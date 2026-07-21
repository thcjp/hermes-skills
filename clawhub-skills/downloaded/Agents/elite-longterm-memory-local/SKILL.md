---
slug: elite-longterm-memory-local
name: elite-longterm-memory-local
version: "1.1.0"
displayName: Elite Longterm Memor
summary: Local vector memory system with LanceDB + Pure JS embedding. No native modules
  or external APIs r...
license: MIT
description: |-
  Local vector memory system with LanceDB + Pure JS embedding。No native
  modules or external APIs r。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Agents
tools:
  - - read
- exec
---

# Elite Longterm Memory

基于 LanceDB + Pure JavaScript Embedding 的本地向量记忆系统，无需外部 API。

## 核心特性

* ✅ **纯本地运行** — Pure JavaScript embedding，零外部依赖
* ✅ **WAL 协议** — 写前日志，防数据丢失
* ✅ **LanceDB 向量搜索** — 语义召回相关记忆
* ✅ **三层存储** — Hot/Warm/Cold 分层管理
* ✅ **无需配置** — 无需 Ollama 或 OpenAI API key
* ✅ **自动召回/捕获** — 智能注入相关上下文

## 架构

```text
┌─────────────────────────────────────────────────────────────────┐
│                    ELITE LONGTERM MEMORY                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │   HOT RAM   │  │  WARM STORE │  │  COLD STORE │             │
│  │             │  │             │  │             │             │
│  │ SESSION-    │  │  LanceDB    │  │  Git-Notes  │             │
│  │ STATE.md    │  │  Vectors    │  │  Knowledge  │             │
│  │             │  │             │  │  Graph      │             │
│  │ (survives   │  │ (semantic   │  │ (permanent  │             │
│  │  compaction)│  │  search)    │  │  decisions) │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│                  ┌─────────────┐                                │
│                  │  MEMORY.md  │  ← Curated long-term           │
│                  │  + daily/   │    (human-readable)            │
│                  └─────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 五层记忆系统

| 层级 | 文件/系统 | 用途 | 持久化 |
| --- | --- | --- | --- |
| 1. Hot RAM | SESSION-STATE.md | 活跃任务上下文 | survived compaction |
| 2. Warm Store | LanceDB Vectors | 语义搜索 | 自动召回 |
| 3. Cold Store | Git-Notes | 结构化决策 | 永久保存 |
| 4. Archive | MEMORY.md + daily/ | 人类可读 | 精选归档 |
| 5. Embedding | Ollama | 本地向量模型 | 纯本地 |

## 快速开始

### 依赖说明

```bash
ollama --version

ollama pull nomic-embed-text

cd skills/elite-longterm-memory
npm install
```

### 2. 初始化记忆系统

```bash
node bin/init.js
```

这会创建：

* `SESSION-STATE.md` — 热内存
* `MEMORY.md` — 长期记忆
* `memory/` — 每日日志目录
* `memory/vectors/` — LanceDB 数据库

### 3. 使用记忆工具

```bash
node bin/memory.js store "用户喜欢深色模式" --importance 0.9 --category preference

node bin/memory.js search "用户界面偏好"

node bin/memory.js stats

node bin/memory.js forget --query "深色模式"
```

## Skill平台 集成

### 启用插件

在 `~/.skill-platform/skill-platform.json` 中添加：

```json
{
  "plugins": {
    "entries": {
      "elite-longterm-memory": {
        "enabled": true,
        "config": {
          "ollamaUrl": "http://localhost:11434",
          "embeddingModel": "nomic-embed-text",
          "dbPath": "./memory/vectors",
          "autoRecall": true,
          "autoCapture": false
        }
      }
    }
  }
}
```

### 使用记忆工具

启用后，Skill平台 会自动提供以下工具：

* `memory_recall` — 搜索相关记忆
* `memory_store` — 存储重要信息
* `memory_forget` — 删除记忆

### 智能提示词

在 `AGENTS.md` 或 `SOUL.md` 中添加：

```markdown
## 记忆协议

### 会话开始时
1. 读取 SESSION-STATE.md — 获取热上下文
2. 使用 memory_recall 搜索相关历史
3. 检查 memory/YYYY-MM-DD.md 了解近期活动

### 对话中
- 用户给出具体细节？→ 先写入 SESSION-STATE.md，再回复
- 重要决策？→ 使用 memory_store 存储
- 表达偏好？→ memory_store --importance 0.9 --category preference

### 会话结束时
1. 更新 SESSION-STATE.md 最终状态
2. 重要内容移至 MEMORY.md
3. 创建/更新 memory/YYYY-MM-DD.md
```

## WAL 协议（关键）

**写前日志**：先写状态，再回复。

| 触发条件 | 动作 |
| --- | --- |
| 用户表达偏好 | 写入 SESSION-STATE.md → 然后回复 |
| 用户做出决策 | 写入 SESSION-STATE.md → 然后回复 |
| 用户给出期限 | 写入 SESSION-STATE.md → 然后回复 |
| 用户纠正你 | 写入 SESSION-STATE.md → 然后回复 |

**为什么？** 如果先回复再保存，崩溃/压缩会导致上下文丢失。WAL 确保数据持久。

## 维护命令

```bash
node bin/memory.js stats

node bin/memory.js search "*" --limit 50

node bin/memory.js dedup

node bin/memory.js export --format json > memories.json

node bin/memory.js backup ./backups/memory-$(date +%Y%m%d).zip
```

## 故障排查

**Ollama 连接失败**
→ 检查 `ollama serve` 是否运行
→ 检查 `OLLAMA_HOST` 环境变量

**向量搜索无结果**
→ 检查 LanceDB 路径是否正确
→ 确认已存储记忆：`node bin/memory.js stats`

**内存占用过高**
→ 运行 `node bin/memory.js compact` 压缩向量
→ 清理旧记忆：`node bin/memory.js cleanup --before 30d`

## 为什么本地 Embedding？

| 对比 | OpenAI API | Ollama 本地 |
| --- | --- | --- |
| 费用 | 按 token 收费 | 免费 |
| 延迟 | 网络依赖 | 本地毫秒级 |
| 隐私 | 数据出域 | 完全本地 |
| 离线 | 不可用 | 可用 |
| 质量 | text-embedding-3 | nomic-embed-text |

对于个人使用，nomic-embed-text 的质量足够，且完全免费。

## 链接

* Ollama: <https://ollama.com>
* LanceDB: <https://lancedb.github.io> (npm: `vectordb`)
* nomic-embed-text: <https://ollama.com/library/nomic-embed-text>

---

*本地优先，隐私至上。*

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

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 示例

### 示例1：基础用法

```
### 依赖说明

```bash
ollama --version

ollama pull nomic-embed-text

cd skills/elite-longterm-memory
npm install
```

### 2. 初始化记忆系统

```bash
node bin/init.js
```

这会创建：

* `SESSION-STATE.md` — 热内存
* `MEMORY.md` — 长期记忆
* `memory/` — 每日日志目录
* `memory/vectors/` — LanceDB 数据库

### 3. 使用记忆工具

```bash
node bin/memory.js store "用户喜欢深色模式" --importance 0.9 --category preference

node bin/memory.js search "用户界面偏好"

node bin/memory.js stats

node bin/memory.js forget --query "深色模式"
```
```

## 常见问题

### Q1: 如何开始使用Elite Longterm Memor？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Elite Longterm Memor有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步

## 异常处理
- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断
- 重试机制: 失败时自动重试, 最多3次

## 输出格式

处理结果以结构化格式返回, 包含状态码、消息和数据字段。
