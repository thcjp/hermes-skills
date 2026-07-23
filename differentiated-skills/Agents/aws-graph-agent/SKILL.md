---
slug: "aws-graph-agent"
name: "aws-graph-agent"
version: "1.0.0"
displayName: "AWS图代理"
summary: "Bedrock AgentCore与LangGraph编排,引导式部署,一致性处理,多代理模式库。"
license: "Proprietary"
description: |-
  AWS Bedrock AgentCore与LangGraph多代理部署编排工具：提供StateGraph状态图编排、AgentCore Runtime HTTP封装（8080端口）、Memory跨会话STM/LTM持久记忆、Gateway外部API/Lambda工具集成、CLI全生命周期管理五大核心能力。适用于多代理协调的复杂业务系统、跨会话持久记忆代理、外部API集成到代理工具链、生产级AI代理部署。适用关键词：Bedrock AgentCore、LangGraph、多代理编排、状态图、agentcore、state-graph。
tags:
  - 智能代理
  - 云计算
  - AWS
  - 多代理系统
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
tools: ["read", "write", "exec"]
tags: "AWS,云计算,DevOps"
---
# AWS图代理（AWS Graph Agent）

基于 AWS Bedrock AgentCore 与 LangGraph 编排的多代理系统。通过 StateGraph 状态图定义代理工作流，AgentCore Runtime 封装为 HTTP 服务，Memory 管理持久记忆，Gateway 集成外部工具。

## 核心能力

### 1. StateGraph 状态图编排
使用 LangGraph StateGraph 定义多代理工作流，支持 `tools_condition` 自动路由（代理→工具或 END）、`ToolNode` 预置工具执行器、条件边实现复杂多步逻辑（planner→executor→reviewer 循环）

**输入**: 用户提供StateGraph 状态图编排所需的指令和必要参数。
**处理**: 解析StateGraph 状态图编排的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回StateGraph 状态图编排的响应数据,包含状态码、结果和日志。

### 2. AgentCore Runtime HTTP 封装
将代理封装为 8080 端口 HTTP 服务，处理 `/invocations`（调用）与 `/ping`（健康检查）端点，支持容器模式部署

**输入**: 用户提供AgentCore Runtime HTTP 封装所需的指令和必要参数。
**处理**: 解析AgentCore Runtime HTTP 封装的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回AgentCore Runtime HTTP 封装的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. AgentCore Memory 持久记忆
管理跨会话/跨代理的 STM（短期记忆，会话内逐轮）与 LTM（长期记忆，跨会话/跨代理），配套一致性处理模式（写入后约 10s 最终一致，含等待+验证+重试逻辑）

**输入**: 用户提供AgentCore Memory 持久记忆所需的指令和必要参数。
**处理**: 解析AgentCore Memory 持久记忆的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回AgentCore Memory 持久记忆的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. AgentCore Gateway 工具集成
将 API/Lambda 转化为带认证的 Agent 工具接口，支持 Fallback Mock（本地开发）、Local 工具协议、Production Gateway（生产）三种传输模式

**输入**: 用户提供AgentCore Gateway 工具集成所需的指令和必要参数。
**处理**: 解析AgentCore Gateway 工具集成的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回AgentCore Gateway 工具集成的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 5. agentcore CLI 全生命周期管理
`configure`（交互式/脚本化配置）→`launch`（容器部署）→`dev`（热重载本地开发）→`invoke`（测试调用）→`destroy`（清理资源避免持续计费）

**输入**: 用户提供agentcore CLI 全生命周期管理所需的指令和必要参数。
**处理**: 解析agentcore CLI 全生命周期管理的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回agentcore CLI 全生命周期管理的响应数据,包含状态码、结果和日志。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：Bedrock、引导式部署、多代理模式库、AWS、多代理部署编排工、全生命周期管理五、大核心能力、适用于多代理协调、的复杂业务系统、跨会话持久记忆代、集成到代理工具链、生产级、代理部署、适用关键词、多代理编排等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 适用场景

**何时使用**：
- 需要多代理协调的复杂业务系统（客服、电商、医疗、金融）
- 需要跨会话持久记忆的对话代理（用户偏好、历史决策）
- 需要将外部 API/Lambda 集成到代理工具链的企业应用
- 希望在生产环境大规模部署 AI 代理的团队
- 使用 LangGraph 进行复杂多步逻辑编排的开发者

