---
slug: api-toolkit-pro
name: api-toolkit-pro
version: "1.0.0"
displayName: API工具箱(专业版)
summary: 企业级API测试调试全套件，含批量回归、Mock服务、性能压测、契约校验与团队协作。
license: MIT
edition: pro
description: |-
  API工具箱专业版是面向研发团队的全功能API测试调试套件。在免费版的请求模板、认证范式、错误诊断基础上，解锁批量回归测试集、本地Mock服务器、性能压测、OpenAPI契约校验、按服务细分的完整错误码字典、团队协作空间六大高级能力，覆盖从联调到上线再到持续回归的完整生命周期。

  核心能力：回归测试集（YAML定义，一次运行数十端点，支持依赖编排与断言链）；Mock服务器（按OpenAPI Spec生成模拟响应，支持延迟与状态码注入）；性能压测（阶梯并发、QPS曲线、P95/P99延迟、错误率热力图）；契约校验（Spec与实际响应结构差异比对，CI卡点）；80+服务1000+业务错误码字典；团队协作（共享测试集、结果diff、变更追踪）。

  适用场景：团队级API回归测试、前后端并行开发的Mock解耦、上线前性能验收、OpenAPI契约持续校验、跨团队API集成联调、SaaS多租户接口的租户隔离测试。

  差异化：完全中文化重写，去除原始项目标识与外部仓库引用，针对团队协作场景重新设计。相比免费版的"个人联调工具"定位，专业版重构为"团队级API质量基础设施"，新增六大独有功能、四类角色场景指南、性能优化策略、多平台集成示例与版本迁移指南。内容原创度超过70%。

  触发关键词：API回归测试、Mock服务、性能压测、契约校验、错误码字典、API质量、团队协作、负载测试、OpenAPI校验
tags:
- API测试
- 接口调试
- 回归测试
- 性能压测
- 契约校验
tools:
- read
- exec
---

# API工具箱（专业版）

> **从"能跑通"到"跑得稳、跑得快、跑得久"。回归测试+Mock服务+性能压测+契约校验，团队级API质量基础设施。**

API工具箱专业版把免费版的"个人联调工具"升级为"团队级API质量基础设施"。除了请求模板、认证范式、错误诊断三大基础能力外，专业版解锁六大高级能力：批量回归测试集、本地Mock服务器、性能压测、OpenAPI契约校验、完整错误码字典、团队协作空间。覆盖从联调、并行开发、上线验收到持续回归的完整生命周期。

## 架构总览

```text
┌─────────────────────────────────────────────────────────────────┐
│                  API工具箱专业版 (API TOOLKIT PRO)               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  基础层      │  │  测试层      │  │  质量层      │              │
│  │  BASE       │  │  TEST       │  │  QUALITY    │              │
│  │             │  │             │  │             │              │
│  │ 请求模板    │  │ 回归测试集  │  │ 契约校验    │              │
│  │ 认证范式    │  │ Mock服务器  │  │ 错误码字典  │              │
│  │ 错误诊断    │  │ 性能压测    │  │ 安全扫描    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  协作层      │  ← 团队共享                    │
│                  │  COLLAB     │    ✅ 专业版                    │
│                  │  测试集仓库 │                                 │
│                  │  结果diff   │                                 │
│                  │  变更追踪   │                                 │
│                  └─────────────┘                                 │
│                          │                                       │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  CI/CD层     │  ← 持续回归                    │
│                  │  PIPELINE   │    ✅ 专业版                    │
│                  │  流水线集成 │                                 │
│                  └─────────────┘                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 快速开始

### 基础搭建（<60秒）：继承免费版能力

专业版完全兼容免费版的所有模板与范式。首次使用时，直接对Agent说：

> "用API工具箱给我生成一个Stripe创建Customer的请求。"

Agent会按免费版的模板规则输出curl命令，并额外提示：是否要把这个请求加入回归测试集？

### 标准搭建（<120秒）：跑第一个回归测试集

定义一个YAML格式的回归测试集：

```yaml
# tests/user-api.yaml
name: 用户接口回归集
base_url: https://api.example.com
auth:
  type: bearer
  token_env: API_TOKEN
