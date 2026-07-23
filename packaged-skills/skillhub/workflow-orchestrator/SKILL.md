---
slug: "workflow-orchestrator"
name: "workflow-orchestrator"
version: "1.0.0"
displayName: "工作流编排器(专业版)"
summary: "全功能工作流编排与调度，含cron调度、DAG并行、熔断器、监控告警与分布式执行。"
license: "Proprietary"
edition: "pro"
description: |-
  工作流编排器专业版是在免费版基础上的全功能升级，为自动化团队提供企业级工作流编排与调度能力。除核心编排能力外，解锁高级调度、复杂重试策略、并行执行、监控告警、分布式执行、版本管理、可视化编排七大高级功能。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - 工作流编排
  - 自动化
  - 任务调度
  - 分布式执行
  - 监控告警
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 工作流编排器(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 工作流编排器(专业版)全功能工作流编排 | 不支持 | 支持 |
| 工作流编排器(专业版)含cron调度 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |

## 核心能力

### 1. 高级调度（专业版）
> 详细代码示例已移至 `references/detail.md`

**cron表达式说明**：

| 表达式 | 含义 |
|:-----|:-----|
| `0 2 * * *` | 每天凌晨2点 |
| `*/15 * * * *` | 每15分钟 |
| `0 9 * * 1-5` | 工作日早上9点 |
| `0 0 1 * *` | 每月1号 |

**输入**: 用户提供高级调度（专业版）所需的指令和必要参数.
**处理**: 解析高级调度（专业版）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回高级调度（专业版）的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`可视化编排（专业版）`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`版本管理（专业版）`的配置文档进行参数调优
### 2. 复杂重试策略（专业版）
> 详细代码示例已移至 `references/detail.md`

**重试策略对比**：

| 策略 | 适用场景 | 优点 | 缺点 |
|---:|---:|---:|---:|
| 固定间隔 | 临时故障 | 简单 | 可能加重负载 |
| 指数退避 | 网络抖动 | 自动适应 | 耗时较长 |
| 熔断器 | 级联故障 | 保护系统 | 需恢复时间 |
| 降级方案 | 持续故障 | 保证可用 | 结果降级 |

**输入**: 用户提供复杂重试策略（专业版）所需的指令和必要参数.
**处理**: 解析复杂重试策略（专业版）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**DAG执行示例**：

```text
fetch-a ──┐
fetch-b ──┼──> merge ──> transform ──> output
fetch-c ──┘
# ...
时间线：
T0: fetch-a, fetch-b, fetch-c 并行执行
T1: 全部完成后，merge执行
T2: transform执行
T3: output执行
```

**输入**: 用户提供DAG并行执行（专业版）所需的指令和必要参数.
### 4. 监控告警（专业版）
> 详细代码示例已移至 `references/detail.md`

**监控指标**：

| 指标 | 说明 | 默认阈值 |
|:---:|:---:|:---:|
| duration | 执行时长 | >3600s |
| success_rate | 成功率 | <95% |
| error_count | 错误数 | >0 |
| cpu | CPU使用率 | >80% |
| memory | 内存使用率 | >85% |
| data_volume | 数据量 | - |

**输入**: 用户提供监控告警（专业版）所需的指令和必要参数.
**输出**: 返回监控告警（专业版）的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 分布式执行（专业版）
```bash
workflow node add --name "worker-1" --host "worker-1.local" --capacity 4
workflow node add --name "worker-2" --host "worker-2.local" --capacity 4
# ...
workflow node list --verbose
# ...
workflow distribute --flow my-flow --strategy least-loaded
# ...
workflow remote execute --flow my-flow --node "worker-1"
# ...
workflow balance --strategy round-robin
```

**分发策略**：

| 策略 | 说明 | 适用场景 |
|:------|------:|:------|
| round-robin | 轮询分配 | 节点性能均匀 |
| least-loaded | 最少负载 | 节点性能不均 |
| affinity | 亲和性 | 数据本地化 |
| random | 随机 | 简单场景 |

**输入**: 用户提供分布式执行（专业版）所需的指令和必要参数.
**输出**: 返回分布式执行（专业版）的处理结果,包含执行状态码、结果数据和执行日志.
### 6. 版本管理（专业版）
```bash
workflow version log --flow my-flow
# ...
workflow version diff --flow my-flow --from "v1.0" --to "v2.0"
# ...
workflow version rollback --flow my-flow --to "v1.0"
# ...
workflow version tag --flow my-flow --tag "stable"
# ...
workflow version export --flow my-flow --version "v1.0" --output "flow-v1.0.tar.gz"
```

**处理**: 解析版本管理（专业版）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `版本管理（专业版）` 选项
- 处理流程: 接收输入 -> 执行版本管理（专业版） -> 返回结果
- 输入: 用户提供版本管理（专业版）所需的参数和指令
- 输出: 返回版本管理（专业版）的处理结果,包含执行状态码、结果数据和执行日志

### 7. 可视化编排（专业版）
```bash
workflow visualize --port 8080
# ...
workflow visualize dag --flow my-flow --output "dag.png"
# ...
workflow visualize realtime --flow my-flow
# ...
workflow visualize report --flow my-flow --run-id "run-001" --output "report.html"
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `可视化编排（专业版）` 选项

#
## 适用场景

### 场景一：企业级数据管道（数据工程团队角色）
**痛点**：企业数据管道涉及多数据源、多阶段处理，需要定时调度、并行执行与故障自愈.
**对策**：用DAG并行+熔断器+监控告警构建健壮的数据管道.
```bash
workflow dag execute --file pipelines/etl-dag.yaml --max-workers 8
# ...
workflow retry circuit-breaker --flow etl-pipeline --threshold 5 --cooldown 300
# ...
workflow monitor alert --flow etl-pipeline --metric success_rate --threshold 95
workflow monitor notify --flow etl-pipeline --channels "slack,pagerduty"
```

**效果**：管道执行时间缩短约60%（并行化），故障恢复<5分钟（熔断器+告警）.
### 场景二：多团队协作的流水线管理（DevOps负责人角色）
**痛点**：多团队共享流水线基础设施，需要权限隔离与版本管理.
**对策**：用版本管理+分布式执行支持多团队协作.
```bash
workflow schedule add --flow team-a-pipeline --cron "0 2 * * *"
# ...
workflow remote execute --flow team-b-pipeline --node "worker-2"
# ...
workflow version diff --flow shared-pipeline --from "team-a" --to "team-b"
```

### 场景三：SLA敏感的定时任务（SRE角色）
**痛点**：SLA要求任务必须在指定时间内完成，超时需告警.
**对策**：用cron调度+超时告警+降级方案保障SLA.
```bash
workflow monitor alert --flow sla-critical --metric duration --threshold 3600
workflow monitor notify --flow sla-critical --channels "pagerduty"
# ...
workflow retry fallback --flow sla-critical --fallback-flow sla-critical-degraded
```

### 场景四：大规模并行ETL（数据工程师角色）
**痛点**：单机ETL处理TB级数据耗时过长.
**对策**：用DAG并行+分布式执行加速.
```bash
workflow dag execute --file etl-parallel.yaml --max-workers 16
# ...
workflow distribute --flow etl-parallel --strategy least-loaded
```

### 场景五：故障自愈的自动化流程（运维角色）
**痛点**：自动化流程故障后需要人工干预，MTTR（平均恢复时间）长.
**对策**：用熔断器+降级方案+自动重试实现自愈.
```bash
workflow retry config --flow auto-process \
  --strategy exponential --max-attempts 5
workflow retry circuit-breaker --flow auto-process --threshold 5 --cooldown 300
workflow retry fallback --flow auto-process --fallback-flow auto-process-safe
```

### 场景六：合规审计的工作流追踪（合规角色）
**痛点**：合规审计要求工作流执行可追溯，包括谁在何时执行了什么.
**对策**：用版本管理+监控历史提供审计追踪.
```bash
workflow monitor history --flow compliance-flow --period "90d"
# ...
workflow monitor report --flow compliance-flow --period "90d" --format csv --output "audit.csv"
# ...
workflow version log --flow compliance-flow
```

### 场景七：微服务编排（架构师角色）
**痛点**：微服务间的业务流程编排复杂，缺乏统一的编排工具.
**对策**：用事件驱动+条件触发编排微服务.
```bash
workflow schedule event --flow order-fulfillment --event "api:order.created"
workflow schedule dependency --flow inventory-update --after "order-fulfillment"
workflow schedule conditional --flow notify-customer \
  --condition "order.status == 'shipped'"
```

## 使用流程

### 基础搭建（<60秒）
```bash
mkdir -p workflows/components/{connections,nodes,triggers}
mkdir -p workflows/flows/my-flow/{state,data,logs}
```

### 标准搭建（<120秒）
在基础搭建之上，启用调度与监控：

> 详细内容已移至 `references/detail.md` - ### 完整搭建（<300秒）

以下是工作流编排器(专业版)的快速搭建流程，从初始化到完整配置的步骤说明.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|:---|---:|---:|
| content | string | 否 | workflow-orchestrator处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "orchestrator_result": "orchestrator_result_value",
      "orchestrator_metadata": "orchestrator_metadata_value",
      "orchestrator_status": "orchestrator_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/workflow-orchestrator_template`

## 异常处理

| 问题 | 可能原因 | 解决方案 | 优先级 |
|:------:|--------|:-------|:------:|
| 调度未触发 | cron表达式错误或时区错误 | 验证cron语法；检查时区配置 | 高 |
| DAG并行度低 | 依赖过多或worker不足 | 分析依赖图；增加max-workers | 中 |
| 熔断器频繁触发 | 下游服务不稳定 | 检查下游服务；调整threshold与cooldown | 高 |
| 分布式节点失联 | 网络问题或节点宕机 | 
| 监控无数据 | 监控未启用或权限不足 | `monitor enable`；检查权限 | 高 |
| 告警未触发 | 阈值设置不合理 | 检查阈值；确认告警条件 | 中 |
| 版本回滚失败 | 历史版本不存在 | 检查`version log`；确认版本ID | 中 |
| 降级方案未触发 | fallback未配置 | `retry fallback`配置降级流程 | 中 |
| 可视化界面无响应 | 端口被占用或服务未启动 | 检查端口；`visualize --port` | 低 |
| 工作流卡住 | 锁文件未释放 | 删除`/tmp/workflow-*.lock`；检查flock | 中 |
| 分布式任务分发不均 | 负载均衡策略不当 | 切换策略（round-ro（请参考skill目录中的脚本文件）） | 低 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Linux / macOS（Windows需WSL或Git Bash）
- **Shell**: Bash 4+（需要flock支持）
- **Python**: 3.8+（用于监控与可视化，专业版功能）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|----|:--:|---:|----|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| jq | JSON处理 | 必需 | 系统包管理器安装 |
| yq | YAML解析 | 必需 | 系统包管理器安装 |
| curl | HTTP工具 | 必需 | 系统自带 |
| flock | 锁文件 | 必需 | Linux自带/macOS需安装 |
| Python 3.8+ | 运行时 | 专业版必需 | 从python.org安装 |
| SSH | 远程执行 | 分布式必需 | 系统自带 |

### API Key 配置
- API凭证通过环境变量配置，禁止硬编码
- 分布式执行的SSH密钥存储在`~/.ssh/`目录
- 告警webhook URL通过环境变量配置
- 建议将凭证存储在`~/.workflow-orchestrator/credentials/`目录（已gitignore）

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行工作流编排任务

## 案例展示

### 与CI/CD集成
```bash
workflow trigger --flow deploy-pipeline --params "branch=$BRANCH"
# ...
workflow wait --flow deploy-pipeline --timeout 3600
# ...
workflow version rollback --flow deploy-pipeline --tag "stable"
```

### 与监控系统集成
```bash
workflow monitor export --format prometheus --port 9090
# ...
workflow monitor dashboard --import grafana-template.json
```

### 与告警系统集成
```bash
workflow monitor notify --channel pagerduty --integration-key "$PD_KEY"
# ...
workflow monitor notify --channel slack --webhook "$SLACK_WEBHOOK"
```

### 与Agent平台集成
```markdown
将 workflow-orchestrator-pro 添加到Agent的技能列表中.
Agent可通过自然语言指令驱动工作流编排与调度.
LLM路由至GPT-4o，确保复杂调度决策的质量.
```

## 常见问题

### Q1：免费版与专业版有什么区别？
免费版提供核心编排能力（目录结构/数据流/状态管理/错误声明/锁文件/组件复用）。专业版解锁七大高级功能：高级调度、复杂重试策略、DAG并行执行、监控告警、分布式执行、版本管理、可视化编排。此外提供多角色场景指南、性能优化策略和多平台集成示例.
### Q2：支持多少个并发工作流？
专业版默认支持10个并发，可通过`maxConcurrent`配置调整。分布式模式下支持数百个并发（受节点数量限制）.
### Q3：DAG并行如何确定可并行节点？
通过依赖图分析。无依赖关系的节点自动并行执行，有依赖的节点按拓扑顺序串行。例如fetch-a/b/c无依赖则并行，merge依赖三者则等待.
### Q4：熔断器触发后如何恢复？
熔断器在cooldown时间（默认300秒）后自动进入半开状态，尝试执行一次。成功则关闭熔断器，失败则重新熔断.
### Q5：分布式执行需要什么网络条件？
节点间需要SSH免密登录或API可达。建议在同一内网或VPN中。跨公网执行需考虑网络延迟与安全性.
### Q6：版本管理支持分支吗？
支持。每个版本相当于一个快照，可通过tag标记。支持任意版本间的对比与回滚.
### Q7：可视化编排支持哪些浏览器？
支持所有现代浏览器（Chrome/Firefox/Safari/Edge）。提供DAG图渲染、实时执行视图、历史回放等功能.
### Q8：监控数据存储在哪里？
默认存储在本地`~/.workflow-orchestrator/metrics/`目录。专业版支持导出到Prometheus、InfluxDB等外部时序数据库.
### Q9：可以与现有调度系统共存吗？
可以。专业版支持以 exporter 模式运行，与Airflow、Prefect等调度系统集成。也支持被外部系统通过API触发.
### Q10：降级方案如何定义？
降级方案是一个独立的工作流（如my-flow-degraded），在主流程失败时自动执行。通常提供简化版的结果，保证业务可用性.
### Q11：专业版数据存储在哪里？安全吗？
所有数据存储在本地`workflows/`与`~/.workflow-orchestrator/`目录。分布式执行的数据通过SSH加密传输。API凭证通过环境变量配置，不硬编码.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|----|----|----|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

