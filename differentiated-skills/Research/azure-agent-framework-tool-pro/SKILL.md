---
slug: azure-agent-framework-tool-pro
name: azure-agent-framework-tool-pro
version: "1.0.0"
displayName: Azure智能体框架工具-专业版
summary: 企业级Azure AI智能体编排,支持批量管理、MCP工具集成、监控告警与多租户隔离
license: MIT
edition: pro
description: |-
  企业级 Azure AI Foundry 智能体编排工具,在免费版核心能力之上,提供智能体批量管理、
  MCP工具深度集成、监控告警、多租户隔离、CI/CD 集成与团队协作能力。

  核心能力:
  - 免费版全部能力(完全兼容)
  - 智能体批量管理与版本控制
  - MCP工具深度集成(托管与客户端模式)
  - 监控指标采集与告警通知
  - 多租户隔离与权限管理
  - CI/CD 集成与自动化部署

  适用场景:
  - 企业级智能体编排与部署
  - 多智能体协作工作流
  - 生产环境监控与运维
  - 团队协作与版本管理

  差异化:专业版面向团队与企业,提供批量管理、监控、多租户等高阶能力,并保持与免费版完全兼容。

  触发关键词: Azure, AI Foundry, 智能体编排, MCP工具, 批量管理, 监控告警, 多租户
tags:
- 研究工具
- AI开发
- 智能体
- 企业级
tools:
- read
- exec
---

# Azure智能体框架工具(专业版)

## 概述

本工具是企业级 Azure AI Foundry 智能体编排工具,在免费版核心能力之上,扩展了智能体批量管理、MCP工具深度集成、监控告警、多租户隔离、CI/CD 集成与团队协作能力,适合企业级智能体编排、多智能体协作工作流、生产环境监控与运维场景。专业版与免费版完全兼容:免费版的所有代码、工作流均可直接在专业版中使用。

### 免费版 vs 专业版对比

| 能力 | 免费版 | 专业版 |
|:-----|:------|:------|
| 基础智能体创建 | 支持 | 支持 |
| 函数工具集成 | 支持 | 支持 |
| 托管工具(代码/搜索/Web) | 支持 | 支持 |
| 流式响应与会话线程 | 支持 | 支持 |
| 结构化输出 | 支持 | 支持 |
| 智能体批量管理 | 不支持 | 支持 |
| MCP工具深度集成 | 基础 | 高级(托管+客户端) |
| 监控告警 | 不支持 | 支持 |
| 多租户隔离 | 不支持 | 支持 |
| CI/CD 集成 | 不支持 | 支持 |
| 版本控制与回滚 | 不支持 | 支持 |
| 优先技术支持 | 不支持 | 支持 |

## 核心能力

### 1. 智能体批量管理(专业版新增)

```python
import asyncio
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import DefaultAzureCredential

async def manage_agents():
    async with (
        DefaultAzureCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        # 批量创建智能体
        agent_configs = [
            {"name": "客服助手", "instructions": "处理客户咨询...", "tools": [faq_tool]},
            {"name": "数据分析助手", "instructions": "分析业务数据...", "tools": [query_tool, chart_tool]},
            {"name": "文档助手", "instructions": "文档检索与问答...", "tools": [search_tool]},
        ]

        agents = []
        for config in agent_configs:
            agent = await provider.create_agent(**config)
            agents.append(agent)
            print(f"已创建: {agent.id} - {config['name']}")

        # 批量查询
        all_agents = await provider.list_agents()
        for a in all_agents:
            print(f"ID: {a.id}, 名称: {a.name}")

asyncio.run(manage_agents())
```

### 2. MCP工具深度集成(专业版增强)

```python
import asyncio
from agent_framework import (
    HostedMCPTool,           # 服务端托管 MCP工具
    MCPStreamableHTTPTool,    # 客户端管理 MCP server
)
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import DefaultAzureCredential

async def main():
    async with (
        DefaultAzureCredential() as credential,
        MCPStreamableHTTPTool(
            name="文档服务",
            url="https://docs.example.com/api/mcp",
        ) as mcp_tool,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="ResearchAssistant",
            instructions="你是一个研究助手,具备多种能力。",
            tools=[
                mcp_tool,                    # 客户端管理的 MCP server
                HostedMCPTool(               # 服务端托管的 MCP工具
                    name="知识库",
                    url="https://kb.example.com/mcp",
                ),
            ],
        )

        result = await agent.run("搜索 Python 最佳实践并总结")
        print(result.text)

asyncio.run(main())
```

### 3. 监控指标采集(专业版新增)

```python
import asyncio
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import DefaultAzureCredential

async def monitored_agent():
    async with (
        DefaultAzureCredential() as credential,
        AzureAIAgentsProvider(
            credential=credential,
            metrics_enabled=True,           # 启用指标采集
            metrics_export_interval=60,     # 导出间隔(秒)
        ) as provider,
    ):
        agent = await provider.create_agent(
            name="MonitoredAgent",
            instructions="你是一个乐于助人的助手。",
        )

        # 执行任务(自动采集指标)
        result = await agent.run("分析最近一周的销售数据")

        # 导出指标
        metrics = await provider.export_metrics(format="prometheus")
        print(metrics)
        # 指标示例:
        # agent_requests_total{agent="MonitoredAgent",status="success"} 1
        # agent_response_time_p95{agent="MonitoredAgent"} 2.5
        # agent_tool_calls_total{tool="query_tool"} 3

asyncio.run(monitored_agent())
```

### 4. 多租户隔离(专业版新增)

```python
import asyncio
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import DefaultAzureCredential

async def multi_tenant():
    # 为不同租户(团队/客户)创建隔离的智能体空间
    tenants = ["acme", "globex", "initech"]

    for tenant in tenants:
        async with (
            DefaultAzureCredential() as credential,
            AzureAIAgentsProvider(
                credential=credential,
                workspace=tenant,           # 租户隔离
            ) as provider,
        ):
            agent = await provider.create_agent(
                name=f"{tenant}-assistant",
                instructions=f"你是 {tenant} 公司的专属助手。",
            )
            print(f"[{tenant}] 智能体已创建: {agent.id}")

asyncio.run(multi_tenant())
```

## 使用场景

### 场景一:多智能体协作工作流

编排多个智能体协作完成复杂任务。

```python
#!/usr/bin/env python3
"""多智能体协作工作流示例"""
import asyncio
from typing import Annotated
from pydantic import BaseModel, Field
from agent_framework import HostedWebSearchTool, HostedCodeInterpreterTool
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import DefaultAzureCredential

class ResearchResult(BaseModel):
    summary: str
    key_findings: list[str]
    confidence: float

async def collaborative_workflow():
    async with (
        DefaultAzureCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        # 研究员智能体:负责信息收集
        researcher = await provider.create_agent(
            name="Researcher",
            instructions="你负责收集和整理信息。使用Web搜索获取最新数据。",
            tools=[HostedWebSearchTool(name="Bing")],
        )

        # 分析师智能体:负责数据分析
        analyst = await provider.create_agent(
            name="Analyst",
            instructions="你负责数据分析。使用代码解释器进行计算。",
            tools=[HostedCodeInterpreterTool()],
        )

        # 写手智能体:负责报告撰写
        writer = await provider.create_agent(
            name="Writer",
            instructions="你负责将研究和分析结果整理成报告。",
            response_format=ResearchResult,
        )

        # 协作流程
        thread = researcher.get_new_thread()

        # 步骤1:研究员收集信息
        research = await researcher.run(
            "研究 2026 年 AI 智能体市场趋势", thread=thread
        )
        print(f"[研究] {research.text[:200]}...")

        # 步骤2:分析师分析数据
        analysis = await analyst.run(
            f"基于以下研究结果进行数据分析: {research.text}", thread=thread
        )
        print(f"[分析] {analysis.text[:200]}...")

        # 步骤3:写手生成报告
        report = await writer.run(
            f"基于以下研究和分析生成报告: 研究={research.text}, 分析={analysis.text}",
            thread=thread,
            response_format=ResearchResult,
        )
        result = ResearchResult.model_validate_json(report.text)
        print(f"\n[报告] 置信度: {result.confidence}")
        print(f"关键发现: {result.key_findings}")

asyncio.run(collaborative_workflow())
```

### 场景二:生产环境监控与告警

部署智能体到生产环境,实时监控并告警。

```python
#!/usr/bin/env python3
"""生产环境智能体监控示例"""
import asyncio
import json
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import DefaultAzureCredential

async def production_monitor():
    async with (
        DefaultAzureCredential() as credential,
        AzureAIAgentsProvider(
            credential=credential,
            metrics_enabled=True,
            alert_webhook="https://hooks.example.com/alerts",
            alert_on_failure=True,
            alert_on_latency_p95=5.0,       # P95 延迟超5秒告警
            alert_on_error_rate=5.0,        # 错误率超5%告警
        ) as provider,
    ):
        # 部署生产智能体
        agent = await provider.create_agent(
            name="ProductionAgent",
            instructions="你是生产环境的客户服务助手。",
            tools=[faq_tool, search_tool],
        )

        # 模拟生产流量
        queries = [
            "如何重置密码?",
            "查询订单状态",
            "退款流程是什么?",
        ]

        for query in queries:
            try:
                result = await agent.run(query)
                print(f"[OK] {query} -> {result.text[:50]}...")
            except Exception as e:
                print(f"[FAIL] {query} -> {e}")
                # 告警自动触发

        # 导出监控指标
        metrics = await provider.export_metrics(format="json")
        with open("metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)
        print("\n指标已导出到 metrics.json")

asyncio.run(production_monitor())
```

### 场景三:CI/CD 集成与自动化部署

将智能体部署嵌入 CI/CD 流水线,实现自动化测试与发布。

```bash
#!/bin/bash
# deploy-agent.sh - CI/CD 智能体部署
set -e

ENVIRONMENT="${1:-staging}"
AGENT_CONFIG="agents/production.yaml"

echo "部署智能体到 ${ENVIRONMENT} 环境..."

# 1. 运行测试
python tests/test_agent.py

# 2. 部署智能体
python deploy.py --config "$AGENT_CONFIG" --env "$ENVIRONMENT"

# 3. 健康检查
python healthcheck.py --env "$ENVIRONMENT" --timeout 60

# 4. 导出指标基线
python export_metrics.py --env "$ENVIRONMENT" --output "baselines/${ENVIRONMENT}_$(date +%Y%m%d).json"

echo "部署完成: ${ENVIRONMENT}"
```

```python
# deploy.py 核心逻辑示例
import asyncio
import yaml
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import DefaultAzureCredential

async def deploy(config_path, environment):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    async with (
        DefaultAzureCredential() as credential,
        AzureAIAgentsProvider(
            credential=credential,
            workspace=environment,           # 按环境隔离
            metrics_enabled=True,
        ) as provider,
    ):
        # 版本化创建(支持回滚)
        agent = await provider.create_agent(
            name=config["name"],
            instructions=config["instructions"],
            tools=config.get("tools", []),
            version=config["version"],       # 版本控制
        )
        print(f"已部署 {agent.name} v{config['version']} 到 {environment}")
        print(f"智能体 ID: {agent.id}")

asyncio.run(deploy("agents/production.yaml", "staging"))
```

## 快速开始

### 1. 安装与初始化

```bash
pip install agent-framework --pre
pip install agent-framework-azure-ai --pre

# 专业版初始化(可选)
python -m agent_framework pro init
python -m agent_framework config set metrics.enabled true
python -m agent_framework config set alerts.webhook "https://hooks.example.com/alerts"
```

### 2. 企业级配置

```bash
# 配置环境变量
export AZURE_AI_PROJECT_ENDPOINT="https://<project>.services.ai.azure.com/api/projects/<project-id>"
export AZURE_AI_MODEL_DEPLOYMENT_NAME="gpt-4o-mini"
export AGENT_FRAMEWORK_EDITION="pro"
export AGENT_FRAMEWORK_METRICS_ENABLED="true"
export AGENT_FRAMEWORK_ALERT_WEBHOOK="https://hooks.example.com/alerts"
```

## 配置示例

### 企业级配置文件

```yaml
# ~/.agent-framework/config.yaml
edition: pro
metrics:
  enabled: true
  export_interval: 60
  format: prometheus
  export_endpoint: https://prometheus.example.com/push
alerts:
  webhook: https://hooks.example.com/alerts
  on_failure: true
  on_latency_p95: 5.0
  on_error_rate: 5.0
workspace:
  default: production
  isolation: strict
deployment:
  version_control: true
  rollback_enabled: true
  max_versions: 10
agents:
  max_concurrent: 50
  default_timeout: 300
```

### 监控指标示例

```bash
# 导出 Prometheus 格式指标
python -m agent_framework metrics export --format prometheus

# 指标示例:
# agent_requests_total{agent="ProductionAgent",status="success"} 1024
# agent_requests_total{agent="ProductionAgent",status="failed"} 12
# agent_response_time_p95{agent="ProductionAgent"} 2.3
# agent_tool_calls_total{agent="ProductionAgent",tool="search"} 256
# agent_active_threads 18
```

## 最佳实践

### 智能体编排
1. **单一职责**:每个智能体专注一个领域,通过多智能体协作处理复杂任务。
2. **版本控制**:为智能体配置版本号,便于回滚与灰度发布。
3. **线程复用**:对话线程跨智能体共享,保持完整上下文。
4. **结构化交接**:智能体间用 Pydantic 模型传递结构化数据。

### 生产运维
1. **监控告警**:启用指标采集,设置延迟与错误率告警阈值。
2. **多环境隔离**:开发/预发/生产使用不同 workspace。
3. **健康检查**:部署后执行健康检查,确认智能体可用。
4. **指标基线**:记录正常指标基线,便于异常检测。

### 安全规范
1. **托管标识**:生产环境用托管标识替代 API Key。
2. **最小权限**:每个智能体仅授予所需工具与数据权限。
3. **审计日志**:启用操作审计,留存智能体调用记录。
4. **数据脱敏**:智能体处理的数据及时脱敏存储。

## 常见问题

### Q1: 专业版是否兼容免费版代码?
完全兼容。免费版的所有代码、SDK 调用、工作流均可直接在专业版中运行。专业版仅在原有能力之上扩展高阶特性。

### Q2: 如何从免费版升级?
```bash
python -m agent_framework pro init --migrate
```
升级过程保留全部历史智能体与配置。

### Q3: 多智能体协作如何编排?
使用共享的 `AgentThread` 在多个智能体间传递上下文。每个智能体专注单一职责,通过结构化输出(Pydantic 模型)传递中间结果。

### Q4: 监控指标如何接入现有系统?
专业版支持 Prometheus 与 JSON 两种导出格式,可推送到 Prometheus/Grafana、Datadog 或自建看板。通过 `metrics.export_endpoint` 配置推送地址。

### Q5: 多租户数据如何隔离?
使用 `workspace` 参数为不同租户(团队/客户)分配独立智能体空间,智能体、线程、配置均按租户隔离。

### Q6: 如何实现灰度发布?
1. 为智能体配置版本号
2. 新版本先部署到预发环境测试
3. 按流量比例逐步切换到新版本
4. 异常时通过 `rollback` 快速回滚

## 与免费版的兼容性

| 维度 | 兼容性 |
|:-----|:------|
| SDK 调用 | 100% 兼容 |
| 代码工作流 | 100% 兼容(无需修改即可运行) |
| 智能体配置 | 100% 兼容(专业版可管理免费版智能体) |
| 会话线程 | 100% 兼容(线程可跨版本使用) |
| 升级路径 | 平滑升级(保留全部历史数据) |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: >= 3.10

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| agent-framework(pro) | Python 包 | 必需 | `pip install agent-framework --pre` |
| agent-framework-azure-ai | Python 包 | 必需 | `pip install agent-framework-azure-ai --pre` |
| azure-identity | Python 包 | 必需 | 随 agent-framework-azure-ai 安装 |
| Azure CLI | 命令行工具 | 推荐 | 官方安装(用于认证) |
| Azure AI Foundry | 云服务 | 必需 | Azure 订阅 |
| PyYAML | Python 包 | 可选 | `pip install pyyaml`(配置文件) |
| 监控系统 | 可观测性 | 可选 | Prometheus / Grafana |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 配置 `AZURE_AI_PROJECT_ENDPOINT`:Azure AI Foundry 项目端点
- 配置 `AZURE_AI_MODEL_DEPLOYMENT_NAME`:模型部署名称
- 配置 `BING_CONNECTION_ID`:Web 搜索连接 ID(可选)
- 认证:生产环境用托管标识,开发环境用 Azure CLI
- 监控告警:配置 `alerts.webhook` 通知地址

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
- **版本**: 专业版(兼容免费版全部能力)
