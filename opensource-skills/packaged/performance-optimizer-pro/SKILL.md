---
slug: performance-optimizer-pro
name: performance-optimizer-pro
version: "1.1.0"
displayName: "性能优化专家"
summary: "测量优先不盲目优化,Core Web Vitals目标驱动的前端性能提升方案"
license: Proprietary
description: |-
  性能优化专家坚持测量优先原则,核心功能包括Core Web Vitals目标设定与基线采集(LCP/CLS/INP/FCP/TTFB)、性能分析工作流(Profiling/瓶颈定位/优化实施/效果验证)、性能反模式检测、持续监控与性能预算。适用于网站性能审计、瓶颈定位、优化实施、性能回归分析、持续监控场景。触发关键词:性能优化、性能调优、Core Web Vitals、LCP、CLS、INP、性能分析、性能瓶颈、前端性能、加载速度、渲染性能。
tags: [性能优化, Core Web Vitals, 前端性能, 性能调优, 用户体验]
tools:
  - read
  - exec
suggested_price: "12.00"
pricing_tier: "business"
pricing_rationale: "编程开发类, medium市场, enterprise复杂度, weekly频次, business层 → 开发者付费意愿高,但竞品多"
---
# 性能优化专家

测量优先的性能优化框架。不猜测瓶颈,用数据定位问题,用指标验证优化效果。

> "过早优化是万恶之源。" — Donald Knuth

## 核心能力

1. **Core Web Vitals目标驱动**:设定LCP<2.5s、CLS<0.1、INP<200ms、FCP<1.8s、TTFB<800ms目标,采集基线(Lighthouse审计+Chrome User Experience Report+自建RUM),记录优化前所有指标作为对比基准。
2. **性能分析工作流**:Profiling(浏览器DevTools Performance/Network/Memory/Coverage面板+Lighthouse深度审计+WebPageTest多地点测试)→瓶颈定位(加载瓶颈:阻塞渲染/大资源/慢接口/重定向;运行时瓶颈:长任务/布局抖动/重排重绘/内存泄漏)→优化实施→效果验证。
3. **优化实施**:加载优化(图片WebP/AVIF/懒加载/响应式、代码分割、资源预加载、CDN、HTTP/2/3),渲染优化(虚拟列表、CSS containment、will-change、requestAnimationFrame、防抖节流),缓存策略(HTTP缓存/Service Worker/内存缓存)。
4. **性能反模式检测**:检测巨型JS包、阻塞渲染、未优化图片、字体闪烁(FOIT/FOUT)、布局抖动、长任务、过度渲染、内存泄漏8类反模式,给出症状与解决方案。
5. **持续监控**:RUM部署采集真实用户性能数据,性能预算设定阈值超限告警,CI集成PR自动跑Lighthouse防止回归,定期审计(月/季度)。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 性能审计 | 网站URL或项目代码 | Core Web Vitals全面测量报告,输出到`output/{project}/audit-report.md` |
| 瓶颈定位 | 页面加载慢/卡顿现象 | Profiling分析+瓶颈定位报告,输出到`output/{project}/bottleneck.md` |
| 优化实施 | 已知瓶颈+优化需求 | 针对性优化方案+代码改动,输出到`output/{project}/optimization-plan.md` |
| 性能回归 | 优化后性能下降现象 | 回归分析报告+修复方案,输出到`output/{project}/regression.md` |
| 持续监控 | 上线后性能维护需求 | 监控配置+性能预算,输出到`output/{project}/monitoring-config.json` |

**不适用于**:
- 后端/数据库性能优化(本Skill聚焦前端Web性能)
- 移动端原生App性能(非Web性能范畴)
- 网络基础设施优化(如BGP路由优化,非应用层)
- 无明确性能指标的"感觉慢"优化(需先量化)

## 使用流程

### Step 1: 测量优先(永远先测量)
1. **设定目标**:LCP<2.5s、CLS<0.1、INP<200ms、FCP<1.8s、TTFB<800ms
2. **采集基线**:
   - Lighthouse审计(实验室数据):`lighthouse https://example.com --output html --output-path ./report.html`
   - Chrome User Experience Report(真实用户数据)
   - 自建RUM(Real User Monitoring)
3. **记录基线**:保存优化前所有指标,作为对比基准(`output/{project}/baseline.md`)

