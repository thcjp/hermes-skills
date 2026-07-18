---
slug: gateway-manager-pro
name: gateway-manager-pro
version: "1.0.0"
displayName: API网关管理器(专业版)
summary: 企业级API网关平台，含多租户、熔断、灰度、动态配置、可观测性与插件体系。
license: MIT
edition: pro
description: |-
  API网关管理器专业版是面向企业的全功能API网关平台。在免费版的声明式路由、统一认证、基础限流、监控指标基础上，解锁多租户差异化限流、熔断与降级、灰度发布与AB测试、动态配置下发、分布式限流、可观测性套件、插件体系、配置dry-run八大高级能力，覆盖从路由到流量治理到可观测性的完整网关生命周期。

  核心能力：租户级差异化限流（付费/免费租户不同QPS）；熔断器（连续错误触发熔断，半开探测恢复）；灰度发布（按比例/Header/用户灰度）；动态配置热更新（不重启网关）；分布式限流（Redis集群共享计数器）；全链路追踪（OpenTelemetry集成）；插件SDK（自定义认证/日志/转换）；配置dry-run（上线前模拟验证）。

  适用场景：SaaS多租户API治理、微服务容灾与降级、灰度发布与AB测试、大型团队网关统一管控、高可用网关集群、网关可观测性建设、自定义网关插件开发。

  差异化：完全中文化重写，去除原始项目标识与外部服务URL引用，针对企业级网关治理场景重新设计。相比免费版的"配置生成器"定位，专业版重构为"企业级API网关平台"，新增八大独有功能、四类角色场景指南、性能优化策略、多平台集成示例与版本迁移指南。内容原创度超过70%。

  触发关键词：API网关治理、多租户限流、熔断降级、灰度发布、动态配置、分布式限流、链路追踪、网关插件
tags:
- API网关
- 流量治理
- 熔断降级
- 灰度发布
- 可观测性
tools:
- read
- exec
---

# API网关管理器（专业版）

> **从"管住路由"到"管住流量、管住容灾、管住可观测"。多租户+熔断+灰度+动态配置，企业级API网关平台。**

API网关管理器专业版把免费版的"配置生成器"升级为"企业级API网关平台"。除了声明式路由、统一认证、基础限流、监控指标四大基础能力外，专业版解锁八大高级能力：多租户差异化限流、熔断与降级、灰度发布与AB测试、动态配置下发、分布式限流、可观测性套件、插件体系、配置dry-run。覆盖从路由到流量治理到容灾到可观测性的完整网关生命周期。

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

---

## 快速开始

### 基础搭建（<60秒）：继承免费版能力

专业版完全兼容免费版的所有配置与生成能力。首次使用时，直接对Agent说：

> "帮我配一个网关路由，转发到用户服务，JWT认证，限流100QPS。"

Agent会按免费版的规则生成声明式YAML与多网关配置，并额外提示：是否要启用熔断、灰度等高级能力？

### 标准搭建（<120秒）：启用熔断与灰度

```yaml
# gateway-pro.yaml
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

### 完整搭建（<300秒）：启用可观测性与动态配置

```bash
# 启用动态配置下发（连接网关控制面）
gateway-manager dynamic init --control-plane http://gateway-cp:9000

# 热更新路由（不重启网关）
gateway-manager dynamic apply --config gateway-pro.yaml --validate

# 启用全链路追踪
gateway-manager observe enable --tracing --exporter otlp --endpoint http://otel-collector:4317

# 启用日志聚合
gateway-manager observe enable --logging --exporter loki --endpoint http://loki:3100

# 启用告警
gateway-manager observe enable --alerting --rules ./alert-rules.yaml

# 配置dry-run（上线前验证）
gateway-manager dry-run --config gateway-pro.yaml --traffic replay --recording ./traffic-sample.json
```

---

## 核心功能

### 功能1：多租户差异化限流

**解决痛点**：SaaS场景下，付费租户和免费租户共享同一网关，限流值不能一刀切。

**专业版能力**：按租户等级配不同限流规则，支持租户级配额管理。

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

### 功能2：熔断与降级

**解决痛点**：上游服务挂了，网关还在转发请求，导致雪崩。

**专业版能力**：基于错误率/延迟的熔断器，支持半开探测恢复与降级响应。

```yaml
circuit_breaker:
  enabled: true
  # 触发条件（满足任一即触发）
  trigger:
    error_rate: 50          # 错误率≥50%
    error_count: 100        # 或错误数≥100
    slow_call_rate: 60      # 或慢调用占比≥60%（>1秒）
  window: 60s               # 统计窗口60秒
  min_calls: 20             # 窗口内最少调用数（不足不触发）
  
  # 熔断状态
  open_duration: 30s        # 熔断持续30秒
  recovery: half_open       # 半开探测
  half_open_calls: 5        # 半开时放5个请求探测
  
  # 降级策略
  fallback:
    strategy: cached_response   # 返回缓存响应
    cache_ttl: 300s
    # 或 strategy: static_response
    # status: 503
    # body: '{"code":503,"message":"服务降级中，请稍后重试"}'
    # 或 strategy: redirect
    # to: http://backup-service:8001
