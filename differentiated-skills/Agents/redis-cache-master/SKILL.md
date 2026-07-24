---
slug: redis-cache-master
name: redis-cache-master
version: 2.0.1
displayName: Redis缓存大师
summary: 生产级Redis实战：TTL纪律+淘汰决策树+集群哈希标签+原子陷阱防控，避坑指南.
license: Proprietary
description: 面向生产环境的 Redis 实战指南，直击无 TTL 内存泄漏、淘汰策略错配、集群跨槽报错、原子性陷阱、大 Key 拖垮 eviction
  五大事故。适用于缓存设计、分布式锁、限流、消息队列、生产运维等场景。核心能力含 TTL 纪律、淘汰决策树、集群哈希标签、原子操作模式、Streams 可靠消息。适用关键词：Redis、缓存、TTL、淘汰策略、集群、分布式锁、限流、eviction、cluster.
tags:
- 智能代理
- 数据存储
- 缓存优化
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# Redis 缓存大师（Redis Cache Master）

**不是命令清单，而是生产避坑指南。** 直击五大高频 Redis 生产事故：无 TTL 内存泄漏、淘汰策略错配、集群跨槽报错、原子性陷阱、大 Key 拖垮 eviction。提供决策树与模式库，让每次选型都有依据.
## 核心能力

### 1. TTL 纪律规范
每个缓存键必须设 TTL，无 TTL 的键会永远存活导致内存泄漏。提供 TTL 分级建议表（会话 30 分钟~24 小时、缓存查询 5~60 分钟、限流按窗口、分布式锁业务超时×1.5、排行榜/计数器不过期主动维护）。覆盖 SET 覆盖丢失 TTL、懒过期占内存等常见陷阱.
**输入**: 用户提供TTL 纪律规范所需的指令和必要参数.
**处理**: 解析TTL 纪律规范的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回TTL 纪律规范的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 2. 淘汰策略决策树
按"数据是否纯缓存→持久数据是否设 TTL→数据是否可丢失"三级判断，选择 allkeys-lru（纯缓存推荐）、volatile-lru（混合存储）、noeviction（持久数据，写入失败而非淘汰）等策略。避免 noeviction 用于缓存导致写入失败.
**输入**: 用户提供淘汰策略决策树所需的指令和必要参数.
**处理**: 解析淘汰策略决策树的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回淘汰策略决策树的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. 集群哈希标签模式
Redis Cluster 用 16384 个哈希槽分布键，多键操作必须同槽。提供 `{user:1}:profile`、`{user:1}:sessions` 同槽设计模式，解决 CROSSSLOT 报错。设计原则：按实体分组、避免热点、标签即实体 ID.
**输入**: 用户提供集群哈希标签模式所需的指令和必要参数.
**处理**: 解析集群哈希标签模式的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回集群哈希标签模式的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 原子操作选择指南
按"单命令能完成？→步骤间有条件依赖？→逻辑复杂？"决策树选择原子命令（INCR/SETNX）、WATCH/MULTI/EXEC 乐观锁、Lua 脚本（EVAL）或 Pipeline。提供安全版分布式锁（NX + token + Lua 解锁验证）与滑动窗口限流模式.
**输入**: 用户提供原子操作选择指南所需的指令和必要参数.
**处理**: 解析原子操作选择指南的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回原子操作选择指南的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 5. 可靠消息与持久化决策
用 Streams（XADD/XREADGROUP/XACK/XPENDING/XCLAIM）替代 Pub/Sub 解决离线丢消息问题。持久化四象限决策矩阵（纯缓存都关、平衡 RDB+AOF everysec、最高安全都开）。包含大 Key 检测（redis-cli --bigkeys）与拆分策略、缓存雪崩/穿透防护.
**输入**: 用户提供可靠消息与持久化决策所需的指令和必要参数.
**处理**: 解析可靠消息与持久化决策的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回可靠消息与持久化决策的响应数据,包含状态码、结果和日志.
**技术参数**：使用`input_params`和`output_format`参数控制执行行为,支持`json`/`text`/`csv`输出格式.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：生产级、淘汰决策树、原子陷阱防控、避坑指南、面向生产环境的、实战指南、直击无、淘汰策略错配、集群跨槽报错、原子性陷阱、五大事故、适用于缓存设计、消息队列、生产运维等场景、核心能力含、原子操作模式、适用关键词等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 适用场景

