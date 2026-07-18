---
slug: javascript-toolkit-pro
name: javascript-toolkit-pro
version: "1.0.0"
displayName: JavaScript工具包专业版
summary: 企业级 JavaScript 开发方案，含性能优化、模块化架构、测试策略与构建工具链。
license: MIT
edition: pro
description: |-
  面向企业级 JavaScript 开发团队的专业工具包，提供性能优化与工程化能力。

  核心能力:
  - 性能优化（内存管理、渲染优化、懒加载、防抖节流）
  - 模块化架构设计（ESM、动态导入、微前端）
  - 测试策略（单元测试、集成测试、E2E 测试）
  - 构建工具链集成（Vite、Webpack、esbuild）
  - TypeScript 迁移与类型安全增强
  - 代码分割与按需加载策略

  适用场景:
  - 高性能前端应用的架构与优化
  - 大型项目的模块化拆分与管理
  - 企业级测试体系建设
  - TypeScript 渐进式迁移

  差异化: 专业版兼容免费版所有陷阱防范能力，额外提供性能优化、模块化架构、测试策略、构建工具链集成，支持企业级前端开发。

  触发关键词: js性能优化, 模块化架构, esm动态导入, 微前端, 单元测试, e2e测试, vite配置, webpack优化, typescript迁移, 代码分割, 懒加载
tags:
- 开发工具
- JavaScript
- 性能优化
- 企业开发
- 前端架构
tools:
- read
- exec
---

# JavaScript 工具包（专业版）

## 概述

本工具面向企业级 JavaScript 开发团队，提供性能优化、模块化架构、测试策略与构建工具链集成方案。在免费版陷阱防范能力之上，专业版新增内存管理与渲染优化、ESM 模块化与动态导入、微前端架构、单元/集成/E2E 测试体系、Vite/Webpack 构建优化、TypeScript 渐进式迁移等能力。通过工程化的工具链与最佳实践，帮助团队构建高性能、可维护的前端应用。

**版本兼容性说明**：专业版完全兼容免费版（`javascript-toolkit-free`）的所有陷阱防范与最佳实践，可无缝升级。

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
| --- | --- | --- |
| 陷阱防范 | 相等性/this/闭包/异步 | 生产级陷阱检测脚本 |
| 性能优化 | - | 内存/渲染/懒加载/防抖节流 |
| 模块化 | - | ESM/动态导入/微前端 |
| 测试 | - | 单元/集成/E2E 体系 |
| 构建工具 | - | Vite/Webpack/esbuild |
| 类型安全 | - | TypeScript 迁移与增强 |
| 代码分割 | - | 路由级/组件级分割 |
| 状态管理 | - | 状态管理方案选型 |

## 使用场景

### 场景一：性能优化方案

应用首屏加载缓慢，需要进行性能优化。

```javascript
// 1. 路由级懒加载（代码分割）
import { lazy, Suspense } from 'react';

const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));

function App() {
    return (
        <Suspense fallback={<Loading />}>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
            </Routes>
        </Suspense>
    );
}

// 2. 组件级懒加载
const HeavyChart = lazy(() => import('./components/HeavyChart'));

// 3. 动态导入（按需加载）
async function loadModule() {
    if (needFeature) {
        const module = await import('./features/advanced');
        module.init();
    }
}

// 4. 防抖（Debounce）
function debounce(fn, delay) {
    let timer = null;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), delay);
    };
}

// 使用：搜索输入防抖
const handleSearch = debounce((query) => {
    fetchResults(query);
}, 300);

// 5. 节流（Throttle）
function throttle(fn, interval) {
    let lastTime = 0;
    return function(...args) {
        const now = Date.now();
        if (now - lastTime >= interval) {
            fn.apply(this, args);
            lastTime = now;
        }
    };
}

// 使用：滚动事件节流
const handleScroll = throttle(() => {
    updatePosition();
}, 16);  // 约 60fps

// 6. 虚拟列表（大数据量渲染）
class VirtualList {
    constructor(container, items, itemHeight, visibleCount) {
        this.container = container;
        this.items = items;
        this.itemHeight = itemHeight;
        this.visibleCount = visibleCount;
        this.startIndex = 0;
        this.init();
    }
    
    init() {
        this.container.style.height = `${this.visibleCount * this.itemHeight}px`;
        this.container.style.overflow = 'auto';
        this.container.addEventListener('scroll', this.onScroll.bind(this));
        this.render();
    }
    
    onScroll() {
        const scrollTop = this.container.scrollTop;
        this.startIndex = Math.floor(scrollTop / this.itemHeight);
        this.render();
    }
    
    render() {
        const visibleItems = this.items.slice(
            this.startIndex,
            this.startIndex + this.visibleCount
        );
        const offset = this.startIndex * this.itemHeight;
        
        this.container.innerHTML = `
            <div style="height: ${this.items.length * this.itemHeight}px; position: relative;">
                <div style="transform: translateY(${offset}px);">
                    ${visibleItems.map(item => 
                        `<div style="height: ${this.itemHeight}px;">${item}</div>`
                    ).join('')}
                </div>
            </div>
        `;
    }
}
```