### Step 2: 性能分析(Profiling)
1. **浏览器DevTools**:
   - Performance面板:录制加载/交互过程
   - Network面板:分析请求瀑布图
   - Memory面板:检测内存泄漏
   - Coverage面板:找出未使用的JS/CSS
2. **Lighthouse深度审计**:获取优化建议清单
3. **WebPageTest**:多地点/多设备测试

### Step 3: 瓶颈定位
1. **加载瓶颈**:阻塞渲染的JS/CSS、大尺寸资源(图片/字体/JS包)、慢接口(TTFB高)、重定向链
2. **运行时瓶颈**:长任务(Long Task>50ms)、强制同步布局(Layout Thrashing)、频繁重排重绘、内存泄漏

### Step 4: 优化实施
1. **加载优化**:图片优化(WebP/AVIF/懒加载/响应式srcset)、代码分割(路由级/组件级)、资源预加载(preload/preconnect)、CDN加速、HTTP/2或HTTP/3
2. **渲染优化**:虚拟列表(长列表)、CSS containment、will-change提示、requestAnimationFrame、防抖节流
3. **缓存策略**:HTTP缓存(Cache-Control/ETag)、Service Worker缓存、内存缓存(数据缓存)

### Step 5: 验证效果
1. 重新测量:用相同环境和方法复测
2. 对比基线:优化前 vs 优化后(`output/{project}/results.md`)
3. 确认无回归:功能完整性+其他指标无下降
4. 记录经验:什么优化有效,效果多少

### Step 6: 持续监控
1. RUM部署:采集真实用户性能数据
2. 性能预算:设定预算阈值,超限告警
3. CI集成:PR中自动跑Lighthouse,防止回归
4. 定期审计:每月/每季度全面性能审计

## 示例

### 示例1: 首屏加载性能优化

**输入**:
```
网站首页LCP=4.2s(目标<2.5s),CLS=0.25(目标<0.1),需要优化首屏加载性能。
Lighthouse报告显示:未优化的PNG图片2.5MB,阻塞渲染的CSS 800KB,未使用的JS 60%。
```

**输出** (`output/myapp/optimization-plan.md`):
```markdown
# 首屏加载性能优化方案

## 当前基线 vs 目标
| 指标 | 当前值 | 目标值 | 差距 |
|:-----|:-------|:-------|:-----|
| LCP | 4.2s | <2.5s | -1.7s |
| CLS | 0.25 | <0.1 | -0.15 |
| FCP | 2.1s | <1.8s | -0.3s |

## 瓶颈分析
1. **LCP瓶颈**: 2.5MB的PNG首图未优化,占LCP主要时间
2. **CLS瓶颈**: 图片未设置width/height属性,加载后布局偏移
3. **渲染阻塞**: 800KB CSS全部阻塞首屏渲染

## 优化方案(按优先级)
### P0: 图片优化(预期LCP -1.5s)
- 将PNG转为WebP,尺寸从2.5MB降至300KB(压缩87%)
- 添加 `loading="eager"` 和 `fetchpriority="high"` 到首图
- 设置width/height属性消除CLS

### P1: CSS优化(预期FCP -0.5s)
- 提取首屏关键CSS(critical CSS)内联到HTML
- 其余CSS异步加载:`<link rel="preload" as="style" onload="this.rel='stylesheet'">`
- Tree Shaking移除未使用的CSS

### P2: JS优化(预期减少1.2s阻塞)
- 代码分割:路由级lazy loading
- 移除60%未使用的JS(Tree Shaking + 动态import)
- 第三方库defer加载

## 验证命令
lighthouse https://example.com --output html --output-path ./after-optimization.html --throttling-method=devtools
```

### 示例2: 性能反模式检测

**输入**:
```
检测以下代码的性能反模式:
- 首页加载了3MB的JS bundle
- 列表页渲染10000条数据,滚动卡顿
- 图片用<img src>无懒加载,无尺寸
```

