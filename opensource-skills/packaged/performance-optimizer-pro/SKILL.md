---
slug: performance-optimizer-pro
name: performance-optimizer-pro
version: "1.0.0"
displayName: "性能优化专家"
summary: "测量优先不盲目优化,Core Web Vitals目标驱动的前端性能提升方案"
license: MIT
description: |-
  性能优化专家——坚持测量优先,用数据定位瓶颈,用指标验证效果。Core Web Vitals目标驱动(LCP/CLS/INP),性能分析工作流+反模式检测,避免盲目优化,让每一分优化投入都有回报。

  核心能力:
  - Core Web Vitals目标:LCP/CLS/INP指标设定与达标策略
  - 性能分析工作流:Profiling→瓶颈定位→优化→验证闭环
  - 反模式检测:常见性能陷阱自动识别与修复建议
  - 加载优化:代码分割/懒加载/预取/资源优先级
  - 渲染优化:虚拟列表/防抖节流/布局抖动消除
  - 持续监控:性能指标持续追踪与回归告警

  适用场景:
  - 独立创业者网站提速:加载慢影响转化,数据驱动优化
  - SaaS创业者性能审计:上线前Core Web Vitals全面达标
  - 副业达人用户体验:页面卡顿影响留存,精准定位修复
  - 一人公司性能回归:优化后性能下降,回归分析与修复

  差异化:不是罗列优化技巧的清单,而是测量优先的性能优化框架,用数据驱动决策而非盲目优化,让没有性能工程经验的开发者也能系统化提升性能。

  触发关键词:性能优化、性能调优、Core Web Vitals、LCP、CLS、INP、性能分析、性能瓶颈、前端性能、加载速度、渲染性能
tags: [性能优化, Core Web Vitals, 前端性能, 性能调优, 用户体验]
tools: [read, exec]
---

# 性能优化专家

测量优先的性能优化框架。不猜测瓶颈,用数据定位问题,用指标验证优化效果。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 性能审计 | 网站性能评估 | Core Web Vitals 全面测量 |
| 瓶颈定位 | 页面加载慢/卡顿 | Profiling 定位瓶颈 |
| 优化实施 | 已知瓶颈需优化 | 针对性优化方案 |
| 性能回归 | 优化后性能下降 | 回归分析与修复 |
| 持续监控 | 上线后性能维护 | 性能指标持续追踪 |

## 工作流

### 1. 测量优先(永远先测量)

> "过早优化是万恶之源。" — Donald Knuth

1. **设定目标**:
   - LCP(Largest Contentful Paint) < 2.5s
   - CLS(Cumulative Layout Shift) < 0.1
   - INP(Interaction to Next Paint) < 200ms
   - FCP(First Contentful Paint) < 1.8s
   - TTFB(Time to First Byte) < 800ms
2. **采集基线**:
   - Lighthouse 审计(实验室数据)
   - Chrome User Experience Report(真实用户数据)
   - 自建 RUM(Real User Monitoring)
3. **记录基线**:保存优化前的所有指标,作为对比基准

### 2. 性能分析工作流

#### 步骤一:Profiling(性能分析)
1. **浏览器 DevTools**:
   - Performance 面板:录制加载/交互过程
   - Network 面板:分析请求瀑布图
   - Memory 面板:检测内存泄漏
   - Coverage 面板:找出未使用的 JS/CSS
2. **Lighthouse 深度审计**:获取优化建议清单
3. **WebPageTest**:多地点/多设备测试

#### 步骤二:瓶颈定位
1. **加载瓶颈**:
   - 阻塞渲染的 JS/CSS
   - 大尺寸资源(图片/字体/JS 包)
   - 慢接口(TTFB 高)
   - 重定向链
2. **运行时瓶颈**:
   - 长任务(Long Task > 50ms)
   - 强制同步布局(Layout Thrashing)
   - 频繁重排重绘
   - 内存泄漏

#### 步骤三:优化实施
1. **加载优化**:
   - 图片优化(WebP/AVIF/懒加载/响应式)
   - 代码分割(路由级/组件级)
   - 资源预加载(preload/preconnect)
   - CDN 加速
   - HTTP/2 或 HTTP/3
2. **渲染优化**:
   - 虚拟列表(长列表)
   - CSS containment
   - will-change 提示
   - requestAnimationFrame
   - 防抖节流
3. **缓存策略**:
   - HTTP 缓存(Cache-Control/ETag)
   - Service Worker 缓存
   - 内存缓存(数据缓存)

#### 步骤四:验证效果
1. **重新测量**:用相同环境和方法复测
2. **对比基线**:优化前 vs 优化后
3. **确认无回归**:功能完整性 + 其他指标无下降
4. **记录经验**:什么优化有效,效果多少

### 3. 性能反模式检测

| 反模式 | 症状 | 解决方案 |
|:-------|:-----|:---------|
| 巨型 JS 包 | 首屏加载大量未使用 JS | 代码分割、Tree Shaking |
| 阻塞渲染 | 外链 CSS/JS 阻塞首屏 | async/defer、内联关键 CSS |
| 未优化图片 | 大尺寸 PNG/JPG | WebP/AVIF、响应式 srcset |
| 字体闪烁 | FOIT/FOUT | font-display: swap |
| 布局抖动 | CLS 高 | 预留尺寸(width/height) |
| 长任务 | INP 高 | 任务拆分、Web Worker |
| 过度渲染 | 重排重绘频繁 | 虚拟 DOM、批量更新 |
| 内存泄漏 | 内存持续增长 | 清理监听器/定时器/引用 |

### 4. 持续监控

1. **RUM 部署**:采集真实用户性能数据
2. **性能预算**:设定预算阈值,超限告警
3. **CI 集成**:PR 中自动跑 Lighthouse,防止回归
4. **定期审计**:每月/每季度全面性能审计

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

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 可选 | 由Agent内置LLM提供性能分析 |
| 性能分析工具 | 工具 | 可选 | profiler/lighthouse等 |

### API Key 配置
- 本Skill无需额外API Key配置

### 纯Markdown使用说明
本Skill为性能优化方法论指导。实际性能分析需要对应语言的profiler工具。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用
