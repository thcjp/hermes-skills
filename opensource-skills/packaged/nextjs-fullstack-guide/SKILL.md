---
slug: nextjs-fullstack-guide
name: nextjs-fullstack-guide
version: 1.1.0
displayName: Next.js全栈指南
summary: 基于Vercel官方优选实践,Next.js全栈应用从路由到部署全流程指导
license: Proprietary
description: Next.js全栈指南基于Vercel官方优选实践构建生产级全栈应用,核心功能包括App Router路由设计、Server/Client组件分层、数据获取策略(SSR/SSG/ISR/Streaming)、Middleware认证、性能优化(Core
  Web Vitals)和部署配置。适用于电商网站、SaaS面板、博客CMS、实时应用等全栈Web场景。触发关键词:Next.js、React、App Router、Server
  Components、全栈、Web应用、Vercel、SSR、SSG、ISR、中间件。
tags:
- Next.js
- 全栈开发
- React
- 前端框架
- Vercel
tools:
- read
- exec
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "write", "exec"]
tags: "UI设计,前端,设计"
---
# Next.js全栈指南

基于 Vercel 官方优选实践,构建生产级 Next.js 全栈应用。从路由设计到数据获取,从性能优化到部署配置,全流程指导。

## 核心能力

1. **App Router架构设计**:基于文件系统的路由(layout.tsx/page.tsx/loading.tsx/error.tsx/not-found.tsx/route.ts),Server Components(默认)与Client Components('use client')分层,目录组织(app/components/lib/actions/types)。
2. **数据获取策略**:Server Components中async/await+fetch自动缓存去重,Server Actions('use server')处理表单提交与数据变更,revalidatePath/revalidateTag重验证,客户端SWR/TanStack Query,流式渲染(Suspense+loading.tsx)。
3. **中间件与认证集成**:middleware.ts请求拦截(认证检查/重定向/A-B测试),NextAuth.js/Auth.js/Better Auth/Clerk认证方案选型与实现。
4. **性能优化**:SSG/SSR/ISR/Streaming渲染策略选择,next/image/next/font/next/script/next/link内置优化,Core Web Vitals目标达成(LCP<2.5s/FID<100ms/CLS<0.1)。
5. **部署配置**:Vercel部署(Git push自动部署/预览部署/环境变量)与自托管(next build+next start/Docker/output:standalone),环境管理(.env.local/.env.production)。

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 全栈Web应用 | 业务需求+技术栈选择 | App Router+API Routes+数据库的全栈项目代码,输出到`output/{project}/` |
| 电商网站 | 商品/购物车/支付需求 | SSR/ISR产品页+Server Actions购物车+支付集成,输出到`output/{project}/` |
| SaaS面板 | 仪表盘+认证+API需求 | Middleware认证+Server Components仪表盘+API路由,输出到`output/{project}/` |
| 博客/CMS | 内容管理+SEO需求 | SSG/ISR+MDX+元数据的博客系统,输出到`output/{project}/` |
| 实时应用 | 实时数据更新需求 | WebSocket/SSE+Server Actions的实时应用,输出到`output/{project}/` |

**不适用于**:
- 纯静态网站(无服务端逻辑,用Astro/Hugo更轻量)
- 纯客户端SPA(无SSR需求,用Vite+React更简单)
- 移动端原生App(用React Native/Flutter)
- 对首屏性能要求极端且无动态内容的场景(SSG静态生成工具更优)

## 使用流程

### Step 1: 项目架构设计
1. 路由结构(App Router):`app/`目录,layout.tsx根布局/嵌套布局,page.tsx页面,loading.tsx加载,error.tsx错误边界,not-found.tsx 404,route.ts API路由
2. 组件分层:Server Components(默认,数据获取/静态渲染)、Client Components('use client',交互/状态/浏览器API)、Shared Components(两端共用)
3. 目录组织:`app/`(路由与页面)、`components/`(UI组件)、`lib/`(工具函数/配置)、`actions/`(Server Actions)、`types/`(TypeScript类型)

### Step 2: 数据获取策略选择
1. Server Components中获取:直接async/await,推荐fetch(自动缓存/去重),`{ cache: 'no-store' }`不缓存,`{ next: { revalidate: 60 } }` ISR
2. Server Actions:`'use server'`标记,表单提交/数据变更,revalidatePath/revalidateTag重验证
3. 客户端获取:SWR/TanStack Query,适用于实时更新/客户端交互
4. 流式渲染:loading.tsx路由级Suspense,`<Suspense>`组件级流式,骨架屏+渐进式加载