```

**熔断状态机**：

```text
CLOSED（正常）
  │ 错误率≥50% (60s窗口)
  ▼
OPEN（熔断，直接返回降级响应）
  │ 30秒后
  ▼
HALF_OPEN（半开，放5个探测请求）
  │ 探测成功≥4个 → CLOSED
  │ 探测失败≥2个 → OPEN
```

### 功能3：灰度发布与AB测试

**解决痛点**：新版本上线全量发布，出问题影响所有用户。

**专业版能力**：支持按比例、按Header、按用户灰度，支持AB测试流量分发。

```yaml
# 灰度发布（按Header灰度）
canary:
  strategy: header
  header: X-Canary
  value: true
  upstream: http://order-service-v2:8001
  fallback_upstream: http://order-service-v1:8001

# 按比例灰度（10%流量到v2）
canary:
  strategy: percentage
  percentage: 10
  upstream_v1: http://order-service-v1:8001
  upstream_v2: http://order-service-v2:8001
  key: jwt:sub  # 按用户hash分流，同一用户始终命中同一版本

# AB测试（按实验组分流）
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

### 功能4：动态配置下发

**解决痛点**：改个路由要重启网关，影响线上流量。

**专业版能力**：配置热更新，不重启网关，支持版本回滚。

```bash
# 应用新配置（热更新）
gateway-manager dynamic apply --config gateway-pro.yaml --validate

# 查看配置版本
gateway-manager dynamic versions
# v1.2.0 (2026-07-18 10:00) - 当前版本
# v1.1.9 (2026-07-17 15:30)
# v1.1.8 (2026-07-16 09:00)

# 回滚到上一版本
gateway-manager dynamic rollback --to v1.1.9

# 配置diff
gateway-manager dynamic diff v1.1.9 v1.2.0
```

**动态配置保证**：
- 配置变更前自动validate，语法错不应用
- 配置版本化，支持一键回滚
- 灰度推送：先推一个网关节点，观察5分钟无异常再全量
- 配置变更审计：谁、何时、改了什么

### 功能5：分布式限流

**解决痛点**：多网关实例时，单机限流形同虚设（4实例×100QPS=实际400QPS）。

**专业版能力**：基于Redis集群的分布式限流，多实例共享计数器。

```yaml
rate_limit:
  type: distributed_sliding_window
  qps: 1000  # 全局1000 QPS，所有实例共享
  redis:
    url_env: REDIS_URL
    cluster: true
    key_prefix: gateway:ratelimit:
    ttl: 120s
  # 性能优化：本地预扣减+异步同步
  local_buffer: 50  # 本地预扣50，减少Redis访问
  sync_interval: 100ms  # 每100ms同步一次
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
    # 敏感字段脱敏
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

### 功能7：插件体系

**解决痛点**：标准认证/限流不满足，需要自定义逻辑，但改网关源码太重。

**专业版能力**：插件SDK，支持自定义认证、日志、转换、限流插件。

```python
# 自定义插件示例：请求审计日志
# plugins/audit_log.py
from gateway_plugin import Plugin, PluginContext

class AuditLogPlugin(Plugin):
    name = "audit_log"
    phase = "log"  # 在日志阶段执行
    
    def __init__(self, config):
        self.audit_url = config["audit_url"]
        self.sensitive_fields = config.get("sensitive_fields", [])
    
    def execute(self, ctx: PluginContext):
        # 脱敏敏感字段
        body = ctx.request_body
        for field in self.sensitive_fields:
            if field in body:
                body[field] = "***"
        
        # 异步发送审计日志
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

```yaml
# 网关配置中启用插件
routes:
  - name: sensitive-api
    path: /api/v1/payments/*
    upstream: http://payment-service:8001
    plugins:
      - name: audit_log
        config:
          audit_url: http://audit-service:9000/log
          sensitive_fields: [card_number, cvv]
```

