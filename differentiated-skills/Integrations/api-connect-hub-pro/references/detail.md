# 详细参考 - api-connect-hub-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
monitor:
  metrics:
    - name: connection_health
      type: gauge
      description: 连接器健康状态（1=健康 0=异常）
      labels: [connector, tenant]

    - name: call_success_rate
      type: gauge
      description: 调用成功率
      labels: [connector, endpoint]
      alert:
        condition: '< 95%'
        window: 5m
        severity: critical

    - name: call_latency_p95
      type: gauge
      description: P95延迟
      labels: [connector, endpoint]
      alert:
        condition: '> 2000ms'
        window: 5m
        severity: warning

    - name: rate_limit_remaining
      type: gauge
      description: 速率限制剩余
      labels: [connector]
      alert:
        condition: '< 100'
        window: 1m
        severity: warning

  alerts:
    - name: connection_down
      condition: connection_health == 0
      for: 1m
      severity: critical
      notify: [slack, pagerduty]

    - name: quota_exhausted
      condition: rate_limit_remaining < 10
      for: 5m
      severity: critical
      notify: [slack, email]

  dashboard:
    refresh: 30s
    panels:
      - title: 连接器健康度
        type: status_map
        query: connection_health
      - title: 调用成功率
        type: time_series
        query: call_success_rate
      - title: P95延迟
        type: time_series
        query: call_latency_p95
      - title: 配额使用
        type: gauge
        query: rate_limit_remaining
```

## 代码示例 (yaml)

```yaml
name: PR提交通知工作流
trigger:
  type: webhook
  source: github
  event: pull_request.opened
steps:
  - name: 获取PR详情
    call: github.get_pr
    params:
      owner: '{{ trigger.payload.repository.owner.login }}'
      repo: '{{ trigger.payload.repository.name }}'
      pr_number: '{{ trigger.payload.number }}'
    output: pr_detail

  - name: 查询PR作者信息
    call: github.get_user
    params:
      username: '{{ pr_detail.user.login }}'
    output: author_info

  - name: 并行通知
    parallel:
      - name: 发送Slack通知
        call: slack.post_message
        params:
          channel: '#dev-pr'
          text: '新PR: {{ pr_detail.title }} by {{ author_info.name }}'
      - name: 创建Notion记录
        call: notion.create_page
        params:
          parent: '{database_id}'
          properties:
            title: '{{ pr_detail.title }}'
            author: '{{ author_info.name }}'
            url: '{{ pr_detail.html_url }}'
    on_error: continue  # 单个通知失败不影响整体
  - name: 更新PR标签
    call: github.add_label
    params:
      owner: '{{ trigger.payload.repository.owner.login }}'
      repo: '{{ trigger.payload.repository.name }}'
      pr_number: '{{ trigger.payload.number }}'
      labels: ['notified']
    on_error: abort  # 这步失败则整体失败
```

## 代码示例 (python)

```python
import time
import requests

class OAuth2TokenManager:
    def __init__(self, config):
        self.token_url = config['token_url']
        self.client_id = config['client_id']
        self.client_secret = config['client_secret']  # 从密钥管理读取
        self.refresh_token = config['refresh_token']
        self._access_token = None
        self._expires_at = 0

    def get_token(self):
        """获取有效token，过期自动刷新"""
        if self._access_token and time.time() < self._expires_at - 60:
            return self._access_token

        return self._refresh()

    def _refresh(self):
        """用refresh_token换取新access_token"""
        response = requests.post(self.token_url, data={
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
        })
        if response.status_code != 200:
            raise RuntimeError(f"Token刷新失败: {response.text}")

        data = response.json()
        self._access_token = data['access_token']
        self._expires_at = time.time() + data.get('expires_in', 3600)

        if 'refresh_token' in data:
            self.refresh_token = data['refresh_token']
            self._save_refresh_token(data['refresh_token'])

        return self._access_token

    def _save_refresh_token(self, token):
        """持久化refresh_token到密钥管理"""
        pass