**输出** (`output/myapp/antipattern-report.md`):
```markdown
# 性能反模式检测报告

## 检测到的反模式
| 反模式 | 严重度 | 症状 | 解决方案 |
|:-------|:-------|:-----|:---------|
| 巨型JS包 | 高 | 3MB JS首屏加载 | 路由级代码分割+Tree Shaking+动态import |
| 长列表全量渲染 | 高 | 10000条数据卡顿 | 虚拟列表(react-window/virtual) |
| 未优化图片 | 中 | 无懒加载无尺寸 | loading="lazy"+width/height+WebP |

## 修复代码示例
### 虚拟列表(修复长列表卡顿)
import { FixedSizeList } from "react-window";
<FixedSizeList height={600} itemCount={10000} itemSize={50} width="100%">
  {({ index, style }) => <div style={style}>第{index}项</div>}
</FixedSizeList>

### 图片优化(修复未优化图片)
<img src="hero.webp" width="800" height="600" loading="lazy" alt="..." />
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| Lighthouse无法运行 | 浏览器版本过低或Node.js版本不兼容 | 升级Chrome到最新版,Node.js 18+,或用Docker运行Lighthouse |
| 性能指标波动大 | 网络波动/设备性能差异/后台进程干扰 | 多次测量取中位数,控制测试环境(无其他程序运行) |
| 优化后指标无改善 | 瓶颈定位错误或优化方案无效 | 重新Profiling确认真实瓶颈,检查优化是否正确实施 |
| 优化引入功能回归 | 代码分割导致依赖缺失/缓存策略错误 | 功能完整性测试+逐步回滚定位问题优化项 |
| RUM数据量过大 | 采样率过高导致存储压力 | 设置采样率(如1%-10%),只采集关键指标 |
| CI中Lighthouse超时 | 构建环境性能不足 | 增加CI超时时间,或降低Lighthouse测试范围 |
| 内存泄漏无法复现 | 泄漏仅在特定操作序列下触发 | 使用Chrome Memory面板Heap Snapshot对比,自动化操作序列复现 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:-------|:-----|:---------|:---------|:-------------|
| Chrome浏览器 | 工具 | 推荐 | Lighthouse运行环境 | 国内可直接下载Chrome |
| Node.js 18+ | 运行时 | 推荐 | Lighthouse CLI运行 | Node.js官网,国内用cnpm/nvm镜像 |
| Lighthouse | 工具 | 推荐 | `npm install -g lighthouse` | `cnpm install -g lighthouse` |
| WebPageTest | 服务 | 可选 | 在线性能测试(webpagetest.org) | 国内可用阿里云PTS性能测试 |
| Chrome DevTools | 工具 | 必需 | Chrome内置 | 直接使用 |
| webpack-bundle-analyzer | 工具 | 可选 | JS包分析 | `cnpm install webpack-bundle-analyzer` |
| LLM API | API | 可选 | 由Agent内置LLM提供性能分析 | 国内Agent(通义/文心/智谱)均可 |

### API Key 配置
- **本Skill本身无需API Key**: 核心性能分析在本地完成
- **WebPageTest API**: 可选,通过环境变量传入API Key
- **安全要求**: API Key零暴露,通过环境变量管理,不写入代码/日志/文档

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于运行Lighthouse和分析工具

## 优化优先级矩阵

| 影响 | 易实现 | 优先做 |
|:-----|:-------|:-------|
| 高 | 易 | 第一优先 |
| 高 | 难 | 规划后做 |
| 低 | 易 | 顺手做 |
| 低 | 难 | 不做 |

## 输出规范

- 性能基线:`output/{project}/baseline.md`
- 审计报告:`output/{project}/audit-report.md`
- 优化方案:`output/{project}/optimization-plan.md`
- 优化结果:`output/{project}/results.md`(前后对比)
- 监控配置:`output/{project}/monitoring-config.json`

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 电商网站全面性能审计

**输入**:
```
网站: https://shop.example.com
Lighthouse审计结果(移动端):
- Performance: 42分
- LCP: 5.8s, FCP: 3.2s, CLS: 0.32, INP: 350ms, TTFB: 1.2s
- 主要问题: 首页Hero图3.5MB JPEG、6个渲染阻塞CSS(共1.2MB)、
  jQuery+3个插件共800KB同步加载、产品图无懒加载
```

**LLM生成输出** (`output/shop-example/audit-report.md`):
```markdown
# 性能审计报告 - shop.example.com

