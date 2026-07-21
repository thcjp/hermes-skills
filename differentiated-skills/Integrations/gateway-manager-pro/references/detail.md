# 详细参考 - gateway-manager-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
observe:
  tracing:
    enabled: true
    exporter: otlp
    endpoint: http://otel-collector:4317
    sampling: 0.1  # 10%采样
    propagate: w3c  # W3C Trace Context
  logging:
    enabled: true
    exporter: loki
    endpoint: http://loki:3100
    fields:
      - timestamp
      - request_id
      - trace_id
      - method
      - path
      - status
      - latency
      - upstream
      - tenant_id
      - user_id
    mask:
      - authorization
      - x-api-key
      - cookie

  alerting:
    rules:
      - name: high_error_rate
        condition: error_rate > 5%
        window: 5m
        severity: critical
        notify: [slack, pagerduty]
      - name: high_latency
        condition: p95_latency > 500ms
        window: 5m
        severity: warning
        notify: [slack]
      - name: circuit_breaker_open
        condition: circuit_breaker.state == open
        window: 1m
        severity: critical
        notify: [slack, pagerduty]
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│              API网关管理器专业版 (GATEWAY MANAGER PRO)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  基础层      │  │  流量治理层  │  │  容灾层      │              │
│  │  BASE       │  │  TRAFFIC    │  │  RESILIENCE │              │
│  │             │  │             │  │             │              │
│  │ 声明式路由  │  │ 多租户限流  │  │ 熔断器      │              │
│  │ 统一认证    │  │ 分布式限流  │  │ 降级策略    │              │
│  │ 基础限流    │  │ 灰度发布    │  │ 重试与超时  │              │
│  │ 监控指标    │  │ AB测试      │  │ 故障转移    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  动态层      │  ← 配置热更新                   │
│                  │  DYNAMIC    │    ✅ 专业版                    │
│                  │  动态下发   │                                 │
│                  │  热重载     │                                 │
│                  │  dry-run    │                                 │
│                  └─────────────┘                                 │
│                          │                                       │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  可观测层    │  ← 全链路追踪                   │
│                  │  OBSERVE    │    ✅ 专业版                    │
│                  │  链路追踪   │                                 │
│                  │  日志聚合   │                                 │
│                  │  告警       │                                 │
│                  └─────────────┘                                 │
│                          │                                       │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  扩展层      │  ← 自定义插件                   │
│                  │  EXTEND     │    ✅ 专业版                    │
│                  │  插件SDK    │                                 │
│                  │  插件市场   │                                 │
│                  └─────────────┘                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (yaml)

```yaml
routes:
  - name: order-service
    path: /api/v1/orders/*
    upstream:
      primary: http://order-service:8001
      secondary: http://order-service-backup:8001  # 故障转移
    auth:
      type: jwt
      secret_env: JWT_SECRET
    rate_limit:
      type: distributed_sliding_window  # 分布式限流
      qps: 1000
      redis:
        url_env: REDIS_URL
        cluster: true
    circuit_breaker:                    # 熔断器
      enabled: true
      threshold: 50                     # 错误率50%触发熔断
      window: 60s                       # 60秒窗口
      recovery: half_open               # 半开探测恢复
      fallback:
        status: 503
        body: '{"code":503,"message":"服务降级中"}'
    canary:                             # 灰度发布
      enabled: true
      strategy: header                  # 按Header灰度
      header: X-Canary
      value: true
      upstream: http://order-service-v2:8001
```

## 代码示例 (bash)

```bash
gateway-manager validate --config <file>
gateway-manager render --config <file> --target <gateway> --output <file>
gateway-manager dry-run --config <file> --traffic <file>

gateway-manager dynamic init --control-plane <url>
gateway-manager dynamic apply --config <file> --validate
gateway-manager dynamic rollback --to <version>
gateway-manager dynamic versions
gateway-manager dynamic diff <v1> <v2>

gateway-manager rate-limit status --route <name>
gateway-manager circuit-breaker status --route <name>
gateway-manager canary status --route <name>

gateway-manager observe enable --tracing --logging --alerting
gateway-manager observe dashboard  # 打开监控看板
gateway-manager observe trace <trace-id>  # 查看单条trace
gateway-manager plugin list
gateway-manager plugin install <name>
gateway-manager plugin enable --route <name> --plugin <name>
gateway-manager plugin disable --route <name> --plugin <name>

gateway-manager record --sample <rate> --duration <time> --output <file>
gateway-manager replay --recording <file> --target <url>

gateway-manager audit log --since <time>
gateway-manager audit who-changed <config>
```

