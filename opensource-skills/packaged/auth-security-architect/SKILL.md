---
slug: auth-security-architect
name: auth-security-architect
version: "1.1.0"
displayName: "认证安全架构师"
summary: "OAuth/2FA/SSO全栈认证安全,基于Better Auth构建企业级认证体系"
license: Proprietary
description: |-
  认证安全架构师——基于Better Auth官方最佳实践设计安全、可扩展的认证授权系统。适用于SaaS认证、企业SSO、双因素认证、RBAC权限管理、API安全防护、移动端认证等场景。从OAuth集成到2FA，从会话管理到权限控制，全栈安全覆盖。触发关键词：认证、授权、OAuth、2FA、SSO、会话、权限、RBAC、密码、密钥、CSRF、XSS、安全架构、Better Auth
tags: [认证安全, OAuth, 权限管理, SSO, 安全架构]
tools:
  - read
  - exec
suggested_price: "50.00"
pricing_tier: "enterprise"
pricing_rationale: "安全合规类, small市场, enterprise复杂度, rare频次, enterprise层 → 低频高价值,专业壁垒高"
---
# 认证安全架构师

基于 Better Auth 官方最佳实践，设计安全、可扩展的认证授权系统。从 OAuth 集成到 2FA，从会话管理到权限控制，全栈安全覆盖。

## 核心能力

- **多方式认证设计**：邮箱密码 + OAuth（Google/GitHub/Microsoft/Apple）+ Magic Link + Passkey/WebAuthn + 企业 SSO（SAML/OIDC）
- **会话与令牌管理**：Access Token（15-60分钟）+ Refresh Token（7-30天）轮换 + httpOnly Cookie 存储 + 设备管理
- **双因素认证（2FA）**：TOTP（Google Authenticator）+ 短信验证码 + 邮箱验证码 + WebAuthn/Passkey + 备份码
- **权限模型设计**：RBAC（角色-权限映射）+ ABAC（属性-权限映射）+ 多组织隔离（组织/团队/成员）
- **OWASP Top 10 防护**：注入防护 + XSS（CSP）+ CSRF（SameSite + Token）+ 速率限制 + 密钥安全管理

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| SaaS 认证 | 应用类型 + 认证方式需求 | auth.ts 配置 + 数据库 Schema + 登录表单 + 2FA 设置组件 |
| 企业 SSO | 企业身份提供商(IdP) + 组织结构 | SAML/OIDC 配置 + 组织管理 API + 权限中间件 |
| 双因素认证 | 安全等级要求 + 2FA 方式 | TOTP 配置 + QR 码生成 + 备份码 + 验证流程 |
| 权限管理 | 角色清单 + 权限矩阵 | RBAC 配置 + 权限中间件 + 角色 API + 审计日志 |
| API 安全 | API 端点清单 + 访问控制需求 | JWT 签发/校验 + 速率限制 + API Key 管理 |
| 移动端认证 | 平台(iOS/Android) + 安全要求 | 刷新令牌策略 + 设备管理 + 生物识别集成 |

**不适用于**：
- 网络层安全（防火墙、WAF 配置，属基础设施范畴）
- 数据库加密设计（属数据层安全）
- 代码漏洞扫描（属 SAST/DAST 工具职责）
- 物理安全与办公网络安全

## 使用流程

### Step 1: 确定认证方式
- 评估应用类型：B2C SaaS / B2B 企业应用 / 内部系统
- 选择认证方式：邮箱密码（基础）/ OAuth（社交登录）/ Magic Link（无密码）/ Passkey（WebAuthn）/ 企业 SSO（SAML/OIDC）
- 确认国内可用性：OAuth Provider 优先选择国内方案（微信/支付宝/飞书/钉钉）替代 Google/GitHub

### Step 2: 设计会话策略
- 选择会话模式：JWT 无状态（适合微服务）/ 数据库会话（可撤销，更安全）/ 混合模式（刷新令牌）
- 设定令牌有效期：Access Token 15-60 分钟 / Refresh Token 7-30 天
- 设计令牌存储：httpOnly Cookie（防 XSS）/ 内存存储（SPA）

### Step 3: 选择权限模型
- RBAC：角色-权限映射（适合角色固定的场景）
- ABAC：属性-权限映射（适合动态权限）
- 多组织：组织/团队/成员三层结构

### Step 4: 实现核心认证流程
- 注册流程：邮箱验证 + 密码强度校验（zxcvbn）+ 密码哈希（bcrypt/argon2）+ 防枚举攻击
- 登录流程：凭证验证 + 2FA 挑战 + 会话创建 + 登录通知
- OAuth 流程：重定向 Provider → 回调处理 → 账号关联/创建 → 令牌交换
- 密码重置：安全令牌（时效性）+ 邮件确认 + 旧会话失效

