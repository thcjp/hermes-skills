---
slug: "task-queue-manager"
name: "task-queue-manager"
version: "1.0.0"
displayName: "任务队列管理器(专业版)"
summary: "全功能持久化任务队列，含分布式处理、优先级调度、数据库存储与监控告警，支持6种角色场景。"
license: "Proprietary"
edition: "pro"
description: |-
  任务队列管理器（专业版）是在免费版基础上的全功能升级，为AI Agent提供企业级的持久化任务队列管理能力。在核心队列管理、断点恢复、幂等去重能力之上，解锁分布式处理、优先级调度、定时触发、数据库持久化、监控仪表盘、告警通知、任务依赖编排七大高级功能。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。
tags:
  - 任务队列
  - 分布式处理
  - 优先级调度
  - 数据库持久化
  - 监控告警
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# 任务队列管理器(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### 一、分布式处理（专业版独有）
| 功能 | 方法 | 说明 |
|------|------|------|
| Worker注册 | `queue.register_worker(name)` | 注册Worker节点 |
| 任务分配 | `queue.assign_to_worker()` | 自动分配任务给空闲Worker |
| 负载均衡 | 自动按Worker负载分配 | 避免单点过载 |
| 故障转移 | Worker失联自动重分配 | 确保任务不丢失 |
| Worker状态 | `queue.worker_status()` | 查看所有Worker状态 |

```python
queue = ProQueue(slug="distributed", distributed=True)

queue.start_workers(count=4)

for worker in queue.worker_status():
    print(f"{worker.name}: {worker.status}, 处理中: {worker.active_tasks}")

```

**输入**: 用户提供一、分布式处理（专业版独有）所需的指令和必要参数。
**输出**: 返回一、分布式处理（专业版独有）的处理结果,包含执行状态码、结果数据和执行日志。### 二、优先级调度（专业版独有）
| 优先级 | 数值 | 说明 |
|--------|------|------|
| 紧急 | 10 | 最高优先级，立即处理 |
| 高 | 7 | 优先于普通任务 |
| 普通 | 5 | 默认优先级 |
| 低 | 3 | 空闲时处理 |
| 后台 | 1 | 最低优先级 |

```python
queue = ProQueue(slug="priority-tasks", priority_schedule=True)

queue.enqueue(task_id="urgent_001", payload=critical_data, priority=10)

queue.enqueue(task_id="normal_001", payload=normal_data, priority=5)

queue.enqueue(task_id="background_001", payload=batch_data, priority=1)

task = queue.dequeue()  # 总是取出优先级最高的
```

**输入**: 用户提供二、优先级调度（专业版独有）所需的指令和必要参数。
**输出**: 返回二、优先级调度（专业版独有）的处理结果,包含执行状态码、结果数据和执行日志。### 三、定时触发（专业版独有）
| 触发方式 | 配置 | 说明 |
|----------|------|------|
| cron定时 | `queue.schedule_cron(slug, expr)` | cron表达式定时触发 |
| 一次性 | `queue.schedule_once(slug, datetime)` | 指定时间触发一次 |
| 间隔 | `queue.schedule_interval(slug, seconds)` | 固定间隔触发 |

```python
queue.schedule_cron("daily_etl", "0 2 * * *", tz="Asia/Shanghai")

queue.schedule_cron("hourly_sync", "0 * * * *")

queue.schedule_interval("monitor", 1800)

queue.schedule_once("one_time_task", "2026-01-20 10:00:00")
```

**处理**: 解析三、定时触发（专业版独有）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回三、定时触发（专业版独有）的处理结果,包含执行状态码、结果数据和执行日志。### 四、数据库持久化（专业版独有）
| 数据库 | 说明 |
|--------|------|
| `关系型数据库` | 企业级关系数据库，推荐生产使用 |
| MySQL | 流行关系数据库 |
| SQLite | 轻量级本地数据库 |
| Redis | 高性能内存数据库（缓存层） |

