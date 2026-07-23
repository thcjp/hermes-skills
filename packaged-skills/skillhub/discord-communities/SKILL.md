---
slug: "discord-communities"
name: "discord-communities"
version: "1.0.0"
displayName: "Discord社区管理"
summary: "Discord社区管理助手,覆盖OAuth连接、公会查询、成员权限、应用命令与商业订阅全流程"
license: "Proprietary"
description: |-
  Discord 社区管理专业版 —— 基于 ClawLink OAuth 集成的一站式 Discord 社区运营助手。
  覆盖用户身份、公会与小组件、应用命令权限、商业权益(SKU/订阅/消耗)、
  角色连接元数据、网关与邀请解析等核心领域。

  核心能力:
  - 用户身份与连接管理:获取当前用户、OIDC 声明、OAuth2 授权详情、第三方连接清单
  - 公会与组件访问:列出公会、获取成员信息、查询公会模板与小组件(JSON/PNG)
  - 应用命令权限:批量获取与编辑命令权限(需 MANAGE_GUILD)
  - 商业权益管理:列出 SKU 订阅、查询权益、消耗与删除测试权益
  - 角色连接元数据:读取、更新、删除用户应用角色连接
  - 网关与工具:WebSocket 网关 URL、公钥验证、邀请解析、贴纸包列表
  - 风险分级:自动识别 safe / confirm / high_impact 操作并要求显式确认

  适用场景:
  - 社区运营者批量盘点公会成员与角色
  - 应用开发者验证用户订阅与权益状态
  - 内容平台同步 Discord 角色连接(如 Xbox Gamertag)
  - 自动化脚手架:用小组件 PNG 嵌入文档与邀请解析落地页

  不适用于:使用 Bot Token 调用需要 Bearer Token 的端点、需发送消息或管理频道的场景。
tags:
  - Communication
  - 社区运营
  - 开发者工具
  - OAuth集成
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Discord 社区管理

基于 ClawLink OAuth 的 Discord 社区管理助手,围绕用户身份、公会、应用命令权限、商业权益与角色连接五大领域提供只读与变更操作。所有变更操作遵循风险分级策略,`confirm` 与 `high_impact` 操作需显式确认。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力
### 1. 先验证 ClawLink 集成可用
```javascript
// 确认 Discord 集成已连接
clawlink_list_integrations();
// 列出可用工具
clawlink_list_tools({ integration: "discord" });
```

未连接时返回 `integration_not_found`,需先完成 OAuth 配对流程。

**输入**: 用户提供先验证 ClawLink 集成可用所需的指令和必要参数。
**处理**: 按照skill规范执行先验证 ClawLink 集成可用操作,遵循单一意图原则。
### 2. 鉴权方式必须匹配

| 鉴权方式 | 适用工具 | 限制 |
|---------|---------|------|
| OAuth2 Bearer Token | 用户身份、商业权益、角色连接 | 需用户授权对应 scope |
| Bot Token | 应用命令权限查询(部分端点) | 写操作多数不支持 |

调用 `discord_modify_current_user`、`discord_update_user_application_role_connection` 等变更类工具必须使用 Bearer Token,Bot Token 会返回 `401 Unauthorized`。

### 3. 风险分级执行策略
| 风险等级 | 典型工具 | 执行策略 |
|---------|---------|---------|
| safe | `discord_get_my_user`、`discord_list_my_guilds` | 直接执行 |
| confirm | `discord_edit_application_command_permissions`、`discord_modify_current_user` | 需显式确认 |
| high_impact | `discord_leave_guild`、`discord_delete_test_entitlement` | 二次确认 + 影响范围说明 |

#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 公会成员盘点 | 公会 ID | 成员角色、昵称、加入时间列表 |
| 订阅权益核验 | 应用 ID + SKU ID | 用户权益清单与订阅状态 |
| 角色连接同步 | 应用 ID + 自定义字段 | 更新后的角色连接元数据 |
| 公会小组件嵌入 | 公会 ID + 渲染类型 | JSON 数据或 PNG 图片字节 |

## 使用流程

1. 调用 `clawlink_list_integrations` 确认 Discord 集成已配对
2. 用 `discord_get_my_oauth2_authorization` 检查 scope 是否覆盖目标工具
3. 按 `safe → confirm → high_impact` 顺序执行,变更操作需用户显式确认
4. 商业权益类操作完成后,建议调用只读工具验证结果
5. 异常时优先检查鉴权方式与 scope,再排查权限缺失

## 工具参考

### 用户与身份

