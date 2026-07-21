---
slug: sql-query
name: sql-query
version: "1.0.0"
displayName: SQL查询工具(专业版)
summary: 面向团队与企业的SQL查询专业版，含慢查询采集、结果缓存、跨库SQL转换、性能基准测试与优先工单支持。
license: Proprietary
edition: pro
description: |-
  面向团队、企业与专业运维的SQL查询执行工具专业版。在免费版基础上新增查询结果缓存与命中率监控、慢查询自动采集与告警、跨数据库SQL自动转换、查询性能基准测试套件、连接池调优与读写分离路由等高级能力，配套面向运维、数据工程师、DBA的多角色场景指南。Use when 需要数据库操作、SQL查询、数据存储管理时使用。不适用于数据库架构设计决策。
tags:
- 集成工具
- 数据库
- SQL查询
- 高级特性
tools:
  - - read
- exec
---
# SQL查询工具(专业版)

## 核心能力

| 能力分类 | 免费版 | 专业版 |
|---------|--------|--------|
| 查询结果缓存 | 无 | 内存+磁盘多级缓存 |
| 慢查询采集 | 手动EXPLAIN | 自动采集+告警+调用链 |
| 跨库SQL转换 | 手动速查表 | 自动语法转换引擎 |
| 性能基准测试 | 无 | 压测套件+回归对比 |
| 连接池调优 | 基础连接 | 复用+健康检查+熔断 |
| 读写分离 | 无 | 自动路由只读副本 |
| 优先支持 | 社区 | 工单优先响应 |

## 适用场景

### 场景一：慢查询治理（运维视角）

自动采集执行时间超过阈值的查询，关联调用链定位来源应用，生成慢查询Top10周报并触发告警。

```python
from sql_query_tool import ProFeatures

pro = ProFeatures(db)
pro.slow_query_monitor(threshold_ms=200, alert_webhook_env="OPS_WEBHOOK")
# 自动采集 >200ms 的查询，推送到运维告警群
```

### 场景二：高频查询缓存（数据工程师视角）

对幂等的聚合查询启用结果缓存，命中即返回，未命中再执行真实查询，命中率可达80%以上，显著降低数据库负载。

```python
pro.enable_cache(
    backend="memory+disk",
    ttl_seconds=300,            # 缓存5分钟
    max_entries=10000,
    key_strategy="query+params" # 按SQL+参数生成缓存键
)
print(pro.cache.metrics())
# 示例
```

### 场景三：跨数据库SQL迁移（DBA视角）

将一份 `PostgreSQL` 业务SQL自动转换为MySQL与SQL Server语法，覆盖LIMIT、UPSERT、日期函数、JSON操作等差异点。

```python
pg_sql = """
SELECT id, metadata->>'source' AS source, created_at
FROM orders
WHERE created_at >= NOW() - INTERVAL '7 days'
ORDER BY created_at DESC
LIMIT 100
"""

mysql_sql = pro.translate_sql(pg_sql, from_dialect="postgresql", to_dialect="mysql")
# 自动转换为：DATE_SUB(NOW(), INTERVAL 7 DAY)、JSON_UNQUOTE(JSON_EXTRACT(...))
```

### 场景四：性能回归测试（架构师视角）

在表结构变更或索引调整后，运行基准测试套件对比前后性能，防止优化一处导致另一处退化。

```python
result = pro.benchmark.run_suite("queries/baseline/")
# 输出：12项查询，10项提升、1项持平、1项退化(需关注)
pro.benchmark.compare(baseline="v1.2", current="v1.3")
```

### 场景五：读写分离路由（DBA视角）

对只读查询自动路由到只读副本，写操作走主库，提升整体吞吐。

```python
pro.enable_read_write_split(
    master="postgresql://master-host:5432/mydb",
    replicas=["postgresql://replica-1:5432/mydb", "postgresql://replica-2:5432/mydb"],
    read_ratio=0.8  # 80%读请求分流到副本
)
```

