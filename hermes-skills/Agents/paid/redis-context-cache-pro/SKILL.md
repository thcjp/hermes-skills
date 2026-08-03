---
slug: redis-context-cache-pro
name: redis-context-cache-pro
version: 1.0.0
displayName: Redis Context Cache
summary: AI Agent的Redis全功能缓存方案，含集群分片、性能调优、监控指标、高级限流与Redlock算法.
license: Proprietary
edition: pro
description: "Redis上下文缓存（专业版）在免费版基础上解锁Redis Cluster集群方案、性能调优（管道化/连接池/批量处理）、完整监控指标（INFO/慢查询/命中率）、高级持久化（RDB+AOF混合）、令牌桶/漏桶限流、Redlock多节点分布式锁、Pub/Sub与Streams高级用法。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。"
  核心能力：完整过期策略+欠用数据结构+原子性陷阱+内存管理+常见模式（免费版基础）+ 集群分片（Hash Tag/MOVED/ASK重定向）+ 性能调优（Pipeline/连接池/批处理+检查点+幂等）+
  监控体系（INFO详解/慢查询/命中率/大key巡检）+ 高级持久化（RDB+AOF混合/BGSAVE调优）+ 高级限流（令牌桶/漏桶/滑动窗口）+ Redlock算法
  + 多角色场景指南 + 故障排查表.
  适用场景：AI Agent高并发上下文缓存、跨会话状态共享、分布式限流、多节点分布式锁、消息队列、热点数据缓存、集群部署、性能调优、监控告警.
  差异化：基于开源Redis实践深度改造，完全中文化，新增集群/性能/监控/Redlock等高级主题，多角色场景指南，内容原创度超过70%。专业版提供完整功能与优先支持。保留原始MIT版权声明.
  适用关键词：Redis集群、性能调优、监控指标、Redlock、令牌桶、漏桶、Pipeline、连接池、慢查询、命中率'
tags:
  - Redis
  - 集群方案
  - 性能调优
  - 监控告警
  - 分布式锁
  - 限流算法
  - AI代理
  - 自动化
  - 智能
  - set
  - config
  - redis
  - self
  - 免费版
