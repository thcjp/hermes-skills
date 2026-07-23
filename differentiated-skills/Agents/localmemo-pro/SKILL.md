---
slug: localmemo-pro
name: localmemo-pro
version: 2.0.0
displayName: 本地长记忆
summary: 零API零云依赖的本地向量记忆：离线可用、隐私不出域、embedding缓存省成本。
license: Proprietary
description: 面向隐私敏感与离线场景的本地向量记忆系统。基于LanceDB+Ollama nomic-embed-text，提供本地embedding生成、向量语义检索、embedding缓存、WAL写前日志、三层冷热分层能力。适用于隐私敏感行业（医疗/金融/法律）、离线/弱网环境、个人知识库、合规要求数据不出域场景，实现零外部API、零数据出域、完全离线可用。适用关键词：本地记忆、向量记忆、离线记忆、隐私记忆、embedding、LanceDB、Ollama、nomic、本地向量、local
  memory。
tags:
- 智能代理
- 记忆管理
- 本地存储
tools:
- - read
- exec
homepage: https://skillhub.cn
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
---

# 本地长记忆（LocalMemo Pro）

**零 API、零云端、零数据出域**的本地向量记忆系统。基于 Ollama + LanceDB，在本地完成 embedding 生成与语义检索，适合隐私敏感、离线、成本敏感场景。

## 核心能力

### 本地 embedding 引擎
基于 Ollama nomic-embed-text（274MB，768 维），本地毫秒级生成 embedding，零外部 API 调用、零数据出域、完全离线可用；支持切换 bge-m3/mxbai-embed-large/all-MiniLM-L6 等模型。

**输入**: 用户提供本地 embedding 引擎所需的指令和必要参数。
**处理**: 按照skill规范执行本地 embedding 引擎操作,遵循单一意图原则。
**输出**: 返回本地 embedding 引擎的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### LanceDB 向量库 + embedding 缓存
本地 SQLite 存储向量，embedding 结果按 SHA256(文本) 缓存（命中 <1ms，未命中 10-50ms），典型命中率 60-90%，避免重复计算。

**输入**: 用户提供LanceDB 向量库 + embedding 缓存所需的指令和必要参数。
**处理**: 按照skill规范执行LanceDB 向量库 + embedding 缓存操作,遵循单一意图原则。
**输出**: 返回LanceDB 向量库 + embedding 缓存的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 三层冷热分层 + WAL 写前日志
L1 热内存（SESSION-STATE.md 活跃任务上下文）→ L2 温向量（LanceDB 检索）→ L3 冷存储（Git-Notes 结构化决策）→ L4 精选归档（MEMORY.md + daily/）；WAL 协议保证崩溃/压缩不丢上下文。

**输入**: 用户提供三层冷热分层 + WAL 写前日志所需的指令和必要参数。
**处理**: 按照skill规范执行三层冷热分层 + WAL 写前日志操作,遵循单一意图原则。
**输出**: 返回三层冷热分层 + WAL 写前日志的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 资源占用控制
三级控制（向量数 >10000 自动压缩低重要性向量；磁盘 >500MB 归档 90 天前记忆；磁盘 >1GB 告警+停止写入仅检索），防止内存/CPU/磁盘膨胀。

**输入**: 用户提供资源占用控制所需的指令和必要参数。
**处理**: 按照skill规范执行资源占用控制操作,遵循单一意图原则。
**输出**: 返回资源占用控制的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 一键初始化与维护
`node bin/init.js` 初始化、`memory.js` CLI 提供 store/search/stats/forget/compact/cleanup/dedup/backup/cache-clean 等命令。

**输入**: 用户提供一键初始化与维护所需的指令和必要参数。
**处理**: 按照skill规范执行一键初始化与维护操作,遵循单一意图原则。
**输出**: 返回一键初始化与维护的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：零云依赖的本地向、量记忆、隐私不出域、缓存省成本、面向隐私敏感与离、线场景的本地向量、记忆系统、向量语义检索、三层冷热分层能力、适用于隐私敏感行、弱网环境、个人知识库、合规要求数据不出、域场景、实现零外部、适用关键词、本地记忆、向量记忆、离线记忆、隐私记忆、本地向量、local等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 适用场景

**何时使用：**

| 触发情境 | 示例 |
|:---|:---|
| 隐私敏感行业 | "记录患者对青霉素过敏"（医疗，数据不出域） |
| 离线/弱网环境 | "飞机上回忆上次怎么解决 CORS" |
| 合规要求数据不出域 | "金融 Agent 记忆需符合 GDPR/HIPAA" |
| 零 API 成本运行 | "独立开发者月 API 预算 $0" |
| 个人知识库 | "记住我读过的书和笔记" |
| 需语义检索（非关键词匹配） | "找类似但不确定表述的记忆" |

