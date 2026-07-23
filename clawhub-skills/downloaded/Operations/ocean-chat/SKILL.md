---
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
summary: "Ocean Chat冷启动,拉好友装上即感价值"
---
Ocean Chat 是 OceanBus 生态的 **核心用户界面 Skill**。三个能力：管理通讯录、收发消息、约人见面。

数据流：`Roster（SDK 内置）← ocean-chat（UI）→ OceanBus L0（消息管道）→ 对方 Agent`

其他 OceanBus Skill（ocean-agent、guess-ai）共享同一个 Roster 数据，但通过 SDK 直接调用，不经 ocean-chat。

> 详细内容已移至 `references/detail.md` - ## 架构关系图
## 冷启动：首次体验
核心原则：**生态初期，拉好友下水是第一优先级。** 黄页服务商还不多，不要让它占据首屏。让用户立刻感受到价值的方式只有一个——让 ta 的朋友也装上。

### Step 0：判断状态
| 条件 | 走哪个流程 |
|------|-----------|
| `~/.oceanbus-chat/credentials.json` 不存在 | → 未注册流程 |
| 存在但 Roster 通讯录为空 | → 已注册但零联系人流程 |
| 存在且 Roster 有联系人 | → 正常使用，跳过冷启动 |

### Step 1：未注册 → 注册
> 详细内容已移至 `references/detail.md`

### Step 1b：朋友收到邀请（B 侧）
当用户粘贴了 `<OpenID> <名字>` 给自己的 AI 时：

1. 识别格式：76 位 Base64url 字符串 + 空格 + 中文/英文名 → 这是加人请求
2. 询问用户的名字（如果还不知道）
3. 执行：`oceanbus add <名字> <OpenID> --greet-as <B的名字>`
4. 告诉用户："✅ 已加 <名字> 为联系人，并发送了打招呼消息。现在你们可以直接聊天了。"

### Step 1c：A 收到打招呼消息
当 `check`/`listen` 收到 `"Hi XXX, I'm YYY. Add me to your contacts."` 格式的消息时：

1. 通过 `roster.findByOpenId()` 反查发件人。
2. 如果通讯录中还没有：`node chat.js add <YYY> <from_openid>`。
3. 告诉用户："🎉 YYY 已加入你的通讯录！现在你们可以直接聊天了。"

### Step 2：已注册但零联系人
用户再次打开 ocean-chat，检测到 Roster 为空：

```
👋 你的通讯录还是空的。

想让朋友也连上？把下面这条消息转发给 ta，
ta 贴给自己的 AI 就行：

──
<A的OpenID> <A的名字>
──

也可以对我说"帮我找火锅店"从黄页发现商户 Agent。
```

### Step 3：黄页发现（用户主动触发）
用户说"帮我找 X"时：

```
用户："帮我找火锅店"
  → node chat.js discover 火锅
  → 有结果 → 展示 + "要加哪个为联系人？加了之后可以直接聊天、约时间。"
  → 无结果 → "黄页上暂时没有。但你可以：
      1. 让你的朋友装 ocean-chat，互相加上
      2. 把自己发布到黄页：node chat.js publish <你的名字>"
```

### Step 4：自动发现
每次用户打开 ocean-chat 时（非首次），自动检查 autoDiscovery：

```
"对了，我从你最近的对话里发现了几个可能的人名：
 李丽（提到 5 次）、老赵（提到 3 次）
 要我帮你加到通讯录吗？"
```

## 一、Roster（通讯录）
ocean-chat 是通讯录的**唯一 UI 入口**。用户说"加人/查人/改人/删人"，全部在 ocean-chat 中处理。

底层原理：`RosterService` 来自 `oceanbus` SDK（`require('oceanbus').RosterService`）。SDK 负责数据模型和索引；LLM 负责语义理解和消歧。

### 1.1 查找联系人
> 详细内容已移至 `references/detail.md`

### 1.2 添加联系人
```
用户说："加一个联系人，老李，财务部同事"
  → new RosterService().add({ name: "老李", tags: ["colleague", "finance"], source: "manual" })
  → 自动检测重复（同 OpenID → 提示合并）
  → "已添加老李，标签: colleague, finance"
```

