# 详细参考 - universal-proxy-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
deployment:
  mode: enterprise_ha
  nodes: 5
  database:
    backend: postgresql
    cluster: pg-cluster.internal
    ha: true
    replicas: 3

circuits:
  pool_size: 20
  regions: [us-east, us-west, eu-west, eu-central, ap-singapore, ap-tokyo]
  hops: 3
  auto_rotate: 1000

load_balancer:
  strategy: region_affinity
  fallback: round_robin

routing:
  region_rules:
    - match: "*.us-restricted.com"
      region: us-east
    - match: "*.eu-restricted.com"
      region: eu-west

nodes:
  self_hosted:
    - id: node-hq
      endpoint: relay-hq.company.com:9001
      auth: mtls
    - id: node-bj
      endpoint: relay-bj.company.com:9001
      auth: mtls
  routing:
    sensitive: self_hosted
    general: public_pool

audit:
  enabled: true
  standards: [SOX, 等保2.0]
  retention: 2555
  immutable: true
  siem_integration:
    platform: splunk
    endpoint: https://siem.company.com/api/logs

monitoring:
  metrics: [rps, circuit_health, latency_p99, bandwidth, error_rate]
  alerts:
    - circuit_unhealthy
    - bandwidth_spike
    - region_unavailable
```

## 代码示例 (python)

```python
from universal_proxy_pro import ProxyClient

client = ProxyClient(
    mode='enterprise',
    db_url='postgresql://user:pass@db:5432/proxy'
)

await client.start_cluster(
    circuits=10,
    regions=['us-east', 'eu-west', 'ap-singapore']
)

async def fetch_regional(url, region):
    response = await client.request(
        url=url,
        region=region,
        timeout=30
    )
    return response

import asyncio
tasks = [
    fetch_regional('https://us-service.com', 'us-east'),
    fetch_regional('https://eu-service.com', 'eu-west'),
    fetch_regional('https://apac-service.com', 'ap-singapore')
]
results = await asyncio.gather(*tasks)
```

## 代码示例 (yaml)

```yaml
nodes:
  self_hosted:
    - id: node-hq
      endpoint: relay-hq.company.com:9001
      auth: mtls
      cert: /etc/ssl/relay.crt
      key: /etc/ssl/relay.key
      ca: /etc/ssl/ca.crt
      capacity: 100  # 最大并发连接
    - id: node-bj
      endpoint: relay-bj.company.com:9001
      auth: mtls
      cert: /etc/ssl/relay.crt
      key: /etc/ssl/relay.key
      capacity: 100

    - id: node-sh
      endpoint: relay-sh.company.com:9001
      auth: mtls
      cert: /etc/ssl/relay.crt
      key: /etc/ssl/relay.key
      capacity: 100

  private_circuits:
    - id: circuit-private-1
      hops: [node-hq, node-bj, node-sh]
      use: sensitive_traffic
```

## 代码示例 (yaml)

```yaml
load_balancer:
  strategy: region_affinity
  fallback: least_connections

  circuits:
    - id: circuit-us-east-1
      region: us-east
      weight: 30
    - id: circuit-us-east-2
      region: us-east
      weight: 30
    - id: circuit-us-west
      region: us-west
      weight: 20
    - id: circuit-eu-west
      region: eu-west
      weight: 20

  health_check:
    interval: 30s
    timeout: 5s
    failure_threshold: 3
    auto_replace: true
```

## 代码示例 (yaml)

```yaml
nodes:
  self_hosted:
    - id: node-hq
      endpoint: relay-hq.company.com:9001
      auth: mtls
      cert: /etc/ssl/relay.crt
      key: /etc/ssl/relay.key

    - id: node-bj
      endpoint: relay-bj.company.com:9001
      auth: mtls
      cert: /etc/ssl/relay.crt
      key: /etc/ssl/relay.key

  public_pool:
    - use_default_circuits: true

  routing:
    sensitive: self_hosted  # 敏感流量走自建节点
    general: public_pool    # 一般流量走公共节点
```

## 代码示例 (yaml)

```yaml
monitoring:
  metrics:
    - requests_per_second
    - circuit_health
    - latency_p99
    - bandwidth_usage
    - error_rate

  alerts:
    - name: circuit_unhealthy
      condition: error_rate > 5%
      action: rotate_circuit

    - name: bandwidth_spike
      condition: bandwidth > 100Mbps
      action: alert_admin

    - name: region_unavailable
      condition: region_error_rate > 10%
      action: failover_to_alternate
```

## 代码示例 (bash)

```bash
universal-proxy init --mode enterprise \
  --db postgresql://user:pass@db:5432/proxy \
  --circuits 10 \
  --regions us-east,eu-west,ap-singapore

universal-proxy serve --port 9050 --workers 4

universal-proxy node add \
  --id node-hq \
  --endpoint relay-hq.company.com:9001 \
  --auth mtls

universal-proxy route configure \
  --rule "*.us-only.com:us-east" \
  --rule "*.eu-only.com:eu-west"

universal-proxy audit enable \
  --standards SOX,等保2.0 \
  --retention 2555
```

## 代码示例 (yaml)

```yaml
circuits:
  pool:
    - id: circuit-us-east
      region: us-east
      hops: 3
      status: ready
    - id: circuit-eu-west
      region: eu-west
      hops: 3
      status: ready
    - id: circuit-apac
      region: ap-singapore
      hops: 3
      status: ready

  max_concurrent: 20
  auto_rotate: 1000  # 每1000请求自动轮换
```

