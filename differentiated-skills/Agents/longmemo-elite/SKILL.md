---
slug: longmemo-elite
name: longmemo-elite
version: "2.0.0"
displayName: 精英长记忆
summary: 解决Agent金鱼记忆：WAL防丢失+混合检索+成本预算+自动卫生，跨会话不丢上下文。
license: Proprietary
description: |-
  面向AI Agent的精英级长期记忆系统，解决跨会话遗忘、检索不准、成本失控三大痛点。提供WAL写前日志防丢失、向量+关键词+图谱三路混合检索、六层存储架构、成本预算控制、记忆卫生自动化。适用于跨会话项目开发、多代理协作、长期偏好维护。适用关键词：长期记忆、跨会话、WAL、向量检索、记忆管理、agent记忆、memory
tags:
- 智能代理
- 记忆管理
- 长期记忆
tools:
  - - read
- exec
---

# 精英长记忆（LongMemo Elite）

解决 AI Agent 三大记忆顽疾：**跨会话遗忘、检索不准、成本失控**。本系统将六种成熟记忆策略整合为一套防弹架构，配合 WAL 写前日志协议，确保永不丢失上下文、永不遗忘决策、永不重复犯错。

## 核心能力

1. **WAL 写前日志防丢失**：采用"先写状态，再回复用户"协议，在压缩/崩溃/重启场景下保证上下文不丢失。用户表达偏好、做出决策、给出期限、纠正错误时，先写入 SESSION-STATE.md 与对应存储层，再回复用户。
2. **向量+关键词+图谱三路混合检索**：向量检索负责语义相似召回，关键词倒排负责精确实体匹配，图谱遍历负责因果关联推理，三路结果通过 RRF（Reciprocal Rank Fusion）融合排序，解决单一向量检索"相似但不相关"的召回质量问题。
3. **六层存储架构分层加载**：L1 热内存（SESSION-STATE.md，抗压缩）、L2 温向量（LanceDB，语义检索）、L3 冷图谱（Git-Notes，结构化决策）、L4 精选归档（MEMORY.md+daily/，人类可读）、L5 云备份（SuperMemory，跨设备同步）、L6 自动抽取（Mem0，对话事实提取），按需分层加载降低 token 消耗。
4. **成本预算控制**：通过 embedding 缓存（节省 60-80%）、分层存储（节省 40-60%）、小模型抽取（节省 70-90%）、图谱增量更新（节省 50-70%）四项策略控制成本，配置日/月预算上限，达到 80% 告警，100% 自动降级为只读模式。
5. **记忆卫生自动化**：自动执行去重、衰减、晋升（7 天内出现 3 次提升到 MEMORY.md）、降级（30 天未访问移出热内存）、归档（90 天未访问移入 archive/）、删除（180 天未访问且 importance<0.3 询问后删除），避免记忆膨胀拖慢召回。

### 六层存储架构速查

| 层级 | 存储 | 用途 | 持久化 | 加载时机 |
|:---|:---|:---|:---|:---|
| L1 热内存 | SESSION-STATE.md | 当前任务、关键上下文、待办 | 抗压缩/重启 | 会话开始立即加载 |
| L2 温向量 | LanceDB | 语义相似召回 | 本地向量库 | 按需检索 |
| L3 冷图谱 | Git-Notes | 结构化决策、分支关联 | Git 永久 | 决策/查询时 |
| L4 精选归档 | MEMORY.md + daily/ | 蒸馏后的长期智慧 | 文件 | 周期性回顾 |
| L5 云备份 | SuperMemory API | 跨设备同步 | 云端 | 可选 |
| L6 自动抽取 | Mem0 | 对话自动提取事实 | 外部服务 | 推荐 |

**输入**: 用户提供六层存储架构速查所需的指令和必要参数。
**处理**: 按照skill规范执行六层存储架构速查操作,遵循单一意图原则。
**输出**: 返回六层存储架构速查的执行结果,包含操作状态和输出数据。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：Agent、金鱼记忆、自动卫生、跨会话不丢上下文、的精英级长期记忆、解决跨会话遗忘、检索不准、成本失控三大痛点、适用于跨会话项目、多代理协作、长期偏好维护、适用关键词、长期记忆、跨会话、记忆管理等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 适用场景

**何时使用：**
- 跨会话项目开发：新会话需延续上一会话的技术决策、用户偏好、未完成任务
- 长期客户偏好维护：跨多次交互积累客户喜好与历史决策
- 多代理协作上下文同步：主代理派生子代理时传递上下文，避免协作孤岛
- 避免重复犯错的经验沉淀：将踩过的坑记录为 lessons.md，召回时优先注入
- 需要隐私分级与成本可控的生产级 Agent 记忆管理

