---
slug: discord-community-hub-pro
name: discord-community-hub-pro
version: "1.0.0"
displayName: Discord社区中心专业版
summary: 企业级 Discord 社区管理,支持应用命令、权益管理、角色连接与用户资料修改。
license: MIT
edition: pro
description: |-
  面向企业运营与社区管理团队的 Discord 社区全功能管理工具。

  核心能力:
  - 应用命令权限管理与批量权限配置
  - 权益(Entitlement)与订阅管理
  - 角色连接元数据读写与外部系统对接
  - 用户资料修改、服务器离开与高级身份管理
  - 多服务器批量运营与审计日志

  适用场景:
  - 企业 Discord 社区的应用命令权限治理
  - 付费订阅与权益发放管理
  - 外部系统(游戏/论坛)与 Discord 角色对接

  差异化: Pro 版在免费版只读基础上解锁应用命令、权益、角色连接与用户修改等写操作;与免费版工具格式完全兼容。

  触发关键词: 应用命令, 权益, 订阅, 角色连接, 用户修改, command, entitlement, subscription, role-connection, enterprise
tags:
- Discord
- 企业管理
- Communication
- 应用命令
- 权益管理
tools:
- read
- exec
---

# Discord 社区中心(专业版)

## 概述

Discord 社区中心专业版是一款面向企业运营与社区管理团队的 Discord 社区全功能管理工具。它在免费版只读查询能力之上,解锁应用命令权限管理、权益(Entitlement)与订阅管理、角色连接元数据读写、用户资料修改、服务器离开等高级写操作,并提供多服务器批量运营与审计能力,帮助企业管理多个 Discord 社区的应用生态、付费体系和身份对接。

专业版与免费版工具格式完全兼容:免费版的所有只读工具在专业版中可直接使用,升级后无需调整即可获得写操作能力。专业版适合企业级 Discord 社区运营、付费应用生态管理和需要外部系统角色对接的场景。

## 核心能力

| 能力模块 | 说明 | 免费版 | Pro 版 |
|:-------|:-----|:------:|:------:|
| 用户/身份 | 资料查询 | 只读 | 只读+修改 |
| 服务器/组件 | 服务器与 widget | 只读 | 只读+离开 |
| 应用命令 | 权限管理 | 不支持 | 支持(单条+批量) |
| 权益/订阅 | Entitlement 管理 | 不支持 | 支持 |
| 角色连接 | 元数据读写 | 不支持 | 支持 |
| 网关/工具 | 网关与工具 | 支持 | 支持 |
| 用户修改 | 用户名/头像 | 不支持 | 支持 |
| 多服务器运营 | 批量管理 | 不支持 | 支持 |
| 审计日志 | 操作记录 | 不支持 | 支持 |

## 使用场景

### 场景一:应用命令权限治理

企业社区注册了多个斜杠命令(slash command),需要按服务器维度批量配置各命令的可用角色范围。

```javascript
// 1. 获取某命令在服务器的当前权限
const perm = await integration.call_tool({
  tool: "discord_get_application_command_permissions",
  parameters: {
    application_id: "987654321",
    guild_id: "123456789",
    command_id: "111111"
  }
});

// 2. 批量获取所有命令的权限
const allPerms = await integration.call_tool({
  tool: "discord_get_batch_application_command_permissions",
  parameters: {
    application_id: "987654321",
    guild_id: "123456789"
  }
});

// 3. 编辑某命令的权限(需 MANAGE_GUILD)
await integration.call_tool({
  tool: "discord_edit_application_command_permissions",
  parameters: {
    application_id: "987654321",
    guild_id: "123456789",
    command_id: "111111",
    permissions: [
      { id: "222", type: 1, permission: true }  // 角色可使用
    ]
  }
});
```

### 场景二:付费订阅与权益发放

付费应用需要查询用户权益、列出订阅记录并消费消耗型权益。

```javascript
// 1. 查询用户在某应用下的权益
const entitlements = await integration.call_tool({
  tool: "discord_get_current_user_application_entitlements",
  parameters: { application_id: "987654321" }
});

// 2. 列出某 SKU 的所有订阅
const subs = await integration.call_tool({
  tool: "discord_list_sku_subscriptions",
  parameters: { sku_id: "123456789" }
});

// 3. 获取特定订阅详情
const sub = await integration.call_tool({
  tool: "discord_get_sku_subscription",
  parameters: {
    sku_id: "123456789",
    subscription_id: "sub_abc123"
  }
});

// 4. 消费消耗型权益(用户已使用该权益)
await integration.call_tool({
  tool: "discord_consume_entitlement",
  parameters: { entitlement_id: "ent_xyz" }
});

// 5. 清理测试权益
await integration.call_tool({
  tool: "discord_delete_test_entitlement",
  parameters: { entitlement_id: "ent_test_001" }
});
```

### 场景三:外部系统与 Discord 角色对接

游戏平台或论坛需将用户的外部身份(如游戏 ID)同步到 Discord 角色连接元数据。

