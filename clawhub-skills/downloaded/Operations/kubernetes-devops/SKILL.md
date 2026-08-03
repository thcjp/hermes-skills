---
slug: kubernetes-devops
name: kubernetes-devops
version: "1.0.0"
displayName: Kubernetes
summary: "Kubernetes清单文件辅助编写,确保YAML配置正确性,减少因配置错误导致的部署失败"
  could copy examples th...
license: MIT
description: |-
  This is a coherent Kubernetes manifest helper; its main risk is that
  users could copy examples th。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags: '[''Operations'']'
tools:
  - read
  - exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---

# Kubernetes

Production-ready Kubernetes manifest generation covering Deployments, StatefulSets,
CronJobs, Services, Ingresses, ConfigMaps, Secrets, and PVCs with security contexts,
health checks, and resource management.

## Installation

### Skill平台 / Moltbot / Clawbot

```bash
npx SkillHub@latest install kubernetes
```

## When to Use

| Scenario | Example |
| --- | --- |
| Create deployment manifests | New microservice needing Deployment + Service |
| Define networking resources | ClusterIP, LoadBalancer, Ingress with TLS |
| Manage configuration | ConfigMaps for app config, Secrets for credentials |
| Stateful workloads | Databases with StatefulSets + PVCs |
| Scheduled jobs | CronJobs for batch processing |
| Multi-environment setup | Kustomize overlays for dev/staging/prod |

## Workload Selection

| Workload Type | Resource | When to Use |
| --- | --- | --- |
| Stateless app | Deployment | Web servers, APIs, microservices |
| Stateful app | StatefulSet | Databases, message queues, caches |
| One-off task | Job | Migrations, data imports |
| Scheduled task | CronJob | Backups, reports, cleanup |
| Per-node agent | DaemonSet | Log collectors, monitoring agents |

## Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  namespace: production
  labels:
    app.kubernetes.io/name: my-app
    app.kubernetes.io/version: "1.0.0"
    app.kubernetes.io/component: backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: my-app
  template:
    metadata:
      labels:
        app.kubernetes.io/name: my-app
        app.kubernetes.io/version: "1.0.0"
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: my-app
          image: registry.example.com/my-app:1.0.0
          ports:
            - containerPort: 8080
              name: http
          resources:
            requests:
              cpu: 250m
              memory: 256Mi
            limits:
              cpu: 500m
              memory: 512Mi
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: [ALL]
          livenessProbe:
            httpGet:
              path: /health
              port: http
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: http
            initialDelaySeconds: 5
            periodSeconds: 5
          env:
            - name: LOG_LEVEL
              valueFrom:
                configMapKeyRef:
                  name: my-app-config
                  key: LOG_LEVEL
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: my-app-secret
                  key: DATABASE_PASSWORD
```

## Services

### ClusterIP (Internal)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app
  namespace: production
spec:
  type: ClusterIP
  selector:
    app.kubernetes.io/name: my-app
  ports:
    - name: http
      port: 80
      targetPort: 8080
      protocol: TCP
```

### LoadBalancer (External)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-lb
  namespace: production
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
spec:
  type: LoadBalancer
  selector:
    app.kubernetes.io/name: my-app
  ports:
    - name: http
      port: 80
      targetPort: 8080
```

### Service Type Quick Reference

| Type | Scope | Use Case |
| --- | --- | --- |
| ClusterIP | Cluster-internal | Inter-service communication |
| NodePort | External via node IP | Dev/testing, on-prem |
| LoadBalancer | External via cloud LB | Production external access |
| ExternalName | DNS alias | Mapping to external services |

## Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-app
  namespace: production
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/rate-limit: "100"
spec:
  ingressClassName: nginx
  tls:
    - hosts: [app.example.com]
      secretName: app-tls
  rules:
    - host: app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-app
                port:
                  number: 80
```

## ConfigMap & Secret

### ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-app-config
  namespace: production
data:
  LOG_LEVEL: info
  APP_MODE: production
  DATABASE_HOST: db.internal.svc.cluster.local
  app.properties: |
    server.port=8080
    server.host=0.0.0.0