## 审计概览
| 指标 | 当前值 | 目标值 | 差距 | 严重度 |
|:-----|:-------|:-------|:-----|:-------|
| Performance | 42 | 90+ | -48 | 严重 |
| LCP | 5.8s | <2.5s | -3.3s | 严重 |
| FCP | 3.2s | <1.8s | -1.4s | 高 |
| CLS | 0.32 | <0.1 | -0.22 | 高 |
| INP | 350ms | <200ms | -150ms | 高 |
| TTFB | 1.2s | <800ms | -0.4s | 中 |

## 瓶颈定位

### 1. 加载瓶颈(影响LCP/FCP/TTFB)
| 瓶颈 | 影响 | 根因 | 测量数据 |
|:-----|:-----|:-----|:---------|
| Hero图过大 | LCP +2.5s | 3.5MB JPEG未压缩 | Network面板:下载3.2s |
| CSS阻塞渲染 | FCP +1.4s | 6个CSS文件同步加载1.2MB | Coverage面板:仅使用15% |
| jQuery同步加载 | FCP +0.8s | 800KB JS在head中同步加载 | Performance面板:主线程阻塞800ms |
| TTFB过高 | TTFB +0.4s | 服务端未缓存,每次动态渲染 | WebPageTest:服务器响应1.2s |

### 2. 运行时瓶颈(影响INP/CLS)
| 瓶颈 | 影响 | 根因 | 测量数据 |
|:-----|:-----|:-----|:---------|
| 产品图无尺寸 | CLS +0.22 | img标签无width/height | Layout Shift记录:22次偏移 |
| 长任务 | INP +150ms | 产品筛选时同步过滤500条 | Performance面板:5个>50ms长任务 |
| 布局抖动 | INP +50ms | 滚动时for循环中读写DOM | Performance面板:forced reflow 12次 |

## 优化方案(按优先级矩阵排序)

### P0: Hero图优化(预期LCP -2.5s)
```html
<!-- 优化前 -->
<img src="/hero.jpg" alt="首页大图" class="hero">

<!-- 优化后 -->
<picture>
  <source srcset="/hero.avif" type="image/avif">
  <source srcset="/hero.webp" type="image/webp">
  <img src="/hero.jpg" alt="首页大图" width="1920" height="800"
       fetchpriority="high" decoding="async" class="hero">
</picture>
<!-- 预期: 3.5MB → 150KB(AVIF), LCP从5.8s降至3.3s -->
```

### P1: CSS优化(预期FCP -1.0s)
```html
<!-- 优化前: 6个阻塞CSS -->
<link rel="stylesheet" href="/css/reset.css">
<link rel="stylesheet" href="/css/layout.css">
<link rel="stylesheet" href="/css/components.css">
<link rel="stylesheet" href="/css/pages.css">
<link rel="stylesheet" href="/css/responsive.css">
<link rel="stylesheet" href="/css/theme.css">

<!-- 优化后: 关键CSS内联 + 非关键CSS异步加载 -->
<style>
  /* 内联首屏关键CSS(提取约15KB) */
  body{margin:0;font-family:sans-serif}
  .hero{width:100%;height:500px;object-fit:cover}
  .nav{display:flex;justify-content:space-between;padding:1rem}
</style>
<link rel="preload" href="/css/main.min.css" as="style"
      onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/css/main.min.css"></noscript>
<!-- 预期: 1.2MB → 15KB内联 + 180KB异步, FCP从3.2s降至2.2s -->
```

### P2: JS优化(预期FCP -0.8s)
```html
<!-- 优化前: head中同步加载jQuery -->
<head>
  <script src="/js/jquery.min.js"></script>
  <script src="/js/plugins.js"></script>
</head>

<!-- 优化后: defer加载 + 按需加载 -->
<head>
  <script src="/js/app.min.js" defer></script>
</head>
<body>
  <!-- 产品筛选改为Web Component延迟加载 -->
  <script type="module">
    import('./product-filter.js').then(m => m.init());
  </script>
</body>
<!-- 预期: 800KB同步 → 120KB defer + 60KB动态, FCP从2.2s降至1.4s -->
```

### P3: 产品图懒加载+尺寸(预期CLS -0.20)
```html
<!-- 优化前 -->
<img src="/product-1.jpg" alt="产品">

<!-- 优化后 -->
<img src="/product-1.webp" alt="产品" width="300" height="300"
     loading="lazy" decoding="async">
<!-- 预期: CLS从0.32降至0.12 -->
```