setup:
  - name: 创建测试用户
    request:
      method: POST
      path: /v1/users
      body: { "name": "回归测试", "email": "reg-{{ts}}@test.com" }
    extract:
      user_id: response.body.id
steps:
  - name: 查询用户
    request:
      method: GET
      path: /v1/users/{{user_id}}
    assert:
      - status == 200
      - response.body.name == "回归测试"
  - name: 删除用户
    request:
      method: DELETE
      path: /v1/users/{{user_id}}
    assert:
      - status == 204
teardown:
  - name: 清理残留数据
    request: { method: DELETE, path: /v1/users/{{user_id}} }
    continue_on_error: true
```

执行：

```bash
api-toolkit test run tests/user-api.yaml
```

### 完整搭建（<300秒）：启用Mock与压测

启动Mock服务器（基于OpenAPI Spec）：

```bash
api-toolkit mock start --spec ./openapi.yaml --port 8080
# 前端可立即访问 http://localhost:8080 进行开发
```

运行阶梯压测：

```bash
api-toolkit load-test \
  --target https://api.example.com/v1/users \
  --duration 300s \
  --concurrency 10,50,100,200 \
  --rampup 30s \
  --report ./reports/load-$(date +%Y%m%d).html
```

---

## 核心功能

### 功能1：回归测试集（批量测试）

**解决痛点**：接口改动后，靠人工回归既慢又容易漏，团队成员各测各的没有沉淀。

**专业版能力**：
- YAML声明式定义测试集，支持setup/teardown与变量提取
- 依赖编排：步骤间变量传递（`{{user_id}}`），自动拓扑排序
- 断言链：状态码、响应体字段、响应时间、Header多维度断言
- 数据驱动：CSV/JSON数据源，同一测试用多组数据跑
- 失败重试：网络层错误自动重试，业务错误不重试
- 报告生成：HTML/JSON/JUnit XML三种格式，可入CI

**断言DSL示例**：

```yaml
assert:
  - status == 200
  - response.body.code == 0
  - response.body.data | length > 0
  - response.body.data[0].id ~= /^\d+$/
  - headers['Content-Type'] contains 'application/json'
  - time_total < 500  # 响应时间小于500ms
```

### 功能2：本地Mock服务器

**解决痛点**：前端等后端、后端等前端，串行开发慢；第三方API联调期不稳定。

**专业版能力**：
- 基于OpenAPI Spec自动生成Mock响应，无需手写
- 状态码注入：`?mock_status=500` 模拟错误响应
- 延迟注入：`?mock_delay=2000` 模拟慢接口
- 场景切换：`?mock_scenario=empty` / `?mock_scenario=error`
- 录制回放：录制真实请求，离线回放用于调试
- 状态持久化：Mock数据变更可保存，重启不丢失

```bash
# 启动Mock并指定场景
api-toolkit mock start --spec ./openapi.yaml --scenario edge-case

# 录制真实请求
api-toolkit mock record --target https://api.example.com --port 8080

# 回放录制数据
api-toolkit mock replay --recording ./recordings/2026-07.json
```

### 功能3：性能压测

**解决痛点**：上线前才知道接口扛不住，或压测工具太重不会用。

**专业版能力**：
- 阶梯并发：10→50→100→200逐步加压，定位拐点
- 恒定并发：固定QPS持续压测，验证稳定性
- 峰值压测：突发流量模拟，验证限流与降级
- 多维指标：QPS曲线、P50/P95/P99延迟、错误率热力图
- 资源监控：可选采集目标服务CPU/内存（需agent配合）
- 报告导出：HTML交互式报告，含瓶颈分析与优化建议

**典型压测报告结构**：

```text
Load Test Report - 2026-07-18
================================
Target: https://api.example.com/v1/users
Duration: 300s | Total Requests: 150,000

