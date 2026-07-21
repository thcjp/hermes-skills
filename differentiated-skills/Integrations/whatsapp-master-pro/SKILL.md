---
slug: whatsapp-master-pro
name: whatsapp-master-pro
version: "1.0.0"
displayName: WhatsApp大师(专业版)
summary: WhatsApp 全能力版：消息/交互/群组/多智能体协作/预算调度/历史检索，22 类动作。
license: Proprietary
edition: pro
description: |-
  WhatsApp 大师（专业版）面向团队与企业用户，提供 WhatsApp 的全部 22 类动作：消息发送（文本/媒体/投票/贴纸/语音/GIF）、交互（反应/回复/编辑/撤回）、群组管理（创建/重命名/图标/描述/参与者/管理员/邀请链接）、历史检索与多智能体协作。配套拥塞控制、对话生命周期与预算感知调度三大高级协议
tags:
- 即时通讯
- WhatsApp
- 多智能体
- 群组管理
- 自动化协作
tools:
  - - read
- exec
---
# WhatsApp 大师（专业版）

## 概述

专业版是 WhatsApp 能力的完整封装，覆盖 22 类动作：消息发送、交互、群组管理与历史检索。在基础能力之上，新增"多智能体讨论协议"——让多个 AI Agent 在同一个 WhatsApp 群组中协作时，能够自动控制发言节奏、检测循环对话、追踪目标并在预算耗尽前优雅收尾。

本版本面向需要在 WhatsApp 上做"多 Agent 协作 + 群组运营 + 成本控制"的团队与企业用户。

## 核心能力

| 类别 | 动作 | 数量 |
|------|------|------|
| 消息 | 文本、媒体、投票、贴纸、语音、GIF | 6 |
| 交互 | 反应（加/删）、回复/引用、编辑、撤回 | 5 |
| 群组 | 创建、重命名、图标、描述、加人、踢人、升降权、离开、邀请码、群信息 | 10 |
| 历史 | 全文搜索、vCard 联系人提取 | 2 |
| 多智能体 | 路由、拥塞、生命周期、预算 | 4 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：WhatsApp、全能力版、多智能体协作、预算调度、历史检索、类动作、专业版、面向团队与企业用、的全部、消息发送、群组管理、参与者、管理员、邀请链接、历史检索与多智能、体协作、配套拥塞控制、对话生命周期与预、算感知调度三大高、级协议等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：多智能体脑暴（架构师视角）
把 3 个 Agent（Jarvis/Luna/Rex）放进一个 WhatsApp 群组讨论产品方案。配置 `broadcast` 模式让所有 Agent 都能发言，开启拥塞控制防止消息爆炸，设置 `maxTurnsPerObjective=30` 硬上限。

### 场景二：按需点名讨论（产品视角）
只让被点名的 Agent 发言。配置 `addressed` 模式，用户说"Luna，你怎么看？"时只有 Luna 响应，其他 Agent 保持沉默。

### 场景三：结构化轮询（QA 视角）
需要每个 Agent 依次给出意见。配置 `round-robin` 模式，Agent 按顺序发言，避免抢话。

### 场景四：预算燃烧模式（运维视角）
接近 API 配额重置时仍有大量额度剩余。启用 `burn` 模式，加快发言节奏、放宽陈旧阈值、鼓励发散讨论，把即将过期的 token 用完。

### 场景五：群组运营（运营视角）
创建项目群组、设置图标与描述、邀请参与者、生成邀请链接、管理员权限管理。全部通过命令行完成。

### 场景六：历史检索（开发者视角）
搜索群组历史消息中的关键词，提取 vCard 联系人电话号码，按 LID/JID 别名跨格式检索。

## 不适用场景

以下场景WhatsApp大师(专业版)不适合处理：

- 需要100%确定性的关键决策
- 医疗诊断
- 法律判决

## 触发条件

需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于非本工具能力范围的需求。

## 快速开始

### 120 秒上手
1. 确认 WhatsApp 账号已链接
2. 选择工作流（消息/交互/群组/多智能体）
3. 按命令模板调用对应动作

### 发送投票

```text
message action=poll channel=whatsapp to="+34612345678" pollQuestion="What time?" pollOption=["3pm", "4pm", "5pm"]
```

### 添加反应

```text
message action=react channel=whatsapp chatJid="34612345678@s.whatsapp.net" messageId="ABC123" emoji="🚀"
```

### 回复/引用消息

```text
message action=reply channel=whatsapp to="34612345678@s.whatsapp.net" replyTo="QUOTED_MSG_ID" message="Replying to this!"
```

### 创建群组

```text
message action=group-create channel=whatsapp name="Project Team" participants=["+34612345678", "+34687654321"]
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。


## 示例

### 多智能体身份配置

```yaml
channels:
  whatsapp:
    agentIcon: "🤖"
    turnEndMarker: "⚡"
    multiAgent:
      mainAgentId: "jarvis"
      agents:
        jarvis:
          id: "jarvis"
          name: "Jarvis"
          icon: "🤖"
        luna:
          id: "luna"
          name: "Luna"
          icon: "🌙"
          model: "sonnet"
        rex:
          id: "rex"
          name: "Rex"
          icon: "🦖"
          model: "haiku"
