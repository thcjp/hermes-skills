---
slug: agent-framework-azure-ai-py
name: agent-framework-azure-ai-py
version: "0.1.0"
displayName: Agent Framework Azure Ai Py
summary: This is a documentation-only skill for building Azure AI Foundry agents;
  its cloud, web search, M...
license: MIT
description: |-
  This is a documentation-only skill for building Azure AI Foundry agents;
  its cloud, web search, M...

  核心能力:

  - 研究工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 数据研究、文献分析、信息收集

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: documentation, azure, building, framework, agent, skill
tags:
- Research
- Development
tools:
- read
- exec
---

# Agent Framework Azure Ai Py

Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK.

## Architecture

```text
User Query → AzureAIAgentsProvider → Azure AI Agent Service (Persistent)
                    ↓
              Agent.run() / Agent.run_stream()
                    ↓
              Tools: Functions | Hosted (Code/Search/Web) | MCP
                    ↓
              AgentThread (conversation persistence)
```

## Installation

```bash
pip install agent-framework --pre

pip install agent-framework-azure-ai --pre
```

## Environment Variables

```bash
export AZURE_AI_PROJECT_ENDPOINT="https://<project>.services.ai.azure.com/api/projects/<project-id>"
export AZURE_AI_MODEL_DEPLOYMENT_NAME="gpt-4o-mini"
export BING_CONNECTION_ID="your-bing-connection-id"  # For web search
```

## Authentication

```python
from azure.identity.aio import AzureCliCredential, DefaultAzureCredential

credential = AzureCliCredential()

credential = DefaultAzureCredential()
```

## Core Workflow

### Basic Agent

```python
import asyncio
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="MyAgent",
            instructions="You are a helpful assistant.",
        )

        result = await agent.run("Hello!")
        print(result.text)

asyncio.run(main())
```

### Agent with Function Tools

```python
from typing import Annotated
from pydantic import Field
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

def get_weather(
    location: Annotated[str, Field(description="City name to get weather for")],
) -> str:
    """Get the current weather for a location."""
    return f"Weather in {location}: 72°F, sunny"

def get_current_time() -> str:
    """Get the current UTC time."""
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="WeatherAgent",
            instructions="You help with weather and time queries.",
            tools=[get_weather, get_current_time],  # Pass functions directly
        )

        result = await agent.run("What's the weather in Seattle?")
        print(result.text)
```

### Agent with Hosted Tools

```python
from agent_framework import (
    HostedCodeInterpreterTool,
    HostedFileSearchTool,
    HostedWebSearchTool,
)
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="MultiToolAgent",
            instructions="You can execute code, search files, and search the web.",
            tools=[
                HostedCodeInterpreterTool(),
                HostedWebSearchTool(name="Bing"),
            ],
        )

        result = await agent.run("Calculate the factorial of 20 in Python")
        print(result.text)
```

### Streaming Responses

```python
async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="StreamingAgent",
            instructions="You are a helpful assistant.",
        )

        print("Agent: ", end="", flush=True)
        async for chunk in agent.run_stream("Tell me a short story"):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print()
```

### Conversation Threads

```python
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="ChatAgent",
            instructions="You are a helpful assistant.",
            tools=[get_weather],
        )

        # Create thread for conversation persistence
        thread = agent.get_new_thread()

        # First turn
        result1 = await agent.run("What's the weather in Seattle?", thread=thread)
        print(f"Agent: {result1.text}")

        # Second turn - context is maintained
        result2 = await agent.run("What about Portland?", thread=thread)
        print(f"Agent: {result2.text}")

        # Save thread ID for later resumption
        print(f"Conversation ID: {thread.conversation_id}")
```

### Structured Outputs

```python
from pydantic import BaseModel, ConfigDict
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

class WeatherResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    location: str
    temperature: float
    unit: str
    conditions: str

async def main():
    async with (
        AzureCliCredential() as credential,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="StructuredAgent",
            instructions="Provide weather information in structured format.",
            response_format=WeatherResponse,
        )

        result = await agent.run("Weather in Seattle?")
        weather = WeatherResponse.model_validate_json(result.text)
        print(f"{weather.location}: {weather.temperature}°{weather.unit}")
```