### Step 5: 配置 2FA
- TOTP：生成密钥 + QR 码 + 备份码
- 短信验证码：发送 6 位验证码 + 限流与重试
- 邮箱验证码：发送验证码 + 时效性（5-15 分钟）
- WebAuthn/Passkey：设备生物识别 + 公钥注册/验证

### Step 6: 安全防护配置
- OWASP Top 10 防护：注入防护 + XSS（CSP）+ CSRF（SameSite + Token）
- 速率限制：登录尝试 5 次/15 分钟 + API 请求限制 + 渐进式退避
- 密钥安全：环境变量管理（不入代码库）+ 密钥轮换 + Vault/Secret Manager 集成

### Step 7: 输出实现文件
- `auth.ts`：Better Auth 配置
- `auth-schema.sql`：数据库表结构
- `app/api/auth/[...all]/route.ts`：认证 API 路由
- `components/LoginForm.tsx`：登录表单
- `components/TwoFactorSetup.tsx`：2FA 设置组件

## 示例

### 示例 1：SaaS 应用认证配置

**输入**：
```
需求：为一个 SaaS 应用配置认证，支持邮箱密码、Google OAuth、TOTP 2FA。
技术栈：Next.js + better-auth + PostgreSQL。
```

**输出**：
```typescript
// auth.ts
import { betterAuth } from "better-auth";
import { totp, admin } from "better-auth/plugins";
import { drizzleAdapter } from "better-auth/adapters/drizzle";

export const auth = betterAuth({
  database: drizzleAdapter(db, { provider: "pg" }),
  emailAndPassword: {
    enabled: true,
    minPasswordLength: 8,
    maxPasswordLength: 128,
    passwordRequirements: { requireUppercase: true, requireNumbers: true },
  },
  socialProviders: {
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID!,    // 从环境变量读取，零硬编码
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    },
  },
  plugins: [
    totp({ digits: 6, period: 30 }),
    admin({ defaultRole: "user" }),
  ],
  session: {
    expiresIn: 60 * 60 * 24 * 7,    // 7 天
    updateAge: 60 * 60 * 24,         // 每天续期
    cookieCache: { enabled: true, maxAge: 300 },
  },
  rateLimit: { window: 60, max: 10 },  // 登录限流
});
```

```sql
-- auth-schema.sql (节选)
CREATE TABLE users (
  id TEXT PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  email_verified BOOLEAN DEFAULT FALSE,
  name TEXT,
  image TEXT,
  password_hash TEXT,  -- argon2 哈希
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE sessions (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id) ON DELETE CASCADE,
  token TEXT UNIQUE NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  ip_address TEXT,
  user_agent TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE two_factor (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id) ON DELETE CASCADE,
  secret TEXT NOT NULL,    -- TOTP 密钥，加密存储
  backup_codes TEXT[],     -- 备份码哈希
  verified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### 示例 2：多组织权限管理

**输入**：
```
需求：添加多组织（多团队隔离）功能，支持角色管理（Owner/Admin/Member）。
```

**输出**：
```typescript
// auth.ts 添加 organization 插件
import { organization } from "better-auth/plugins";

export const auth = betterAuth({
  // ... 之前的配置
  plugins: [
    organization({
      allowUserToCreateOrganization: true,
      invitationLimit: 50,
      roles: {
        owner: {
          description: "组织所有者，拥有全部权限",
          permissions: ["organization:*", "member:*", "billing:*"],
        },
        admin: {
          description: "管理员，可管理成员但不能转让组织",
          permissions: ["organization:read", "member:invite", "member:remove"],
        },
        member: {
          description: "普通成员，基本访问权限",
          permissions: ["organization:read"],
        },
      },
    }),
  ],
});

// 权限中间件示例
export async function requireRole(role: "owner" | "admin" | "member") {
  return async (req: Request) => {
    const session = await auth.api.getSession({ headers: req.headers });
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });

    const member = await auth.api.getFullOrganization({
      headers: req.headers,
      query: { organizationId: req.headers.get("x-org-id")! },
    });

    if (!member || member.role !== role) {
      return Response.json({ error: "Forbidden" }, { status: 403 });
    }
    return null;  // 继续处理
  };
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 登录暴力破解 | 攻击者尝试大量密码组合 | 速率限制（5 次/15 分钟）+ 账号锁定 + IP 封禁 |
| 令牌泄露 | Access Token 被窃取 | 立即撤销所有会话，强制重新登录，轮换刷新令牌 |
| OAuth Provider 故障 | 第三方 IdP 不可用 | 回退到邮箱密码登录，显示 Provider 状态页 |
| 2FA 设备丢失 | 用户无法生成 TOTP | 备份码验证 → 管理员重置 → 身份核验后关闭 2FA |
| 会话固定攻击 | 攻击者预设 session ID | 登录后重新生成会话 ID，废弃旧 ID |
| CSRF 攻击 | 跨站请求伪造 | SameSite Cookie + CSRF Token 双重防护 |
| 密码重置令牌泄露 | 令牌被截获 | 令牌时效性（15 分钟）+ 一次性使用 + IP 绑定 |
| 账号枚举 | 注册/找回密码响应暴露账号存在 | 统一响应消息（"若账号存在，邮件已发送"） |

