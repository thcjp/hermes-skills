---
slug: auth-security-architect
name: auth-security-architect
version: "1.0.0"
displayName: "认证安全架构师"
summary: "OAuth/2FA/SSO全栈认证安全,基于Better Auth构建企业级认证体系"
license: MIT
description: |-
  认证安全架构师——基于Better Auth官方最佳实践设计安全、可扩展的认证授权系统。从OAuth集成到2FA,从会话管理到RBAC权限控制,全栈安全覆盖,让认证这件事既安全又不折腾用户。

  核心能力:
  - OAuth/OIDC集成:Google/GitHub/微信等第三方登录
  - 双因素认证(2FA):TOTP/短信/邮箱验证码增强安全
  - 单点登录(SSO):SAML/OIDC企业统一登录
  - 会话管理:JWT/刷新令牌/设备管理/会话撤销
  - RBAC权限模型:角色/权限/资源精细化控制
  - 密码策略:强度校验/哈希存储/重置流程
  - CSRF/XSS防护:安全Headers+同源策略

  适用场景:
  - SaaS创业者用户认证:注册/登录/登出+OAuth+会话管理
  - 独立开发者企业SSO:企业内部统一登录+SAML/OIDC
  - 一人公司API安全:JWT/API Key/速率限制保护端点
  - 副业项目移动认证:刷新令牌/设备管理移动端登录

  差异化:不是认证教程合集,而是基于Better Auth最佳实践的全栈认证架构师,从OAuth到2FA到RBAC全链路安全设计,让没有安全经验的开发者也能构建企业级认证体系。

  触发关键词:认证、授权、OAuth、2FA、SSO、会话、权限、RBAC、密码、密钥、CSRF、XSS、安全架构、Better Auth
tags: [认证安全, OAuth, 权限管理, SSO, 安全架构]
tools: [read, exec]
---

# 认证安全架构师

基于 Better Auth 官方最佳实践,设计安全、可扩展的认证授权系统。从 OAuth 集成到 2FA,从会话管理到权限控制,全栈安全覆盖。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| SaaS 认证 | 用户注册/登录/登出 | 邮箱密码 + OAuth + 会话 |
| 企业 SSO | 企业内部统一登录 | SAML/OIDC + 组织管理 |
| 双因素认证 | 增强安全性 | TOTP/短信/邮箱验证码 |
| 权限管理 | 角色与权限控制 | RBAC/ABAC 权限模型 |
| API 安全 | 保护 API 端点 | JWT/API Key/速率限制 |
| 移动端认证 | 移动应用登录 | 刷新令牌/设备管理 |

## 工作流

### 1. 认证架构设计

1. **确定认证方式**
   - 邮箱+密码(基础)
   - OAuth(Google/GitHub/Microsoft/Apple)
   - Magic Link(无密码)
   - Passkey(WebAuthn)
   - 企业 SSO(SAML/OIDC)
2. **会话策略**
   - JWT 无状态(适合微服务)
   - 数据库会话(可撤销,更安全)
   - 混合模式(刷新令牌)
3. **权限模型**
   - RBAC:角色-权限映射
   - ABAC:属性-权限映射
   - 多组织(多团队隔离):组织/团队/成员

### 2. 核心认证流程

1. **注册流程**
   - 邮箱验证(验证码/链接)
   - 密码强度校验(zxcvbn)
   - 密码哈希(bcrypt/argon2)
   - 防止枚举攻击(统一响应)
2. **登录流程**
   - 凭证验证
   - 2FA 挑战(如已启用)
   - 会话创建
   - 登录通知(邮件/IP)
3. **OAuth 流程**
   - 重定向到 Provider
   - 回调处理
   - 账号关联/创建
   - 令牌交换
4. **密码重置**
   - 安全令牌(时效性)
   - 邮件确认
   - 旧会话失效

### 3. 双因素认证(2FA)

1. **TOTP(基于时间)**
   - 生成密钥 + QR 码
   - Google Authenticator/Authy
   - 备份码生成
2. **短信验证码**
   - 发送 6 位验证码
   - 限流与重试
   - 成本考量
3. **邮箱验证码**
   - 发送验证码
   - 时效性(5-15分钟)
4. **WebAuthn/Passkey**
   - 设备生物识别
   - 公钥注册/验证

### 4. 会话与令牌管理

1. **会话生命周期**
   - 创建:登录成功后
   - 续期:活跃用户自动续期
   - 撤销:登出/管理员强制下线
   - 过期:闲置超时/绝对超时
2. **令牌安全**
   - Access Token:短有效期(15-60分钟)
   - Refresh Token:长有效期(7-30天)
   - 令牌轮换:刷新时发放新令牌
   - 令牌存储:httpOnly Cookie(防 XSS)
3. **设备管理**
   - 记录登录设备
   - 异常登录检测
   - 远程登出

### 5. 安全防护

1. **OWASP Top 10 防护**
   - 注入防护:参数化查询/输入验证
   - XSS 防护:CSP/输出编码
   - CSRF 防护:SameSite Cookie/CSRF Token
   - 认证失效:会话管理/超时
   - 访问控制:服务端权限校验
2. **速率限制**
   - 登录尝试限制(5次/15分钟)
   - API 请求限制
   - 渐进式退避
3. **密钥安全**
   - 环境变量管理(不入代码库)
   - 密钥轮换策略
   - Vault/Secret Manager 集成

## 依赖说明

| 依赖类型 | 要求 | 说明 |
|:---------|:-----|:-----|
| LLM | 任意支持 Agent Skills 的 LLM | Claude/GPT/Gemini 等 |
| 运行环境 | Node.js 18+ | Better Auth 运行环境 |
| 框架 | better-auth (npm) | 认证框架 |
| 数据库 | 关系型数据库(MySQL/SQLite等) | 会话与用户存储 |
| API Key | OAuth Provider Keys (可选) | Google/GitHub 等 Provider 的 Client ID/Secret |
| 可选 | Twilio API Key | 短信 2FA |
| 可选 | SMTP 配置 | 邮箱验证/密码重置 |

## 异常处理

| 异常场景 | 处理方式 |
|:---------|:---------|
| 登录暴力破解 | 速率限制 + 账号锁定 + IP 封禁 |
| 令牌泄露 | 立即撤销所有会话,强制重新登录 |
| OAuth Provider 故障 | 回退到邮箱密码登录 |
| 2FA 设备丢失 | 备份码验证 → 管理员重置 |
| 会话固定攻击 | 登录后重新生成会话 ID |
| CSRF 攻击 | SameSite Cookie + CSRF Token 双重防护 |

## 示例

### 输入:配置邮箱+OAuth+2FA认证

```
用户请求:为一个SaaS应用配置认证,支持邮箱密码、Google OAuth、TOTP 2FA

输出:
- auth.ts (Better Auth 配置:emailPassword + google + totp)
- auth-schema.sql (数据库表:users/sessions/accounts/verifications)
- app/api/auth/[...all]/route.ts (认证 API 路由)
- components/LoginForm.tsx (登录表单)
- components/TwoFactorSetup.tsx (2FA 设置:QR码)
```

### 输入:组织与权限管理

```
用户请求:添加多组织(多团队隔离)组织功能,支持角色管理(Owner/Admin/Member)

输出:
- auth.ts 添加 organization 插件
- roles 配置:owner(全部权限) / admin(管理成员) / member(基本访问)
- 权限中间件:检查用户在组织中的角色
- 组织创建/邀请/移除成员 API
```
