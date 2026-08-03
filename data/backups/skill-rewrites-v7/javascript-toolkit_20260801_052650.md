---
slug: javascript-toolkit
name: "javascript-toolkit"
version: 1.0.1
displayName: "JavaScript工具包专业版"
summary: "企业级 JavaScr"
summary_zh: "企业级 JavaScript 开发方案，含性能优化、模块化架构、测试策略与构建工具链。面向企业级 JavaScript 开发团队的专业工具包。Use when 需要代码生成、编程辅助、调试"
license: "MIT"
edition: "pro"
description: |-
  面向企业级 JavaScript 开发团队的专业工具包。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。
tags:
  - 开发工具
  - JavaScript
  - 性能优化
  - 企业开发
  - 前端架构
  - 工具
  - 效率
  - 创意
  - vite
  - typescript
  - true
  - api
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# JavaScript工具包专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
|:-----|:-----|:-----|
| 陷阱防范 | 相等性/this/闭包/异步 | 生产级陷阱检测脚本 |
| 性能优化 | - | 内存/渲染/懒加载/防抖节流 |
| 模块化 | - | ESM/动态导入/微前端 |
| 测试 | - | 单元/集成/E2E 体系 |
| 构建工具 | - | Vite/Webpack/esbuild |
| 类型安全 | - | TypeScript 迁移与增强 |
| 代码分割 | - | 路由级/组件级分割 |
| 状态管理 | - | 状态管理方案选型 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 陷阱防范

针对陷阱防范,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供陷阱防范相关的配置参数、输入数据和处理选项.
**输出**: 返回陷阱防范的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`陷阱防范`的配置文档进行参数调优
### 性能优化

针对性能,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供性能优化相关的配置参数、输入数据和处理选项.
**输出**: 返回性能优化的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`性能优化`的配置文档进行参数调优

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：性能优化方案
应用首屏加载缓慢，需要进行性能优化.
> 详细代码示例已移至 `references/detail.md`

### 场景二：微前端架构
大型应用需要拆分为多个独立子应用.
### 场景三：测试体系建设
项目需要建立完整的测试体系.
## 使用流程

### Vite 构建配置
```javascript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
// ...
export default defineConfig({
    plugins: [react()],
// ...
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
// ...
    // 依赖预构建
    optimizeDeps: {
        include: ['react', 'react-dom', 'lodash'],
    },
// ...
    // 开发服务器代理
    server: {
        proxy: {
            '/api': {
                target: 'http://localhost:8080',
                changeOrigin: true,
            },
        },
    },
// ...
    // 性能分析
    build: {
        sourcemap: true,
    },
});
```

### TypeScript 渐进式迁移