| 工具 | 风险 | 用途 |
|------|------|------|
| `discord_get_my_user` | safe | 获取当前用户资料(含 email,如授权) |
| `discord_get_user` | safe | 按 ID 获取任意用户(`@me` 表示当前用户) |
| `discord_get_openid_connect_userinfo` | safe | 获取 OIDC 声明(sub/email/picture/locale) |
| `discord_get_my_oauth2_authorization` | safe | 获取授权详情、scope、过期时间 |
| `discord_list_my_connections` | safe | 列出已绑定的第三方账户 |
| `discord_list_my_guilds` | safe | 列出当前用户所在公会(部分字段) |
| `discord_get_my_guild_member` | safe | 获取当前用户在指定公会的成员信息 |

### 公会与组件

| 工具 | 风险 | 用途 |
|------|------|------|
| `discord_get_guild_template` | safe | 按模板 code 获取公会模板 |
| `discord_get_guild_widget` | safe | 获取公会小组件 JSON(需启用 widget) |
| `discord_get_guild_widget_png` | safe | 获取公会小组件 PNG |
| `discord_leave_guild` | high_impact | 当前用户退出指定公会 |

### 应用命令权限

| 工具 | 风险 | 用途 |
|------|------|------|
| `discord_get_application_command_permissions` | safe | 获取指定命令权限 |
| `discord_get_batch_application_command_permissions` | safe | 批量获取公会内命令权限 |
| `discord_edit_application_command_permissions` | confirm | 编辑命令权限(需 MANAGE_GUILD) |

### 商业权益

| 工具 | 风险 | 用途 |
|------|------|------|
| `discord_get_current_user_application_entitlements` | safe | 获取用户对应用的权益 |
| `discord_get_sku_subscription` | safe | 按 ID 获取 SKU 订阅 |
| `discord_list_sku_subscriptions` | safe | 列出 SKU 的全部订阅 |
| `discord_consume_entitlement` | confirm | 标记可消耗权益为已消耗 |
| `discord_delete_test_entitlement` | high_impact | 删除测试权益 |

### 角色连接

| 工具 | 风险 | 用途 |
|------|------|------|
| `discord_get_user_application_role_connection` | safe | 获取用户应用角色连接 |
| `discord_update_user_application_role_connection` | confirm | 更新角色连接元数据(需 role_connections.write) |
| `discord_delete_user_application_role_connection` | high_impact | 删除角色连接元数据 |

### 网关与工具

| 工具 | 风险 | 用途 |
|------|------|------|
| `discord_get_gateway` | safe | 获取 WebSocket 网关 URL |
| `discord_get_public_keys` | safe | 获取 OAuth2 公钥(用于验签外部 JWT) |
| `discord_invite_resolve` | safe | 解析邀请 code 获取详情 |
| `discord_list_sticker_packs` | safe | 列出 Nitro 贴纸包 |

## 案例展示

### 案例1: 公会成员盘点与角色核验

社区运营者需要快速盘点当前用户在某公会的成员身份与所持有的角色。

```javascript
// 1. 列出当前用户所在公会(部分字段)
const guilds = await clawlink_call_tool({
  tool: "discord_list_my_guilds",
  parameters: {}
});
// 返回: [{ id, name, owner, permissions, ... }]

// 2. 获取当前用户在指定公会的成员信息
const member = await clawlink_call_tool({
  tool: "discord_get_my_guild_member",
  parameters: { guild_id: "123456789012345678" }
});
// 返回: { roles: [...], nick, joined_at, premium_since }

// 3. 验证当前 OAuth2 授权范围
const auth = await clawlink_call_tool({
  tool: "discord_get_my_oauth2_authorization",
  parameters: {}
});
// 返回: { application: {...}, scopes: ["identify","guilds"], expires: "..." }
```

输出: 公会清单 + 成员角色数组 + 授权 scope 列表,可用于判断是否具备后续管理操作权限。

### 案例2: SKU 订阅状态核验

应用开发者需要核验用户订阅状态,以决定是否解锁高级功能。

```javascript
// 1. 获取用户对该应用的权益清单
const entitlements = await clawlink_call_tool({
  tool: "discord_get_current_user_application_entitlements",
  parameters: { application_id: "9876543210" }
});
// 返回: { data: [{ id, sku_id, user_id, entitlement_type, ... }] }

// 2. 按 SKU 列出全部订阅(分页)
const subs = await clawlink_call_tool({
  tool: "discord_list_sku_subscriptions",
  parameters: { sku_id: "1234567890", limit: 50 }
});
// 返回: { data: [{ id, status, current_period_end, ... }] }

// 3. 消耗一次性可消耗权益(需显式确认)
await clawlink_call_tool({
  tool: "discord_consume_entitlement",
  parameters: { entitlement_id: "abc123", sku_id: "1234567890" }
});
```

