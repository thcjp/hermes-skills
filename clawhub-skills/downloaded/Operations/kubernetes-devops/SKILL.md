---
slug: kubernetes-devops
name: kubernetes-devops
version: "1.0.0"
displayName: Kubernetes
summary: This is a coherent Kubernetes manifest helper; its main risk is that users
  could copy examples th...
license: MIT
description: |-
  This is a coherent Kubernetes manifest helper; its main risk is that
  users could copy examples th。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags: '[''Operations'']'
tools:
  - read
  - exec
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