### Step 3: 中间件与认证实现
1. Middleware:middleware.ts请求拦截,认证检查/重定向/A-B测试,基于Cookie/Header路由
2. 认证集成:NextAuth.js/Auth.js(开源)、Better Auth、Clerk(托管)、自定义JWT/Cookie

### Step 4: 性能优化实施
1. 渲染策略:SSG(默认,构建时生成)、SSR(请求时渲染)、ISR(静态+定时更新)、Streaming(流式渲染)
2. 优化手段:next/image(图片自动优化)、next/font(字体优化)、next/script(脚本加载策略)、next/link(路由预取)、React lazy/Suspense(代码分割)
3. Core Web Vitals目标:LCP<2.5s、FID<100ms、CLS<0.1

### Step 5: 部署配置
1. **Vercel部署**(海外推荐):Git push自动部署,预览部署(PR预览),环境变量管理,Edge/Node运行时选择
2. **国内自托管**:`next build`+`next start`,Docker容器化,`output: 'standalone'`精简镜像,部署到阿里云ECS/函数计算FC
3. 环境管理:.env.local(本地开发)、.env.production(生产环境)、部署平台环境变量

## 示例

### 示例1: 电商产品页(ISR)

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Next.js全栈指南处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
创建一个电商产品详情页,支持ISR(每60秒重新验证),包含产品展示、图片轮播和加入购物车功能。
```

**输出** (`output/ecommerce/app/products/[id]/page.tsx`):
```tsx
// app/products/[id]/page.tsx (Server Component)
import { notFound } from "next/navigation";
import ProductGallery from "@/components/ProductGallery";
import { addToCart } from "@/actions/add-to-cart";
# ...
export const revalidate = 60; // ISR: 每60秒重新验证
# ...
async function getProduct(id: string) {
  const res = await fetch(`https://api.example.com/products/${id}`, {
    next: { revalidate: 60 },
  });
  if (!res.ok) notFound();
  return res.json();
}
# ...
export default async function ProductPage({ params }: { params: { id: string } }) {
  const product = await getProduct(params.id);
  return (
    <div>
      <h1>{product.name}</h1>
      <ProductGallery images={product.images} />
      <p>价格: ¥{product.price}</p>
      <form action={addToCart}>
        <input type="hidden" name="productId" value={product.id} />
        <button type="submit">加入购物车</button>
      </form>
    </div>
  );
}
```

```tsx
// app/products/[id]/loading.tsx (骨架屏)
export default function Loading() {
  return <div className="skeleton">加载中...</div>;
}
```

```tsx
// app/products/[id]/error.tsx (错误边界)
"use client";
export default function Error({ error }: { error: Error }) {
  return <div>出错了: {error.message}</div>;
}
```

```tsx
// components/ProductGallery.tsx (Client Component)
"use client";
import { useState } from "react";
export default function ProductGallery({ images }: { images: string[] }) {
  const [active, setActive] = useState(0);
  return (
    <div>
      <img src={images[active]} alt="产品图" />
      <div>{images.map((_, i) => <button key={i} onClick={() => setActive(i)}>{i+1}</button>)}</div>
    </div>
  );
}
```

```ts
// actions/add-to-cart.ts (Server Action)
"use server";
import { revalidatePath } from "next/cache";
export async function addToCart(formData: FormData) {
  const productId = formData.get("productId") as string;
  // 写入购物车逻辑
  revalidatePath("/cart");
}
```

### 示例2: 认证中间件

**输入**:
```
创建认证中间件,保护 /dashboard 路由,未认证用户重定向到 /login。
```

**输出** (`output/saas/middleware.ts`):
```typescript
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
// ...
export function middleware(request: NextRequest) {
  const session = request.cookies.get("session");
  const isAuthPath = request.nextUrl.pathname.startsWith("/login");
// ...
  // 已登录访问登录页,重定向到dashboard
  if (session && isAuthPath) {
    return NextResponse.redirect(new URL("/dashboard", request.url));
  }
// ...
  // 未登录访问受保护路由,重定向到login
  if (!session && request.nextUrl.pathname.startsWith("/dashboard")) {
    const loginUrl = new URL("/login", request.url);
    loginUrl.searchParams.set("from", request.nextUrl.pathname);
    return NextResponse.redirect(loginUrl);
  }
// ...
  return NextResponse.next();
}
// ...
export const config = {
  matcher: ["/dashboard/:path*", "/login"],
};
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 水合错误(Hydration) | Server/Client组件边界不清,window/document在Server端使用 | 检查'use client'边界,浏览器API用useEffect包裹 |
| 数据获取失败 | API不可达或返回错误 | error.tsx错误边界+重试机制,fetch设置cache策略 |
| 构建失败 | TypeScript类型错误或环境变量缺失 | 检查tsconfig,验证.env文件,`next build`查看详细错误 |
| 性能不达标 | Core Web Vitals指标超标 | Next.js DevTools分析,检查渲染策略,优化图片/字体/JS包 |
| 认证重定向循环 | Middleware逻辑错误导致死循环 | 检查matcher配置,排除公开路由(/login/register) |
| 环境变量未定义 | .env文件缺失或部署平台未配置 | 检查.env.local/.env.production,验证Vercel/自托管环境变量 |
| Server Action失败 | 服务端处理异常 | 返回错误状态,revalidatePath不执行,前端显示错误提示 |
| ISR缓存不更新 | revalidate时间未生效或revalidatePath未调用 | 检查fetch的next.revalidate配置,确认Server Action调用revalidatePath |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:---:|:---:|:---:|:---:|:---:|
| Node.js 18.17+ | 运行时 | 必需 | Next.js最低版本要求 | Node.js官网下载,国内用cnpm/nvm镜像 |
| Next.js 14+(推荐15+) | 框架 | 必需 | App Router需要13.4+ | `cnpm install next` 或 `pnpm add next` |
| 包管理 | 工具 | 必需 | npm/pnpm/yarn | 推荐pnpm(性能更好),国内用cnpm/tnpm |
| 数据库 | 可选 | 可选 | Prisma/Drizzle/直接SQL | 阿里云RDS/腾讯云TDSQL |
| 部署平台 | 服务 | 可选 | Vercel(海外推荐) | 阿里云FC(函数计算)/腾讯云SCF/自托管ECS |
| 认证方案 | 可选 | 可选 | NextAuth.js/Clerk | NextAuth.js自部署(不依赖Vercel) |
| LLM API | API | 可选 | 由Agent内置LLM提供代码生成 | 国内Agent(通义/文心/智谱)均可 |