```

### Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-app-secret
  namespace: production
type: Opaque
stringData:
  DATABASE_PASSWORD: "changeme"
  API_KEY: "secret-api-key"
```

> **Important:** Never commit plaintext Secrets to Git. Use Sealed Secrets,
> External Secrets Operator, or Vault for production.

## Persistent Storage

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-app-data
  namespace: production
spec:
  accessModes: [ReadWriteOnce]
  storageClassName: gp3
  resources:
    requests:
      storage: 10Gi
```

Mount in a container:

```yaml
containers:
  - name: app
    volumeMounts:
      - name: data
        mountPath: /var/lib/app
volumes:
  - name: data
    persistentVolumeClaim:
      claimName: my-app-data
```

| Access Mode | Abbreviation | Use Case |
| --- | --- | --- |
| ReadWriteOnce | RWO | Single-pod databases |
| ReadOnlyMany | ROX | Shared config/static assets |
| ReadWriteMany | RWX | Multi-pod shared storage |

## Security Context

### Pod-Level

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
```

### Container-Level

```yaml
securityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: [ALL]
```

### Security Checklist

| Check | Status |
| --- | --- |
| `runAsNonRoot: true` | Required |
| `allowPrivilegeEscalation: false` | Required |
| `readOnlyRootFilesystem: true` | Recommended |
| `capabilities.drop: [ALL]` | Required |
| `seccompProfile: RuntimeDefault` | Recommended |
| Specific image tags (never `:latest`) | Required |
| Resource requests and limits set | Required |

## Standard Labels

```yaml
metadata:
  labels:
    app.kubernetes.io/name: my-app
    app.kubernetes.io/instance: my-app-prod
    app.kubernetes.io/version: "1.0.0"
    app.kubernetes.io/component: backend
    app.kubernetes.io/part-of: my-system
    app.kubernetes.io/managed-by: kubectl
```

## Manifest Organization

### Option 1 — Separate Files

```text
manifests/
├── configmap.yaml
├── secret.yaml
├── deployment.yaml
├── service.yaml
└── pvc.yaml
```

### Option 2 — Kustomize

```text
base/
├── kustomization.yaml
├── deployment.yaml
├── service.yaml
└── configmap.yaml
overlays/
├── dev/
│   └── kustomization.yaml
└── prod/
    ├── kustomization.yaml
    └── resource-patch.yaml
```

## Validation

```bash
kubectl apply -f manifest.yaml --dry-run=client

kubectl apply -f manifest.yaml --dry-run=server

kube-score score manifest.yaml

kube-linter lint manifest.yaml
```

## 错误处理

| Problem | Diagnosis | Fix |
| --- | --- | --- |
| Pod stuck `Pending` | `kubectl describe pod` — check events | Fix resource requests, node capacity, PVC binding |
| `ImagePullBackOff` | Wrong image name/tag or missing pull secret | Verify image exists, add `imagePullSecrets` |
| `CrashLoopBackOff` | App crashes on start | Check logs: `kubectl logs <pod> --previous` |
| Service not reachable | Selector mismatch | Verify `kubectl get endpoints <svc>` is non-empty |
| ConfigMap not loading | Name mismatch or wrong namespace | Check names match and namespace is correct |
| Readiness probe failing | Wrong path or port | Verify health endpoint works inside container |
| OOMKilled | Memory limit too low | Increase `resources.limits.memory` |

## NEVER Do

| Anti-Pattern | Why | Do Instead |
| --- | --- | --- |
| Use `:latest` image tag | Non-reproducible deployments | Pin exact version: `image:1.2.3` |
| Skip resource limits | Pods can starve the node | Always set `requests` and `limits` |
| Run as root | Container escape = full host access | Set `runAsNonRoot: true` + `USER` |
| Commit plaintext Secrets | Credentials in Git history forever | Use Sealed Secrets / External Secrets / Vault |
| Skip health checks | K8s can't detect unhealthy pods | Always configure liveness + readiness probes |
| Omit labels | Cannot filter, select, or organize | Use standard `app.kubernetes.io/*` labels |
| Single replica for production | Zero availability during updates | Use `replicas: 3` minimum for HA |
| Hardcode config in containers | Requires rebuild for config changes | Use ConfigMaps and Secrets |