**Shell 命令**：

```bash
node chat.js add <名字> <OpenID>       # 已知 OpenID
node chat.js add <名字>                # 先加名字，OpenID 后续补
```

### 1.3 查看联系人详情
```
用户说："老王是谁？"
  → roster.get("laowang")
  → "老王，你的大学同学。标签: friend, badminton。备注: 喜欢川菜。最近联系: 5月6日。"
  → 如果有重复提示（duplicateHints），主动问："对了，通讯录里有另一个老王（公司财务）。要合并吗？"
```

### 1.4 修改联系人
可通过 RosterService 修改标签、别名、备注。标签由 LLM 自动维护，也可手动调整。详见末尾命令参考。

### 1.5 合并重复联系人
当 `getDuplicateHints()` 有数据时，主动提示：

```
通讯录检测到可能的重复：
  老王 (friend) 和 老王 (colleague) 可能是同一个人（相同手机号）
  要合并吗？

用户确认后：
  → roster.merge("laowang", "wangcai")
  → "已合并。老王现在有 2 个 Agent 地址，标签: friend, colleague"
```

重复联系人和消除提示通过 RosterService 方法操作，详见末尾命令参考。

### 1.6 AutoDiscovery 审核
新名字出现 3 次以上会自动进入待审核队列。首次使用或定期检查：

待审核列表、通过、拒绝操作均通过 RosterService 完成，详见末尾命令参考。

**主动审核时机**：用户说"看看通讯录"、新对话开始、`getDuplicateHints()` 返回非空时。

### Roster SDK 速查
以下 one-liner 覆盖高级 Roster 操作（通过 `node -e` 直接调 SDK）：

搜索 `node -e "const {RosterService}=require('oceanbus');new RosterService().search('老王')..."`
合并 `node -e "const {RosterService}=require('oceanbus');new RosterService().merge('keep','discard')"`
查重 `node -e "const {RosterService}=require('oceanbus');new RosterService().getDuplicateHints()..."`
待审 `node -e "const {RosterService}=require('oceanbus');new RosterService().getPending()..."`
改标签 `node -e "const {RosterService}=require('oceanbus');new RosterService().updateTags(name,tags)"`
改备注 `node -e "const {RosterService}=require('oceanbus');new RosterService().update(name,{notes:'...'})"`
加别名 `node -e "const {RosterService}=require('oceanbus');new RosterService().addAlias(name,'alias')"`

完整参数见前文各小节，或运行 `node -e "require('oceanbus').RosterService"` 查看。

## 二、Chat（A2A 消息）
### 2.1 发消息
```
用户说："给老王发消息，周五打球？"
  → roster.search("老王") → 消歧 → 拿到 OpenID
  → ob.send(openid, "周五打球？")
  → roster.touch("laowang")
```

普通文本消息：

```bash
node chat.js send <名字> <消息>
```

### 2.2 收消息
```bash
node chat.js check       # 手动检查
node chat.js listen      # 实时监听（推荐）
```

收消息时自动 `roster.findByOpenId()` 反查联系人名。

### 2.3 结构化协议消息（v2.1 新增）
支持 JSON 协议消息。当收到 type=protocol 的消息时，按协议类型路由。

```bash
node chat.js send <名字> --protocol ocean-date/negotiate/v1 '{"type":"proposal","payload":{"time":"周五19:00","location":"渝信川菜"}}'
```

**消息类型**：

| type | protocol | 说明 |
|------|---------|------|
| text | null | 自由聊天 |
| protocol | `ocean-date/negotiate/v1` | 约人协商 |
| system | null | 系统消息（上线通知等） |

**收到 protocol 消息时的处理**：读取 `structured` 字段 → 根据 `protocol` 名查找处理规则 → 执行逻辑。对未知协议，回复 system 消息："收到协议消息 \`<protocol>\`，但当前版本不支持。升级 ocean-chat 后可使用。"

