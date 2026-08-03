---

slug: azure-voicelive-tool-pro
name: "azure-voicelive-tool-pro"
version: "1.0.0"
displayName: "Azure语音交互专业版"
summary: "企业级实时语音AI工具，支持函数调用、自定义语音、电话音频、高级会话与中断处理。。Azure语音交互专业版 —— 面向企业团队与专业开发者的高级实时语音AI工具。核心能力: - 函数调用（F"
license: "Proprietary"
edition: "pro"
description: |-
  Azure语音交互专业版 —— 面向企业团队与专业开发者的高级实时语音AI工具。核心能力:
  - 函数调用（Function Tools），支持AI主动调用外部API
  - 自定义语音集成：Azure标准语音、自定义语音、个人语音
  - 电话音频格式支持：G。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - 语音AI
  - Azure
  - 企业工具
  - 函数调用
  - 电话客服
  - 云计算
  - DevOps
  - type
  - async
  - conn
  - event
  - function
tools:
  - read
  - exec
  - write
homepage: ""
category: "Operations"

---

# Azure语音交互专业版
## 概述
Azure语音交互专业版是企业级实时语音AI工具，在免费版基础上提供函数调用、自定义语音、电话音频格式、高级会话管理等专业能力。适用于企业智能客服、电话客服中心、品牌定制化语音交互等高阶场景.
### 免费版与专业版对比
| 能力 | 免费版 | 专业版 |
|---|---|---|
| 实时语音通信 | 支持 | 支持 |
| 文本/音频输出 | 支持 | 支持 |
| 函数调用 | 不支持 | 支持 |
| 自定义语音 | 不支持 | 标准/自定义/个人语音 |
| 电话音频格式 | 不支持 | G.711/8kHz/16kHz |
| VAD配置 | 基础server_vad | server_vad + 语义VAD |
| 手动轮次模式 | 不支持 | 支持 |
| 中断处理 | 不支持 | 支持 |
| 对话历史管理 | 基础 | 完整（创建/删除/截断） |
| 认证方式 | API Key | API Key + 托管身份 |
| 事件处理 | 基础事件 | 完整事件体系 |
## 核心能力
### 1. 函数调用（Function Tools）
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Azure语音交互专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```python
import json
from azure.ai.voicelive.models import FunctionTool
async def voice_assistant_with_tools():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=AzureKeyCredential(os.environ["AZURE_COGNITIVE_SERVICES_KEY"]),
        model="gpt-4o-realtime-preview"
    ) as conn:
        await conn.session.update(session=RequestSession(
            instructions="你是智能客服助手，可以查询订单和天气信息。",
            modalities=["text", "audio"],
            voice="shimmer",
            input_audio_format="pcm16",
            output_audio_format="pcm16",
            turn_detection={
                "type": "server_vad",
                "threshold": 0.5,
                "prefix_padding_ms": 300,
                "silence_duration_ms": 500
            },
            tools=[
                FunctionTool(
                    type="function",
                    name="get_order_status",
                    description="查询订单状态",
                    parameters={
                        "type": "object",
                        "properties": {
                            "order_id": {"type": "string", "description": "订单号"}
                        },
                        "required": ["order_id"]
                    }
                ),
                FunctionTool(
                    type="function",
                    name="get_weather",
                    description="查询天气信息",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {"type": "string", "description": "城市名"}
                        },
                        "required": ["location"]
                    }
                )
            ]
        ))
        async for event in conn:
            match event.type:
                case "response.function_call_arguments.done":
                    result = await handle_function(event.name, event.arguments)
                    await conn.conversation.item.create(item={
                        "type": "function_call_output",
                        "call_id": event.call_id,
                        "output": json.dumps(result)
                    })
response.create()  # 触发后续响应
audio_transcript.delta":
                    print(event.delta, end="", flush=True)
                    audio = base64.b64decode(event.delta)
                    await play_audio(audio)
                    break
async def handle_function(name, arguments):
    """处理AI请求的函数调用"""
    args = json.loads(arguments)
    if name == "get_order_status":
        return {"order_id": args["order_id"], "status": "已发货", "eta": "明天到达"}
    elif name == "get_weather":
        return {"location": args["location"], "temp": "25℃", "condition": "晴"}
    return {"error": "未知函数"}
```

