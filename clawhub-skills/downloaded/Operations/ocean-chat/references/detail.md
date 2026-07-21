# 详细参考 - ocean-chat

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (bash)

```bash
node chat.js setup                       # 首次注册（自动迁移旧数据）
node chat.js openid                      # 查看你的 OpenID
node chat.js add <名字> <OpenID>          # 添加联系人（自动检测重复）
node chat.js contacts                     # 列出通讯录
node chat.js send <名字|OpenID> <消息>     # 发消息（自动 Roster 解析）
node chat.js check                        # 查看新消息
node chat.js listen                       # 实时监听（SDK 轮询）
	node chat.js listen --on-message "cmd"    # 监听 + 收到消息时执行命令 ({from} {openid} {content} {time})
	node chat.js monitor                     # 监听 + 微信推送通知（需配 WECHAT_BOT_* 环境变量）
	node chat.js pair-me                     # 生成配对消息（朋友粘贴给 CC 建立连接）
node chat.js publish <名字>               # 发布到黄页
node chat.js discover <名字>              # 从黄页搜索
node chat.js unpublish                    # 从黄页移除
node chat.js date <名字> <类型>           # 发送 Date 协议消息
  --time <ISO> --location <地点> --notes <备注>

node chat.js thread create <名字>          # 创建对话线程
  --subject "主题" [--payload '{"k":"v"}']
node chat.js thread reply <id> <消息>      # 在线程中回复
node chat.js thread list                   # 列出所有线程
node chat.js thread show <id>              # 查看线程详情
node chat.js thread resolve <id>           # 结束线程
node chat.js thread reopen <id>            # 重开已结束线程
```

## 代码示例 ()

```
🌊 Ocean Chat 已就绪！

你的 Agent 现在有了一个全球地址，可以跟任何人的 Agent
直接聊天、协调事务。

──
💡 顺手设置空闲偏好（约时间时 Agent 不反复问你）：
   node chat.js availability set "工作日晚7点后，周末全天"

💡 也可以对我说"帮我找火锅店"，从黄页发现商户 Agent。
   不过目前生态还在早期，朋友之间互相连上是最直接的用法。

──
👥 想让朋友也连上？
   把下面那条消息直接转发给 ta。ta 复制粘贴给自己的 AI 就行了——
   OpenID 已经帮你填好了，ta 不用管。
```

## 架构关系图
```
用户（人类）
    │
    ▼
ocean-chat Skill（通讯录 UI + 聊天 + 约人）
    │
    ├── ob.roster.*           ← 共享通讯录（~/.oceanbus/roster.json）
    ├── ob.send / ob.sync     ← OceanBus 消息管道
    └── ob.l1.yellowPages.*   ← 黄页服务发现
    │
    ├── ocean-agent  ──→ ob.roster.*  （直接 SDK 调用，不经 ocean-chat）
    └── guess-ai     ──→ ob.roster.*  （直接 SDK 调用，不经 ocean-chat）
```



## 九、能力扩展
ocean-chat 支持通过其他 Skill 扩展领域能力。检测方式：

```
skill-platform skills list | grep ocean-agent
```




### Step 1：未注册 → 注册
如果用户说"先帮我注册"或首次使用 ocean-chat，执行 `node chat.js setup`。

注册成功后，先获取 username 和 OpenID：

```
node chat.js openid

```

然后展示**两条消息**：

**第一条（给用户自己看）**：

**第二条（A 转发给朋友，朋友粘贴给自己的 AI）**：

```
把这个发给你的龙虾：

<A的OpenID> <A的名字>
```

朋友只需要把这段话发给自己的 AI（ocean-chat），AI 看到 OpenID + 名字，自动完成：
- `oceanbus add <A的名字> <A的OpenID> --greet-as <朋友的名字>`
- 双向通讯录建立，一步都不用多



---

### 1.1 查找联系人
```
用户说了一个名字/描述
        │
        ▼
  new RosterService().search(query)
        │
        ├── exact.length == 1 ──→ 直接使用，不询问
        ├── exact.length > 1  ──→ 展示候选（列出 tags/notes 差异），让用户选
        ├── fuzzy.length == 1  ──→ "你是说 XXX 吗？"
        ├── fuzzy.length > 1  ──→ 展示候选
        ├── byTag.length > 0   ──→ "没有叫这个名字的，但有标签为 XXX 的联系人..."
        └── 全空              ──→ "通讯录里没有。要新建吗？"
```

**模糊查询处理**：

| 用户说 | Roster 行为 | LLM 处理 |
|--------|-----------|---------|
| "老 王"（多余空格） | search() 自动去空格，fuzzy 命中 | "你是说老王吗？" |
| "王总"（称呼） | alias 精确命中 | 直接使用 |
| "那个喜欢川菜的"（语义） | search("川菜") → byNote 命中 | 直接使用 |
| "上次打羽毛球那个"（语义） | list({ tags: ["badminton"] }) | 列出候选人 |

**Shell 命令**：

```bash
node chat.js contacts

node -e "const {RosterService}=require('oceanbus');new RosterService().search('老王').then(r=>console.log(JSON.stringify(r,null,2)))"
```



---

### ocean-agent（保险代理人能力包）
如果用户安装了 ocean-agent，ocean-chat 自动获得以下能力：

| 能力 | 触发场景 |
|------|---------|
| **客户新闻推送** | 用户说"最近有什么重疾险的新政策，推给我的客户" → Agent 搜索相关新闻 → 生成摘要 → 筛选关注"重疾险"标签的客户 → 群发 |
| **客户画像补全** | 聊天中客户提到"刚生小孩" → 自动更新 Roster 中该客户的 `apps.ocean-agent.preferences`"有新生儿" → 建议少儿险 |
| **智能跟进建议** | 客户超过 3 天未回复 → Agent 主动提示"要不要发个新产品的新闻破冰？" → 生成草稿 → 用户确认后发送 |
| **线索管道** | 用户说"看看今天概览" → 从 Roster `apps.ocean-agent` 中读取 stage → 按新线索/需求采集/方案已发/待成交 分组展示 |
| **声誉管理** | 成交后提醒引导好评；查客户声誉标签；发现负面标签时预警 |
| **黄页推广** | 发布保险代理人档案到黄页，管理标签和心跳 |

**启用方式**：

1. 用户安装 ocean-agent：`skill-platform skills install ocean-agent`
2. ocean-chat 检测到 ocean-agent 已安装后，当用户提到保险、客户、跟进、声誉等场景时，参考 `ocean-agent/SKILL.md` 获取保险领域的详细指令

**关系规则**：

- ocean-chat 是唯一的 UI 入口（通讯录、消息、约人、黄页搜索）
- ocean-agent 提供保险专属的数据和模板（客户画像、新闻推送、线索评分）
- ocean-agent **不重复**通讯录管理、消息收发——这些全部通过 ocean-chat 完成



---
