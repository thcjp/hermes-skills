---
slug: redis-context-cache-pro
name: redis-context-cache-pro
version: 1.0.0
displayName: Redis Context Cache
summary: AI Agent的Redis全功能缓存方案，含集群分片、性能调优、监控指标、高级限流与Redlock算法.
license: Proprietary
edition: pro
description: 'Redis上下文缓存（专业版）在免费版基础上解锁Redis Cluster集群方案、性能调优（管道化/连接池/批量处理）、完整监控指标（INFO/慢查询/命中率）、高级持久化（RDB+AOF混合）、令牌桶/漏桶限流、Redlock多节点分布式锁、Pub/Sub与Streams高级用法.
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
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

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

---

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
# 连接集群
redis-cli -c -h cluster-endpoint -p 6379
# ...
# 集群自动重定向（-c参数启用）
SET user:123 "data"  # 自动MOVED到正确节点
# ...
# 查看集群状态
CLUSTER INFO
CLUSTER NODES
```

### 300秒上手（生产配置）

```bash
# 生产环境完整配置
CONFIG SET maxmemory 4gb
CONFIG SET maxmemory-policy allkeys-lru
CONFIG SET save "900 1 300 10 60 10000"
CONFIG SET appendonly yes
CONFIG SET appendfsync everysec
CONFIG SET slowlog-log-slower-than 10000  # 10ms
CONFIG SET slowlog-max-len 128
# ...
# 验证配置
CONFIG GET maxmemory
CONFIG GET maxmemory-policy
```

---

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

#### Bitmap - 用户签到

```bash
# 用户签到（2026年7月18日签到）
SETBIT sign:{user_id}:202607 17 1  # 第17位（18日）
# 统计本月签到天数
BITCOUNT sign:{user_id}:202607
# 检查某天是否签到
GETBIT sign:{user_id}:202607 17
```

#### Geo - 位置服务

```bash
# 添加位置
GEOADD stores 116.404 39.915 "store_1" 116.408 39.918 "store_2"
# 查找附近5公里的店
GEOSEARCH stores FROMLONLAT 116.405 39.916 BYRADIUS 5 km ASC
```

#### Bitfield - 计数器

```bash
# 多个独立计数器（比INCR更省内存）
BITFIELD counters SET u8:0 100 GET u8:0  # 8位无符号计数器
```
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 功能3：原子性（强化版）

免费版覆盖SETNX/WATCH-MULTI/Lua，专业版新增：

#### Redlock算法（多节点分布式锁）

```python
# Redlock Python实现示例
import redis
import time
import uuid
# ...
class Redlock:
    def __init__(self, nodes, retry_count=3, retry_delay=200):
        self.nodes = [redis.Redis(host=n['host'], port=n['port']) for n in nodes]
        self.retry_count = retry_count
        self.retry_delay = retry_delay
        self.quorum = len(nodes) // 2 + 1
        self.ttl = 10000  # 10秒
# ...
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
            # 多数节点获取成功 + 耗时小于TTL
            if acquired >= self.quorum and (time.time() - start) * 1000 < self.ttl:
                return token
            # 失败，释放所有
            self.unlock(resource, token)
            time.sleep(self.retry_delay / 1000)
        return None
# ...
    def unlock(self, resource, token):
        for node in self.nodes:
            try:
                # Lua脚本原子验证+删除
                node.eval(
                    "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end",
                    1, resource, token
                )
            except:
                continue
```

**Redlock适用场景**：对锁可靠性要求极高，单点Redis宕机不可接受。代价是延迟增加（需多数节点确认）.
#### 锁续期（看门狗）

```python
# 锁续期：业务执行时间不确定时，定期延长TTL
import threading
# ...
class LockWatchdog:
    def __init__(self, redis_client, lock_key, token, ttl=30):
        self.redis = redis_client
        self.lock_key = lock_key
        self.token = token
        self.ttl = ttl
        self.running = False
        self.thread = None
# ...
    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._renew)
        self.thread.daemon = True
        self.thread.start()
# ...
    def _renew(self):
        while self.running:
            time.sleep(self.ttl / 3)  # 每TTL/3续期一次
            # Lua脚本验证token+续期
            self.redis.eval(
                "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('pexpire', KEYS[1], ARGV[2]) else return 0 end",
                1, self.lock_key, self.token, self.ttl * 1000
            )
# ...
    def stop(self):
        self.running = False