```javascript
// 1. 获取用户当前角色连接
const roleConn = await integration.call_tool({
  tool: "discord_get_user_application_role_connection",
  parameters: { application_id: "987654321" }
});

// 2. 更新角色连接(写入游戏标签等元数据)
await integration.call_tool({
  tool: "discord_update_user_application_role_connection",
  parameters: {
    application_id: "987654321",
    metadata: {
      platform_name: "Xbox",
      platform_username: "PlayerOne",
      custom_fields: [
        { name: "等级", value: "42" },
        { name: "段位", value: "钻石" }
      ]
    }
  }
});

// 3. 清除角色连接(用户解绑)
await integration.call_tool({
  tool: "discord_delete_user_application_role_connection",
  parameters: { application_id: "987654321" }
});
```

## 快速开始

### 第一步:升级授权 scope

Pro 版写操作需更完整的 OAuth2 scope。重新连接 Discord 时确保授予:

- `identify` `guilds` `email`(基础)
- `applications.commands`(命令权限)
- `role_connections.write`(角色连接写入)
- `applications.entitlements`(权益查询)

### 第二步:验证权限

```javascript
// 确认当前授权
const auth = await integration.call_tool({
  tool: "discord_get_my_oauth2_authorization",
  parameters: {}
});

// 确认目标服务器管理权限
const member = await integration.call_tool({
  tool: "discord_get_my_guild_member",
  parameters: { guild_id: "123456789" }
});
```

编辑命令权限需用户在目标服务器具备 `MANAGE_GUILD` 和 `MANAGE_ROLES` 权限。

### 第三步:执行写操作

```javascript
// 修改当前用户名(每小时限 2 次)
await integration.call_tool({
  tool: "discord_modify_current_user",
  parameters: {
    username: "new_display_name",
    avatar: "data:image/png;base64,..."
  }
});
```

## 配置示例

### 应用命令权限完整配置

```javascript
// 批量配置多个命令的权限
const commands = ["cmd_001", "cmd_002", "cmd_003"];

for (const cmdId of commands) {
  await integration.call_tool({
    tool: "discord_edit_application_command_permissions",
    parameters: {
      application_id: "987654321",
      guild_id: "123456789",
      command_id: cmdId,
      permissions: [
        { id: "role_admin", type: 1, permission: true },
        { id: "role_member", type: 1, permission: false }
      ]
    }
  });
}
```

### 权益管理流程

```javascript
// 完整的权益发放与消费流程

// 1. 查询用户是否有有效订阅
const entitlements = await integration.call_tool({
  tool: "discord_get_current_user_application_entitlements",
  parameters: { application_id: "987654321" }
});

const activeEnt = entitlements.find(e =>
  e.type === "subscription" && !e.consumed
);

// 2. 用户使用后消费权益
if (activeEnt) {
  await integration.call_tool({
    tool: "discord_consume_entitlement",
    parameters: { entitlement_id: activeEnt.id }
  });
}
```

### 角色连接批量同步

```javascript
// 从外部系统批量同步用户角色连接
const externalUsers = [
  { discord_id: "111", gamer_tag: "Alpha", level: 50 },
  { discord_id: "222", gamer_tag: "Beta", level: 30 }
];

for (const u of externalUsers) {
  await integration.call_tool({
    tool: "discord_update_user_application_role_connection",
    parameters: {
      application_id: "987654321",
      metadata: {
        platform_name: "Xbox",
        platform_username: u.gamer_tag,
        custom_fields: [
          { name: "等级", value: String(u.level) }
        ]
      }
    }
  });
}
```

### 服务器离开管理

```javascript
// 离开指定服务器(高影响操作)
await integration.call_tool({
  tool: "discord_leave_guild",
  parameters: { guild_id: "123456789" }
});
```

## 最佳实践

1. **写操作二次确认**: 应用命令权限编辑、权益消费、角色连接更新、用户修改等写操作建议执行前二次确认。Pro 版支持审计配置,对高影响操作(leave_guild、delete_test_entitlement、delete_role_connection)强制确认并记录。

2. **命令权限最小化**: 应用命令权限遵循最小可用原则。默认禁止,按角色显式开放。管理类命令只对管理员角色开放,普通命令对所有成员开放。使用 `get_batch_application_command_permissions` 定期审计权限配置。

3. **权益消费幂等性**: `consume_entitlement` 是幂等操作,重复消费同一权益不会重复扣减。但仍建议在业务侧记录消费状态,避免重复调用。

4. **测试权益及时清理**: 测试环境产生的测试权益(test entitlement)用完及时用 `delete_test_entitlement` 清理,避免污染生产数据。建议在 CI/CD 流程中加入清理步骤。

5. **角色连接同步频率**: 外部系统与 Discord 角色连接的同步不宜过高频,建议事件驱动(用户等级变化时同步)或低频轮询(每小时一次),避免触发 API 频率限制。

6. **用户名修改限频**: Discord 限制用户名每小时最多修改 2 次。批量修改场景需分散执行,单用户每小时不超过 1 次为宜。

