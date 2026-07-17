---
slug: nextjs-fullstack-guide
name: nextjs-fullstack-guide
version: "1.0.0"
displayName: "Next.js全栈指南"
summary: "基于Vercel官方最佳实践,Next.js全栈应用从路由到部署全流程指导"
license: Apache-2.0
description: |-
  Next.js全栈指南——基于Vercel官方最佳实践构建生产级全栈应用。从App Router路由设计到Server Components,从数据获取到性能优化,从认证集成到部署配置,全流程专业指导。

  核心能力:
  - App Router架构:路由结构/布局/加载状态/错误边界
  - Server/Client Components:服务端渲染与客户端交互平衡
  - 数据获取策略:SSR/SSG/ISR/流式渲染按场景选择
  - 中间件与认证:Middleware认证+Server Actions
  - API路由设计:Route Handlers+边缘运行时
  - 性能与SEO:Core Web Vitals优化+元数据管理
  - 部署配置:Vercel/Docker/自托管全方案

  适用场景:
  - 独立创业者全栈应用:前后端一体的Web应用快速上线
  - 电商卖家在线商店:SSR/ISR+Server Actions商品展示与支付
  - SaaS创业者数据面板:Middleware认证+Server Components仪表盘
  - 副业达人博客CMS:SSG/ISR+MDX内容管理+SEO优化

  差异化:不是基础Next.js教程,而是基于Vercel官方最佳实践的生产级全栈指南,覆盖架构到部署全链路,让个人开发者也能构建企业级Web应用。

  触发关键词:Next.js、React、App Router、Server Components、全栈、Web应用、Vercel、SSR、SSG、ISR、中间件
tags: [Next.js, 全栈开发, React, 前端框架, Vercel]
tools: [read, exec]
---

# Next.js全栈指南

基于 Vercel 官方最佳实践,构建生产级 Next.js 全栈应用。从路由设计到数据获取,从性能优化到部署配置,全流程指导。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 全栈Web应用 | 需要前后端一体 | App Router + API Routes + 数据库 |
| 电商网站 | 商品展示+购物车+支付 | SSR/ISR + Server Actions |
| SaaS面板 | 仪表盘+认证+API | Middleware认证 + Server Components |
| 博客/CMS | 内容管理+SEO | SSG/ISR + MDX + 元数据 |
| 实时应用 | 实时数据更新 | WebSocket/SSE + Server Actions |

## 工作流

### 1. 项目架构设计

1. **路由结构(App Router)**
   - `app/`:基于文件系统的路由
   - `layout.tsx`:根布局/嵌套布局
   - `page.tsx`:页面组件
   - `loading.tsx`:加载状态
   - `error.tsx`:错误边界
   - `not-found.tsx`:404页面
   - `route.ts`:API 路由
2. **组件分层**
   - Server Components(默认):数据获取/静态渲染
   - Client Components('use client'):交互/状态/浏览器API
   - Shared Components:两端共用
3. **目录组织**
   - `app/`:路由与页面
   - `components/`:UI组件
   - `lib/`:工具函数/配置
   - `actions/`:Server Actions
   - `types/`:TypeScript类型

### 2. 数据获取策略

1. **Server Components 中获取**
   - 直接使用 async/await
   - 推荐使用 fetch(自动缓存/去重)
   - `{ cache: 'no-store' }`:不缓存(实时数据)
   - `{ next: { revalidate: 60 } }`:ISR(定时重新验证)
2. **Server Actions**
   - `'use server'` 标记的服务端函数
   - 表单提交/数据变更
   - 自动重验证关联路由
   - `revalidatePath()` / `revalidateTag()`
3. **客户端数据获取**
   - SWR / TanStack Query
   - 适用于实时更新/客户端交互
4. **流式渲染**
   - `loading.tsx`:路由级 Suspense
   - `<Suspense>`:组件级流式
   - 骨架屏 + 渐进式加载

### 3. 中间件与认证

1. **Middleware**
   - `middleware.ts`:请求拦截
   - 认证检查/重定向/A-B测试
   - 基于 Cookie/Header 的路由
2. **认证集成**
   - NextAuth.js / Auth.js
   - Better Auth
   - Clerk(托管认证)
   - 自定义 JWT/Cookie

### 4. 性能优化

1. **渲染策略**
   - SSG(默认):构建时生成
   - SSR:请求时渲染
   - ISR:静态+定时更新
   - Streaming:流式渲染
2. **优化手段**
   - `next/image`:图片自动优化
   - `next/font`:字体优化
   - `next/script`:脚本加载策略
   - `next/link`:路由预取
   - React `lazy`/`Suspense`:代码分割
3. **Core Web Vitals**
   - LCP < 2.5s
   - FID < 100ms
   - CLS < 0.1

### 5. 部署配置

1. **Vercel 部署**(推荐)
   - Git push 自动部署
   - 预览部署(PR 预览)
   - 环境变量管理
   - Edge/Node 运行时选择
2. **自托管**
   - `next build` + `next start`
   - Docker 容器化
   - `output: 'standalone'` 精简镜像
3. **环境管理**
   - `.env.local`:本地开发
   - `.env.production`:生产环境
   - Vercel 环境变量

## 依赖说明

| 依赖类型 | 要求 | 说明 |
|:---------|:-----|:-----|
| LLM | 任意支持 Agent Skills 的 LLM | Claude/GPT/Gemini 等 |
| 运行环境 | Node.js 18.17+ | Next.js 最低版本要求 |
| 框架 | Next.js 14+ (推荐15+) | App Router 需要 13.4+ |
| 包管理 | npm/pnpm/yarn | 推荐 pnpm(性能更好) |
| 数据库 | 可选(Prisma/Drizzle/直接SQL) | 根据项目需求选择 |
| 部署平台 | Vercel(推荐) / 自托管 | Vercel 免费版可用 |
| 可选 | NextAuth.js / Clerk | 认证方案 |

## 异常处理

| 异常场景 | 处理方式 |
|:---------|:---------|
| 水合错误 | 检查 Server/Client 组件边界,避免 window/document 在 Server 端使用 |
| 数据获取失败 | error.tsx 错误边界 + 重试机制 |
| 构建失败 | 检查 TypeScript 类型,验证环境变量 |
| 性能问题 | 使用 Next.js DevTools 分析,检查渲染策略 |
| 认证重定向循环 | 检查 Middleware 逻辑,排除公开路由 |
| 环境变量未定义 | 检查 .env 文件,验证部署平台配置 |

## 示例

### 输入:创建电商产品页

```
用户请求:创建一个电商产品详情页,支持 ISR(每60秒重新验证)

输出:
- app/products/[id]/page.tsx (Server Component, fetch 产品数据, revalidate: 60)
- app/products/[id]/loading.tsx (骨架屏)
- app/products/[id]/error.tsx (错误边界)
- components/ProductGallery.tsx (Client Component, 图片轮播)
- actions/add-to-cart.ts (Server Action, 添加购物车)
```

### 输入:创建认证中间件

```
用户请求:创建认证中间件,保护 /dashboard 路由

输出:
- middleware.ts (检查 session cookie, 未认证重定向到 /login)
- matcher 配置: ['/dashboard/:path*']
```
