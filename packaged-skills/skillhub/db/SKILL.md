---
slug: "db"
name: "db"
version: 1.0.1
displayName: "数据库设计与运维"
summary: "识别并规避数据库连接、事务、Schema变更、备份恢复、复制、查询、数据完整性与扩展性陷阱"
license: "Proprietary"
description: |-
  数据库设计与运维——帮助设计和操作数据库时避免常见的扩展性、可靠性和数据完整性陷阱.
  核心能力包括：
  - 连接管理陷阱识别（连接池耗尽、Serverless连接泄漏、空闲连接内存占用）
  - 事务陷阱规避（长事务锁膨胀、MVCC快照阻塞、死锁、丢失更新）
  - Schema变更安全策略（带默认值加列、并发索引创建、列重命名与删除顺序）
  - 备份与恢复最佳实践（逻辑备份锁表、PITR WAL保留、备份验证、副本一致性）
  - 复制陷阱预防（复制延迟、副本写入、Schema变更同步、脑裂、故障转移重连）
  - 查询性能模式优化（N+1查询、外键索引、大IN子句、COUNT(*)优化、无界SELECT）
  - 数据完整性保障（唯一约束竞态、CHECK约束、孤儿行、时区存储、金额精度）
  - 扩展性限制规划（1亿行分片、Autovacuum监控、统计信息更新、连接数非线性扩展、IOPS瓶颈）
tags:
  - 研发工具
  - database
  - operations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# 数据库设计与运维

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 数据库设计与运维处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 概述

设计和操作数据库时，常见的扩展性、可靠性和数据完整性陷阱往往在生产环境才暴露。本技能系统梳理8大类陷阱及其规避方案，帮助在架构设计阶段就预防问题.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 连接管理陷阱
| 陷阱 | 表现 | 规避方案 |
|:---:|:---:|:---:|
| 连接池耗尽 | 应用静默挂起，无错误日志 | 设置最大连接数，监控连接池使用率 |
| Serverless连接泄漏 | 每次调用打开新连接 | 使用连接池代理（`RDS Proxy`、`PgBouncer`） |
| 连接阻塞Schema变更 | `ALTER TABLE` 等待所有事务完成 | 维护窗口期执行，或设置 `lock_timeout` |
| 空闲连接占用内存 | 大量空闲连接耗尽数据库内存 | 设置 `idle_in_transaction_session_timeout`，定期清理 |

**输入**: 用户提供连接管理陷阱所需的指令和必要参数.
**输出**: 返回连接管理陷阱的处理结果,包含执行状态码、结果数据和执行日志。### 事务陷阱
| 陷阱(续)| 表现 | 规避方案 |
|:-------|-------:|:-------|
| 长事务锁膨胀 | 事务持锁过久，MVCC版本堆积 | 保持事务简短，避免事务内做HTTP调用 |
| 只读事务阻塞清理 | 只读事务仍取快照，阻塞 `VACUUM` | Postgres 中设置 `statement_timeout`，及时关闭事务 |
| 隐式自动提交差异 | 不同数据库自动提交行为不一致 | 显式使用 `BEGIN`/`COMMIT`，不依赖隐式行为 |
| 死锁 | 多事务以不同顺序锁定相同资源 | 统一加锁顺序，使用 `SELECT FOR UPDATE` 预锁定 |
| 丢失更新 | 读-改-写无锁导致并发覆盖 | 使用 `SELECT FOR UPDATE` 悲观锁或乐观锁（版本号） |

**输入**: 用户提供事务陷阱所需的指令和必要参数.
**输出**: 返回事务陷阱的处理结果,包含执行状态码、结果数据和执行日志。### Schema变更安全策略

| 操作 | 风险 | 安全方案 |
|---:|:---|---:|
| 带默认值加列 | 旧版MySQL/Postgres全表重写 | 先加 `NULL` 默认列，回填数据，再 `ALTER` 设默认值 |
| 创建索引 | 部分数据库锁写操作 | Postgres 用 `CREATE INDEX CONCURRENTLY`，MySQL 8+ 用 `ONLINE` |
| 重命名列 | 运行中应用引用旧列名报错 | 先加新列，迁移代码，再删旧列 |
| 删除列 | 活跃查询引用被删列报错 | 先部署代码变更（不再引用该列），再执行Schema变更 |
| 批量插入外键检查 | 外键约束拖慢批量插入 | 先 `SET CONSTRAINTS DEFERRED`，插入后重新启用 |