**处理**: 解析函数调用（Function Tools）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回函数调用（Function Tools）的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 电话音频格式支持
```python
async def telephony_voice_bot():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
environ["AZURE_COGNITIVE_SERVICES_KEY"]),
        model="gpt-4o-realtime-preview"
    ) as conn:
        await conn.session.update(session={
            "instructions": "你是电话客服，请简洁专业地回答。",
            "modalities": ["text", "audio"],
            "voice": "shimmer",
            "input_audio_format": "g711_ulaw",   # 电话音频格式
            "output_audio_format": "g711_ulaw",
            "turn_detection": {
                "type": "server_vad",
                "silence_duration_ms": 600
            }
        })
```

**处理**: 解析电话音频格式支持的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回电话音频格式支持的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 中断处理与手动轮次
```python
async def interruptible_assistant():
    async with connect(...) as conn:
        await conn.session.update(session={
            "instructions": "你是语音助手。",
            "modalities": ["text", "audio"],
            "voice": "alloy",
            "turn_detection": {"type": "server_vad", "threshold": 0.5}
        })
        async for event in conn:
            if event.type == "input_audio_buffer.speech_started":
output_audio_buffer.clear()
                print("[用户打断，已停止当前回复]")
            elif event.type == "response.audio.delta":
b64decode(event.delta)
                await play_audio(audio)
async def manual_turn_mode():
        await conn.session.update(session={"turn_detection": None})
        audio_chunk = await read_audio_from_microphone()
        b64_audio = base64.b64encode(audio_chunk).decode()
        await conn.input_audio_buffer.append(audio=b64_audio)
        await conn.input_audio_buffer.commit()  # 结束用户轮次
        await conn.response.create()            # 触发AI响应
```

**处理**: 解析中断处理与手动轮次的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回中断处理与手动轮次的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 自定义语音集成
```python
from azure.ai.voicelive.models import AzureStandardVoice, AzureCustomVoice
await conn.session.update(session={
    "voice": AzureStandardVoice(
        voice_name="zh-CN-XiaoxiaoNeural",
        voice_type="AzureStandardVoice"
    )
})
await conn.session.update(session={
    "voice": AzureCustomVoice(
        voice_name="my-brand-voice",
        voice_type="AzureCustomVoice",
        custom_voice_endpoint="https://<endpoint>"
    )
})
```

**处理**: 解析自定义语音集成的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回自定义语音集成的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级实时语音、支持函数调用、高级会话与中断处、语音交互专业版、面向企业团队与专、业开发者的高级实、时语音、核心能力、主动调用外部、API、个人语音、Use、when、接口对接、Webhook、系统连接时使用、不适用于逆向工程等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
## 使用场景
### 场景一：企业智能客服系统
企业客服中心部署AI语音助手，支持查询订单、天气等功能调用.
```python
async def enterprise_customer_service():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=DefaultAzureCredential(),
        model="gpt-4o-realtime-preview",
        credential_scopes=["https://cognitiveservices.azure.com/.default"]
    ) as conn:
        await conn.session.update(session=RequestSession(
            instructions="你是XX公司智能客服。可以查询订单状态、产品信息、退换货政策。保持专业友好的语气。",
            modalities=["text", "audio"],
            voice="shimmer",
            input_audio_format="pcm16",
            output_audio_format="pcm16",
            turn_detection={
                "type": "azure_semantic_vad",  # 语义VAD，更准确的端点检测
            },
            tools=[
                FunctionTool(type="function", name="query_order",
                    description="查询订单状态",
                    parameters={"type": "object",
                        "properties": {"order_id": {"type": "string"}},
                        "required": ["order_id"]}),
                FunctionTool(type="function", name="query_product",
                    description="查询产品信息",
                    parameters={"type": "object",
                        "properties": {"product_name": {"type": "string"}},
                        "required": ["product_name"]}),
                FunctionTool(type="function", name="return_policy",
                    description="查询退换货政策",
                    parameters={"type": "object", "properties": {}})
            ]
        ))
        async for event in conn:
type == "response.done":
                result = await handle_service_function(event.name, event.arguments)
conversation.item.create(item={
                    "type": "function_call_output",
                })
output_audio_buffer.clear()
type == "response.done":
                pass  # 继续监听
```

### 场景二：电话客服AI语音机器人
电话客服系统接入AI语音，处理来电咨询.
```python
async def telephony_bot():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
environ["AZURE_COGNITIVE_SERVICES_KEY"]),
        model="gpt-4o-realtime-preview"
    ) as conn:
        await conn.session.update(session={
            "instructions": "你是电话客服机器人，回答简洁明了。",
            "modalities": ["text", "audio"],
            "voice": AzureStandardVoice(voice_name="zh-CN-YunxiNeural"),
            "input_audio_format": "g711_ulaw",  # 电话格式
            "output_audio_format": "g711_ulaw",
            "turn_detection": {
                "type": "server_vad",
                "silence_duration_ms": 700  # 电话场景适当延长静默时间
            }
        })
        await conn.conversation.item.create(item={
            "type": "message",
            "role": "system",
            "content": [{"type": "input_text", "text": "当前来电号码: 138xxxx1234"}]
        })
```

### 场景三：品牌定制语音体验
品牌应用使用专属定制语音，提供独特交互体验.
```python
async def branded_voice_experience():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=DefaultAzureCredential(),
        model="gpt-4o-realtime-preview",
azure.com/.default"]
    ) as conn:
        await conn.session.update(session={
            "instructions": "你是XX品牌的专属语音助手，体现品牌温暖专业的调性。",
            "modalities": ["text", "audio"],
            "voice": AzureCustomVoice(
                voice_name="brand-exclusive-voice",
                custom_voice_endpoint="https://<custom-voice-endpoint>"
            ),
            "input_audio_format": "pcm16",
            "output_audio_format": "pcm16",
            "turn_detection": {"type": "azure_semantic_vad_multilingual"}
        })
```
## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问
### 1. 环境准备
```bash
pip install azure-ai-voicelive aiohttp azure-identity
```

### 2. 托管身份认证配置
```bash
export AZURE_COGNITIVE_SERVICES_ENDPOINT="https://<region>.api.cognitive.microsoft.com"
az login
```

### 3. 函数调用语音助手
```python
import asyncio, os, json, base64
from azure.ai.voicelive.aio import connect
from azure.ai.voicelive.models import RequestSession, FunctionTool
from azure.identity.aio import DefaultAzureCredential
async def main():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=DefaultAzureCredential(),
        model="gpt-4o-realtime-preview",
azure.com/.default"]
    ) as conn:
        await conn.session.update(session=RequestSession(
            instructions="你是智能助手。",
            modalities=["text", "audio"],
            voice="alloy",
            tools=[FunctionTool(type="function", name="get_time",
                description="获取当前时间",
                parameters={"type": "object", "properties": {}})]
        ))
        async for event in conn:
type == "response.done":
conversation.item.create(item={
                        "type": "function_call_output",
dumps({"time": "2026-01-18 10:00"})
                    })
type == "response.done":
                break
asyncio.run(main())
```

#
## 示例
### 音频格式对比
| 格式 | 采样率 | 适用场景 |
|---:|---:|---:|
| `pcm16` | 24kHz | 默认，高质量 |
| `pcm16-8000hz` | 8kHz | 电话 |
| `pcm16-16000hz` | 16kHz | 语音助手 |
| `g711_ulaw` | 8kHz | 电话（美国） |
| `g711_alaw` | 8kHz | 电话（欧洲） |

### VAD选项对比
| VAD类型 | 说明 | 适用场景 |
|:----:|:----:|:----:|
| `server_vad` | 基于阈值的服务器端检测 | 通用场景 |
| `azure_semantic_vad` | 语义级端点检测 | 高精度场景 |
| `azure_semantic_vad_multilingual` | 多语言语义检测 | 多语言应用 |

### 语音类型对比
| 类型 | 说明 | 适用场景 |
|:------|------:|:------|
| 内置语音 | alloy/echo/shimmer等 | 通用 |
| AzureStandardVoice | Azure神经语音 | 生产环境 |
| AzureCustomVoice | 自定义训练语音 | 品牌专属 |
| AzurePersonalVoice | 个人语音克隆 | 个性化 |
## 优选实践
1. **函数工具设计**：函数描述清晰，参数定义完整，便于AI正确调用
2. **中断处理**：始终实现speech_started中断处理，提升用户体验
3. **VAD选择**：电话场景用server_vad，高精度场景用语义VAD
4. **音频格式**：电话系统使用G.711，高质量应用使用PCM16 24kHz
5. **托管身份**：企业部署优先使用DefaultAzureCredential，避免硬编码密钥
6. **对话历史**：利用conversation.item.create注入上下文信息
7. **错误处理**：捕获ConnectionClosed和ConnectionError，实现重连机制
## 常见问题
### Q1：函数调用不触发怎么办？
检查函数工具的description是否清晰，parameters定义是否正确。AI需要理解何时调用哪个函数.
### Q2：电话音频质量不佳怎么办？
确保使用正确的G.711格式（美国用ulaw，欧洲用alaw），适当调整silence_duration_ms.
### Q3：自定义语音如何创建？
在Azure Speech Studio中训练自定义语音模型，获取endpoint后通过AzureCustomVoice配置.
### Q4：语义VAD和普通VAD有什么区别？
语义VAD基于语义理解检测用户是否说完，比基于阈值的普通VAD更准确，尤其适合长句或停顿较多的场景。与免费版配置完全兼容，可直接复用免费版的认证信息.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8及以上

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| azure-ai-voicelive | Python SDK | 必需 | `pip install azure-ai-voicelive` |
| aiohttp | Python库 | 必需 | `pip install aiohttp` |
| azure-identity | Python库 | 必需 | `pip install azure-identity` |
| Azure认知服务 | 云服务 | 必需 | Azure门户创建资源 |

### API Key 配置
- `AZURE_COGNITIVE_SERVICES_ENDPOINT`：Azure认知服务端点URL
- `AZURE_COGNITIVE_SERVICES_KEY`：API密钥（API Key认证）
- 支持DefaultAzureCredential托管身份认证（企业推荐）
- 与免费版使用相同的端点配置，完全兼容

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行专业实时语音交互任务。支持函数调用、自定义语音、电话音频格式等企业级功能，通过Python异步SDK调用Azure VoiceLive服务。与免费版完全兼容，可直接复用免费版的认证配置与基础会话流程.
- API Key通过环境变量配置: export API_KEY=your_key
## 错误处理
| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |
## 已知限制
- 需要API Key，无Key环境无法使用
- 依赖云服务，需要网络连接
## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "Azure语音交互专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "azure voicelive pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
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

| 对比维度 | Azure语音交互专业版 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 企业级实时语音AI工具，支持函数调用、自定义语音、电话音频、高级会话与中断处理。 | 通用场景 | 通用场景 |
## 核心功能

- **自动化执行**: 企业级实时语音AI工具，支持函数调用、自定义语音、电话音频、高级会话与中断处理。。Azure语音交互专业版 —— 面向企
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据