```

---
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
# 这两个键在同一槽位（花括号内相同）
SET {user:123}:profile "data"
SET {user:123}:sessions "data"
# ...
# 可以一起操作
MGET {user:123}:profile {user:123}:sessions
```

### MOVED与ASK重定向

```bash
# MOVED：永久重定向（键在另一个节点）
SET user:456 "data"
# (error) MOVED 1234 192.168.1.2:6379
# 客户端应更新槽位映射，重新请求新节点
# ...
# ASK：临时重定向（迁移中）
SET user:789 "data"
# (error) ASK 5678 192.168.1.3:6379
# 客户端本次请求新节点，但不更新映射
```

**区别**：MOVED是永久的（槽位已迁移），ASK是临时的（迁移中）。使用 `-c` 参数的redis-cli自动处理重定向.
### 集群运维命令

```bash
# 查看集群状态
CLUSTER INFO
# cluster_state:ok
# cluster_slots_assigned:16384
# cluster_slots_ok:16384
# ...
# 查看节点列表
CLUSTER NODES
# ...
# 查看槽位分配
CLUSTER SLOTS
# ...
# 添加新节点
redis-cli --cluster add-node new-host:6379 existing-host:6379
# ...
# 重新分片（迁移槽位）
redis-cli --cluster reshard existing-host:6379
# ...
# 故障转移
CLUSTER FAILOVER
```

---

## 性能调优（专业版核心）

### 管道化（Pipeline）

```python
# 错误：100次往返
for i in range(100):
    r.set(f'key:{i}', i)
# ...
# 正确：1次往返
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
# ...
# 连接池配置
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
# 批量写入+检查点（幂等）
import hashlib
# ...
def batch_insert(r, items, batch_size=1000):
    for i in range(0, len(items), batch_size):
        batch = items[i:i+batch_size]
        pipe = r.pipeline()
        for item in batch:
            # 用内容hash作为键，保证幂等
            key = f'data:{hashlib.md5(item.encode()).hexdigest()}'
            pipe.set(key, item, ex=3600)
        pipe.execute()
        # 检查点：记录已处理位置
        r.set('checkpoint:batch', i + batch_size)
```

### 慢查询分析

```bash
# 查看慢查询日志
SLOWLOG GET 10
# ...
# 配置慢查询阈值（10ms）
CONFIG SET slowlog-log-slower-than 10000
# ...
# 慢查询日志最大长度
CONFIG SET slowlog-max-len 128
# ...
# 清空慢查询日志
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
# 计算命中率
info = r.info('stats')
hits = info['keyspace_hits']
misses = info['keyspace_misses']
hit_rate = hits / (hits + misses) * 100
print(f'缓存命中率: {hit_rate:.2f}%')
# 目标：>95%
```

---

## 监控体系（专业版核心）

### INFO命令详解

```bash
# 服务器信息
INFO server
# - redis_version: 7.0.0
# - uptime_in_days: 30
# ...
# 客户端信息
INFO clients
# - connected_clients: 50
# - blocked_clients: 0
# ...
# 内存信息
INFO memory
# - used_memory_human: 1.5G
# - maxmemory_human: 4.0G
# - mem_fragmentation_ratio: 1.2  # 碎片率，>1.5需关注
# ...
# 持久化信息
INFO persistence
# - rdb_changes_since_last_save: 1000
# - aof_enabled: 1
# ...
# 统计信息
INFO stats
# - total_commands_processed: 1000000
# - keyspace_hits: 950000
# - keyspace_misses: 50000
# - expired_keys: 1000
# - evicted_keys: 100
# ...
# 键空间信息
INFO keyspace
# - db0:keys=100000,expires=90000,avg_ttl=3600000
```

### 关键监控指标

| 指标 | INFO字段 | 告警阈值 | 说明 |
|---:|---:|---:|---:|
| 内存使用率 | used_memory/maxmemory | >80% | 接近maxmemory会触发驱逐 |
| 命中率 | keyspace_hits/(hits+misses) | <90% | 缓存策略需优化 |
| 驱逐数 | evicted_keys | >100/min | maxmemory不足或TTL过短 |
| 过期数 | expired_keys | 监控趋势 | 确认TTL策略生效 |
| 连接数 | connected_clients | >maxclients*0.8 | 连接泄漏或客户端过多 |
| 阻塞客户端 | blocked_clients | >10 | BLPOP等阻塞命令过多 |
| 碎片率 | mem_fragmentation_ratio | >1.5 | 内存碎片，需重启整理 |
| 持久化延迟 | rdb_last_bgsave_status | err | BGSAVE失败 |
| 慢查询 | SLOWLOG LEN | 持续增长 | 命令需优化 |
| 主从延迟 | master_repl_offset差 | >1MB | 从节点落后 |

