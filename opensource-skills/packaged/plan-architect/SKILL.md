---
slug: plan-architect
name: plan-architect
version: 1.0.1
displayName: 计划架构师
summary: "把设计文档变成可执行计划,任务拆到2-5分钟粒度,初级工程师也能照做。计划架构师把设计文档转化为可执行的详细实现计划,核心功能包括设计文档解析、任务拆分(2-5分钟粒度)、TDD驱动计划(红"
license: Proprietary
description: 计划架构师把设计文档转化为可执行的详细实现计划,核心功能包括设计文档解析、任务拆分(2-5分钟粒度)、TDD驱动计划(红-绿-重构)、YAGNI与DRY原则应用、计划文档与执行检查清单输出。适用于项目实施、功能开发、系统重构、技术迁移、Bug修复计划、技术债务清理场景。触发关键词:项目计划、任务拆分、TDD开发、实现计划、工程效率、计划架构、设计转计划。
tags:
  - 项目计划
  - 任务拆分
  - TDD开发
  - 独立开发
  - 工程效率
  - 工具
  - 效率
  - 自动化
  - 开发
  - 代码
  - 写作
  - 电商
  - 创意
tools:
  - read
  - exec
  - glob
  - grep
category: "Automation"
---
# 计划架构师

将设计文档转化为可执行的详细实现计划。每个任务都是 2-5 分钟可完成的粒度,包含精确的文件路径、完整的代码片段、明确的验证步骤。让一个"热情但缺乏判断力的初级工程师"也能按计划执行。

## 核心能力

1. **设计文档解析**:读取design.md或设计输入,提取目标/范围/技术栈/数据模型/架构图,识别依赖关系与执行顺序,确认技术栈版本/团队规模/时间约束/测试要求。
2. **任务拆分(2-5分钟粒度)**:每个任务2-5分钟可完成,有明确"完成"定义,可独立验证,有精确文件路径;按功能模块/层级(数据层→服务层→API层→UI层)/测试优先(TDD)拆分;无依赖任务可并行,有依赖按序执行,标注阻塞关系。
3. **TDD驱动计划**:红-绿-重构循环(先写失败测试→再写最小实现→最后重构),测试策略(单元80%/集成15%/E2E 5%),测试覆盖率目标80%+。
4. **YAGNI与DRY原则**:只实现当前需要的功能(不提前实现"可能需要"的功能),重复代码提取为函数/常量/组件(但不过度抽象,遵循Rule of Three)。
5. **计划输出**:保存为plan.md(任务列表带编号+依赖关系图+时间预估总计),执行检查清单(每个任务完成后勾选+验证命令一键运行+回滚步骤)。

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 项目实施 | 已批准的设计文档(design.md) | 可执行实现计划plan.md,输出到`output/{project}/plan.md` |
| 功能开发 | 新功能需求描述 | 任务拆分+TDD驱动+验证步骤的plan.md |
| 重构计划 | 系统重构需求 | 渐进式重构计划+安全步骤+回滚策略 |
| 迁移计划 | 技术迁移需求(如数据库迁移) | 数据迁移+服务切换+回滚方案的plan.md |
| Bug修复计划 | 复杂Bug描述+根因分析 | 根因修复+测试覆盖+防御措施的plan.md |
| 技术债务 | 债务清单+优先级 | 优先级排序+渐进清理+验证的plan.md |

**不适用于**:
- 需求探索阶段(应先用brainstorming明确需求)
- 架构设计阶段(应先完成设计文档再转计划)
- 执行实现阶段(本Skill只生成计划,执行由plan-executor完成)
- 运维/SRE操作计划(非软件开发场景)

## 使用流程

### Step 1: 计划输入分析
1. **设计文档解析**:读取design.md或设计输入,提取目标/范围/技术栈/数据模型/架构图,识别依赖关系与执行顺序
2. **约束确认**:技术栈版本、团队规模与技能、时间约束、测试要求

### Step 2: 任务拆分(2-5分钟粒度)
1. **拆分原则**:每个任务2-5分钟可完成,有明确"完成"定义,可独立验证,有精确文件路径
2. **拆分维度**:按功能模块拆分、按层级拆分(数据层→服务层→API层→UI层)、按测试优先拆分(TDD:先测试后实现)
3. **依赖排序**:无依赖任务可并行,有依赖任务按序执行,标注阻塞关系

### Step 3: 任务描述格式化
每个任务按以下格式描述:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 计划架构师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
### Task N: [任务名称]
- **文件**: `src/path/to/file.ts` (新建/修改)
- **描述**: [具体做什么]
- **代码**: [完整代码片段或关键改动]
- **验证**: [如何验证这个任务完成]
  - 命令: `npm test -- --grep "test name"`
  - 预期: 测试通过
