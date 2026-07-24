---
slug: "css"
name: "css"
version: 1.0.2
displayName: "CSS避坑指南"
summary: "规避堆叠上下文、布局怪癖与现代CSS特性误用,覆盖flex/grid/响应式/性能。。规避常见CSS陷阱:堆叠上下文失效、margin collapse、flexbox/grid 误解、响应"
license: "Proprietary"
description: |-
  规避常见CSS陷阱:堆叠上下文失效、margin collapse、flexbox/grid
  误解、响应式策略、现代选择器、滚动行为、简写陷阱、性能优化与
  可访问性基线.
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 通用办公
  - 工具
  - 效率
  - 自动化
  - 开发
  - 代码
  - AI代理
  - agent
  - 创意
  - 执行核心
  - 处理逻辑
  - 返回结构
  - 化结果和
  - 执行状态
category: "Automation"
---
# CSS避坑指南

用户需要CSS专业能力时提供支持,从布局挑战到生产级优化。覆盖堆叠上下文、flexbox/grid模式、响应式设计、性能与可访问性.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | CSS避坑指南处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 堆叠上下文陷阱
- `z-index` 仅对定位元素或 flex/grid 子元素生效
- `isolation: isolate` 创建堆叠上下文,无需 position 即可隔离 z-index 混乱
- `opacity < 1`、`transform`、`filter` 会创建堆叠上下文,导致 z-index 行为异常
- 新堆叠上下文重置 z-index 层级,子元素 `z-index:9999` 无法逃出父级

**输入**: 用户提供堆叠上下文陷阱所需的指令和必要参数.
**处理**: 解析堆叠上下文陷阱的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 2. 布局陷阱
- margin collapse 仅在垂直方向、仅块级元素;flex/grid 子元素不发生塌陷
- `overflow: hidden` 在 flex 容器上可能破坏布局,改用 `overflow: clip` 若无需滚动

**输入**: 用户提供布局陷阱所需的指令和必要参数.
**处理**: 解析布局陷阱的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回布局陷阱的处理结果,包含执行状态码、结果数据和执行日志.
### 3. Flexbox陷阱
- `flex: 1` 等价于 `flex: 1 1 0%`,basis 为 0 而非 auto
- flex 子元素文本截断需设 `min-width: 0`,默认 min-width 为 min-content
- `flex-basis` 优先于 `width`:basis 在 grow/shrink 之前,width 在之后
- `gap` 已支持 flex,不再需要 margin hack 做间距

**输入**: 用户提供Flexbox陷阱所需的指令和必要参数.
**处理**: 解析Flexbox陷阱的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Flexbox陷阱的处理结果,包含执行状态码、结果数据和执行日志.
### 4. Grid陷阱
- `fr` 单独使用不尊重 min-content,需用 `minmax(min-content, 1fr)`
- `auto-fit` 与 `auto-fill` 区别:fit 折叠空轨道,fill 保留
- `grid-template-columns: 1fr 1fr` 不是 50%,而是剩余空间的等分
- 隐式网格轨道可能出人意料,放置在显式网格外的项目仍会出现

**输入**: 用户提供Grid陷阱所需的指令和必要参数.
**处理**: 解析Grid陷阱的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回Grid陷阱的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 响应式哲学
- 移动优先:`min-width` 媒体查询,基础样式面向移动端
- 容器查询:`@container (min-width: 400px)`,基于组件的响应式
- 父元素需设 `container-type: inline-size` 容器查询才能生效
- 真机测试:模拟器遗漏触控目标与真实性能

**输入**: 用户提供响应式哲学所需的指令和必要参数.
**处理**: 解析响应式哲学的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回响应式哲学的处理结果,包含执行状态码、结果数据和执行日志.
### 6. 尺寸函数
- `clamp(min, preferred, max)` 做流式排版:`clamp(1rem, 2.5vw, 2rem)`
- `min()` 与 `max()`:`width: min(100%, 600px)` 替代媒体查询
- `fit-content` 按内容 sizing 直到上限:`width: fit-content` 或 `fit-content(300px)`

**输入**: 用户提供尺寸函数所需的指令和必要参数.
**处理**: 解析尺寸函数的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回尺寸函数的处理结果,包含执行状态码、结果数据和执行日志.
### 7. 现代选择器
- `:is()` 分组:`:is(h1, h2, h3) + p` 减少重复
- `:where()` 同 `:is()` 但零特异性,更易覆盖
- `:has()` 父级选择器:`.card:has(img)` 样式化含图片的卡片
- `:focus-visible` 仅键盘聚焦显示轮廓,鼠标点击不显示

**输入**: 用户提供现代选择器所需的指令和必要参数.
**处理**: 解析现代选择器的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回现代选择器的处理结果,包含执行状态码、结果数据和执行日志.
### 8. 滚动行为
- `scroll-behavior: smooth` 设于 html,原生锚点平滑滚动
- `overscroll-behavior: contain` 防止滚动链到父级/body
- `scroll-snap-type` 与 `scroll-snap-align` 实现原生轮播,无需 JS
- `scrollbar-gutter: stable` 预留滚动条空间,防止布局抖动

**输入**: 用户提供滚动行为所需的指令和必要参数.
**处理**: 解析滚动行为的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回滚动行为的处理结果,包含执行状态码、结果数据和执行日志.
### 9. 简写陷阱
- `inset: 0` 等价于 `top/right/bottom/left: 0`
- `place-items` 是 `align-items` + `justify-items`,`place-items: center` 同时居中
- `margin-inline`、`margin-block` 逻辑属性,尊重书写方向

