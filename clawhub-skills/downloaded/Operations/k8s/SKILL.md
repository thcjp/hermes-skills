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
  selector mismatches, and...

  核心能力:

  - 运维工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 系统运维、监控告警、资源管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: avoid, mistakes, kubernetes, common, resource, k8s
tags:
- Operations
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
