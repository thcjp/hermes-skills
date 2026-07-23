---
slug: "whatsapp-master"
name: "whatsapp-master"
version: "1.0.0"
displayName: "WhatsApp大师(专业版)"
summary: "WhatsApp 全能力版：消息/交互/群组/多智能体协作/预算调度/历史检索，22 类动作。"
license: "Proprietary"
edition: "pro"
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
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# WhatsApp大师(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 多智能体 | 支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 类别 | 动作 | 数量 |
|------|------|------|
| 消息 | 文本、媒体、投票、贴纸、语音、GIF | 6 |
| 交互 | 反应（加/删）、回复/引用、编辑、撤回 | 5 |
| 群组 | 创建、重命名、图标、描述、加人、踢人、升降权、离开、邀请码、群信息 | 10 |
| 历史 | 全文搜索、vCard 联系人提取 | 2 |
| 多智能体 | 路由、拥塞、生命周期、预算 | 4 |
### 多智能体

执行多智能体操作,处理用户输入并返回结果。

**输入**: 用户提供多智能体所需的参数和指令。

**输出**: 返回多智能体的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`多智能体`相关配置参数进行设置
#
## 适用场景

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

## 使用流程

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
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 且具备 WhatsApp 通道集成的 AI Agent
- **操作系统**：Windows / macOS / Linux
- **WhatsApp 账号**：已通过二维码链接的有效账号
- **Node.js**：18+（运行通道插件与协议库）

### 依赖说明
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
- **数据存储**：历史检索与联系人数据可归档到 `关系型数据库` 数据库做长期分析


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

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

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