```python
queue = ProQueue(
    slug="db-backed",
    storage="database",
    database_url="关系型数据库://user:pass@host:5432/db"
)

queue.enqueue_batch(tasks)  # 全部成功或全部回滚
history = queue.query_history(
    status="done",
    date_from="2026-01-01",
    date_to="2026-01-31"
)
```

**处理**: 解析四、数据库持久化（专业版独有）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回四、数据库持久化（专业版独有）的处理结果,包含执行状态码、结果数据和执行日志。### 五、监控仪表盘（专业版独有）
| 功能 | 说明 |
|------|------|
| 实时状态 | 队列长度、处理速度、Worker状态 |
| 历史统计 | 成功率、平均耗时、吞吐量趋势 |
| 告警面板 | 失败任务、卡住任务、资源告警 |
| 任务详情 | 查看任意任务的完整信息与日志 |
| Worker监控 | 各Worker的负载与处理统计 |

```python
queue.enable_dashboard(
    port=8080,
    auth=True,
    username="admin",
    password="${DASHBOARD_PASSWORD}"
)

```

### 六、告警通知（专业版独有）
| 告警类型 | 触发条件 | 推送渠道 |
|----------|----------|----------|
| 任务失败 | 单个任务执行失败 | 邮件/企业微信 |
| 批量失败 | 失败率超过阈值 | 邮件/企业微信/飞书 |
| 队列积压 | 待处理任务超过阈值 | 邮件/企业微信 |
| Worker失联 | Worker超过时间无心跳 | 邮件/电话 |
| 处理卡住 | 任务处理时间超过阈值 | 邮件/企业微信 |

```python
queue = ProQueue(
    slug="alerted-queue",
    alerts={
        "on_failure": True,
        "on_batch_failure": {"threshold": 0.1},  # 失败率>10%告警
        "on_backlog": {"threshold": 1000},        # 积压>1000告警
        "on_worker_down": True,
        "on_stuck": {"timeout": 3600},            # 处理>1小时告警
        "channels": ["email", "wechat_work", "feishu"]
    }
)
```

**输出**: 返回六、告警通知（专业版独有）的处理结果,包含执行状态码、结果数据和执行日志。
### 七、任务依赖编排（专业版独有）
| 编排模式 | 说明 |
|----------|------|
| 串行依赖 | A完成后执行B |
| 并行执行 | A和B同时执行 |
| 汇聚依赖 | A和B都完成后执行C |
| 条件分支 | 根据A的结果决定执行B或C |
| 循环 | 遍历列表执行 |

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供七、任务依赖编排（专业版独有）所需的指令和必要参数。
### 八、免费版全部功能
专业版包含免费版的全部功能：任务入队与去重、任务处理与进度追踪、断点恢复、锁机制与并发控制、失败任务重试。详见免费版文档。

**输入**: 用户提供八、免费版全部功能所需的指令和必要参数。
**输出**: 返回八、免费版全部功能的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`八、免费版全部功能`的配置文档进行参数调优
#
## 适用场景

### 场景一：大规模数据ETL（数据工程师）
**痛点**：每日需处理TB级数据，涉及采集、清洗、加载多环节，单进程处理需12小时，需分布式加速。

**解决方案**：

> 详细代码示例已移至 `references/detail.md`

**效果**：ETL从12小时缩短至2小时，8个Worker并行处理，失败自动告警。

### 场景二：分布式爬虫调度（爬虫工程师）
**痛点**：需爬取100万个页面，单机需3天，需多机分布式且不重复爬取。

**解决方案**：

> 详细代码示例已移至 `references/detail.md`

**效果**：100万页面从3天缩短至8小时，16个Worker跨4台机器并行，无重复爬取。

> 详细内容已移至 `references/detail.md` - ### 场景三：企业级批处理（系统架构师）
### 场景四：实时监控与告警（运维工程师）
**痛点**：任务队列需要7x24小时稳定运行，需实时监控与异常告警。

**解决方案**：

> 详细代码示例已移至 `references/detail.md`

**效果**：队列运行状态实时可见，异常分钟级告警，运维效率提升5倍。

### 场景五：跨系统数据同步（集成工程师）
**痛点**：需在CRM、ERP、BI系统间同步数据，各系统API不同，需编排复杂同步流程。