- **依赖**: Task M (如果有)
- **时间预估**: ~3分钟
```

### Step 4: TDD驱动计划
1. **红-绿-重构循环**:先写失败测试(Red)→再写最小实现(Green)→最后重构(Refactor)
2. **测试策略**:单元测试(每个函数/方法)、集成测试(模块间交互)、端到端测试(关键用户流程),覆盖率目标80%+
3. **测试金字塔**:80%单元测试(快速/隔离)、15%集成测试(模块交互)、5%E2E测试(用户流程)

### Step 5: YAGNI与DRY原则检查
1. **YAGNI**:只实现当前需要的功能,不提前实现"可能需要"的功能,不过度设计接口,不添加未使用的配置项
2. **DRY**:重复代码提取为函数,重复配置提取为常量,重复模式提取为组件,但不过度抽象(Rule of Three)

### Step 6: 计划输出
1. **计划文档**:保存为plan.md,任务列表(带编号)+依赖关系图+时间预估总计
2. **执行检查清单**:每个任务完成后勾选+验证命令一键运行+回滚步骤(如需要)

## 示例

### 示例1: 用户认证功能计划

**输入**:
```
为Next.js应用添加邮箱密码认证,使用better-auth,数据库用Drizzle+SQLite。
设计文档已批准,需要生成可执行实现计划。
```

**输出** (`output/auth-feature/plan.md`):
```markdown
# 用户认证功能实现计划
# ...
## 概述
- 目标: 为Next.js应用添加邮箱密码认证
- 技术栈: Next.js 15 + better-auth + Drizzle + SQLite
- 总任务数: 8
- 预估总时间: ~35分钟
# ...
## Task 1: 安装better-auth依赖
- **文件**: package.json (修改)
- **描述**: 安装better-auth及其类型依赖
- **命令**: `cnpm install better-auth`
- **验证**: `cat package.json | grep better-auth` 输出包含better-auth
- **时间**: ~1分钟
# ...
## Task 2: 编写认证配置测试
- **文件**: tests/auth.test.ts (新建)
- **描述**: 测试auth配置能正确初始化
- **代码**:
```ts
import { describe, it, expect } from "vitest";
import { auth } from "../lib/auth";

describe("auth配置", () => {
  it("应正确初始化auth实例", () => {
    expect(auth).toBeDefined();
    expect(auth.api).toBeDefined();
  });
});
```
- **验证**: `npx vitest run tests/auth.test.ts`
- **预期**: 测试失败(配置尚未实现) - Red阶段
- **时间**: ~3分钟
# ...
## Task 3: 实现认证配置
- **文件**: lib/auth.ts (新建)
- **描述**: 配置better-auth邮箱密码认证
- **代码**:
```ts
import { betterAuth } from "better-auth";
import { drizzleAdapter } from "better-auth/adapters/drizzle";
import { db } from "./db";

export const auth = betterAuth({
  database: drizzleAdapter(db, { provider: "sqlite" }),
  emailAndPassword: { enabled: true },
});
```
- **验证**: `npx vitest run tests/auth.test.ts`
- **预期**: 测试通过 - Green阶段
- **依赖**: Task 1, Task 2
- **时间**: ~4分钟
# ...
## Task 4: 创建数据库Schema
- **文件**: lib/db/schema.ts (新建)
- **描述**: 创建users/sessions/accounts表
- **验证**: `npx drizzle-kit push && sqlite3 app.db ".tables"`
- **预期**: 输出包含users/sessions/accounts表
- **依赖**: Task 3
- **时间**: ~3分钟
# ...
...(共8个任务,总计~35分钟)
```

### 示例2: Bug修复计划

**输入**:
```
Bug: 用户购物车在刷新后丢失商品。
根因: 购物车数据仅存在内存中,未持久化到localStorage。
需要生成修复计划,包含测试覆盖和防御措施。
```

**输出** (`output/cart-bugfix/plan.md`):
```markdown
# 购物车刷新丢失Bug修复计划
# ...
## Bug分析
- 现象: 刷新页面后购物车商品丢失
- 根因: 购物车state仅存内存,未持久化
- 修复策略: 添加localStorage持久化
# ...
## Task 1: 编写购物车持久化测试
- **文件**: tests/cart.test.ts (修改)
- **描述**: 测试刷新后购物车数据保留
- **代码**: [测试localStorage持久化和恢复的测试用例]
- **验证**: `npx vitest run tests/cart.test.ts`
- **预期**: 测试失败(持久化未实现)
- **时间**: ~3分钟
# ...
## Task 2: 实现购物车持久化
- **文件**: hooks/useCart.ts (修改)
- **描述**: 添加localStorage读写逻辑
- **代码**: [useEffect持久化+初始化时恢复的代码]
- **验证**: `npx vitest run tests/cart.test.ts`
- **预期**: 测试通过
- **依赖**: Task 1
- **时间**: ~4分钟
# ...
## Task 3: 添加防御措施(SSR安全)
- **文件**: hooks/useCart.ts (修改)
- **描述**: SSR环境下localStorage不存在,需做安全检查
- **代码**: [typeof window检查+try-catch包裹]
- **验证**: `npm run build` 构建成功(无SSR错误)
- **依赖**: Task 2
- **时间**: ~2分钟
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 设计文档不完整 | 缺少关键信息(数据模型/API设计/技术栈) | 标注缺失部分,建议补充后再制定计划,不臆测 |
| 任务太大无法拆分到2-5分钟 | 功能复杂度高或耦合严重 | 进一步分解为多阶段,或拆分子任务,标注"需进一步设计" |
| 依赖不确定 | 模块间耦合关系不明 | 标注假设条件,提供替代路径,建议先做技术调研 |
| 测试无法编写 | 缺乏测试框架或功能不可测 | 先写最小验证(日志/手动测试),标注技术债,建议后续补测试 |
| 计划执行偏差 | 实际执行发现计划不合理 | 允许调整计划,但记录偏差原因,更新plan.md |
| 时间预估不准 | 任务复杂度评估偏差 | 预估时间仅为参考,实际执行以"完成定义"为准 |
| 技术栈版本冲突 | 设计文档指定版本与现有项目冲突 | 标注冲突,提供升级/兼容方案,建议确认后再执行 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:---:|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供计划生成 | 国内Agent(通义/文心/智谱)均可 |
| 前置Skill | Skill | 推荐 | brainstorm-facilitator输出的设计文档 | 任何能产出设计文档的方法 |
| 后续Skill | Skill | 推荐 | plan-executor或subagent-orchestrator执行计划 | 手动执行也可 |
| 测试框架 | 工具 | 推荐 | 项目对应的测试框架(Jest/pytest/Go test/vitest) | 国内cnpm/pip安装 |
| Git | 工具 | 可选 | 版本控制,每个任务一个提交 | 国内用Gitee/GitCode |
| 包管理器 | 工具 | 必需 | npm/pnpm/pip/cargo | 国内用cnpm/tnpm/清华源 |

### API Key 配置
- **本Skill无需额外API Key配置**: 纯方法论指导,计划生成由Agent LLM完成
- **安全要求**: API Key零暴露,不写入计划文档、不输出到日志、不硬编码

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和验证命令运行

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 支付功能集成实现计划(Stripe + Next.js)