### P4: 长任务拆分(预期INP -120ms)
```javascript
// 优化前: 同步过滤500条产品
function filterProducts(criteria) {
  return products.filter(p => matchCriteria(p, criteria));
  // 阻塞主线程180ms
}

// 优化后: 分片处理,每帧处理100条
function filterProductsAsync(criteria) {
  return new Promise(resolve => {
    const results = [];
    let index = 0;
    function processChunk() {
      const chunk = products.slice(index, index + 100);
      results.push(...chunk.filter(p => matchCriteria(p, criteria)));
      index += 100;
      if (index < products.length) {
        requestAnimationFrame(processChunk);
      } else {
        resolve(results);
      }
    }
    processChunk();
  });
}
// 预期: 180ms阻塞 → 5x16ms分片, INP从350ms降至230ms
```

### P5: 服务端缓存(预期TTFB -0.4s)
```nginx
# Nginx配置: 页面缓存5分钟
location ~ \.html$ {
  proxy_cache my_cache;
  proxy_cache_valid 200 5m;
  add_header X-Cache-Status $upstream_cache_status;
}
# 预期: TTFB从1.2s降至400ms
```

## 优化后预期指标
| 指标 | 优化前 | 优化后(P0-P2) | 优化后(全部) | 目标 |
|:-----|:-------|:--------------|:-------------|:-----|
| LCP | 5.8s | 3.3s | 2.2s | <2.5s |
| FCP | 3.2s | 1.4s | 1.4s | <1.8s |
| CLS | 0.32 | 0.32 | 0.08 | <0.1 |
| INP | 350ms | 350ms | 210ms | <200ms |
| TTFB | 1.2s | 1.2s | 0.4s | <800ms |
| Performance | 42 | 65 | 88 | 90+ |

## 验证命令
```bash
# 优化前基线
lighthouse https://shop.example.com --output json --output-path ./before.json --preset=desktop

# 优化后验证
lighthouse https://shop.example.com --output json --output-path ./after.json --preset=desktop

# 对比
npx lighthouse-compare before.json after.json
```
```

**效果验证**: ✓6项指标全面诊断(LCP/FCP/CLS/INP/TTFB/Performance) ✓瓶颈定位有测量数据支撑 ✓优化按优先级矩阵排序(P0-P5) ✓每项含优化前/后代码对比 ✓量化预期效果与验证命令

### 案例2: 运行时性能瓶颈定位(长任务+内存泄漏)

**输入**:
```
问题: 管理后台数据表格页面,滚动和筛选时严重卡顿
Profiling数据:
- Performance面板: 7个>50ms长任务,最大230ms
- Memory面板: 10分钟内堆内存从15MB增长到120MB(疑似泄漏)
- 页面操作: 打开→筛选→排序→滚动→重复
```

**LLM生成输出** (`output/admin-table/bottleneck.md`):
```markdown
# 运行时性能瓶颈定位报告

## 瓶颈1: 长任务导致交互卡顿

### 症状
- 用户筛选/排序时页面冻结230ms
- Performance面板显示7个Long Task(>50ms)
- 最大长任务230ms,发生在排序点击时

### 根因分析
```javascript
// 问题代码: 排序时同步处理10000条数据
function handleSort(column) {
  // 1. 读取所有行数据(同步) - 50ms
  const rows = table.querySelectorAll('tr');
  const data = Array.from(rows).map(row => extractData(row));

  // 2. 排序(同步) - 120ms
  data.sort((a, b) => compare(a[column], b[column]));

  // 3. 重新渲染所有行(同步) - 60ms
  data.forEach(item => {
    const row = createRow(item);
    table.appendChild(row);  // 每次appendChild触发reflow
  });
}
// 总计230ms长任务,阻塞主线程
```