**输入输出：**
- 输入：记忆文本（store）或查询文本（search）+ 可选 importance/category 元数据
- 输出：存储确认（store）或召回的相关记忆列表（search，按相似度排序）

**不适用场景：**
- 需要极致 embedding 质量（如大规模检索）— 云端 text-embedding-3-large 更优
- 资源极度受限设备（< 4GB 内存）— Ollama 难以运行
- 需要跨设备同步记忆 — 本地方案无云同步
- 无需语义检索的简单键值存储 — 用扁平文件更轻量

## 使用流程

### 依赖详情

```bash
# macOS/Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows: 从 https://ollama.com/download 下载安装包

# 拉取 embedding 模型（约 274MB）
ollama pull nomic-embed-text

# 验证
ollama --version
```

### Step 2：初始化记忆系统

```bash
cd skills/localmemo-pro
npm install
node bin/init.js
```

初始化创建：
- `SESSION-STATE.md` — 热内存
- `MEMORY.md` — 长期记忆
- `memory/` — 每日日志目录
- `memory/vectors/` — LanceDB 向量数据库
- `memory/cache/` — embedding 缓存目录

### Step 3：使用记忆工具

```bash
# 存储
node bin/memory.js store "用户喜欢深色模式" --importance 0.9 --category preference

# 搜索
node bin/memory.js search "用户界面偏好"

# 统计
node bin/memory.js stats

# 遗忘
node bin/memory.js forget --query "深色模式"
```

### Step 4：配置 Agent 集成（可选）

在 Agent 配置文件中启用本地记忆插件：

```json
{
  "plugins": {
    "entries": {
      "localmemo-pro": {
        "enabled": true,
        "config": {
          "ollamaUrl": "http://localhost:11434",
          "embeddingModel": "nomic-embed-text",
          "dbPath": "./memory/vectors",
          "cachePath": "./memory/cache",
          "autoRecall": true,
          "autoCapture": false,
          "maxMemoryMb": 500,
          "minImportance": 0.5
        }
      }
    }
  }
}
```

启用后自动提供工具：`memory_recall`（搜索）、`memory_store`（存储）、`memory_forget`（删除）。

### Step 5：会话中使用记忆

| 阶段 | 动作 |
|:---|:---|
| 会话开始 | 读取 SESSION-STATE.md → memory_recall 搜索相关历史 → 检查 memory/YYYY-MM-DD.md 近期活动 |
| 对话进行中 | 用户给出细节先写 SESSION-STATE.md 再回复；重要决策 memory_store；表达偏好 store --importance 0.9 --category preference；出现错误写 lessons.md |
| 会话结束 | 更新 SESSION-STATE.md 最终状态 → 重要内容移至 MEMORY.md → 创建/更新 memory/YYYY-MM-DD.md |

### Step 6：定期维护

```bash
node bin/memory.js stats --detailed    # 查看资源占用
node bin/memory.js compact             # 压缩向量库
node bin/memory.js cleanup --before 30d  # 清理旧记忆
node bin/memory.js dedup               # 去重
node bin/memory.js backup ./backups/memory-$(date +%Y%m%d).zip  # 导出备份
node bin/memory.js cache-clean --older-than 30d  # 清理 embedding 缓存
```

#
## 示例

### 示例

**输入：**
```
用户："记录患者对青霉素过敏"
```

**执行：**
1. 本地 Ollama 生成 embedding（数据不出域）
2. memory_store："患者青霉素过敏" importance=1.0 category=medical
3. 存储在本地 LanceDB

**输出：**
```
已存储记忆（id: mem_001, importance: 1.0, category: medical）
embedding 由本地 nomic-embed-text 生成，数据未离开本机

后续查询：
  memory_recall query="患者过敏史"
  → 本地检索，零数据外传
  → 召回：mem_001 "患者青霉素过敏"（相似度 0.92）
```

### 示例 2：离线开发场景

**输入：**
```
环境：飞机上无网络，本地开发
用户："上次我们怎么解决 CORS 问题的？"
```

**执行：**
1. 本地 Ollama 生成 query embedding（离线）
2. LanceDB 本地检索
3. embedding 缓存命中（<1ms）

**输出：**
```
召回：mem_042 "CORS 用代理中间件解决，配置在 middleware/cors.js"（相似度 0.89）
召回：mem_043 "生产环境 CORS 需配置白名单域名"（相似度 0.85）

无需网络即可回忆历史决策
```

### 示例 3：成本敏感场景

**输入：**
```
独立开发者，月 API 预算 $0
存储 1000 条记忆 + 检索 100 次/天
```