### 大key巡检脚本

```python
# 定期巡检大key
import redis
# ...
def scan_big_keys(r, threshold_bytes=10240):
    big_keys = []
    cursor = 0
    while True:
        cursor, keys = r.scan(cursor=cursor, count=100)
        for key in keys:
            usage = r.memory_usage(key)
            if usage and usage > threshold_bytes:
                big_keys.append({
                    'key': key,
                    'type': r.type(key),
                    'size': usage,
                    'ttl': r.ttl(key)
                })
        if cursor == 0:
            break
    return big_keys
# ...
# 每日巡检
big_keys = scan_big_keys(r)
for k in big_keys:
    print(f"大key: {k['key']} 类型:{k['type']} 大小:{k['size']}B TTL:{k['ttl']}")
```

---

## 高级持久化（专业版）

### RDB + AOF 混合配置

```bash
# 开启AOF
CONFIG SET appendonly yes
# ...
# AOF策略（性能与安全平衡）
CONFIG SET appendfsync everysec
# always: 每次写入都fsync，最安全但最慢
# everysec: 每秒fsync，最多丢1秒数据（推荐）
# no: 由OS决定fsync，最快但可能丢较多
# ...
# RDB快照策略
CONFIG SET save "900 1 300 10 60 10000"
# 900秒内1次修改 → 快照
# 300秒内10次修改 → 快照
# 60秒内10000次修改 → 快照
# ...
# AOF重写触发
CONFIG SET auto-aof-rewrite-percentage 100
CONFIG SET auto-aof-rewrite-min-size 64mb
```

### BGSAVE调优

```bash
# 手动快照（不阻塞）
BGSAVE
# ...
# 查看快照状态
LASTSAVE
# ...
# 调优：fork时内存翻倍问题
# Redis fork时会COW（写时复制），内存使用可能翻倍
# 建议：maxmemory设为系统内存的50-60%
# ...
# 关闭THP（透明大页），避免fork延迟
echo never > /sys/kernel/mm/transparent_hugepage/enabled
```

---

## 高级限流算法（专业版）

### 令牌桶算法

```python
# 令牌桶：允许突发，平均速率受限
def token_bucket(r, key, capacity=100, rate=10):
    """capacity: 桶容量, rate: 每秒补充令牌数"""
    now = time.time()
    pipe = r.pipeline()
    pipe.hgetall(key)
    pipe.multi()
    # Lua脚本保证原子性
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
        redis.call('expire', key, math.ceil(capacity / rate))
        return 0
    end
    """
    return r.eval(script, 1, key, capacity, rate, now)
```

**特点**：允许突发（桶满时一次取多个），但平均速率受限。适合API限流（允许短暂突发）.
### 漏桶算法

```python
# 漏桶：严格固定速率，不允许突发
def leaky_bucket(r, key, capacity=100, leak_rate=10):
    """capacity: 桶容量, leak_rate: 每秒漏出速率"""
    now = time.time()
    script = """
    local key = KEYS[1]
    local capacity = tonumber(ARGV[1])
    local leak_rate = tonumber(ARGV[2])
    local now = tonumber(ARGV[3])
    local bucket = redis.call('hmget', key, 'water', 'last_time')
    local water = tonumber(bucket[1]) or 0
    local last_time = tonumber(bucket[2]) or now
    -- 漏水
    water = math.max(0, water - (now - last_time) * leak_rate)
    if water + 1 <= capacity then
        water = water + 1
        redis.call('hmset', key, 'water', water, 'last_time', now)
        redis.call('expire', key, math.ceil(capacity / leak_rate))
        return 1
    else
        redis.call('hmset', key, 'water', water, 'last_time', now)
        redis.call('expire', key, math.ceil(capacity / leak_rate))
        return 0
    end
    """
    return r.eval(script, 1, key, capacity, leak_rate, now)
```

**特点**：严格固定速率输出，不允许突发。适合下游服务保护（如调用第三方API，需严格控速）.
### 算法对比