**输入**:
```
设计文档: 为SaaS产品添加Stripe订阅支付功能
技术栈: Next.js 15 + TypeScript + Prisma + PostgreSQL
功能: 月度/年度订阅、免费试用14天、Webhook处理支付事件
测试要求: TDD,覆盖率80%+
```

**LLM生成输出** (`output/stripe-payment/plan.md`):
```markdown
# Stripe订阅支付功能实现计划
# ...
## 补充概述
- 目标: 为SaaS产品添加Stripe订阅支付
- 技术栈: Next.js 15 + TypeScript + Prisma + PostgreSQL + Stripe SDK
- 总任务数: 10
- 预估总时间: ~42分钟
# ...
## 依赖关系图
```
Task 1 (安装依赖)
  ├→ Task 2 (Schema测试) → Task 3 (Schema实现) → Task 4 (Migration)
  └→ Task 5 (Stripe配置测试) → Task 6 (Stripe配置实现)
Task 4 + Task 6 → Task 7 (订阅API测试) → Task 8 (订阅API实现)
Task 8 → Task 9 (Webhook测试) → Task 10 (Webhook实现)
```
# ...
## Task 1: 安装Stripe SDK依赖
- **文件**: package.json (修改)
- **描述**: 安装Stripe SDK及其类型定义
- **命令**: `pnpm add stripe @stripe/stripe-js`
- **验证**: `cat package.json | grep stripe` 输出包含stripe和@stripe/stripe-js
- **时间**: ~1分钟
# ...
## Task 2: 编写订阅Schema测试(Red阶段)
- **文件**: tests/schema.test.ts (新建)
- **描述**: 测试Subscription模型字段完整性
- **代码**:
```typescript
import { describe, it, expect } from "vitest";
import { SubscriptionStatus } from "@prisma/client";

describe("Subscription Schema", () => {
  it("应支持所有订阅状态枚举", () => {
    const validStatuses = ["trialing", "active", "past_due", "canceled", "incomplete"];
    validStatuses.forEach((status) => {
      expect(Object.values(SubscriptionStatus)).toContain(status);
    });
  });

  it("应包含必要的订阅字段", () => {
    const requiredFields = [
      "id", "userId", "stripeCustomerId", "stripeSubscriptionId",
      "stripePriceId", "status", "currentPeriodStart", "currentPeriodEnd",
      "trialEnd", "cancelAtPeriodEnd",
    ];
    // 验证Prisma schema包含这些字段
    expect(requiredFields.length).toBe(10);
  });
});
```
- **验证**: `npx vitest run tests/schema.test.ts`
- **预期**: 测试失败(Schema未定义) - Red阶段
- **时间**: ~3分钟
# ...
## Task 3: 实现订阅Schema(Green阶段)
- **文件**: prisma/schema.prisma (修改)
- **描述**: 添加Subscription模型和相关字段
- **代码**:
```prisma
enum SubscriptionStatus {
  trialing
  active
  past_due
  canceled
  incomplete
}

model Subscription {
  id                    String             @id @default(cuid())
  userId                String             @unique
  user                  User               @relation(fields: [userId], references: [id])
  stripeCustomerId      String             @unique
  stripeSubscriptionId  String?            @unique
  stripePriceId         String
  status                SubscriptionStatus @default(incomplete)
  currentPeriodStart    DateTime?
  currentPeriodEnd      DateTime?
  trialEnd              DateTime?
  cancelAtPeriodEnd     Boolean            @default(false)
  createdAt             DateTime           @default(now())
  updatedAt             DateTime           @updatedAt

  @@index([status])
}
```
- **验证**: `npx vitest run tests/schema.test.ts`
- **预期**: 测试通过 - Green阶段
- **依赖**: Task 1, Task 2
- **时间**: ~4分钟
# ...
## Task 4: 运行数据库Migration
- **文件**: prisma/migrations/ (新建)
- **描述**: 生成并应用Subscription表迁移
- **命令**: `npx prisma migrate dev --name add_subscription`
- **验证**: `npx prisma db pull` 输出包含Subscription表
- **依赖**: Task 3
- **时间**: ~2分钟
# ...
## Task 5: 编写Stripe配置测试(Red阶段)
- **文件**: tests/stripe-config.test.ts (新建)
- **描述**: 测试Stripe客户端正确初始化
- **代码**:
```typescript
import { describe, it, expect } from "vitest";
import { getStripeClient } from "../lib/stripe";

describe("Stripe配置", () => {
  it("应返回有效的Stripe客户端实例", () => {
    const stripe = getStripeClient();
    expect(stripe).toBeDefined();
    expect(stripe.customers).toBeDefined();
    expect(stripe.subscriptions).toBeDefined();
  });

  it("应正确配置Webhook端点签名密钥", () => {
    expect(process.env.STRIPE_WEBHOOK_SECRET).toBeDefined();
  });
});
```
- **验证**: `npx vitest run tests/stripe-config.test.ts`
- **预期**: 测试失败(配置未实现) - Red阶段
- **时间**: ~2分钟
# ...
## Task 6: 实现Stripe配置(Green阶段)
- **文件**: lib/stripe.ts (新建)
- **描述**: 创建Stripe客户端单例
- **代码**:
```typescript
import Stripe from "stripe";

let stripeClient: Stripe | null = null;

export function getStripeClient(): Stripe {
  if (!stripeClient) {
    const key = process.env.STRIPE_SECRET_KEY;
    if (!key) throw new Error("STRIPE_SECRET_KEY is required");
    stripeClient = new Stripe(key, {
      apiVersion: "2024-06-20",
      typescript: true,
    });
  }
  return stripeClient;
}