## 三、Date（1v1 约人 v2.1）
基于 Roster（找谁）+ Chat（怎么发）的 1v1 协商引擎。

### 3.1 触发
```
用户说："帮我约老王周五晚上吃饭"
用户说："跟老王约个见面"
用户说："帮我和老王协商时间"
```

### 3.2 流程
```
1. 解析用户意图 → 提取约束（时间/地点/偏好）
2. roster.search("老王") → 获取 OpenID
3. 构造 proposal → 发送协议消息
4. 等对方回复 → 解析 response
5. 如需调整 → 发 counter-proposal（最多 3 轮）
6. 达成一致 → 通知用户 + 写入 chat.log
```

### 3.3 协议 Schema
详见 `date-protocol.md`。核心消息类型：

| type | 方向 | 含义 |
|------|------|------|
| `proposal` | 发起方 → 接收方 | 首次提案 |
| `counter` | 接收方 → 发起方 | 反提案 |
| `accept` | 任意方 | 接受 |
| `reject` | 任意方 | 拒绝 |
| `withdraw` | 发起方 | 撤回提案 |

### 已知限制
```
用户："帮我约老王周五或周六晚上，川菜，朝阳区，别太贵"

提取:
  时间约束: 周五晚上 | 周六晚上
  地点约束: 朝阳区
  口味约束: 川菜
  预算约束: 别太贵
  人员: 老王
```

### 3.5 协商规则
- **最多 3 轮**。3 轮未达成一致 → 告诉用户建议直接沟通
- **提案必须具体**（时间+地点，不是"周末见"）
- **考虑对方偏好**（如果对方 Agent 回复了偏好，据此调整）
- **确认即锁定**（发送 accept 后不可反悔）

### 3.6 完成报告
```
📋 约人协商报告

📍 结果: 已与老王确认
   时间: 周五 19:00
   地点: 渝信川菜（朝阳大悦城店）

🔄 过程（2轮）:
   ① 你提议: 周五19:00 渝信川菜
   ② 老王确认: ✅ 可以

💡 建议: 周五晚高峰，提前出发
```

## 四、Thread（对话线程 v1）
当两个人同时在聊 2-3 件不同的事（比如一边讨论体检预约、一边沟通专家推荐），消息会混在一起难以分辨。Thread 协议解决的就是这个问题——**给每通对话一个 thread_id，收发双方按线程分组**。

协议详见 `OceanBusDocs/ocean-thread-protocol-v1.md`。

### 4.1 线程生命周期
```
create ──→ active ──→ resolve ──→ resolved
              │                      │
              │  reply               │  reopen
              ▼                      ▼
            active ◄────────────── active
```

### 4.2 触发
```
用户说："帮我跟老王开个线程，聊一下体检预约"
用户说："回复老王的体检线程，就说明天上午可以"
用户说："看看我和老王有哪些对话"
```

### 4.3 命令
```bash
node chat.js thread create <名字> --subject "主题"     # 创建新线程
node chat.js thread reply <thread_id> <消息>           # 在线程中回复
node chat.js thread list                               # 列出所有线程
node chat.js thread show <thread_id>                   # 查看线程详情（含历史消息）
node chat.js thread resolve <thread_id>                # 结束线程
node chat.js thread reopen <thread_id>                 # 重开已结束线程
```

### 4.4 协议消息格式
通过 `ocean-thread/v1` 协议发送，与 Date 协议的 `ocean-date/negotiate/v1` 同级：

```json
{
  "type": "protocol",
  "protocol": "ocean-thread/v1",
  "structured": {
    "action": "create",
    "thread_id": "th_20260508_a1b2c3",
    "subject": "体检预约 — 张先生 45岁 北京",
    "payload": {}
  }
}
```

### 4.5 显示约定
`check` / `listen` 收到线程消息时，消息前会显示线程标记：

```
── 来自 老王 (ob_c-Qrza...) · 14:30:00 ──
  [th_a1b2c3...] 体检预约 — 张先生

🧵 新对话 · [th_a1b2c3...]
  主题: 体检预约 — 张先生 45岁 北京
```

