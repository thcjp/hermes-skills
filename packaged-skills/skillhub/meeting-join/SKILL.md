---
slug: "meeting-join"
name: "meeting-join"
version: "1.0.0"
displayName: "AI会议助手专业版"
summary: "企业级AI会议机器人,支持可视化头像、屏幕共享、实时协作、批量会议与团队管理,适合企业与团队场景。"
license: "Proprietary"
edition: "pro"
description: |-
  AI会议助手专业版为企业与团队提供全方位的智能会议机器人解决方案。在免费版语音会议能力之上,增加可视化头像、屏幕共享、实时网页协作、
  多种语音策略、批量会议调度与团队管理能力。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - 会议
  - 语音转写
  - AI助手
  - 企业级
  - 屏幕共享
  - 协作
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# AI会议助手专业版

## 核心能力

### 多模式会议接入

PRO版支持四种会议模式,适应不同场景需求:

| 模式 | 说明 | 适用场景 |
|------|------|---------|
| `audio` | 纯语音(与免费版一致) | 会议记录、语音问答 |
| `webpage-audio` | 网页提供音频 | 音频应用、播客接入 |
| `webpage-av` | 可视化头像 | 品牌展示、动画头像 |
| `webpage-av-screenshare` | 头像+屏幕共享 | 销售演示、培训宣讲 |

```bash
# 企业级:头像+屏幕共享模式
./scripts/run.sh "https://meet.google.com/abc-defg-hij" \
  --mode webpage-av-screenshare \
  --bot-name "销售助手" \
  --template pattern \
  --voice-strategy collaborative \
  --trigger-words "助手,小助,帮助" \
  --port 3000 \
  --screenshare-port 3001 \
  --context "企业销售会议,产品演示..."
```- 验证执行结果，确认输出符合预期格式
- 参考`批量会议调度`相关配置参数进行设置
### 协作式语音策略
PRO版支持`collaborative`语音策略,实现更自然的多人会议交互:

```python
# 协作式语音策略配置
collaborative_config = {
    "barge_in_prevention": True,      # 等待静默再发言
    "interruption_handling": True,    # 智能打断处理
    "follow_up_window": 20,           # 追问窗口(秒)
    "voice": "voice.heart",           # 语音音色
    "context": "会议上下文..."        # 初始知识库
}
```

**工作流程**:

1. 参会者提问 -> 语音智能层即时响应("让我查一下")
2. Agent后台处理 -> 获取数据并更新上下文
3. 语音智能层 -> 在自然停顿处播报结果
4. 参会者追问 -> 基于上下文即时回答

**输入**: 用户提供协作式语音策略所需的指令和必要参数。
### 屏幕共享与实时演示
```bash
# 启动屏幕共享(会议中动态控制)
# 共享本地内容
{"command": "screenshare.start", "port": 3001}

# 共享在线URL
{"command": "screenshare.start", "url": "https://slides.example.com/..."}

# 切换共享内容(无缝切换)
{"command": "screenshare.swap", "port": 3002}

# 停止共享
{"command": "screenshare.stop"}
```

**实时内容更新模式**:

```python
# 创建动态屏幕共享内容
import json

# 初始化状态
state = {"slide": 0, "title": "产品介绍", "content": "..."}
with open("/tmp/screenshare/state.json", "w") as f:
    json.dump(state, f)

# 会议中切换幻灯片
state["slide"] = 1
state["title"] = "市场分析"
with open("/tmp/screenshare/state.json", "w") as f:
    json.dump(state, f)
# 页面每2秒轮询,自动更新显示
```

**输入**: 用户提供屏幕共享与实时演示所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `屏幕共享与实时演示` 选项
- 处理流程: 接收输入 -> 执行屏幕共享与实时演示 -> 返回结果
- 输入: 用户提供屏幕共享与实时演示所需的参数和指令
- 输出: 返回屏幕共享与实时演示的执行结果,包含操作状态和输出数据