export const STRIPE_PRICES = {
  monthly: process.env.STRIPE_PRICE_MONTHLY!,
  yearly: process.env.STRIPE_PRICE_YEARLY!,
} as const;
```
- **验证**: `npx vitest run tests/stripe-config.test.ts`
- **预期**: 测试通过 - Green阶段
- **依赖**: Task 1, Task 5
- **时间**: ~3分钟
# ...
## Task 7: 编写创建订阅API测试(Red阶段)
- **文件**: tests/api/create-subscription.test.ts (新建)
- **描述**: 测试订阅创建API的输入验证和响应格式
- **代码**:
```typescript
import { describe, it, expect, vi } from "vitest";
import { POST } from "../app/api/subscriptions/route";

vi.mock("../lib/stripe", () => ({
  getStripeClient: () => ({
    customers: { create: vi.fn().mockResolvedValue({ id: "cus_test123" }) },
    subscriptions: { create: vi.fn().mockResolvedValue({ id: "sub_test123", status: "trialing" }) },
  }),
  STRIPE_PRICES: { monthly: "price_monthly", yearly: "price_yearly" },
}));

describe("POST /api/subscriptions", () => {
  it("应拒绝无效的价格计划", async () => {
    const req = new Request("http://localhost/api/subscriptions", {
      method: "POST",
      body: JSON.stringify({ plan: "invalid" }),
    });
    const res = await POST(req);
    expect(res.status).toBe(400);
  });

  it("应成功创建试用订阅", async () => {
    const req = new Request("http://localhost/api/subscriptions", {
      method: "POST",
      body: JSON.stringify({ plan: "monthly", email: "test@example.com" }),
    });
    const res = await POST(req);
    expect(res.status).toBe(200);
    const data = await res.json();
    expect(data.subscriptionId).toBe("sub_test123");
    expect(data.status).toBe("trialing");
  });
});
```
- **验证**: `npx vitest run tests/api/create-subscription.test.ts`
- **预期**: 测试失败(API未实现) - Red阶段
- **时间**: ~4分钟
# ...
## Task 8: 实现创建订阅API(Green阶段)
- **文件**: app/api/subscriptions/route.ts (新建)
- **描述**: 创建Stripe客户+订阅(含14天试用期)
- **代码**:
```typescript
import { NextRequest, NextResponse } from "next/server";
import { getStripeClient, STRIPE_PRICES } from "@/lib/stripe";
import { prisma } from "@/lib/prisma";

export async function POST(req: NextRequest) {
  const body = await req.json();
  const { plan, email, userId } = body;

  if (!plan || !["monthly", "yearly"].includes(plan)) {
    return NextResponse.json({ error: "无效的价格计划" }, { status: 400 });
  }

  const stripe = getStripeClient();

  // 1. 创建Stripe客户
  const customer = await stripe.customers.create({
    email,
    metadata: { userId },
  });

  // 2. 创建订阅(14天试用)
  const subscription = await stripe.subscriptions.create({
    customer: customer.id,
    items: [{ price: STRIPE_PRICES[plan as "monthly" | "yearly"] }],
    trial_period_days: 14,
    metadata: { userId },
  });

  // 3. 保存到数据库
  await prisma.subscription.create({
    data: {
      userId,
      stripeCustomerId: customer.id,
      stripeSubscriptionId: subscription.id,
      stripePriceId: STRIPE_PRICES[plan as "monthly" | "yearly"],
      status: "trialing",
      trialEnd: new Date(Date.now() + 14 * 24 * 60 * 60 * 1000),
    },
  });

  return NextResponse.json({
    subscriptionId: subscription.id,
    status: subscription.status,
  });
}
```
- **验证**: `npx vitest run tests/api/create-subscription.test.ts`
- **预期**: 测试通过 - Green阶段
- **依赖**: Task 4, Task 6, Task 7
- **时间**: ~5分钟
# ...
## Task 9: 编写Webhook处理测试(Red阶段)
- **文件**: tests/api/webhook.test.ts (新建)
- **描述**: 测试Stripe Webhook事件处理
- **代码**:
```typescript
import { describe, it, expect, vi } from "vitest";
import { POST } from "../app/api/stripe/webhook/route";

vi.mock("../lib/stripe", () => ({
  getStripeClient: () => ({
    webhooks: {
      constructEvent: vi.fn().mockReturnValue({
        type: "customer.subscription.updated",
        data: {
          object: {
            id: "sub_test123",
            customer: "cus_test123",
            status: "active",
            current_period_start: 1700000000,
            current_period_end: 1702592000,
          },
        },
      }),
    },
  }),
}));

describe("POST /api/stripe/webhook", () => {
  it("应处理subscription.updated事件", async () => {
    const req = new Request("http://localhost/api/stripe/webhook", {
      method: "POST",
      headers: { "stripe-signature": "test_sig" },
      body: JSON.stringify({ id: "evt_test" }),
    });
    const res = await POST(req);
    expect(res.status).toBe(200);
  });
});
```
- **验证**: `npx vitest run tests/api/webhook.test.ts`
- **预期**: 测试失败 - Red阶段
- **时间**: ~3分钟
# ...
## Task 10: 实现Webhook处理(Green阶段)
- **文件**: app/api/stripe/webhook/route.ts (新建)
- **描述**: 处理Stripe Webhook事件,同步订阅状态
- **代码**:
```typescript
import { NextRequest, NextResponse } from "next/server";
import { getStripeClient } from "@/lib/stripe";
import { prisma } from "@/lib/prisma";