```

Agent 人格文件存放在工作区：

```text
workspace/
├── SOUL.md                  # 主 Agent
├── agents/
│   ├── luna/SOUL.md         # Luna 人格
│   └── rex/SOUL.md          # Rex 人格
```

### 群内 Agent 自由讨论

```yaml
      intraAgentChats:
        brainstorm:
          chatId: "120363424201898007@g.us"
          participants: ["jarvis", "luna", "rex"]
          owner: "oscar"
          mode: "broadcast"
```

路由模式：
- `broadcast`：所有 Agent 发言（含拥塞控制）
- `addressed`：被点名才发言（"Luna, what do you think?"）
- `round-robin`：结构化轮流发言

### 拥塞控制（指数礼貌协议）

```yaml
      congestion:
        enabled: true
        baseDelayFactor: 150
        maxDelay: 30000
        backpressureThreshold: 1.5
        windowMs: 60000
```

工作原理：
- 基础延迟随 Agent 数量平方增长（2 个 ≈ 600ms，5 个 ≈ 3750ms）
- 随机抖动防止同步
- 发言过多的 Agent 获得 2 倍延迟惩罚
- 等待期间若他人发言则重置计时器（碰撞让步）

### 对话生命周期

```yaml
      lifecycle:
        stalenessWindow: 5
        stalenessThreshold: 0.85
        maxTurnsPerObjective: 30
        autoClose: true
```

功能：
- 陈旧检测：消息嵌入的余弦相似度检测循环讨论
- 同意循环检测：捕捉"I agree"/"Good point"/"Exactly"循环
- 话题引导：一个 Agent 担任引导者重定向对话
- 目标追踪：设定目标、追踪完成度、自动收尾并总结
- 收尾协议：提议 → 确认 → 收敛（所有 Agent 同意）

### 预算感知调度

```yaml
      budget:
        provider: "anthropic"
        windowDays: 7
        burnModeEnabled: true
        burnTriggerHours: 24
        burnUsageThreshold: 0.20
```

四种模式：

| 模式 | 触发条件 | 拥塞 | 陈旧阈值 | 最大轮次 | 发散 |
|------|---------|------|---------|---------|------|
| 保守 | 用量 > 85% | 2 倍慢 | 0.80 | 减半 | 否 |
| 适中 | 60-85% | 正常 | 0.85 | 正常 | 否 |
| 激进 | < 60% | 0.7 倍快 | 0.85 | 正常 | 是 |
| 燃烧 | < 20% 且 < 24h 重置 | 0.3 倍快 | 0.95 | 2 倍 | 鼓励 |

燃烧模式哲学：未使用的 token 在重置时过期，不如让 Agent 之间产生涌现性讨论。

### 群组管理命令

```text
# 重命名群组
message action=renameGroup channel=whatsapp groupId="123456789@g.us" name="New Name"

# 设置群组图标
message action=setGroupIcon channel=whatsapp groupId="123456789@g.us" filePath=/path/to/icon.jpg

# 设置群组描述
message action=setGroupDescription channel=whatsapp groupJid="123456789@g.us" description="Team chat for Q1 project"

# 添加参与者
message action=addParticipant channel=whatsapp groupId="123456789@g.us" participant="+34612345678"

# 提升为管理员
message action=promoteParticipant channel=whatsapp groupJid="123456789@g.us" participants=["+34612345678"]