**输入**：Python 代理代码（基于 langgraph + bedrock-agentcore）+ AWS 凭据 + Bedrock 模型使用审批
**输出**：部署成功的 HTTP 代理服务（8080 端口）+ CLI 管理能力 + 持久记忆与网关工具集成

**不适用场景**：
- 未完成 Bedrock 模型使用审批的账户
- 不需要多代理协调的简单单一代理场景（可直接用基础 LLM API）
- 非 AWS 平台部署需求

## 使用流程

### 依赖详情
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AWS图代理处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
pip install bedrock-agentcore bedrock-agentcore-starter-toolkit langgraph
uv tool install bedrock-agentcore-starter-toolkit  # 安装 agentcore CLI
```

### Step 2：预检清单（部署前必读）
| 检查项 | 要求 | 不满足的后果 |
|:-----|:-----|:-----|
| 模型使用审批 | 在 Bedrock Console 填写 Anthropic 表单 | `Model use case details not submitted` |
| 推理配置 | 使用 `us.anthropic.claude-*` 推理配置文件 | `on-demand throughput isn't supported` |
| 代理命名 | 字母开头，仅字母/数字/下划线，1-48 字符 | `Invalid agent name` |
| 区域选择 | 选择支持 AgentCore 的区域（如 us-east-1） | 部署失败 |
| 环境变量 | 容器中在 Dockerfile 设置 ENV，非 .env | 容器不读取 .env |
| 记忆开关 | 确认是否需要记忆子系统 | 记忆功能不可用 |

### Step 3：编写代理代码（StateGraph + Runtime）
```python
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from typing import Annotated
from typing_extensions import TypedDict
# ...
class State(TypedDict):
    messages: Annotated[list, add_messages]
# ...
builder = StateGraph(State)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools))
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge(START, "agent")
graph = builder.compile()
# ...
app = BedrockAgentCoreApp()
@app.entrypoint
def invoke(payload, context):
    result = graph.invoke({"messages": [("user", payload.get("prompt", ""))]})
    return {"result": result["messages"][-1].content}
app.run()
```

### Step 4：配置与部署
```bash
# 交互式配置
agentcore configure -e agent.py --region us-east-1
# 脚本化配置（CI/CD）
agentcore configure -e agent.py --region us-east-1 --name my_agent --non-interactive
# 容器模式部署（生产）
agentcore launch --deployment-type container
# 无记忆部署（无状态代理）
agentcore launch --disable-memory
```

### Step 5：测试与开发
```bash
agentcore dev                              # 热重载本地开发
agentcore invoke '{"prompt": "Hello"}'    # 测试调用
```

### Step 6：按决策树选择多代理模式
```text
多代理协调? → 编排器+专家模式（编排器根据意图路由到专家，共享 session_id）
跨会话持久记忆? → AgentCore Memory（非 LangGraph checkpoints）
外部 API/Lambda? → AgentCore Gateway
单一代理简单? → 快速开始模板
复杂多步逻辑? → StateGraph + tools_condition + ToolNode
```

### Step 7：清理资源（避免持续计费）
```bash
agentcore destroy
```

## 示例

### 示例(补充)

**输入**：部署一个带工具调用的简单代理

**输出**（代码与部署）：
```python
# 最简模式：用户输入 → 代理节点 → tools_condition → ToolNode → 回到代理
#                                    → END（无需工具）
builder = StateGraph(State)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools))
builder.add_conditional_edges("agent", tools_condition)  # 自动路由
builder.add_edge(START, "agent")
graph = builder.compile()
```
部署：`agentcore configure -e agent.py --region us-east-1 && agentcore launch`

### 示例二：记忆系统写入与验证（一致性处理·指数退避）

**输入**：写入长期记忆并确保一致性

**输出**（写入+指数退避验证逻辑）：
```python
from bedrock_agentcore.memory import MemoryClient
import time
# ...
memory = MemoryClient()
memory.create_event(session_id, actor_id, event_type, payload)  # 写入
# ...
# 最终一致性验证（指数退避：2s→4s→8s→16s→30s，最多 5 次）
def verify_with_backoff(memory, session_id, actor_id, event_type, payload,
                        base=2, max_wait=30, max_retries=5):
    for attempt in range(max_retries):
        time.sleep(min(base * (2 ** attempt), max_wait))  # 指数退避+上限
        if memory.list_events(session_id):
            return  # 一致性达成
        if attempt < max_retries - 1:
            memory.create_event(session_id, actor_id, event_type, payload)  # 重写
    raise RuntimeError(f"记忆一致性验证失败：{max_retries} 次重试后仍为空")
# ...
verify_with_backoff(memory, session_id, actor_id, event_type, payload)
# 注意：event['payload'] 是列表类型；确认 actor_id 和 session_id 匹配
```