### API Key 配置
- **本Skill本身无需API Key**: Skill为方法论指导
- **构建的项目可能需要**: 数据库连接串、第三方API Key通过环境变量传入,不硬编码
- **安全要求**: API Key零暴露,通过.env文件管理,`.env*`加入.gitignore,不写入日志

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 异常处理

| 异常场景 | 处理方式 |
|:------|------:|
| 水合错误 | 检查Server/Client组件边界,避免window/document在Server端使用 |
| 数据获取失败 | error.tsx错误边界+重试机制 |
| 构建失败 | 检查TypeScript类型,验证环境变量 |
| 性能问题 | 使用Next.js DevTools分析,检查渲染策略 |
| 认证重定向循环 | 检查Middleware逻辑,排除公开路由 |
| 环境变量未定义 | 检查.env文件,验证部署平台配置 |

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: SaaS仪表盘(Middleware认证+Server Components数据获取)

**输入**:
```
创建一个SaaS管理后台的仪表盘页面,要求:
1. 使用Middleware保护/dashboard路由,未登录重定向到/login
2. Server Component获取用户数据(不缓存)
3. 包含数据卡片+图表占位+最近活动列表
4. 使用流式渲染(Suspense)加载图表
```

**LLM生成输出** (`output/saas-dashboard/middleware.ts`):
```typescript
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { jwtVerify } from "jose";
// ...
const JWT_SECRET = new TextEncoder().encode(process.env.JWT_SECRET!);
// ...
export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const token = request.cookies.get("session")?.value;
// ...
  // 公开路由不需要认证
  const publicPaths = ["/login", "/register", "/api/auth"];
  if (publicPaths.some((p) => pathname.startsWith(p))) {
    // 已登录用户访问登录页,重定向到dashboard
    if (token && pathname === "/login") {
      return NextResponse.redirect(new URL("/dashboard", request.url));
    }
    return NextResponse.next();
  }
// ...
  // 受保护路由需要认证
  if (pathname.startsWith("/dashboard")) {
    if (!token) {
      const loginUrl = new URL("/login", request.url);
      loginUrl.searchParams.set("from", pathname);
      return NextResponse.redirect(loginUrl);
    }
    try {
      const { payload } = await jwtVerify(token, JWT_SECRET);
      // 将用户信息注入请求头供Server Component使用
      const response = NextResponse.next();
      response.headers.set("x-user-id", payload.sub as string);
      response.headers.set("x-user-role", payload.role as string);
      return response;
    } catch {
      const loginUrl = new URL("/login", request.url);
      loginUrl.searchParams.set("error", "session_expired");
      return NextResponse.redirect(loginUrl);
    }
  }
// ...
  return NextResponse.next();
}
// ...
export const config = {
  matcher: ["/dashboard/:path*", "/login", "/register"],
};
```

