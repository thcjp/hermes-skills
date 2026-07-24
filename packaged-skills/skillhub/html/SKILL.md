---
slug: "html"
name: "html"
version: 1.0.1
displayName: "HTML"
summary: "规避HTML常见错误,无障碍/表单/SEO疏漏一网打尽。Avoid common HTML mistakes — accessibility gaps, form pitfalls, and"
license: "MIT"
description: |-
  Avoid common HTML mistakes — accessibility gaps, form pitfalls, and
  SEO oversights。核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Other
  - 工具
  - 效率
  - 自动化
  - 创意
  - 图像
  - 通信
  - 邮件
  - div
  - label
  - meta
  - type
  - html
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# HTML

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

- HTML 语义化标签审查：正确使用 `<header>`/`<nav>`/`<main>`/`<article>`/`<section>`/`<aside>`/`<footer>`
- 无障碍（Accessibility）检查：ARIA 属性、标签关联、键盘导航、屏幕阅读器兼容性
- 表单可访问性：`<label>` 关联、`fieldset`/`legend` 分组、输入验证、错误提示
- SEO 优化：Meta 标签、Open Graph、结构化数据（Schema.org）、canonical、robots
- HTML5 最佳实践：文档结构、资源加载策略、懒加载、预连接
- HTML 验证与修复：W3C 标准合规、标签嵌套规则、属性正确性
- 性能优化：关键渲染路径、资源优先级、HTTP 头部优化

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 无障碍检查 | 页面 HTML 与 WCAG 标准 | 无障碍问题列表与修复建议 |
| SEO优化 | 网站页面与关键词 | 优化建议与结构化数据方案 |
| 表单审查 | 表单 HTML 代码 | 可访问性修复与验证增强 |
| 语义化重构 | 旧版 HTML 代码 | 语义化标签重构方案 |
| 性能优化 | 页面 HTML 与资源列表 | 加载策略优化建议 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

### 流程详解：无障碍审查

**步骤 1：文档结构检查**

```html
<!-- 错误示例：全部用 div -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main">
  <div class="article">...</div>
</div>

<!-- 正确示例：语义化标签 -->
<header>
  <nav aria-label="主导航">...</nav>
</header>
<main>
  <article>
    <h1>文章标题</h1>
    <section>
      <h2>章节标题</h2>
      <p>内容...</p>
    </section>
  </article>
  <aside aria-label="相关内容">...</aside>
</main>
<footer>...</footer>
```

**步骤 2：ARIA 属性检查**

| 检查项 | 错误示例 | 正确做法 |
|:-------|:---------|:---------|
| 图片替代文本 | `<img src="logo.png">` | `<img src="logo.png" alt="公司Logo">` |
| 装饰性图片 | `<img src="spacer.gif" alt="间隔">` | `<img src="spacer.gif" alt="" role="presentation">` |
| 按钮语义 | `<div onclick="submit()">提交</div>` | `<button type="submit">提交</button>` |
| 表单标签 | `<input type="text" placeholder="姓名">` | `<label for="name">姓名</label><input id="name" type="text">` |
| 动态内容 | `<div id="msg"></div>` | `<div id="msg" role="status" aria-live="polite"></div>` |
| 隐藏内容 | `<div style="display:none">` | `<div hidden>` 或 `aria-hidden="true"` |

## 表单可访问性规范

### 正确的表单结构

```html
<form action="/submit" method="post" novalidate>
  <!-- 分组表单字段 -->
  <fieldset>
    <legend>个人信息</legend>

    <!-- 文本输入 -->
    <div class="form-group">
      <label for="username">用户名 <span aria-hidden="true">*</span></label>
      <input
        type="text"
        id="username"
        name="username"
        required
        aria-required="true"
        aria-describedby="username-hint username-error"
        autocomplete="username"
      >
      <small id="username-hint">3-20个字符，仅限字母数字</small>
      <span id="username-error" role="alert" class="error"></span>
    </div>

    <!-- 邮箱输入 -->
    <div class="form-group">
      <label for="email">邮箱 <span aria-hidden="true">*</span></label>
      <input
        type="email"
        id="email"
        name="email"
        required
        aria-required="true"
        autocomplete="email"
      >
    </div>

    <!-- 单选按钮 -->
    <fieldset>
      <legend>性别</legend>
      <label><input type="radio" name="gender" value="male"> 男</label>
      <label><input type="radio" name="gender" value="female"> 女</label>
      <label><input type="radio" name="gender" value="other"> 其他</label>
    </fieldset>

    <!-- 复选框 -->
    <div class="form-group">
      <label>
        <input type="checkbox" name="agree" required aria-required="true">
        我已阅读并同意<a href="/terms">服务条款</a>
      </label>
    </div>
  </fieldset>

  <button type="submit">提交</button>
</form>
```