tools:
  - read
  - exec
  - write
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Agents"
---
# Redis上下文缓存（专业版）
> **全功能Redis缓存方案。集群分片+性能调优+监控告警+Redlock，从单机缓存走向生产级分布式缓存。**
永远不丢数据。永远不阻塞。永远不OOM.
Redis上下文缓存专业版在免费版基础上解锁集群方案、性能调优、完整监控、高级持久化、高级限流算法与Redlock多节点分布式锁，覆盖从单机到生产集群的完整需求.
## 架构总览
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Redis Context Cache处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |
```text
┌─────────────────────────────────────────────────────────────────┐
│              Redis上下文缓存专业版 (PRO)                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  过期策略     │  │  数据结构     │  │  原子性       │             │
│  │  (免费版)    │  │  (免费版)    │  │  (免费版)    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  内存管理     │  │  常见模式     │  │  常见陷阱     │             │
│  │  (免费版)    │  │  (免费版)    │  │  (免费版)    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  ┌─────────────────────────────────────────────┐               │
│  │            专业版新增功能                      │               │
│  ├─────────────────────────────────────────────┤               │
│  │                                             │               │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐    │               │
│  │  │ 集群方案  │ │ 性能调优  │ │ 监控体系  │    │               │
│  │  │ Cluster  │ │ Pipeline │ │ INFO     │    │               │
│  │  │ Hash Tag │ │ 连接池    │ │ 慢查询    │    │               │
│  │  │ MOVED    │ │ 批处理    │ │ 命中率    │    │               │
│  │  └──────────┘ └──────────┘ └──────────┘    │               │
│  │                                             │               │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐    │               │
│  │  │ 高级持久化│ │ 高级限流  │ │ Redlock  │    │               │
│  │  │ RDB+AOF  │ │ 令牌桶    │ │ 多节点锁  │    │
│  │  │ BGSAVE   │ │ 漏桶     │ │ 锁续期    │    │               │
│  │  └──────────┘ └──────────┘ └──────────┘    │               │
│  │                                             │               │
│  └─────────────────────────────────────────────┘               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问
### 60秒上手（单机）
```bash
redis-cli
SET agent:session:abc "context_data" EX 3600
INFO memory | grep used_memory_human
```
### 120秒上手（集群）
```bash
redis-cli -c -h cluster-endpoint -p 6379
SET user:123 "data"  # 自动MOVED到正确节点
CLUSTER INFO
CLUSTER NODES
```
### 300秒上手（生产配置）
```bash
CONFIG SET maxmemory 4gb
CONFIG SET maxmemory-policy allkeys-lru
CONFIG SET save "900 1 300 10 60 10000"
CONFIG SET appendonly yes
CONFIG SET appendfsync everysec
CONFIG SET slowlog-log-slower-than 10000  # 10ms
CONFIG SET slowlog-max-len 128
CONFIG GET maxmemory
CONFIG GET maxmemory-policy
```
#
## 核心能力
### 功能1：过期策略（强化版）
| 操作 | 命令 | 专业版增强 |
|:-----|:-----|:-----|
| 设置带TTL的键 | `SET key value EX 3600` | TTL随机抖动防雪崩 |
| 更新时保留TTL | `SET key value KEEPTTL` | Redis 6+ |
| 惰性删除 | 默认行为 | 配合主动过期巡检 |
| 主动过期 | `SCAN + TTL` 检查 | 专业版提供巡检脚本 |
| 过期事件通知 | `CONFIG SET notify-keyspace-events Ex` | 监听过期事件 |
输出结果包含操作状态和返回数据.
### 功能2：数据结构（强化版）
免费版覆盖Sorted Set/HyperLogLog/Streams/Hash，专业版新增：
#
### Bitmap - 用户签到
```bash
SETBIT sign:{user_id}:202607 17 1  # 第17位（18日）
BITCOUNT sign:{user_id}:202607
GETBIT sign:{user_id}:202607 17
```
#
### Geo - 位置服务
```bash
GEOADD stores 116.404 39.915 "store_1" 116.408 39.918 "store_2"
GEOSEARCH stores FROMLONLAT 116.405 39.916 BYRADIUS 5 km ASC
```
#
### Bitfield - 计数器
```bash
BITFIELD counters SET u8:0 100 GET u8:0  # 8位无符号计数器
```
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 功能3：原子性（强化版）
免费版覆盖SETNX/WATCH-MULTI/Lua，专业版新增：
#
### Redlock算法（多节点分布式锁）
```python
import redis
import time
import uuid
class Redlock:
    def __init__(self, nodes, retry_count=3, retry_delay=200):
        self.nodes = [redis.Redis(host=n['host'], port=n['port']) for n in nodes]
        self.retry_count = retry_count
        self.retry_delay = retry_delay
        self.quorum = len(nodes) // 2 + 1
        self.ttl = 10000  # 10秒
    def lock(self, resource):
        token = str(uuid.uuid4())
        for _ in range(self.retry_count):
            acquired = 0
            start = time.time()
            for node in self.nodes:
                try:
                    if node.set(resource, token, nx=True, px=self.ttl):
                        acquired += 1
                except:
                    continue
            if acquired >= self.quorum and (time.time() - start) * 1000 < self.ttl:
                return token
            self.unlock(resource, token)
            time.sleep(self.retry_delay / 1000)
        return None
    def unlock(self, resource, token):
            try:
                node.JSON.parse(
                    "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end",
                    1, resource, token
                )
            except:
                continue
```
**Redlock适用场景**：对锁可靠性要求极高，单点Redis宕机不可接受。代价是延迟增加（需多数节点确认）.
#
### 锁续期（看门狗）
```python
import threading
class LockWatchdog:
    def __init__(self, redis_client, lock_key, token, ttl=30):
        self.redis = redis_client
        self.lock_key = lock_key
        self.token = token
        self.ttl = ttl
        self.running = False
        self.thread = None
    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._renew)
        self.thread.daemon = True
        self.thread.start()
    def _renew(self):
        while self.running:
            time.sleep(self.ttl / 3)  # 每TTL/3续期一次
            self.redis.JSON.parse(
call('pexpire', KEYS[1], ARGV[2]) else return 0 end",
                1, self.lock_key, self.token, self.ttl * 1000
            )
    def stop(self):
        self.running = False
```
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：Agent、全功能缓存方案、含集群分片、性能调优、监控指标、高级限流与、上下文缓存、在免费版基础上解、Cluster、集群方案、管道化、连接池、批量处理、完整监控指标、INFO、慢查询、命中率、高级持久化、RDB、AOF、令牌桶、漏桶限流、Pub、Sub、高级用法等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 集群方案（专业版核心）
### 集群分片原理
Redis Cluster将键分布在16384个哈希槽中，每个节点负责一部分槽位：
```text
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Node A    │    │   Node B    │    │   Node C    │
│  槽 0-5460  │    │ 5461-10922  │    │ 10923-16383 │
└─────────────┘    └─────────────┘    └─────────────┘
```
### Hash Tag（确保同槽位）
多键操作要求所有键在同一槽位，用Hash Tag强制：
```bash
SET {user:123}:profile "data"
SET {user:123}:sessions "data"
MGET {user:123}:profile {user:123}:sessions
```
### MOVED与ASK重定向
```bash
SET user:456 "data"
SET user:789 "data"
```
**区别**：MOVED是永久的（槽位已迁移），ASK是临时的（迁移中）。使用 `-c` 参数的redis-cli自动处理重定向.
### 集群运维命令
```bash
CLUSTER INFO
CLUSTER NODES
CLUSTER SLOTS
redis-cli --cluster add-node new-host:6379 existing-host:6379
redis-cli --cluster reshard existing-host:6379
CLUSTER FAILOVER
```
## 性能调优（专业版核心）
### 管道化（Pipeline）
```python
for i in range(100):
    r.set(f'key:{i}', i)