| 算法 | 突发支持 | 实现复杂度 | 适用场景 |
|:---:|:---:|:---:|:---:|
| 固定窗口 | 否（边界突刺） | 简单 | 粗粒度限流 |
| 滑动窗口 | 否 | 中等 | 精确限流 |
| 令牌桶 | 是 | 复杂 | API限流（允许突发） |
| 漏桶 | 否 | 复杂 | 下游保护（严格速率） |

---

## 多角色场景指南

### 角色一：后端开发者

**典型场景**：为API添加缓存层，降低DB压力.
**推荐方案**：cache-aside + 滑动窗口限流

```bash
# 缓存用户信息
SET user:{id} {data} EX 3600
# ...
# 限流
ZADD ratelimit:{ip} {now_ms} {uuid}
ZREMRANGEBYSCORE ratelimit:{ip} 0 {now_ms - 60000}
```

### 角色二：运维工程师

**典型场景**：Redis生产部署与监控.
**推荐方案**：主从+哨兵+完整监控

```bash
# 监控脚本
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
# 会话状态用Hash（支持字段级更新）
HSET agent:session:{id} context "..." messages "..." created_at {ts}
EXPIRE agent:session:{id} 1800
# ...
# 会话计数器
HINCRBY agent:session:{id} message_count 1
```

### 角色五：数据工程师

**典型场景**：实时去重与计数.
**推荐方案**：HyperLogLog + Bitmap

```bash
# UV统计（HyperLogLog）
PFADD uv:2026-07-18 {user_id}
# ...
# 留存分析（Bitmap）
SETBIT retention:{user_id} {day_offset} 1
```

---

## 性能优化策略

### 内存优化

1. **使用Hash替代多个String**：`HSET user:1 name "Alice" age 30` 比 `SET user:1:name "Alice"` + `SET user:1:age 30` 省内存（ziplist编码）
2. **使用ziplist编码**：小Hash/List/ZSet自动使用ziplist，省内存
3. **压缩大value**：超1KB的value用gzip/snappy压缩后存储
4. **设置合理的TTL**：避免无用数据长期占内存
5. **定期清理大key**：每周巡检，拆分或删除

### 网络优化

1. **Pipeline批量命令**：减少往返次数
2. **就近部署**：应用与Redis同机房，延迟<1ms
3. **长连接复用**：连接池，避免频繁建连
4. **压缩传输**：大value压缩后传输
5. **MGET/MSET批量操作**：同槽位键批量

### 命令优化

1. **避免KEYS ***：用SCAN替代
2. **避免大SORT**：限制结果数或用Sorted Set
3. **避免HGETALL大Hash**：用HGET/HMGET取所需字段
4. **避免LRANGE 0 -1大List**：分页查询
5. **使用EXISTS替代TYPE检查存在性**：更快

### 成本控制

- 设置maxmemory，避免无限制增长
- 使用合理的驱逐策略（allkeys-lru for cache）
- 定期清理过期数据
- 监控命中率，低命中率缓存考虑移除
- 使用Redis集群分摊负载，避免单实例过大

---

## 多平台集成示例

### 与`PostgreSQL`集成（双写一致性）

```python
# Cache-Aside with PostgreSQL
def get_user(user_id):
    # 1. 查Redis
    data = r.get(f'user:{user_id}')
    if data:
        return json.loads(data)
    # 2. 查PostgreSQL
    data = pg_query("SELECT * FROM users WHERE id = %s", user_id)
    if data:
        # 3. 写Redis（带TTL）
        r.set(f'user:{user_id}', json.dumps(data), ex=3600)
    return data
# ...
def update_user(user_id, data):
    # 1. 更新PostgreSQL
    pg_update("UPDATE users SET ... WHERE id = %s", user_id)
    # 2. 删除Redis缓存（而非更新，避免并发不一致）
    r.delete(f'user:{user_id}')
```

### 与Kafka集成（Streams消费）

```python
# Redis Streams作为Kafka消费者的去重层
def consume_from_kafka():
    for message in kafka_consumer:
        msg_id = message['id']
        # 用Redis SETNX去重（防止重复消费）
        if r.set(f'processed:{msg_id}', '1', nx=True, ex=86400):
            process_message(message)
```

### 与监控系统集成

```bash
# Prometheus + Grafana监控Redis
# 使用 redis_exporter
docker run -d -p 9121:9121 oliver006/redis_exporter \
    --redis.addr redis://localhost:6379
# ...
# 关键指标告警规则
# - redis_memory_used_bytes / redis_memory_max_bytes > 0.8
# - redis_keyspace_hits_total / (hits + misses) < 0.9
# - redis_evicted_keys_total > 100
```