```

## 代码示例 (yaml)

```yaml
webhooks:
  - name: GitHub Webhook
    path: /webhooks/github
    source: github
    secret_env: GITHUB_WEBHOOK_SECRET
    verify:
      algorithm: hmac-sha256
      header: X-Hub-Signature-256
      prefix: sha256=
    events:
      - pull_request.opened
      - push
      - issues.opened
    route_to: workflows.notify-on-pr  # 路由到工作流
    dedup:
      enabled: true
      header: X-GitHub-Delivery
      ttl: 24h
    retry:
      on_failure: true
      max: 5
      backoff: exponential

  - name: Stripe Webhook
    path: /webhooks/stripe
    source: stripe
    secret_env: STRIPE_WEBHOOK_SECRET
    verify:
      algorithm: hmac-sha256
      header: Stripe-Signature
    events:
      - charge.succeeded
      - charge.failed
      - invoice.paid
    route_to: workflows.process-payment
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│             API连接中心专业版 (CONNECT HUB PRO)                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  连接层      │  │  编排层      │  │  数据层      │              │
│  │  CONNECT    │  │  ORCHESTRA  │  │  DATA       │              │
│  │             │  │             │  │             │              │
│  │ 连接器注册  │  │ 调用链编排  │  │ 数据同步    │              │
│  │ 凭证管理    │  │ 条件分支    │  │ 字段映射    │              │
│  │ OAuth2刷新  │  │ 并行调用    │  │ 增量同步    │              │
│  │ 错误重试    │  │ 批量调用    │  │ 数据转换    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  事件层      │  ← Webhook驱动                 │
│                  │  EVENT      │    ✅ 专业版                    │
│                  │  Webhook接收│                                 │
│                  │  验签重放   │                                 │
│                  │  事件路由   │                                 │
│                  └─────────────┘                                 │
│                          │                                       │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  治理层      │  ← 监控与多租户                 │
│                  │  GOVERN     │    ✅ 专业版                    │
│                  │  监控告警   │                                 │
│                  │  多租户隔离 │                                 │
│                  │  连接器市场 │                                 │
│                  └─────────────┘                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (bash)

```bash
api-connect connector list
api-connect connector register --file <yaml>
api-connect connector test --name <name>

api-connect workflow list
api-connect workflow run --name <name> --input <json>
api-connect workflow status <run-id>
api-connect workflow rollback --name <name> --to <version>

api-connect sync list
api-connect sync create --config <yaml>
api-connect sync run --name <name> --mode manual
api-connect sync status --name <name>

api-connect webhook start --port <port>
api-connect webhook list
api-connect webhook replay --event-id <id>

api-connect oauth refresh --connector <name>
api-connect oauth status --connector <name>

api-connect monitor dashboard  # 打开看板
api-connect monitor alert list
api-connect monitor metric <name>

api-connect tenant list
api-connect tenant quota --id <tenant_id>
api-connect tenant rotate-key --id <tenant_id>

api-connect market search --service <name>
api-connect market install <name>
api-connect market publish <file>

api-connect batch --calls <json> --mode parallel --aggregate merge
```

## 代码示例 (yaml)

```yaml
workflows:
  - name: 订单处理流程
    steps:
      - name: 创建订单
        call: stripe.create_charge
        params:
          amount: '{{ input.amount }}'
          currency: 'cny'
          source: '{{ input.card_token }}'
        output: charge_result
        retry: { max: 3, backoff: exponential }

      - name: 条件分支
        if: '{{ charge_result.status == "succeeded" }}'
        then:
          - name: 扣库存
            call: internal.deduct_stock
            params:
              sku: '{{ input.sku }}'
              qty: '{{ input.qty }}'
          - name: 发通知
            parallel:
              - call: slack.post_message
                params: { channel: '#orders', text: '新订单 {{ input.order_id }}' }
              - call: sendgrid.send_email
                params: { to: '{{ input.customer_email }}', template: 'order_confirmed' }
        else:
          - name: 退款
            call: stripe.refund_charge
            params: { charge_id: '{{ charge_result.id }}' }
          - name: 通知失败
            call: slack.post_message
            params: { channel: '#alerts', text: '订单 {{ input.order_id }} 支付失败' }
```

## 代码示例 (yaml)