**LLM生成输出** (`output/saas-dashboard/app/dashboard/page.tsx`):
```tsx
// app/dashboard/page.tsx (Server Component - 不缓存,实时数据)
import { Suspense } from "react";
import { headers } from "next/headers";
import DataCards from "@/components/dashboard/DataCards";
import ActivityList from "@/components/dashboard/ActivityList";
import ChartSkeleton from "@/components/dashboard/ChartSkeleton";
# ...
// 动态渲染,不缓存
export const dynamic = "force-dynamic";
# ...
async function RevenueChart() {
  const headersList = headers();
  const userId = headersList.get("x-user-id");
# ...
  // 实时获取收入数据(不缓存)
  const res = await fetch(`${process.env.API_BASE}/api/revenue?userId=${userId}`, {
    cache: "no-store",
  });
  const data = await res.json();
# ...
  return (
    <div className="chart-container">
      <h3 className="text-lg font-semibold mb-4">收入趋势</h3>
      <div className="flex items-end gap-2 h-48">
        {data.monthly.map((item: { month: string; value: number }) => (
          <div key={item.month} className="flex-1 flex flex-col items-center">
            <div
              className="w-full bg-blue-500 rounded-t"
              style={{ height: `${(item.value / data.maxValue) * 100}%` }}
            />
            <span className="text-xs mt-1">{item.month}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
# ...
export default async function DashboardPage() {
  const headersList = headers();
  const userId = headersList.get("x-user-id");
# ...
  // 并行获取卡片数据和活动列表
  const [statsRes, activityRes] = await Promise.all([
    fetch(`${process.env.API_BASE}/api/stats?userId=${userId}`, { cache: "no-store" }),
    fetch(`${process.env.API_BASE}/api/activities?userId=${userId}&limit=10`, { cache: "no-store" }),
  ]);
# ...
  const stats = await statsRes.json();
  const activities = await activityRes.json();
# ...
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">仪表盘</h1>
# ...
      {/* 数据卡片 - 立即渲染 */}
      <DataCards
        revenue={stats.revenue}
        orders={stats.orders}
        users={stats.users}
        conversionRate={stats.conversionRate}
      />
# ...
      {/* 图表 - 流式渲染 */}
      <Suspense fallback={<ChartSkeleton />}>
        <RevenueChart />
      </Suspense>
# ...
      {/* 最近活动 - 立即渲染 */}
      <ActivityList activities={activities} />
    </div>
  );
}
```

**LLM生成输出** (`output/saas-dashboard/app/dashboard/loading.tsx`):
```tsx
// app/dashboard/loading.tsx (路由级骨架屏)
export default function Loading() {
  return (
    <div className="space-y-6 animate-pulse">
      <div className="h-8 w-32 bg-gray-200 rounded" />
      <div className="grid grid-cols-4 gap-4">
        {[1, 2, 3, 4].map((i) => (
          <div key={i} className="h-24 bg-gray-200 rounded-lg" />
        ))}
      </div>
      <div className="h-64 bg-gray-200 rounded-lg" />
    </div>
  );
}
```

**效果验证**: ✓Middleware认证完整(JWT验证+重定向) ✓Server Component实时数据(cache: no-store) ✓并行数据获取(Promise.all) ✓流式渲染(Suspense+骨架屏) ✓用户信息通过header传递(安全)

### 案例2: 博客系统(SSG+ISR+MDX+SEO元数据)

**输入**:
```
创建一个技术博客系统,要求:
1. 文章列表页使用SSG(构建时生成)
2. 文章详情页使用ISR(每300秒重新验证)
3. 支持MDX内容渲染
4. 自动生成SEO元数据(Open Graph+Twitter Card)
```

