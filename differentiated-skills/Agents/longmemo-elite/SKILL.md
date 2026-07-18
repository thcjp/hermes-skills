---
slug: longmemo-elite
name: longmemo-elite
version: "2.0.0"
displayName: 精英长记忆
summary: 解决Agent金鱼记忆：WAL防丢失+混合检索+成本预算+自动卫生，跨会话不丢上下文。
license: MIT
description: |-
  面向 AI Agent 的精英级长期记忆系统，直击"金鱼记忆"痛点。通过 WAL 写前日志协议保证上下文在压缩/崩溃/重启时不丢失，结合向量语义检索、关键词倒排、知识图谱三路混合召回，显著提升记忆命中率。

  核心能力包括六层存储架构（热内存/温向量/冷图谱/精选归档/云备份/自动抽取）、混合检索策略（向量+关键词+图遍历）、成本预算控制（embedding缓存+分层存储+小模型抽取+日/月预算上限）、子代理上下文传递协议、记忆卫生自动化（去重/衰减/晋升/降级）。

  适用场景：跨会话项目开发、长期客户偏好维护、多代理协作上下文同步、避免重复犯错的经验沉淀、需要隐私分级与成本可控的生产级 Agent 记忆管理。

  差异化：相比单一向量检索方案，本系统提供混合检索提升召回质量、显式成本预算防止账单失控、WAL 协议从根上解决写入丢失、子代理上下文协议解决协作孤岛、自动卫生机制避免记忆膨胀。所有指令按需分层加载，降低 token 消耗。

  触发关键词：记忆、长期记忆、上下文丢失、金鱼记忆、跨会话、WAL、向量检索、记忆管理、agent记忆、memory
tags:
- 智能代理
- 记忆管理
- 长期记忆
tools:
- read
- exec
---

# 精英长记忆（LongMemo Elite）

解决 AI Agent 三大记忆顽疾：**跨会话遗忘、检索不准、成本失控**。本系统将六种成熟记忆策略整合为一套防弹架构，配合 WAL 写前日志协议，确保永不丢失上下文、永不遗忘决策、永不重复犯错。

## 痛点与对策速查

| 用户痛点 | 发生场景 | 本系统对策 |
|:---|:---|:---|
| 金鱼记忆 | 新会话忘记上一会话内容 | WAL 协议 + SESSION-STATE.md 热内存持久化 |
| 检索不准 | 向量召回全是无关记忆 | 向量+关键词+图谱三路混合检索，投票排序 |
| 账单失控 | embedding/API 调用费用暴涨 | 成本预算上限 + embedding 缓存 + 分层存储 |
| 子代理孤岛 | 派生代理拿不到主上下文 | 上下文传递协议 + 任务提示词注入模板 |
| 记忆膨胀 | 旧记忆堆积拖慢召回 | 自动卫生：去重/衰减/晋升/降级/归档 |
| 重复犯错 | 同样的坑踩多次 | lessons.md 强制记录 + 召回时优先注入 |

## 六层存储架构

```text
┌───────────────────────────────────────────────────────────────┐
│                   LONGMEMO ELITE 六层架构                       │
├───────────────────────────────────────────────────────────────┤
│  L1 热内存      SESSION-STATE.md   活跃任务上下文（抗压缩）      │
│  L2 温向量      LanceDB            语义检索（embedding 缓存）   │
│  L3 冷图谱      Git-Notes          结构化决策（分支感知）        │
│  L4 精选归档    MEMORY.md + daily/ 人类可读长期记忆             │
│  L5 云备份      SuperMemory        跨设备同步（可选）           │
│  L6 自动抽取    Mem0               对话自动提取事实（推荐）     │
└───────────────────────────────────────────────────────────────┘
```

| 层级 | 存储 | 用途 | 持久化 | 加载时机 |
|:---|:---|:---|:---|:---|
| L1 热内存 | SESSION-STATE.md | 当前任务、关键上下文、待办 | 抗压缩/重启 | 会话开始立即加载 |
| L2 温向量 | LanceDB | 语义相似召回 | 本地向量库 | 按需检索 |
| L3 冷图谱 | Git-Notes | 结构化决策、分支关联 | Git 永久 | 决策/查询时 |
| L4 精选归档 | MEMORY.md + daily/ | 蒸馏后的长期智慧 | 文件 | 周期性回顾 |
| L5 云备份 | SuperMemory API | 跨设备同步 | 云端 | 可选 |
| L6 自动抽取 | Mem0 | 对话自动提取事实 | 外部服务 | 推荐 |

## 快速开始（5 分钟）

### 第 1 步：创建热内存文件

```bash
cat > SESSION-STATE.md << 'EOF'
# 会话热内存

## 当前任务
[待填写]

## 关键上下文
- 用户偏好：[待填写]
- 已做决策：[待填写]
- 当前阻塞：[待填写]

## 待办动作
- [ ] [待填写]

## 近期决策
[待填写]

---
*最后更新：[时间戳]*
EOF
```

### 第 2 步：启用混合检索

在 Agent 配置文件中启用三路混合检索：