7. **Bearer 令牌专用**: 编辑命令权限、获取权益等操作必须使用 OAuth2 Bearer 令牌,机器人令牌会报错。确认集成网关使用的是 Bearer 令牌授权。

8. **审计日志保留**: 企业场景建议保留 90 天以上审计日志,记录所有写操作的执行人、目标、参数和结果,满足合规追溯需求。

9. **与免费版兼容**: Pro 版完全兼容免费版只读工具。升级后原有查询指令无需修改,直接获得写操作能力。建议生产环境统一使用 Pro 版。

## 常见问题

### Q1: 编辑命令权限报「Missing MANAGE_GUILD permission」?

编辑应用命令权限需要当前用户在目标服务器具备 `MANAGE_GUILD` 和 `MANAGE_ROLES` 权限,且使用 OAuth2 Bearer 令牌(机器人令牌会报错)。请确认:用户是服务器管理员或有管理权限的角色;集成网关使用 Bearer 令牌;OAuth2 授权包含 `applications.commands` scope。

### Q2: 「Role connection write scope missing」是什么原因?

角色连接写入需要 OAuth2 授权包含 `role_connections.write` scope。若当前授权缺失,需重新连接 Discord 并补全该 scope。重新授权后即可正常调用 `discord_update_user_application_role_connection`。

### Q3: 权益查询返回为空?

确认:查询的 `application_id` 正确;用户确实有该应用的付费订阅;OAuth2 授权包含 `applications.entitlements` scope。测试权益需通过 `discord_delete_test_entitlement` 单独管理,不在正式权益列表中返回。

### Q4: 角色连接的 custom_fields 有什么限制?

`custom_fields` 是应用在 Discord Developer Portal 中预先定义的元数据字段。字段 `name` 必须与预定义一致,`value` 为字符串。未预定义的字段会被忽略。最多支持 8 个自定义字段。

### Q5: `discord_delete_test_entitlement` 和 `discord_consume_entitlement` 有什么区别?

`consume_entitlement` 用于标记消耗型权益(如一次性道具)为已使用,正式权益不会被删除,只是状态变更;`delete_test_entitlement` 用于删除测试环境产生的测试权益,是物理删除,仅对测试权益有效,不影响正式权益。

### Q6: 多服务器批量运营如何管理?

Pro 版支持遍历服务器列表批量执行操作。建议:按操作类型分组批量执行;配置频率限制避免触发 API 限流;记录每个服务器的执行结果汇总;失败项单独重试。大规模批量操作建议在低峰时段执行。

### Q7: 审计日志记录哪些内容?

审计日志记录:操作时间、操作人、工具名称、目标(application_id/guild_id/user_id)、参数摘要、结果(成功/失败)、错误信息。高影响操作(leave_guild、delete_test_entitlement、delete_role_connection)额外记录操作前状态快照。日志建议加密存储,保留 90 天以上。

### Q8: Pro 版能管理机器人的应用命令吗?

可以。通过 `application_id`(机器人的应用 ID)管理其在各服务器的命令权限。但需注意:编辑命令权限使用的是用户的 OAuth2 Bearer 令牌(需用户有管理权限),而非机器人令牌。这是设计上的权限分离。

## 依赖说明

### 运行环境

- **Agent 平台**: 支持解析 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux(推荐 Linux 用于生产环境)
- **网络**: 需稳定访问 Discord API 与集成网关
- **浏览器**: OAuth 授权流程需在浏览器中完成

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM 能力 | API | 必需 | 由 Agent 内置大模型提供 |
| 集成网关插件 | 插件 | 必需 | Agent 平台插件市场安装 |
| Discord OAuth2 | 授权 | 必需 | Discord Developer Portal 注册应用 |
| Discord API | 服务 | 必需 | Discord 平台提供 |
| 浏览器 | 运行时 | 必需 | 用于 OAuth 授权流程 |
| 外部系统 | 集成 | 可选 | 游戏平台/论坛等角色对接源 |

### API Key 配置

- **OAuth2 应用**: 在 Discord Developer Portal 注册 OAuth2 应用,获取 Client ID 和 Client Secret。
- **完整授权 scope**: Pro 版需更完整的 scope:`identify` `guilds` `email` `applications.commands` `role_connections.write` `applications.entitlements`。重新连接时务必补全。
- **Bearer 令牌**: 写操作(命令权限、权益、角色连接)必须使用 OAuth2 Bearer 令牌,非机器人令牌。集成网关自动管理令牌刷新。
- **审计存储**: 审计日志建议配置独立存储路径,加密存储,设置保留策略(建议 90 天以上)。

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令 + 部分功能需 `exec` 执行能力)
- **说明**: 以自然语言指令驱动 Agent 通过集成网关调用 Discord 工具完成社区管理与写操作
- **适用规模**: 企业级,多服务器批量运营,支持应用生态与付费体系管理
- **兼容性**: 与 `discord-community-hub-free` 工具格式完全兼容,可平滑升级
- **支持级别**: 优先支持(Pro 版享有问题优先响应与功能迭代建议通道)