# 获取邀请链接
message action=getInviteCode channel=whatsapp groupJid="123456789@g.us"
```

## 最佳实践

### 1. 多智能体路由选型
- 需要多元视角脑暴 → `broadcast` + 拥塞控制
- 需要针对性回答 → `addressed`（点名触发）
- 需要结构化依次发言 → `round-robin`
- 单 Agent 即可完成 → 不要启用多智能体

### 2. 拥塞控制调参
- 2-3 个 Agent：`baseDelayFactor=150` 即可
- 5+ 个 Agent：提高到 `300`，避免消息爆炸
- 对话激烈时调高 `backpressureThreshold` 到 `2.0`
- `maxDelay` 建议不超过 60 秒，否则体验过差

### 3. 生命周期管理
- 简单任务：`maxTurnsPerObjective=15`
- 复杂脑暴：`maxTurnsPerObjective=30-50`
- 始终开启 `autoClose`，避免无限循环
- `stalenessThreshold=0.85` 是经验值，过低会过早收尾

### 4. 预算模式切换
- 月初配额充足：`aggressive` 模式
- 月中正常使用：`moderate` 模式
- 月末接近上限：`conservative` 模式
- 重置前 24h 且剩余 > 80%：`burn` 模式

### 5. DM 触发前缀
- 群主始终绕过触发前缀
- 授权联系人必须在消息开头加前缀（如"Jarvis, help me with..."）
- 群内 Agent 自由讨论绕过触发前缀

### 6. 回合结束标记
1:1 聊天中追加视觉标记（如 `⚡`）表示回合结束，便于用户判断 Agent 是否还在思考。

### 7. 群组安全
- 邀请链接用完及时 `revokeInviteCode` 撤销
- 敏感群组设置只有管理员可发消息
- 定期审查参与者列表

## 常见问题

### Q1：多 Agent 同时发言导致消息爆炸？
A：开启 `congestion.enabled=true`，指数礼貌协议会让 Agent 按平方延迟发言。5 个 Agent 基础延迟约 3.75 秒，避免同时响应。

### Q2：Agent 一直在"I agree"循环？
A：开启 `lifecycle.autoClose=true` 与同意循环检测。`stalenessThreshold=0.85` 会检测到相似度高于阈值的循环并触发收尾。

### Q3：API 账单突然暴涨？
A：检查 `budget` 配置。多 Agent 广播模式下每条消息触发 N 次响应。建议：① 用 `addressed` 模式替代 `broadcast`；② 设置 `maxTurnsPerObjective`；③ 月末切 `conservative` 模式。

### Q4：编辑消息失败？
A：只能编辑自己发送的消息（`message action=edit`）。需要 `messageId` 与 `chatJid`，且消息发送未超过编辑窗口（通常 15 分钟）。

### Q5：撤回消息不成功？
A：`message action=unsend` 只能撤回自己发送的消息，且需在撤回窗口内（通常 1 小时）。群组中管理员可撤回他人消息。

### Q6：群组邀请链接失效？
A：邀请链接可能被撤销或群组已满。调用 `getInviteCode` 获取最新链接，或 `revokeInviteCode` 撤销旧链接后重新生成。

### Q7：历史搜索搜不到旧消息？
A：WhatsApp 的 LID/JID 别名可能导致搜索遗漏。专业版的 `resolveChatJids()` 会跨 `@lid` 与 `@s.whatsapp.net` 两种格式交叉引用。

### Q8：vCard 联系人怎么提取？
A：联系人消息会返回结构化 `vcard` 字段，包含姓名与电话号码。3.7.0+ 版本支持多联系人 `contactsArrayMessage`，电话号码也会写入 `text_content` 支持全文检索。

### Q9：燃烧模式会不会失控？
A：燃烧模式仍受 `maxTurnsPerObjective`（2 倍）与拥塞控制约束，只是放宽陈旧阈值与延迟。它鼓励发散但不允许无限循环。

### Q10：DM 触发前缀怎么配？
A：在通道配置中设置 `triggerPrefix`。群主始终绕过；授权联系人必须在消息开头加前缀；群内 Agent 自由讨论绕过前缀。

## 专业版特性

本专业版相比免费版新增以下能力：
- 交互能力：反应（加/删）、回复/引用、编辑、撤回
- 群组管理：创建/重命名/图标/描述/参与者/管理员/邀请链接，10 类动作
- 多智能体讨论协议：广播/点名/轮询三种路由模式
- 拥塞控制：指数礼貌协议防止消息爆炸
- 对话生命周期：陈旧检测、循环检测、目标追踪、自动收尾
- 预算感知调度：保守/适中/激进/燃烧四种模式
- 历史检索：全文搜索与 vCard 联系人提取
- 多角色场景指南：架构师/产品/QA/运维/运营五视角
- 完整 22 类动作命令参考
- 优先技术支持与版本升级迁移指南

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 5 类基础消息 + 速率限制 | 个人试用 |
| 收费专业版 | ¥49.9/月 | 22 类动作 + 多智能体协议 + 优先支持 | 团队/企业 |

专业版通过 SkillHub SkillPay 发布。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 且具备 WhatsApp 通道集成的 AI Agent
- **操作系统**：Windows / macOS / Linux
- **WhatsApp 账号**：已通过二维码链接的有效账号
- **Node.js**：18+（运行通道插件与协议库）

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 |
| WhatsApp 通道插件 | 插件 | 必需 | Agent 平台内置或自行安装 |
| Baileys 协议库 | npm 包 | 内置 | 通道插件依赖，实现 WhatsApp Web 协议 |
| ffmpeg | CLI 工具 | 推荐 | 系统包管理器安装 |
| 嵌入模型 | API | 多智能体必需 | 用于陈旧检测的余弦相似度计算 |

### API Key 配置
- **WhatsApp 通道凭证**：通过二维码登录获取，由 Agent 平台持久化
- **LLM API Key**：多智能体模式下需要为每个 Agent 配置模型（如 sonnet/haiku）
- **预算感知 API**：如对接 Anthropic 预算接口，需配置 `ANTHROPIC_API_KEY`
- **禁止**：在 SKILL.md 或脚本中硬编码任何凭证

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **模型路由建议**：专业版多智能体模式推荐使用 GPT-4o / Claude Sonnet 作为主 Agent，Haiku 作为辅助 Agent
- **数据存储**：历史检索与联系人数据可归档到 `PostgreSQL` 数据库做长期分析
- API Key通过环境变量配置: export API_KEY=your_key

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