### 优化方案
```javascript
// 优化1: 使用DocumentFragment批量DOM操作
function handleSort(column) {
  const data = extractAllData(); // 复用缓存数据
  data.sort((a, b) => compare(a[column], b[column]));

  // 使用DocumentFragment,仅触发一次reflow
  const fragment = document.createDocumentFragment();
  data.forEach(item => fragment.appendChild(createRow(item)));
  table.innerHTML = '';
  table.appendChild(fragment);
}

// 优化2: 大数据量使用虚拟列表
import { useVirtualizer } from '@tanstack/react-virtual';

function VirtualTable({ data }) {
  const parentRef = useRef(null);
  const rowVirtualizer = useVirtualizer({
    count: data.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 40,
    overscan: 10,
  });

  return (
    <div ref={parentRef} style={{ height: 600, overflow: 'auto' }}>
      <div style={{ height: rowVirtualizer.getTotalSize(), position: 'relative' }}>
        {rowVirtualizer.getVirtualItems().map(virtualRow => (
          <div key={virtualRow.key}
               style={{ position: 'absolute', top: virtualRow.start, height: 40 }}>
            {data[virtualRow.index].name}
          </div>
        ))}
      </div>
    </div>
  );
}
```

### 预期效果
| 场景 | 优化前 | 优化后 | 提升 |
|:-----|:-------|:-------|:-----|
| 排序(10000条) | 230ms长任务 | 15ms(虚拟列表) | 93% |
| 滚动FPS | 15fps | 60fps | 300% |

---

## 瓶颈2: 内存泄漏(10分钟堆内存15MB→120MB)

### 症状
- 堆内存持续增长,10分钟从15MB到120MB
- 页面操作越多内存增长越快
- Chrome Memory面板Heap Snapshot对比发现游离DOM节点

### 根因分析
```javascript
// 问题代码: 事件监听器未清理
class TableFilter {
  constructor(table) {
    this.table = table;
    // 每次筛选都添加新监听器,旧的不移除
    this.table.addEventListener('click', this.handleClick);
    this.table.addEventListener('input', this.handleInput);

    // 闭包引用: 缓存了完整的行数据
    this.allRows = Array.from(table.querySelectorAll('tr')).map(row => ({
      element: row,        // 引用DOM节点
      data: extractData(row), // 大量数据
    }));
  }

  filter(criteria) {
    // 每次筛选创建新对象但不清除旧的
    this.filteredRows = this.allRows.filter(row =>
      matchCriteria(row.data, criteria)
    );
  }
}

// 每次重新初始化TableFilter,旧实例的监听器和数据仍被引用
// 导致DOM节点和数据无法被GC回收
```

### 优化方案
```javascript
// 修复1: 使用WeakRef或及时清理引用
class TableFilter {
  #listeners = [];

  constructor(table) {
    this.table = table;
    this.setupListeners();
  }

  setupListeners() {
    const clickHandler = this.handleClick.bind(this);
    const inputHandler = this.handleInput.bind(this);
    this.table.addEventListener('click', clickHandler);
    this.table.addEventListener('input', inputHandler);
    this.#listeners = [
      ['click', clickHandler],
      ['input', inputHandler],
    ];
  }

  destroy() {
    // 清理所有事件监听器
    this.#listeners.forEach(([event, handler]) => {
      this.table.removeEventListener(event, handler);
    });
    this.#listeners = [];
    // 释放数据引用
    this.allRows = null;
    this.filteredRows = null;
  }

  filter(criteria) {
    // 复用缓存数据,不创建新引用
    if (!this.allRows) {
      this.allRows = extractAllData(this.table);
    }
    this.filteredRows = this.allRows.filter(row =>
      matchCriteria(row.data, criteria)
    );
  }
}

// 使用AbortController管理监听器(现代方案)
class TableFilterV2 {
  constructor(table) {
    this.table = table;
    this.abortController = new AbortController();
    this.table.addEventListener('click', this.handleClick, {
      signal: this.abortController.signal,
    });
  }

  destroy() {
    this.abortController.abort(); // 一次性清理所有监听器
  }
}
```

### 验证方法
```javascript
// 1. Chrome DevTools Memory面板
//    - 录制Heap Snapshot → 操作10次 → 录制Snapshot → 对比
//    - 预期: 修复后两次Snapshot间无游离节点增长

// 2. 自动化内存测试
async function memoryTest() {
  const initial = performance.memory.usedJSHeapSize;
  for (let i = 0; i < 100; i++) {
    const filter = new TableFilter(table);
    filter.filter({ status: 'active' });
    filter.destroy(); // 关键: 清理
  }
  // 强制GC(需--js-flags="--expose-gc")
  if (window.gc) window.gc();
  const final = performance.memory.usedJSHeapSize;
  console.log(`内存增长: ${(final - initial) / 1024}KB`);
  // 预期: 修复后增长<100KB
}
```