```json
{
  "memorySearch": {
    "enabled": true,
    "provider": "openai",
    "sources": ["memory"],
    "minScore": 0.35,
    "maxResults": 10,
    "hybrid": {
      "vector": true,
      "keyword": true,
      "graph": true,
      "fusion": "rrf"
    }
  }
}
```

### 第 3 步：初始化冷存储

```bash
git init
python3 memory.py -p . sync --start
mkdir -p memory
```

### 第 4 步：验证

```bash
memory_recall query="测试查询" limit=3
```

## WAL 写前日志协议（核心）

**原则：先写状态，再回复用户。** 若先回复后崩溃/压缩，上下文必丢。

| 触发条件 | 写入动作 | 写入位置 |
|:---|:---|:---|
| 用户表达偏好 | 先写再回复 | SESSION-STATE.md + memory_store |
| 用户做出决策 | 先写再回复 | SESSION-STATE.md + Git-Notes |
| 用户给出期限 | 先写再回复 | SESSION-STATE.md |
| 用户纠正错误 | 先写再回复 | SESSION-STATE.md + lessons.md |
| 出现代码错误 | 先记录再修复 | lessons.md + memory_store |

### WAL 执行示例

```text
用户："这个项目用 Tailwind，不要原生 CSS"

代理内部执行顺序：
1. 写入 SESSION-STATE.md："决策：使用 Tailwind，弃用原生 CSS"
2. 写入 Git-Notes：CSS 框架决策（带分支标记）
3. memory_store："用户偏好 Tailwind 胜于原生 CSS" importance=0.9
4. 然后才回复用户："收到，采用 Tailwind..."
```

## 混合检索策略（差异化核心）

单一向量检索的缺陷：相似但不相关的内容也会被召回。本系统采用三路混合 + 排序融合：

```text
查询 → ┬→ 向量检索（语义相似）────────────┐
       ├→ 关键词倒排（精确匹配）──────────┤→ RRF 融合排序 → Top-K 结果
       └→ 图谱遍历（关联推理）────────────┘
```

| 检索路 | 擅长 | 召回质量 |
|:---|:---|:---|
| 向量 | 语义相似、模糊意图 | 召回宽，精度中 |
| 关键词 | 精确实体、代码符号 | 精度高，召回窄 |
| 图谱 | 因果关联、时间序列 | 关联强，覆盖深 |

**RRF（Reciprocal Rank Fusion）融合公式**：`score = Σ 1/(rank_i + 60)`，三路排名融合后取 Top-K。

## 成本预算控制（差异化核心）

记忆系统四大成本源：embedding 生成、向量存储、LLM 事实抽取、图谱处理。无预算控制会导致账单失控。

| 成本源 | 优化策略 | 预期节省 |
|:---|:---|:---|
| embedding 生成 | 缓存 embedding 结果，相同文本不重复计算 | 60-80% |
| 向量存储 | 分层存储，低重要性记忆降级到文件 | 40-60% |
| LLM 事实抽取 | 用小模型（如 Haiku）做抽取，大模型仅做关键决策 | 70-90% |
| 图谱处理 | 增量更新，避免全量重建 | 50-70% |

### 预算配置模板

```json
{
  "costBudget": {
    "dailyLimitUsd": 2.0,
    "monthlyLimitUsd": 50.0,
    "alertThreshold": 0.8,
    "strategies": {
      "embeddingCache": true,
      "tieredStorage": true,
      "smallModelExtraction": true,
      "incrementalGraph": true
    }
  }
}
```

达到 80% 阈值告警，达到 100% 自动降级为只读模式（仅检索不写入）。

## 子代理上下文传递协议

派生子代理默认拿不到主代理上下文，导致协作孤岛。解决方法：

```text
[主代理派生子代理时，在任务提示词中注入以下上下文块]

## 上下文继承
- 项目：[项目名]
- 当前任务：[来自 SESSION-STATE.md]
- 关键决策：[来自 Git-Notes，最近 3 条]
- 用户偏好：[来自 memory.md，相关条目]
- 已知约束：[来自 lessons.md，相关教训]
```

## 代理行为指令

### 会话开始时

1. 读取 SESSION-STATE.md（热内存）
2. 执行 memory_recall 检索相关历史
3. 检查 memory/YYYY-MM-DD.md 近期活动
4. 若有 lessons.md，扫描相关教训

### 对话进行中

| 情境 | 动作 |
|:---|:---|
| 用户给出具体细节 | 写入 SESSION-STATE.md 后再回复 |
| 做出重要决策 | 静默写入 Git-Notes |
| 表达偏好 | memory_store importance=0.9 |
| 出现错误 | 写入 lessons.md |
| 派生子代理 | 注入上下文继承块 |

### 会话结束时

1. 更新 SESSION-STATE.md 最终状态
2. 重要内容迁移到 MEMORY.md
3. 创建/更新 memory/YYYY-MM-DD.md 日志

## 记忆卫生自动化（每周）

```bash
# 查看记忆统计
memory_recall query="*" limit=50

# 去重
memory_dedup

# 清理低重要性向量
memory_forget --below-importance 0.3 --older-than 30d

# 压缩旧日志
memory_compact --before 30d

# 导出备份
memory_export --format json > memories.json
```