export async function POST(req: NextRequest) {
  const body = await req.text();
  const signature = req.headers.get("stripe-signature")!;
  const stripe = getStripeClient();

  let event;
  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    );
  } catch (err) {
    return NextResponse.json({ error: "签名验证失败" }, { status: 400 });
  }

  switch (event.type) {
    case "customer.subscription.updated":
    case "customer.subscription.deleted": {
      const sub = event.data.object;
      await prisma.subscription.update({
        where: { stripeSubscriptionId: sub.id },
        data: {
          status: sub.status,
          currentPeriodStart: new Date(sub.current_period_start * 1000),
          currentPeriodEnd: new Date(sub.current_period_end * 1000),
          cancelAtPeriodEnd: sub.cancel_at_period_end,
        },
      });
      break;
    }
    case "invoice.payment_failed": {
      const invoice = event.data.object;
      await prisma.subscription.update({
        where: { stripeCustomerId: invoice.customer as string },
        data: { status: "past_due" },
      });
      break;
    }
  }

  return NextResponse.json({ received: true });
}
```
- **验证**: `npx vitest run tests/api/webhook.test.ts`
- **预期**: 测试通过 - Green阶段
- **依赖**: Task 8, Task 9
- **时间**: ~5分钟
# ...
## 执行检查清单
- [ ] Task 1: 安装Stripe SDK
- [ ] Task 2: Schema测试(Red)
- [ ] Task 3: Schema实现(Green)
- [ ] Task 4: Migration
- [ ] Task 5: Stripe配置测试(Red)
- [ ] Task 6: Stripe配置实现(Green)
- [ ] Task 7: 订阅API测试(Red)
- [ ] Task 8: 订阅API实现(Green)
- [ ] Task 9: Webhook测试(Red)
- [ ] Task 10: Webhook实现(Green)
# ...
## 验证命令
```bash
# 全部测试
npx vitest run

# 覆盖率检查
npx vitest run --coverage

# 类型检查
npx tsc --noEmit

# 集成测试(需Stripe测试密钥)
STRIPE_SECRET_KEY=sk_test_xxx npx vitest run tests/api/
```
```

**效果验证**: ✓10个任务粒度合理(1-5分钟,Task1为安装命令约1分钟) ✓TDD红绿循环完整(Red→Green) ✓依赖关系图清晰 ✓每个任务含文件路径+代码+验证命令 ✓YAGNI原则(只实现核心订阅+Webhook,未提前实现退款/发票)

### 案例2: 数据库迁移计划(MySQL→PostgreSQL)

**输入**:
```
需求: 将生产环境从MySQL 5.7迁移到PostgreSQL 15
当前数据量: 50GB, 120张表, 8个存储过程
要求: 零停机迁移,支持回滚,数据一致性验证
```

**LLM生成输出** (`output/mysql-to-pg/plan.md`):
```markdown
# MySQL到PostgreSQL迁移计划
# ...
## 概述(续3)
- 目标: MySQL 5.7 → PostgreSQL 15 零停机迁移
- 数据量: 50GB / 120张表 / 8个存储过程
- 策略: 双写+增量同步+切换+回滚
- 总任务数: 8
- 预估总时间: ~45分钟(计划制定), 实际迁移4-8小时
# ...
## 依赖关系图(续1)
```
Task 1 (Schema映射) → Task 2 (PG Schema创建)
Task 2 → Task 3 (全量迁移脚本) → Task 4 (全量迁移验证)
Task 2 → Task 5 (双写层测试) → Task 6 (双写层实现)
Task 6 → Task 7 (增量同步) → Task 8 (切换+回滚方案)
```
# ...
## Task 1: 创建Schema映射文档
- **文件**: docs/migration/schema-mapping.md (新建)
- **描述**: 逐表记录MySQL到PG的类型映射和SQL差异
- **代码**:
```markdown
# MySQL → PostgreSQL Schema映射

## 类型映射表
| MySQL | PostgreSQL | 注意事项 |
|:-------|-------:|:-------|
| TINYINT(1) | BOOLEAN | MySQL的TINYINT(1)常做布尔用 |
| INT AUTO_INCREMENT | SERIAL | PG用SERIAL或IDENTITY |
| DATETIME | TIMESTAMP | PG推荐TIMESTAMP WITH TIME ZONE |
| TEXT | TEXT | 相同 |
| ENUM | VARCHAR + CHECK | PG也可用CREATE TYPE enum |
| JSON | JSONB | PG的JSONB支持索引,优于JSON |
| DOUBLE | DOUBLE PRECISION | 相同 |
| MEDIUMTEXT | TEXT | PG无MEDIUMTEXT,统一用TEXT |

## 存储过程迁移
- MySQL存储过程语法 → PL/pgSQL函数
- 8个存储过程需逐个手动改写
- 注意: MySQL的DELIMITER // → PG的$$语法

## 特殊处理
1. MySQL的ON UPDATE CURRENT_TIMESTAMP → PG用TRIGGER实现
2. MySQL的LIMIT offset,count → PG的LIMIT count OFFSET offset
3. MySQL的反引号`` → PG的双引号""
4. MySQL的CONCAT() → PG的|| 操作符
```
- **验证**: 人工review映射文档完整性
- **时间**: ~5分钟
# ...
## Task 2: 编写PG Schema创建脚本
- **文件**: migrations/pg-schema.sql (新建)
- **描述**: 创建PostgreSQL版本的表结构(含索引和约束)
- **代码**:
```sql
-- 示例: users表迁移
-- MySQL原版:
-- CREATE TABLE users (
--   id INT AUTO_INCREMENT PRIMARY KEY,
--   email VARCHAR(255) NOT NULL,
--   is_active TINYINT(1) DEFAULT 1,
--   data JSON,
--   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
--   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );

-- PostgreSQL版本:
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  data JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ON UPDATE CURRENT_TIMESTAMP用TRIGGER实现
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER users_updated_at
  BEFORE UPDATE ON users
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at();

-- JSONB字段添加GIN索引(比MySQL JSON查询更快)
CREATE INDEX idx_users_data ON users USING GIN (data);

-- 唯一索引
CREATE UNIQUE INDEX idx_users_email ON users (email);
```
- **验证**: `psql -d testdb -f migrations/pg-schema.sql && psql -d testdb -c "\dt" | grep users`
- **依赖**: Task 1
- **时间**: ~5分钟
# ...
## Task 3: 编写全量数据迁移脚本测试
- **文件**: tests/migration.test.ts (新建)
- **描述**: 测试数据迁移脚本的行数一致性和类型转换
- **代码**:
```typescript
import { describe, it, expect } from "vitest";
import { migrateTable } from "../scripts/migrate";
import { mysqlCount, pgCount } from "./helpers";