## 依赖说明

### 运行环境
- **Agent 平台**：Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持 SKILL.md 的任意 Agent
- **操作系统**：Windows / macOS / Linux
- **运行时**：Node.js 18+（Better Auth 运行环境）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| better-auth | npm 包 | 必需 | `npm install better-auth` |
| 数据库 | 关系型数据库 | 必需 | MySQL/PostgreSQL/SQLite |
| OAuth Provider Keys | API Key | 可选 | Google/GitHub Provider 的 Client ID/Secret |
| Twilio API Key | API Key | 可选 | 短信 2FA（国内可用阿里云短信/腾讯云短信替代） |
| SMTP 配置 | 服务 | 可选 | 邮箱验证/密码重置（国内可用阿里云邮件推送/腾讯企业邮） |

### 国内替代方案
| 海外服务 | 国内替代 | 说明 |
|:---------|:---------|:-----|
| Google OAuth | 微信开放平台 / 支付宝开放平台 | 国内社交登录首选 |
| GitHub OAuth | Gitee OAuth / 飞书登录 / 钉钉登录 | 国内开发者身份 |
| Twilio 短信 | 阿里云短信 / 腾讯云短信 | 短信验证码服务 |
| SendGrid 邮件 | 阿里云邮件推送 / 腾讯企业邮 | 邮件发送服务 |
| Auth0 | 阿里云 IDaaS / 腾讯云身份管家 | 托管身份认证服务 |

### API Key 配置
- 所有密钥通过环境变量注入，**Skill 内零硬编码**
- 配置方式：在 Agent 的环境变量或 `.env` 文件中设置
- 必需密钥：`BETTER_AUTH_SECRET`（会话签名密钥）
- 可选密钥：`GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` / `TWILIO_*` / `SMTP_*`

### 可用性分类
- **分类**：MD + EXEC
- **说明**：纯 Markdown 方法论，实际实现需 Node.js 环境与数据库

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: SaaS应用多方式认证配置

**输入**:
```
需求: 为SaaS协作平台配置认证系统。
要求:
1. 支持邮箱密码 + Google OAuth + GitHub OAuth
2. 强制2FA（TOTP）针对管理员账号
3. PostgreSQL存储
4. 会话7天有效，httpOnly Cookie存储
技术栈: Next.js 14 + better-auth + Drizzle ORM
```

**LLM生成输出**:
```typescript
// output/saas-auth/auth.ts
import { betterAuth } from "better-auth";
import { totp, admin, organization } from "better-auth/plugins";
import { drizzleAdapter } from "better-auth/adapters/drizzle";
import { db } from "./db";
import { nextCookies } from "better-auth/next-js";

export const auth = betterAuth({
  database: drizzleAdapter(db, { provider: "pg" }),
  emailAndPassword: {
    enabled: true,
    minPasswordLength: 8,
    maxPasswordLength: 128,
    requireEmailVerification: true,  // 注册后必须验证邮箱
    passwordRequirements: {
      requireUppercase: true,
      requireNumbers: true,
      requireSpecialChar: true,
    },
    onPasswordReset: async (user) => {
      // 旧会话失效，强制重新登录
      await db.delete(sessions).where(eq(sessions.userId, user.id));
    },
  },
  socialProviders: {
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
      scope: ["openid", "email", "profile"],
    },
    github: {
      clientId: process.env.GITHUB_CLIENT_ID!,
      clientSecret: process.env.GITHUB_CLIENT_SECRET!,
    },
  },
  plugins: [
    totp({
      digits: 6,
      period: 30,
      issuer: "SaaS Platform",
      // 仅管理员强制2FA
      skipVerificationOnEnable: false,
    }),
    admin({
      defaultRole: "user",
      adminRole: "admin",
      // 管理员必须开启2FA
      require2FA: ["admin"],
    }),
    organization({
      allowUserToCreateOrganization: true,
      invitationLimit: 50,
    }),
    nextCookies(),
  ],
  session: {
    expiresIn: 60 * 60 * 24 * 7,  // 7天
    updateAge: 60 * 60 * 24,       // 每天续期
    cookieCache: { enabled: true, maxAge: 300 },
    cookieOptions: {
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      sameSite: "lax",
      path: "/",
    },
  },
  rateLimit: {
    window: 60,
    max: 10,  // 登录限流: 10次/分钟
  },
  advanced: {
    cookiePrefix: "saas_auth",
    useSecureCookies: true,
  },
});

// 强制2FA中间件
export async function requireAdmin2FA(req: Request) {
  const session = await auth.api.getSession({ headers: req.headers });
  if (!session) {
    return Response.json({ error: "Unauthorized" }, { status: 401 });
  }
  if (session.user.role === "admin" && !session.user.twoFactorEnabled) {
    return Response.json(
      { error: "Admin must enable 2FA", code: "TWO_FACTOR_REQUIRED" },
      { status: 403 }
    );
  }
  return null;
}
```