**处理**: 解析简写陷阱的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回简写陷阱的处理结果,包含执行状态码、结果数据和执行日志.
### 10. 性能思维
- `contain: layout` 隔离重绘,用于独立组件
- `content-visibility: auto` 跳过屏外渲染,长页面性能大幅提升
- `will-change` 谨慎使用,会创建图层消耗内存
- 避免布局抖动:批量读写 DOM

**输入**: 用户提供性能思维所需的指令和必要参数.
**处理**: 解析性能思维的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 11. 可访问性基线
- `prefers-reduced-motion: reduce` 为前庭障碍用户禁用动画
- `prefers-color-scheme`:`@media (prefers-color-scheme: dark)` 暗色模式
- `forced-colors: active` 适配 Windows 高对比度
- 焦点指示器必须可见,不依赖颜色单独传达

**处理**: 解析可访问性基线的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回可访问性基线的处理结果,包含执行状态码、结果数据和执行日志.
### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证返回数据的完整性和格式正确性
- 参考`输出格式`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:---:|:---:|:---:|
| z-index失效 | DOM结构与CSS | 堆叠上下文诊断与修复方案 |
| flex布局异常 | flex容器与子元素CSS | min-width/basis/gap修复 |
| 响应式适配 | 设计稿与断点 | 移动优先+容器查询方案 |
| 性能优化 | 长页面DOM | contain/content-visibility应用 |
| 可访问性审查 | 页面CSS | prefers-* 与焦点指示器修复 |

不适用于:CSS-in-JS框架特定问题、预处理器(Sass/Less)语法、设计系统架构决策.
## 使用流程

1. 识别问题类别:堆叠上下文、布局、响应式、性能、可访问性
2. 查阅对应参考文件:`layout.md`、`responsive.md`、`selectors.md`、`performance.md`
3. 用极端内容测试:最长名称、缺失图片、空状态
4. 优先内建 sizing,让内容决定尺寸
5. 真机验证触控目标与性能

#
## 示例

### 示例1:堆叠上下文修复
```css
/* 问题:子元素 z-index:9999 无法覆盖模态框 */
.modal-wrapper { isolation: isolate; } /* 创建新堆叠上下文,隔离内部z-index */
.modal { z-index: 100; } /* 现在可正确层级 */
```

### 示例2:flex文本截断
```css
/* 问题:flex子元素文本溢出容器 */
.flex-child {
  min-width: 0; /* 默认min-width:min-content 导致溢出 */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

### 示例3:流式排版
```css
/* clamp实现响应式字号 */
h1 { font-size: clamp(1rem, 2.5vw, 2rem); }
/* 最小1rem,首选2.5vw,最大2rem */
```

### 示例4:容器查询
```css
.card-container { container-type: inline-size; }
@container (min-width: 400px) {
  .card { display: grid; grid-template-columns: 1fr 2fr; }
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| `z-index` 不生效 | 元素未定位或非flex/grid子元素 | 添加 `position: relative` 或改用 `isolation: isolate` |
| flex子元素文本无法截断 | 默认 `min-width: min-content` | 设置 `min-width: 0` 后再加 `overflow: hidden` |
| `1fr 1fr` 不是50%宽度 | fr是剩余空间等分,非总宽度 | 改用 `50% 50%` 或 `minmax(min-content, 1fr)` |
| 容器查询不生效 | 父元素未设 `container-type` | 在父容器添加 `container-type: inline-size` |
| 滚动链到body | 缺少 `overscroll-behavior` | 子滚动容器设 `overscroll-behavior: contain` |
| 布局抖动(滚动条出现) | 滚动条占位不一致 | html 设 `scrollbar-gutter: stable` |
| 焦点指示器不可见 | `outline: none` 未提供替代 | 用 `:focus-visible` 提供可见轮廓,不依赖颜色 |

## 常见问题

### Q1: `flex: 1` 为什么basis是0?
A: `flex: 1` 是 `flex: 1 1 0%` 的简写,basis 为 0 意味着所有空间通过 grow 分配,而非按内容尺寸。若要保留内容尺寸作为基准,用 `flex: 1 1 auto`.
### Q2: `:is()` 与 `:where()` 有何区别?
A: 两者功能相同,但 `:where()` 特异性为 0,更易被后续样式覆盖;`:is()` 取参数中最高特异性。需要易覆盖时用 `:where()`,需要继承特异性时用 `:is()`.
### Q3: `content-visibility: auto` 何时使用?
A: 长页面中屏外内容较多的场景,如长列表、文档页。它会跳过屏外渲染,大幅提升性能。但需配合 `contain-intrinsic-size` 避免滚动条跳动.
### Q4: 容器查询与媒体查询如何选择?
A: 组件化设计优先容器查询,因为组件在不同父容器中尺寸不同。页面级布局用媒体查询。两者可共存:媒体查询控制页面结构,容器查询控制组件内部.
### Q5: `clamp()` 的中间值如何选?
A: 中间值通常用视口单位加 rem,如 `clamp(1rem, 2.5vw, 2rem)`。2.5vw 在 400px 视口下约 10px,加上 1rem 基础值,确保移动端不低于 1rem,桌面端不超过 2rem.
### Q6: `will-change` 何时使用?
A: 仅在已知元素即将发生动画或变换时使用,且动画结束后移除。长期保留会创建图层消耗内存,反而降低性能。优先用 `transform` 和 `opacity` 做动画,它们不触发重排.
## 已知限制

- 需要LLM支持,无LLM环境无法生成CSS方案
- 浏览器兼容性需用户自行验证,特别是 `:has()` 在旧浏览器不支持
- 性能建议基于通用最佳实践,实际效果需在目标设备测量
- 不处理CSS-in-JS框架特定问题与预处理器语法