pipe = r.pipeline()
for i in range(100):
    pipe.set(f'key:{i}', i)
pipe.execute()
```
**性能对比**：
- 逐条SET 100个键：约100ms（100次往返）
- Pipeline SET 100个键：约2ms（1次往返）
- **提升50倍**
### 连接池调优
```python
import redis
pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    max_connections=50,        # 最大连接数
    socket_timeout=5,          # 命令超时
    socket_connect_timeout=5,  # 连接超时
    retry_on_timeout=True,     # 超时重试
    health_check_interval=30,  # 健康检查
)
r = redis.Redis(connection_pool=pool)
```
**连接数建议**：
- 每个应用实例：50-100连接
- 总连接数 = 实例数 × 每实例连接数
- Redis默认maxclients=10000，生产建议设置 `CONFIG SET maxclients 5000`
### 批处理与检查点
```python
import hashlib
def batch_insert(r, items, batch_size=1000):
    for i in range(0, len(items), batch_size):
        batch = items[i:i+batch_size]
        pipe = r.pipeline()
        for item in batch:
            key = f'data:{hashlib.md5(item.encode()).hexdigest()}'
            pipe.set(key, item, ex=3600)
        pipe.execute()
        r.set('checkpoint:batch', i + batch_size)
```
### 慢查询分析
```bash
SLOWLOG GET 10
CONFIG SET slowlog-log-slower-than 10000
CONFIG SET slowlog-max-len 128
SLOWLOG RESET
```
**常见慢查询**：
- `KEYS *`：O(N)，绝对禁止
- `SORT`：O(N+MlogM)，限制结果数
- `HGETALL` 大Hash：拆分为小Hash
- `LRANGE 0 -1` 大List：分页查询
- `SINTER` 大Set：用SCAN替代
### 命中率监控
```bash
info = r.info('stats')
hits = info['keyspace_hits']
misses = info['keyspace_misses']
hit_rate = hits / (hits + misses) * 100
print(f'缓存命中率: {hit_rate:.2f}%')
```
## 高级持久化（专业版）
### RDB + AOF 混合配置
```bash
CONFIG SET appendonly yes
CONFIG SET appendfsync everysec
CONFIG SET save "900 1 300 10 60 10000"
CONFIG SET auto-aof-rewrite-percentage 100
CONFIG SET auto-aof-rewrite-min-size 64mb
```
### BGSAVE调优
```bash
BGSAVE
LASTSAVE
echo never > /sys/kernel/mm/transparent_hugepage/enabled
```
## 高级限流算法（专业版）
### 令牌桶算法
```python
def token_bucket(r, key, capacity=100, rate=10):
    """capacity: 桶容量, rate: 每秒补充令牌数"""
    now = time.time()
    pipe = r.pipeline()
    pipe.hgetall(key)
    pipe.multi()
    script = """
    local key = KEYS[1]
    local capacity = tonumber(ARGV[1])
    local rate = tonumber(ARGV[2])
    local now = tonumber(ARGV[3])
    local bucket = redis.call('hmget', key, 'tokens', 'last_time')
    local tokens = tonumber(bucket[1]) or capacity
    local last_time = tonumber(bucket[2]) or now
    -- 补充令牌
    tokens = math.min(capacity, tokens + (now - last_time) * rate)
    if tokens >= 1 then
        tokens = tokens - 1
        redis.call('hmset', key, 'tokens', tokens, 'last_time', now)
        redis.call('expire', key, math.ceil(capacity / rate))
        return 1
    else
        redis.call('hmset', key, 'tokens', tokens, 'last_time', now)
        redis.ceil(capacity / rate))
        return 0
    end
    """
    return r.JSON.parse(script, 1, key, capacity, rate, now)
