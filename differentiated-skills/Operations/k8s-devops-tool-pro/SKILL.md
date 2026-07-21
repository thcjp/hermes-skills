---
slug: k8s-devops-tool-pro
name: k8s-devops-tool-pro
version: "1.0.0"
displayName: K8s清单生成专业版
summary: 企业级K8s清单管理平台，支持Helm/Kustomize、策略校验与CI/CD集成。
license: Proprietary
edition: pro
description: |-
  面向企业DevOps团队的K8s清单管理平台。支持Helm Chart与Kustomize
  完整工作流、策略合规校验、多环境覆盖、GitOps集成与CRD管理。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Operations
- Kubernetes
- DevOps
- 企业级
tools:
  - - read
- exec
---

# K8s清单生成专业版（PRO版）

## 概述

本平台为企业DevOps团队提供全功能的K8s清单管理能力。相比免费版，PRO版新增Helm Chart、Kustomize、策略校验、多环境管理和GitOps集成等高级功能，全面满足企业级K8s清单管理的复杂需求。

PRO版完全兼容免费版清单生成命令，升级后原有模板可直接使用。

## 核心能力

### PRO版功能增强对比

| 功能 | 免费版 | PRO版 |
| --- | --- | --- |
| 清单格式 | 原生YAML | +Helm+Kustomize |
| 模板系统 | 预置模板 | 自定义+治理 |
| 环境管理 | 不支持 | 多环境覆盖 |
| 策略校验 | 基础检查 | OPA/Kyverno合规 |
| GitOps | 不支持 | ArgoCD/Flux集成 |
| CRD管理 | 不支持 | 完整生命周期 |
| 版本管理 | 不支持 | 版本化清单 |
| CI/CD | 基础集成 | 完整流水线 |

## 使用场景

### 场景一：Helm Chart管理

用户输入："为我的应用创建Helm Chart"

```bash
# 创建Helm Chart
python3 scripts/devops_pro.py helm create \
  --name my-app \
  --version 1.0.0 \
  --output-dir ./charts/

# 打包Chart
python3 scripts/devops_pro.py helm package \
  --chart-dir ./charts/my-app \
  --version 1.0.0 \
  --destination ./repo/

# 发布到仓库
python3 scripts/devops_pro.py helm push \
  --chart my-app-1.0.0.tgz \
  --repo https://harbor.example.com/chartrepo
```

### 场景二：多环境部署

用户输入："为dev/staging/prod生成差异化配置"

```bash
# 创建Kustomize结构
python3 scripts/devops_pro.py kustomize init \
  --base ./base/ \
  --overlays "dev,staging,prod"

# 生成各环境配置
python3 scripts/devops_pro.py kustomize build \
  --overlay prod \
  --output ./manifests/prod/

# 输出差异化配置
```

### 场景三：策略校验

用户输入："校验清单是否符合安全策略"

```bash
# 策略校验
python3 scripts/devops_pro.py validate \
  --file ./manifests/ \
  --policies "require_limits,disallow_latest,require_labels" \
  --engine "kyverno"

# 输出：
# 已知限制
# [FAIL] disallow_latest - web-app使用了latest标签
# [PASS] require_labels - 所有资源包含必要标签
```

## 快速开始

### PRO版初始化

```bash
# 依赖说明
pip install -r requirements_pro.txt

# 安装Helm
# macOS: brew install helm
# Linux: 下载官方安装包
```

### 常用命令

```bash
# Helm管理
python3 scripts/devops_pro.py helm create --name my-app --version 1.0.0
python3 scripts/devops_pro.py helm package --chart-dir ./charts/my-app
python3 scripts/devops_pro.py helm push --chart my-app-1.0.0.tgz

# Kustomize
python3 scripts/devops_pro.py kustomize init --base ./base/ --overlays "dev,prod"
python3 scripts/devops_pro.py kustomize build --overlay prod

# 策略校验
python3 scripts/devops_pro.py validate --file ./manifests/ --policies "require_limits"

# GitOps
python3 scripts/devops_pro.py gitops sync --app my-app --cluster production

# CRD管理
python3 scripts/devops_pro.py crd generate --definition ./crd-spec.yaml
python3 scripts/devops_pro.py crd install --file ./crd.yaml
```

