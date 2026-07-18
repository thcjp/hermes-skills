---
slug: kubernetes-toolkit-free
name: kubernetes-toolkit-free
version: "1.0.0"
displayName: K8s集群管理入门
summary: Kubernetes集群基础管理工具，支持多Agent协作与常用资源操作。
license: MIT
edition: free
description: |-
  面向个人开发者与小团队的K8s集群管理工具。支持多Agent协作模式，
  提供Pod/Service/Deployment/ConfigMap等常用资源的创建、查询与
  管理功能。适合个人开发环境与小规模集群的日常管理。

  核心能力:
  - 多Agent协作集群管理
  - 常用资源CRUD操作
  - 基础故障排查
  - kubectl命令封装

  适用场景:
  - 个人K8s集群管理
  - 开发测试环境运维
  - 小团队协作管理
  - K8s学习实践

  差异化:
  - 免费版聚焦基础资源管理
  - 支持多Agent协作
  - 不支持企业级治理
  - 不支持高级运维自动化

  触发关键词: Kubernetes, K8s, 集群管理, 多Agent, Pod, Service, 资源管理, kubectl
tags:
- Operations
- Kubernetes
- 集群管理
tools:
- read
- exec
---

# K8s集群管理入门（免费版）

## 概述

本工具为个人开发者和小团队提供K8s集群管理能力。采用多Agent协作模式，支持常用K8s资源的创建、查询与管理。适合个人开发环境与小规模集群的日常运维。

## 核心能力

### 管理功能

| 功能 | 说明 | 免费版支持 |
| --- | --- | --- |
| 资源管理 | Pod/Service/Deployment等 | 支持 |
| 多Agent | 协作管理模式 | 支持 |
| 配置管理 | ConfigMap/Secret | 支持 |
| 故障排查 | 基础问题诊断 | 支持 |
| 命名空间 | 命名空间管理 | 支持 |
| 节点管理 | 节点查询与标签 | 基础 |
| 监控告警 | 集群监控 | 不支持 |
| 策略治理 | 策略管理 | 不支持 |

### 支持的资源类型

| 资源 | 创建 | 查询 | 更新 | 删除 |
| --- | --- | --- | --- | --- |
| Pod | 支持 | 支持 | 有限 | 支持 |
| Deployment | 支持 | 支持 | 支持 | 支持 |
| Service | 支持 | 支持 | 支持 | 支持 |
| ConfigMap | 支持 | 支持 | 支持 | 支持 |
| Secret | 支持 | 支持 | 支持 | 支持 |
| Ingress | 支持 | 支持 | 支持 | 支持 |
| PVC | 支持 | 支持 | 有限 | 支持 |
| Namespace | 支持 | 支持 | 不支持 | 支持 |

## 使用场景

### 场景一：部署应用

用户输入："帮我部署一个Nginx应用"

```bash
# 创建Deployment
python3 scripts/k8s.py deploy \
  --name nginx-app \
  --image nginx:1.25 \
  --replicas 3 \
  --port 80 \
  --namespace default

# 创建Service
python3 scripts/k8s.py expose \
  --deployment nginx-app \
  --port 80 \
  --type ClusterIP \
  --name nginx-service
```

### 场景二：多Agent协作管理

用户输入："让多个Agent分别管理不同命名空间"

```bash
# 配置多Agent
python3 scripts/k8s.py agents config \
  --agent dev-agent --namespace development \
  --agent staging-agent --namespace staging \
  --agent prod-agent --namespace production

# 各Agent独立管理各自命名空间
python3 scripts/k8s.py agents status
```

### 场景三：资源查询

用户输入："查看default命名空间的所有资源"

```bash
# 查询资源
python3 scripts/k8s.py list --namespace default --all-resources

# 输出：
# Deployments: nginx-app (3/3)
# Services: nginx-service (ClusterIP: 10.96.0.10)
# ConfigMaps: nginx-config
# Pods: nginx-app-xxx (running)
```

## 快速开始

### 环境准备

```bash
# 安装kubectl并配置kubeconfig
# 安装Python依赖
pip install kubernetes

# 验证连接
python3 scripts/k8s.py info
```

### 常用命令

```bash
# 部署应用
python3 scripts/k8s.py deploy --name my-app --image my-image:v1 --replicas 3

# 查询资源
python3 scripts/k8s.py list --namespace default
python3 scripts/k8s.py get pod --name my-app-xxx
python3 scripts/k8s.py logs --name my-app-xxx --tail 100

# 更新资源
python3 scripts/k8s.py scale --deployment my-app --replicas 5
python3 scripts/k8s.py rollout --deployment my-app --status

# 配置管理
python3 scripts/k8s.py configmap create --name my-config --from-file ./config.yaml
python3 scripts/k8s.py secret create --name my-secret --from-literal password=xxx

# 故障排查
python3 scripts/k8s.py diagnose --pod my-app-xxx
```

## 配置示例

### K8s管理配置

```yaml
k8s_config:
  kubeconfig: "~/.kube/config"
  context: "default"
  namespace: "default"

  agents:
    mode: "collaborative"         # collaborative | single
    max_agents: 5
    namespaces:
      - agent: "dev-agent"
        namespace: "development"
      - agent: "prod-agent"
        namespace: "production"

  defaults:
    replicas: 2
    image_pull_policy: "IfNotPresent"
    restart_policy: "Always"
    service_type: "ClusterIP"

  resources:
    default_requests:
      cpu: "100m"
      memory: "128Mi"
    default_limits:
      cpu: "500m"
      memory: "512Mi"
```

## 最佳实践

1. **命名规范**：统一资源命名规范，便于管理
2. **标签管理**：使用标签组织资源，便于查询筛选
3. **命名空间隔离**：不同环境使用不同命名空间
4. **配置分离**：使用ConfigMap/Secret管理配置

| 实践要点 | 说明 |
| --- | --- |
| 资源限制 | 所有Pod设置resources |
| 镜像版本 | 使用固定版本号 |
| 健康检查 | 配置liveness/readiness |
| 多Agent | 按命名空间分工，避免冲突 |

## 常见问题

### Q1：多Agent协作如何工作？

多个Agent各自管理指定命名空间的资源，互不干扰。中央协调器负责跨命名空间的协调与冲突检测。适合团队按环境或项目分工。

### Q2：免费版支持多少个命名空间？

免费版支持最多5个命名空间的管理。如需管理更多命名空间或大规模集群，建议升级PRO版。

### Q3：支持CRD（自定义资源）吗？

免费版支持查询CRD，但创建和管理CRD能力有限。如需完整CRD支持，建议升级PRO版。

### Q4：如何接入已有集群？

配置kubeconfig文件指向已有集群的API Server。本工具通过kubernetes-python客户端连接集群，无需在集群内部署。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+
- **kubectl**: 已配置集群访问

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| kubernetes | Python库 | 必需 | `pip install kubernetes` |
| PyYAML | Python库 | 必需 | `pip install pyyaml` |

### API Key 配置

- 通过kubeconfig认证集群
- 无需额外API Key
- kubeconfig文件包含集群访问凭证

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+kubectl执行）
- **说明**: 通过kubernetes-python客户端管理K8s集群
- **免费版限制**: 基础资源管理、5命名空间、不支持监控与策略治理
