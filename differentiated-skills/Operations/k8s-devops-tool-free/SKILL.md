---
slug: k8s-devops-tool-free
name: k8s-devops-tool-free
version: "1.0.0"
displayName: K8s清单生成入门
summary: Kubernetes YAML清单生成工具，支持常用资源模板与基础校验。
license: Proprietary
edition: free
description: |-
  面向个人开发者的K8s YAML清单生成工具。支持Deployment/Service/
  ConfigMap等常用资源的清单生成与基础校验。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Operations
- Kubernetes
- DevOps
- 清单生成
tools:
  - - read
- exec
---

# K8s清单生成入门（免费版）

## 概述

本工具为个人开发者提供K8s YAML清单生成能力。支持常用K8s资源的清单生成、模板化创建和基础校验，帮助开发者快速编写规范的K8s配置文件。

## 核心能力

### 清单生成功能

| 资源类型 | 生成 | 校验 | 模板 |
| --- | --- | --- | --- |
| Deployment | 支持 | 支持 | Web应用/任务 |
| Service | 支持 | 支持 | ClusterIP/NodePort |
| ConfigMap | 支持 | 支持 | 配置文件 |
| Secret | 支持 | 支持 | 密码/证书 |
| Ingress | 支持 | 支持 | 基础路由 |
| Job/CronJob | 支持 | 支持 | 定时任务 |
| PVC | 支持 | 支持 | 存储卷 |
| Namespace | 支持 | 支持 | 命名空间 |
| Helm Chart | 不支持 | 不支持 | - |
| Kustomize | 不支持 | 不支持 | - |

## 使用场景

### 场景一：生成Deployment清单

用户输入："帮我生成一个Web应用的Deployment清单"

```bash
# 生成Deployment清单
python3 scripts/generate.py deployment \
  --name web-app \
  --image nginx:1.25 \
  --replicas 3 \
  --port 80 \
  --output deployment.yaml

# 输出文件内容
cat deployment.yaml
```

### 场景二：生成完整应用栈

用户输入："生成Web+数据库的完整K8s清单"

```bash
# 生成应用栈
python3 scripts/generate.py stack \
  --template "web_db" \
  --app-name my-app \
  --app-image my-app:v1 \
  --db-image postgres:15 \
  --output-dir ./manifests/

# 输出：
# ./manifests/deployment.yaml
# ./manifests/service.yaml
# ./manifests/configmap.yaml
# ./manifests/secret.yaml
# ./manifests/pvc.yaml
```

### 场景三：校验清单

用户输入："检查我的YAML清单有没有问题"

```bash
# 校验清单
python3 scripts/generate.py validate \
  --file deployment.yaml \
  --dry-run

# 输出：
# [OK] 语法正确
# [OK] 必填字段完整
# 已知限制
# [建议] 添加livenessProbe
```

## 快速开始

### 环境准备

```bash
# 依赖说明
pip install pyyaml jsonschema

# 生成清单
python3 scripts/generate.py deployment --name my-app --image nginx:1.25
```

### 常用命令

```bash
# 生成单个资源
python3 scripts/generate.py deployment --name my-app --image my-image:v1 --replicas 3
python3 scripts/generate.py service --name my-service --port 80 --type ClusterIP
python3 scripts/generate.py configmap --name my-config --from-file ./config.yaml

# 生成应用栈
python3 scripts/generate.py stack --template "web_db" --app-name my-app

# 校验清单
python3 scripts/generate.py validate --file deployment.yaml --dry-run

# 查看模板列表
python3 scripts/generate.py templates list
```

## 示例

### 生成模板配置

```yaml
generate_config:
  defaults:
    api_version: "apps/v1"
    namespace: "default"
    replicas: 2
    image_pull_policy: "IfNotPresent"

  resources:
    requests:
      cpu: "100m"
      memory: "128Mi"
    limits:
      cpu: "500m"
      memory: "512Mi"

  templates:
    - name: "web_app"
      resources: ["deployment", "service", "configmap", "ingress"]
    - name: "web_db"
      resources: ["deployment", "service", "configmap", "secret", "pvc"]
    - name: "cron_job"
      resources: ["cronjob", "configmap"]

  validation:
    schema_check: true
    dry_run: true               # kubectl dry-run验证
    best_practices: true         # 最佳实践检查
```

## 最佳实践

1. **模板复用**：将常用配置保存为模板，避免重复编写
2. **校验优先**：生成后先校验再应用，避免配置错误
3. **版本控制**：将清单文件纳入Git管理
4. **标签统一**：使用统一的标签规范

| 实践要点 | 说明 |
| --- | --- |
| 资源限制 | 生成的清单包含resources默认值 |
| 健康检查 | 模板中预置探针配置 |
| 镜像版本 | 使用具体版本号，避免latest |
| 命名规范 | 资源名使用小写和中划线 |

## 常见问题

### Q1：免费版支持Helm Chart吗？

免费版不包含Helm Chart生成。如需Helm支持，建议升级PRO版。

### Q2：生成的清单可以直接apply吗？

可以。生成后通过 `kubectl apply -f` 直接应用。建议先用 `--dry-run` 校验。

### Q3：支持Kustomize吗？

免费版不包含Kustomize支持。如需Kustomize覆盖层管理，建议升级PRO版。

### Q4：模板可以自定义吗？

免费版提供预置模板，不支持自定义模板。如需自定义模板系统，建议升级PRO版。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+
- **kubectl**: 可选（dry-run校验需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| PyYAML | Python库 | 必需 | `pip install pyyaml` |
| jsonschema | Python库 | 可选 | `pip install jsonschema`（校验） |

### API Key 配置

- 免费版无需API Key
- 纯本地生成与校验

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: K8s YAML清单生成与校验工具
- **免费版限制**: 基础资源生成、不支持Helm/Kustomize与自定义模板

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |
