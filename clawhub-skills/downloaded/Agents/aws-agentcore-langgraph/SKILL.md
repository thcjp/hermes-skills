---
slug: aws-agentcore-langgraph
name: aws-agentcore-langgraph
version: "1.0.2"
displayName: aws-agentcore-langgraph
summary: This skill is a coherent AWS AgentCore/LangGraph deployment aid, but users
  should treat its cloud...
license: MIT
description: |-
  This skill is a coherent AWS AgentCore/LangGraph deployment aid, but
  users should treat its cloud...

  核心能力:

  - 智能代理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - AI代理增强、记忆管理、自主决策

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: aws-agentcore-langgraph, aws, coherent, agentcore, langgraph, skill
tags:
- Agents
- Operations
tools:
- read
- exec
---

# aws-agentcore-langgraph

Multi-agent systems on AWS Bedrock AgentCore with LangGraph orchestration. Source: <https://github.com/aws/bedrock-agentcore-starter-toolkit>

## Install

```bash
pip install bedrock-agentcore bedrock-agentcore-starter-toolkit langgraph
uv tool install bedrock-agentcore-starter-toolkit  # installs agentcore CLI
```

## Quick Start

```python
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition  # routing + tool execution
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from typing import Annotated
from typing_extensions import TypedDict

class State(TypedDict):
    messages: Annotated[list, add_messages]

builder = StateGraph(State)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools))  # prebuilt tool executor
builder.add_conditional_edges("agent", tools_condition)  # routes to tools or END
builder.add_edge(START, "agent")
graph = builder.compile()

app = BedrockAgentCoreApp()  # Wraps as HTTP service on port 8080 (/invocations, /ping)
@app.entrypoint
def invoke(payload, context):
    result = graph.invoke({"messages": [("user", payload.get("prompt", ""))]})
    return {"result": result["messages"][-1].content}
app.run()
```

## CLI Commands

| Command | Purpose |
| --- | --- |
| `agentcore configure -e agent.py --region us-east-1` | Setup |
| `agentcore configure -e agent.py --region us-east-1 --name my_agent --non-interactive` | Scripted setup |
| `agentcore launch --deployment-type container` | Deploy (container mode) |
| `agentcore launch --disable-memory` | Deploy without memory subsystem |
| `agentcore dev` | Hot-reload local dev server |
| `agentcore invoke '{"prompt": "Hello"}'` | Test |
| `agentcore destroy` | Cleanup |

## Core Patterns

### Multi-Agent Orchestration

* Orchestrator delegates to specialists (customer service, e-commerce, healthcare, financial, etc.)
* Specialists: inline functions or separate deployed agents; all share `session_id` for context

### Memory (STM/LTM)

```python
from bedrock_agentcore.memory import MemoryClient
memory = MemoryClient()
memory.create_event(session_id, actor_id, event_type, payload)  # Store
events = memory.list_events(session_id)  # Retrieve (returns list)
```

* **STM**: Turn-by-turn within session | **LTM**: Facts/decisions across sessions/agents
* ~10s eventual consistency after writes

### Gateway Tools

```bash
python -m bedrock_agentcore.gateway.deploy --stack-name my-agents --region us-east-1
```

```python
from bedrock_agentcore.gateway import GatewayToolClient
gateway = GatewayToolClient()
result = gateway.call("tool_name", param1=value1, param2=value2)
```

* Transport: Fallback Mock (local), Local MCP servers, Production Gateway (Lambda/REST/MCP)
* Auto-configures `BEDROCK_AGENTCORE_GATEWAY_URL` after deploy

## Decision Tree

```text
Multiple agents coordinating? → Orchestrator + specialists pattern
Persistent cross-session memory? → AgentCore Memory (not LangGraph checkpoints)
External APIs/Lambda? → AgentCore Gateway
Single agent, simple? → Quick Start above
Complex multi-step logic? → StateGraph + tools_condition + ToolNode
```

## Key Concepts

* **AgentCore Runtime**: HTTP service on port 8080 (handles `/invocations`, `/ping`)
* **AgentCore Memory**: Managed cross-session/cross-agent memory
* **LangGraph Routing**: `tools_condition` for agent→tool routing, `ToolNode` for execution
* **AgentCore Gateway**: Transforms APIs/Lambda into MCP tools with auth

## Naming Rules

* Start with letter, only letters/numbers/underscores, 1-48 chars: `my_agent` not `my-agent`

## Troubleshooting

| Issue | Fix |
| --- | --- |
| `on-demand throughput isn't supported` | Use `us.anthropic.claude-*` inference profiles |
| `Model use case details not submitted` | Fill Anthropic form in Bedrock Console |
| `Invalid agent name` | Use underscores not hyphens |
| Memory empty after write | Wait ~10s (eventual consistency) |
| Container not reading .env | Set ENV in Dockerfile, not .env |
| Memory not working after deploy | Check logs for "Memory enabled/disabled" |
| `list_events` returns empty | Check actor_id/session_id match; `event['payload']` is a list |
| Gateway "Unknown tool" | Lambda must strip `___` prefix from `bedrockAgentCoreToolName` |
| Platform mismatch warning | Normal - CodeBuild handles ARM64 cross-platform builds |

## References

* [agentcore-cli.md](/api/v1/skills/aws-agentcore-langgraph/file?path=references%2Fagentcore-cli.md&ownerHandle=killerapp) - CLI commands, deployment, lifecycle
* [agentcore-runtime.md](/api/v1/skills/aws-agentcore-langgraph/file?path=references%2Fagentcore-runtime.md&ownerHandle=killerapp) - Streaming, async, observability
* [agentcore-memory.md](/api/v1/skills/aws-agentcore-langgraph/file?path=references%2Fagentcore-memory.md&ownerHandle=killerapp) - STM/LTM patterns, API reference
* [agentcore-gateway.md](/api/v1/skills/aws-agentcore-langgraph/file?path=references%2Fagentcore-gateway.md&ownerHandle=killerapp) - Tool integration, MCP, Lambda
* [langgraph-patterns.md](/api/v1/skills/aws-agentcore-langgraph/file?path=references%2Flanggraph-patterns.md&ownerHandle=killerapp) - StateGraph design, routing
* [reference-architecture-advertising-agents-use-case.pdf](/api/v1/skills/aws-agentcore-langgraph/file?path=references%2Freference-architecture-advertising-agents-use-case.pdf&ownerHandle=killerapp) - Example multi-agent architecture

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