## 使用流程

### 优秀步：启用专业版功能

```python
from sql_query_tool import ProFeatures

pro = ProFeatures(db)
pro.enable_cache(backend="memory", ttl_seconds=300)
pro.slow_query_monitor(threshold_ms=200)
```

### 第二步：注册性能基线

```python
pro.benchmark.capture_baseline(name="v1.0", query_dir="queries/")
# 将当前查询性能快照保存为基线
```

### 第三步：跨库SQL转换

```python
translated = pro.translate_sql(source_sql, from_dialect="postgresql", to_dialect="mysql")
```

完整上手时间约120秒。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| sqlite3 | CLI工具 | 必需 | 系统自带或官网下载 |
| psql | CLI工具 | 可选 | `PostgreSQL` 安装包 |
| mysql | CLI工具 | 可选 | MySQL 客户端安装包 |
| sqlcmd | CLI工具 | 可选 | SQL Server 工具包 |
| Python | 运行时 | 必需 | python.org 官方下载 |
| redis | Python包 | 可选 | `pip install redis`（分布式缓存） |
| psycopg2 | Python包 | 可选 | `pip install psycopg2`（`PostgreSQL`驱动） |

### API Key 配置
- **数据库连接凭证**: 通过环境变量或配置文件注入，禁止硬编码
- **OPS_WEBHOOK**: 慢查询告警Webhook地址，通过环境变量配置
- **分布式缓存凭证**: 若启用Redis缓存，配置REDIS_URL环境变量

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1：缓存命中率一直低于50%怎么办？

A：(1) 检查缓存键是否包含过多变化参数，导致键爆炸；(2) 评估查询是否真的幂等，非幂等查询不应缓存；(3) 调大TTL或预热高频查询。

### Q2：慢查询告警频繁但都是同一条SQL？

A：这是典型的高频慢查询。先通过`pro.slow_query_report`查看调用链定位来源应用，再针对性优化：补建索引、改写SQL、或对结果启用缓存。

### Q3：跨库转换后JSON查询报错？

A：不同数据库JSON函数差异较大。`PostgreSQL`用`->>`、`@>`，MySQL用`JSON_EXTRACT`、`JSON_CONTAINS`，SQL Server用`JSON_VALUE`。专业版转换引擎覆盖常见场景，复杂嵌套JSON建议人工适配。

### Q4：基准测试结果波动很大如何稳定？

A：(1) 测试前执行`ANALYZE`更新统计信息；(2) 预热数据到缓存；(3) 关闭其他并发进程；(4) 每个查询跑3次取中位数；(5) 排除首次冷启动结果。

### Q5：连接池监控告警频繁触发？

A：命中率低于90%通常是连接数不足，建议提高`max_connections`；等待数持续大于0说明并发过高，考虑读写分离或引入缓存层。

### Q6：读写分离后出现"写后读不到"？

A：只读副本存在复制延迟。对"写后立即读"场景使用`pro.route_to_master()`强制走主库，或配置`read_your_writes=True`让框架自动判断。

### Q7：性能基准测试套件如何组织？

A：按业务模块拆分查询文件，每个文件包含3-5个代表性查询。建议：热查询（高频）、冷查询（低频）、复杂查询（多表JOIN）、边界查询（空表/大表）。

### Q8：跨库转换支持存储过程吗？

A：不支持。存储过程与数据库方言深度绑定，无法自动转换。专业版仅覆盖标准SQL语法差异，存储过程需人工重写。

### Q9：缓存与事务一致性如何保证？

A：专业版支持表事件驱动的缓存失效。当某表发生INSERT/UPDATE/DELETE时，自动失效依赖该表的所有缓存条目，可通过`pro.cache.register_dependency`注册依赖关系。

### Q10：专业版支持哪些数据库？

A：`PostgreSQL` 9.6+、MySQL 5.7+、SQL Server 2016+、SQLite 3.35+。对更低版本仅保证基础查询能力，高级特性可能不可用。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