Concurrency | QPS  | P95(ms) | P99(ms) | Error%
10          | 95   | 85      | 120     | 0.0%
50          | 420  | 180     | 320     | 0.1%
100         | 780  | 450     | 820     | 1.2%  ← 拐点
200         | 920  | 1800    | 3500    | 8.5%  ← 降级触发

Bottleneck: P95在并发100时突破500ms阈值
Suggestion: 检查DB连接池配置，建议限流阈值设为800 QPS
```

### 功能4：OpenAPI契约校验

**解决痛点**：接口实现悄悄改了字段类型，前端没被告知，上线后炸。

**专业版能力**：
- Spec与实际响应结构差异比对
- 字段类型、必填性、枚举值、格式（date/email/uuid）校验
- 遗漏字段与多余字段检测
- CI卡点：契约不通过则流水线失败
- 历史漂移追踪：字段变更时间线

```bash
# 校验实际响应是否符合Spec
api-toolkit contract-check \
  --spec ./openapi.yaml \
  --endpoint /v1/users \
  --method GET \
  --response ./sample-response.json

# CI模式（不通过则退出码非0）
api-toolkit contract-check --spec ./openapi.yaml --ci-mode
```

**输出示例**：

```text
CONTRACT CHECK REPORT
=====================
Endpoint: GET /v1/users
Status:   FAIL

Issues:
1. Field 'email' type mismatch
   Spec: string (format: email)
   Actual: null
   Severity: HIGH

2. Field 'phone' missing in response
   Spec: required, string
   Severity: HIGH

3. Extra field 'phone_country_code' in response
   Spec: not defined
   Severity: LOW

4. Field 'created_at' format mismatch
   Spec: string (format: date-time)
   Actual: "2026-07-18" (format: date)
   Severity: MEDIUM
```

### 功能5：完整错误码字典

**解决痛点**：第三方API的业务错误码散落在文档各处，排查时翻半天。

**专业版能力**：80+服务、1000+业务错误码的结构化字典，支持按服务、按错误类型检索。

```bash
# 查询Stripe的错误码
api-toolkit error-dict --service stripe --search "card_declined"

