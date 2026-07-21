# 详细参考 - task-bot-orchestrator-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────────┐
│                任务编排机器人 (专业版) PRO                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ 数据处理  │  │ 定时调度  │  │ 通知推送  │  │ 任务编排  │            │
│  │ Data     │  │ Schedule │  │ Notify   │  │ Pipeline │            │
│  │          │  │          │  │          │  │          │            │
│  │ CSV/Excel│  │ 每日提醒 │  │ 邮件通知 │  │ 链式执行 │            │
│  │ 清洗转换 │  │ 周期同步 │  │ 消息推送 │  │ 步骤串联 │            │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ 条件触发  │  │ 高级编排  │  │ 数据库    │  │ 错误恢复  │            │
│  │ Trigger  │  │ Advanced │  │ Database │  │ Recovery │            │
│  │          │  │          │  │          │  │          │            │
│  │ 事件驱动 │  │ 并行/分支 │  │ 读写集成 │  │ 重试/回滚 │            │
│  │ 文件/邮件│  │ 循环/子流程│  │ 多数据库 │  │ 断点续传 │            │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                         │
│  │ 多渠道    │  │ 监控仪表盘│  │ 团队协作  │                         │
│  │ Multi-CH │  │ Dashboard│  │ Team     │                         │
│  │          │  │          │  │          │                         │
│  │ Slack/DC │  │ 实时状态 │  │ 多用户   │                         │
│  │ 短信/电话│  │ 历史统计 │  │ 权限管理 │                         │
│  └──────────┘  └──────────┘  └──────────┘                         │
│                                                                     │
│       ✅ 专业版独有（条件触发/高级编排/数据库/恢复/多渠道/监控/团队）  │
└─────────────────────────────────────────────────────────────────────┘
```

## 代码示例 (python)

```python
orch = Orchestrator(
    database=Database(postgres_url="postgresql://..."),
    error_recovery={"max_retries": 3, "checkpoint": True}
)

workflow = orch.workflow("etl_pipeline")

workflow.parallel([
    workflow.step("采集API数据", fetch_api).retry(3, 60),
    workflow.step("采集数据库", fetch_db).retry(3, 60),
    workflow.step("采集文件", fetch_files).retry(3, 60)
])

workflow.branch(
    condition=lambda ctx: ctx["data_size"] > 1_000_000,
    if_true=workflow.step("大数据清洗", clean_large_batch),
    if_false=workflow.step("标准清洗", clean_standard)
)

workflow.loop(
    items=lambda ctx: ctx["batches"],
    body=workflow.step("加载批次", load_to_postgres).retry(5, 30)
)

workflow.step("发送完成通知", notify_completion)
workflow.step("更新监控指标", update_metrics)

orch.enable_dashboard(port=8080)
```

## 代码示例 (python)

```python
Trigger.on_db_change(table="orders", event="insert").do(process_order)

def process_order():
    workflow = orch.workflow("order_processing")

    workflow.parallel([
        workflow.step("处理支付", process_payment).retry(3, 60),
        workflow.step("锁定库存", lock_inventory).retry(3, 30)
    ])

    workflow.branch(
        condition=lambda ctx: ctx["payment_status"] == "success",
        if_true=workflow.subflow("ship_order"),
        if_false=workflow.step("退款处理", process_refund)
    )

    ship_workflow = orch.workflow("ship_order")
    ship_workflow.step("创建物流单", create_shipment)
    ship_workflow.step("通知仓库", notify_warehouse)
    ship_workflow.step("发送发货通知", notify_customer)

    workflow.step("完成通知", lambda: notify.broadcast(
        message="订单处理完成",
        channels=["email", "sms", "wechat_work"]
    ))
```

## 代码示例 (python)

```python
Trigger.on_api_call("/api/metrics/alert").do(handle_alert)

def handle_alert():
    workflow = orch.workflow("alert_handling")

    workflow.branch(
        condition=lambda ctx: ctx["severity"] == "critical",
        if_true=workflow.subflow("critical_alert"),
        if_false=workflow.step("记录告警", log_alert)
    )

    critical = orch.workflow("critical_alert")
    critical.parallel([
        critical.step("电话通知", lambda: notify.alert(
            message="严重告警", channels=["phone", "sms"]
        )),
        critical.step("创建工单", create_ticket)
    ])
    critical.step("自动恢复", auto_recover).retry(3, 60)
    critical.step("验证恢复", verify_recovery)
    critical.branch(
        condition=lambda ctx: ctx["recovered"],
        if_true=critical.step("关闭告警", close_alert),
        if_false=critical.step("升级处理", escalate)
    )
```

## 代码示例 (python)

```python
orch = Orchestrator(
    team={
        "members": ["alice", "bob", "charlie", "diana"],
        "roles": {
            "alice": "admin",
            "bob": "editor",
            "charlie": "editor",
            "diana": "viewer"
        }
    }
)

workflow = orch.workflow("team_task")
workflow.step("创建任务", create_task)
workflow.step("负责人审批", lambda: orch.approve("alice"))
workflow.branch(
    condition=lambda ctx: ctx["approved"],
    if_true=workflow.step("分配任务", assign_task),
    if_false=workflow.step("退回修改", return_for_revision)
)
workflow.step("执行任务", execute_task)
workflow.step("验收", lambda: orch.approve("diana"))
workflow.step("归档", archive_task)

orch.share_workflow("team_task", team=["alice", "bob", "charlie", "diana"])
```

## 代码示例 (python)

```python
workflow = orch.workflow("ecommerce_order")

workflow.parallel([
    workflow.step("获取订单数据", fetch_orders),
    workflow.step("获取库存数据", fetch_inventory),
    workflow.step("获取用户数据", fetch_users)
])

workflow.branch(
    condition=lambda ctx: ctx["orders_count"] > 1000,
    if_true=workflow.subflow("batch_process"),
    if_false=workflow.subflow("realtime_process")
)

workflow.loop(
    items=lambda ctx: ctx["orders"],
    body=workflow.step("处理订单", process_order).retry(3, 60)
)

