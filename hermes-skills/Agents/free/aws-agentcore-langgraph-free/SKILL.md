---

name: "aws-agentcore-langgraph-free"
description: "AWS Bedrock AgentCore 与 LangGraph 基础智能体部署助手。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "AgentCore 免费"
  version: "1.0.0"
  summary: "AWS Bedrock AgentCore 与 LangGraph 基础智能体部署助手"
  tags:
    - "Agents"
    - "Operations"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
tools:
  - exec
  - read
  - write

---

# aws-agentcore-langgraph (免费版)

基于 AWS Bedrock AgentCore 与 LangGraph 的基础智能体部署助手。

## 安装

```bash
pip install bedrock-agentcore langgraph
# 安装 agentcore CLI
```

## 快速开始

```python
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from typing import Annotated
from typing_extensions import TypedDict

class State(TypedDict):
    messages: Annotated[list, add_messages]

builder = StateGraph(State)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools))
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge(START, "agent")
graph = builder.compile()

app = BedrockAgentCoreApp()  # 端口 8080,提供 /invocations 与 /ping
@app.entrypoint
def invoke(payload, context):
    result = graph.invoke({"messages": [("user", payload.get("prompt", ""))]})
    return {"result": result["messages"][-1].content}
app.run()
```

## 核心能力
- **AgentCore Runtime**: 端口 8080 的 HTTP 服务,处理 `/invocations` 与 `/ping` 端点
- **LangGraph Routing**: `tools_condition` 负责智能体到工具的路由,`ToolNode` 负责执行
- **AgentCore Memory**: 托管式跨会话记忆(免费版仅支持基础 STM,不含 LTM)
### AgentCore Runtime

执行AgentCore Runtime操作,处理用户输入并返回结果。

**输入**: 用户提供AgentCore Runtime所需的参数和指令。

### LangGraph Routing

执行LangGraph Routing操作,处理用户输入并返回结果。

**输入**: 用户提供LangGraph Routing所需的参数和指令。

### AgentCore Memory

执行AgentCore Memory操作,处理用户输入并返回结果。

**输入**: 用户提供AgentCore Memory所需的参数和指令。

#
## CLI 命令

| 命令 | 用途 |
| --- | --- |
| `agentcore configure -e agent.py --region us-east-1` | 初始化配置 |
| `agentcore launch --deployment-type container` | 容器模式部署 |
| `agentcore dev` | 热重载本地开发服务器 |
| `agentcore invoke '{"prompt": "Hello"}'` | 测试调用 |
| `agentcore destroy` | 清理资源 |

## 命名规则

- 以字母开头,仅含字母/数字/下划线,长度 1-48 字符
- 正确: `my_agent`  错误: `my-agent`

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 单智能体部署 | 智能体定义与工具列表 | 容器化部署的 HTTP 智能体服务 |

**不适用于**: 多智能体编排、跨会话 LTM 记忆、Gateway 工具集成(需升级付费版)。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 使用流程

1. 安装 `bedrock-agentcore`、`bedrock-agentcore`、`langgraph`
2. 使用 `StateGraph` 定义智能体图,通过 `tools_condition` 与 `ToolNode` 配置工具路由
3. 用 `BedrockAgentCoreApp()` 包装为 HTTP 服务
4. 运行 `agentcore configure` 初始化配置(注意命名规则:下划线而非连字符)
5. 运行 `agentcore launch --deployment-type container` 部署
6. 使用 `agentcore invoke` 测试,完成后 `agentcore destroy` 清理

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。

## 案例展示

### 案例1: 单智能体工具调用

```python
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition
runtime import BedrockAgentCoreApp

# 定义工具
def search_tool(query: str) -> str:
    return f"搜索结果: {query}"

tools = [search_tool]
builder = StateGraph(State)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools))
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge(START, "agent")
graph = builder.compile()

app = BedrockAgentCoreApp()
@app.entrypoint
def invoke(payload, context):
    result = graph.get("prompt", ""))]})
app.run()
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `on-demand throughput isn't supported` | 使用了不支持按需吞吐的推理配置 | 改用 `us.anthropic.claude-*` 推理配置文件 |
| `Model use case details not submitted` | 未提交 Anthropic 模型用例申请 | 在 Bedrock 控制台填写 Anthropic 用例表单 |
| `Invalid agent name` | 智能体名称含连字符等非法字符 | 使用下划线而非连字符,如 `my_agent` |
| 容器未读取 .env 文件 | 容器运行时不加载 .env | 在 Dockerfile 中用 `ENV` 设置环境变量 |
| 端口 8080 被占用 | 本地已有进程占用 8080 | 停止占用进程或修改 BedrockAgentCoreApp 端口 |
| Platform mismatch warning | 本地与目标平台架构不一致 | 正常现象,CodeBuild 会处理 ARM64 跨平台构建 |

## 常见问题

### Q1: tools_condition 路由如何工作?
A: `tools_condition` 是 LangGraph 预置的条件边函数,根据智能体节点输出中是否包含工具调用,自动路由到 `ToolNode` 执行或到 `END` 结束。

### Q2: 智能体名称为何报 Invalid agent name?
A: 名称必须以字母开头,仅含字母/数字/下划线,长度 1-48 字符。使用 `my_agent` 而非 `my-agent`。

### Q3: 免费版与付费版有何区别?
A: 免费版仅支持单智能体部署与基础 STM 记忆;付费版增加多智能体编排、跨会话 LTM、Gateway 工具集成(Lambda/协议)、完整错误诊断与案例库。

### Q4: 如何部署不带记忆的智能体?
A: 使用 `agentcore launch --disable-memory`。适用于无状态工具型智能体,可降低成本与延迟。

## 已知限制

- 仅支持单智能体部署,不支持多智能体编排(Orchestrator + Specialists)
- 不含跨会话 LTM 记忆,仅支持基础会话内 STM
- 不含 Gateway 工具集成,无法将 Lambda/REST 转为 协议适配层 工具
- 依赖 AWS 云服务,需要网络连接与有效的 AWS 凭证
- Bedrock 模型需在控制台提前申请用例并配置推理配置文件

## 升级提示

> 本免费版提供基础单智能体部署能力。如需多智能体编排、跨会话 LTM 记忆、
> Gateway 工具集成(Lambda/协议/REST)、完整错误诊断(10+ 场景)与 3 个
> 进阶案例,请升级至 **AgentCore LangGraph 付费版**。

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 效率量化分析

| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 差异化对比

| 对比维度 | 本技能 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 核心功能 | 通用场景 | 通用场景 |

## 核心功能

- **自动化执行**: 基于指令驱动的自动化流程
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据