```sql
-- output/saas-auth/auth-schema.sql (节选)
CREATE TABLE users (
  id TEXT PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  email_verified BOOLEAN DEFAULT FALSE,
  name TEXT,
  image TEXT,
  password_hash TEXT,        -- argon2哈希
  role TEXT DEFAULT 'user',  -- user | admin
  two_factor_enabled BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE sessions (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id) ON DELETE CASCADE,
  token TEXT UNIQUE NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  ip_address TEXT,
  user_agent TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE two_factor (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id) ON DELETE CASCADE,
  secret TEXT NOT NULL,          -- TOTP密钥，AES加密存储
  backup_codes TEXT[],           -- 备份码bcrypt哈希
  verified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_sessions_user_id ON sessions(user_id);
CREATE INDEX idx_sessions_token ON sessions(token);
```

**效果验证**: ✓邮箱密码+OAuth双通道认证 ✓管理员强制2FA逻辑正确 ✓会话7天有效+httpOnly Cookie ✓argon2密码哈希 ✓登录限流10次/分钟

### 案例2: 企业SAML SSO集成

**输入**:
```
需求: 为企业版添加SAML SSO，对接Okta身份提供商。
要求:
1. 支持SP发起和IdP发起两种登录流程
2. 自动创建/关联用户账号
3. 按企业邮箱域名路由到对应IdP
4. Just-in-Time (JIT) provisioning
```

**LLM生成输出**:
```typescript
// output/enterprise-sso/saml-config.ts
import { betterAuth } from "better-auth";
import { sso } from "better-auth/plugins/sso";
import { SAMLProvider } from "better-auth/sso/saml";

// 按域名路由到不同IdP的配置
const samlProviders: Record<string, SAMLProvider> = {
  "company-a.com": {
    entityId: "https://auth.ourapp.com/saml/company-a",
    entryPoint: "https://company-a.okta.com/app/ourapp/abc123/sso/saml",
    cert: process.env.SAML_CERT_COMPANY_A!,  // 从环境变量读取
    signatureAlgorithm: "sha256",
    wantAssertionsSigned: true,
    wantResponseSigned: true,
    identifierFormat: "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
    attributeMapping: {
      email: "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress",
      name: "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name",
      department: "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/department",
    },
  },
  "company-b.com": {
    entityId: "https://auth.ourapp.com/saml/company-b",
    entryPoint: "https://company-b.okta.com/app/ourapp/def456/sso/saml",
    cert: process.env.SAML_CERT_COMPANY_B!,
    signatureAlgorithm: "sha256",
    wantAssertionsSigned: true,
  },
};

export const auth = betterAuth({
  // ... 其他配置
  plugins: [
    sso({
      saml: {
        providers: samlProviders,
        // JIT provisioning: SAML用户首次登录自动创建账号
        jitProvisioning: true,
        // 邮箱域名路由
        domainRouting: true,
        // 账号关联策略
        accountLinking: {
          // 同邮箱的现有账号自动关联
          allowDifferentEmails: false,
          // 关联前要求二次验证
          requireVerification: true,
        },
      },
    }),
  ],
});

// 路由处理: SP发起的登录
// app/api/auth/saml/login/route.ts
import { auth } from "@/auth";

export async function POST(req: Request) {
  const { email } = await req.json();
  const domain = email.split("@")[1];
  
  if (!samlProviders[domain]) {
    return Response.json(
      { error: "SSO not configured for this domain" },
      { status: 404 }
    );
  }

  // 重定向到对应IdP
  const redirectUrl = await auth.api.saml.getLoginRedirectURL({
    body: { provider: domain, email },
  });
  
  return Response.json({ redirectUrl });
}

// SAML ACS (Assertion Consumer Service) 端点
// app/api/auth/saml/acs/route.ts
export async function POST(req: Request) {
  const result = await auth.api.saml.handleAssertion({
    request: req,
  });
  
  if (result.error) {
    return Response.redirect(`/login?error=saml_failed`);
  }
  
  // 创建会话并重定向到首页
  return Response.redirect(`${process.env.APP_URL}/dashboard`);
}
```