describe("全量数据迁移", () => {
  it("users表行数应一致", async () => {
    await migrateTable("users");
    const mysqlTotal = await mysqlCount("users");
    const pgTotal = await pgCount("users");
    expect(pgTotal).toBe(mysqlTotal);
  });

  it("JSON字段应正确转换为JSONB", async () => {
    const pgRow = await pgQuery("SELECT data FROM users WHERE id = 1");
    expect(pgRow.data).toEqual({ name: "test", roles: ["admin"] });
  });

  it("布尔字段应正确转换", async () => {
    const pgRow = await pgQuery("SELECT is_active FROM users WHERE id = 1");
    expect(typeof pgRow.is_active).toBe("boolean");
  });
});
```
- **验证**: `npx vitest run tests/migration.test.ts`
- **预期**: 测试失败(迁移脚本未实现)
- **时间**: ~4分钟
# ...
## Task 4: 实现全量数据迁移脚本
- **文件**: scripts/migrate.ts (新建)
- **描述**: 分批从MySQL读取并写入PostgreSQL
- **代码**:
```typescript
import mysql from "mysql2/promise";
import pg from "pg";
import { TABLES } from "./config";

const BATCH_SIZE = 1000;

export async function migrateTable(tableName: string) {
  const mysqlConn = await mysql.createConnection(process.env.MYSQL_URL!);
  const pgClient = new pg.Client({ connectionString: process.env.PG_URL! });
  await pgClient.connect();

  const [countResult] = await mysqlConn.query(`SELECT COUNT(*) as count FROM ${tableName}`);
  const total = (countResult as any)[0].count;
  console.log(`迁移 ${tableName}: ${total} 行`);

  for (let offset = 0; offset < total; offset += BATCH_SIZE) {
    const [rows] = await mysqlConn.query(
      `SELECT * FROM ${tableName} LIMIT ${BATCH_SIZE} OFFSET ${offset}`
    );

    if ((rows as any[]).length === 0) break;

    // 批量插入PG
    const values = (rows as any[]).map((row) => transformRow(tableName, row));
    const placeholders = values.map((_, i) =>
      `(${Object.keys(values[0]).map((_, j) => `$${i * Object.keys(values[0]).length + j + 1}`).join(",")})`
    ).join(",");

    const flatValues = values.flatMap((v) => Object.values(v));
    const columns = Object.keys(values[0]).join(",");

    await pgClient.query(
      `INSERT INTO ${tableName} (${columns}) VALUES ${placeholders}`,
      flatValues
    );

    console.log(`  ${tableName}: ${offset + (rows as any[]).length}/${total}`);
  }

  await mysqlConn.end();
  await pgClient.end();
}

function transformRow(table: string, row: any): any {
  // TINYINT(1) → boolean
  if (table === "users") {
    row.is_active = !!row.is_active;
    if (typeof row.data === "string") row.data = JSON.parse(row.data);
  }
  return row;
}
```
- **验证**: `npx vitest run tests/migration.test.ts`
- **预期**: 测试通过
- **依赖**: Task 2, Task 3
- **时间**: ~5分钟
# ...
## Task 5: 编写双写层测试(Red阶段)
- **文件**: tests/dual-write.test.ts (新建)
- **描述**: 测试双写层同时写入MySQL和PG
- **代码**:
```typescript
import { describe, it, expect } from "vitest";
import { dualWriteUser } from "../lib/dual-write";

describe("双写层", () => {
  it("应同时写入MySQL和PostgreSQL", async () => {
    const userData = { email: "test@example.com", is_active: true };
    const result = await dualWriteUser(userData);
    expect(result.mysqlId).toBeDefined();
    expect(result.pgId).toBeDefined();
    expect(result.mysqlId).toBe(result.pgId);
  });

  it("PG写入失败时MySQL应回滚", async () => {
    // 模拟PG故障
    process.env.PG_URL = "postgresql://invalid";
    await expect(dualWriteUser({ email: "fail@test.com" }))
      .rejects.toThrow("PG写入失败");
  });
});
```
- **验证**: `npx vitest run tests/dual-write.test.ts`
- **预期**: 测试失败
- **时间**: ~3分钟
# ...
## Task 6: 实现双写层(Green阶段)
- **文件**: lib/dual-write.ts (新建)
- **描述**: 应用层双写,同时写入MySQL和PG,任一失败则回滚
- **代码**:
```typescript
import { prismaMysql, prismaPg } from "./prisma-clients";

export async function dualWriteUser(data: { email: string; is_active: boolean }) {
  // 先写MySQL
  const mysqlUser = await prismaMysql.user.create({ data });

  try {
    // 再写PG(使用相同ID)
    const pgUser = await prismaPg.user.create({
      data: { ...data, id: mysqlUser.id },
    });
    return { mysqlId: mysqlUser.id, pgId: pgUser.id };
  } catch (error) {
    // PG失败,回滚MySQL
    await prismaMysql.user.delete({ where: { id: mysqlUser.id } });
    throw new Error("PG写入失败,MySQL已回滚");
  }
}
```
- **验证**: `npx vitest run tests/dual-write.test.ts`
- **预期**: 测试通过
- **依赖**: Task 5
- **时间**: ~4分钟
# ...
## Task 7: 实现增量同步(基于binlog)
- **文件**: scripts/sync-incremental.ts (新建)
- **描述**: 监听MySQL binlog,实时同步增量变更到PG
- **代码**:
```typescript
import { Zongji } from "zongji";
import { pgClient } from "./pg-client";

const zongji = new Zongji({
  host: process.env.MYSQL_HOST,
  user: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  // 从指定binlog位置开始
  serverId: 100,
  startAtEnd: true,
});

