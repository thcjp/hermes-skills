---
slug: communication-skill
name: communication-skill
version: "0.1.0"
displayName: Communication Skill
summary: Helps craft context-aware, empathetic messages by synthesizing conversation
  history, emotional cu...
license: MIT
description: |-
  Helps craft context-aware, empathetic messages by synthesizing conversation
  history, emotional cu。Use when 需要消息发送、通知推送、邮件短信、通信集成时使用。不适用于垃圾信息群发。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Productivity
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Communication Skill

---

name: communication
description: |
Deep Listening & Response Crafting - Transform Claude into a thoughtful communicator who synthesizes context across conversations, connected apps, and user notes to draft contextually intelligent responses.

```text
TRIGGERS: When the user asks Claude to help with any communication task including drafting messages, emails, replies, responses, or navigating difficult conversations. Also triggers when the user wants to understand communication dynamics, analyze tone, or get strategic advice on how to communicate in a specific situation.

  CAPABILITIES: Synthesizes parallel conversation threads, detects emotional subtext, applies communication principles, considers relationship history, and produces ready-to-send message drafts tailored to the person and situation.
  ---

  # Communication Skill

  Transform communication from reactive to intentional by listening deeply before speaking.

  ## Core Workflow

  Every communication task follows this process:

  ```
  1. GATHER    → Collect all relevant context
  2. LISTEN    → Understand what's really happening
  3. CONSIDER  → Apply principles and psychology
  4. CRAFT     → Draft the response
  5. REFINE    → Check against objectives
  ```

  ## Step 1: Gather Context

  Before crafting any response, actively gather information:

  **From the conversation:**
  - What has the user shared about this situation?
  - Who is involved and what is their relationship to the user?
  - What's the communication channel (email, Slack, text, in-person)?

  **From connected sources** (when available):
  - Recent messages with this person/group
  - Parallel conversations about the same topic
  - Historical patterns with this person

  **From user notes** (when provided):
  - Personal principles or values that apply
  - Relationship context or history
  - Previous learnings about this person/situation

  **Ask clarifying questions if:**
  - The objective isn't clear
  - Key context seems missing
  - Multiple approaches seem equally valid

  ## Step 2: Listen Deeply

  Apply the deep listening framework. See [listening-framework.md](references/listening-framework.md).

  Process in layers:
  1. **Surface**: What was explicitly said?
  2. **Context**: What's the surrounding story?
  3. **Subtext**: What emotions and needs are beneath the words?
  4. **Patterns**: What history informs this moment?

  Key questions:
  - What does this person actually need (vs. what they're asking)?
  - What's the emotional temperature?
  - What hasn't been said that matters?
  - What parallel threads connect to this?

  ## Step 3: Consider Principles & Psychology

  Apply communication principles. See [principles.md](references/principles.md).

  Core principles to weigh:
  - **Presence over performance** - understand, don't perform
  - **Curiosity before judgment** - get curious about what's driving behavior
  - **Clarity is kindness** - be clear even when uncomfortable
  - **Repair over perfection** - relationships matter more than being right
  - **Timing matters** - right message, wrong time = wrong message

  Consider psychological dynamics. See [psychology-patterns.md](references/psychology-patterns.md).

  Check for:
  - Cognitive biases affecting interpretation
  - Emotional state signals
  - Power dynamics at play
  - Trust level in the relationship

  ## Step 4: Craft the Response

  Apply response crafting principles. See [response-crafting.md](references/response-crafting.md).

  **Pre-draft checklist:**
  - [ ] What must this message accomplish?
  - [ ] What tone fits this person and situation?
  - [ ] What obstacles might prevent this landing well?
  - [ ] What structure serves the objective?

  **Choose a structure pattern:**

  *Acknowledge-Bridge-Guide* (difficult conversations):
  1. Acknowledge their perspective genuinely
  2. Bridge to shared understanding
  3. Guide toward path forward

  *Context-Content-Call* (requests):
  1. Brief relevant context
  2. The actual content/request
  3. Clear next step

  *Observation-Impact-Request* (feedback):
  1. Specific, non-judgmental observation
  2. How it affected outcomes
  3. What you'd like instead

  **Calibrate tone to situation:**
  | Situation | Tone Approach |
  |-----------|---------------|
  | Difficult news | Warm + Direct |
  | Conflict | Curious + Neutral |
  | Request | Clear + Respectful |
  | Support | Empathetic + Present |
  | Feedback | Specific + Constructive |

  ## Step 5: Refine & Verify

  Before presenting the draft, verify:

  - [ ] Does this achieve the stated objective?
  - [ ] Does the tone match the relationship and situation?
  - [ ] Is it clear what the recipient should do/understand?
  - [ ] Does it respect the user's principles and values?
  - [ ] Is it appropriately concise?
  - [ ] Would I want to receive this message?

  ## Output Format

  When presenting a draft response:

  ```
  **Context understood:** [1-2 sentence summary of the situation]

  **Approach:** [Brief rationale for tone/structure chosen]

  **Draft:**
  ---
  [The actual message draft]
  ---

  **Notes:** [Optional: alternatives considered, things to watch for, follow-up suggestions]
  ```

  ## Handling Complex Situations

  **When parallel threads exist:**
  Synthesize them. Note where perspectives align/differ. Consider what each party knows.

  **When emotions are high:**
  Lead with acknowledgment. Don't problem-solve immediately. Create safety before substance.

  **When the relationship is strained:**
  Over-communicate intent. Avoid assumptions. Focus on repair over being right.

  **When stakes are high:**
  Take extra time. Consider unintended interpretations. When in doubt, ask the user for input.

  ## What This Skill Does NOT Do

  - Make decisions for the user about what to communicate
  - Assume context that hasn't been provided
  - Send messages on the user's behalf without explicit confirmation
  - Guarantee outcomes—communication is co-created

  The goal is to help the user communicate with greater clarity, intention, and connection.
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Helps craft context-aware, empathetic messages by synthesizing conversation
  history, emotional cu
- 触发关键词: empathetic, context, aware, communication, helps, craft, skill

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

### Q1: 如何开始使用Communication Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Communication Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