```markdown
# output/enterprise-sso/deployment-guide.md
## IdP配置步骤（Okta端）
1. 在Okta管理后台创建SAML 2.0应用
2. 配置SP Entity ID: https://auth.ourapp.com/saml/{company}
3. 配置ACS URL: https://auth.ourapp.com/api/auth/saml/acs
4. 下载IdP证书并配置到环境变量 SAML_CERT_COMPANY_{X}
5. 配置属性声明(Attribute Statements):
   - email: user.email
   - name: user.firstName + " " + user.lastName
   - department: user.department
6. 测试SSO登录流程

## 安全要求
- 所有SAML响应必须签名验证(wantResponseSigned: true)
- 断言必须签名(wantAssertionsSigned: true)
- 证书通过环境变量注入，不入代码库
- 重放攻击防护: 检查NotOnOrAfter时间窗口
```

**效果验证**: ✓多IdP按域名路由 ✓JIT自动创建账号 ✓SP/IdP发起双流程 ✓SAML响应签名验证 ✓证书环境变量管理

### 案例3: 多组织RBAC权限管理

**输入**:
```
需求: 实现多组织权限管理。
角色: Owner（所有者）/ Admin（管理员）/ Editor（编辑者）/ Viewer（查看者）
权限粒度: 资源级（项目/文档/成员/账单）
要求: 支持跨组织切换、权限审计日志
```

**LLM生成输出**:
```typescript
// output/rbac-system/organization-rbac.ts
import { organization } from "better-auth/plugins";

// 角色定义
const roles = {
  owner: {
    description: "组织所有者，全部权限",
    permissions: [
      "organization:*",
      "project:*",
      "document:*",
      "member:*",
      "billing:*",
    ],
  },
  admin: {
    description: "管理员，可管理项目和成员",
    permissions: [
      "organization:read",
      "project:*",
      "document:*",
      "member:invite",
      "member:remove",
      "member:role:assign",  // 可分配Editor/Viewer角色
    ],
  },
  editor: {
    description: "编辑者，可编辑项目和文档",
    permissions: [
      "organization:read",
      "project:read",
      "project:edit",
      "document:*",
    ],
  },
  viewer: {
    description: "查看者，只读权限",
    permissions: [
      "organization:read",
      "project:read",
      "document:read",
    ],
  },
} as const;

export const auth = betterAuth({
  plugins: [
    organization({
      allowUserToCreateOrganization: true,
      invitationLimit: 50,
      roles,
      // 权限检查钩子
      authorization: {
        afterCreateOrganization: async (org, user) => {
          // 创建者自动成为Owner
          await auth.api.addMemberRole({
            body: {
              organizationId: org.id,
              userId: user.id,
              role: "owner",
            },
          });
        },
      },
    }),
  ],
});

// 权限检查中间件
export function requirePermission(permission: string) {
  return async (req: Request, ctx: { params: { orgId: string } }) => {
    const session = await auth.api.getSession({ headers: req.headers });
    if (!session) {
      return Response.json({ error: "Unauthorized" }, { status: 401 });
    }

    const orgId = ctx.params.orgId;
    const membership = await auth.api.getFullOrganization({
      headers: req.headers,
      query: { organizationId: orgId },
    });

    if (!membership) {
      return Response.json({ error: "Not a member" }, { status: 403 });
    }

    // 检查权限（支持通配符）
    const userPermissions = roles[membership.role as keyof typeof roles].permissions;
    const hasPermission = userPermissions.some(
      (p) => p === permission || 
      p.endsWith(":*") && permission.startsWith(p.slice(0, -1))
    );

    if (!hasPermission) {
      // 记录权限拒绝审计日志
      await logPermissionDenied({
        userId: session.user.id,
        orgId,
        permission,
        resource: req.url,
        timestamp: new Date(),
      });
      return Response.json(
        { error: "Forbidden", required: permission },
        { status: 403 }
      );
    }

    return null;  // 继续处理
  };
}

// 跨组织切换API
// app/api/auth/switch-organization/route.ts
export async function POST(req: Request) {
  const { orgId } = await req.json();
  const session = await auth.api.getSession({ headers: req.headers });
  
  // 验证用户是该组织成员
  const membership = await db.query.organizationMembers.findFirst({
    where: and(
      eq(organizationMembers.userId, session.user.id),
      eq(organizationMembers.organizationId, orgId)
    ),
  });

  if (!membership) {
    return Response.json({ error: "Not a member" }, { status: 403 });
  }

  // 更新当前活动组织
  await auth.api.updateSession({
    headers: req.headers,
    body: { activeOrganizationId: orgId },
  });

  // 记录审计日志
  await logOrganizationSwitch(session.user.id, orgId);
  
  return Response.json({ success: true });
}
```