```yaml
sync:
  name: HubSpot到Salesforce联系人同步
  source:
    connector: hubspot
    endpoint: list_contacts
    key_field: id
    updated_field: lastmodifieddate
  target:
    connector: salesforce
    endpoint: upsert_contact
    key_field: HubSpot_Id__c
    external_id: HubSpot_Id__c
  schedule: "*/30 * * * *"  # 每30分钟
  mode: incremental  # 增量同步
  mapping:
    - source: firstname
      target: FirstName
    - source: lastname
      target: LastName
    - source: email
      target: Email
      transform: lowercase  # 转换函数
    - source: phone
      target: Phone
      transform: format_phone
    - source: createdate
      target: Created_Date__c
      transform: timestamp_to_date
  conflict_resolution: source_wins  # 冲突时源端为准
  batch_size: 200  # 每批200条
  on_error: continue  # 单条失败不中断
  webhook: https://api.example.com/sync-callback  # 同步完成回调
```

## 代码示例 (yaml)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: connect-hub-webhook
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: webhook
          image: registry.example.com/connect-hub:1.0
          ports: [{containerPort: 9000}]
          env:
            - name: GITHUB_WEBHOOK_SECRET
              valueFrom:
                secretKeyRef:
                  name: webhook-secrets
                  key: github
```

## 代码示例 (python)

```python
result = api_connect.batch(
    calls=[
        {'connector': 'github', 'endpoint': 'get_user', 'params': {'username': 'alice'}},
        {'connector': 'slack', 'endpoint': 'get_user_info', 'params': {'user': 'U123'}},
        {'connector': 'notion', 'endpoint': 'get_user', 'params': {'user_id': 'abc'}},
    ],
    mode='parallel',  # 并行调用
    timeout=10,
    aggregate='merge',  # 结果合并
)

{
    "github": {"login": "alice", "name": "Alice Wang", "followers": 120},
    "slack": {"name": "Alice", "email": "alice@company.com", "title": "Engineer"},
    "notion": {"name": "Alice Wang", "avatar": "https://..."},
    "_meta": {"success": 3, "failed": 0, "duration_ms": 850}
}
```

## 代码示例 (bash)

```bash
api-connect sync create \
  --name github-issues-to-jira \
  --source github \
  --target jira \
  --mapping ./mappings/github-jira.json \
  --schedule "*/30 * * * *" \
  --mode incremental

api-connect webhook start --port 9000 --routes ./webhooks/

api-connect monitor enable \
  --metrics prometheus \
  --alerting slack \
  --dashboard grafana
```

### 功能5：监控告警
**解决痛点**：集成出问题不知道，等用户投诉才发现某API挂了或配额用完了。

**专业版能力**：连接健康度、调用成功率、延迟、配额四维监控。

```yaml
monitor:
  metrics:
    - name: connection_health
      type: gauge
      description: 连接器健康状态（1=健康 0=异常）
      labels: [connector, tenant]

    - name: call_success_rate
      type: gauge
      description: 调用成功率
      labels: [connector, endpoint]
      alert:
        condition: '< 95%'
        window: 5m
        severity: critical

    - name: call_latency_p95
      type: gauge
      description: P95延迟
      labels: [connector, endpoint]
      alert:
        condition: '> 2000ms'
        window: 5m
        severity: warning

    - name: rate_limit_remaining
      type: gauge
      description: 速率限制剩余
      labels: [connector]
      alert:
        condition: '< 100'
        window: 1m
        severity: warning

  alerts:
    - name: connection_down
      condition: connection_health == 0
      for: 1m
      severity: critical
      notify: [slack, pagerduty]

    - name: quota_exhausted
      condition: rate_limit_remaining < 10
      for: 5m
      severity: critical
      notify: [slack, email]

  dashboard:
    refresh: 30s
    panels:
      - title: 连接器健康度
        type: status_map
        query: connection_health
      - title: 调用成功率
        type: time_series
        query: call_success_rate
      - title: P95延迟
        type: time_series
        query: call_latency_p95
      - title: 配额使用
        type: gauge
        query: rate_limit_remaining
```



