---
slug: aws-graph-agent
name: aws-graph-agent
version: "1.0.0"
displayName: AWS图代理
summary: Bedrock AgentCore与LangGraph编排,引导式部署,一致性处理,多代理模式库。
license: MIT
description: |-
  AWS图代理是一个基于AWS Bedrock AgentCore与LangGraph的多代理系统部署与编排辅助工具。针对传统部署"配置复杂、记忆一致性延迟、命名规则混淆、模型审批缺失、网关配置繁琐"五大痛点,构建了引导式部署模板、一致性处理模式、预检清单、多代理模式库和成本优化策略五大核心能力。

  核心能力包括:StateGraph状态图编排多代理工作流;AgentCore Runtime将代理封装为HTTP服务;AgentCore Memory管理跨会话/跨代理的短期与长期记忆;AgentCore Gateway将API/Lambda转化为Agent工具接口;agentcore CLI实现配置、部署、开发、测试、销毁全生命周期管理。

  适用场景:需要多代理协调的复杂业务系统(客服、电商、医疗、金融)、需要跨会话持久记忆的对话代理、需要将外部API集成到代理工具链的企业应用、希望在生产环境大规模部署AI代理的团队、使用LangGraph进行复杂多步逻辑编排的开发者。

  差异化亮点:相比原始版本,新增引导式部署模板(脚本化vs交互式)、预检清单(模型审批/命名规则/区域支持)、一致性处理模式(记忆写入~10s延迟的应对策略)、多代理模式库(编排器+专家/团队/手-off)、命名规则自动校验、成本优化建议、决策树快速路由、FAQ与故障排查表。

  触发关键词:AWS图代理、Bedrock AgentCore、LangGraph、多代理编排、状态图、aws-graph-agent、agentcore、state-graph
tags:
- 智能代理
- 云计算
- AWS
- 多代理系统
tools:
- read
- exec
---

# AWS图代理

基于AWS Bedrock AgentCore与LangGraph编排的多代理系统。通过StateGraph状态图定义代理工作流,AgentCore Runtime封装为HTTP服务,Memory管理持久记忆,Gateway集成外部工具。

## 安装

```bash
pip install bedrock-agentcore bedrock-agentcore-starter-toolkit langgraph
uv tool install bedrock-agentcore-starter-toolkit  # 安装agentcore CLI
```

## 预检清单(差异化,部署前必读)

部署前逐项确认,避免常见失败:

| 检查项 | 要求 | 不满足的后果 |
|--------|------|-------------|
| 模型使用审批 | 在Bedrock Console填写Anthropic表单 | `Model use case details not submitted` |
| 推理配置 | 使用 `us.anthropic.claude-*` 推理配置文件 | `on-demand throughput isn't supported` |
| 代理命名 | 字母开头,仅字母/数字/下划线,1-48字符 | `Invalid agent name` |
| 区域选择 | 选择支持AgentCore的区域(如us-east-1) | 部署失败 |
| 环境变量 | 容器中在Dockerfile设置ENV,非.env | 容器不读取.env |
| 记忆开关 | 确认是否需要记忆子系统 | 记忆功能不可用 |

## 快速开始

```python
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition  # 路由+工具执行
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from typing import Annotated
from typing_extensions import TypedDict

class State(TypedDict):
    messages: Annotated[list, add_messages]

builder = StateGraph(State)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools))  # 预置工具执行器
builder.add_conditional_edges("agent", tools_condition)  # 路由到tools或END
builder.add_edge(START, "agent")
graph = builder.compile()

app = BedrockAgentCoreApp()  # 封装为8080端口HTTP服务(/invocations, /ping)
@app.entrypoint
def invoke(payload, context):
    result = graph.invoke({"messages": [("user", payload.get("prompt", ""))]})
    return {"result": result["messages"][-1].content}
app.run()
```

## CLI命令速查

| 命令 | 用途 | 示例 |
|------|------|------|
| `agentcore configure -e agent.py --region us-east-1` | 交互式配置 | 标准设置 |
| `agentcore configure -e agent.py --region us-east-1 --name my_agent --non-interactive` | 脚本化配置 | CI/CD部署 |
| `agentcore launch --deployment-type container` | 容器模式部署 | 生产环境 |
| `agentcore launch --disable-memory` | 无记忆部署 | 无状态代理 |
| `agentcore dev` | 热重载本地开发 | 开发调试 |
| `agentcore invoke '{"prompt": "Hello"}'` | 测试调用 | 功能验证 |
| `agentcore destroy` | 清理资源 | 避免持续计费 |

