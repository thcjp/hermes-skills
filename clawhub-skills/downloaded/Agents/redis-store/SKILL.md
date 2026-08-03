---
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
summary: "Redis缓存用法,每个key设TTL过期防泄漏"
---
# Redis

## Expiration (Memory Leaks)

* Keys without TTL live forever—set expiry on every cache key: `SET key value EX 3600`
* Can't add TTL after SET without another command—use `SETEX` or `SET ... EX`
* `EXPIRE` resets on key update by default—`SET` removes TTL; use `SET ... KEEPTTL` (Redis 6+)
* Lazy expiration: expired keys removed on access—may consume memory until touched
* `SCAN` with large database: expired keys still show until cleanup cycle runs

## Data Structures I Underuse

* Sorted sets for rate limiting: `ZADD limits:{user} {now} {request_id}` + `ZREMRANGEBYSCORE` for sliding window
* HyperLogLog for unique counts: `PFADD visitors {ip}` uses 12KB for billions of uniques
* Streams for queues: `XADD`, `XREAD`, `XACK`—better than LIST for reliable queues
* Hashes for objects: `HSET user:1 name "Alice" email "a@b.com"`—more memory efficient than JSON string

## Atomicity Traps

* `GET` then `SET` is not atomic—another client can modify between; use `INCR`, `SETNX`, or Lua
* `SETNX` for locks: `SET lock:resource {token} NX EX 30`—NX = only if not exists
* `WATCH`/`MULTI`/`EXEC` for optimistic locking—transaction aborts if watched key changed
* Lua scripts are atomic—use for complex operations: `EVAL "script" keys args`

## 已知限制

* Messages not persisted—subscribers miss messages sent while disconnected
* At-most-once delivery—no acknowledgment, no retry
* Use Streams for reliable messaging—`XREAD BLOCK` + `XACK` pattern
* Pub/Sub across cluster: message goes to all nodes—works but adds overhead

## Persistence Configuration

* RDB (snapshots): fast recovery, but data loss between snapshots—default every 5min
* AOF (append log): less data loss, slower recovery—`appendfsync everysec` is good balance
* Both off = pure cache—acceptable if data can be regenerated
* `BGSAVE` for manual snapshot—doesn't block but forks process, needs memory headroom

## Memory Management (Critical)

* `maxmemory` must be set—without it, Redis uses all RAM, then swap = disaster
* Eviction policies: `allkeys-lru` for cache, `volatile-lru` for mixed, `noeviction` for persistent data
* `INFO memory` shows usage—monitor `used_memory` vs `maxmemory`
* Large keys hurt eviction—one 1GB key evicts poorly; prefer many small keys

## Clustering

* Hash slots: keys distributed by hash—same slot required for multi-key operations
* Hash tags: `{user:1}:profile` and `{user:1}:sessions` go to same slot—use for related keys
* No cross-slot `MGET`/`MSET`—error unless all keys in same slot
* `MOVED` redirect: client must follow—use cluster-aware client library

## Common Patterns

* Cache-aside: check Redis, miss → fetch DB → write Redis—standard caching
* Write-through: write DB + Redis together—keeps cache fresh
* Rate limiter: `INCR requests:{ip}:{minute}` with `EXPIRE`—simple fixed window
* Distributed lock: `SET ... NX EX` + unique token—verify token on release

## Connection Management

* Connection pooling: reuse connections—creating is expensive
* Pipeline commands: send batch without waiting—reduces round trips
* `QUIT` on shutdown—graceful disconnect
* Sentinel or Cluster for HA—single Redis is SPOF

## Common Mistakes

* No TTL on cache keys—memory grows until OOM
* Using as primary database without persistence—data loss on restart
* Blocking operations in single-threaded Redis—`KEYS *` blocks everything; use `SCAN`
* Storing large blobs—Redis is RAM; 100MB values are expensive
* Ignoring `maxmemory`—production Redis without limit will crash host

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

- Use Redis effectively for caching, queues, and data structures with
  proper expiration and persist
- 触发关键词: redis, caching, queues, data, store, effectively

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```

```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Redis？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Redis有什么限制？
A: 请参考已知限制章节了解具体限制。

---
## 边界条件与限制

### 输入限制
- **键值对大小限制**：Redis对单个键值对的大小有限制，通常为512MB。超过此限制的键值对无法存储在Redis中。
- **键名长度限制**：键名长度不能超过255个字节。
- **数据类型限制**：Redis支持的数据类型有限，包括字符串、列表、集合、有序集合、哈希表和流。不支持其他复杂的数据结构。

### 性能边界
- **内存限制**：Redis运行在内存中，因此其性能受限于可用内存的大小。超过`maxmemory`配置的内存会导致数据被淘汰。
- **并发限制**：Redis是单线程的，因此在高并发情况下可能会出现性能瓶颈。使用Redis集群或哨兵可以提升并发处理能力。

### 兼容性约束
- **操作系统兼容性**：Redis在大多数操作系统上都能运行，但某些功能可能在不同操作系统之间存在差异。
- **版本兼容性**：不同版本的Redis在功能上可能存在差异，使用时应注意版本兼容性。

### TTL限制
- **TTL范围**：Redis的TTL（Time To Live）范围通常为1秒到2^32-1秒（约1439年）。
- **TTL精度**：Redis的TTL精度为秒级，无法设置更精确的时间间隔。

### 持久性限制
- **RDB快照频率**：RDB快照的频率由配置决定，默认为5分钟。频繁的快照会增加磁盘I/O压力。
- **AOF日志频率**：AOF日志的频率由配置决定，包括`appendfsync`选项。较高的频率会增加磁盘I/O压力，但能提供更好的数据持久性。

### 分布式限制
- **集群节点数量**：Redis集群支持最多16384个节点。
- **跨节点操作**：跨节点的操作（如`MGET`和`MSET`）需要所有键都在同一个哈希槽中。

### 安全限制
- **密码认证**：Redis默认不开启密码认证，容易受到未授权访问。建议开启密码保护。
- **网络隔离**：Redis默认监听所有网络接口，容易受到网络攻击。建议限制监听接口或使用防火墙。

---