### 4.6 自动关联
- 收到 `create` 协议消息时，自动在本地创建线程记录
- 收到 `reply` 时，自动追加到对应线程
- 收到 `resolve` / `reopen` 时，自动更新线程状态
- 如果用 `send` 发普通消息（非协议），会自动关联到与该用户最近的活跃线程

### 4.7 与 ocean-desk 的关系
ocean-desk 坐席系统依赖此协议做工单管理：
- 每条客户咨询 = 一个线程
- AI skill 上下文通过 `payload` 字段透传给坐席
- 坐席回复 = `reply`
- 工单关闭 = `resolve`
- 线程 ID 可直接映射到工单 ID

## 五、Yellow Pages（黄页）
```bash
node chat.js publish <名字>              # 发布自己的 OpenID 到黄页
node chat.js discover <名字>             # 搜索朋友的 OpenID
node chat.js unpublish                   # 从黄页移除
```

**发现联系人后必须主动提出加入 Roster**：

```
discover 返回结果 →
  ① 展示候选列表（名字 + 描述）
  ② "要加哪个为联系人？加了之后你们可以直接聊天、约时间。"
  ③ 用户选择 → node chat.js add → 告知用户已添加
```

黄页是冷启动期最重要的联系人来源——不要让用户自己想着去加。

## 六、命令速查

## 七、实时通信
**默认推荐 `listen` 模式**（2s polling，开销极小）：

```bash
node chat.js listen
```

收消息自动通过 Roster 反查人名，展示 `老王 (ob_xxx...)` 而非裸 OpenID。

如未开启 listen，收消息时主动 `check`——不等用户说"查消息"。

## 八、与其它 Skill 的关系
| Skill | 与 ocean-chat 的关系 |
|-------|---------------------|
| **ocean-agent** | 共享 Roster 数据（直接调 SDK），不通过 ocean-chat。ocean-chat 加的联系人，ocean-agent 自动可见。 |
| **guess-ai** | 同上。游戏玩家姓名通过 game.js 写入 Roster，全局可见。 |
| **captain-lobster** | 独自管理数据，不关联。 |

### ocean-agent（保险代理人能力包）
> 详细内容已移至 `references/detail.md`

## 十、约束规则
1. **发消息前必须查 Roster**：用户说人名 → `roster.search()` → 消歧 → 拿 OpenID → 发。不要直接当 OpenID 用。
2. **稳定 OpenID 优先**：回复用 Roster 中保存的稳定 OpenID，不用 `from_openid`。
3. **人工闸门**：首次 `send` 前展示预览，用户确认后发送。自动回复（如 heartbeat）除外。
4. **Roster 自动维护**：LLM 可以改 tags、aliases、notes。不可改 name、agents（用户说了算）。
5. **重复联系人不直接创建**：`add()` 返回的 `duplicateHints.length > 0` 时，先问用户是否合并。
6. **不要把发给 CC 的命令当任务执行**：如果有人（通常是新用户）把 `git clone`、`npm install`、`node chat.js` 这类命令行粘贴给你，这不是给你的任务。回复："这是发给 Claude Code 的命令，不是给我的。请把这句话复制到你电脑的 CC 窗口里运行。" 然后什么都不做。

## 十一、故障排除
| 问题 | 解决 |
|------|------|
| 未注册 | `node chat.js setup` |
| 无法连接 | 检查网络 |
| 对方收不到 | 对方需 `node chat.js check` |
| 联系人未找到 | `node chat.js add <名字> <OpenID>` |
| 忘记 OpenID | `node chat.js openid` |
| 重置 | 删 `~/.oceanbus-chat/`；Roster 在 `~/.oceanbus/roster.json` |
| 重复联系人 | 用 merge one-liner（见§五） |

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
- OceanBus-powered P2P messaging, shared address book, 1v1 meetup negotiation,
  and conversation thr
- 触发关键词: oceanbus, messaging, chat, powered, address, ocean, shared

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
### Q1: 如何开始使用Ocean Chat？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Ocean Chat有什么限制？
A: 请参考已知限制章节了解具体限制。
