# 详细参考 - task-queue-manager-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────────┐
│                任务队列管理器 (专业版) PRO                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ 任务入队  │  │ 任务处理  │  │ 状态追踪  │  │ 锁机制    │            │
│  │ Enqueue  │  │ Process  │  │ Track    │  │ Lock     │            │
│  │          │  │          │  │          │  │          │            │
│  │ 批量入队 │  │ 逐条处理 │  │ 进度文件 │  │ 防并发   │            │
│  │ 幂等去重 │  │ 断点恢复 │  │ 实时统计 │  │ 过期清理 │            │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ 分布式    │  │ 优先级    │  │ 定时触发  │  │ 数据库    │            │
│  │ Distrib  │  │ Priority │  │ Cron     │  │ Database │            │
│  │          │  │          │  │          │  │          │            │
│  │ 多Worker │  │ 动态调度 │  │ cron定时 │  │ PG/MySQL │            │
│  │ 负载均衡 │  │ 优先队列 │  │ 一次性   │  │ 持久化   │            │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                         │
│  │ 监控仪表盘│  │ 告警通知  │  │ 依赖编排  │                         │
│  │ Dashboard│  │ Alert    │  │ DAG      │                         │
│  │          │  │          │  │          │                         │
│  │ 实时状态 │  │ 邮件/企微 │  │ 任务依赖 │            │            │
│  │ 历史统计 │  │ 飞书/钉钉│  │ DAG有向图│            │            │
│  └──────────┘  └──────────┘  └──────────┘                         │
│                                                                     │
│       ✅ 专业版独有（分布式/优先级/定时/数据库/监控/告警/DAG依赖）    │
└─────────────────────────────────────────────────────────────────────┘
```

## 代码示例 (python)

```python
queue = ProQueue(
    slug="daily_etl",
    storage="database",
    database_url="postgresql://...",
    distributed=True,
    worker_count=8,
    dag_support=True,
    monitoring={"dashboard": True, "port": 8080},
    alerts={
        "on_failure": True,
        "on_stuck": {"timeout": 3600},
        "channels": ["email", "wechat_work"]
    }
)

queue.define_dag("daily_etl", [
    {"id": "fetch_api", "task": fetch_api_data},
    {"id": "fetch_db", "task": fetch_db_data},
    {"id": "fetch_files", "task": fetch_file_data},

    {"id": "clean", "task": clean_data, "depends_on": ["fetch_api", "fetch_db", "fetch_files"]},

    {"id": "load", "task": batch_load, "depends_on": ["clean"]},

    {"id": "notify", "task": notify_completion, "depends_on": ["load"]}
])

queue.schedule_cron("daily_etl", "0 2 * * *")

queue.start_workers()
```

## 代码示例 (python)

```python
queue = ProQueue(
    slug="enterprise-batch",
    storage="database",
    database_url="postgresql://...",
    distributed=True,
    worker_count=8,
    priority_schedule=True,
    dag_support=True,
    cron_trigger=True,
    monitoring={"dashboard": True}
)

queue.define_dag("finance_batch", [
    {"id": "extract", "task": extract_finance},
    {"id": "calculate", "task": calculate, "depends_on": ["extract"]},
    {"id": "report", "task": generate_report, "depends_on": ["calculate"]},
    {"id": "distribute", "task": distribute_report, "depends_on": ["report"]}
])

queue.define_dag("log_batch", [
    {"id": "collect", "task": collect_logs},
    {"id": "parse", "task": parse_logs, "depends_on": ["collect"]},
    {"id": "archive", "task": archive_logs, "depends_on": ["parse"]}
])

queue.schedule_cron("finance_batch", "0 6 * * *")    # 每天6点
queue.schedule_cron("log_batch", "0 0 * * *")         # 每天0点
queue.set_dag_priority("finance_batch", 10)
queue.set_dag_priority("log_batch", 3)
```

## 代码示例 (python)

```python
queue = ProQueue(
    slug="web-crawler",
    storage="database",
    database_url="postgresql://...",
    distributed=True,
    worker_count=16,              # 16个Worker（可跨4台机器）
    priority_schedule=True,
    alerts={
        "on_failure": True,
        "on_backlog": {"threshold": 50000},
        "channels": ["email", "feishu"]
    }
)

for url in url_list:
    queue.enqueue(
        task_id=url,              # URL作为幂等键，自动去重
        payload={"url": url},
        priority=5
    )