### 预期效果
| 指标 | 优化前 | 优化后 |
|:-----|:-------|:-------|
| 10分钟堆内存 | 15MB→120MB(增长700%) | 15MB→18MB(增长20%) |
| 游离DOM节点 | 2000+ | 0 |
| 事件监听器泄漏 | 每次操作+2 | 0(destroy清理) |
```

**效果验证**: ✓长任务根因定位精确(同步排序+逐行appendChild) ✓虚拟列表方案正确(@tanstack/react-virtual) ✓内存泄漏根因清晰(监听器未清理+闭包引用) ✓修复方案含WeakRef/AbortController两种 ✓验证方法可操作(Heap Snapshot对比+自动化测试)

### 案例3: 性能预算设定与CI集成

**输入**:
```
团队需求: 防止性能回归,在CI中自动检测性能下降
当前基线: LCP 2.3s, CLS 0.08, JS bundle 180KB
要求: 设定性能预算,在GitHub Actions中集成Lighthouse CI
```

**LLM生成输出** (`output/perf-budget/monitoring-config.json`):
```json
{
  "performance_budget": {
    "metrics": {
      "lcp": { "target": 2500, "warning": 2200, "unit": "ms" },
      "cls": { "target": 0.1, "warning": 0.08, "unit": "score" },
      "inp": { "target": 200, "warning": 180, "unit": "ms" },
      "fcp": { "target": 1800, "warning": 1500, "unit": "ms" },
      "ttfb": { "target": 800, "warning": 600, "unit": "ms" }
    },
    "resources": {
      "javascript": { "target": 200000, "warning": 180000, "unit": "bytes" },
      "css": { "target": 50000, "warning": 40000, "unit": "bytes" },
      "images": { "target": 500000, "warning": 400000, "unit": "bytes" },
      "total": { "target": 800000, "warning": 700000, "unit": "bytes" }
    },
    "lighthouse_score": {
      "performance": { "target": 90, "warning": 85 }
    }
  }
}
```

**LLM生成输出** (`output/perf-budget/lighthouserc.js`):
```javascript
// lighthouserc.js - Lighthouse CI配置
module.exports = {
  ci: {
    collect: {
      url: [
        'http://localhost:3000/',
        'http://localhost:3000/products',
        'http://localhost:3000/checkout',
      ],
      numberOfRuns: 3,  // 每个URL跑3次取中位数
      startServerCommand: 'npm run start',
      startServerReadyPattern: 'Ready',
      settings: {
        preset: 'desktop',
        throttling: {
          rttMs: 40,
          throughputKbps: 10240,
          cpuSlowdownMultiplier: 1,
        },
      },
    },
    assert: {
      assertions: {
        // 核心Web Vitals预算
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
        'first-contentful-paint': ['warn', { maxNumericValue: 1800 }],
        'total-blocking-time': ['warn', { maxNumericValue: 200 }],
        // Lighthouse评分
        'categories:performance': ['error', { minScore: 0.9 }],
        'categories:accessibility': ['warn', { minScore: 0.9 }],
        // 资源预算
        'resource-summary:script:size': ['error', { maxNumericValue: 200000 }],
        'resource-summary:stylesheet:size': ['warn', { maxNumericValue: 50000 }],
        'resource-summary:image:size': ['warn', { maxNumericValue: 500000 }],
        'resource-summary:total:size': ['error', { maxNumericValue: 800000 }],
      },
    },
    upload: {
      target: 'filesystem',
      outputDir: './lighthouse-reports',
      reportFilenamePattern: '%%PATHNAME%%-%%DATETIME%%-report.%%EXTENSION%%',
    },
  },
};
```

**LLM生成输出** (`output/perf-budget/github-actions.yml`):
```yaml
# .github/workflows/lighthouse-ci.yml
name: Lighthouse CI
on: [pull_request]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run build
      - name: Run Lighthouse CI
        run: npx @lhci/cli autorun
        env:
          LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_TOKEN }}
      - name: Upload reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: lighthouse-reports
          path: ./lighthouse-reports/
```

**LLM生成输出** (`output/perf-budget/README.md`):
```markdown
# 性能预算使用说明