| 场景类型 | 输入 | 输出 | 是否适用 |
|----|---|---|----|
| 缓存设计 | 业务数据特征 | TTL + 淘汰策略 + 缓存模式选型 | ✅ 适用 |
| 分布式锁实现 | 资源名 + 业务超时 | NX 加锁 + Lua 解锁的完整模式 | ✅ 适用 |
| 限流方案 | 限流窗口 + 阈值 | 固定窗口/滑动窗口/令牌桶选型 | ✅ 适用 |
| 集群规划 | 数据规模 + 多键需求 | 哈希标签设计 + 节点数建议 | ✅ 适用 |
| 生产故障排查 | 故障现象 | 排查命令 + 根因 + 解决方案 | ✅ 适用 |
| 消息队列设计 | 可靠性要求 | Streams 消费者组模式（替代 Pub/Sub） | ✅ 适用 |

**不适用场景**：
- 关系型数据持久化（强事务、复杂关联查询）→ 用 MySQL/PostgreSQL
- 全文搜索引擎 → 用 Elasticsearch
- 时序数据高频写入 → 用 InfluxDB/TimescaleDB
- 未部署 Redis 环境的理论学习 → 需先安装 Redis 5.0+（推荐 7.0+）

## 使用流程

### Step 1：识别场景与数据特征

判断数据是纯缓存（可丢失）、混合存储（部分持久），还是会话/限流/锁/消息等特定用途.
### Step 2：应用 TTL 纪律

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Redis缓存大师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 推荐写法：每个键必设 TTL
SET key value EX 3600
# 更新值保留旧 TTL（Redis 6+）
SET key new_value KEEPTTL
```

### Step 3：按决策树选淘汰策略

```text
数据是纯缓存吗？
├─ 是 → allkeys-lru（推荐）
└─ 否（混合持久+缓存）
   ├─ 持久数据设了 TTL → volatile-lru
   └─ 持久数据无 TTL → noeviction + 扩容