for urgent_url in urgent_urls:
    queue.enqueue(task_id=urgent_url, payload={"url": urgent_url}, priority=10)

queue.start_workers()
```

## 代码示例 (python)

```python
queue = ProQueue(
    slug="cross-system-sync",
    storage="database",
    database_url="postgresql://...",
    dag_support=True,
    cron_trigger=True,
    alerts={"on_failure": True, "channels": ["email", "feishu"]}
)

queue.define_dag("hourly_sync", [
    {"id": "fetch_crm", "task": fetch_crm_changes},
    {"id": "fetch_erp", "task": fetch_erp_changes},
    {"id": "fetch_bi", "task": fetch_bi_changes},

    {"id": "align", "task": align_data, "depends_on": ["fetch_crm", "fetch_erp", "fetch_bi"]},

    {"id": "sync_crm", "task": sync_to_crm, "depends_on": ["align"]},
    {"id": "sync_erp", "task": sync_to_erp, "depends_on": ["align"]},
    {"id": "sync_bi", "task": sync_to_bi, "depends_on": ["align"]},

    {"id": "verify", "task": verify_consistency, "depends_on": ["sync_crm", "sync_erp", "sync_bi"]}
])

queue.schedule_cron("hourly_sync", "0 * * * *")
```

## 代码示例 (python)

```python
queue = ProQueue(
    slug="monitored-tasks",
    storage="database",
    database_url="postgresql://...",
    distributed=True,
    worker_count=4,
    monitoring={
        "dashboard": True,
        "port": 8080,
        "metrics_interval": 60       # 每60秒采集指标
    },
    alerts={
        "on_failure": True,          # 单任务失败告警
        "on_batch_failure": {"threshold": 0.05},  # 失败率>5%告警
        "on_backlog": {"threshold": 500},          # 积压>500告警
        "on_worker_down": True,                    # Worker失联告警
        "on_stuck": {"timeout": 1800},             # 处理>30分钟告警
        "channels": ["email", "wechat_work", "phone"],
        "escalate_after": 300                       # 5分钟未确认升级
    }
)

```

## 代码示例 (python)

```python
queue = ProQueue(
    slug="etl-pipeline",
    storage="database",
    database_url="postgresql://...",
    distributed=True,
    worker_count=8,
    dag_support=True,                # 启用DAG依赖
    cron_trigger=True                # 启用定时触发
)

queue.define_dag("daily_etl", [
    {"id": "extract", "task": extract_data},
    {"id": "transform", "task": transform_data, "depends_on": ["extract"]},
    {"id": "load_warehouse", "task": load_to_warehouse, "depends_on": ["transform"]},
    {"id": "load_mart", "task": load_to_mart, "depends_on": ["transform"]},
    {"id": "notify", "task": notify_done, "depends_on": ["load_warehouse", "load_mart"]}
])

queue.schedule_cron("daily_etl", "0 2 * * *", tz="Asia/Shanghai")

queue.start()
```

## 代码示例 (python)

```python
queue = ProQueue(
    slug="distributed-tasks",
    storage="database",
    database_url="postgresql://...",
    distributed=True,                # 启用分布式
    worker_count=4,                  # 4个Worker并行
    priority_schedule=True,          # 优先级调度
    alerts={
        "on_failure": True,          # 失败告警
        "on_stuck": True,            # 卡住告警
        "channels": ["email", "wechat_work"]
    },
    monitoring={
        "dashboard": True,
        "port": 8080
    }
)

queue.start_workers()
```

## 代码示例 (python)

```python
queue = ProQueue(slug="dag-tasks", dag_support=True)

queue.define_dag("sales_report", [
    {"id": "fetch_crm", "task": fetch_crm_data},
    {"id": "fetch_erp", "task": fetch_erp_data},

    {"id": "clean", "task": clean_data, "depends_on": ["fetch_crm", "fetch_erp"]},

    {"id": "load_warehouse", "task": load_to_warehouse, "depends_on": ["clean"]},
    {"id": "load_mart", "task": load_to_mart, "depends_on": ["clean"]},

    {"id": "notify", "task": notify_done, "depends_on": ["load_warehouse", "load_mart"]}
])

queue.execute_dag("sales_report")
```

## 代码示例 (text)

```text
企业微信集成：
- 任务失败推送企业微信群
- 队列积压@相关负责人
- Worker失联电话告警

