---
slug: k8s
name: k8s
version: "1.0.0"
displayName: Kubernetes
summary: Avoid common Kubernetes mistakes — resource limits, probe configuration,
  selector mismatches, and...
license: MIT
description: |-
  Avoid common Kubernetes mistakes — resource limits, probe configuration,
  selector mismatches, and。Use when 用户需要Kubernetes相关功能时使用。不适用于超出本技能能力范围的复杂需求。
tags:
- Operations
tools:
  - - read
- exec
pricing_tier: "L3"
pricing_model: "per_use"
suggested_price: 29.9
---


# Kubernetes

## Resource Management

* `requests` = guaranteed minimum — scheduler uses this for placement
* `limits` = maximum allowed — exceeding memory = OOMKilled, CPU = throttled
* No limits = can consume entire node — always set production limits
* `requests` without `limits` = burstable — can use more if available

## Probes

* `readinessProbe` controls traffic — fails = removed from Service endpoints
* `livenessProbe` restarts container — fails = container killed and restarted
* `startupProbe` for slow starts — disables liveness/readiness until success
* Don't use same endpoint for liveness and readiness — liveness should be minimal health check

## Probe Pitfalls

* Liveness probe checking dependencies — if DB down, all pods restart indefinitely
* `initialDelaySeconds` too short — pod killed before app starts
* `timeoutSeconds` too short — slow response = restart loop
* HTTP probe to HTTPS endpoint — needs `scheme: HTTPS`

## Labels and Selectors

* Service selector must match Pod labels exactly — typo = no endpoints
* Deployment selector is immutable — can't change after creation
* Use consistent labeling scheme — `app`, `version`, `environment`
* `matchExpressions` for complex selection — `In`, `NotIn`, `Exists`

## ConfigMaps and Secrets

* ConfigMap changes don't restart pods — mount as volume for auto-update, or restart manually
* Secrets are base64 encoded, not encrypted — use external secrets manager for sensitive data
* `envFrom` imports all keys — `env.valueFrom` for specific keys
* Volume mount makes files — `subPath` for single file without replacing directory

## Networking

* `ClusterIP` internal only — default, only accessible within cluster
* `NodePort` exposes on node IP — 30000-32767 range, not for production
* `LoadBalancer` provisions cloud LB — works only in supported environments
* Ingress needs Ingress Controller — nginx-ingress, traefik, etc. installed separately

## Persistent Storage

* PVC binds to PV — must match capacity and access modes
* `storageClassName` must match — or use `""` for no dynamic provisioning
* `ReadWriteOnce` = single node — `ReadWriteMany` needed for multi-pod
* Pod deletion doesn't delete PVC — `persistentVolumeReclaimPolicy` controls PV fate

## Common Mistakes

* `kubectl apply` vs `create` — apply for declarative (can update), create for imperative (fails if exists)
* Forgetting namespace — `-n namespace` or set context default
* Image tag `latest` in production — no version pinning, unpredictable updates
* Not setting `imagePullPolicy` — `Always` for latest tag, `IfNotPresent` for versioned
* Service port vs targetPort — port is Service's, targetPort is container's

## Debugging

* `kubectl describe pod` for events — shows scheduling failures, probe failures
* `kubectl logs -f pod` for logs — `-p` for previous container (after crash)
* `kubectl exec -it pod -- sh` for shell — debug inside container
* `kubectl get events --sort-by=.lastTimestamp` — cluster-wide events timeline

## RBAC

* `ServiceAccount` per workload — not default, for least privilege
* `Role` is namespaced — `ClusterRole` is cluster-wide
* `RoleBinding` binds Role to user/SA — `ClusterRoleBinding` for cluster-wide
* Check permissions: `kubectl auth can-i verb resource --as=system:serviceaccount:ns:sa`

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

- Avoid common Kubernetes mistakes — resource limits, probe configuration,
  selector mismatches, and
- 触发关键词: avoid, mistakes, kubernetes, common, resource, k8s

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

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
