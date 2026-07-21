# 详细参考 - javascript-toolkit-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (javascript)

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

## 代码示例 (javascript)

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

## 代码示例 (javascript)

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

## 代码示例 (javascript)

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

## 代码示例 (typescript)

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