## 代码示例 (yaml)

```yaml
canary:
  strategy: header
  header: X-Canary
  value: true
  upstream: http://order-service-v2:8001
  fallback_upstream: http://order-service-v1:8001

canary:
  strategy: percentage
  percentage: 10
  upstream_v1: http://order-service-v1:8001
  upstream_v2: http://order-service-v2:8001
  key: jwt:sub  # 按用户hash分流，同一用户始终命中同一版本
ab_test:
  experiment: checkout_flow_v2
  key: jwt:sub
  variants:
    - name: control
      weight: 50
      upstream: http://order-service:8001
    - name: treatment
      weight: 50
      upstream: http://order-service-v2:8001
  metrics:
    - conversion_rate
    - avg_order_value
```

## 代码示例 (yaml)

```yaml
rate_limit:
  type: tenant_aware
  tenant_header: X-Tenant-Id
  rules:
    - tenant_tier: enterprise     # 企业版租户
      qps: 1000
      burst: 200
      daily_quota: 10000000       # 日配额1000万次
    - tenant_tier: pro            # 专业版租户
      qps: 200
      burst: 50
      daily_quota: 1000000
    - tenant_tier: free           # 免费版租户
      qps: 10
      burst: 5
      daily_quota: 10000
    - default: true               # 未识别租户
      qps: 5
      burst: 2
      daily_quota: 1000
  over_limit_response:
    status: 429
    body: '{"code":429,"message":"配额已用尽，请升级套餐"}'
    headers:
      Retry-After: 3600
```

## 代码示例 (python)

```python
from gateway_plugin import Plugin, PluginContext

class AuditLogPlugin(Plugin):
    name = "audit_log"
    phase = "log"  # 在日志阶段执行
    def __init__(self, config):
        self.audit_url = config["audit_url"]
        self.sensitive_fields = config.get("sensitive_fields", [])

    def execute(self, ctx: PluginContext):
        body = ctx.request_body
        for field in self.sensitive_fields:
            if field in body:
                body[field] = "***"

        ctx.async_http_post(self.audit_url, {
            "timestamp": ctx.timestamp,
            "user_id": ctx.user_id,
            "tenant_id": ctx.tenant_id,
            "method": ctx.method,
            "path": ctx.path,
            "status": ctx.status,
            "body": body,
        })
```

## 代码示例 (bash)

```bash
gateway-manager record --sample 0.01 --duration 1h --output ./traffic.json

gateway-manager dry-run \
  --config gateway-new.yaml \
  --traffic ./traffic.json \
  --report ./dry-run-report.html

DRY-RUN REPORT
==============
Traffic Samples: 360,000
Config: gateway-new.yaml

Results:
  MATCHED:      359,520 (99.8%)
  UNMATCHED:    480 (0.1%)   ← 新配置漏了这些路由
  RATE_LIMITED: 1,200 (0.3%) ← 新限流规则会限这些请求
  BLOCKED:      0 (0%)

Issues:
1. 480 requests to /api/v1/legacy/* would be UNMATCHED
   Suggestion: 添加 /api/v1/legacy/* 路由，或确认已下线
2. 1,200 requests from tenant "free-tier" would be RATE_LIMITED
   Suggestion: 确认免费租户10QPS是否合适
```

## 代码示例 (yaml)

```yaml
groups:
  - name: gateway
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(gateway_request_total{status=~"5.."}[5m])) by (route)
          / sum(rate(gateway_request_total[5m])) by (route) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "路由 {{ $labels.route }} 错误率超5%"

      - alert: CircuitBreakerOpen
        expr: gateway_circuit_breaker_state == 1
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "熔断器开启: {{ $labels.route }}"
```

## 代码示例 (yaml)