## Provider Methods

| Method | Description |
| --- | --- |
| `create_agent()` | Create new agent on Azure AI service |
| `get_agent(agent_id)` | Retrieve existing agent by ID |
| `as_agent(sdk_agent)` | Wrap SDK Agent object (no HTTP call) |

## Hosted Tools Quick Reference

| Tool | Import | Purpose |
| --- | --- | --- |
| `HostedCodeInterpreterTool` | `from agent_framework import HostedCodeInterpreterTool` | Execute Python code |
| `HostedFileSearchTool` | `from agent_framework import HostedFileSearchTool` | Search vector stores |
| `HostedWebSearchTool` | `from agent_framework import HostedWebSearchTool` | Bing web search |
| `HostedMCPTool` | `from agent_framework import HostedMCPTool` | Service-managed MCP |
| `MCPStreamableHTTPTool` | `from agent_framework import MCPStreamableHTTPTool` | Client-managed MCP |

## Complete Example

```python
import asyncio
from typing import Annotated
from pydantic import BaseModel, Field
from agent_framework import (
    HostedCodeInterpreterTool,
    HostedWebSearchTool,
    MCPStreamableHTTPTool,
)
from agent_framework.azure import AzureAIAgentsProvider
from azure.identity.aio import AzureCliCredential

def get_weather(
    location: Annotated[str, Field(description="City name")],
) -> str:
    """Get weather for a location."""
    return f"Weather in {location}: 72°F, sunny"

class AnalysisResult(BaseModel):
    summary: str
    key_findings: list[str]
    confidence: float

async def main():
    async with (
        AzureCliCredential() as credential,
        MCPStreamableHTTPTool(
            name="Docs MCP",
            url="https://learn.microsoft.com/api/mcp",
        ) as mcp_tool,
        AzureAIAgentsProvider(credential=credential) as provider,
    ):
        agent = await provider.create_agent(
            name="ResearchAssistant",
            instructions="You are a research assistant with multiple capabilities.",
            tools=[
                get_weather,
                HostedCodeInterpreterTool(),
                HostedWebSearchTool(name="Bing"),
                mcp_tool,
            ],
        )

        thread = agent.get_new_thread()

        # Non-streaming
        result = await agent.run(
            "Search for Python best practices and summarize",
            thread=thread,
        )
        print(f"Response: {result.text}")

        # Streaming
        print("\nStreaming: ", end="")
        async for chunk in agent.run_stream("Continue with examples", thread=thread):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print()

        # Structured output
        result = await agent.run(
            "Analyze findings",
            thread=thread,
            response_format=AnalysisResult,
        )
        analysis = AnalysisResult.model_validate_json(result.text)
        print(f"\nConfidence: {analysis.confidence}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Conventions

* Always use async context managers: `async with provider:`
* Pass functions directly to `tools=` parameter (auto-converted to AIFunction)
* Use `Annotated[type, Field(description=...)]` for function parameters
* Use `get_new_thread()` for multi-turn conversations
* Prefer `HostedMCPTool` for service-managed MCP, `MCPStreamableHTTPTool` for client-managed

## Reference Files

* [references/tools.md](/api/v1/skills/agent-framework-azure-ai-py/file?path=references%2Ftools.md&ownerHandle=thegovind): Detailed hosted tool patterns
* [references/mcp.md](/api/v1/skills/agent-framework-azure-ai-py/file?path=references%2Fmcp.md&ownerHandle=thegovind): MCP integration (hosted + local)
* [references/threads.md](/api/v1/skills/agent-framework-azure-ai-py/file?path=references%2Fthreads.md&ownerHandle=thegovind): Thread and conversation management
* [references/advanced.md](/api/v1/skills/agent-framework-azure-ai-py/file?path=references%2Fadvanced.md&ownerHandle=thegovind): OpenAPI, citations, structured outputs

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