飞书集成：
- 告警通过飞书机器人推送
- 支持飞书卡片交互确认
- 告警升级链路可配置

邮件集成：
- 日报/周报自动发送
- 失败任务详情邮件通知
- 支持HTML格式与附件
```

### 场景三：企业级批处理（系统架构师）
**痛点**：企业有多个批处理任务，需按优先级调度，且任务间有依赖关系。

**解决方案**：

```python
queue = ProQueue(
    slug="enterprise-batch",
    storage="database",
    database_url="postgresql://...",
    distributed=True,
    worker_count=8,
    priority_schedule=True,
    dag_support=True,
    cron_trigger=True,
    monitoring={"dashboard": True}
)

queue.define_dag("finance_batch", [
    {"id": "extract", "task": extract_finance},
    {"id": "calculate", "task": calculate, "depends_on": ["extract"]},
    {"id": "report", "task": generate_report, "depends_on": ["calculate"]},
    {"id": "distribute", "task": distribute_report, "depends_on": ["report"]}
])

queue.define_dag("log_batch", [
    {"id": "collect", "task": collect_logs},
    {"id": "parse", "task": parse_logs, "depends_on": ["collect"]},
    {"id": "archive", "task": archive_logs, "depends_on": ["parse"]}
])

queue.schedule_cron("finance_batch", "0 6 * * *")    # 每天6点
queue.schedule_cron("log_batch", "0 0 * * *")         # 每天0点
queue.set_dag_priority("finance_batch", 10)
queue.set_dag_priority("log_batch", 3)
```

**效果**：多个批处理任务按优先级自动调度，高优先级任务优先处理，资源利用率提升60%。



## 架构总览
```text
┌─────────────────────────────────────────────────────────────────────┐
│                任务队列管理器 (专业版) PRO                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ 任务入队  │  │ 任务处理  │  │ 状态追踪  │  │ 锁机制    │            │
│  │ Enqueue  │  │ Process  │  │ Track    │  │ Lock     │            │
│  │          │  │          │  │          │  │          │            │
│  │ 批量入队 │  │ 逐条处理 │  │ 进度文件 │  │ 防并发   │            │
│  │ 幂等去重 │  │ 断点恢复 │  │ 实时统计 │  │ 过期清理 │            │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ 分布式    │  │ 优先级    │  │ 定时触发  │  │ 数据库    │            │
│  │ Distrib  │  │ Priority │  │ Cron     │  │ Database │            │
│  │          │  │          │  │          │  │          │            │
│  │ 多Worker │  │ 动态调度 │  │ cron定时 │  │ PG/MySQL │            │
│  │ 负载均衡 │  │ 优先队列 │  │ 一次性   │  │ 持久化   │            │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                         │
│  │ 监控仪表盘│  │ 告警通知  │  │ 依赖编排  │                         │
│  │ Dashboard│  │ Alert    │  │ DAG      │                         │
│  │          │  │          │  │          │                         │
│  │ 实时状态 │  │ 邮件/企微 │  │ 任务依赖 │            │            │
│  │ 历史统计 │  │ 飞书/钉钉│  │ DAG有向图│            │            │
│  └──────────┘  └──────────┘  └──────────┘                         │
│                                                                     │
│       ✅ 专业版独有（分布式/优先级/定时/数据库/监控/告警/DAG依赖）    │
└─────────────────────────────────────────────────────────────────────┘
```



### 完整搭建（<300秒）
配置DAG依赖与定时触发：

```python
queue = ProQueue(
    slug="etl-pipeline",
    storage="database",
    database_url="postgresql://...",
    distributed=True,
    worker_count=8,
    dag_support=True,                # 启用DAG依赖
    cron_trigger=True                # 启用定时触发
)

queue.define_dag("daily_etl", [
    {"id": "extract", "task": extract_data},
    {"id": "transform", "task": transform_data, "depends_on": ["extract"]},
    {"id": "load_warehouse", "task": load_to_warehouse, "depends_on": ["transform"]},
    {"id": "load_mart", "task": load_to_mart, "depends_on": ["transform"]},
    {"id": "notify", "task": notify_done, "depends_on": ["load_warehouse", "load_mart"]}
])

queue.schedule_cron("daily_etl", "0 2 * * *", tz="Asia/Shanghai")

queue.start()
```