## 多代理模式库(差异化)

### 模式1:编排器+专家

```
编排器代理 ──委派──→ 客服专家
         ──委派──→ 电商专家
         ──委派──→ 医疗专家
         ──委派──→ 金融专家
```
- 编排器根据意图路由到专家
- 专家可以是内联函数或独立部署的代理
- 所有代理共享 `session_id` 保持上下文

### 模式2:单一代理+工具

```
用户输入 → 代理节点 → tools_condition → ToolNode → 回到代理
                    → END(无需工具)
```
- 最简模式,适合简单场景
- `tools_condition` 自动路由
- `ToolNode` 预置工具执行

### 模式3:复杂多步逻辑

```python
builder = StateGraph(State)
builder.add_node("planner", plan_node)
builder.add_node("executor", execute_node)
builder.add_node("reviewer", review_node)
builder.add_conditional_edges("reviewer", lambda s: "executor" if s["needs_revision"] else END)
builder.add_edge(START, "planner")
builder.add_edge("planner", "executor")
builder.add_edge("executor", "reviewer")
```

## 记忆系统(STM/LTM)

```python
from bedrock_agentcore.memory import MemoryClient
memory = MemoryClient()
memory.create_event(session_id, actor_id, event_type, payload)  # 存储
events = memory.list_events(session_id)  # 检索(返回列表)
```

### 记忆类型

| 类型 | 范围 | 用途 |
|------|------|------|
| **STM(短期记忆)** | 会话内逐轮 | 当前对话上下文 |
| **LTM(长期记忆)** | 跨会话/跨代理 | 事实、决策、偏好 |

### 一致性处理模式(差异化)

记忆写入后约10秒最终一致。应对策略:

```python
import time

def write_and_verify(memory, session_id, actor_id, event_type, payload):
    """写入记忆并验证一致性"""
    memory.create_event(session_id, actor_id, event_type, payload)

    # 等待最终一致性(~10s)
    time.sleep(10)

    # 验证写入
    events = memory.list_events(session_id)
    if not events:
        # 重试逻辑
        memory.create_event(session_id, actor_id, event_type, payload)
        time.sleep(5)

    return memory.list_events(session_id)
```

**注意事项:**
- `list_events` 返回空时,先等待10秒再重试
- `event['payload']` 是列表类型
- 确认 `actor_id` 和 `session_id` 匹配
- 检查日志中"Memory enabled/disabled"确认记忆已启用

## 网关工具

```bash
python -m bedrock_agentcore.gateway.deploy --stack-name my-agents --region us-east-1
```

```python
from bedrock_agentcore.gateway import GatewayToolClient
gateway = GatewayToolClient()
result = gateway.call("tool_name", param1=value1, param2=value2)
```

### 传输模式

| 模式 | 场景 | 说明 |
|------|------|------|
| Fallback Mock | 本地开发 | 模拟工具响应 |
| Local 工具协议 | 本地工具协议服务器 | 本地工具集成 |
| Production Gateway | 生产环境 | Lambda/REST/工具协议生产工具 |

部署后自动配置 `BEDROCK_AGENTCORE_GATEWAY_URL`。

### Gateway工具注意事项

- Lambda必须从 `bedrockAgentCoreToolName` 中去除 `___` 前缀
- 否则返回"Unknown tool"错误

## 决策树(快速路由)

```text
多代理协调? → 编排器+专家模式
跨会话持久记忆? → AgentCore Memory(非LangGraph checkpoints)
外部API/Lambda? → AgentCore Gateway
单一代理,简单? → 快速开始模板
复杂多步逻辑? → StateGraph + tools_condition + ToolNode
```

## 关键概念

