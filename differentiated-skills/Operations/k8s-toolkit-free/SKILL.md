---
slug: k8s-toolkit-free
name: k8s-toolkit-free
version: "1.0.0"
displayName: K8s避坑入门工具
summary: Kubernetes常见问题避坑指南，提供基础排查与最佳实践建议。
license: MIT
edition: free
description: |-
  面向K8s初学者与个人开发者的常见问题避坑工具。总结Kubernetes
  使用中的高频问题与陷阱，提供排查思路与解决方案。适合K8s入门
  学习与日常问题排查。

  核心能力:
  - 常见问题避坑指南
  - Pod/Service/Deployment基础排查
  - 资源配置最佳实践
  - 常用kubectl命令速查

  适用场景:
  - K8s初学者学习
  - 日常问题排查
  - 配置优化参考
  - 命令速查手册

  差异化:
  - 免费版聚焦基础知识与避坑
  - 适合个人开发者学习
  - 不支持集群级管理
  - 不支持高级运维自动化

  触发关键词: K8s, Kubernetes, 避坑, 排查, Pod, Service, Deployment, kubectl, 问题诊断
tags:
- Operations
- Kubernetes
- 运维
- 学习
tools:
- read
- exec
---

# K8s避坑入门工具（免费版）

## 概述

本工具为K8s初学者和个人开发者提供常见问题避坑指南。总结Kubernetes使用中的高频问题与陷阱，提供排查思路、解决方案和最佳实践建议，帮助用户快速解决日常K8s问题。

## 核心能力

### 避坑知识库

| 类别 | 问题数量 | 免费版覆盖 |
| --- | --- | --- |
| Pod问题 | 15个 | 常见8个 |
| Service问题 | 10个 | 常见5个 |
| Deployment问题 | 12个 | 常见6个 |
| 网络问题 | 10个 | 常见5个 |
| 存储问题 | 8个 | 常见4个 |
| 安全问题 | 8个 | 常见4个 |
| 性能问题 | 10个 | 不支持 |
| 集群运维 | 15个 | 不支持 |

### 常见避坑主题

| 主题 | 常见陷阱 | 影响 |
| --- | --- | --- |
| 资源限制 | 未设置resources | Pod抢占资源 |
| 镜像策略 | 用latest标签 | 版本不可控 |
| 健康检查 | 未配置探针 | 僵尸Pod |
| 服务类型 | 误用LoadBalancer | 成本增加 |
| 配置管理 | 硬编码配置 | 环境不可迁移 |
| 持久化 | 数据卷未备份 | 数据丢失 |

## 使用场景

### 场景一：Pod问题排查

用户输入："我的Pod一直处于CrashLoopBackOff状态"

```bash
# 排查Pod问题
/k8s troubleshoot pod --name my-app --namespace default

# 输出排查步骤：
# 1. 查看Pod事件
#    kubectl describe pod my-app
# 2. 查看容器日志
#    kubectl logs my-app --previous
# 3. 常见原因：
#    - 应用启动失败（检查配置）
#    - 资源不足（调整resources）
#    - 健康检查失败（调整探针）
#    - 镜像拉取失败（检查镜像名）
```

### 场景二：Service无法访问

用户输入："Service创建成功但访问不了"

```bash
# 排查Service问题
/k8s troubleshoot service --name my-service

# 输出排查步骤：
# 1. 检查Service端点
#    kubectl get endpoints my-service
# 2. 检查Pod标签匹配
#    kubectl get pods --show-labels
# 3. 检查端口配置
# 4. 常见原因：标签不匹配、端口不一致
```

### 场景三：最佳实践检查

用户输入："检查我的Deployment配置是否有问题"

```bash
# 配置检查
/k8s check deployment --name my-app

# 输出建议：
# [警告] 未设置resources限制
# [建议] 添加liveness/readiness探针
# [建议] 使用具体镜像版本而非latest
# [建议] 配置PodDisruptionBudget
```

## 快速开始

### 常用命令

```bash
# 问题排查
/k8s troubleshoot pod --name <pod-name>
/k8s troubleshoot service --name <svc-name>
/k8s troubleshoot deployment --name <dep-name>

# 配置检查
/k8s check deployment --name <dep-name>
/k8s check pod --name <pod-name>

# 命令速查
/k8s cheat-sheet
/k8s cheat-sheet --topic networking

# 避坑指南
/k8s pitfalls --category resources
/k8s pitfalls --category networking
```

### 常用kubectl速查

```bash
# 集群信息
kubectl cluster-info
kubectl get nodes

# Pod管理
kubectl get pods --all-namespaces
kubectl describe pod <name>
kubectl logs <name> --previous
kubectl exec -it <name> -- /bin/sh

# Service管理
kubectl get svc
kubectl get endpoints <name>

# Deployment管理
kubectl get deployments
kubectl scale deployment <name> --replicas=3
kubectl rollout status deployment/<name>
```

## 配置示例

### 安全Deployment模板

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: safe-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: safe-app
  template:
    metadata:
      labels:
        app: safe-app
    spec:
      containers:
      - name: app
        image: my-app:v1.2.3          # 避免用latest
        resources:                      # 必须设置资源限制
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:                  # 必须配置健康检查
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
        securityContext:                # 安全上下文
          runAsNonRoot: true
          readOnlyRootFilesystem: true
```

## 最佳实践

1. **资源限制必设**：所有容器必须设置requests和limits
2. **镜像版本固定**：使用具体版本号，避免latest
3. **健康检查必配**：配置liveness和readiness探针
4. **标签规范统一**：统一标签命名规范，便于管理

| 避坑要点 | 说明 |
| --- | --- |
| 资源设置 | requests用于调度，limits用于限制 |
| 探针配置 | liveness检测存活，readiness检测就绪 |
| 镜像策略 | 固定版本便于回滚和追踪 |
| 配置分离 | 使用ConfigMap/Secret管理配置 |

## 常见问题

### Q1：免费版支持集群级问题排查吗？

免费版聚焦Pod/Service/Deployment基础排查。如需集群级问题诊断，建议升级PRO版。

### Q2：避坑指南覆盖多少问题？

免费版覆盖约32个常见问题。如需完整知识库（88+问题），建议升级PRO版。

### Q3：支持哪些K8s发行版？

通用K8s避坑指南适用于所有K8s发行版（包括EKS/GKE/AKS/自建集群）。发行版特有问题建议升级PRO版。

### Q4：可以直接修复问题吗？

免费版提供排查建议和解决方案，需手动执行修复。如需自动修复功能，建议升级PRO版。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **kubectl**: 已配置集群访问（排查时需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| kubectl | CLI工具 | 推荐 | 官网安装 |

### API Key 配置

- 免费版无需API Key
- 避坑指南为纯知识库，无需集群连接

### 可用性分类

- **分类**: MD（纯Markdown指令知识库）
- **说明**: K8s常见问题避坑指南与排查建议
- **免费版限制**: 基础问题覆盖、不支持集群级诊断与自动修复