### 备份与恢复
| 陷阱 | 风险 | 最佳实践 |
|:------:|--------|:-------|
| 逻辑备份锁表 | `pg_dump`/`mysqldump` 锁表或丢失并发写入 | 使用一致性快照（`--snapshot` 或 `--single-transaction`） |
| PITR不可用 | 未配置WAL/binlog保留 | 在需要之前配置WAL归档（`archive_mode=on`） |
| 备份未验证 | 恢复时才发现备份损坏 | 定期从备份恢复到测试环境验证 |
| 副本备份不一致 | 复制延迟导致备份与主库不一致 | 从副本备份后验证一致性，或从主库一致性快照备份 |

**输入**: 用户提供备份与恢复所需的指令和必要参数.
**处理**: 解析备份与恢复的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回备份与恢复的处理结果,包含执行状态码、结果数据和执行日志。### 复制陷阱
| 陷阱(续)(续)| 表现 | 规避方案 |
|-----|:---:|----:|
| 复制延迟导致脏读 | 从副本读取到过期数据 | 读取前检查复制延迟（`pg_stat_replication`） |
| 副本写入破坏复制 | 写入副本导致复制中断 | 设置副本为只读（`hot_standby=on` + `default_transaction_read_only=on`） |
| Schema变更破坏复制 | 分别在主从执行Schema变更 | 通过复制通道同步Schema变更，不手动在副本执行 |
| 故障转移脑裂 | 两个主库同时接受写入 | 使用 fencing/STONITH 机制防止旧主库继续写入 |
| 提升副本后连接未切换 | 应用仍连旧主库 | 应用层实现重连逻辑，或使用VIP/DNS自动切换 |

**输入**: 用户提供复制陷阱所需的指令和必要参数.
**输出**: 返回复制陷阱的处理结果,包含执行状态码、结果数据和执行日志。### 查询性能模式
| 问题 | 原因 | 优化方案 |
|----|----|----|
| N+1查询 | ORM懒加载关联关系 | 预加载（`eager load`）或批量查询 |
| 外键缺索引 | JOIN和级联删除全表扫描 | 为外键列创建索引 |
| 大IN子句变慢 | `IN (1,2,...,10000)` 性能下降 | 拆分为多个查询或使用临时表JOIN |
| `COUNT(*)` 慢 | 大表全表扫描计数 | 使用近似计数（`pg_class.reltuples`）或缓存结果 |
| 无界SELECT | `SELECT * FROM huge_table` 导致OOM | 必须加 `LIMIT`，或使用游标分批读取 |

**输入**: 用户提供查询性能模式所需的指令和必要参数.
**处理**: 解析查询性能模式的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 数据完整性
| 陷阱 | 后果 | 保障方案 |
|:-----|:-----|:-----|
| 应用层唯一检查竞态 | 并发下产生重复数据 | 使用数据库唯一约束（`UNIQUE`） |
| CHECK约束被禁用 | 数据逐渐腐化 | 保持 `CHECK` 约束启用，不做"灵活性"让步 |
| 外键缺失致孤儿行 | 引用完整性破坏 | 先清理孤儿行，再添加 `FOREIGN KEY` 约束 |
| 时区混乱 | 跨时区显示错误 | 存储 `UTC`，显示时转换（`TIMESTAMPTZ`） |
| 浮点数存金额 | 舍入误差导致账目不平 | 使用 `DECIMAL` 或整数分（`INTEGER` 存分） |

**输入**: 用户提供数据完整性所需的指令和必要参数.
**输出**: 返回数据完整性的处理结果,包含执行状态码、结果数据和执行日志。### 扩展性限制