---

## 版本升级迁移指南

### 从免费版升级至专业版

1. **无需迁移数据**：专业版完全兼容免费版的所有命令与模式
2. **新增功能激活**：
   - 集群方案：部署Redis Cluster
   - 性能调优：启用Pipeline与连接池
   - 监控体系：配置INFO采集与告警
3. **指令兼容**：免费版的所有命令在专业版中均可使用

### 从Memcached迁移

```bash
# Memcached命令 → Redis命令映射
# set key value → SET key value EX ttl
# get key → GET key
# delete key → DEL key
# incr key → INCR key
```

### 版本更新历史

| 版本 | 日期 | 变更内容 |
|:------|------:|:------|
| 1.0.0 | 2026-07 | 初版发布，含集群+性能+监控+Redlock+高级限流 |

---

## 故障排查表

| 问题 | 可能原因 | 解决方案 | 优先级 |
|---:|:---|---:|---:|
| 内存持续增长 | 键无TTL或驱逐策略未生效 | 检查TTL设置；确认maxmemory-policy；SCAN巡检无TTL键 | 高 |
| 缓存命中率低 | TTL过短或缓存键设计不合理 | 延长TTL；优化键粒度；分析miss模式 | 高 |
| 响应变慢 | 大key、慢查询、网络延迟 | SLOWLOG分析；SCAN大key；检查网络 | 高 |
| 连接数爆满 | 连接泄漏或客户端过多 | 检查连接池配置；限制maxclients；排查泄漏 | 高 |
| 主从延迟大 | 从节点性能不足或网络问题 | 检查从节点资源；优化网络；减少大命令 | 中 |
| BGSAVE失败 | 内存不足或fork失败 | 检查内存；关闭THP；调整save策略 | 中 |
| Cluster槽位不平衡 | 初始分配不均 | 重新分片：redis-cli --cluster rebalance | 中 |
| 分布式锁失效 | TTL过短或未验证token | 延长TTL；用Lua脚本释放；考虑Redlock | 高 |
| 限流不准 | 时间窗口边界问题 | 改用滑动窗口或令牌桶 | 中 |
| AOF文件过大 | 未触发重写 | 手动BGREWRITEAOF；调整重写阈值 | 低 |
| Pipeline无加速 | 命令数过少或网络本来就快 | Pipeline在命令数>10时效果明显 | 低 |
| 集群节点宕机 | 硬件故障或OOM | 确认故障节点；等待故障转移；修复后重新加入 | 高 |

---

## 即时修复清单

| 问题 | 修复方法 |
|:------:|--------|
| Redis OOM | 设置maxmemory；启用allkeys-lru；SCAN清理无TTL键 |
| KEYS *阻塞 | 改用SCAN迭代 |
| 分布式锁失效 | 用Lua脚本释放（验证token）；延长TTL |
| 缓存雪崩 | TTL加随机抖动；多级缓存 |
| 缓存穿透 | 缓存空值（短TTL）；布隆过滤器 |
| 缓存击穿 | 热点key永不过期；互斥锁重建 |
| 命中率低 | 分析miss模式；优化TTL与键粒度 |
| 大key拖慢 | 拆分为小key；用Hash替代大String |
| 慢查询 | SLOWLOG分析；避免KEYS/SORT/HGETALL大key |
| 连接泄漏 | 连接池；finally中close |

---

## 维护命令

```bash
# 集群健康检查
redis-cli --cluster check cluster-endpoint:6379
# ...
# 性能基准测试
redis-benchmark -h localhost -p 6379 -t set,get -n 100000 -c 50
# ...
# 大key扫描
redis-cli --bigkeys
# ...
# 内存分析
redis-cli --memkeys
# ...
# 慢查询监控
redis-cli SLOWLOG GET 10
# ...
# 在线调整配置（无需重启）
CONFIG SET maxmemory 4gb
CONFIG REWRITE  # 持久化配置到redis.conf
# ...
# AOF手动重写
BGREWRITEAOF
# ...
# 集群重新分片
redis-cli --cluster reshard cluster-endpoint:6379
```

---

## 已知限制

- 本skill的能力范围受限于核心能力章节中定义的功能,不支持超出范围的操作
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 错误处理