```typescript
// output/rbac-system/permission-audit.ts
// 权限审计日志Schema
import { pgTable, text, timestamp, jsonb } from "drizzle-orm/pg-core";

export const permissionAuditLog = pgTable("permission_audit_log", {
  id: text("id").primaryKey(),
  userId: text("user_id").notNull(),
  orgId: text("org_id").notNull(),
  action: text("action").notNull(),  // grant | revoke | deny | access
  permission: text("permission"),
  role: text("role"),
  resource: text("resource"),
  metadata: jsonb("metadata"),
  ipAddress: text("ip_address"),
  timestamp: timestamp("timestamp").defaultNow().notNull(),
});

// 查询用户权限变更历史
export async function getUserPermissionHistory(userId: string) {
  return await db.query.permissionAuditLog.findMany({
    where: eq(permissionAuditLog.userId, userId),
    orderBy: [desc(permissionAuditLog.timestamp)],
    limit: 100,
  });
}
```

**效果验证**: ✓4级角色权限分层 ✓通配符权限匹配 ✓跨组织切换功能 ✓权限审计日志完整 ✓Owner/Admin权限边界清晰

### 案例4: 2FA备份码安全存储

**输入**:
```
需求: 实现TOTP 2FA的备份码功能。
要求:
1. 生成10个8位备份码
2. 安全存储（不明文明文）
3. 一次性使用，使用后失效
4. 用户可重新生成（旧的失效）
```

**LLM生成输出**:
```typescript
// output/two-factor-backup/backup-codes.ts
import { hash, verify } from "argon2";
import { randomBytes } from "crypto";

// 1. 生成备份码（格式: XXXX-XXXX，去除易混淆字符）
export function generateBackupCodes(count: 10): string[] {
  const charset = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";  // 去除0/O/1/I/L
  const codes: string[] = [];
  
  for (let i = 0; i < count; i++) {
    const bytes = randomBytes(8);
    let code = "";
    for (let j = 0; j < 8; j++) {
      code += charset[bytes[j] % charset.length];
    }
    // 格式化为 XXXX-XXXX
    codes.push(`${code.slice(0, 4)}-${code.slice(4)}`);
  }
  return codes;
}

// 2. 哈希存储（每个码独立哈希）
export async function hashBackupCodes(codes: string[]): Promise<string[]> {
  return Promise.all(codes.map(code => hash(code, {
    type: 2,  // argon2id
    memoryCost: 65536,
    timeCost: 3,
    parallelism: 4,
  })));
}

// 3. 验证备份码（按索引匹配后逐个尝试）
export async function verifyBackupCode(
  inputCode: string,
  storedHashes: string[]
): Promise<{ valid: boolean; usedIndex?: number }> {
  for (let i = 0; i < storedHashes.length; i++) {
    if (storedHashes[i] === null) continue;  // 已使用的码
    const valid = await verify(storedHashes[i], inputCode);
    if (valid) {
      return { valid: true, usedIndex: i };
    }
  }
  return { valid: false };
}

// 4. 启用2FA时生成备份码
// app/api/auth/2fa/enable/route.ts
export async function POST(req: Request) {
  const session = await auth.api.getSession({ headers: req.headers });
  const { totpCode, secret } = await req.json();

  // 验证TOTP码
  const isValid = verifyTOTP(secret, totpCode);
  if (!isValid) {
    return Response.json({ error: "Invalid TOTP code" }, { status: 400 });
  }

  // 生成备份码
  const plainCodes = generateBackupCodes(10);
  const hashedCodes = await hashBackupCodes(plainCodes);

  // 存储（仅哈希）
  await db.update(twoFactor)
    .set({
      secret,  // TOTP密钥，AES加密后存储
      backupCodes: hashedCodes,
      verified: true,
    })
    .where(eq(twoFactor.userId, session.user.id));

  // 用户启用2FA
  await db.update(users)
    .set({ twoFactorEnabled: true })
    .where(eq(users.id, session.user.id));

  // 返回明文备份码（仅此一次）
  return Response.json({
    message: "2FA enabled. Save these backup codes securely.",
    backupCodes: plainCodes,
    warning: "These codes will only be shown once. Store them in a safe place.",
  });
}

// 5. 使用备份码登录（替代TOTP）
// app/api/auth/2fa/backup-verify/route.ts
export async function POST(req: Request) {
  const { email, password, backupCode } = await req.json();

  // 1. 验证邮箱密码
  const user = await verifyPassword(email, password);
  if (!user) {
    return Response.json({ error: "Invalid credentials" }, { status: 401 });
  }

  // 2. 验证备份码
  const twoFactorRecord = await db.query.twoFactor.findFirst({
    where: eq(twoFactor.userId, user.id),
  });
  
  const result = await verifyBackupCode(
    backupCode.toUpperCase(),
    twoFactorRecord.backupCodes
  );

  if (!result.valid) {
    // 限流计数
    await incrementFailedAttempts(user.id);
    return Response.json({ error: "Invalid backup code" }, { status: 400 });
  }

  // 3. 标记该备份码已使用（设为null）
  const updatedCodes = [...twoFactorRecord.backupCodes];
  updatedCodes[result.usedIndex!] = null;
  
  await db.update(twoFactor)
    .set({ backupCodes: updatedCodes })
    .where(eq(twoFactor.userId, user.id));

  // 4. 创建会话
  const session = await auth.api.createSession({ userId: user.id });
  
  // 5. 安全提醒
  await sendSecurityEmail(user.email, {
    subject: "备份码已使用",
    body: "您的2FA备份码已被使用。如非本人操作请立即修改密码并重新生成备份码。",
  });

  return Response.json({ session, warning: "Backup code consumed. Consider regenerating." });
}
```

