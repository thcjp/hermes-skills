---
slug: "k8s"
name: "k8s"
version: "1.0.0"
displayName: "Kubernetes"
summary: "规避Kubernetes常见错误,资源限制/探针/选择器"
license: "Proprietary"
description: |-
  Avoid common Kubernetes mistakes — resource limits, probe configuration,
  selector mismatches, and。Use when 用户需要Kubernetes相关功能时使用。不适用于超出本技能能力范围的复杂需求.
tags:
  - Operations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Kubernetes

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

- **资源限制审查**：检测未设置 `resources.requests`/`limits` 的容器，防止资源争抢与OOMKill
- **探针配置检查**：验证 `livenessProbe`、`readinessProbe`、`startupProbe` 的配置合理性，避免误杀健康Pod
- **选择器匹配验证**：检查 `selector.matchLabels` 与 `template.metadata.labels` 是否一致，防止Service/Deployment失联
- **镜像安全扫描**：识别使用 `:latest` 标签、root用户运行、未设置 `imagePullPolicy` 的风险配置
- **网络策略审计**：验证NetworkPolicy的ingress/egress规则，检测未限制命名空间间流量的场景
- **RBAC最小权限检查**：分析ClusterRoleBinding/RoleBinding，标记过度授权（如 `*.*` verbs）

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 生产环境部署前审查 | Deployment/StatefulSet YAML清单 | 风险项列表 + 修复建议 + 合规评分 |
| OOMKill根因排查 | Pod事件日志与资源配置 | OOM原因分析 + 资源调整建议 |
| Service无法路由排查 | Service + Pod标签与选择器 | 匹配状态 + 修复方案 |
| 多集群配置漂移检测 | 多集群YAML清单差异 | 漂移项对比 + 统一建议 |
| 安全合规审计 | 全命名空间RBAC与NetworkPolicy | 权限矩阵 + 违规项 + 修复脚本 |

**不适用于**：集群安装初始化、节点硬件故障诊断、etcd数据恢复、Service Mesh配置管理

## 使用流程