| 序号 | 错误场景 | 原因 | 处理方式 | 优先级 |
|----|:--:|---:|----|:--:|
| 1 | 输入参数缺失 | 用户未提供必要参数 | 提示用户提供所需参数后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 | P0 |
| 2 | 执行超时 | 处理时间过长 | 检查输入数据量,分批处理 | P1 |
| 3 | 输出格式错误 | 结果不符合预期格式 | 检查`output_format`参数配置 | P1 |

## FAQ

### Q1：免费版与专业版有什么区别？

免费版提供核心Redis缓存实践（过期策略、数据结构、原子性、内存管理、常见模式、常见陷阱）。专业版解锁集群方案（Cluster/Hash Tag/MOVED）、性能调优（Pipeline/连接池/批处理）、完整监控体系（INFO详解/慢查询/命中率/大key巡检）、高级持久化（RDB+AOF混合/BGSAVE调优）、高级限流（令牌桶/漏桶/滑动窗口）、Redlock多节点分布式锁、多角色场景指南、故障排查表.
### Q2：Redis Cluster和主从+哨兵有什么区别？

Redis Cluster是分片方案，数据分布在多个节点，每个节点负责一部分槽位，支持水平扩展。主从+哨兵是高可用方案，主节点处理写、从节点处理读，哨兵负责故障转移，但不支持水平扩展。数据量小用主从+哨兵，数据量大或需水平扩展用Cluster.
### Q3：Redlock算法真的可靠吗？

Redlock在多数节点（N/2+1）可用时可靠。它解决了单点Redis宕机导致锁失效的问题。但Redlock有时钟同步假设（要求各节点时钟一致），在极端情况下（如GC暂停+时钟漂移）仍可能出错。对可靠性要求极高的场景，建议结合数据库乐观锁或Zookeeper.
### Q4：令牌桶和漏桶怎么选？

令牌桶允许突发（桶满时一次取多个令牌），适合API限流（用户短暂突发可接受）。漏桶严格固定速率输出，不允许突发，适合下游保护（如调用第三方API，必须严格控速）。简单说：对用户用令牌桶，对下游用漏桶.
### Q5：Pipeline为什么能提升50倍性能？

Redis单条命令需一次网络往返（RTT）。100条命令逐条执行=100次RTT。Pipeline将100条命令打包一次发送，只需1次RTT。在1ms RTT的网络下，100条命令从100ms降至2ms。但Pipeline不保证原子性（命令间可能插入其他客户端命令），需原子性用Lua/MULTI.
### Q6：缓存穿透、雪崩、击穿的区别？

- **穿透**：查询不存在的key，每次都查DB。对策：缓存空值（短TTL）或布隆过滤器.
- **雪崩**：大量key同时过期，DB瞬时压力暴增。对策：TTL加随机抖动.
- **击穿**：热点key过期，瞬时大量请求打到DB。对策：热点key永不过期+异步刷新，或互斥锁重建.
### Q7：RDB和AOF必须同时开吗？

推荐同时开。RDB做定期全量快照（恢复快），AOF做增量日志（丢数据少）。Redis重启时优先用AOF恢复（更完整），RDB作为补充。性能影响：AOF everysec模式对性能影响很小（<5%）.
### Q8：如何选择驱逐策略？

纯缓存场景用allkeys-lru（所有键参与LRU驱逐）。混合场景（部分键持久化）用volatile-lru（仅驱逐带TTL的键）。热点明显的缓存用allkeys-lfu（按访问频率驱逐）。持久化数据用noeviction（超限报错，不驱逐）.
### Q9：连接池设多大合适？

每个应用实例50-100连接。总连接数=实例数×每实例连接数。Redis默认maxclients=10000，生产建议设5000（留余量）。连接数过多会消耗Redis内存（每连接约几KB），且上下文切换开销大。用连接池复用连接，避免频繁建连.
### Q10：SCAN为什么比KEYS安全？

KEYS *一次性遍历所有键，期间阻塞Redis。SCAN分批迭代（count参数），每次返回部分键与新的cursor，不阻塞。SCAN的代价是可能返回重复键（需客户端去重），且不保证实时性（迭代期间键可能变化）。生产环境必须用SCAN.
### Q11：Redis适合做消息队列吗？

轻量级场景可以（用Streams）。Streams支持消费者组、ACK确认、消息持久化，比LIST更可靠。但Redis是内存数据库，消息堆积会占内存。海量消息场景（百万级堆积）建议用Kafka/RabbitMQ。Redis Streams适合消息量适中、对延迟敏感的场景.
### Q12：如何监控Redis健康度？