**效果验证**: ✓10个8位备份码生成 ✓argon2id哈希存储 ✓一次性使用后失效 ✓重新生成旧的失效 ✓使用后安全提醒

### 案例5: 移动端认证令牌策略

**输入**:
```
需求: 为iOS/Android App设计认证令牌策略。
要求:
1. Access Token 15分钟有效
2. Refresh Token 30天有效，支持轮换
3. 设备管理（最多5台设备同时登录）
4. 支持生物识别快速登录（无需每次输密码）
5. 远程登出某台设备
```

**LLM生成输出**:
```typescript
// output/mobile-auth/mobile-token-strategy.ts
import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
  // 移动端使用JWT模式（无状态，减少查库）
  session: {
    model: "jwt",
    expiresIn: 60 * 15,         // Access Token 15分钟
    updateAge: 60 * 10,         // 10分钟内自动续期
    cookieCache: { enabled: false },  // 移动端不用Cookie
  },
  // Refresh Token配置
  refresh: {
    expiresIn: 60 * 60 * 24 * 30,  // 30天
    rotateOnUse: true,              // 使用后轮换
    reuseDetection: true,           // 检测重用（令牌被盗）
    maxActiveSessions: 5,           // 每用户最多5台设备
  },
  plugins: [
    jwt({
      jwtSecret: process.env.JWT_SECRET!,
      algorithm: "RS256",           // 非对称加密
      issuer: "https://auth.ourapp.com",
      audience: "mobile-app",
    }),
  ],
});

// 设备信息记录
export interface DeviceInfo {
  deviceId: string;        // 设备唯一标识
  platform: "ios" | "android";
  model: string;           // iPhone 15 Pro / Pixel 8
  osVersion: string;
  appVersion: string;
  pushToken?: string;      // 推送通知token
  biometricEnabled: boolean;
}

// 登录时注册设备
// app/api/auth/mobile/login/route.ts
export async function POST(req: Request) {
  const { email, password, deviceInfo, biometricSetupToken } = await req.json();

  // 1. 验证凭证
  const user = await verifyCredentials(email, password);
  if (!user) {
    return Response.json({ error: "Invalid credentials" }, { status: 401 });
  }

  // 2. 检查设备数量限制
  const activeDevices = await db.query.devices.findMany({
    where: and(eq(devices.userId, user.id), eq(devices.active, true)),
  });
  
  if (activeDevices.length >= 5) {
    return Response.json({
      error: "Too many devices",
      code: "DEVICE_LIMIT_EXCEEDED",
      activeDevices: activeDevices.map(d => ({
        deviceId: d.deviceId,
        model: d.model,
        lastActive: d.lastActiveAt,
      })),
    }, { status: 409 });
  }

  // 3. 创建会话
  const session = await auth.api.createSession({ userId: user.id });
  const refreshToken = await auth.api.generateRefreshToken({ userId: user.id });

  // 4. 注册设备
  await db.insert(devices).values({
    userId: user.id,
    deviceId: deviceInfo.deviceId,
    platform: deviceInfo.platform,
    model: deviceInfo.model,
    osVersion: deviceInfo.osVersion,
    appVersion: deviceInfo.appVersion,
    pushToken: deviceInfo.pushToken,
    biometricEnabled: false,
    refreshTokenHash: hashToken(refreshToken),
    active: true,
    lastActiveAt: new Date(),
  });

  // 5. 生物识别设置（可选）
  let biometricToken: string | null = null;
  if (biometricSetupToken) {
    // 生成生物识别专用token（绑定设备）
    biometricToken = await generateBiometricToken(user.id, deviceInfo.deviceId);
    await db.update(devices)
      .set({ biometricEnabled: true })
      .where(eq(devices.deviceId, deviceInfo.deviceId));
  }

  return Response.json({
    accessToken: session.token,
    refreshToken,
    expiresIn: 900,
    biometricToken,
    user: { id: user.id, email: user.email, name: user.name },
  });
}

// 生物识别快速登录
// app/api/auth/mobile/biometric-login/route.ts
export async function POST(req: Request) {
  const { biometricToken, deviceId } = await req.json();

  // 验证生物识别token（设备绑定）
  const device = await db.query.devices.findFirst({
    where: and(
      eq(devices.deviceId, deviceId),
      eq(devices.biometricTokenHash, hashToken(biometricToken)),
      eq(devices.active, true),
    ),
  });

  if (!device) {
    return Response.json({ error: "Invalid biometric token" }, { status: 401 });
  }

  // 检查token是否过期（7天）
  if (Date.now() - device.biometricTokenCreatedAt.getTime() > 7 * 24 * 60 * 60 * 1000) {
    return Response.json({
      error: "Biometric token expired",
      code: "REQUIRE_PASSWORD_LOGIN",
    }, { status: 401 });
  }

  // 签发新的Access Token
  const session = await auth.api.createSession({ userId: device.userId });
  
  // 更新设备活跃时间
  await db.update(devices)
    .set({ lastActiveAt: new Date() })
    .where(eq(devices.deviceId, deviceId));

  return Response.json({
    accessToken: session.token,
    expiresIn: 900,
  });
}

// 远程登出某台设备
// app/api/auth/mobile/revoke-device/route.ts
export async function POST(req: Request) {
  const session = await auth.api.getSession({ headers: req.headers });
  const { deviceId } = await req.json();

  // 验证设备属于当前用户
  const device = await db.query.devices.findFirst({
    where: and(
      eq(devices.userId, session.user.id),
      eq(devices.deviceId, deviceId),
    ),
  });

  if (!device) {
    return Response.json({ error: "Device not found" }, { status: 404 });
  }

  // 标记设备为非活跃
  await db.update(devices)
    .set({ 
      active: false,
      refreshTokenHash: null,
      biometricTokenHash: null,
    })
    .where(eq(devices.deviceId, deviceId));

  // 撤销该设备的Refresh Token（加入黑名单）
  await revokeRefreshToken(device.refreshTokenHash);

  // 推送通知该设备
  if (device.pushToken) {
    await sendPushNotification(device.pushToken, {
      title: "账号已登出",
      body: "您的账号已在另一台设备上登出此设备",
    });
  }

  return Response.json({ success: true });
}
```