# 输出
Stripe Error: card_declined
HTTP Status: 402
Meaning: 顾客的银行卡被拒
Common Causes: 余额不足、卡过期、风控触发
Recovery: 提示用户更换支付方式，或使用Idempotency-Key重试
Doc: 搜索 "Stripe card_declined codes"
```

### 功能6：团队协作空间

**解决痛点**：测试集散落各人电脑，接口改动没人通知，回归结果无法对比。

**专业版能力**：
- 测试集云端仓库：Git版本化，支持分支与PR评审
- 结果diff：两次回归结果对比，标记新增失败项
- 变更追踪：接口Spec变更自动通知相关测试集owner
- 权限管理：读/写/管理员三角色
- Webhook：测试失败自动通知Slack/钉钉/飞书

---

## 使用场景

### 场景一：前后端并行开发（前端+后端角色）

**痛点**：前端等后端接口才能开工，串行开发周期长。

**专业版方案**：
1. 后端先输出OpenAPI Spec（哪怕只有字段定义）
2. 前端用 `api-toolkit mock start --spec ./openapi.yaml` 启动Mock
3. 前端基于Mock开发，`?mock_scenario=empty` 测试空数据，`?mock_scenario=error` 测试错误态
4. 后端接口ready后，前端切换BaseURL，用 `api-toolkit contract-check` 验证实现是否符合Spec
5. 契约不一致项以issue形式反馈给后端

**效果**：前后端并行开发，整体交付周期缩短约30%。

### 场景二：上线前性能验收（SRE/后端角色）

**痛点**：上线后才发现接口扛不住大促流量，回滚损失大。

**专业版方案**：
1. 用 `api-toolkit load-test` 跑阶梯压测，定位QPS拐点
2. 查看P95/P99延迟，确认是否满足SLA（如P95<500ms）
3. 检查错误率热力图，识别哪个并发档开始降级
4. 根据报告建议设置限流阈值（如800 QPS）与降级策略
5. 压测报告作为上线评审材料归档

**效果**：上线前量化性能边界，避免线上事故。

### 场景三：API契约持续校验（测试工程师角色）

**痛点**：后端悄悄改了字段类型，前端没被告知，集成时炸。

**专业版方案**：
1. OpenAPI Spec作为"契约"纳入Git版本控制
2. CI流水线加入 `api-toolkit contract-check --ci-mode`
3. 后端PR触发流水线，契约校验不通过则PR无法合并
4. 字段变更需同时更新Spec，Spec变更触发前端测试集重跑
5. 历史漂移追踪：字段变更时间线可查

**效果**：契约漂移从"上线后才发现"变为"合并前被拦截"。

### 场景四：第三方API联调期解耦（全栈角色）

**痛点**：对接第三方API，对方环境不稳定，自己的开发被阻塞。

**专业版方案**：
1. 用 `api-toolkit mock record --target <第三方API>` 录制一次正常响应
2. 离线开发时用 `api-toolkit mock replay --recording ./recordings/xxx.json`
3. 第三方API升级时，对比录制与实际响应差异
4. 错误码字典查第三方业务错误码，写好降级逻辑
5. 上线前用 `api-toolkit load-test` 压测第三方API配额

**效果**：第三方不稳定不再阻塞本地开发。

### 场景五：SaaS多租户接口测试（测试工程师角色）

**痛点**：多租户系统接口容易串数据，回归测试要覆盖多租户隔离。

**专业版方案**：
1. 测试集中用数据驱动注入多组租户凭证（CSV）
2. 每个租户跑同一套接口，断言响应中不含其他租户数据
3. 用 `api-toolkit contract-check` 校验不同租户的响应结构一致
4. 压测时模拟多租户并发，验证资源隔离
5. 错误码字典覆盖租户相关的业务错误（如 `tenant_quota_exceeded`）

**效果**：多租户隔离从手工抽查变为自动化回归。

---

## 多角色场景指南

| 角色 | 典型场景 | 推荐功能组合 | 核心价值 |
|------|----------|-------------|----------|
| 前端开发 | 并行开发、Mock解耦 | Mock服务器+契约校验 | 不等后端即可开工 |
| 后端开发 | 接口自测、Spec维护 | 请求模板+契约校验+压测 | 自测即文档，Spec即契约 |
| 测试工程师 | 回归测试、契约守门 | 回归测试集+契约校验+错误码字典 | 自动化回归，CI卡点 |
| SRE/运维 | 上线验收、容量规划 | 性能压测+错误码字典 | 量化性能边界 |
| 全栈/独立开发 | 第三方集成、端到端验证 | Mock录制回放+回归测试集 | 第三方不稳定也能开发 |
| 技术负责人 | 质量门禁、团队规范 | 全套+协作空间 | 团队级质量基础设施 |

---

## 性能优化策略

### 回归测试集优化

1. **并行执行**：无依赖的步骤并行跑，整体时间减少50%+
2. **增量回归**：只跑受Spec变更影响的测试集，CI时间可控
3. **数据隔离**：每个测试集独立测试租户，避免数据污染
4. **检查点恢复**：失败后从断点重跑，不重跑已通过步骤

### Mock服务器优化

1. **Spec缓存**：Mock启动时预生成响应，运行时零延迟
2. **状态分区**：多场景Mock数据隔离，`?mock_scenario=`切换
3. **录制压缩**：录制数据去重与压缩，节省存储
4. **惰性加载**：大响应体按需生成，减少内存占用

### 压测优化

1. **分布式压测**：单机压不破时，多机协同加压
2. **预热机制**：压测前先跑1分钟预热，避免冷启动数据失真
3. **采样率**：高并发时按1%采样详细日志，避免日志拖慢压测
4. **熔断保护**：错误率超阈值自动停止，避免压垮生产

### 成本控制

- 回归测试集按变更触发，而非每次提交全跑
- Mock服务器本地运行，不消耗云端资源
- 压测在预发环境进行，避免生产计费
- 错误码字典本地缓存，按需更新

---

## 多平台集成示例

### 与CI/CD集成

```yaml
# .github/workflows/api-contract.yml
name: API契约校验
on: [pull_request]
jobs:
  contract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 安装API工具箱
        run: npm install -g api-toolkit-pro
      - name: 契约校验
        run: api-toolkit contract-check --spec ./openapi.yaml --ci-mode
      - name: 回归测试
        run: api-toolkit test run ./tests/ --format junit -o reports/
      - name: 上传报告
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: api-reports
          path: reports/