| 限制 | 阈值 | 规划方案 |
|---:|---:|---:|
| 单表行数过多 | 超过 1 亿（100M）行 | 提前规划分片策略，按时间或哈希分区 |
| Autovacuum滞后 | 死元组比率过高 | 监控 `pg_stat_user_tables` 的死元组比率，调优 `autovacuum` 参数 |
| 统计信息过期 | 批量导入后查询计划变差 | 大批量导入后手动执行 `ANALYZE` |
| 连接数非线性扩展 | 连接越多锁竞争越激烈 | 使用连接池限制最大连接数（`PgBouncer`） |
| 磁盘IOPS瓶颈 | I/O等待先于CPU成为瓶颈 | 监控 `iostat` 的 I/O wait，使用SSD或Provisioned IOPS |
### 连接池耗尽

针对连接池耗尽,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供连接池耗尽相关的配置参数、输入数据和处理选项.
**输出**: 返回连接池耗尽的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`连接池耗尽`的配置文档进行参数调优
#
## 使用流程

1. **场景识别**：判断当前属于连接、事务、Schema、备份、复制、查询、完整性还是扩展性问题
2. **陷阱匹配**：在对应类别中查找匹配的陷阱描述与规避方案
3. **方案选择**：根据数据库类型（PostgreSQL/MySQL）选择具体实现命令
4. **风险评估**：评估方案对现有系统的影响（锁表时间、连接数变化、复制延迟）
5. **逐步执行**：按安全方案顺序执行，每步验证后再进行下一步

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 详细示例

### 示例1：安全添加带默认值的列

```sql
-- 错误做法（旧版Postgres会全表重写，锁表数小时）:
-- ALTER TABLE orders ADD COLUMN status VARCHAR(20) DEFAULT 'pending';
# ...
-- 安全做法（分三步）:
-- 第一步: 添加NULL列（瞬时完成，不锁表）
ALTER TABLE orders ADD COLUMN status VARCHAR(20);
# ...
-- 第2步: 分批回填数据
UPDATE orders SET status = 'pending' WHERE id BETWEEN 1 AND 100000;
UPDATE orders SET status = 'pending' WHERE id BETWEEN 100001 AND 200000;
# ...
-- 第3步: 设置默认值与非空约束
ALTER TABLE orders ALTER COLUMN status SET DEFAULT 'pending';
ALTER TABLE orders ALTER COLUMN status SET NOT NULL;
```

### 示例2：并发创建索引

```sql
-- Postgres: CONCURRENTLY 不阻塞写入（但不能在事务块中使用）
CREATE INDEX CONCURRENTLY idx_orders_customer_id ON orders(customer_id);
# ...
-- MySQL 8+: ONLINE DDL
ALTER TABLE orders ADD INDEX idx_customer_id (customer_id), ALGORITHM=INPLACE, LOCK=NONE;
```

### 示例3：避免N+1查询

```python
# 错误: N+1查询（100个订单 = 101次查询）
orders = Order.objects.all()  # 1次查询
for order in orders:
    print(order.customer.name)  # 每次循环1次查询
# ...
# 正确: 预加载（2次查询）
orders = Order.objects.select_related('customer').all()  # JOIN一次查出
for order in orders:
    print(order.customer.name)  # 无额外查询
```

### 示例4：避免丢失更新

```sql
-- 错误: 读-改-写无锁，并发下丢失更新
SELECT balance FROM accounts WHERE id = 1;  -- 读到 balance=100
-- 另一事务同时读到100，各自扣减20
UPDATE accounts SET balance = 80 WHERE id = 1;  -- 丢失了另一事务的扣减
# ...
-- 正确: 使用 SELECT FOR UPDATE 悲观锁
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;  -- 加行锁
UPDATE accounts SET balance = balance - 20 WHERE id = 1;
COMMIT;
```

### 示例5：金额存储与计算

```sql
-- 错误: 浮点数存金额（舍入误差）
CREATE TABLE bad_orders (total FLOAT);  -- 0.1+0.2 = 0.30000000000000004
# ...
-- 正确: DECIMAL 精确存储
CREATE TABLE good_orders (total DECIMAL(10,2));  -- 0.10+0.20 = 0.30
# ...
-- 或: 整数分存储
CREATE TABLE cent_orders (total_cents INT);  -- 10分+20分=30分
```

### 示例6：大表COUNT(*)优化