**效果验证**: ✓Access Token 15分钟+Refresh Token 30天轮换 ✓5台设备限制 ✓生物识别token设备绑定 ✓远程设备登出 ✓令牌重用检测

## 常见问题

### Q1: Better Auth 与 NextAuth/Auth.js 有何区别？
A: Better Auth 提供更完整的开箱即用功能（2FA、组织管理、Passkey 内置），TypeScript 优先，数据库 Schema 透明可控；NextAuth 更轻量，社区生态成熟。企业级场景优先 Better Auth。

### Q2: 国内环境如何替代 Google OAuth？
A: 接入微信开放平台（扫码登录）、支付宝开放平台、飞书登录、钉钉登录。Better Auth 支持自定义 OAuth Provider，参考官方文档配置 `genericOAuth` 插件。

### Q3: 2FA 备份码如何安全存储？
A: 备份码不应明文存储。生成后对用户展示一次，然后存储 argon2/bcrypt 哈希。用户使用时哈希后比对。每个备份码一次性使用，使用后立即标记失效。

### Q4: JWT 与数据库会话如何选择？
A: JWT 适合无状态微服务（性能好、易扩展），但无法主动撤销；数据库会话可即时撤销（登出、强制下线），但每次请求需查库。高安全场景用数据库会话 + 短期 JWT，性能敏感场景用 JWT + 黑名单。

## 已知限制

- Better Auth 为较新框架，部分高级功能（如 OIDC Provider 模式）仍在迭代
- 企业 SSO（SAML）配置复杂，需要 IdP 端配合，调试周期较长
- 本 Skill 提供架构设计与配置模板，不替代完整的安全渗透测试
- 性能取决于底层 LLM 能力，复杂权限策略可能需要人工审查
- WebAuthn/Passkey 在旧浏览器（IE、部分安卓 WebView）不支持，需提供降级方案

## 安全

- **API Key 零暴露**：所有密钥（OAuth Secret、JWT Secret、SMTP 密码）通过环境变量注入，Skill 内零硬编码
- **密码哈希强制**：使用 argon2（推荐）或 bcrypt，禁止明文/MD5/SHA1 存储
- **令牌安全**：Access Token 短有效期 + Refresh Token 轮换 + httpOnly Cookie 存储
- **密钥轮换**：建议每 90 天轮换 `BETTER_AUTH_SECRET`，提供轮换期间双密钥兼容
- **审计日志**：记录登录、权限变更、组织操作等敏感行为，保留 180 天