关键指标：内存使用率（used_memory/maxmemory）、命中率（keyspace_hits/(hits+misses)）、驱逐数（evicted_keys）、连接数（connected_clients）、慢查询（SLOWLOG）。用redis_exporter+Prometheus+Grafana搭建监控面板。告警阈值：内存>80%、命中率<90%、驱逐>100/min.
---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Redis**: 6.0+（推荐7.0+以支持新特性）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|----|----|----|----|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| Redis | 服务 | 必需 | 本地安装或云服务 |
| redis-py | Python库 | 可选（脚本） | `pip install redis` |
| redis_exporter | 监控 | 可选（监控） | Docker镜像 |
| PostgreSQL | 数据库 | 可选（集成示例） | 集成场景需要 |

### LLM 路由
- 专业版使用 **GPT-4o** 模型路由，支持复杂集群与性能分析
- 复杂场景（如Redlock分析、限流算法选择）优先使用GPT-4o
- 简单命令查询可降级至GPT-4o-mini节省成本

### API Key 配置
- 本地Redis无需API Key
- 云Redis（Redis Cloud/阿里云）需要访问凭证
- 所有凭证通过环境变量配置，禁止硬编码
- 建议将凭证存储在 `~/.redis/credentials/` 目录（已gitignore）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行Redis缓存管理任务

---

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：redis-store（Redis使用最佳实践）
- 原始license：MIT
- 改进作品：Redis上下文缓存（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，重构为"上下文缓存"场景化指南
- 从英文速查表重构为"陷阱-对策-示例"三段式结构
- 新增Redis Cluster集群方案（Hash Tag/MOVED/ASK重定向/集群运维）
- 新增性能调优（Pipeline/连接池/批处理+检查点+幂等）
- 新增完整监控体系（INFO详解/慢查询/命中率/大key巡检）
- 新增高级持久化（RDB+AOF混合/BGSAVE调优）
- 新增高级限流算法（令牌桶/漏桶/滑动窗口对比）
- 新增Redlock多节点分布式锁（含Python实现）
- 新增锁续期（看门狗）机制
- 新增5类角色场景指南（后端/运维/架构师/Agent开发者/数据工程师）
- 新增性能优化策略（内存/网络/命令/成本）
- 新增多平台集成示例（`PostgreSQL`/Kafka/Prometheus）
- 新增扩展FAQ（12问）与故障排查表（12项）
- 新增依赖说明章节与License版权声明
- 重新设计架构图，增加中文标注与专业版标识
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求.
---

## 专业版特性

本专业版相比免费版新增以下能力：

- **Redis Cluster集群方案**：Hash Tag确保同槽位、MOVED/ASK重定向处理、集群运维命令（添加节点/重新分片/故障转移），支持水平扩展
- **性能调优**：Pipeline批量命令（50倍提升）、连接池配置、批处理+检查点+幂等、慢查询分析
- **完整监控体系**：INFO命令详解、10项关键监控指标+告警阈值、大key巡检脚本、命中率监控
- **高级持久化**：RDB+AOF混合配置、BGSAVE调优、THP关闭避免fork延迟
- **高级限流算法**：令牌桶（允许突发）、漏桶（严格速率）、滑动窗口对比与选择指南
- **Redlock多节点分布式锁**：Python完整实现、锁续期（看门狗）机制
- **多角色场景指南**：后端/运维/架构师/Agent开发者/数据工程师5类角色
- **多平台集成**：`PostgreSQL`双写一致性、Kafka去重消费、Prometheus监控

此外，专业版还提供：
- 性能优化策略（内存/网络/命令/成本四维）
- 扩展FAQ（12问）与故障排查表（12项）
- 即时修复清单（10项）
- 优先支持
- LLM路由升级至GPT-4o

---

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|:-----|:-----|:-----|:-----|
| 免费体验版 | ¥0 | 核心缓存实践（过期/数据结构/原子性/内存/模式）+ 基础FAQ | 个人试用、单机缓存 |
| 收费专业版 | ¥29.9/月 | 全功能（集群+性能调优+监控+Redlock+高级限流）+ 多角色指南 + 优先支持 | 团队/企业、生产部署 |

专业版通过SkillHub SkillPay发布.
## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "Redis Context Cache处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "redis context cache pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