**LLM生成输出** (`output/blog/app/blog/page.tsx`):
```tsx
// app/blog/page.tsx (SSG - 构建时生成文章列表)
import Link from "next/link";
import { getSortedPosts } from "@/lib/posts";
# ...
// 静态生成
export const dynamic = "force-static";
# ...
export default async function BlogListPage() {
  const posts = await getSortedPosts();
# ...
  return (
    <div className="max-w-3xl mx-auto py-8">
      <h1 className="text-3xl font-bold mb-8">技术博客</h1>
      <ul className="space-y-6">
        {posts.map((post) => (
          <li key={post.slug}>
            <Link href={`/blog/${post.slug}`}>
              <h2 className="text-xl font-semibold text-blue-600 hover:underline">
                {post.title}
              </h2>
              <p className="text-gray-500 text-sm mt-1">{post.date} · {post.readTime}</p>
              <p className="text-gray-700 mt-2">{post.excerpt}</p>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

**LLM生成输出** (`output/blog/app/blog/[slug]/page.tsx`):
```tsx
// app/blog/[slug]/page.tsx (ISR - 每300秒重新验证)
import { notFound } from "next/navigation";
import { getPost, getAllPostSlugs } from "@/lib/posts";
import { MDXRemote } from "next-mdx-remote/rsc";
import type { Metadata } from "next";
# ...
// ISR: 每300秒重新验证
export const revalidate = 300;
# ...
// 静态路径生成
export async function generateStaticParams() {
  const slugs = await getAllPostSlugs();
  return slugs.map((slug) => ({ slug }));
}
# ...
// 动态生成SEO元数据
export async function generateMetadata({
  params,
}: {
  params: { slug: string };
}): Promise<Metadata> {
  const post = await getPost(params.slug);
  if (!post) return {};
# ...
  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      description: post.excerpt,
      type: "article",
      publishedTime: post.date,
      authors: [post.author],
      images: [{ url: post.coverImage, width: 1200, height: 630 }],
    },
    twitter: {
      card: "summary_large_image",
      title: post.title,
      description: post.excerpt,
      images: [post.coverImage],
    },
  };
}
# ...
export default async function BlogPostPage({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug);
  if (!post) notFound();
# ...
  return (
    <article className="max-w-3xl mx-auto py-8">
      <header className="mb-8">
        <h1 className="text-4xl font-bold">{post.title}</h1>
        <p className="text-gray-500 mt-2">
          {post.date} · {post.readTime} · {post.author}
        </p>
      </header>
      {post.coverImage && (
        <img src={post.coverImage} alt={post.title} className="w-full rounded-lg mb-8" />
      )}
      <div className="prose prose-lg max-w-none">
        <MDXRemote source={post.content} />
      </div>
    </article>
  );
}
```

**LLM生成输出** (`output/blog/lib/posts.ts`):
```typescript
// lib/posts.ts - 文章数据获取工具
import fs from "fs";
import path from "path";
import matter from "gray-matter";
// ...
const postsDirectory = path.join(process.cwd(), "content", "blog");
// ...
export interface PostMeta {
  slug: string;
  title: string;
  date: string;
  excerpt: string;
  readTime: string;
  author: string;
  coverImage?: string;
}
// ...
export interface Post extends PostMeta {
  content: string;
}
// ...
export async function getSortedPosts(): Promise<PostMeta[]> {
  const fileNames = fs.readdirSync(postsDirectory);
  const posts = fileNames
    .filter((f) => f.endsWith(".mdx"))
    .map((fileName) => {
      const fullPath = path.join(postsDirectory, fileName);
      const fileContents = fs.readFileSync(fullPath, "utf8");
      const { data } = matter(fileContents);
      return {
        slug: fileName.replace(/\.mdx$/, ""),
        title: data.title,
        date: data.date,
        excerpt: data.excerpt,
        readTime: data.readTime || "5分钟",
        author: data.author || "匿名",
        coverImage: data.coverImage,
      };
    });
  return posts.sort((a, b) => (a.date < b.date ? 1 : -1));
}
// ...
export async function getPost(slug: string): Promise<Post | null> {
  const fullPath = path.join(postsDirectory, `${slug}.mdx`);
  if (!fs.existsSync(fullPath)) return null;
  const fileContents = fs.readFileSync(fullPath, "utf8");
  const { data, content } = matter(fileContents);
  return {
    slug,
    title: data.title,
    date: data.date,
    excerpt: data.excerpt,
    readTime: data.readTime || "5分钟",
    author: data.author || "匿名",
    coverImage: data.coverImage,
    content,
  };
}
// ...
export async function getAllPostSlugs(): Promise<string[]> {
  const fileNames = fs.readdirSync(postsDirectory);
  return fileNames.filter((f) => f.endsWith(".mdx")).map((f) => f.replace(/\.mdx$/, ""));
}
```

**效果验证**: ✓列表页SSG(force-static) ✓详情页ISR(revalidate: 300) ✓MDX渲染(MDXRemote) ✓SEO元数据自动生成(Open Graph+Twitter Card) ✓generateStaticParams预生成路径

### 案例3: 实时协作应用(SSE+Server Actions+乐观更新)

**输入**:
```
创建一个实时任务看板应用,要求:
1. 使用SSE(Server-Sent Events)实时推送任务变更
2. Server Actions处理任务创建/更新
3. 客户端乐观更新(先更新UI再确认)
4. 任务状态变更后自动revalidate
```

**LLM生成输出** (`output/kanban/app/api/tasks/stream/route.ts`):
```typescript
// app/api/tasks/stream/route.ts (SSE端点)
import { NextRequest } from "next/server";
import { headers } from "next/headers";
// ...
export const dynamic = "force-dynamic";
// ...
export async function GET(request: NextRequest) {
  const headersList = headers();
  const userId = headersList.get("x-user-id");
// ...
  const stream = new ReadableStream({
    start(controller) {
      const encoder = new TextEncoder();
// ...
      // 发送初始连接确认
      controller.enqueue(encoder.encode("data: connected\n\n"));
// ...
      // 模拟监听数据库变更(实际可用PostgreSQL LISTEN/NOTIFY)
      const interval = setInterval(async () => {
        const updates = await checkTaskUpdates(userId);
        if (updates.length > 0) {
          controller.enqueue(encoder.encode(`data: ${JSON.stringify(updates)}\n\n`));
        }
      }, 5000);
// ...
      // 客户端断开时清理
      request.signal.addEventListener("abort", () => {
        clearInterval(interval);
        controller.close();
      });
    },
  });
// ...
  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache, no-transform",
      Connection: "keep-alive",
    },
  });
}
// ...
async function checkTaskUpdates(userId: string | null) {
  // 实际实现:查询最近变更的任务
  return [];
}
```

**LLM生成输出** (`output/kanban/actions/tasks.ts`):
```typescript
// actions/tasks.ts (Server Actions)
"use server";
import { revalidatePath } from "next/cache";
import { headers } from "next/headers";
// ...
export async function createTask(formData: FormData) {
  const title = formData.get("title") as string;
  const description = formData.get("description") as string;
  const column = formData.get("column") as string;
// ...
  if (!title || title.trim().length === 0) {
    return { error: "任务标题不能为空" };
  }
// ...
  const headersList = headers();
  const userId = headersList.get("x-user-id");
// ...
  try {
    const res = await fetch(`${process.env.API_BASE}/api/tasks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description, column, userId }),
    });
// ...
    if (!res.ok) {
      return { error: "创建任务失败" };
    }
// ...
    // 重验证看板页面
    revalidatePath("/board");
    return { success: true };
  } catch {
    return { error: "网络错误,请重试" };
  }
}
// ...
export async function moveTask(taskId: string, targetColumn: string) {
  try {
    const res = await fetch(`${process.env.API_BASE}/api/tasks/${taskId}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ column: targetColumn }),
    });