## 预算规则
- **error**: 超过target值,阻止PR合并
- **warn**: 超过warning值,PR评论提醒但不阻止

## 本地验证
```bash
# 安装Lighthouse CI
npm install -g @lhci/cli

# 本地运行性能检测
lhci autorun --collect.url=http://localhost:3000

# 查看报告
open ./lighthouse-reports/localhost-*.html
```

## 当预算超标时
1. 查看PR中Lighthouse CI的评论,定位超标指标
2. 使用 `lhci open` 查看详细报告
3. 对照优化方案(见audit-report.md)进行修复
4. 修复后重新push,CI自动重测
```

**效果验证**: ✓性能预算JSON配置完整(metrics+resources+lighthouse_score) ✓Lighthouse CI配置含error/warn两级 ✓GitHub Actions集成完整(build→test→upload) ✓3个URL各跑3次取中位数(减少波动) ✓本地验证说明清晰

## 常见问题

### Q1: 如何在国内使用Lighthouse和WebPageTest?
A: Lighthouse是本地工具,`cnpm install -g lighthouse`安装后直接使用,不依赖海外服务。WebPageTest(wpt.org)国内访问可能不稳定,替代方案:阿里云PTS(性能测试服务)、腾讯云压测、或用Lighthouse CI在本地搭建持续性能监控。Chrome DevTools完全本地使用,无网络依赖。

### Q2: Core Web Vitals的三个指标分别代表什么?怎么优化?
A: LCP(最大内容绘制)衡量加载性能,优化:图片优化(WebP/预加载)、减少阻塞资源、CDN。CLS(累积布局偏移)衡量视觉稳定性,优化:图片设width/height、字体font-display:swap、避免动态插入内容。INP(交互到下次绘制)衡量交互响应性,优化:拆分长任务、Web Worker、减少JS执行时间。

### Q3: 优化后性能指标反而下降了怎么办?
A: (1)确认测量环境一致(网络/设备/浏览器);(2)检查优化是否正确实施(代码分割是否生效、缓存是否配置);(3)逐步回滚优化项,定位是哪个优化导致回归;(4)重新Profiling确认新瓶颈。优化可能引入新问题(如代码分割导致 waterfall请求增多),需整体权衡。

### Q4: 性能预算怎么设定和执行?
A: 设定方法:基于当前基线设定合理阈值(如JS bundle<200KB、LCP<2.5s)。执行方式:(1)CI集成:PR中自动跑Lighthouse CI,指标超标则阻止合并;(2)webpack-bundle-analyzer:构建时检查bundle大小;(3)RUM告警:真实用户指标超阈值时通知。预算应渐进收紧,不是一步到位。

### Q5: 移动端性能优化和PC端有什么不同?
A: 移动端需额外考虑:(1)网络:移动网络不稳定,需更激进缓存和更小资源;(2)CPU:移动设备性能弱,减少JS执行和长任务;(3)内存:移动设备内存小,注意内存泄漏;(4)触摸:INP在移动端更关键,触控响应需<100ms。测试时务必用Lighthouse移动模式或真实移动设备。

## 已知限制

- Lighthouse实验室数据与真实用户数据(RUM)存在差异,实验室环境无法完全模拟真实网络/设备条件,关键决策应以RUM数据为准
- 性能优化效果受项目具体技术栈影响,本Skill提供通用方法论,具体优化方案需结合框架特性(React/Vue/Angular各有不同优化策略)
- 持续监控需要额外基础设施投入(RUM服务/CI集成/告警系统),小团队可能资源不足
- 性能优化与功能开发存在时间冲突,需团队平衡优先级
- 浏览器版本差异导致性能指标不一致,需明确目标浏览器范围并多版本测试

## 安全

- **API Key零暴露**: WebPageTest等第三方服务API Key通过环境变量传入,不硬编码到代码、不写入日志、不输出到报告
- **性能数据脱敏**: RUM采集的用户性能数据可能含URL路径,敏感页面需过滤不上报
- **Lighthouse报告安全**: Lighthouse报告可能含页面DOM结构,敏感项目报告不公开分享
- **CI环境隔离**: CI中运行Lighthouse的测试环境与生产环境隔离,不访问真实用户数据
- **监控数据合规**: RUM数据采集需符合隐私法规(如GDPR/个人信息保护法),不采集用户身份信息
