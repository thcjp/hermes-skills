# 详细参考 - api-toolkit-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (text)

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

## 代码示例 (yaml)

```yaml
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

## 代码示例 (text)

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

## 代码示例 (bash)

```bash
api-toolkit test list

api-toolkit test run ./tests/user-api.yaml --report ./reports/

api-toolkit test run ./tests/ --parallel --workers 4

api-toolkit mock start --spec ./openapi.yaml --port 8080
api-toolkit mock stop
api-toolkit mock status

api-toolkit load-test --target <URL> --concurrency 100 --duration 300s

api-toolkit contract-check --spec ./openapi.yaml --ci-mode

api-toolkit error-dict --service stripe --search "card"
api-toolkit error-dict --update  # 同步最新错误码
api-toolkit collab login
api-toolkit collab push ./tests/  # 推送测试集到云端
api-toolkit collab pull            # 拉取最新测试集
api-toolkit collab diff            # 对比本地与云端差异
api-toolkit report convert --from json --to html ./report.json
api-toolkit report archive --month 2026-07
```

## 代码示例 (yaml)

```yaml
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

### 标准搭建（<120秒）：跑第一个回归测试集
定义一个YAML格式的回归测试集：

```yaml
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