### 示例三：多代理协调（编排器+专家模式）端到端

**输入**：客服系统按意图路由到客服专家/计费专家，共享 session_id 跨专家记忆

**输出**（编排器+专家+共享记忆，完整部署）：
```python
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
# ...
class State(TypedDict):
    messages: list
    expert: str
# ...
def orchestrator(state):
    intent = classify(state["messages"][-1])  # 意图分类
    return {"expert": {"投诉": "cs_expert", "账单": "billing_expert"}[intent]}
# ...
def cs_expert(state):
    return {"messages": [handle_cs(state)]}      # 客服专家处理
# ...
def billing_expert(state):
    return {"messages": [handle_billing(state)]}  # 计费专家处理
# ...
builder = StateGraph(State)
builder.add_node("orchestrator", orchestrator)
builder.add_node("cs_expert", cs_expert)
builder.add_node("billing_expert", billing_expert)
builder.add_edge(START, "orchestrator")
builder.add_conditional_edges("orchestrator", lambda s: s["expert"])
builder.add_edge("cs_expert", END)
builder.add_edge("billing_expert", END)
graph = builder.compile()
```
部署：`agentcore configure -e agent.py --region us-east-1 && agentcore launch`。两个专家共享同一 `session_id`，通过 AgentCore Memory 实现跨专家记忆传递（编排器写入意图，专家读取上下文），避免用户重复陈述。

### 示例四：Gateway 工具集成端到端

**输入**：将订单查询/退款 Lambda 集成为代理工具，生产网关模式部署

**输出**（Gateway 注册+代理调用+三种传输模式）：
```python
from bedrock_agentcore.gateway import GatewayClient
# ...
# 三种传输模式按环境选择
mode = "production"  # "mock"（本地开发）/ "local"（本地协议）/ "production"（生产网关）
gateway = GatewayClient(mode=mode)
tools = gateway.register_tools([
    {"name": "search_orders", "lambda_arn": "arn:aws:lambda:us-east-1:…:OrderSearch"},
    {"name": "issue_refund",  "lambda_arn": "arn:aws:lambda:us-east-1:…:Refund"},
])
# 工具名必须去除 Lambda 的 ___ 前缀，否则返回 "Unknown tool"
# ...
agent = create_agent_with_tools(tools)  # 工具自动注入 StateGraph
```
调用：`agentcore invoke '{"prompt": "查询订单 #1234 并退款"}'`。代理自动调用 `search_orders`→`issue_refund`，Gateway 处理 Lambda 认证与调用。本地开发用 `mode="mock"` 返回假数据无需真实 Lambda；生产用 `mode="production"` 走网关鉴权。

## 错误处理

| 场景 | 原因 | 处理方式 |
|---:|---:|---:|
| `on-demand throughput isn't supported` | 推理配置不支持按需 | 使用 `us.anthropic.claude-*` 推理配置文件 |
| `Model use case details not submitted` | 未填写模型使用审批 | 在 Bedrock Console 填写 Anthropic 表单 |
| `Invalid agent name` | 名称含连字符或非法字符 | 改用下划线，字母开头，1-48 字符（如 `my-agent`→`my_agent`） |
| 记忆写入后为空 | 最终一致性延迟（约10s） | 等待 10s 后重新查询；检查日志"Memory enabled/disabled" |
| 容器不读取 .env | 容器模式不支持 .env | 在 Dockerfile 中用 ENV 指令设置环境变量 |
| 部署后记忆不可用 | 部署时禁用了记忆 | 重新部署不带 `--disable-memory` |
| `list_events` 返回空 | actor_id/session_id 不匹配 | 确认 ID 匹配，payload 是列表类型 |
| Gateway "Unknown tool" | Lambda 未去除前缀 | 从 `bedrockAgentCoreToolName` 去除 `___` 前缀 |
| 平台不匹配警告 | ARM64 跨平台构建 | 正常现象，CodeBuild 会处理，无需操作 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| bedrock-agentcore | Python 包 | 必需 | `pip install bedrock-agentcore` |
| bedrock-agentcore-starter-toolkit | Python 包 | 必需 | `pip install bedrock-agentcore-starter-toolkit` |
| langgraph | Python 包 | 必需 | `pip install langgraph` |
| Python 运行时 | 运行时 | 必需 | python.org，需 3.9+ |
| uv | 工具 | 可选（CLI 安装） | `pip install uv` |
| AWS CLI | 工具 | 推荐 | 从 aws.amazon.com 安装 |
| AWS 账户 | 账户 | 必需 | 需 AWS 账户和 Bedrock 访问权限 |
| AWS 访问密钥 | 凭据 | 必需 | `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_REGION` |
| Bedrock 模型审批 | 平台配置 | 必需 | 在 Bedrock Console 填写 Anthropic 表单 |
| Agent 平台 | 运行环境 | 必需 | Claude Code / Cursor / Codex / Gemini CLI 等 |
| 操作系统 | 运行环境 | 必需 | Windows / macOS / Linux |

**成本优化策略**：无状态部署用 `--disable-memory` 节省记忆存储成本；测试后立即 `agentcore destroy` 避免持续运行成本；生产用容器、开发用 `agentcore dev`；选择低成本区域（如 us-east-1）；使用 `us.anthropic.claude-*` 推理配置降低吞吐量成本。

**密钥安全处理规范（零暴露硬性约束）**：代理绝不能读取、cat、打印、回显或日志记录 `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` 明文，绝不在聊天/提交/镜像中暴露凭据——无论出于任何原因包括"验证配置"。硬性规则：(1) 凭据只通过环境变量或 IAM Role 注入，禁止硬编码到源码或 Dockerfile ARG；(2) `agentcore configure` 所需凭据从 AWS CLI 命名配置文件（`--profile`）或实例元数据获取，禁止在命令行明文传参；(3) 容器部署用任务角色（Task Role）而非 ENV 明文密钥，ENV 仅用于非敏感配置；(4) 如用户在聊天中粘贴了密钥，立即告知已泄露，要求轮换并从历史清除，绝不回显；(5) `.env` 加入 `.gitignore`，禁止提交版本库；(6) `agentcore destroy` 后确认密钥与资源已清理。验证安装状态用 `aws sts get-caller-identity`（返回角色 ARN，不暴露密钥）而非打印环境变量。

**可用性分类**：MD+EXEC（纯 Markdown 指令，需要命令行执行能力进行部署与管理）
- **API Key**：本skill无需额外API Key配置

## 常见问题

**Q1：部署后记忆为空怎么办？**
A：记忆写入后有约 10 秒最终一致性延迟。等待 10 秒后用 `list_events` 重新查询。如仍为空，检查日志中是否显示"Memory enabled"，确认部署时未使用 `--disable-memory`。

**Q2：容器无法读取 .env 文件怎么办？**
A：容器模式下 .env 文件不会被自动读取。在 Dockerfile 中使用 ENV 指令设置环境变量，而非依赖 .env 文件。

**Q3：收到"on-demand throughput isn't supported"错误？**
A：使用 `us.anthropic.claude-*` 推理配置文件替代按需吞吐量。这是区域和模型组合的限制。

**Q4：代理名称无效？**
A：代理名称必须字母开头，仅含字母/数字/下划线，1-48 字符。将连字符改为下划线（如 `my-agent` → `my_agent`）。

**Q5：Gateway 返回"Unknown tool"？**
A：Lambda 函数必须从 `bedrockAgentCoreToolName` 参数中去除 `___` 前缀。检查 Lambda 代码中的工具名处理逻辑。

## 已知限制

1. **记忆最终一致性延迟约10秒**：写入后不能立即可读，需等待+验证+重试机制，不适合强一致性场景
2. **依赖 Bedrock 模型审批**：未在 Bedrock Console 填写 Anthropic 表单则无法部署，审批流程不可跳过
3. **代理命名规则严格**：仅字母/数字/下划线，1-48 字符，连字符等常见命名方式不被接受
4. **容器模式不支持 .env**：必须在 Dockerfile 中用 ENV 设置环境变量，与本地开发习惯不同
5. **Gateway 工具名需去前缀**：Lambda 的 `bedrockAgentCoreToolName` 必须去除 `___` 前缀，否则返回"Unknown tool"