| 概念 | 说明 |
|------|------|
| **AgentCore Runtime** | 8080端口HTTP服务(处理 `/invocations`、`/ping`) |
| **AgentCore Memory** | 托管的跨会话/跨代理记忆 |
| **LangGraph路由** | `tools_condition` 代理→工具路由,`ToolNode` 执行 |
| **AgentCore Gateway** | 将API/Lambda转为带认证的Agent工具接口 |

## 命名规则

- 字母开头,仅字母/数字/下划线,1-48字符
- 正确: `my_agent`
- 错误: `my-agent`(连字符不允许)

## 成本优化策略(差异化)

| 策略 | 说明 | 节省 |
|------|------|------|
| 无状态部署 | 不需要记忆的代理用 `--disable-memory` | 记忆存储成本 |
| 按需销毁 | 测试后立即 `agentcore destroy` | 持续运行成本 |
| 容器模式 | 生产用容器,开发用 `agentcore dev` | 开发环境成本 |
| 区域选择 | 选择低成本区域(如us-east-1) | 区域定价差异 |
| 推理配置 | 使用 `us.anthropic.claude-*` 而非按需 | 吞吐量成本 |

## 常见问题FAQ

**Q: 部署后记忆为空怎么办?**
A: 记忆写入后有约10秒最终一致性延迟。等待10秒后用 `list_events` 重新查询。如仍为空,检查日志中是否显示"Memory enabled",确认部署时未使用 `--disable-memory`。

**Q: 容器无法读取.env文件怎么办?**
A: 容器模式下.env文件不会被自动读取。在Dockerfile中使用ENV指令设置环境变量,而非依赖.env文件。

**Q: 收到"on-demand throughput isn't supported"错误?**
A: 使用 `us.anthropic.claude-*` 推理配置文件替代按需吞吐量。这是区域和模型组合的限制。

**Q: 代理名称无效?**
A: 代理名称必须字母开头,仅含字母/数字/下划线,1-48字符。将连字符改为下划线(如 `my-agent` → `my_agent`)。

**Q: Gateway返回"Unknown tool"?**
A: Lambda函数必须从 `bedrockAgentCoreToolName` 参数中去除 `___` 前缀。检查Lambda代码中的工具名处理逻辑。

**Q: 平台不匹配警告需要处理吗?**
A: 不需要。这是正常的,CodeBuild会处理ARM64跨平台构建。

## 故障排查

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `on-demand throughput isn't supported` | 推理配置不支持按需 | 使用 `us.anthropic.claude-*` 推理配置文件 |
| `Model use case details not submitted` | 未填写模型使用审批 | 在Bedrock Console填写Anthropic表单 |
| `Invalid agent name` | 名称含连字符或非法字符 | 改用下划线,字母开头,1-48字符 |
| 记忆写入后为空 | 最终一致性延迟 | 等待~10秒后重新查询 |
| 容器不读取.env | 容器模式不支持.env | 在Dockerfile中用ENV设置环境变量 |
| 部署后记忆不可用 | 部署时禁用了记忆 | 检查日志"Memory enabled/disabled",重新部署不带--disable-memory |
| `list_events` 返回空 | actor_id/session_id不匹配 | 确认ID匹配,payload是列表类型 |
| Gateway "Unknown tool" | Lambda未去除前缀 | 从 `bedrockAgentCoreToolName` 去除 `___` 前缀 |
| 平台不匹配警告 | ARM64跨平台构建 | 正常现象,无需处理 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.9+
- **AWS账户**: 需要AWS账户和Bedrock访问权限

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| bedrock-agentcore | Python包 | 必需 | `pip install bedrock-agentcore` |
| bedrock-agentcore-starter-toolkit | Python包 | 必需 | `pip install bedrock-agentcore-starter-toolkit` |
| langgraph | Python包 | 必需 | `pip install langgraph` |
| uv | 工具 | 可选(CLI安装) | `pip install uv` |
| AWS CLI | 工具 | 推荐 | 从aws.amazon.com安装 |

### API Key 配置
- 需要AWS访问密钥(AWS_ACCESS_KEY_ID、AWS_SECRET_ACCESS_KEY)
- 需要AWS区域配置(AWS_REGION)
- 需要在Bedrock Console完成模型使用审批

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,需要命令行执行能力进行部署与管理)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent在AWS Bedrock AgentCore上部署与编排多代理系统。需要Python环境和AWS账户。
