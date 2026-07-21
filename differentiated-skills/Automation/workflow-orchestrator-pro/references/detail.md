# 详细参考 - workflow-orchestrator-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (json)

```json
{
  "scheduling": {
    "engine": "cron",
    "timezone": "Asia/Shanghai",
    "maxConcurrent": 10
  },
  "retry": {
    "defaultStrategy": "exponential",
    "circuitBreaker": {
      "enabled": true,
      "threshold": 5,
      "cooldown": 300
    }
  },
  "parallel": {
    "enabled": true,
    "maxWorkers": 8,
    "loadBalancer": "round-robin"
  },
  "monitor": {
    "enabled": true,
    "interval": 30,
    "metrics": ["duration", "success_rate", "error_count", "cpu", "memory"],
    "alerts": {
      "onFailure": true,
      "onSlowRun": true,
      "slowThreshold": 3600
    },
    "notifications": {
      "channels": ["webhook", "slack", "email"],
      "webhook": "$ALERT_WEBHOOK",
      "slack": "$SLACK_WEBHOOK",
      "email": "ops@example.com"
    }
  },
  "distributed": {
    "enabled": true,
    "nodes": ["node1.local", "node2.local", "node3.local"],
    "strategy": "least-loaded"
  },
  "versioning": {
    "enabled": true,
    "retention": 30
  },
  "visualization": {
    "enabled": true,
    "port": 8080
  }
}
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│            工作流编排器 专业版 (WORKFLOW ORCHESTRATOR PRO)         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  核心引擎层  │  │  调度层      │  │  重试策略层  │             │
│  │             │  │             │  │             │             │
│  │ 数据流      │  │ cron调度    │  │ 指数退避    │             │
│  │ 状态管理    │  │ 依赖图      │  │ 熔断器      │             │
│  │ 锁文件      │  │ 条件触发    │  │ 降级方案    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  并行执行层  │  │  监控告警层  │  │  分布式层    │             │
│  │             │  │             │  │             │             │
│  │ DAG并行     │  │ 指标采集    │  │ 多节点      │             │
│  │ 负载均衡    │  │ 阈值告警    │  │ 远程执行    │             │
│  │ 资源调度    │  │ 多渠道通知  │  │ 任务分发    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (bash)

```bash
cat > workflows/flows/parallel-pipeline/dag.yaml << 'EOF'
nodes:
  fetch-a:
    command: "curl -s $API_A > data/01-a.json"
  fetch-b:
    command: "curl -s $API_B > data/01-b.json"
  fetch-c:
    command: "curl -s $API_C > data/01-c.json"
  merge:
    command: "jq -s '[.[][]]' data/01-*.json > data/02-merge.json"
    depends_on: [fetch-a, fetch-b, fetch-c]
  transform:
    command: "jq '...' data/02-merge.json > data/03-transform.json"
    depends_on: [merge]
  output:
    command: "cp data/03-transform.json output.json"
    depends_on: [transform]
EOF

workflow dag execute --file workflows/flows/parallel-pipeline/dag.yaml

workflow dag config --max-workers 8 --load-balancer round-robin
```

## 代码示例 (bash)

```bash
cat > workflows/flows/my-flow/config.yaml << 'EOF'
schedule:
  cron: "0 2 * * *"    # 每天凌晨2点
  timezone: "Asia/Shanghai"

retry:
  max_attempts: 3
  backoff: exponential
  initial_delay: 5

monitor:
  enabled: true
  metrics: [duration, success_rate, error_count]
  alert:
    on_failure: true
    webhook: "$ALERT_WEBHOOK"
EOF

workflow monitor enable --flow my-flow
```

## 代码示例 (bash)

```bash
workflow monitor enable --flow my-flow --interval 30

workflow monitor metrics --flow my-flow

workflow monitor history --flow my-flow --since "7d" --metric duration

workflow monitor alert --flow my-flow \
  --metric duration \
  --threshold 3600 \
  --condition ">"

workflow monitor notify --flow my-flow \
  --channels "webhook,slack,email" \
  --webhook "$WEBHOOK_URL" \
  --slack "$SLACK_WEBHOOK" \
  --email "ops@example.com"

workflow monitor report --flow my-flow --period "30d" --output "report.md"
```

## 代码示例 (bash)

```bash
workflow schedule add --flow my-flow --cron "0 2 * * *" --timezone "Asia/Shanghai"

workflow schedule dependency --flow pipeline-B --after "pipeline-A"

workflow schedule conditional --flow etl-flow \
  --condition "data_size > 1000" \
  --check-interval 60

workflow schedule event --flow notify-flow --event "api:order.created"

workflow schedule list --verbose

workflow schedule pause --flow my-flow
workflow schedule resume --flow my-flow
```

## 代码示例 (bash)

```bash
workflow retry config --flow my-flow \
  --strategy exponential \
  --max-attempts 5 \
  --initial-delay 5 \
  --max-delay 300

workflow retry circuit-breaker --flow my-flow \
  --threshold 5 \
  --cooldown 300

workflow retry fallback --flow my-flow \
  --fallback-flow my-flow-degraded

workflow retry manual --flow my-flow --run-id "run-20260130"
```

### 完整搭建（<300秒）
配置分布式执行与可视化：

在 `~/.workflow-orchestrator/config.json` 中配置：

```json
{
  "scheduling": {
    "engine": "cron",
    "timezone": "Asia/Shanghai",
    "maxConcurrent": 10
  },
  "retry": {
    "defaultStrategy": "exponential",
    "circuitBreaker": {
      "enabled": true,
      "threshold": 5,
      "cooldown": 300
    }
  },
  "parallel": {
    "enabled": true,
    "maxWorkers": 8,
    "loadBalancer": "round-robin"
  },
  "monitor": {
    "enabled": true,
    "interval": 30,
    "metrics": ["duration", "success_rate", "error_count", "cpu", "memory"],
    "alerts": {
      "onFailure": true,
      "onSlowRun": true,
      "slowThreshold": 3600
    },
    "notifications": {
      "channels": ["webhook", "slack", "email"],
      "webhook": "$ALERT_WEBHOOK",
      "slack": "$SLACK_WEBHOOK",
      "email": "ops@example.com"
    }
  },
  "distributed": {
    "enabled": true,
    "nodes": ["node1.local", "node2.local", "node3.local"],
    "strategy": "least-loaded"
  },
  "versioning": {
    "enabled": true,
    "retention": 30
  },
  "visualization": {
    "enabled": true,
    "port": 8080
  }
}
```



## 架构总览
```text
┌─────────────────────────────────────────────────────────────────┐
│            工作流编排器 专业版 (WORKFLOW ORCHESTRATOR PRO)         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  核心引擎层  │  │  调度层      │  │  重试策略层  │             │
│  │             │  │             │  │             │             │
│  │ 数据流      │  │ cron调度    │  │ 指数退避    │             │
│  │ 状态管理    │  │ 依赖图      │  │ 熔断器      │             │
│  │ 锁文件      │  │ 条件触发    │  │ 降级方案    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          ▼                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  并行执行层  │  │  监控告警层  │  │  分布式层    │             │
│  │             │  │             │  │             │             │
│  │ DAG并行     │  │ 指标采集    │  │ 多节点      │             │
│  │ 负载均衡    │  │ 阈值告警    │  │ 远程执行    │             │
│  │ 资源调度    │  │ 多渠道通知  │  │ 任务分发    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```