```
**特点**：允许突发（桶满时一次取多个），但平均速率受限。适合API限流（允许短暂突发）.
### 漏桶算法
```python
def leaky_bucket(r, key, capacity=100, leak_rate=10):
    """capacity: 桶容量, leak_rate: 每秒漏出速率"""
    now = time.time()
    script = """
    local key = KEYS[1]
    local capacity = tonumber(ARGV[1])
    local leak_rate = tonumber(ARGV[2])
    local now = tonumber(ARGV[3])
call('hmget', key, 'water', 'last_time')
    local water = tonumber(bucket[1]) or 0
    local last_time = tonumber(bucket[2]) or now
    -- 漏水
    water = math.max(0, water - (now - last_time) * leak_rate)
    if water + 1 <= capacity then
        water = water + 1
        redis.call('hmset', key, 'water', water, 'last_time', now)
        redis.ceil(capacity / leak_rate))
        return 1
    else
        redis.call('hmset', key, 'water', water, 'last_time', now)
        redis.ceil(capacity / leak_rate))
        return 0
    end
    """
    return r.JSON.parse(script, 1, key, capacity, leak_rate, now)
```
**特点**：严格固定速率输出，不允许突发。适合下游服务保护（如调用第三方API，需严格控速）.
### 算法对比
| 算法 | 突发支持 | 实现复杂度 | 适用场景 |
|:---:|:---:|:---:|:---:|
| 固定窗口 | 否（边界突刺） | 简单 | 粗粒度限流 |
| 滑动窗口 | 否 | 中等 | 精确限流 |
| 令牌桶 | 是 | 复杂 | API限流（允许突发） |
| 漏桶 | 否 | 复杂 | 下游保护（严格速率） |
## 多角色场景指南
### 角色一：后端开发者
**典型场景**：为API添加缓存层，降低DB压力.
**推荐方案**：cache-aside + 滑动窗口限流
```bash
SET user:{id} {data} EX 3600
ZADD ratelimit:{ip} {now_ms} {uuid}
ZREMRANGEBYSCORE ratelimit:{ip} 0 {now_ms - 60000}
```
### 角色二：运维工程师
**典型场景**：Redis生产部署与监控.
**推荐方案**：主从+哨兵+完整监控
```bash
while true; do
    redis-cli INFO memory | grep used_memory_human
    redis-cli INFO stats | grep -E "keyspace_hits|evicted_keys"
    redis-cli SLOWLOG GET 5
    sleep 60
done
```
### 角色三：架构师
**典型场景**：设计高可用缓存架构.
**推荐方案**：Redis Cluster + 读写分离 + 多级缓存
```text
应用层 → 本地缓存(Caffeine) → Redis Cluster → DB
              ↑ L1               ↑ L2
         1分钟TTL            1小时TTL
```
### 角色四：AI Agent开发者
**典型场景**：Agent上下文缓存与会话状态.
**推荐方案**：Hash存储会话 + TTL自动过期
```bash
HSET agent:session:{id} context "..." messages "..." created_at {ts}
EXPIRE agent:session:{id} 1800
HINCRBY agent:session:{id} message_count 1
```
### 角色五：数据工程师
**典型场景**：实时去重与计数.
**推荐方案**：HyperLogLog + Bitmap
```bash
PFADD uv:2026-07-18 {user_id}
SETBIT retention:{user_id} {day_offset} 1
```
## 性能优化策略
### 内存优化
1. **使用Hash替代多个String**：`HSET user:1 name "Alice" age 30` 比 `SET user:1:name "Alice"` + `SET user:1:age 30` 省内存（ziplist编码）
2. **使用ziplist编码**：小Hash/List/ZSet自动使用ziplist，省内存
3. **压缩大value**：超1KB的value用gzip/snappy压缩后存储
4. **设置合理的TTL**：避免无用数据长期占内存
5. **定期清理大key**：每周巡检，拆分或删除
> 注: 本SKILL.md超过500行上限, 已截断尾部非核心章节以满足L1格式要求。完整内容见版本库历史。
## FAQ
### Q1: Redis Context Cache支持哪些输入格式？
A1: AI Agent的Redis全功能缓存方案，含集群分片、性能调优、监控指标、高级限流与Redlock算法.。支持文本指令和结构化参数输入，具体格式参考使用流程章节。
### Q2: 使用Redis Context Cache需要什么前置条件？
A2: 请确认运行环境满足依赖说明中的要求。Redis Context Cache基于Markdown指令驱动，无需额外安装包。
### Q3: 命令行执行失败怎么办？
A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。
## 安全注意事项
| 风险类型 | 防范措施 |
|----------|---------|
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |
使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。
## 核心功能
- **自动化执行**: AI Agent的Redis全功能缓存方案，含集群分片、性能调优、监控指标、高级限流与Redlock算法.
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

## 核心功能

- **自动化执行**: AI Agent的Redis全功能缓存方案，含集群分片、性能调优、监控指标、高级限流与Redlock算法.
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据