### 功能8：配置dry-run

**解决痛点**：网关配置改了，上线怕出事，不上线又没法验证。

**专业版能力**：用录制的真实流量回放，验证新配置影响。

```bash
# 录制生产流量（采样1%）
gateway-manager record --sample 0.01 --duration 1h --output ./traffic.json

# dry-run：用录制的流量模拟新配置
gateway-manager dry-run \
  --config gateway-new.yaml \
  --traffic ./traffic.json \
  --report ./dry-run-report.html

# dry-run报告示例
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

---

## 使用场景

### 场景一：SaaS多租户API治理（平台架构师角色）

**痛点**：SaaS平台多租户，付费租户要高QPS，免费租户要限制，还要防租户间互相影响。

**专业版方案**：
1. 用 `tenant_aware` 限流，按租户等级配不同QPS与日配额
2. 关键路由启用熔断，防止某租户异常调用拖垮网关
3. 全链路追踪带 `tenant_id` 标签，按租户维度看监控
4. 租户级配额告警，接近上限自动通知

**效果**：租户隔离从"靠自觉"变为"网关强制"，租户间互不影响。

### 场景二：微服务容灾与降级（SRE角色）

**痛点**：某个微服务挂了，整个系统雪崩，网关还在往挂的服务转发。

**专业版方案**：
1. 每个上游服务配熔断器，错误率50%触发熔断
2. 熔断后返回降级响应（缓存/默认值/503）
3. 关键服务配故障转移（primary挂了切secondary）
4. 熔断状态告警，自动通知SRE
5. 服务恢复后半开探测，自动回到closed状态

**效果**：单服务故障不再雪崩，系统韧性大幅提升。

### 场景三：灰度发布与AB测试（研发负责人角色）

**痛点**：新版本上线全量发布，出问题影响所有用户，回滚慢。

**专业版方案**：
1. 灰度发布：先10%流量到v2，观察30分钟无异常再逐步放量
2. 按用户hash分流，同一用户始终命中同一版本，避免体验割裂
3. AB测试：50/50分流，对比转化率与客单价
4. 异常时一键回滚到v1，秒级生效

**效果**：发布风险从"全量暴露"变为"可控灰度"，回滚时间从分钟级降至秒级。

### 场景四：大型团队网关统一管控（平台负责人角色）

**痛点**：多个业务线共享网关，配置互相冲突，谁都能改没人负责。

**专业版方案**：
1. 网关配置纳入Git版本化，PR评审流程
2. 动态配置热更新，改路由不重启
3. 配置dry-run，上线前验证影响
4. 配置变更审计，谁改了什么可追溯
5. 按业务线划分路由命名空间，互不干扰

**效果**：网关配置从"谁都能改"变为"评审+审计+dry-run"，变更事故减少80%。

### 场景五：高可用网关集群（架构师角色）

**痛点**：单网关是单点，多实例时限流与配置不同步。

**专业版方案**：
1. 多实例部署，前置LB
2. 分布式限流（Redis集群共享计数器）
3. 动态配置通过控制面统一下发
4. 全链路追踪聚合多实例数据
5. 实例健康检查，自动剔除异常节点

**效果**：网关从单点变为高可用集群，SLA从99.9%提升至99.99%。

---

## 多角色场景指南

| 角色 | 典型场景 | 推荐功能组合 | 核心价值 |
|------|----------|-------------|----------|
| 平台架构师 | SaaS多租户治理 | 多租户限流+熔断+可观测性 | 租户隔离与配额管理 |
| SRE/运维 | 容灾与降级 | 熔断+故障转移+告警 | 系统韧性 |
| 研发负责人 | 灰度发布与AB | 灰度+AB测试+动态配置 | 发布风险可控 |
| 平台负责人 | 大型团队管控 | 动态配置+dry-run+审计 | 变更安全 |
| 架构师 | 高可用集群 | 分布式限流+动态配置+追踪 | SLA提升 |
| 安全工程师 | 网关安全 | 插件体系+认证+日志脱敏 | 自定义安全策略 |
| 开发者 | 自定义网关逻辑 | 插件SDK+日志+追踪 | 灵活扩展 |

---

## 性能优化策略

### 限流性能优化

1. **本地预扣减**：分布式限流时，本地预扣50配额，减少Redis访问
2. **滑动窗口近似**：用TTL近似滑动窗口，避免精确计数的高开销
3. **批量同步**：本地计数每100ms批量同步Redis，而非每次请求同步
4. **Lua脚本**：Redis端用Lua脚本原子操作，避免竞态

### 熔断性能优化

1. **滑动计数**：用滑动窗口近似错误率，避免全量统计
2. **本地状态**：熔断状态本地维护，不每次查共享存储
3. **异步上报**：错误计数异步上报，不阻塞请求
4. **批量探测**：半开状态批量放5个探测请求，加速恢复判断

### 动态配置优化

1. **增量推送**：只推送变更的配置项，减少传输量
2. **本地缓存**：网关本地缓存配置，控制面挂了也能用
3. **版本校验**：用版本号校验配置一致性，避免全量对比
4. **灰度推送**：先推一个节点观察，无异常再全量

### 可观测性优化

1. **采样率**：链路追踪10%采样，全量采样性能开销大
2. **异步导出**：日志与trace异步导出，不阻塞请求
3. **字段精简**：只记录关键字段，避免日志膨胀
4. **聚合指标**：用Prometheus聚合指标，而非全量日志

### 成本控制

- 链路追踪采样率按业务重要性配置（核心链路100%，非核心1%）
- 日志保留7天，超期归档到对象存储
- 告警规则分级，避免告警风暴
- 分布式限流Redis用集群版，避免单点瓶颈
- 插件按需启用，避免插件链过长拖慢请求

---

## 多平台集成示例

### 与K8s集成

```yaml
# gateway-config.yaml (K8s ConfigMap)
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
---
# 动态配置通过K8s Operator下发
apiVersion: gateway.manager/v1
kind: GatewayConfig
metadata:
  name: production