TypeScript 渐进式迁移支持将现有 JavaScript 项目逐步转换为类型安全的 TypeScript 项目。通过配置 `allowJs` 和 `checkJs` 选项，可在不修改现有 `.js` 文件的前提下逐步引入 `.ts` 文件。建议从入口文件开始迁移，优先处理核心模块的类型定义，利用 `// @ts-check` 注释对 JavaScript 文件进行渐进式类型检查.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | 处理的内容输入 |
| mode | string | 否 | 处理模式, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "处理结果",
    "status": "success",
    "metadata": {
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Node.js 版本**: 建议 18 及以上
- **包管理器**: npm / yarn / pnpm

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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

## 案例展示

### 状态管理方案对比
| 方案 | 适用场景 | 优点 | 缺点 |
|---:|:---|---:|---:|
| Context + useReducer | 小型应用 | 内置无依赖 | 性能影响大 |
| Zustand | 中型应用 | 轻量简单 | 功能较少 |
| Redux Toolkit | 大型应用 | 生态完善 | 模板代码多 |
| Pinia | Vue 应用 | 类型安全 | 仅 Vue |
| Jotai | 原子化状态 | 细粒度控制 | 学习曲线 |

```javascript
// Zustand 状态管理示例
import { create } from 'zustand';
// ...
const useUserStore = create((set) => ({
    user: null,
    loading: false,
    error: null,
// ...
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
// ...
    logout: () => set({ user: null }),
}));
// ...
// 使用
function UserProfile() {
    const { user, loading, fetchUser } = useUserStore();
// ...
    useEffect(() => {
        fetchUser(1);
    }, []);
// ...
    if (loading) return <Loading />;
    return <div>{user?.name}</div>;
}
```

### 性能监控配置

## 常见问题

### Q1：如何优化首屏加载？
```javascript
// 1. 路由懒加载
const Home = lazy(() => import('./pages/Home'));
// ...
// 2. 预加载关键资源
<link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>
// ...
// 3. 图片懒加载
<img src="image.jpg" loading="lazy" alt="..." />
// ...
// 4. 代码分割
const { chunk } = await import('lodash-es');
// ...
// 5. Service Worker 缓存
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js');
}
// ...
// 6. CDN 加速静态资源
```

### Q2：如何选择构建工具？
| 工具 | 优势 | 适用场景 |
|:------:|--------|:-------|
| Vite | 开发体验极佳，ESM 原生 | 新项目首选 |
| Webpack | 生态最完善，插件丰富 | 遗留项目维护 |
| esbuild | 构建速度极快 | 库打包 |
| Rollup | 输出体积最小 | 库发布 |

### Q3：如何做 Tree Shaking？
```javascript
// 正确：命名导入（可 Tree Shaking）
import { debounce } from 'lodash-es';
// ...
// 错误：默认导入整个包
import _ from 'lodash';  // 不会 Tree Shaking
// ...
// package.json 配置
{
    "sideEffects": false  // 标记无副作用
}
// ...
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
// ...
// 生产环境：CORS 头
// 服务器端配置
app.use(cors({
    origin: ['https://example.com'],
    credentials: true,
}));
// ...
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
// ...
// 2. Promise 未捕获异常
window.addEventListener('unhandledrejection', (event) => {
    reportError({
        type: 'unhandledrejection',
        reason: event.reason,
    });
});
// ...
// 3. React 错误边界
class ErrorBoundary extends React.Component {
    state = { hasError: false };
// ...
    static getDerivedStateFromError(error) {
        return { hasError: true };
    }
// ...
    componentDidCatch(error, info) {
        reportError({ error, info });
    }
// ...
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
npm install -g webpack-bundle-analyzer
npx webpack-bundle-analyzer dist/stats.json
# ...
npx vite-bundle-visualizer
# ...
import { Button } from 'antd';  // 而非 import { Button } from 'antd/lib/button'
# ...
npx depcheck
# ...
build: {
    minify: 'terser',
    terserOptions: {
        compress: { drop_console: true },
    },
}
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 请求重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 功能详解与边界条件

### 核心功能详解

1. **代码静态分析与质量评分**
   - **输入**: JavaScript 代码文件
   - **处理逻辑**: 分析代码结构，检查潜在的问题和错误，评估代码质量
   - **输出**: 代码质量评分、问题列表、建议改进点

2. **依赖漏洞检测与升级建议**
   - **输入**: 项目依赖列表
   - **处理逻辑**: 检查依赖项是否存在已知漏洞，提供升级建议
   - **输出**: 存在漏洞的依赖列表、安全评分、升级方案

3. **批量代码审查与报告生成**
   - **输入**: 代码文件列表
   - **处理逻辑**: 执行代码审查，生成报告
   - **输出**: 审查报告、问题列表、改进建议

4. **CI/CD流水线集成**
   - **输入**: CI/CD流水线配置
   - **处理逻辑**: 将工具集成到CI/CD流程中，自动化代码构建、测试和部署
   - **输出**: 流水线执行状态、测试结果、部署记录

5. **代码复杂度可视化与重构建议**
   - **输入**: 代码文件
   - **处理逻辑**: 分析代码复杂度，提供可视化展示和重构建议
   - **输出**: 复杂度图表、重构建议、优化方案

### 边界条件

1. **输入大小限制**: 代码文件大小不超过500MB
2. **字符编码要求**: 输入代码文件需使用UTF-8编码
3. **并发限制**: 同时处理的请求不超过100个
4. **安全限制**: 防止SQL注入、XSS攻击等安全风险
5. **性能限制**: 单个代码审查任务处理时间不超过5分钟
6. **版本兼容性限制**: 支持Node.js 18及以上版本
7. **依赖版本限制**: 支持npm/yarn/pnpm包管理器
8. **环境限制**: 需要配置Node.js环境变量

### 错误处理

1. **配置错误**: 参数缺失或格式错误，提示用户检查配置要求
2. **运行时错误**: 运行环境不满足，提示用户确认运行环境符合依赖说明
3. **网络错误**: 连接超时或不可达，提示用户检查网络连接
4. **输入格式错误**: 输入内容格式不正确，提示用户参考使用说明中的格式要求
5. **执行结果不符预期**: 指令描述不够明确或上下文不足，提示用户提供更详细的指令描述和上下文信息

### 性能指标

1. **代码质量评分**: 0-100分，分数越高表示代码质量越好
2. **安全评分**: 0-100分，分数越高表示安全性越高
3. **审查报告生成时间**: 单个报告不超过5分钟
4. **流水线执行时间**: 单个任务不超过5分钟
5. **复杂度图表生成时间**: 单个文件不超过30秒

## 安全注意事项

### API密钥与认证
JavaScript工具包专业版使用API密钥进行认证，确保只有授权用户才能访问敏感功能。密钥管理如下：
- **密钥生成**：使用强随机算法生成API密钥，确保唯一性和安全性。
- **权限要求**：根据用户角色分配不同的API访问权限，避免越权操作。
- **认证方式**：采用HTTPS协议进行数据传输，确保密钥在传输过程中的安全。

### 数据安全
在数据传输、存储和处理过程中，JavaScript工具包专业版采取以下安全措施：
- **数据传输**：使用HTTPS协议加密数据传输，防止数据在传输过程中被窃取。
- **数据存储**：对敏感数据进行加密存储，确保数据安全。
- **数据处理**：对敏感数据进行脱敏处理，避免泄露用户隐私。

### 风险评估
潜在安全风险包括：
- **API密钥泄露**：可能导致未授权访问敏感功能。
- **数据泄露**：可能导致用户隐私泄露。
- **代码注入**：可能导致恶意代码执行。

缓解措施如下：
- **API密钥泄露**：定期更换API密钥，限制API访问权限。
- **数据泄露**：对敏感数据进行加密存储，加强网络安全防护。
- **代码注入**：对输入数据进行严格验证和过滤，防止恶意代码执行。

### 安全优选实践
1. 定期更新JavaScript工具包专业版，修复已知安全漏洞。
2. 限制API密钥的访问权限，避免未授权访问。
3. 对敏感数据进行加密存储，确保数据安全。
4. 对输入数据进行严格验证和过滤，防止代码注入攻击。
5. 定期进行安全审计，发现并修复潜在安全风险。