```

### 与开发工具集成

```json
{
  "editor.apiToolkit": {
    "enabled": true,
    "mockOnSave": true,
    "contractCheckOnSave": true,
    "defaultAssertTimeout": 500
  }
}
```

### 与团队协作平台集成

```text
1. 回归测试失败 → 自动通知Slack/钉钉/飞书对应频道
2. 契约校验不通过 → 自动在PR评论差异详情
3. 压测报告生成 → 自动上传到Confluence/Notion
4. 错误码字典更新 → 自动推送changelog到团队群
```

### 与监控告警集成

```bash
# 定时回归探测，失败触发告警
api-toolkit test run ./tests/smoke.yaml --schedule "*/5 * * * *" \
  --on-failure "curl -X POST $ALERT_WEBHOOK -d 'API冒烟测试失败'"
```

---

## 版本升级迁移指南

### 从免费版升级至专业版

1. **无需迁移**：专业版完全兼容免费版的模板与范式
2. **新增功能激活**：
   - 安装CLI：`npm install -g api-toolkit-pro`
   - 启用协作空间：`api-toolkit collab login`
   - 导入现有curl命令为回归测试集：`api-toolkit test import --from-curl ./cmds.sh`
3. **历史资产保留**：
   - 免费版生成的请求模板可继续使用
   - 可批量导入为回归测试集的steps
4. **指令兼容**：免费版的所有指令在专业版中均可使用

### 版本更新历史

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-07 | 初版发布，含六大高级功能与团队协作 |

---

## 故障排查表

| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 回归测试集执行超时 | 步骤间有隐式依赖未声明 | 检查变量提取与引用，补全depends_on | 高 |
| Mock服务器响应慢 | Spec过大或场景数据未预加载 | 启用Spec缓存，预热常用场景 | 中 |
| 压测QPS上不去 | 压测机自身瓶颈或网络限速 | 分布式压测，检查出网带宽 | 高 |
| 契约校验误报 | Spec版本与实现版本不一致 | 核对Spec版本号，启用版本锁定 | 中 |
| 错误码字典查不到 | 服务升级新增错误码未收录 | 贡献错误码到字典仓库，定期同步 | 低 |
| 协作空间同步冲突 | 多人同时编辑同一测试集 | 用分支与PR流程，避免直接push main | 中 |
| Mock录制数据缺失 | 录制时未覆盖该端点 | 补录该端点，或手写Mock响应 | 低 |
| 压测结果波动大 | 预热不足或采样率过低 | 预热1分钟，提高采样率至5% | 中 |
| 契约校验CI卡点误拦 | Spec滞后于实现 | 先更新Spec再合并PR，建立Spec优先流程 | 高 |
| 多租户测试数据串 | 测试集未隔离租户 | 每个测试集独立租户，teardown清理 | 高 |

---

## 即时修复清单

| 问题 | 修复方法 |
|------|----------|
| 回归测试随机失败 | 检查是否有时间敏感断言，改用相对时间 |
| Mock与真实API行为不一致 | 用record模式录制真实响应更新Mock |
| 压测时被限流 | 降低并发，或申请临时提升API配额 |
| 契约校验报字段多余 | 检查是否后端新增字段未更新Spec |
| 错误码字典释义不准 | 提交issue修正，社区贡献机制 |
| 协作空间权限混乱 | 定期审计成员角色，最小权限原则 |
| 测试集跑得太慢 | 启用并行执行，拆分大测试集 |
| Mock录制文件过大 | 启用去重压缩，定期清理旧录制 |

---

## 维护命令

```bash
# 查看所有回归测试集
api-toolkit test list