1. 确认运行环境满足依赖说明中的要求，已配置 `kubectl` 并可访问目标集群
2. 确定审查范围：单个资源文件、整个命名空间或全集群
3. 提供YAML清单或使用 `kubectl get -o yaml` 导出的资源配置
4. 执行审查并查看输出的风险项列表与修复建议
5. 按优先级（Critical > Warning > Info）修复问题
6. 修复后重新审查确认问题已解决

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | 待审查的Kubernetes YAML清单内容，或 `kubectl get -o yaml` 输出 |
| resource_type | string | 否 | 资源类型，可选值: `deployment`/`statefulset`/`service`/`pod`/`all`，默认 `all` |
| namespace | string | 否 | 目标命名空间，默认从kubeconfig当前上下文读取 |
| check_level | string | 否 | 检查级别，可选值: `strict`/`standard`/`basic`，默认 `standard` |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "summary": {
      "total_checks": 15,
      "passed": 11,
      "warnings": 3,
      "critical": 1,
      "compliance_score": 73
    },
    "findings": [
      {
        "severity": "critical",
        "category": "resources",
        "resource": "deployment/my-app",
        "message": "容器 'web' 未设置 resources.limits.memory，存在OOMKill风险",
        "suggestion": "添加 resources.limits.memory: 512Mi 和 resources.requests.memory: 256Mi"
      },
      {
        "severity": "warning",
        "category": "probe",
        "resource": "deployment/my-app",
        "message": "livenessProbe.initialDelaySeconds 设置为5s，可能低于启动时间",
        "suggestion": "根据应用实际启动时间调整，或使用 startupProbe 代替"
      }
    ],
    "metadata": {
      "template_used": "reviewer",
      "check_level": "standard",
      "namespace": "production"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 详细使用示例

### 示例1：资源限制审查

```yaml
# 问题配置：未设置资源限制
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      containers:
      - name: web
        image: nginx:1.25

# 审查输出:
# [CRITICAL] 容器 'web' 未设置 resources.requests 和 limits
# 建议: 添加以下配置
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
```

### 示例2：探针配置检查

```yaml
# 问题配置：livenessProbe过于激进
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 5      # 太短，应用可能还未启动
  periodSeconds: 3            # 过于频繁
  failureThreshold: 1         # 一次失败即重启

# 建议修复:
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30     # 留足启动时间
  periodSeconds: 10           # 10秒检查一次
  failureThreshold: 3         # 连续3次失败才重启
```

### 示例3：选择器匹配验证

```yaml
# 问题配置：selector与labels不匹配
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-server
spec:
  selector:
    matchLabels:
      app: api-server       # 选择器
  template:
    metadata:
      labels:
        app: api            # 标签不一致！
# 审查输出:
# [CRITICAL] selector.matchLabels.app=api-server 与 template.metadata.labels.app=api 不匹配
# Deployment将无法创建ReplicaSet，kubectl get pods 无输出
# 修复: 将 labels.app 改为 api-server
```

## 最佳实践

### 资源管理
- 始终同时设置 `requests` 和 `limits`，`requests` 用于调度，`limits` 用于约束
- CPU `requests` 设为应用平均使用量，`limits` 设为峰值1.5-2倍
- Memory `requests` 和 `limits` 设为相同值，避免因内存超限被OOMKill
- 使用 HorizontalPodAutoscaler (HPA) 基于CPU/Memory `requests` 百分比自动扩缩容

### 探针策略
- **startupProbe**：慢启动应用（如Java）优先使用，`failureThreshold * periodSeconds` 应大于启动时间
- **readinessProbe**：流量就绪检查，失败时从Service Endpoints移除但不重启
- **livenessProbe**：存活检查，失败时重启容器，`initialDelaySeconds` 必须大于应用启动时间
- 探针端点应轻量（<10ms响应），避免 `/health` 执行重逻辑

### 安全加固
```yaml
# 推荐的安全上下文配置
spec:
  template:
    spec:
      securityContext:
        runAsNonRoot: true        # 禁止root运行
        runAsUser: 1000           # 指定非root UID
        fsGroup: 2000             # 文件系统组
      containers:
      - name: app
        securityContext:
          allowPrivilegeEscalation: false  # 禁止提权
          readOnlyRootFilesystem: true     # 只读根文件系统
          capabilities:
            drop: ["ALL"]                 # 删除所有Linux capabilities
        image: my-app:1.2.3              # 禁止使用 :latest
        imagePullPolicy: IfNotPresent     # 明确设置拉取策略
```

## 常见排查命令

```bash
# 查看Pod资源使用情况
kubectl top pods -n <namespace> --sort-by=memory

# 查看OOMKill事件
kubectl get events -n <namespace> --field-selector reason=OOMKilling

# 查看Pod重启次数与原因
kubectl get pods -n <namespace> -o wide | grep -i restart

# 查看Service Endpoints是否匹配Pod
kubectl get endpoints <service-name> -n <namespace>

# 导出资源YAML进行审查
kubectl get deployment <name> -n <namespace> -o yaml > deploy.yaml

# 查看Pod详细事件（探针失败、拉取失败等）
kubectl describe pod <pod-name> -n <namespace>
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查kubeconfig配置与集群网络连通性 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| kubectl | CLI | 推荐 | https://kubernetes.io/docs/tasks/tools/ |
| kubeconfig | 配置 | 推荐 | 集群管理员提供，`~/.kube/config` |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.

## 常见问题

### Q1: 如何开始使用Kubernetes审查功能？
A: 准备好待审查的YAML清单文件，或使用 `kubectl get <resource> -o yaml` 导出集群中已有的资源配置。将YAML内容作为 `content` 传入，设置 `check_level` 为 `strict`（严格）、`standard`（标准）或 `basic`（基础）。审查结果按 `critical`（必须修复）、`warning`（建议修复）、`info`（提示信息）三级分类，每项包含问题描述与修复建议。

### Q2: 审查覆盖哪些Kubernetes资源类型？
A: 覆盖核心工作负载资源：Deployment、StatefulSet、DaemonSet、Pod、Job、CronJob。服务网络资源：Service、Ingress、NetworkPolicy。配置资源：ConfigMap、Secret。安全资源：ServiceAccount、Role、ClusterRole、RoleBinding、ClusterRoleBinding。存储资源：PersistentVolume、PersistentVolumeClaim、StorageClass。

### Q3: 如何解读合规评分？
A: 合规评分（compliance_score）为0-100的整数，计算方式为 `passed / total_checks * 100`。90+为优秀（生产就绪），70-89为合格（建议修复warning项），50-69为风险（需修复critical项），50以下为高风险（不建议上线）。评分不包含 `info` 级别的提示项。

### Q4: 是否支持自定义检查规则？
A: 标准版内置15+检查规则覆盖资源限制、探针、选择器、镜像安全、RBAC等。自定义规则需在 `references/custom-rules.yaml` 中定义，支持基于字段路径匹配、正则表达式和阈值的规则。每个规则可指定 `severity`、`category` 和 `suggestion` 模板。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
| kubeconfig未配置 | 无法连接集群 | 运行 `kubectl config view` 确认配置，或设置 `KUBECONFIG` 环境变量 |
| YAML解析失败 | YAML缩进或语法错误 | 使用 `kubectl apply --dry-run=client -f file.yaml` 验证语法 |

## 已知限制

- 审查基于静态YAML分析，不执行运行时检查（如实际CPU使用率）
- 不覆盖CRD（Custom Resource Definition）的自定义资源审查
- 不支持Helm Chart模板渲染后的差异化审查（需先 `helm template` 渲染）
- RBAC权限分析不包含聚合ClusterRole的权限继承链
- 网络策略检查不模拟实际流量路径，仅验证规则配置合理性