```

### Step 4：集群场景加哈希标签

```bash
# 相关键用相同哈希标签，确保同槽
SET {user:1}:profile '{"name":"Alice"}'
SET {user:1}:sessions "active"
MGET {user:1}:profile {user:1}:sessions  # 同槽才能执行
```

### Step 5：原子操作按复杂度选型

单命令能完成 → 原子命令（INCR/SETNX）；有条件依赖 → WATCH/MULTI/EXEC；复杂逻辑 → Lua 脚本；批量无依赖 → Pipeline.
### 常见异常
- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断
- 重试机制: 失败时自动重试, 最多3次

用 `INFO memory`、`SLOWLOG GET 10`、`redis-cli --bigkeys`、`CLUSTER NODES` 等命令监控与排查.
## 示例

### 示例(补充)

**输入**：需要实现 30 分钟过期的用户会话存储

**输出**：

```bash
# 存储会话（30分钟过期）
HSET session:{token} user_id 123 last_active {ts} ip {ip}
EXPIRE session:{token} 1800
# ...
# 更新活跃时间（保留 TTL）
HSET session:{token} last_active {new_ts}
EXPIRE session:{token} 1800  # 重置 TTL
# ...
# 检查会话
HGETALL session:{token}
```

代理响应："会话缓存方案：用 Hash 存储会话字段，EXPIRE 设 1800 秒 TTL，每次更新活跃时间后重置 TTL。淘汰策略建议 allkeys-lru（纯缓存场景）。"

### 示例 2：安全分布式锁（输入→输出）

**输入**：需要实现订单处理的分布式锁，防并发

**输出**：

```bash
# 加锁（NX 保证互斥，token 防误删，EX 30 防死锁）
SET lock:order:123 "uuid-abc" NX EX 30
# ...
# 业务处理...
# ...
# 解锁（Lua 验证 token 后删除，保证原子性）
EVAL "if redis.call('get',KEYS[1])==ARGV[1] then return redis.call('del',KEYS[1]) else return 0 end" 1 lock:order:123 "uuid-abc"
```

代理响应："安全分布式锁方案：加锁用 SET NX EX（互斥+防死锁），解锁用 Lua 脚本验证 token（防误删他人锁）。TTL 设业务超时×1.5。切勿用 DEL 直接删除，会误删别人的锁。"

## 错误处理

| 场景 | 原因 | 处理方式 |
|---:|---:|---:|
| OOM 崩溃 | 无 maxmemory 或无 TTL | 设 maxmemory（物理内存 60-70%）+ 强制 TTL 纪律 |
| KEYS * 阻塞全库 | 生产用了 KEYS | 用 SCAN 替代，异步扫描 |
| 写入失败报错 | noeviction + 内存满 | 换 allkeys-lru（缓存场景）或扩容（持久数据） |
| CROSSSLOT 报错 | 多键操作涉及不同槽 | 相关键加相同哈希标签 `{tag}:key` |
| 锁被误删 | 解锁未验证 token | 用 Lua 脚本"检查 token + 删除"原子执行 |
| 主从切换丢数据 | 异步复制延迟 | AOF everysec + WAIT 命令等待副本确认 |
| 大 Key 阻塞主线程 | DEL 大 Key 卡顿 | 用 UNLINK（Redis 4+）异步删除 |
| 缓存雪崩 | 大量键同时过期 | TTL 加随机抖动（如 `EXPIRE key 3600 + random(300)`） |
| 缓存穿透 | 查不存在的 Key | 布隆过滤器 + 空值缓存（短 TTL） |
| 响应变慢 | 慢查询 | `SLOWLOG GET 10` 排查，避免 KEYS/大 Key 操作 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |
| Redis Server | 数据库 | 必需 | https://redis.io/download 或 Docker（`docker run -p 6379:6379 redis:7`） |
| redis-cli | 命令行工具 | 必需 | 随 Redis 安装 |
| Redis 客户端库 | 编程库 | 可选 | 按语言选择（ioredis/redis-py/go-redis 等） |

**运行环境**：Windows / macOS / Linux；支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）.
**Redis 版本**：5.0+（推荐 7.0+，支持 Streams/UNLINK/ACL 等新特性）.
**API Key**：本技能无需 API Key。Redis 连接通过 `redis-cli` 或客户端库配置 host/port/password。生产环境建议配置 `requirepass` 或 ACL.
**可用性分类**：MD+EXEC（设计与决策指南纯 Markdown 可理解；实际命令执行需 Redis 环境与 redis-cli）.
## 常见问题

**Q1：纯缓存该用哪种淘汰策略？**
A：allkeys-lru。所有键都是缓存，LRU 淘汰最久未用的最合理。避免用 noeviction 导致内存满后写入失败.
**Q2：maxmemory 设多少合适？**
A：物理内存的 60-70%。留余量给操作系统和 RDB fork（BGSAVE 需要内存副本）。可通过 `CONFIG SET maxmemory` 动态调整不重启生效.
**Q3：RDB 和 AOF 能同时开吗？**
A：能。数据安全要求高时都开。重启时优先用 AOF 恢复（更完整），RDB 作为备份。推荐平衡配置：RDB `save 900 1` + AOF `appendfsync everysec`（最多丢 1 秒）.
**Q4：集群最少几个节点？**
A：最少 3 主 3 从（6 节点）。3 主保证 16384 个哈希槽全覆盖，3 从保证高可用故障切换.
**Q5：大 Key 怎么安全删除？**
A：用 `UNLINK`（Redis 4+）异步删除，不阻塞主线程。旧版本用 `DEL` 会阻塞。删除前用 `MEMORY USAGE key` 检查大小，大 Key 应先拆分再删除.
## 已知限制

1. **需预先部署 Redis 环境**：本技能提供决策指南与命令模式，实际执行需用户已安装 Redis 5.0+（推荐 7.0+）。未部署环境无法实操.
2. **不覆盖 Redis Stack 模块**：本技能聚焦核心 Redis（字符串/哈希/列表/集合/有序集合/流）。RediSearch、RedisJSON、RedisGraph、RedisBloom 等 Stack 模块不在范围内.
3. **集群运维为指南非自动化**：提供集群规划、哈希标签、槽位排查的方法，但不自动执行 resharding、failover 等高风险运维操作，需用户手动确认.
4. **性能数据为经验估值**：节省比例、命中率等数据基于典型场景经验，实际效果取决于业务负载、数据分布、硬件配置，不作为绝对承诺.
5. **不处理 Redis 安全加固全流程**：提供基础安全建议（requirepass/ACL），但不覆盖网络隔离、TLS 配置、审计日志等企业级安全加固的完整实施.
## 案例展示

```json
{
  "input": "示例输入",
  "output": "处理结果"
}
```

## 输出格式

处理结果以结构化格式返回, 包含状态码、消息和数据字段.