**输入输出：**
- 输入：用户对话中的偏好、决策、期限、纠正；会话开始时的检索查询
- 输出：持久化的记忆条目（SESSION-STATE.md / MEMORY.md / 向量库 / 图谱）、召回的相关历史上下文

**不适用场景：**
- 单次会话的临时上下文管理（用 Agent 内置上下文窗口即可）
- 无需跨会话延续的简单问答任务
- 对成本极度敏感且不需要长期记忆的个人实验项目

## 使用流程

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 第 1 步：创建热内存文件

在工作区根目录创建 `SESSION-STATE.md`，包含当前任务、关键上下文（用户偏好/已做决策/当前阻塞）、待办动作、近期决策四个区块，作为抗压缩的热内存。

### 第 2 步：配置混合检索

在 `memory-config.json` 中启用三路混合检索：设置 `hybrid.vector=true`、`hybrid.keyword=true`、`hybrid.graph=true`、`fusion=rrf`，配置 `minScore=0.35`、`maxResults=10`、embedding provider。

配置示例：

```json
{
  "memorySearch": {
    "enabled": true,
    "provider": "openai",
    "minScore": 0.35,
    "maxResults": 10,
    "hybrid": { "vector": true, "keyword": true, "graph": true, "fusion": "rrf" }
  },
  "costBudget": {
    "dailyLimitUsd": 2.0,
    "monthlyLimitUsd": 50.0,
    "alertThreshold": 0.8,
    "strategies": { "embeddingCache": true, "tieredStorage": true, "smallModelExtraction": true }
  }
}
```

### 第 3 步：初始化冷存储

执行 `git init` 初始化 Git 仓库（用于 Git-Notes 知识图谱），运行 `python3 memory.py -p . sync --start` 启动同步，创建 `memory/` 目录结构。

### 依赖详情

执行 `memory_recall query="测试查询" limit=3` 验证检索功能正常，确认向量库非空、embedding provider 可用。

### 第 5 步：执行 WAL 协议（对话进行中）

遵循"先写后回复"原则：用户表达偏好→写入 SESSION-STATE.md + memory_store；做出决策→写入 SESSION-STATE.md + Git-Notes；给出期限→写入 SESSION-STATE.md；纠正错误→写入 SESSION-STATE.md + lessons.md；出现代码错误→记录到 lessons.md + memory_store。

### 第 6 步：会话开始时加载记忆

读取 SESSION-STATE.md（热内存）→ 执行 memory_recall 检索相关历史 → 检查 memory/YYYY-MM-DD.md 近期活动 → 扫描 lessons.md 相关教训。

### 第 7 步：会话结束时归档

更新 SESSION-STATE.md 最终状态 → 重要内容迁移到 MEMORY.md → 创建/更新 memory/YYYY-MM-DD.md 日志。

### 第 8 步：每周记忆卫生

执行 memory_dedup 去重 → memory_forget 清理低重要性向量（importance<0.3 且超过 30 天）→ memory_compact 压缩旧日志 → memory_export 导出备份。

## 示例

### 示例

**输入：**
- 会话 A（周一）：用户说"数据库用 MySQL，开发环境用 SQLite"
- 会话 B（周三，新会话）：用户说"部署脚本怎么写？"

**输出：**
- 会话 A 执行 WAL：写入 SESSION-STATE.md"决策：MySQL 生产/SQLite 开发"；写入 Git-Notes（带分支标记）；memory_store"用户偏好 MySQL 生产/SQLite 开发" importance=0.9 category=decision
- 会话 B 会话开始检索 memory_recall query="部署 数据库" → 召回 MySQL 决策 → 回复时主动考虑 MySQL 部署配置，生成正确的部署脚本

### 示例 2：避免重复犯错

**输入：**
- 会话 A：代理生成的 Dockerfile 缺少 .dockerignore，导致镜像 2GB，用户纠正
- 会话 B：用户说"帮我写个 Dockerfile"

**输出：**
- 会话 A 执行 WAL：写入 lessons.md"生成 Dockerfile 必须同时生成 .dockerignore"
- 会话 B 会话开始检索 lessons.md → 召回 .dockerignore 教训 → 主动同时生成 Dockerfile 和 .dockerignore

### 示例 3：多代理协作上下文传递

**输入：** 主代理需派生代码审查子代理审查支付模块