### 场景二：微前端架构

大型应用需要拆分为多个独立子应用。

```javascript
// 微前端主应用配置
const microApps = [
    {
        name: 'dashboard',
        entry: 'https://dashboard.example.com',
        container: '#sub-app',
        activeRule: '/dashboard',
    },
    {
        name: 'settings',
        entry: 'https://settings.example.com',
        container: '#sub-app',
        activeRule: '/settings',
    },
];

// 使用 qiankun 微前端框架
import { registerMicroApps, start } from 'qiankun';

registerMicroApps(microApps, {
    beforeLoad: [(app) => {
        console.log(`加载子应用: ${app.name}`);
        return Promise.resolve();
    }],
    beforeMount: [(app) => {
        console.log(`挂载子应用: ${app.name}`);
        return Promise.resolve();
    }],
    afterUnmount: [(app) => {
        console.log(`卸载子应用: ${app.name}`);
        return Promise.resolve();
    }],
});

start({
    prefetch: true,           // 预加载
    sandbox: {
        strictStyleIsolation: false,  // 样式隔离
        experimentalStyleIsolation: true,
    },
});

// 子应用入口配置
export async function bootstrap() {
    console.log('子应用启动');
}

export async function mount(props) {
    console.log('子应用挂载', props);
    render(props);
}

export async function unmount(props) {
    console.log('子应用卸载');
    // 清理副作用
    props.container.innerHTML = '';
}
```

### 场景三：测试体系建设

项目需要建立完整的测试体系。

```javascript
// 1. 单元测试（Vitest/Jest）
import { describe, it, expect, vi } from 'vitest';
import { UserService } from './UserService';

describe('UserService', () => {
    it('应该正确获取用户信息', async () => {
        // Mock 依赖
        const mockRepo = {
            findById: vi.fn().mockResolvedValue({ id: 1, name: '张三' }),
        };
        const service = new UserService(mockRepo);
        
        const user = await service.getUser(1);
        
        expect(user).toEqual({ id: 1, name: '张三' });
        expect(mockRepo.findById).toHaveBeenCalledWith(1);
    });
    
    it('用户不存在时应抛出异常', async () => {
        const mockRepo = {
            findById: vi.fn().mockResolvedValue(null),
        };
        const service = new UserService(mockRepo);
        
        await expect(service.getUser(999)).rejects.toThrow('用户不存在');
    });
});

// 2. 集成测试
import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import { createServer } from '../server';
import request from 'supertest';

describe('用户 API 集成测试', () => {
    let server;
    
    beforeAll(async () => {
        server = await createServer({ testMode: true });
    });
    
    afterAll(async () => {
        await server.close();
    });
    
    it('GET /api/users/:id 返回用户信息', async () => {
        const res = await request(server).get('/api/users/1');
        
        expect(res.status).toBe(200);
        expect(res.body).toHaveProperty('id', 1);
        expect(res.body).toHaveProperty('name');
    });
});

// 3. E2E 测试（Playwright）
import { test, expect } from '@playwright/test';

test('用户登录流程', async ({ page }) => {
    await page.goto('http://localhost:3000/login');
    
    await page.fill('[data-testid="username"]', 'admin');
    await page.fill('[data-testid="password"]', 'password');
    await page.click('[data-testid="submit"]');
    
    await expect(page).toHaveURL('http://localhost:3000/dashboard');
    await expect(page.locator('[data-testid="welcome"]')).toBeVisible();
});
```

## 快速开始

### Vite 构建配置