### 表单验证与错误提示

```html
<!-- 使用 aria-live 区域显示验证错误 -->
<div id="form-status" role="alert" aria-live="assertive"></div>

<!-- 输入框验证状态 -->
<input
  type="text"
  id="phone"
  aria-invalid="false"
  aria-describedby="phone-error"
>
<span id="phone-error" role="alert" class="error-message"></span>

<!-- JavaScript 验证示例 -->
<script>
function validateField(field) {
  const errorEl = document.getElementById(field.id + '-error');
  if (!field.checkValidity()) {
    field.setAttribute('aria-invalid', 'true');
    errorEl.textContent = field.validationMessage;
  } else {
    field.setAttribute('aria-invalid', 'false');
    errorEl.textContent = '';
  }
}
</script>
```

## SEO 优化指南

### Meta 标签优化

```html
<head>
  <!-- 基础 Meta -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>页面标题 - 品牌名（建议60字符以内）</title>
  <meta name="description" content="页面描述，建议155字符以内，包含核心关键词">
  <meta name="keywords" content="关键词1,关键词2,关键词3">
  <link rel="canonical" href="https://example.com/page">

  <!-- Open Graph（社交媒体分享） -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="分享标题">
  <meta property="og:description" content="分享描述">
  <meta property="og:image" content="https://example.com/image.jpg">
  <meta property="og:url" content="https://example.com/page">
  <meta property="og:site_name" content="网站名">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="分享标题">
  <meta name="twitter:description" content="分享描述">
  <meta name="twitter:image" content="https://example.com/image.jpg">

  <!-- Robots -->
  <meta name="robots" content="index, follow">
</head>
```

### 结构化数据（Schema.org）

```html
<!-- 文章结构化数据 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "文章标题",
  "author": {
    "@type": "Person",
    "name": "作者名"
  },
  "datePublished": "2024-07-24",
  "dateModified": "2024-07-24",
  "image": "https://example.com/image.jpg",
  "publisher": {
    "@type": "Organization",
    "name": "机构名",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  }
}
</script>

<!-- 面包屑结构化数据 -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "首页", "item": "https://example.com/"},
    {"@type": "ListItem", "position": 2, "name": "分类", "item": "https://example.com/category/"},
    {"@type": "ListItem", "position": 3, "name": "当前页面"}
  ]
}
</script>
```

### 语义化标题层级

```html
<!-- 正确的标题层级（不要跳级） -->
<h1>页面主标题（每页仅一个）</h1>
  <h2>主要章节</h2>
    <h3>子章节</h3>
    <h3>子章节</h3>
  <h2>另一个主要章节</h2>
    <h3>子章节</h3>
      <h4>更细分的章节</h4>

<!-- 错误示例：跳级 -->
<h1>主标题</h1>
<h3>跳过了 h2</h3>  <!-- 错误！ -->

<!-- 错误示例：多个 h1 -->
<h1>标题1</h1>
<h1>标题2</h1>  <!-- 错误！每页应只有一个 h1 -->
```

## 资源加载优化

```html
<head>
  <!-- 预连接到关键域名 -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://cdn.example.com" crossorigin>

  <!-- DNS 预解析 -->
  <link rel="dns-prefetch" href="https://analytics.example.com">

  <!-- 预加载关键资源 -->
  <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/css/critical.css" as="style">

  <!-- 预渲染可能导航的页面 -->
  <link rel="prerender" href="/next-page">

  <!-- CSS 阻塞渲染 -->
  <link rel="stylesheet" href="/css/styles.css">

  <!-- 非关键 CSS 异步加载 -->
  <link rel="preload" href="/css/non-critical.css" as="style" onload="this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/css/non-critical.css"></noscript>
</head>
<body>
  <!-- 图片懒加载 -->
  <img src="image.jpg" loading="lazy" width="400" height="300" alt="描述">

  <!-- 首屏图片立即加载 -->
  <img src="hero.jpg" loading="eager" width="1200" height="600" alt="主图" fetchpriority="high">

  <!-- iframe 懒加载 -->
  <iframe src="embed.html" loading="lazy" title="嵌入内容"></iframe>

  <!-- JavaScript 异步加载 -->
  <script src="/js/main.js" defer></script>  <!-- 延迟到 DOM 解析完成 -->
  <script src="/js/analytics.js" async></script>  <!-- 异步加载，不阻塞 -->
</body>
```