### 批量会议调度
```python
# 批量调度多个会议
meetings = [
    {"url": "https://meet.google.com/aaa", "time": "09:00", "topic": "晨会"},
    {"url": "https://meet.google.com/bbb", "time": "11:00", "topic": "客户演示"},
    {"url": "https://meet.google.com/ccc", "time": "14:00", "topic": "项目评审"},
    {"url": "https://meet.google.com/ddd", "time": "16:00", "topic": "周总结"}
]

scheduler = MeetingScheduler(
    api_key="YOUR_API_KEY",
    parallel=3,                    # 并发会议数
    default_mode="webpage-av",    # 默认模式
    auto_summary=True,            # 自动生成纪要
    auto_archive=True              # 自动归档
)

for meeting in meetings:
    scheduler.add(meeting)

scheduler.run()  # 按计划执行
```

**输入**: 用户提供批量会议调度所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量会议调度` 选项
- 处理流程: 接收输入 -> 执行批量会议调度 -> 返回结果
- 输入: 用户提供批量会议调度所需的参数和指令
- 输出: 返回批量会议调度的执行结果,包含操作状态和输出数据

### 团队管理与多租户
```python
# 多团队配置
teams = {
    "sales": {
        "name": "销售团队",
        "bot_name": "销售助手",
        "default_mode": "webpage-av-screenshare",
        "templates": ["pattern", "dashboard"],
        "context_pool": "sales_knowledge_base"
    },
    "support": {
        "name": "客服团队",
        "bot_name": "客服小助手",
        "default_mode": "audio",
        "templates": ["voice-agent"],
        "context_pool": "support_kb"
    },
    "training": {
        "name": "培训团队",
        "bot_name": "培训讲师",
        "default_mode": "webpage-av-screenshare",
        "templates": ["pattern", "ring"],
        "context_pool": "training_materials"
    }
}
```

**输入**: 用户提供团队管理与多租户所需的指令和必要参数。
**处理**: 按照skill规范执行团队管理与多租户操作,遵循单一意图原则。
**输出**: 返回团队管理与多租户的执行结果,包含操作状态和输出数据。

#
## 适用场景

### 场景一:企业销售演示会议

需求:销售团队需要机器人辅助产品演示,实时展示幻灯片并回答客户问题。

```bash
# 启动销售演示会议
./scripts/run.sh "https://meet.google.com/sales-demo" \
  --mode webpage-av-screenshare \
  --bot-name "产品专家" \
  --template pattern \
  --voice-strategy collaborative \
  --trigger-words "专家,产品,演示" \
  --port 3000 \
  --screenshare-port 3001 \
  --context "产品:企业级项目管理SaaS。
            功能:任务管理、甘特图、时间追踪、报表。
            定价:团队版¥99/人/月,企业版¥299/人/月。
            竞品优势:更直观的可视化、更灵活的自定义。" \
  --max-duration 60
```

会议中动态控制屏幕共享:

```python
# 销售演示流程
slides = [
    {"slide": 0, "title": "产品概述", "content": "..."},
    {"slide": 1, "title": "核心功能", "content": "..."},
    {"slide": 2, "title": "客户案例", "content": "..."},
    {"slide": 3, "title": "定价方案", "content": "..."}
]

# 切换幻灯片
for slide in slides:
    update_screenshare_state(slide)
    # 机器人同步讲解...
```

### 场景二:团队协作会议自动化

需求:为团队的每日站会、周会、月度评审自动安排机器人参会记录。

```python
# 自动化会议工作流
schedule = {
    "daily_standup": {
        "time": "09:00",
        "days": ["mon", "tue", "wed", "thu", "fri"],
        "mode": "audio",
        "auto_summary": True,
        "summary_recipients": ["team@example.com"]
    },
    "weekly_review": {
        "time": "friday 16:00",
        "mode": "webpage-av",
        "auto_summary": True,
        "auto_create_tasks": True  # 自动创建待办
    },
    "monthly_review": {
        "time": "last-friday 14:00",
        "mode": "webpage-av-screenshare",
        "auto_summary": True,
        "generate_report": True  # 生成月度报告
    }
}

# 启动调度器
scheduler = SmartScheduler(schedule)
scheduler.start()
```

### 场景三:在线培训与网络研讨会

需求:培训机构需要机器人在网络研讨会中辅助讲师,展示资料并回答学员问题。

```bash
# 网络研讨会配置
./scripts/run.sh "https://zoom.us/j/webinar-123" \
  --mode webpage-av-screenshare \
  --bot-name "学习伙伴" \
  --template avatar \
  --voice-strategy collaborative \
  --trigger-words "伙伴,学习,问题" \
  --context "课程:Python数据分析入门。
            章节:数据清洗、可视化、统计分析。
            学员可随时提问,机器人会基于课程内容回答。
            常见问题已预置在知识库中。" \
  --max-duration 120
```

## 使用流程

### 依赖说明

### 运行环境

1. **Agent平台**: 支持SKILL.md规范的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
2. **操作系统**: Windows / macOS / Linux
3. **Python**: 3.10+ 或 **Node.js**: 18+
4. **本地HTTP服务**: 用于网页模式(可选,使用模板时自动启动)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| aiohttp | Python库 | 必需 | pip install aiohttp |
| websockets | Python库 | 必需 | pip install websockets |
| 会议平台账户 | 服务 | 必需 | Google/MS/Zoom企业账户 |
| 本地HTTP服务 | 工具 | 网页模式必需 | Python/Node.js自带 |

### API Key 配置

5. 通过 `~/.agentcall/config.json` 或 `AGENTCALL_API_KEY` 环境变量配置
6. 企业版支持API Key池与负载均衡
7. 隧道认证使用独立的 `tunnel_access_key`(非API Key)

### 可用性分类

8. **分类**: MD+EXEC(纯Markdown指令+脚本执行能力)
9. **说明**: 专业版基于Markdown指令驱动Agent执行企业级会议任务,通过Python/Node.js脚本实现多模式接入、屏幕共享、批量调度与团队管理
10. **PRO版增强**: 四种会议模式、可视化头像、屏幕共享、协作式语音、批量会议、团队管理、CI/CD集成、数据分析

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 模板系统

PRO版提供多种内置可视化模板:

| 模板 | 说明 | 适用场景 |
|------|------|---------|
| `pattern` | 径向光芒,状态变色(默认) | 通用、品牌展示 |
| `ring` | 霓虹光环 | 科技感、现代风格 |
| `orb` | 球体动画 | 极简、抽象 |
| `avatar` | 拟人头像 | 拟人化交互 |
| `dashboard` | 仪表盘 | 数据展示 |
| `voice-agent` | 无本地服务 | 纯语音应用 |

### 协作式语音配置

```python
# 高级语音配置
advanced_voice_config = {
    "strategy": "collaborative",
    "trigger_words": ["助手", "小助", "帮助"],
    "barge_in_prevention": True,
    "interruption_use_full_text": True,
    "voice": "voice.heart",  # 也可选 voice.bella/echo/eric
    "context": "初始知识库(4000字符)",
    "predictive_context": True  # 预测性上下文更新
}
```

### 隧道与本地服务

```bash
# 本地服务配置
python -m http.server 3000 --directory ./avatar-page/
python -m http.server 3001 --directory ./screenshare-content/

# 使用公共URL(无需隧道)
./scripts/run.sh "会议链接" \
  --webpage-url "https://your-site.com/bot" \
  --screenshare-url "https://your-site.com/slides"
```

## 常见问题

### Q1: 如何从免费版升级至PRO版?

A: PRO版完全兼容免费版。现有API Key与配置可直接使用,只需在命令中指定高级模式与参数即可启用PRO功能。

### Q2: 屏幕共享支持哪些内容?

A: 支持本地HTML页面、在线URL、动态内容(通过状态文件轮询更新)。设计为1280x720视口,建议标题字号40px+,正文字号24px+以保证可读性。

### Q3: 协作式语音策略与直接策略有何区别?


### Q4: 批量会议的并发能力如何?

A: 支持并行会议,默认并发3个,可通过配置调整。每个会议独立运行,互不干扰,各自生成纪要。

### Q5: 如何保障企业会议数据安全?

A: 建议配置Agent框架的权限系统(如allow列表、hooks、plan模式)限制机器人行为。会议转写内容作为Agent输入处理,建议在可信环境中使用。支持端到端加密与审计日志。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