## Assets & References

### Assets (Templates)

| Template | Description |
| --- | --- |
| [assets/deployment-template.yaml](/api/v1/skills/kubernetes-devops/file?path=assets%2Fdeployment-template.yaml&ownerHandle=wpank) | Production Deployment with security + probes |
| [assets/service-template.yaml](/api/v1/skills/kubernetes-devops/file?path=assets%2Fservice-template.yaml&ownerHandle=wpank) | ClusterIP, LoadBalancer, NodePort examples |
| [assets/configmap-template.yaml](/api/v1/skills/kubernetes-devops/file?path=assets%2Fconfigmap-template.yaml&ownerHandle=wpank) | ConfigMap with data types |
| [assets/statefulset-template.yaml](/api/v1/skills/kubernetes-devops/file?path=assets%2Fstatefulset-template.yaml&ownerHandle=wpank) | StatefulSet with headless Service + PVC |
| [assets/cronjob-template.yaml](/api/v1/skills/kubernetes-devops/file?path=assets%2Fcronjob-template.yaml&ownerHandle=wpank) | CronJob with concurrency + history |
| [assets/ingress-template.yaml](/api/v1/skills/kubernetes-devops/file?path=assets%2Fingress-template.yaml&ownerHandle=wpank) | Ingress with TLS, rate limiting, CORS |

### References

| Reference | Description |
| --- | --- |
| [references/deployment-spec.md](/api/v1/skills/kubernetes-devops/file?path=references%2Fdeployment-spec.md&ownerHandle=wpank) | Detailed Deployment specification |
| [references/service-spec.md](/api/v1/skills/kubernetes-devops/file?path=references%2Fservice-spec.md&ownerHandle=wpank) | Service types and networking details |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- This is a coherent Kubernetes manifest helper
- its main risk is that
  users could copy examples th
- 触发关键词: devops, kubernetes, coherent, manifest, helper

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 常见问题

### Q1: 如何开始使用Kubernetes？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Kubernetes有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力

---
## 边界条件与限制 (Boundary Conditions)

### 输入限制
- **输入格式**: 用户输入必须遵循特定的格式，例如使用YAML语法描述Kubernetes资源。
- **资源类型**: 支持的Kubernetes资源类型有限，如Deployments, Services, ConfigMaps等，不支持所有可能的Kubernetes资源。
- **复杂性**: 对于过于复杂的Kubernetes配置，技能可能无法正确解析或生成清单文件。

### 性能边界
- **并发处理**: 同时处理多个请求时，性能可能会受到影响，特别是在高负载情况下。
- **资源消耗**: 生成清单文件时，可能会消耗较多的内存和CPU资源，特别是在处理大型配置文件时。

### 兼容性约束
- **Kubernetes版本**: 支持的Kubernetes版本有限，可能不支持所有版本的Kubernetes集群。
- **插件和扩展**: 对于使用特定插件或扩展的Kubernetes集群，技能可能无法正确处理这些资源。

### 其他限制
- **外部依赖**: 需要外部工具（如kubectl）来应用生成的清单文件。
- **安全性**: 不支持生成包含敏感信息的清单文件，如密码和密钥，这些信息需要通过安全的方式进行管理。

## 安全注意事项 (Security Considerations)

### 认证与授权
- **敏感操作**: 对于可能影响集群安全性的操作，如创建或修改Secrets，需要适当的认证和授权。
- **最小权限原则**: 用户应该只被授予执行其任务所需的最小权限。

### 数据保护
- **敏感数据**: 不要在清单文件中直接包含敏感数据，如密码和密钥，应使用Secrets管理。
- **数据加密**: 对于传输中的数据，应使用TLS等加密协议。