```javascript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
    plugins: [react()],
    
    // 代码分割优化
    build: {
        rollupOptions: {
            output: {
                manualChunks: {
                    'react-vendor': ['react', 'react-dom'],
                    'utils-vendor': ['lodash', 'dayjs'],
                    'ui-vendor': ['antd', '@ant-design/icons'],
                },
            },
        },
        // chunk 大小警告阈值
        chunkSizeWarningLimit: 1000,
        // 启用 gzip 压缩
        minify: 'terser',
        terserOptions: {
            compress: {
                drop_console: true,  // 移除 console
                drop_debugger: true,
            },
        },
    },
    
    // 依赖预构建
    optimizeDeps: {
        include: ['react', 'react-dom', 'lodash'],
    },
    
    // 开发服务器代理
    server: {
        proxy: {
            '/api': {
                target: 'http://localhost:8080',
                changeOrigin: true,
            },
        },
    },
    
    // 性能分析
    build: {
        sourcemap: true,
    },
});
```

### TypeScript 渐进式迁移

```typescript
// 1. 允许 JS 和 TS 共存
// tsconfig.json
{
    "compilerOptions": {
        "allowJs": true,           // 允许 JS 文件
        "checkJs": false,          // 暂不检查 JS
        "strict": false,           // 逐步开启
        "noImplicitAny": false,    // 先允许隐式 any
        "strictNullChecks": true,  // 先开空值检查
        "target": "ES2022",
        "module": "ESNext",
        "moduleResolution": "bundler",
        "esModuleInterop": true,
        "skipLibCheck": true,
    },
    "include": ["src/**/*"],
    "exclude": ["node_modules"]
}

// 2. 类型定义文件（.d.ts）
// src/types/global.d.ts
declare module '*.css' {
    const content: Record<string, string>;
    export default content;
}

declare module '*.png' {
    const src: string;
    export default src;
}

// 3. 渐进式类型增强
// 从宽松到严格
type User = {
    id: number;
    name: string;
    email?: string;        // 可选属性
    age: number | null;    // 联合类型
    metadata: unknown;     // 逐步收紧
};

// 4. 泛型工具类型
function apiRequest<T>(url: string): Promise<T> {
    return fetch(url).then(res => res.json());
}

interface UserDTO {
    id: number;
    name: string;
}

const user = await apiRequest<UserDTO>('/api/users/1');
// user 类型为 UserDTO
```

## 配置示例

### 状态管理方案对比

| 方案 | 适用场景 | 优点 | 缺点 |
| --- | --- | --- | --- |
| Context + useReducer | 小型应用 | 内置无依赖 | 性能影响大 |
| Zustand | 中型应用 | 轻量简单 | 功能较少 |
| Redux Toolkit | 大型应用 | 生态完善 | 模板代码多 |
| Pinia | Vue 应用 | 类型安全 | 仅 Vue |
| Jotai | 原子化状态 | 细粒度控制 | 学习曲线 |

```javascript
// Zustand 状态管理示例
import { create } from 'zustand';

const useUserStore = create((set) => ({
    user: null,
    loading: false,
    error: null,
    
    fetchUser: async (id) => {
        set({ loading: true, error: null });
        try {
            const response = await fetch(`/api/users/${id}`);
            const user = await response.json();
            set({ user, loading: false });
        } catch (error) {
            set({ error, loading: false });
        }
    },
    
    logout: () => set({ user: null }),
}));

// 使用
function UserProfile() {
    const { user, loading, fetchUser } = useUserStore();
    
    useEffect(() => {
        fetchUser(1);
    }, []);
    
    if (loading) return <Loading />;
    return <div>{user?.name}</div>;
}
```

### 性能监控配置

```javascript
// 性能监控工具
class PerformanceMonitor {
    constructor() {
        this.metrics = {};
    }
    
    // 测量函数执行时间
    measure(name, fn) {
        return async (...args) => {
            const start = performance.now();
            const result = await fn(...args);
            const duration = performance.now() - start;
            
            this.metrics[name] = this.metrics[name] || [];
            this.metrics[name].push(duration);
            
            if (duration > 100) {
                console.warn(`[性能告警] ${name} 耗时 ${duration}ms`);
            }
            
            return result;
        };
    }
    
    // 上报性能数据
    report() {
        const summary = {};
        for (const [name, times] of Object.entries(this.metrics)) {
            summary[name] = {
                count: times.length,
                avg: times.reduce((a, b) => a + b, 0) / times.length,
                max: Math.max(...times),
                min: Math.min(...times),
            };
        }
        return summary;
    }
}

// Web Vitals 监控
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

function sendToAnalytics(metric) {
    navigator.sendBeacon('/api/analytics', JSON.stringify({
        name: metric.name,
        value: metric.value,
        rating: metric.rating,
    }));
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getFCP(sendToAnalytics);
getLCP(sendToAnalytics);
getTTFB(sendToAnalytics);
```

## 最佳实践

1. **路由级代码分割**：所有路由组件使用懒加载