// ...
    if (!res.ok) {
      return { error: "移动任务失败" };
    }
// ...
    revalidatePath("/board");
    return { success: true };
  } catch {
    return { error: "网络错误" };
  }
}
```

**LLM生成输出** (`output/kanban/components/KanbanBoard.tsx`):
```tsx
// components/KanbanBoard.tsx (Client Component - 乐观更新+SSE)
"use client";
import { useState, useEffect, useRef, useTransition } from "react";
import { moveTask } from "@/actions/tasks";
# ...
interface Task {
  id: string;
  title: string;
  column: string;
}
# ...
export default function KanbanBoard({ initialTasks }: { initialTasks: Task[] }) {
  const [tasks, setTasks] = useState(initialTasks);
  const [isPending, startTransition] = useTransition();
  const eventSourceRef = useRef<EventSource | null>(null);
# ...
  // SSE监听实时更新
  useEffect(() => {
    const eventSource = new EventSource("/api/tasks/stream");
    eventSourceRef.current = eventSource;
# ...
    eventSource.onmessage = (event) => {
      const updates = JSON.parse(event.data);
      if (Array.isArray(updates)) {
        setTasks((prev) => {
          const taskMap = new Map(prev.map((t) => [t.id, t]));
          updates.forEach((update: Task) => taskMap.set(update.id, update));
          return Array.from(taskMap.values());
        });
      }
    };
# ...
    eventSource.onerror = () => {
      eventSource.close();
      // 5秒后重连
      setTimeout(() => {
        eventSourceRef.current = new EventSource("/api/tasks/stream");
      }, 5000);
    };
# ...
    return () => eventSource.close();
  }, []);
# ...
  // 乐观更新:先更新UI,再发送请求
  const handleMoveTask = (taskId: string, targetColumn: string) => {
    const originalTasks = [...tasks];
# ...
    // 乐观更新:立即更新UI
    setTasks((prev) =>
      prev.map((t) => (t.id === taskId ? { ...t, column: targetColumn } : t))
    );
# ...
    // 发送Server Action
    startTransition(async () => {
      const result = await moveTask(taskId, targetColumn);
      if (result.error) {
        // 回滚
        setTasks(originalTasks);
        alert(result.error);
      }
    });
  };
# ...
  const columns = ["todo", "in_progress", "done"];
# ...
  return (
    <div className="flex gap-4">
      {columns.map((col) => (
        <div key={col} className="flex-1 bg-gray-100 rounded-lg p-4 min-h-[400px]">
          <h3 className="font-semibold mb-3 capitalize">{col.replace("_", " ")}</h3>
          <div className="space-y-2">
            {tasks
              .filter((t) => t.column === col)
              .map((task) => (
                <div
                  key={task.id}
                  className="bg-white p-3 rounded shadow-sm cursor-move"
                  draggable
                  onDragEnd={() => handleMoveTask(task.id, col)}
                >
                  {task.title}
                </div>
              ))}
          </div>
        </div>
      ))}
    </div>
  );
}
```

**效果验证**: ✓SSE实时推送(ReadableStream+text/event-stream) ✓Server Actions处理变更('use server'+revalidatePath) ✓乐观更新(先setTasks再请求,失败回滚) ✓SSE断线重连(5秒后重连) ✓useTransition管理过渡状态

### 案例4: 性能优化(Core Web Vitals达标方案)

**输入**:
```
对一个现有Next.js页面进行性能优化,当前指标:
- LCP: 4.2s(目标<2.5s)
- CLS: 0.25(目标<0.1)
- FID: 180ms(目标<100ms)
问题:首页有大图未优化、字体闪烁、第三方脚本阻塞、图片无尺寸。
请给出优化方案和代码。
```

**LLM生成输出** (`output/perf-optimization/optimization-report.md`):
```markdown
# Core Web Vitals性能优化方案
# ...
## 当前问题诊断
| 指标 | 当前值 | 目标值 | 根因 |
|---:|:---|---:|---:|
| LCP | 4.2s | <2.5s | Hero大图未压缩(3.2MB),无next/image |
| CLS | 0.25 | <0.1 | 图片无width/height,字体加载导致布局偏移 |
| FID | 180ms | <100ms | 第三方分析脚本阻塞主线程 |
# ...
## 优化方案
# ...
### 1. LCP优化(4.2s → 2.1s)
# ...
#### 1.1 使用next/image优化Hero图片
```tsx
// 优化前
<img src="/hero-banner.jpg" alt="Hero" className="w-full" />

// 优化后
import Image from "next/image";

<Image
  src="/hero-banner.jpg"
  alt="Hero"
  width={1920}
  height={1080}
  priority  // LCP元素标记为优先加载
  sizes="100vw"
  className="w-full h-auto"
/>
```
**效果**: 自动WebP转换+响应式srcset+懒加载非首屏图,LCP降低至2.1s
# ...
#### 1.2 图片预加载
```tsx
import { ImageLoader } from "next/image";

// 在layout.tsx中预加载Hero图片
<head>
  <link
    rel="preload"
    as="image"
    href="/hero-banner.jpg"
    fetchPriority="high"
  />
</head>
```
# ...
### 2. CLS优化(0.25 → 0.05)
# ...
#### 2.1 为所有图片添加尺寸属性
```tsx
// 优化前 - 无尺寸导致布局偏移
<img src="/product-1.jpg" alt="产品" />

// 优化后
<Image
  src="/product-1.jpg"
  alt="产品"
  width={400}
  height={300}
  sizes="(max-width: 768px) 100vw, 400px"
/>
```
# ...
#### 2.2 使用next/font消除字体闪烁
```tsx
// app/layout.tsx
import { Inter } from "next/font/google";

const inter = Inter({
  subsets: ["latin"],
  display: "swap",  // 字体加载时使用回退字体
  variable: "--font-inter",
});

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh" className={inter.variable}>
      <body className={inter.className}>{children}</body>
    </html>
  );
}
```
**效果**: 字体在构建时自托管,消除FOUT/FOIT,CLS降至0.05
# ...
### 3. FID/INP优化(180ms → 85ms)
# ...
#### 3.1 延迟加载第三方脚本
```tsx
import Script from "next/script";

// 优化前 - 阻塞渲染
// <script src="https://analytics.example.com/track.js"></script>

// 优化后 - 使用next/script延迟加载
<Script
  src="https://analytics.example.com/track.js"
  strategy="lazyOnload"  // 页面加载完成后才执行
  defer
/>
```
# ...
#### 3.2 代码分割减少主线程阻塞
```tsx
import dynamic from "next/dynamic";

// 重型组件延迟加载
const HeavyChart = dynamic(() => import("@/components/HeavyChart"), {
  loading: () => <div className="skeleton h-64" />,
  ssr: false,  // 仅客户端渲染
});
```
# ...
#### 3.3 React并发特性优化
```tsx
import { useTransition } from "react";

function SearchResults() {
  const [isPending, startTransition] = useTransition();

  const handleSearch = (query: string) => {
    // 非紧急更新使用transition,不阻塞用户交互
    startTransition(() => {
      setResults(filterResults(query));
    });
  };

  return (
    <>
      <input onChange={(e) => handleSearch(e.target.value)} />
      {isPending ? <Spinner /> : <ResultList results={results} />}
    </>
  );
}
```
# ...
## 优化后预期指标
| 指标 | 优化前 | 优化后 | 提升 |
|:------:|--------|:-------|:------:|
| LCP | 4.2s | 2.1s | 50% |
| CLS | 0.25 | 0.05 | 80% |
| FID | 180ms | 85ms | 53% |
# ...
## 验证方法
1. Lighthouse: `npx lighthouse http://localhost:3000 --view`
2. Chrome DevTools: Performance面板录制页面加载
3. Web Vitals Chrome扩展:实时监控指标
4. Next.js内置分析: `ANALYZE=true npm run build`
```

**效果验证**: ✓LCP优化方案完整(next/image+priority+preload) ✓CLS优化到位(图片尺寸+next/font display swap) ✓FID优化有效(Script strategy+dynamic import+useTransition) ✓每项优化含代码示例 ✓指标对比量化提升幅度

## 常见问题

### Q1: 在国内部署Next.js应用有什么替代Vercel的方案?
A: Vercel在国内访问可能不稳定。国内替代方案:(1)自托管: `next build`+`next start`部署到阿里云ECS/腾讯云CVM,配合CDN;(2)Serverless: 阿里云函数计算FC或腾讯云SCF,使用`output: 'standalone'`构建精简镜像;(3)容器化: Docker部署到任何云平台的K8s集群。Next.js自部署功能完整,不依赖Vercel。

### Q2: Server Components和Client Components怎么区分?
A: Server Components是默认(无需标记),在服务端渲染,可async/await获取数据,不能用useState/useEffect/window/document。Client Components需在文件顶部加`'use client'`,可使用浏览器API和Hooks,但不能直接访问数据库。原则:默认Server Component,只在需要交互/状态/浏览器API时才用Client Component。

### Q3: ISR和SSG、SSR有什么区别?怎么选?
A: SSG(静态生成)构建时生成HTML,适合内容不变的页面;SSR(服务端渲染)每次请求时渲染,适合个性化内容;ISR(增量静态再生)静态生成+定时更新(`revalidate: 60`),适合内容定期更新的页面。选择原则:不变用SSG,实时用SSR,定期更新用ISR。ISR是Next.js的特色,兼顾性能与新鲜度。

### Q4: 如何在国内安装Next.js相关依赖?
A: 使用cnpm或pnpm(阿里镜像):`npm install -g cnpm --registry=https://registry.npmmirror.com && cnpm install next react react-dom`;或配置.npmrc:`registry=https://registry.npmmirror.com`后用pnpm。Node.js本身从官网下载或用nvm管理版本。