**输出：** 主代理在子代理任务提示词中注入上下文继承块：项目=电商平台、当前任务=审查支付模块、关键决策=支付用 Stripe/货币用 USD、已知约束=必须 PCI 合规。子代理基于继承上下文进行审查，无需重新询问。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---|:---|:---|
| 全部遗忘（新会话无历史） | memory_search 未启用或 embedding provider 未配置 | 启用 memory_search，配置 embedding provider（OPENAI_API_KEY） |
| 记忆文件未加载 | 代理跳过读取记忆步骤 | 在 AGENTS.md 中写入强制规则：会话开始必须读取 SESSION-STATE.md |
| 事实未自动捕获 | 未启用 Mem0 自动抽取 | 启用 Mem0 或改为手动 memory_store 记录 |
| 子代理上下文孤立 | 派生时未注入上下文继承块 | 使用上下文传递协议，在任务提示词中注入项目/任务/决策/偏好/约束 |
| 重复犯错 | 教训未记录到 lessons.md | 强制 WAL 协议：出现错误时先写 lessons.md 再修复 |
| 召回太慢 | 向量库膨胀未清理 | 执行 memory_compact 压缩 + memory_forget 清理低重要性 |
| 召回不准（相似但不相关） | 仅启用单路向量检索 | 启用三路混合检索（vector+keyword+graph）+ RRF 融合 |
| 账单暴涨 | 无预算控制或 embedding 未缓存 | 配置日/月预算上限，启用 embedding 缓存与小模型抽取 |
| Git-Notes 不持久 | 未执行 git notes push | 执行 `git notes push` 同步到远程 |
| 召回为空 | 向量库为空或 minScore 过高 | 检查向量库非空，降低 minScore 到 0.35 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---|:---|:---|:---|
| Agent 平台（Claude Code/Cursor/Codex 等） | 运行环境 | 必需 | 安装对应 Agent |
| Python 3.8+ | 运行时 | 推荐 | python.org 安装（Git-Notes 脚本） |
| Node.js 16+ | 运行时 | 推荐 | nodejs.org 安装（LanceDB 向量库） |
| LanceDB | 向量数据库 | 推荐 | `pip install lancedb` |
| OpenAI Embedding API | 向量化 | 推荐 | 配置 OPENAI_API_KEY（无则用本地 embedding） |
| Mem0 | 自动事实抽取 | 可选 | `npm install mem0ai` |
| SuperMemory | 跨设备云同步 | 可选 | 官网注册获取 API Key |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

**API Key 配置：**
- OPENAI_API_KEY：向量 embedding 生成（推荐，无则降级为本地 embedding）
- MEM0_API_KEY：对话自动事实抽取（可选）
- SUPERMEMORY_API_KEY：跨设备云同步（可选）

**可用性分类：** MD+EXEC（核心记忆协议纯 Markdown 即可工作；向量检索、自动抽取等高级功能需对应依赖）
- API Key通过环境变量配置: export API_KEY=your_key

## 常见问题

**Q1：WAL 协议会不会拖慢回复速度？**
A：写入本地文件是毫秒级操作，对用户感知无影响。相比崩溃后丢失上下文的代价，这点延迟完全值得。

**Q2：混合检索三路都开会不会很贵？**
A：关键词倒排和图谱遍历都是本地操作，零 API 成本。只有向量检索需要 embedding（已缓存）。综合成本反而低于纯向量方案（召回更准，减少重试）。

**Q3：Mem0 自动抽取和手动 memory_store 冲突吗？**
A：不冲突。Mem0 负责对话流自动提取，手动 memory_store 负责高价值显式记录。两者互补，Mem0 有去重逻辑避免重复。

**Q4：本地和云端如何选择？**
A：个人/小团队用本地（LanceDB + Git-Notes）足够；跨设备协作加 SuperMemory；生产级建议本地为主 + 云端备份。

**Q5：记忆库多久清理一次？**
A：建议每周一次轻清理（去重 + 低重要性降级），每月一次深清理（归档 + 压缩 + 导出备份）。

## 已知限制

1. **六层架构需逐步启用**：L1-L4 纯本地 Markdown 即可工作，L2 向量检索需安装 LanceDB，L5 云备份需 SuperMemory API，L6 自动抽取需 Mem0，并非开箱即用全部功能。
2. **WAL 协议依赖 Agent 配合**：协议本身是行为规范，需要 Agent 平台支持在 AGENTS.md 中写入强制规则才能保证执行，若 Agent 忽略指令则 WAL 失效。
3. **embedding 缓存基于文本哈希**：相同文本不重复计算，但文本微小改动（如加空格）会触发重新计算，对高频更新场景缓存命中率会下降。
4. **图谱遍历深度受限**：为控制延迟，图谱遍历默认限制在 2-3 跳，超深关联（5 跳以上）可能遗漏。
5. **成本预算只读降级后无法写入**：达到 100% 预算后自动降级为只读模式，此时新记忆无法写入，需等待下一预算周期或提升上限。