```sql
-- 慢: COUNT(*) 全表扫描（1亿行需数十秒）
SELECT COUNT(*) FROM huge_table;
# ...
-- 快: 近似计数（毫秒级，误差约5%）
SELECT reltuples::BIGINT FROM pg_class WHERE relname = 'huge_table';
# ...
-- 或: 缓存计数
SELECT count FROM table_count_cache WHERE table_name = 'huge_table';
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| `lock timeout` Schema变更超时 | `ALTER TABLE` 等待长事务释放锁 | 设置 `lock_timeout='5s'`，超时后避免无限等待 |
| `deadlock detected` 死锁 | 多事务以不同顺序锁定相同资源 | 统一加锁顺序，捕获死锁异常后事务 |
| `too many connections` 连接耗尽 | 连接池配置过小或连接泄漏 | 使用 `PgBouncer` 连接池，设置 `max_connections` 上限 |
| `replication lag` 复制延迟 | 大事务或网络带宽不足 | 监控 `pg_stat_replication.replay_lag`，将大事务拆小 |
| `out of memory` 查询OOM | `SELECT *` 无界查询加载全表 | 添加 `LIMIT`，使用游标分批读取，或增加 `work_mem` |
| `duplicate key value` 唯一约束冲突 | 应用层检查与插入之间存在竞态 | 使用 `INSERT ... ON CONFLICT DO NOTHING` 或数据库唯一约束 |
| `integer out of range` 整数溢出 | `INT` 最大值 2147483647 不足 | 改用 `BIGINT`（最大 9223372036854775807） |
| `column "x" cannot be cast automatically` 类型转换失败 | `ALTER COLUMN TYPE` 不兼容 | 先添加新类型列，迁移数据，再删除旧列 |

## 常见问题

### Q1: 连接池应该设置多大？
A: 公式：`pool_size = (核心数 * 2) + 有效磁盘数`。但连接数不是越多越好——连接越多锁竞争越激烈。建议从 `pool_size = 10` 开始，根据监控调整。Serverless 环境必须使用 `RDS Proxy` 或 `PgBouncer`.
### Q2: 事务应该保持多短？
A: 事务应只包含数据库操作，不包含HTTP调用、文件IO等耗时操作。Postgres 中长事务会持有 MVCC 快照，阻塞 `VACUUM` 清理死元组。建议设置 `idle_in_transaction_session_timeout = 60s`.
### Q3: 单表超过1亿行就必须分片吗？
A: 不一定。如果查询都命中索引，1亿行仍可高效运行。需要分片的信号：(1) 写入QPS超过单库极限；(2) 索引维护成本过高；(3) 维护窗口不足以完成 `VACUUM`。可以先尝试分区表（按时间或哈希），分片是最后手段.
### Q4: 为什么浮点数不能存金额？
A: IEEE 754浮点数无法精确表示十进制小数。`0.1 + 0.2` 在浮点数中等于 `0.30000000000000004`。大量累加后误差会累积，导致账目不平。必须使用 `DECIMAL(10,2)` 或整数分（`INT` 存分）.
### Q5: `CREATE INDEX CONCURRENTLY` 失败了怎么办？
A: `CONCURRENTLY` 失败后会留下 `INVALID` 索引。需要先 `DROP INDEX` 删除无效索引，再重新执行 `CREATE INDEX CONCURRENTLY`。注意：`CONCURRENTLY` 不能在事务块中使用.
### Q6: 如何监控复制延迟？
A: PostgreSQL数据库 中查询 `pg_stat_replication` 视图：`SELECT application_name, replay_lag FROM pg_stat_replication;`。延迟超过30秒应告警。大事务是延迟的主要原因，建议将大事务拆分为小批次.
## 已知限制

- 主要覆盖 PostgreSQL 与 MySQL 场景，其他数据库（如 MongoDB、Redis）的陷阱需另行参考
- 扩展性建议基于单机房架构，跨地域多活场景需额外考虑
- 分片策略需结合具体业务场景设计，本技能提供原则而非具体方案
- 备份恢复验证需要额外测试环境，资源受限时可能无法定期执行

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "数据库设计与运维处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "db"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