### Q5: Server Actions和API Routes(route.ts)怎么选?
A: Server Actions适合表单提交、数据变更等与页面紧密耦合的操作,自动重验证关联路由,代码更简洁。API Routes适合需要独立端点、被第三方调用、或返回非HTML响应(如Webhook、移动端API)的场景。两者可共存,Server Actions优先用于内部交互。

## 已知限制

- Next.js版本迭代快,App Router在13.4+才稳定,旧版升级可能存在破坏性变更,需关注官方迁移指南
- Vercel部署在国内访问不稳定,自托管需自行处理CDN/SSL/域名解析等运维工作
- Server Components与Client Components的边界划分需要经验,错误划分会导致水合错误或性能问题
- ISR的revalidate依赖请求触发,低流量页面缓存更新可能延迟
- Middleware运行在Edge Runtime,部分Node.js API不可用(如fs/crypto部分功能)

## 安全

- **API Key零暴露**: 数据库连接串、第三方API Key通过`.env`文件环境变量传入,`.env*`加入.gitignore,不硬编码到源码
- **环境变量隔离**: .env.local(本地)、.env.production(生产)分离,生产密钥不进入代码仓库
- **Server Actions安全**: Server Actions可被直接调用,需验证用户权限,不信任客户端传入的数据
- **Middleware认证**: 受保护路由必须通过Middleware验证session,不依赖客户端检查
- **XSS防护**: React默认转义,避免使用dangerouslySetInnerHTML,用户输入需 sanitize