## 常见 HTML 错误速查

| 错误类型 | 错误示例 | 正确做法 |
|:---------|:---------|:---------|
| 重复 ID | `<div id="main">...<div id="main">` | 每个 ID 唯一 |
| 未闭合标签 | `<p>文本<span>强调</p>` | `<p>文本<span>强调</span></p>` |
| 块级元素嵌套在行内中 | `<span><div>块</div></span>` | `<div><span>行内</span></div>` |
| 缺少 alt 属性 | `<img src="pic.jpg">` | `<img src="pic.jpg" alt="描述">` |
| 按钮用 div | `<div class="btn" onclick="...">` | `<button onclick="...">` |
| 表格缺表头 | `<table><tr><td>数据</td></tr>` | 添加 `<th scope="col">` |
| 缺少 lang 属性 | `<html>` | `<html lang="zh-CN">` |
| 外链无 rel | `<a href="https://other.com">` | `<a href="..." rel="noopener noreferrer">` |

## 最佳实践

### 文档模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="页面描述">
  <title>页面标题</title>
  <link rel="canonical" href="https://example.com/page">
  <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
  <header>
    <nav aria-label="主导航"><!-- 导航 --></nav>
  </header>
  <main>
    <h1>页面主标题</h1>
    <article><!-- 主内容 --></article>
  </main>
  <aside aria-label="侧边栏"><!-- 侧边内容 --></aside>
  <footer><!-- 页脚 --></footer>
  <script src="/js/main.js" defer></script>
</body>
</html>
```

### 无障碍检查清单

1. **每个图片都有 alt 属性**（装饰性图片用 `alt=""`）
2. **每个表单控件有关联的 label**
3. **标题层级不跳级**（h1 -> h2 -> h3）
4. **颜色对比度 >= 4.5:1**（正文）或 3:1（大文本）
5. **所有交互元素可键盘操作**（Tab/Enter/Space）
6. **焦点可见**（`:focus-visible` 样式）
7. **动态内容有 aria-live 通知**
8. **页面有跳过导航的链接**（Skip to main content）
9. **视频有字幕，音频有文字版**
10. **尊重 `prefers-reduced-motion`**

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| action | string | 是 | 操作类型: `accessibility`/`seo`/`form`/`semantic`/`performance` |
| html_content | string | 否 | 待审查的 HTML 代码 |
| url | string | 否 | 待审查的页面 URL |
| content | string | 否 | html处理的内容输入，可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    "action": "accessibility",
    "issues_found": 8,
    "issues": [
      {
        "severity": "critical",
        "type": "missing-alt",
        "element": "<img src='banner.jpg'>",
        "line": 42,
        "description": "图片缺少 alt 属性",
        "fix": "<img src='banner.jpg' alt='网站横幅图片'>"
      },
      {
        "severity": "warning",
        "type": "missing-label",
        "element": "<input type='email' name='email'>",
        "line": 78,
        "description": "表单输入缺少关联的 label",
        "fix": "<label for='email'>邮箱</label><input id='email' type='email' name='email'>"
      }
    ],
    "score": 72,
    "metadata": {
      "template_used": "html-auditor",
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
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 常见问题

### Q1: 如何开始使用HTML？
A: 提供你的 HTML 代码或页面 URL，描述你想要的审查类型即可。例如"检查这个页面的无障碍问题"或"优化这个页面的 SEO"。系统会扫描 HTML 代码，识别无障碍缺陷（缺少 alt、label 关联缺失、ARIA 错误等）、SEO 问题（Meta 标签、结构化数据、标题层级等）和性能优化机会，给出具体的修复代码和建议。

### Q2: 审查覆盖哪些 WCAG 标准？
A: 覆盖 WCAG 2.1 AA 级别的主要检查项，包括：感知性（图片替代文本、颜色对比度、字幕）、可操作性（键盘导航、焦点可见、时间调整）、可理解性（表单标签、错误提示、语言声明）、健壮性（ARIA 属性正确性、HTML 语义化）。每条问题会标注严重程度（critical/warning/info）并给出具体的修复代码。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