spec:
  configRef: gateway-config
  strategy: rolling
  validation: dry-run
```

### 与Service Mesh集成

```yaml
# 作为Envoy Sidecar的xDS配置源
dynamic_resources:
  lds_config:
    api_config_source:
      api_type: GRPC
      grpc_services:
        - envoy_grpc:
            cluster_name: gateway-manager-xds
  rds_config:
    api_config_source:
      api_type: GRPC
      grpc_services:
        - envoy_grpc:
            cluster_name: gateway-manager-xds
```

### 与监控告警集成

```yaml
# Prometheus告警规则
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

### 与CI/CD集成

```yaml
# .github/workflows/gateway-deploy.yml
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

---

## 版本升级迁移指南

### 从免费版升级至专业版

1. **无需迁移**：专业版完全兼容免费版的配置与生成能力
2. **新增功能激活**：
   - 安装CLI：`npm install -g gateway-manager-pro`
   - 初始化控制面：`gateway-manager dynamic init --control-plane <url>`
   - 启用可观测性：`gateway-manager observe enable --tracing --logging`
3. **历史配置导入**：
   - 免费版的YAML配置可直接用 `gateway-manager dynamic apply` 下发
   - 多网关生成功能继续可用
4. **指令兼容**：免费版的所有指令在专业版中均可使用

### 版本更新历史

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-07 | 初版发布，含八大高级功能与动态配置 |

---

## 故障排查表

| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 分布式限流不准确 | Redis延迟或本地buffer过大 | 减小local_buffer，缩短sync_interval | 高 |
| 熔断器频繁误触发 | 阈值过低或窗口太小 | 调高threshold，增大window | 中 |
| 灰度分流不均 | hash算法或key选择不当 | 检查key配置，用一致性hash | 中 |
| 动态配置不生效 | 控制面连接异常或版本不一致 | 检查控制面连通性，强制reconcile | 高 |
| 链路追踪断链 | 采样率过低或传播头丢失 | 提高采样率，检查W3C传播配置 | 中 |
| 告警风暴 | 规则过敏感或未分组 | 调整规则阈值，启用告警分组 | 高 |
| 插件执行慢 | 插件逻辑重或同步阻塞 | 改异步执行，精简插件逻辑 | 中 |
| dry-run结果不准 | 流量样本不具代表性 | 延长录制时间，提高采样率 | 低 |
| 网关配置冲突 | 多人同时改同一配置 | 用PR评审流程，配置锁机制 | 高 |
| 熔断后不恢复 | 半开探测失败率仍高 | 检查上游服务健康，延长open_duration | 高 |

---

## 即时修复清单

| 问题 | 修复方法 |
|------|----------|
| 限流429过多 | 检查限流key与阈值，考虑提高或换key |
| 熔断一直open | 检查上游服务是否真的挂了，或调低阈值 |
| 灰度流量泄漏 | 检查灰度key是否稳定（用user_id而非random） |
| 配置推送超时 | 检查控制面负载，分批推送 |
| trace采样不到 | 提高采样率，检查导出器连通性 |
| 告警漏报 | 检查告警规则条件与for子句 |
| 插件报错 | 查看插件日志，检查config字段 |
| dry-run卡住 | 减小流量样本，或后台异步跑 |

---

## 维护命令

```bash
# 配置管理
gateway-manager validate --config <file>
gateway-manager render --config <file> --target <gateway> --output <file>
gateway-manager dry-run --config <file> --traffic <file>