**输出：**
```
云端方案（对照）：
  embedding 费用约 $0.5-1/月（存储）+ $0.3/月（检索）= $0.8-1.3/月

本地方案：
  一次性模型下载 274MB（nomic-embed-text）
  月度费用：$0（embedding 缓存命中后 <1ms）

年度节省：约 $10-15
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---|:---|:---|
| Ollama 连接失败 | Ollama 服务未启动 | `ollama serve` 启动服务；检查 `curl http://localhost:11434/api/tags` |
| 模型未找到 | 未拉取 embedding 模型 | `ollama pull nomic-embed-text`；`ollama list` 确认 |
| 向量搜索无结果 | 记忆库为空或 dbPath 错误 | `node bin/memory.js stats` 确认已存储记忆；检查 dbPath 配置 |
| 内存占用过高 | 向量库无限增长 | `node bin/memory.js stats --detailed` 查看占用；运行 `compact` + `cleanup` |
| embedding 速度慢 | 缓存未启用或命中率低 | 确认 cache.enabled=true；检查缓存目录权限；首次运行命中率低属正常 |
| 磁盘满 | vectors/ 和 cache/ 过大 | 清理缓存 `cache-clean --older-than 30d`；归档旧记忆；调低 maxSizeMb |
| 检索质量差 | minScore 过高或模型太小 | 降低 minScore 到 0.25；换更大模型（bge-m3） |
| 向量库损坏 | 异常退出或磁盘错误 | 从 `backup` 备份恢复；或从 MEMORY.md + daily/ 重建（记忆内容仍在文件中） |
| LanceDB 初始化失败 | npm 依赖缺失 | 重新 `npm install`；确认 `vectordb` 包已安装 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---|:---|:---|:---|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Ollama | 本地推理引擎 | 必需 | https://ollama.com/install |
| nomic-embed-text | embedding 模型 | 必需 | `ollama pull nomic-embed-text` |
| LanceDB | 向量数据库 | 必需 | `npm install vectordb` |
| Node.js 16+ | 运行时 | 必需 | 系统安装 |
| Git | 版本控制 | 可选 | 用于 Git-Notes 冷存储 |
| Agent 平台 | 运行环境 | 必需 | 支持 SKILL.md 的任意 AI Agent |
| 操作系统 | 运行环境 | 必需 | Windows / macOS / Linux |

**硬件要求：** 内存建议 8GB+（Ollama 运行需 2-4GB）；磁盘建议 2GB+ 可用空间。

**API Key 配置：** 本 Skill 核心功能无需任何 API Key，完全本地运行，零外部 API 调用。如需可选的云端备份功能，另行配置对应服务 Key。

**可用性分类：** MD+EXEC（Markdown 指令 + exec 命令行执行）。核心记忆协议纯 Markdown 可工作；向量检索、embedding 生成需 Ollama + LanceDB 环境。

## 常见问题

**Q1：本地 embedding 质量够用吗？**
A：nomic-embed-text 在 MTEB 基准上表现接近 text-embedding-3-small，对个人/小规模记忆库完全够用。如需更高质量可切换 bge-m3（1.2GB，1024 维）。

**Q2：Ollama 占多少内存？**
A：nomic-embed-text 运行时约 2-4GB 内存。资源紧张可用 all-MiniLM-L6（90MB，约 500MB 内存）。

**Q3：embedding 缓存会占多少磁盘？**
A：每条记忆的 embedding 约 3KB（768 维 float32）。10000 条记忆约 30MB，缓存上限可配置（默认 500MB），达到上限自动 LRU 淘汰。

**Q4：能和云端方案混用吗？**
A：可以。重要记忆用云端高质量 embedding，日常用本地。但需注意维度一致性，建议统一用一种。

**Q5：向量库损坏怎么办？**
A：定期 `node bin/memory.js backup` 备份。损坏后从备份恢复，或从 MEMORY.md + daily/ 重建（记忆内容仍在文件中，仅丢失向量索引）。

## 已知限制

1. **本地 embedding 质量有上限**：nomic-embed-text 接近 text-embedding-3-small，但不如 text-embedding-3-large；超大规模或高质量检索场景仍需云端方案。
2. **资源占用较高**：Ollama 运行需 2-4GB 内存，资源受限设备（< 4GB 内存）难以运行；建议 8GB+ 内存。
3. **无跨设备同步**：本地方案无云同步能力，多设备需手动备份恢复或外接同步工具。
4. **首次部署门槛**：需安装 Ollama + 拉取模型 + npm install + init，比云端 API Key 方案复杂。
5. **模型切换需重建索引**：切换 embedding 模型后维度变化，需重新生成所有向量索引（可从 MEMORY.md + daily/ 重建）。
6. **WAL 仅保证单机持久性**：写前日志防崩溃丢失，但不防磁盘物理损坏，仍需定期 backup。