输出: 权益清单 + 订阅状态,可结合 `entitlement_type`(purchase/premium_subscription/developer_gift)判断权益来源。

### 案例3: 角色连接元数据同步(如 Xbox Gamertag)

游戏平台需要把用户的 Xbox Gamertag 写入 Discord 角色连接,以便 Discord 端显示游戏身份徽章。

```javascript
// 1. 读取当前角色连接
const conn = await clawlink_call_tool({
  tool: "discord_get_user_application_role_connection",
  parameters: { application_id: "9876543210" }
});
// 返回: { platform_name, metadata: { ... } }

// 2. 更新角色连接元数据(需 role_connections.write scope)
await clawlink_call_tool({
  tool: "discord_update_user_application_role_connection",
  parameters: {
    application_id: "9876543210",
    metadata: {
      custom_fields: [
        { name: "Xbox Gamertag", value: "PlayerOne" },
        { name: "Level", value: "42" }
      ]
    }
  }
});
```

输出: 更新后的角色连接对象。若 scope 不足将返回 `role_connection_write_scope_missing`,需引导用户重新授权。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `401 Unauthorized` 调用变更类工具 | Bot Token 用于需 Bearer 的端点 | 改用 OAuth2 Bearer Token,确保 scope 包含目标操作 |
| `Missing MANAGE_GUILD permission` | 用户在目标公会缺少管理权限 | 引导用户向公会管理员申请 `MANAGE_GUILD` + `MANAGE_ROLES` |
| `Guild widget disabled` | 公会未启用小组件 | 服务器管理员在 Server Settings > Widget 中启用 |
| `Role connection write scope missing` | OAuth2 未授权 `role_connections.write` | 重新发起授权流程,带上 `role_connections.write` scope |
| `Username change limit reached` | 1 小时内已修改 2 次用户名 | 等待限速重置(约 1 小时)后 |
| `Entitlement already consumed` | 同一可消耗权益被重复消耗 | 检查调用幂等性,记录已消耗 entitlement_id 避免重复 |
| `SKU subscription not found` | SKU ID 错误或订阅已被取消 | 核对 SKU ID 与应用归属,优先用 list 接口定位 |
| `Invite code invalid or expired` | 邀请码已失效或被删除 | 用 `discord_invite_resolve` 先验证,失败则提示用户重新生成 |

## 常见问题

### Q1: Bot Token 与 OAuth2 Bearer Token 何时切换?
A: 用户身份、商业权益、角色连接类工具必须用 Bearer Token;Bot Token 仅适用于少数应用命令权限端点。变更类工具几乎全部要求 Bearer。若不确定,先用 `discord_get_my_oauth2_authorization` 检查当前 token 类型与 scope。

### Q2: 如何批量获取公会内所有应用命令的权限?
A: 优先使用 `discord_get_batch_application_command_permissions` 一次性拉取,避免循环调用单条接口触发速率限制。返回结果包含每条命令的 `id` 与 `permissions` 数组,可直接 diff 后再调用 edit 接口。

### Q3: 删除测试权益会自动续期吗?
A: 不会。`discord_delete_test_entitlement` 仅删除测试权益,不会影响真实付费订阅。建议在测试完成后立即清理,避免污染生产环境权益列表。

### Q4: 公会小组件 PNG 与 JSON 返回内容有何差异?
A: JSON 返回公会基本信息、在线成员与频道列表(部分);PNG 返回图片字节流,适合嵌入文档或落地页。两者均要求公会启用 widget,否则返回 `guild_widget_disabled`。

### Q5: 角色连接的 custom_fields 有数量上限吗?
A: 单个应用的角色连接元数据字段数量受 Discord 应用配置限制(通常 ≤ 5 个字段)。超出会返回 `metadata_field_limit_exceeded`,需精简字段或合并语义相近的字段。

### Q6: 如何安全退出一个公会?
A: 使用 `discord_leave_guild` 属于 high_impact 操作,需二次确认。退出后用户将立即失去该公会访问权限,且不可自动恢复,需重新申请邀请。建议在执行前导出公会成员信息作为备份。

## 已知限制

- 无法发送消息或管理频道内容,本 skill 聚焦身份与权限管理
- `discord_list_my_guilds` 仅返回部分字段,完整公会信息需另行调用(超出当前 scope)
- 用户名修改受 Discord 限速:每小时最多 2 次
- 公会小组件必须在 Discord 服务器设置中显式启用,否则相关接口报错
- 商业权益接口仅适用于已上架 SKU 的应用,沙箱应用需在 Dev Portal 配置测试 SKU
- 角色连接元数据字段值长度与类型受 Discord 元数据配置约束
- 不支持直接通过本 skill 创建或删除 Discord 应用、SKU 或贴纸包

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。