## 示例

### PRO企业级配置

```yaml
pro_config:
  helm:
    repo: "https://harbor.example.com/chartrepo"
    username: "${HELM_USER}"
    password: "${HELM_PASS}"
    sign: true                     # Chart签名

  kustomize:
    overlays:
      - name: "dev"
        patches: ["replicas:1", "resources:small"]
      - name: "staging"
        patches: ["replicas:2", "resources:medium"]
      - name: "prod"
        patches: ["replicas:5", "resources:large", "hpa:enabled"]

  validation:
    engine: "kyverno"              # kyverno | opa
    policies:
      - require_resource_limits
      - disallow_latest_tag
      - require_namespace_labels
      - restrict_privileged
      - require_security_context
    block_on_fail: true            # 校验失败阻止部署

  gitops:
    engine: "argocd"
    repo: "https://git.example.com/k8s-manifests"
    auto_sync: true
    auto_prune: true

  templates:
    governance: true               # 模板治理
    versioning: true               # 版本化
    approval: true                 # 模板需审批

  cicd:
    pipeline: "gitlab-ci"         # gitlab-ci | github-actions | jenkins
    stages: ["lint", "validate", "build", "deploy"]
    environments: ["dev", "staging", "prod"]
```

## 最佳实践

### PRO版企业实践

| 实践领域 | 建议做法 |
| --- | --- |
| Helm管理 | Chart版本与应用版本一致，签名后发布 |
| Kustomize | base保持通用，overlay做环境差异化 |
| 策略校验 | CI流水线中强制校验，失败即阻止 |
| GitOps | 所有变更通过Git，ArgoCD自动同步 |
| 模板治理 | 模板需审批后才能使用 |

### 免费版兼容性

```text
免费版命令 → PRO版命令（增强）：
generate.py deployment  → devops_pro.py helm create (Helm Chart)
generate.py stack       → devops_pro.py kustomize build (多环境)
基础校验                 → +策略合规+GitOps+CRD
```

## 常见问题

### Q1：Helm和Kustomize该用哪个？

Helm适合打包发布完整应用（含模板化变量）；Kustomize适合多环境覆盖（无模板化）。两者可结合使用：Helm打包基础Chart，Kustomize做环境覆盖。

### Q2：策略校验支持什么规则？

支持资源限制检查、镜像标签检查、标签规范、安全上下文、特权模式检查等。可通过Kyverno或OPA编写自定义策略。

### Q3：GitOps如何集成？

PRO版生成Git仓库结构（base+overlays），ArgoCD/Flux监控Git仓库变更并自动同步到集群。所有部署通过Git提交触发。

### Q4：支持私有Helm仓库吗？

支持。PRO版兼容Harbor、ChartMuseum等私有Helm仓库。支持认证访问与Chart签名验证。

### Q5：模板治理如何工作？

企业级模板需经过审批后才能使用。模板版本化管理，变更需评审。确保团队使用经过验证的标准化模板。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.9+
- **Helm**: 3.0+（Chart管理需要）
- **kubectl**: 可选（部署验证需要）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| PyYAML | Python库 | 必需 | `pip install pyyaml` |
| jsonschema | Python库 | 必需 | `pip install jsonschema` |
| helm | CLI工具 | 可选 | 官网安装 |
| kustomize | CLI工具 | 可选 | 官网安装 |

### API Key 配置

| 服务 | 环境变量 | 是否必需 | 用途 |
|:-------|:---------|:---------|:-----|
| Harbor | `HELM_USER`/`HELM_PASS` | 可选 | 私有Chart仓库 |
| ArgoCD | `ARGOCD_TOKEN` | 可选 | GitOps集成 |
| Git | `GIT_TOKEN` | 可选 | 仓库访问 |

- 未配置的服务自动跳过
- 所有凭证存储在本地配置文件

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本+Helm执行）
- **说明**: 企业级K8s清单管理平台，支持Helm/Kustomize与GitOps
- **PRO版特性**: Helm Chart、Kustomize、策略校验、多环境、GitOps、CRD、模板治理
- **兼容性**: 完全兼容免费版清单生成命令

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |
