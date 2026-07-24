---
slug: "work"
name: "work"
version: 1.0.1
displayName: "职场工作汇报"
summary: "职场日常工作指导，覆盖专业沟通、会议准备、职场动态与入职90天策略"
license: "Proprietary"
description: |-
  Work Skill 是职场日常工作指导工具，覆盖 Professional Communication（专业沟通）、
  Workplace Dynamics（职场动态）、First 90 Days（入职90天）、Situation Detection（情境识别）、
  Work Profile（工作画像）五大能力。帮助处理邮件起草、会议准备、状态汇报、
  职场政治、入职适应等日常工作场景.
tags:
  - 通用办公
tools:
  - read
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Work Skill 职场工作汇报

职场日常工作指导，覆盖专业沟通、职场动态处理、入职适应、情境识别与工作画像构建.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 职场工作汇报处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

### Professional Communication（专业沟通）
处理日常沟通任务，包括邮件起草、会议准备和状态汇报.
**邮件起草（Email drafts）**：根据收件人级别和紧急程度调整语气。高管邮件先给执行摘要，细节放在下方。状态标记：DONE（已完成）、IN PROGRESS（进行中）、BLOCKED（被阻塞，附原因）.
**会议准备（Meeting prep）**：三步准备法：
1. Review context（previous threads, decisions）— 回顾之前的讨论线索和已做决策
2. Define your contribution（questions, updates, blockers）— 明确你要贡献什么：提出问题、进度更新或阻塞点
3. Prepare one-liner if asked "any updates?" — 准备一句话电梯汇报，被问到时能快速回答

**状态汇报（Status updates）**：主动汇报，不等被问。格式：本周完成 → 下周计划 → 风险/阻塞。用书面记录贡献，邮件先发再开会.
**输出**: 返回Professional Communication（专业沟通）的处理结果,包含执行状态码、结果数据和执行日志.
### Workplace Dynamics（职场动态）
识别和处理办公室政治与人际动态.
- **被抢功（When someone takes credit）**：Document contributions in writing before meetings. 会前用邮件记录你的贡献。会后跟进 "as I mentioned in my email about X..."
- **被公开质疑（When undermined publicly）**：当场不反应。私下先沟通："I noticed X happened. Can we talk about how we work together?"
- **建立联盟（Building alliances）**：Visibility comes from being useful to the right people. 找到你的工作与有影响力的人的交集.
- **读懂氛围（Reading the room）**：观察谁发言、谁被打断、谁做最终决定 — 那才是真正的组织架构图.
**输出**: 返回Workplace Dynamics（职场动态）的处理结果,包含执行状态码、结果数据和执行日志.
### First 90 Days（入职90天）
新角色适应的分阶段策略：

- **Week 1-4**：Listen more than contribute. 绘制人际关系图，理解这里 "好" 的标准.
- **Week 5-8**：开始交付小胜利。主动寻求反馈.
- **Week 9-12**：Own something end-to-end. 进行 "how am I doing?" 对话.
向经理提出三个关键问题：
- "What does success look like in 90 days?" — 明确成功标准
- "Who should I build relationships with?" — 确定需要建立关系的关键人物
- "What should I definitely avoid?" — 了解必须避免的雷区

**输入**: 用户提供First 90 Days（入职90天）所需的指令和必要参数.
**处理**: 解析First 90 Days（入职90天）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回First 90 Days（入职90天）的处理结果,包含执行状态码、结果数据和执行日志。### Situation Detection（情境识别）
根据用户描述自动识别工作情境并加载对应策略：

| 信号 | 上下文 | 对应场景 |
|---:|---:|---:|
| 入职、新员工、onboarding | 新角色适应 | new-hire 策略 |
| 抢功、被质疑、办公室政治 | 职场动态 | politics 策略 |
| 邮件、会议准备、状态汇报 | 沟通任务 | comms 策略 |
| 可见性、被忽视、认可 | 感知管理 | visibility 策略 |
| 模糊任务、不清晰优先级 | 任务清晰度 | clarity 策略 |

**处理**: 解析Situation Detection（情境识别）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Situation Detection（情境识别）的处理结果,包含执行状态码、结果数据和执行日志。### Work Profile（工作画像）
逐步构建用户的工作环境画像，包括 Environment（工作环境）、Key Relationships（关键关系）、Culture Signals（文化信号）、Challenges（挑战）。每次工作相关问题都会丰富画像。空字段表示尚未收集到信息.
**处理**: 解析Work Profile（工作画像）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Work Profile（工作画像）的处理结果,包含执行状态码、结果数据和执行日志.
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`work`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 示例

### 基本用法

向Agent发送指令:

```
使用 职场工作汇报 处理以下任务:
[具体任务描述]
```

### 输出说明

Agent将根据指令调用对应能力,返回响应数据。响应格式取决于具体能力点的输出定义.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD（纯Markdown指令，无需exec命令行能力）

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 情境识别失败 | 用户描述过于模糊或混合多个场景 | 请求用户补充具体情境细节，分别处理每个场景 |
| 沟通建议不适用 | 行业/公司文化差异大 | 询问用户公司文化和沟通风格偏好，调整建议 |
| 邮件语气不当 | 未考虑收件人级别和关系 | 确认收件人身份（高管/平级/下属），按级别调整正式程度 |
| 职场政治建议风险 | 直接对抗可能恶化关系 | 优先建议私下沟通和书面记录，避免公开对抗 |
| 入职建议过于激进 | 新人过早表现可能适得其反 | 遵循 listen-first 原则，前4周以观察为主 |
| 状态汇报遗漏关键信息 | 未结构化汇报内容 | 使用 DONE/IN PROGRESS/BLOCKED 格式，附风险和阻塞原因 |
| 工作画像信息不足 | 用户首次使用尚未积累上下文 | 主动询问环境、关系、文化信号等关键问题 |
| 紧急职场危机处理不当 | 未区分紧急与常规场景 | 紧急场景优先提供即时应对话术，常规场景提供长期策略 |

## 常见问题

### Q1: 如何在会议中被看到而不显得刻意？
A: 会前准备贡献点，会中主动提供数据和视角，会后用邮件书面跟进。Visibility comes from being useful, not from being loud.
### Q2: 入职前90天最应该做什么？
A: 前四周多听少说，绘制人际关系图。5-8周开始交付小胜利。9-12周独立负责一件事。主动问经理 "What should I definitely avoid?".
### Q3: 被同事抢功怎么办？
A: Document contributions in writing before meetings。会前邮件发出你的工作记录，会后引用邮件跟进。不公开指责，用事实说话.
## 已知限制

- 不提供职业规划策略（使用 career skill）
- 不提供个人生产力工具建议（使用 productivity skill）
- 职场文化建议基于通用企业环境，特定行业可能需调整
- 无法替代专业法律建议（如劳动纠纷场景）