### 自动晋升/降级规则

| 规则 | 触发条件 | 动作 |
|:---|:---|:---|
| 晋升到热内存 | 信号 7 天内出现 3 次 | 提升到 MEMORY.md |
| 降级到温存储 | 记录 30 天未访问 | 从热内存移除 |
| 归档到冷存储 | 记录 90 天未访问 | 移入 archive/ |
| 删除 | 180 天未访问且 importance<0.3 | 询问后删除 |

## 真实场景示例

### 场景 1：跨会话项目开发

```text
会话 A（周一）：
  用户："数据库用 MySQL，开发环境用 SQLite"
  → WAL 写入决策到 SESSION-STATE.md + Git-Notes
  → memory_store："MySQL 生产 / SQLite 开发" importance=0.9 category=decision

会话 B（周三，新会话）：
  用户："部署脚本怎么写？"
  → 会话开始检索 memory_recall query="部署 数据库"
  → 召回 MySQL 决策
  → 回复时主动考虑 MySQL 部署配置
```

### 场景 2：避免重复犯错

```text
会话 A：
  代理生成的 Dockerfile 缺少 .dockerignore，导致镜像 2GB
  → 用户纠正
  → WAL 写入 lessons.md："生成 Dockerfile 必须同时生成 .dockerignore"

会话 B：
  用户："帮我写个 Dockerfile"
  → 会话开始检索 lessons.md 相关条目
  → 召回 .dockerignore 教训
  → 主动同时生成 .dockerignore
```

### 场景 3：多代理协作

```text
主代理派生代码审查子代理：
  注入上下文继承块：
    - 项目：电商平台
    - 当前任务：审查支付模块
    - 关键决策：支付用 Stripe，货币用 USD
    - 已知约束：必须 PCI 合规
  子代理基于继承上下文进行审查，无需重新询问
```

## 记忆失败模式与修复

| 失败模式 | 根因 | 修复 |
|:---|:---|:---|
| 全部遗忘 | memory_search 未启用 | 启用 + 配置 embedding provider |
| 文件未加载 | 代理跳过读取记忆 | 写入 AGENTS.md 强制规则 |
| 事实未捕获 | 无自动抽取 | 启用 Mem0 或手动记录 |
| 子代理孤立 | 未继承上下文 | 使用上下文传递协议 |
| 重复犯错 | 教训未记录 | 强制 lessons.md 写入 |
| 召回太慢 | 向量库膨胀 | 执行卫生清理 + 压缩 |
| 召回不准 | 单路检索 | 启用三路混合检索 |
| 账单暴涨 | 无预算控制 | 配置日/月预算上限 |

## 常见问题 FAQ

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

## 故障排查

| 现象 | 排查步骤 |
|:---|:---|
| 代理对话中遗忘 | 检查 SESSION-STATE.md 是否在更新；验证 WAL 协议执行 |
| 召回无关记忆 | 提高 minScore 到 0.4+；关闭 autoCapture；提高 minImportance |
| 召回为空 | 检查 embedding provider 配置；确认向量库非空 |
| 记忆库过大 | 运行 compact；清理低重要性；归档旧日志 |
| Git-Notes 不持久 | 执行 `git notes push` 同步到远程 |
| 成本超预算 | 检查 embedding 缓存是否生效；降低抽取频率；启用小模型 |

## 文件结构总览

```text
workspace/
├── SESSION-STATE.md          # L1 热内存
├── MEMORY.md                 # L4 精选归档（<5KB 摘要）
├── AGENTS.md                 # 代理行为规则（含记忆协议）
├── memory/
│   ├── vectors/              # L2 LanceDB 向量库
│   ├── 2026-07-18.md         # 每日日志
│   ├── topics/               # 主题文件
│   ├── lessons.md            # 教训记录
│   └── projects/
│       └── [项目名].md
├── .git/
│   └── notes/                # L3 Git-Notes 知识图谱
└── memory-config.json        # 记忆系统配置
```

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（用于 Git-Notes 脚本）
- **Node.js**：16+（用于 LanceDB 向量库）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---|:---|:---|:---|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| LanceDB | 向量数据库 | 推荐 | `pip install lancedb` |
| Mem0 | 自动抽取 | 可选 | `npm install mem0ai` |
| SuperMemory | 云备份 | 可选 | 官网注册获取 API Key |
| OpenAI Embedding | 向量化 | 推荐 | 配置 OPENAI_API_KEY |

### API Key 配置

| Key 名称 | 用途 | 是否必需 |
|:---|:---|:---|
| OPENAI_API_KEY | 向量 embedding 生成 | 推荐（无则用本地 embedding） |
| MEM0_API_KEY | 对话自动事实抽取 | 可选 |
| SUPERMEMORY_API_KEY | 跨设备云同步 | 可选 |

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令为主，部分功能需 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行记忆管理任务。核心记忆协议（WAL、分层加载）纯 Markdown 即可工作；向量检索、自动抽取等高级功能需对应依赖。
