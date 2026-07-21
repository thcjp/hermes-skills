---
slug: kubernetes
name: kubernetes
version: "2.1.0"
displayName: Kubernetes
summary: Kubernetes & OpenShift Platform Agent Swarm — A coordinated multi-agent system
  for cluster operat...
license: MIT-0
description: |-
  Kubernetes & OpenShift Platform Agent Swarm — A coordinated multi-agent
  system for cluster operat。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Operations
tools:
  - - read
- exec
---

# Kubernetes Agent Swarm

A multi-agent system for Kubernetes and OpenShift platform operations. Seven specialized agents work together as a coordinated swarm.

## 依赖说明

| Requirement | Required | Description |
| --- | --- | --- |
| `kubectl` | ✅ Yes | Kubernetes CLI — must be in PATH |
| `oc` | Optional | OpenShift CLI — needed for OCP/ROSA/ARO |
| `helm` | Optional | For GitOps agent Helm operations |
| `jq` | Optional | For JSON output parsing |
| `KUBECONFIG` | ✅ Yes | Cluster access via env var or `~/.kube/config` |

Optional cloud CLIs (`aws`, `az`, `gcloud`, `rosa`) — only needed for managed cluster operations.

## Installation

> 安装此Skill请参考SkillHub平台指南

Or install individual agents:

```bash
* 安装此Skill请参考SkillHub平台指南
* 安装此Skill请参考SkillHub平台指南
* 安装此Skill请参考SkillHub平台指南
* 安装此Skill请参考SkillHub平台指南
* 安装此Skill请参考SkillHub平台指南
* 安装此Skill请参考SkillHub平台指南
* 安装此Skill请参考SkillHub平台指南
```

## The Swarm — Agent Roster

| Agent | Code Name | Domain |
| --- | --- | --- |
| Orchestrator | Jarvis | Task routing, coordination, standups |
| Cluster Ops | Atlas | Cluster lifecycle, nodes, upgrades |
| GitOps | Flow | ArgoCD, Helm, Kustomize, deploys |
| Security | Shield | RBAC, policies, secrets, scanning |
| Observability | Pulse | Metrics, logs, alerts, incidents |
| Artifacts | Cache | Registries, SBOM, promotion, CVEs |
| Developer Experience | Desk | Namespaces, onboarding, support |

## How It Works

This is an **instruction-only** skill. Agents receive markdown instructions describing what commands to run and how to interpret output. No executable scripts are included — the agent translates instructions into actions using the host's installed CLI tools.

### Session Setup

Before using the swarm, establish cluster context:

```bash
kubectl cluster-info
kubectl get nodes

oc status
```

### Agent Communication

Agents communicate via @mentions in shared task comments:

```text
@Shield Please review the RBAC for payment-service v3.2 before I sync.
@Pulse Is the CPU spike related to the deployment or external traffic?
@Atlas The staging cluster needs 2 more worker nodes.
```

### Escalation Path

1. Agent detects issue
2. Agent attempts resolution within guardrails
3. If blocked → @mention another agent or escalate to human
4. P1 incidents → all relevant agents auto-notified

## Heartbeat Schedule

```text
*/5  * * * *  Atlas, Pulse, Shield     (fast response: incidents, alerts, CVEs)
*/10 * * * *  Flow, Cache              (scheduled: deploys, promotions)
*/15 * * * *  Desk, Orchestrator       (batch: onboarding, standups)
```

## Agent Capabilities

### What Agents CAN Do

* Read cluster state (`kubectl get`, `kubectl describe`, `oc get`)
* Deploy via GitOps (`argocd app sync`, Flux reconciliation)
* Create documentation and reports
* Investigate and triage incidents
* Provision standard resources (namespaces, quotas, RBAC)
* Run health checks and audits
* Query metrics and logs

### What Agents CANNOT Do (Human-in-the-Loop Required)

* Delete production resources
* Modify cluster-wide policies
* Make direct changes to secrets without rotation workflow
* Perform irreversible cluster upgrades
* Approve production deployments (can prepare, human approves)

## Key Principles

* **Roles over genericism** — Each agent has a defined domain
* **Files over mental notes** — Only files persist between sessions
* **Human-in-the-loop** — Critical actions require approval
* **Guardrails over freedom** — Define what agents can and cannot do
* **Audit everything** — Every action logged

## File Structure

```text
kubernetes/
├── SKILL.md                    # This file — combined swarm
├── AGENTS.md                   # Swarm configuration and protocols
├── skills/
│   ├── orchestrator/SKILL.md   # Jarvis — task routing
│   ├── cluster-ops/SKILL.md    # Atlas — cluster operations
│   ├── gitops/SKILL.md         # Flow — GitOps
│   ├── security/SKILL.md       # Shield — security
│   ├── observability/SKILL.md  # Pulse — monitoring
│   ├── artifacts/SKILL.md      # Cache — artifacts
│   └── developer-experience/SKILL.md  # Desk — DevEx
├── memory/MEMORY.md            # Long-term agent memory
├── working/WORKING.md          # Session progress
└── logs/LOGS.md                # Action audit trail
```

## Detailed Agent Documentation

See individual SKILL.md files for each agent's full capabilities, personality, and workflow instructions.

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

## 核心能力

- Kubernetes & OpenShift Platform Agent Swarm — A coordinated multi-agent
  system for cluster operat
- 触发关键词: kubernetes, swarm, platform, agent, openshift

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