**解决方案**：

> 详细代码示例已移至 `references/detail.md`

**效果**：跨系统同步从手动半天变为自动1小时一次，数据一致性达99.9%。

### 场景六：高优先级任务插队（产品经理）
**痛点**：日常批处理任务运行中，突然有紧急任务需要优先处理。

**解决方案**：

```python
queue = ProQueue(
    slug="mixed-priority",
    priority_schedule=True,
    distributed=True,
    worker_count=4
)

for item in routine_data:
    queue.enqueue(task_id=f"routine_{item.id}", payload=item, priority=3)

for item in urgent_data:
    queue.enqueue(task_id=f"urgent_{item.id}", payload=item, priority=10)

```

**效果**：紧急任务响应时间从小时级缩短至分钟级，不影响日常批处理。

## 使用流程

### 基础搭建（<60秒）
初始化专业版队列与数据库连接：

```bash
pip install psycopg2-binary redis schedule flask
```

```python
from task_queue_manager import ProQueue

queue = ProQueue(
    slug="enterprise-tasks",
    storage="database",              # 使用数据库存储
    database_url="关系型数据库://...",  # PostgreSQL连接
    enable_monitoring=True,           # 启用监控
    enable_alerts=True                # 启用告警
)

queue.enqueue(task_id="urgent_001", payload=data, priority=10)
```

### 标准搭建（<120秒）
配置分布式Worker与告警：

> 详细代码示例已移至 `references/detail.md`

> 详细内容已移至 `references/detail.md` - ### 完整搭建（<300秒）

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | task-queue-manager处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| Worker无法连接数据库 | 连接配置错误/网络问题 | 验证连接字符串；
| 分布式Worker任务重复 | 锁机制失效/锁过期 | 检查锁配置；调大lock_stale_minutes；检查时钟同步 | 高 |
| 优先级调度不准 | 优先级配置错误/饥饿提升 | 验证优先级配置；检查动态提升参数 | 中 |
| DAG执行卡住 | 依赖配置错误/循环依赖 | 检查DAG拓扑；移除循环依赖；查看卡住节点 | 高 |
| 监控仪表盘无法访问 | 端口占用/认证失败 | 更换端口；检查认证配置 | 中 |
| 告警未触发 | 告警规则配置错误 | 验证阈值配置；检查渠道Token | 高 |
| 告警频繁触发 | 阈值设置不合理 | 调整阈值；启用告警去重；设置静默期 | 中 |
| 数据库性能下降 | 索引缺失/连接过多 | 添加索引；使用连接池；优化查询 | 中 |
| 定时任务未触发 | cron表达式错误/时区错误 | 验证cron表达式；检查时区配置 | 高 |
| 任务大量失败 | 处理逻辑错误/资源不足 | 查看失败日志；检查资源；修复处理逻辑 | 高 |
| Worker频繁失联 | 网络不稳定/资源耗尽 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **数据库**: `关系型数据库`/MySQL/SQLite（专业版数据库持久化需要）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | 系统自带或从python.org安装 |
| psycopg2 | Python库 | 专业版可选 | `pip install psycopg2-binary`（`关系型数据库`） |
| redis | Python库 | 专业版可选 | `pip install redis`（Redis缓存） |
| flask | Python库 | 专业版必需 | `pip install flask`（监控仪表盘） |
| schedule | Python库 | 专业版可选 | `pip install schedule`（定时触发） |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- 数据库连接需配置连接字符串（存储于环境变量）
- 告警通知需配置各渠道Token（存储于环境变量）
- 监控仪表盘需配置访问密码（存储于环境变量）
- LLM调用由Agent平台内置LLM提供（专业版使用GPT-4o路由）
- 所有敏感信息通过环境变量配置，禁止硬编码

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 队列管理

## 案例展示

### 与数据库集成
支持 `关系型数据库`、MySQL、SQLite、Redis等多种数据库。连接配置存储在环境变量中：

```python
queue = ProQueue(
    storage="database",
    database_url=os.getenv('POSTGRES_URL')
)

queue = ProQueue(
    storage="database",
    database_url=os.getenv('POSTGRES_URL'),
    cache_url=os.getenv('REDIS_URL')  # Redis缓存加速
)
```

### 与消息队列集成
```python
queue.consume_from_kafka(topic="tasks")

queue.consume_from_rabbitmq(queue="task_queue")
```

### 与监控系统集成
```python
queue.export_metrics(port=9090)

```

### 与告警平台集成

> 详细代码示例已移至 `references/detail.md`

## 常见问题

### Q1：免费版与专业版有什么区别？
免费版提供核心队列管理（入队去重、断点恢复、锁机制、失败重试）。专业版新增分布式处理、优先级调度、定时触发、数据库持久化、监控仪表盘、告警通知、DAG依赖编排七大高级功能。此外提供6种角色场景指南和性能优化策略。

### Q2：分布式处理如何工作？
专业版支持多Worker并行处理。Worker可分布在不同机器上，通过数据库共享队列状态。任务自动分配给空闲Worker，支持负载均衡与故障转移。Worker失联后其任务自动重新分配。

### Q3：优先级调度如何防止低优先级任务饥饿？
采用动态优先级提升策略：低优先级任务随等待时间增加自动提升优先级。同时支持公平调度，保证低优先级任务定期获得执行机会。可配置提升速率与公平调度间隔。

### Q4：数据库持久化相比文件存储有什么优势？
数据库存储优势：(1) 支持事务，保证原子性；(2) 支持并发安全的多Worker访问；(3) 支持复杂查询（按状态/时间/优先级筛选）；(4) 支持大规模任务（百万级+）；(5) 支持历史数据分析。文件存储适合小规模与无数据库环境。

### Q5：DAG依赖编排支持哪些模式？
支持五种编排模式：串行依赖（A→B）、并行执行（A∥B）、汇聚依赖（A+B→C）、条件分支（A?B:C）、循环（遍历列表）。可嵌套组合实现任意复杂工作流。DAG会自动检测循环依赖并报错。

### Q6：监控仪表盘提供哪些功能？
提供五大功能：(1) 实时队列状态（长度/速度/Worker）；(2) 历史统计（成功率/耗时趋势）；(3) 告警面板（失败/积压/卡住）；(4) 任务详情（任意任务完整信息）；(5) Worker监控（负载/处理统计）。支持密码认证。

### Q7：告警如何配置与升级？
通过JSON配置告警规则，包含触发条件、严重级别、推送渠道。支持告警升级：未确认时按链路升级（如5分钟未确认从邮件升级至电话）。告警去重机制避免短时间内重复推送。

### Q8：分布式Worker如何部署？
Worker可部署在同一机器（多进程）或不同机器（分布式）。部署步骤：(1) 配置统一的数据库连接；(2) 在每台机器上启动Worker进程；(3) Worker自动注册到队列；(4) 任务自动分配。支持容器化部署（Docker/K8s）。

### Q9：定时触发支持哪些调度方式？
支持三种调度：(1) cron表达式（如 `0 2 * * *` 每天2点）；(2) 一次性定时（指定日期时间）；(3) 固定间隔（如每1800秒）。支持时区配置。定时任务可暂停/恢复/删除。

### Q10：如何处理任务卡住（处理时间过长）？
专业版提供卡住检测：任务处理时间超过阈值（默认30分钟，可配置）时触发告警。可配置自动操作：(1) 告警通知；(2) 自动超时标记失败；(3) 重新分配给其他Worker。建议为每个任务设置合理超时。

### Q11：支持任务取消吗？
支持。通过 `queue.cancel(task_id)` 取消待处理任务。正在执行中的任务通过协作式取消（Worker检查取消标志后优雅停止）。取消的任务记录到取消列表，不会重复执行。

### Q12：如何查看历史执行记录？
通过监控仪表盘或API查询：`queue.query_history(status, date_from, date_to)` 可按状态与时间范围筛选。数据库存储支持复杂查询（如按优先级、Worker、耗时筛选）。历史记录可导出为CSV/Excel。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