```yaml
name: 网关配置部署
on:
  push:
    paths: ['gateway/*.yaml']
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 安装网关管理器
        run: npm install -g gateway-manager-pro
      - name: 配置校验
        run: gateway-manager validate --config gateway/production.yaml
      - name: dry-run测试
        run: gateway-manager dry-run --config gateway/production.yaml --traffic ./traffic-sample.json
      - name: 灰度推送（单节点）
        run: gateway-manager dynamic apply --config gateway/production.yaml --canary --nodes 1
      - name: 全量推送
        if: success()
        run: gateway-manager dynamic apply --config gateway/production.yaml
```

## 代码示例 (yaml)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: gateway-config
data:
  gateway.yaml: |
    routes:
      - name: user-service
        path: /api/v1/users/*
        upstream: http://user-service.default.svc:8001
apiVersion: gateway.manager/v1
kind: GatewayConfig
metadata:
  name: production
spec:
  configRef: gateway-config
  strategy: rolling
  validation: dry-run
```

## 代码示例 (yaml)

```yaml
circuit_breaker:
  enabled: true
  trigger:
    error_rate: 50          # 错误率≥50%
    error_count: 100        # 或错误数≥100
    slow_call_rate: 60      # 或慢调用占比≥60%（>1秒）
  window: 60s               # 统计窗口60秒
  min_calls: 20             # 窗口内最少调用数（不足不触发）
  open_duration: 30s        # 熔断持续30秒
  recovery: half_open       # 半开探测
  half_open_calls: 5        # 半开时放5个请求探测
  fallback:
    strategy: cached_response   # 返回缓存响应
    cache_ttl: 300s
```

### 功能6：可观测性套件
**解决痛点**：网关出问题不知道是哪条路由、哪个上游、哪个用户。

**专业版能力**：全链路追踪、日志聚合、告警三位一体。

```yaml
observe:
  tracing:
    enabled: true
    exporter: otlp
    endpoint: http://otel-collector:4317
    sampling: 0.1  # 10%采样
    propagate: w3c  # W3C Trace Context
  logging:
    enabled: true
    exporter: loki
    endpoint: http://loki:3100
    fields:
      - timestamp
      - request_id
      - trace_id
      - method
      - path
      - status
      - latency
      - upstream
      - tenant_id
      - user_id
    mask:
      - authorization
      - x-api-key
      - cookie

  alerting:
    rules:
      - name: high_error_rate
        condition: error_rate > 5%
        window: 5m
        severity: critical
        notify: [slack, pagerduty]
      - name: high_latency
        condition: p95_latency > 500ms
        window: 5m
        severity: warning
        notify: [slack]
      - name: circuit_breaker_open
        condition: circuit_breaker.state == open
        window: 1m
        severity: critical
        notify: [slack, pagerduty]
```



## 架构总览
```text
┌─────────────────────────────────────────────────────────────────┐
│              API网关管理器专业版 (GATEWAY MANAGER PRO)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  基础层      │  │  流量治理层  │  │  容灾层      │              │
│  │  BASE       │  │  TRAFFIC    │  │  RESILIENCE │              │
│  │             │  │             │  │             │              │
│  │ 声明式路由  │  │ 多租户限流  │  │ 熔断器      │              │
│  │ 统一认证    │  │ 分布式限流  │  │ 降级策略    │              │
│  │ 基础限流    │  │ 灰度发布    │  │ 重试与超时  │              │
│  │ 监控指标    │  │ AB测试      │  │ 故障转移    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  动态层      │  ← 配置热更新                   │
│                  │  DYNAMIC    │    ✅ 专业版                    │
│                  │  动态下发   │                                 │
│                  │  热重载     │                                 │
│                  │  dry-run    │                                 │
│                  └─────────────┘                                 │
│                          │                                       │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  可观测层    │  ← 全链路追踪                   │
│                  │  OBSERVE    │    ✅ 专业版                    │
│                  │  链路追踪   │                                 │
│                  │  日志聚合   │                                 │
│                  │  告警       │                                 │
│                  └─────────────┘                                 │
│                          │                                       │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  扩展层      │  ← 自定义插件                   │
│                  │  EXTEND     │    ✅ 专业版                    │
│                  │  插件SDK    │                                 │
│                  │  插件市场   │                                 │
│                  └─────────────┘                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```