zongji.on("binlog", (event) => {
  if (event.getTypeName() === "TableMap") return;

  const { table, rows } = event;
  if (event.getTypeName() === "WriteRows") {
    rows.forEach(async (row) => {
      const transformed = transformRow(table, row);
      await pgClient.query(
        `INSERT INTO ${table} (${Object.keys(transformed).join(",")}) VALUES (${Object.keys(transformed).map((_, i) => `$${i + 1}`).join(",")})`,
        Object.values(transformed)
      );
    });
  } else if (event.getTypeName() === "UpdateRows") {
    rows.forEach(async (row) => {
      const transformed = transformRow(table, row.after);
      const sets = Object.keys(transformed).map((k, i) => `${k}=$${i + 1}`).join(",");
      await pgClient.query(
        `UPDATE ${table} SET ${sets} WHERE id = $${Object.keys(transformed).length + 1}`,
        [...Object.values(transformed), transformed.id]
      );
    });
  } else if (event.getTypeName() === "DeleteRows") {
    rows.forEach(async (row) => {
      await pgClient.query(`DELETE FROM ${table} WHERE id = $1`, [row.id]);
    });
  }
});

zongji.start();
console.log("增量同步已启动,监听MySQL binlog...");
```
- **验证**: 在MySQL插入测试数据,检查PG是否同步
- **依赖**: Task 6
- **时间**: ~5分钟
# ...
## Task 8: 切换与回滚方案文档
- **文件**: docs/migration/cutover-plan.md (新建)
- **描述: 零停机切换步骤和回滚方案
- **代码**:
```markdown
# 切换与回滚方案

## 切换步骤(预计停机<5分钟)
1. [T-0] 通知用户维护窗口,设置只读模式
2. [T+1min] 停止应用写入,等待binlog同步完成
3. [T+2min] 运行数据一致性校验脚本
4. [T+3min] 切换应用数据库连接到PostgreSQL
5. [T+4min] 验证应用功能正常
6. [T+5min] 恢复正常服务,移除只读模式
7. [T+1h] 观察无异常后,关闭双写和增量同步

## 回滚方案
### 触发条件
- 数据一致性校验失败
- 切换后应用报错率>1%
- 关键功能不可用

### 回滚步骤
1. 立即将应用数据库连接切回MySQL
2. MySQL仍保持双写期间的数据(未停止双写)
3. 回滚后检查MySQL数据完整性
4. 排查PG问题后重新执行迁移

### 回滚验证
- 验证MySQL读写正常
- 验证无数据丢失(对比切换前后的行数)
- 验证应用功能恢复
```
- **验证**: 团队review切换和回滚方案
- **依赖**: Task 7
- **时间**: ~4分钟
# ...
## 执行检查清单(续1)
- [ ] Task 1: Schema映射文档
- [ ] Task 2: PG Schema创建脚本
- [ ] Task 3: 迁移测试(Red)
- [ ] Task 4: 迁移脚本(Green)
- [ ] Task 5: 双写层测试(Red)
- [ ] Task 6: 双写层实现(Green)
- [ ] Task 7: 增量同步
- [ ] Task 8: 切换回滚方案
```

**效果验证**: ✓零停机策略完整(双写+增量同步+切换) ✓类型映射精确(TINYINT→BOOLEAN/JSON→JSONB) ✓ON UPDATE用TRIGGER替代 ✓回滚方案含触发条件+步骤 ✓数据一致性校验脚本

### 案例3: 技术债务清理计划(优先级排序)

**输入**:
```
技术债务清单:
1. 全项目使用any类型(约200处)
2. 测试覆盖率仅35%(目标80%)
3. 存在3个已弃用的API仍在使用
4. 重复的工具函数散落在5个文件中
5. eslint有120个warning未处理
时间约束: 每周可投入8小时,持续4周
```

**LLM生成输出** (`output/tech-debt/plan.md`):
```markdown
# 技术债务清理计划
# ...
## 概述(续4)
- 债务项: 5项
- 可用时间: 4周 × 8小时/周 = 32小时
- 策略: 按影响×紧急度排序,渐进式清理
# ...
## 债务优先级矩阵
| 债务项 | 影响 | 紧急度 | 预估工时 | 优先级 | 安排周次 |
|---:|:---|---:|---:|:---|---:|
| 已弃用API使用 | 高(安全风险) | 高 | 6h | P0 | 第1周 |
| any类型(200处) | 中(类型安全) | 中 | 12h | P1 | 第2-3周 |
| 测试覆盖率35% | 高(质量风险) | 中 | 8h | P1 | 第3周 |
| 重复工具函数 | 低(可维护性) | 低 | 3h | P2 | 第4周 |
| eslint 120 warning | 低(代码规范) | 低 | 3h | P2 | 第4周 |
# ...
---
# ...

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。
## 第1周: 清理已弃用API(P0, 6h)
# ...
### Task 1: 检测已弃用API使用位置
- **文件**: scripts/find-deprecated.ts (新建)
- **描述**: 扫描代码中使用的已弃用API
- **命令**: `npx ts-migrate deprecated ./src`
- **验证**: 输出弃用API清单及使用位置
- **时间**: ~1h
# ...
### Task 2: 逐个替换弃用API(3个API)
- **文件**: src/api/ (多个文件修改)
- **描述**: 将弃用API替换为新版API
- **验证**: `npx tsc --noEmit` 无弃用警告
- **依赖**: Task 1
- **时间**: ~3h
# ...
### Task 3: 添加弃用API的eslint规则
- **文件**: .eslintrc.js (修改)
- **描述**: 添加deprecation规则防止未来再次使用
- **代码**:
```javascript
module.exports = {
  rules: {
    "deprecation/deprecation": "error",
  },
};
```
- **验证**: `npx eslint ./src --rule 'deprecation/deprecation: error'`
- **依赖**: Task 2
- **时间**: ~2h
# ...
---
# ...
## 第2-3周: 消除any类型(P1, 12h)
# ...
### Task 4: 生成any类型使用报告
- **命令**: `npx tsc --noEmit --noImplicitAny | grep "implicitly has an 'any'" | wc -l`
- **验证**: 确认约200处any类型
- **时间**: ~0.5h
# ...
### Task 5: 按模块逐步替换any(5个模块)
- **策略**: 每次处理一个模块,替换后跑测试确认无回归
- **模块**: auth(40处) → api(60处) → utils(30处) → components(40处) → types(30处)
- **每个模块流程**:
  1. 识别any使用场景
  2. 定义正确的TypeScript类型
  3. 替换any
  4. `npx tsc --noEmit` 检查类型
  5. `npx vitest run` 确认测试通过
- **验证**: 每模块any数量降至0
- **时间**: ~10h(2h/模块 × 5模块)
# ...
### Task 6: 开启strict模式
- **文件**: tsconfig.json (修改)
- **代码**:
```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true
  }
}
```
- **验证**: `npx tsc --noEmit` 零错误
- **依赖**: Task 5
- **时间**: ~1.5h
# ...
---
# ...
## 第3周: 提升测试覆盖率(P1, 8h)
# ...
### Task 7: 生成覆盖率报告
- **命令**: `npx vitest run --coverage`
- **验证**: 确认当前覆盖率35%,识别未覆盖模块
- **时间**: ~0.5h
# ...
### Task 8: 补充核心模块测试
- **策略**: 优先覆盖核心业务逻辑(auth/api/services)
- **目标**: 从35%提升至65%
- **验证**: `npx vitest run --coverage` 覆盖率≥65%
- **时间**: ~6h
# ...
### Task 9: 补充工具函数测试
- **目标**: 工具函数覆盖率100%
- **验证**: `npx vitest run --coverage` utils模块100%
- **依赖**: Task 8
- **时间**: ~1.5h
# ...
---
# ...
## 第4周: 消除重复+eslint警告(P2, 6h)
# ...
### Task 10: 合并重复工具函数
- **描述**: 将5个文件中的重复函数提取到 src/utils/shared.ts
- **原则**: Rule of Three(重复3次以上才提取)
- **验证**: `npx ts-prune` 无未使用的导出
- **时间**: ~3h
# ...
### Task 11: 修复eslint 120个warning
- **策略**: 自动修复 + 手动修复
- **命令**: `npx eslint ./src --fix` (自动修复约60%)
- **验证**: `npx eslint ./src` warning数量为0
- **时间**: ~3h
# ...
## 总览
| 周次 | 债务项 | 投入工时 | 预期效果 |
|:------:|--------|:-------|:------:|
| 第1周 | 弃用API | 6h | 0个弃用API + eslint规则 |
| 第2周 | any类型(前半) | 8h | any从200→100 |
| 第3周 | any类型(后半)+测试 | 8h | any→0, 覆盖率35%→65% |
| 第4周 | 重复函数+eslint | 6h | 0 warning, 0重复 |
| 合计 | - | 28h(余4h缓冲) | 全部债务清理完成 |
```