### 配置管理
- **配置审计**: 定期审计配置文件，确保没有意外的更改。
- **版本控制**: 使用版本控制系统管理配置文件，以便跟踪更改和回滚到以前的状态。

## 代码示例与最佳实践 (Code Examples and Best Practices)

### 代码示例
```yaml
apiVersion: v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        ports:
        - containerPort: 80
```

### 最佳实践
- **使用标签**: 为资源使用清晰、一致的标签，以便于管理和组织。
- **资源分离**: 将配置文件分解为多个文件，以保持清晰和可维护性。
- **版本控制**: 使用版本控制系统跟踪配置更改，并确保代码质量。

## 文档更新与维护 (Documentation Updates and Maintenance)

### 更新频率
- **定期更新**: 定期检查文档的准确性和相关性，根据Kubernetes的更新进行必要的调整。
- **社区反馈**: 关注社区反馈，根据用户的需求和建议进行文档改进。

### 维护策略
- **版本控制**: 使用版本控制系统管理文档，以便跟踪更改和回滚到以前的状态。
- **文档结构**: 保持文档结构的清晰和一致，以便用户易于导航。

## 用户支持与反馈 (User Support and Feedback)

### 支持渠道
- **官方论坛**: 在官方论坛上提供技术支持，帮助用户解决使用过程中的问题。
- **社区支持**: 鼓励用户参与社区讨论，共同解决问题。

### 反馈机制
- **用户反馈**: 提供反馈机制，收集用户的意见和建议。
- **问题跟踪**: 使用问题跟踪系统记录和解决用户反馈的问题。

## 法律声明与免责条款 (Legal Statements and Disclaimers)

### 法律声明
- **版权声明**: 本文档版权所有，未经授权不得复制、分发或使用。
- **知识产权**: 保留所有知识产权，包括但不限于商标、专利和版权。

### 免责条款
- **使用风险**: 用户使用本技能时自行承担风险，开发者不承担任何责任。
- **服务中断**: 开发者不保证服务的连续性和可用性。

## 差异化优势

### 与同类方案对比

1. **手动操作**：手动编写Kubernetes配置文件需要深入的技术知识和经验，且容易出错。手动操作效率低下，且难以维护和更新。相比之下，我们的技能通过自动化生成YAML配置文件，减少了配置错误，提高了部署效率。

2. **其他工具**：虽然市面上存在一些Kubernetes配置生成工具，但它们通常功能单一，不支持多种资源类型的配置。我们的技能集成了丰富的资源类型，包括Deployments、Services、Ingresses等，并提供安全上下文、健康检查和资源管理等功能，提供更全面的解决方案。

3. **通用方法**：通用方法如使用在线模板或手动编写YAML文件，缺乏个性化定制和自动化功能。我们的技能通过预定义模板和编程辅助功能，允许用户快速定制配置，并通过自动化脚本提高工作效率。

### 独特功能

1. **自动化代码生成**：提供丰富的预定义模板和自动化脚本，可以快速生成各种Kubernetes资源配置，节省手动编写的时间。

2. **安全上下文管理**：支持设置运行用户、安全策略和资源限制，提高容器运行的安全性。

3. **多环境支持**：通过Kustomize功能，支持为开发、测试和生产环境快速定制资源配置，提高部署灵活性。

4. **集成配置管理**：支持ConfigMaps和Secrets管理，简化应用程序配置和敏感信息的处理。

5. **健康检查和资源管理**：提供liveness和readiness probes，以及CPU和内存资源限制，确保应用程序稳定运行。

### 效率提升

使用本技能可以节省大量时间，例如：

- 自动生成YAML配置文件，节省手动编写时间；
- 减少配置错误，降低部署失败率；
- 通过自动化脚本，提高部署和更新效率。

### 应用场景创新

1. **微服务架构**：利用本技能自动化部署和管理微服务，提高开发效率。

2. **持续集成/持续部署（CI/CD）**：集成到CI/CD流程中，实现自动化部署和测试，提高交付速度。

3. **多云环境**：在多个云平台上使用本技能，简化跨云部署和管理。