workflow.parallel([
    workflow.step("邮件通知", send_email),
    workflow.step("短信通知", send_sms),
    workflow.step("推送通知", send_push)
)
```

## 代码示例 (python)

```python
workflow = orch.workflow("cross_system_sync")

workflow.parallel([
    workflow.step("CRM采集", fetch_from_crm),
    workflow.step("ERP采集", fetch_from_erp),
    workflow.step("财务采集", fetch_from_finance)
])

workflow.step("数据对齐", align_data)
workflow.step("冲突解决", resolve_conflicts)

workflow.branch(
    condition=lambda ctx: ctx["has_changes"],
    if_true=workflow.subflow("sync_changes"),
    if_false=workflow.step("无变更跳过", skip_sync)
)

sync = orch.workflow("sync_changes")
sync.parallel([
    sync.step("同步至CRM", sync_to_crm).retry(3, 60),
    sync.step("同步至ERP", sync_to_erp).retry(3, 60),
    sync.step("同步至财务", sync_to_finance).retry(3, 60)
])
sync.step("记录同步日志", log_sync)
```

## 代码示例 (python)

```python
orch = Orchestrator()

workflow = orch.workflow("data_pipeline")

workflow.parallel([
    workflow.step("采集API数据", fetch_api_data),
    workflow.step("采集数据库数据", fetch_db_data)
])

workflow.branch(
    condition=lambda ctx: ctx["data_count"] > 10000,
    if_true=workflow.step("大数据处理", process_large_batch),
    if_false=workflow.step("小数据处理", process_small_batch)
)

workflow.loop(
    items=lambda ctx: ctx["batches"],
    body=workflow.step("处理批次", process_batch)
)

workflow.step("通知完成", notify_completion)

orch.enable_dashboard(port=8080)
```

## 代码示例 (python)

```python
Trigger.on_event("git_push").do(ci_cd_pipeline)

def ci_cd_pipeline():
    workflow = orch.workflow("ci_cd")

    workflow.parallel([
        workflow.step("单元测试", run_unit_tests),
        workflow.step("代码质量检查", run_lint),
        workflow.step("安全扫描", run_security_scan)
    ])

    workflow.branch(
        condition=lambda ctx: ctx["branch"] == "main",
        if_true=workflow.subflow("deploy_prod"),
        if_false=workflow.step("通知测试", notify_qa)
    )

    deploy_workflow = orch.workflow("deploy_prod")
    deploy_workflow.step("构建镜像", build_image)
    deploy_workflow.step("推送镜像", push_image)
    deploy_workflow.step("部署生产", deploy_k8s)
    deploy_workflow.step("健康检查", health_check).retry(5, 30)
    deploy_workflow.step("通知团队", notify_team)
```

## 代码示例 (python)

```python
orch = Orchestrator(
    error_recovery={
        "max_retries": 3,           # 最多重试3次
        "retry_delay": 60,          # 重试间隔60秒
        "retry_backoff": "exponential",  # 指数退避
        "rollback_on_failure": True,     # 失败回滚
        "checkpoint": True,              # 启用检查点
        "dead_letter_queue": True        # 启用死信队列
    }
)

workflow.step("关键操作", critical_task).retry(
    times=5,
    delay=30,
    backoff="exponential"
)

workflow.step("主流程", primary_process).fallback(
    workflow.step("降级流程", fallback_process)
)
```

## 代码示例 (python)

```python
orch = Orchestrator(
    database=Database(postgres_url="postgresql://..."),
    error_recovery={
        "max_retries": 3,
        "retry_delay": 60,
        "rollback_on_failure": True,
        "checkpoint": True
    },
    monitoring={
        "dashboard": True,
        "port": 8080,
        "alert_on_failure": True
    },
    team={
        "members": ["alice", "bob", "charlie"],
        "roles": {"alice": "admin", "bob": "editor", "charlie": "viewer"}
    }
)
```

## 代码示例 (python)

```python
notify = orch.notifier

notify.broadcast(
    message="订单处理完成",
    channels=["email", "wechat_work", "feishu", "slack"],
    severity="info"
)

notify.alert(
    message="数据库连接失败，请立即处理",
    channels=["phone", "sms"],
    severity="critical",
    escalate_after=300  # 5分钟未确认升级
)
```

## 代码示例 (text)

```text
Slack集成：
- 任务状态变更推送Slack频道
- 失败告警@相关负责人
- 支持Slack内交互式审批

飞书集成：
- 工作流审批通过飞书卡片
- 任务完成推送飞书群
- 支持飞书机器人查询任务状态

企业微信集成：
- 告警推送企业微信群
- 支持群内任务创建
- 审批流程企业微信通知
```

### 二、高级编排（专业版独有）
| 编排模式 | 方法 | 说明 |
|----------|------|------|
| 并行执行 | `workflow.parallel([step1, step2])` | 多个步骤同时执行 |
| 条件分支 | `workflow.branch(cond, if_true, if_false)` | 根据条件选择路径 |
| 循环 | `workflow.loop(items, body)` | 遍历列表执行 |
| 子流程 | `workflow.subflow("sub_workflow_name")` | 调用其他工作流 |
| 延迟 | `workflow.delay(seconds)` | 延迟执行 |
| 等待 | `workflow.wait_for(event)` | 等待事件触发 |
| 重试 | `workflow.retry(times, delay)` | 失败自动重试 |

```python
workflow = orch.workflow("ecommerce_order")

workflow.parallel([
    workflow.step("获取订单数据", fetch_orders),
    workflow.step("获取库存数据", fetch_inventory),
    workflow.step("获取用户数据", fetch_users)
])

workflow.branch(
    condition=lambda ctx: ctx["orders_count"] > 1000,
    if_true=workflow.subflow("batch_process"),
    if_false=workflow.subflow("realtime_process")
)

workflow.loop(
    items=lambda ctx: ctx["orders"],
    body=workflow.step("处理订单", process_order).retry(3, 60)
)

workflow.parallel([
    workflow.step("邮件通知", send_email),
    workflow.step("短信通知", send_sms),
    workflow.step("推送通知", send_push)
)
```