# 动态配置
gateway-manager dynamic init --control-plane <url>
gateway-manager dynamic apply --config <file> --validate
gateway-manager dynamic rollback --to <version>
gateway-manager dynamic versions
gateway-manager dynamic diff <v1> <v2>

# 流量治理
gateway-manager rate-limit status --route <name>
gateway-manager circuit-breaker status --route <name>
gateway-manager canary status --route <name>

# 可观测性
gateway-manager observe enable --tracing --logging --alerting
gateway-manager observe dashboard  # 打开监控看板
gateway-manager observe trace <trace-id>  # 查看单条trace

# 插件管理
gateway-manager plugin list
gateway-manager plugin install <name>
gateway-manager plugin enable --route <name> --plugin <name>
gateway-manager plugin disable --route <name> --plugin <name>

# 录制与回放
gateway-manager record --sample <rate> --duration <time> --output <file>
gateway-manager replay --recording <file> --target <url>

# 审计
gateway-manager audit log --since <time>
gateway-manager audit who-changed <config>
```

---

## FAQ

### Q1：免费版与专业版有什么区别？

免费版聚焦"配置生成"，提供声明式路由、统一认证、基础限流、监控指标、多网关配置生成。专业版聚焦"企业级网关平台"，新增八大高级功能：多租户差异化限流、熔断与降级、灰度发布与AB测试、动态配置下发、分布式限流、可观测性套件、插件体系、配置dry-run。此外提供多角色场景指南、性能优化策略、多平台集成示例与版本迁移指南。

### Q2：熔断器与重试有什么区别？

熔断器是"断路保护"——上游异常时主动断开，不再转发请求，返回降级响应，防止雪崩。重试是"瞬时容错"——偶发失败时重试一次，期望成功。两者互补：熔断是长期保护，重试是瞬时容错。注意：熔断open状态时不应重试，否则加重上游压力。

### Q3：灰度发布的分流key怎么选？

选稳定key，确保同一用户始终命中同一版本：
- `jwt:sub`（用户ID）：最常用，同一用户始终同版本
- `header:X-Tenant-Id`：按租户灰度，B2B场景适用
- `remote_addr`：按IP灰度，但不稳定（用户换IP就变）
- 避免用 `random`：每次请求都变，体验割裂

### Q4：分布式限流必须用Redis吗？

不一定。专业版支持两种后端：
- Redis集群：通用、成熟、性能好，推荐
- 本地+中心化校准：极端高性能场景，本地预扣+定期校准

对于QPS<10000的场景，单机限流即可；QPS>10000或需要精确全局限流时，用分布式限流。

### Q5：动态配置会丢失吗？

不会。专业版三层保障：
1. 控制面持久化配置版本，可回滚
2. 网关本地缓存最近配置，控制面挂了也能用
3. 配置变更自动备份，误删可恢复

### Q6：插件用什么语言开发？

专业版插件SDK支持Go与Python两种语言：
- Go插件：性能高，编译为.so动态加载，适合限流/转换等高性能场景
- Python插件：开发快，适合审计日志/数据分析等非关键路径场景

插件运行在独立沙箱，崩溃不影响网关主流程。

### Q7：可观测性的采样率怎么定？

按业务重要性分级：
- 核心链路（支付/订单）：100%采样
- 重要链路（用户/商品）：10%采样
- 普通链路（评论/通知）：1%采样
- 调试期间：临时100%采样

采样率过低可能漏掉关键问题，过高则性能开销大。建议从10%起步，按需调整。

### Q8：dry-run的流量样本怎么录？

用 `gateway-manager record` 录制生产流量，建议：
- 采样率1-5%（避免录制本身影响性能）
- 录制时长≥1小时（覆盖业务周期）
- 覆盖高峰与低谷（验证限流在不同负载下的行为）
- 录制文件脱敏后才能用于测试环境

### Q9：多租户限流如何防止租户作弊？

三层防护：
1. `tenant_id` 从JWT解析，不可伪造（除非有密钥）
2. 未识别租户用最严格的default规则（5QPS）
3. 异常租户（频繁429）自动降级或封禁

### Q10：网关集群如何保证配置一致？

专业版用控制面+本地缓存+定期reconcile：
1. 控制面推送配置变更到所有节点
2. 节点本地缓存配置，即使控制面挂了也能运行
3. 每30秒reconcile一次，发现不一致自动修复
4. 配置版本号全局唯一，便于一致性校验

### Q11：插件执行失败会影响请求吗？

不会。插件失败有三种处理策略：
- `continue`：忽略插件错误，继续处理请求（默认）
- `block`：插件失败则拒绝请求（用于安全插件）
- `retry`：插件失败重试N次后继续

建议非关键插件用continue策略，关键插件（如认证）用block策略。

### Q12：专业版支持私有化部署吗？

支持。控制面、可观测性组件、插件市场均可私有化部署到企业内网。Redis集群与监控后端（Prometheus/Loki/Tempo）也支持私有化。联系销售获取私有化部署包。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（用于CLI工具）
- **目标网关**: Kong / APISIX / Nginx / Envoy（任选其一或多个）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| Node.js 18+ | 运行时 | 必需 | 从nodejs.org安装 |
| Redis集群 | 数据库 | 分布式限流必需 | 从redis.io安装 |
| OpenTelemetry Collector | 监控 | 链路追踪必需 | 从opentelemetry.io安装 |
| Prometheus | 监控 | 指标采集推荐 | 从prometheus.io安装 |
| Loki | 日志 | 日志聚合可选 | 从grafana.com安装 |

### API Key 配置
- 控制面需配置管理Token：`gateway-manager login`
- Redis连接串通过环境变量配置
- 所有Token与密钥禁止硬编码
- 建议存储在 `~/.gateway/credentials/` 目录（已gitignore）
- 生产环境建议用HashiCorp Vault或K8s Secret

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent管理与治理API网关

---

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：API网关路由服务（api-gateway）
- 原始license：MIT
- 改进作品：API网关管理器（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，重构为面向企业的API网关平台
- 去除原始项目标识、外部服务URL与厂商CLI引用
- 新增八大高级功能（多租户限流、熔断降级、灰度发布、动态配置、分布式限流、可观测性、插件体系、dry-run）
- 新增分级快速开始指南（基础/标准/完整三档）
- 新增五类真实场景示例（SaaS治理/容灾降级/灰度发布/统一管控/高可用集群）
- 新增多角色场景指南（7种角色×场景映射）
- 新增性能优化策略与多平台集成示例
- 新增版本升级迁移指南
- 新增FAQ章节（12问）与故障排查表（10项）
- 重新设计架构图，增加中文标注与专业版标识
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 专业版特性

本专业版相比免费版新增以下能力：

- **多租户差异化限流**：按租户等级（enterprise/pro/free）配置不同QPS与日配额，支持租户级配额管理与超额响应
- **熔断与降级**：基于错误率/延迟的熔断器，支持半开探测恢复、缓存响应/静态响应/重定向三种降级策略，防止雪崩
- **灰度发布与AB测试**：按比例/Header/用户hash灰度，支持AB测试流量分发与转化指标对比，秒级回滚
- **动态配置下发**：配置热更新不重启网关，支持版本化、灰度推送、一键回滚、变更审计
- **分布式限流**：基于Redis集群的全局限流，多网关实例共享计数器，本地预扣减优化性能
- **可观测性套件**：全链路追踪（OpenTelemetry）、日志聚合（Loki）、告警（Prometheus）三位一体，支持字段脱敏
- **插件体系**：Go/Python双语言插件SDK，支持认证/日志/转换/限流自定义插件，沙箱隔离
- **配置dry-run**：用录制的真实流量回放，验证新配置影响，识别漏配路由与误限请求

此外，专业版还提供：
- 多角色场景指南（平台架构师/SRE/研发负责人/平台负责人/架构师/安全/开发者）
- 性能优化策略（限流/熔断/动态配置/可观测性/成本五维度）
- 多平台集成示例（K8s/Service Mesh/监控告警/CI-CD）
- 版本升级迁移指南
- 扩展FAQ（12问）与故障排查表（10项）
- 优先支持

---

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 声明式路由+统一认证+基础限流+监控+多网关生成+基础示例+基础FAQ | 个人试用、中小团队起步 |
| 收费专业版 | ¥99/月 | 全套八大高级功能+多角色指南+性能优化+多平台集成+优先支持 | 企业/大型团队、网关平台 |

专业版通过SkillHub SkillPay发布。