**效果验证**: ✓债务按影响×紧急度排序 ✓4周32小时分配合理(含4h缓冲) ✓每项含具体Task+验证命令 ✓渐进式清理(逐模块替换any) ✓防御措施(eslint规则防回归)

## 常见问题

### Q1: 为什么要拆分到2-5分钟粒度?
A: 2-5分钟粒度确保每个任务足够小,初级工程师能独立完成且容易验证。粒度太大容易中途出错或偏离方向,粒度太小则计划文档过于冗长。这个粒度也便于在Agent中逐步执行,每个任务完成后可检查点验证。对于复杂任务,先拆为多阶段再逐阶段细拆。

### Q2: TDD计划中测试先写但失败了怎么办?
A: 测试先失败(Red)是TDD的正常流程,表示功能尚未实现。然后写最小实现使测试通过(Green),最后重构(Refactor)。如果测试本身有语法错误或测试框架问题,需先修复测试代码。计划中每个Task都标注"预期:测试失败/通过"状态,帮助执行者判断是否在正确轨道上。

### Q3: 如何处理任务间的依赖关系?
A: 在任务描述中用"**依赖**: Task M"标注。无依赖任务可并行执行(如前端UI和后端API可并行),有依赖任务必须按序执行(如先创建Schema再写数据访问层)。计划文档开头提供依赖关系图,帮助执行者理解执行顺序。建议按依赖拓扑排序排列任务。

### Q4: YAGNI原则和提前设计冲突吗?
A: YAGNI(You Aren't Gonna Need It)强调不实现"可能需要"的功能,但不是不设计。设计阶段可以预留扩展点(如接口设计),但实现阶段只做当前需要的功能。例如:设计用户系统时可以预留角色字段,但只实现当前需要的邮箱密码登录,不提前实现OAuth(等需要时再加)。

### Q5: 计划执行中发现设计有问题怎么办?
A: (1)暂停执行,记录遇到的问题;(2)评估问题严重程度:小问题(如字段名调整)可在计划中修正后继续,大问题(如架构方向错误)需回到设计阶段;(3)更新plan.md,记录偏差原因;(4)计划是可调整的,不是一成不变的,但每次调整都需记录。

## 已知限制

- 计划质量取决于设计文档质量,设计文档不完整或含错误会导致计划不合理,需先确保设计文档完整准确
- 2-5分钟粒度是目标值,部分复杂任务(如数据库Schema设计、复杂算法实现)可能超出,需进一步拆分或标注"需更多时间"
- 计划基于当前已知信息制定,执行中可能遇到未预见的技术障碍(如第三方库bug、兼容性问题),需灵活调整
- TDD驱动计划假设项目有测试框架,无测试框架的项目需先搭建测试基础设施
- 时间预估为参考值,实际执行时间受开发者经验、环境配置、调试难度等因素影响,可能偏差较大

## 安全

- **API Key零暴露**: 计划文档中不包含任何API Key、密码、密钥,涉及认证的任务只描述配置方法,不写入实际凭据
- **敏感信息脱敏**: 示例代码中使用占位符(如`your-api-key-here`),不使用真实凭据
- **测试数据安全**: 测试用例不使用真实用户数据,使用mock数据或测试专用数据
- **回滚步骤安全**: 计划中的回滚步骤不删除用户数据,只回滚代码变更
- **依赖来源可信**: 计划中推荐的依赖包来自官方源或可信镜像(国内用cnpm/清华源),不推荐未知来源包