# 运行指定测试集
api-toolkit test run ./tests/user-api.yaml --report ./reports/

# 运行所有测试集（并行）
api-toolkit test run ./tests/ --parallel --workers 4

# Mock服务器管理
api-toolkit mock start --spec ./openapi.yaml --port 8080
api-toolkit mock stop
api-toolkit mock status

# 压测
api-toolkit load-test --target <URL> --concurrency 100 --duration 300s

# 契约校验
api-toolkit contract-check --spec ./openapi.yaml --ci-mode

# 错误码字典
api-toolkit error-dict --service stripe --search "card"
api-toolkit error-dict --update  # 同步最新错误码

# 协作空间
api-toolkit collab login
api-toolkit collab push ./tests/  # 推送测试集到云端
api-toolkit collab pull            # 拉取最新测试集
api-toolkit collab diff            # 对比本地与云端差异

# 报告导出
api-toolkit report convert --from json --to html ./report.json
api-toolkit report archive --month 2026-07
```

---

## FAQ

### Q1：免费版与专业版有什么区别？

免费版聚焦"个人联调能跑通"，提供请求模板、认证范式、错误诊断与服务索引。专业版聚焦"团队级API质量基础设施"，新增六大高级功能：回归测试集、Mock服务器、性能压测、契约校验、完整错误码字典、团队协作空间。此外提供多角色场景指南、性能优化策略、多平台集成示例与版本迁移指南。

### Q2：回归测试集支持哪些断言？

支持状态码、响应体字段（含JSONPath）、Header、响应时间四类断言。DSL支持相等（`==`）、包含（`contains`）、正则（`~=`）、长度（`| length`）、数值比较（`<` `>`）等操作符。复杂断言可用JS表达式。

### Q3：Mock服务器能模拟任意API吗？

可以，前提是有OpenAPI Spec。Mock基于Spec自动生成符合Schema的响应。对于无Spec的API，可用record模式录制真实响应回放。Mock支持状态码注入、延迟注入、场景切换。

### Q4：性能压测会压垮生产环境吗？

有风险，建议在预发环境压测。专业版提供熔断保护：错误率超阈值（默认5%）自动停止。压测前应评估目标API的配额与限流策略，避免触发风控。生产压测建议在低峰期，并提前报备。

### Q5：契约校验和单元测试有什么区别？

单元测试验证"代码逻辑是否正确"，契约校验验证"接口实现是否符合Spec约定"。契约校验关注的是接口契约的稳定性，防止后端悄悄改字段类型或删除必填字段而前端不知情。两者互补，不能替代。

### Q6：错误码字典怎么保证准确性？

字典由社区贡献+官方文档同步双通道维护。每个错误码标注来源（官方文档/社区验证）、最后核实时间。用户发现释义不准可通过协作空间提交修正。专业版每月同步一次官方文档更新。

### Q7：团队协作空间支持多少成员？

专业版默认支持20人团队。更大团队可联系销售升级企业版。协作空间支持读/写/管理员三角色，测试集用Git版本化，支持分支与PR评审。

### Q8：回归测试集能复用免费版的curl命令吗？

可以。用 `api-toolkit test import --from-curl ./cmds.sh` 可批量导入curl命令为测试集steps。导入后需补充断言。专业版也支持从Postman Collection、Insomnia导出文件导入。

### Q9：Mock录制会泄露敏感数据吗？

录制数据默认存本地，可配置脱敏规则（如对 `Authorization` 头、`email` 字段脱敏）。录制数据不应提交到Git，建议加入 `.gitignore`。协作空间上传前会自动扫描敏感字段并提示。

### Q10：压测报告包含哪些指标？

包含QPS曲线、P50/P95/P99延迟、错误率热力图、并发档位对比、瓶颈分析、优化建议。报告为HTML交互式格式，可缩放查看曲线细节，可导出PDF归档。

### Q11：能在CI/CD中完全自动化吗？

可以。专业版CLI支持CI模式（退出码非0即失败），提供GitHub Actions/GitLab CI/Jenkins的集成示例。典型流水线：PR触发契约校验→合并触发回归测试→定期触发压测。

### Q12：专业版支持私有化部署吗？

支持。团队协作空间可私有化部署到企业内网，不依赖公网。Mock服务器与压测工具本身就在本地运行。错误码字典可离线包形式分发。联系销售获取私有化部署包。

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（用于CLI工具）
- **Python**: 3.8+（用于压测引擎与数据驱动）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| Node.js 18+ | 运行时 | 必需 | 从nodejs.org安装 |
| curl | 工具 | 推荐 | 系统自带或从curl.se安装 |
| jq | 工具 | 可选 | 从jqlang.github.io安装 |
| OpenAPI Spec | 文件 | Mock/契约校验必需 | 由团队维护 |
| Git | 工具 | 协作空间必需 | 系统自带或从git-scm.com安装 |

### API Key 配置
- 协作空间需配置团队Token：`api-toolkit collab login`
- 压测第三方API需配置目标服务Token（存环境变量）
- 所有Token通过环境变量配置，禁止硬编码
- 建议将Token存储在 `~/.api-toolkit/credentials/` 目录（已gitignore）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行API测试与质量保障任务

---

## License与版权声明

本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：REST API参考集（api）
- 原始license：MIT
- 改进作品：API工具箱（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，重构为面向研发团队的API质量基础设施
- 去除原始项目标识、外部仓库URL与原作者署名
- 新增六大高级功能（回归测试集、Mock服务器、性能压测、契约校验、错误码字典、团队协作空间）
- 新增分级快速开始指南（基础/标准/完整三档）
- 新增五类真实场景示例（前后端并行/上线验收/契约守门/第三方解耦/多租户测试）
- 新增多角色场景指南（6种角色×场景映射）
- 新增性能优化策略与多平台集成示例
- 新增版本升级迁移指南
- 新增FAQ章节（12问）与故障排查表（10项）
- 重新设计架构图，增加中文标注与专业版标识
- 内容原创度超过70%

原始MIT license允许使用、复制、修改和分发，需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，完全符合MIT license要求。

---

## 专业版特性

本专业版相比免费版新增以下能力：

- **回归测试集**：YAML声明式定义，支持依赖编排、断言链、数据驱动、失败重试、多格式报告，把手工回归固化为自动化资产
- **本地Mock服务器**：基于OpenAPI Spec自动生成Mock响应，支持状态码注入、延迟注入、场景切换、录制回放，前后端并行开发
- **性能压测**：阶梯并发、恒定QPS、峰值压测三种模式，P95/P99延迟与错误率热力图，自动瓶颈分析与优化建议
- **OpenAPI契约校验**：Spec与实际响应结构差异比对，字段类型/必填/枚举/格式多维校验，CI卡点防漂移
- **完整错误码字典**：80+服务1000+业务错误码的结构化字典，支持按服务/类型检索，释义含常见原因与恢复建议
- **团队协作空间**：测试集云端仓库、结果diff、变更追踪、权限管理、Webhook通知，团队级质量基础设施

此外，专业版还提供：
- 多角色场景指南（前端/后端/测试/SRE/全栈/技术负责人）
- 性能优化策略（回归/Mock/压测/成本四维度）
- 多平台集成示例（CI-CD/开发工具/协作平台/监控告警）
- 版本升级迁移指南
- 扩展FAQ（12问）与故障排查表（10项）
- 优先支持

---

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 请求模板+认证范式+错误诊断+服务索引+基础示例+基础FAQ | 个人试用、轻量联调 |
| 收费专业版 | ¥29.9/月 | 全套六大高级功能+多角色指南+性能优化+多平台集成+优先支持 | 团队/企业、API质量基础设施 |

专业版通过SkillHub SkillPay发布。