2. **第三方依赖分割**：vendor chunk 分离频繁更新的业务代码

3. **防抖节流高频事件**：scroll、resize、input 等事件

4. **虚拟列表处理大数据**：超过 100 条的列表用虚拟滚动

5. **图片懒加载**：使用 IntersectionObserver 或 loading="lazy"

6. **Tree Shaking**：使用 ES Module 的命名导入

7. **测试分层覆盖**：单元 > 集成 > E2E

8. **TypeScript 渐进迁移**：先 allowJs 再逐步收紧

## 常见问题

### Q1：如何优化首屏加载？

```javascript
// 1. 路由懒加载
const Home = lazy(() => import('./pages/Home'));

// 2. 预加载关键资源
<link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>

// 3. 图片懒加载
<img src="image.jpg" loading="lazy" alt="..." />

// 4. 代码分割
const { chunk } = await import('lodash-es');

// 5. Service Worker 缓存
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js');
}

// 6. CDN 加速静态资源
```

### Q2：如何选择构建工具？

| 工具 | 优势 | 适用场景 |
| --- | --- | --- |
| Vite | 开发体验极佳，ESM 原生 | 新项目首选 |
| Webpack | 生态最完善，插件丰富 | 遗留项目维护 |
| esbuild | 构建速度极快 | 库打包 |
| Rollup | 输出体积最小 | 库发布 |

### Q3：如何做 Tree Shaking？

```javascript
// 正确：命名导入（可 Tree Shaking）
import { debounce } from 'lodash-es';

// 错误：默认导入整个包
import _ from 'lodash';  // 不会 Tree Shaking

// package.json 配置
{
    "sideEffects": false  // 标记无副作用
}

// 或指定有副作用的文件
{
    "sideEffects": ["*.css", "*.scss"]
}
```

### Q4：如何处理跨域问题？

```javascript
// 开发环境：Vite 代理
server: {
    proxy: {
        '/api': 'http://localhost:8080',
    },
}

// 生产环境：CORS 头
// 服务器端配置
app.use(cors({
    origin: ['https://example.com'],
    credentials: true,
}));

// 或使用 BFF 代理
app.use('/api', createProxyMiddleware({
    target: 'http://backend:8080',
    changeOrigin: true,
}));
```

### Q5：如何实现前端错误监控？

```javascript
// 1. 全局错误捕获
window.addEventListener('error', (event) => {
    reportError({
        type: 'error',
        message: event.message,
        filename: event.filename,
        lineno: event.lineno,
        colno: event.colno,
        stack: event.error?.stack,
    });
});

// 2. Promise 未捕获异常
window.addEventListener('unhandledrejection', (event) => {
    reportError({
        type: 'unhandledrejection',
        reason: event.reason,
    });
});

// 3. React 错误边界
class ErrorBoundary extends React.Component {
    state = { hasError: false };
    
    static getDerivedStateFromError(error) {
        return { hasError: true };
    }
    
    componentDidCatch(error, info) {
        reportError({ error, info });
    }
    
    render() {
        if (this.state.hasError) {
            return <ErrorFallback />;
        }
        return this.props.children;
    }
}
```

### Q6：如何优化打包体积？

```bash
# 分析打包体积
npm install -g webpack-bundle-analyzer
npx webpack-bundle-analyzer dist/stats.json

# Vite 分析
npx vite-bundle-visualizer

# 常见优化手段
# 1. 按需导入 UI 库
import { Button } from 'antd';  // 而非 import { Button } from 'antd/lib/button'

# 2. 替换大体积库
# moment.js → dayjs（280KB → 2KB）
# lodash → lodash-es（支持 Tree Shaking）

# 3. 移除未使用的依赖
npx depcheck

# 4. 压缩配置
build: {
    minify: 'terser',
    terserOptions: {
        compress: { drop_console: true },
    },
}
```

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Node.js 版本**: 建议 18 及以上
- **包管理器**: npm / yarn / pnpm

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node.js | 运行时 | 必需 | nodejs.org 下载 |
| Vite | 构建工具 | 推荐 | `npm install -D vite` |
| Vitest | 测试框架 | 推荐 | `npm install -D vitest` |
| Playwright | E2E 测试 | 可选 | `npm install -D @playwright/test` |
| TypeScript | 类型系统 | 可选 | `npm install -D typescript` |
| web-vitals | 性能监控 | 可选 | `npm install web-vitals` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- 前端代理需要配置后端服务地址
- 错误监控需要配置监控平台 SDK 的密钥

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 提供前端工程化建议，构建与测试需要 Node.js 执行能力
