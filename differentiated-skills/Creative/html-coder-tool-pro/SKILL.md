---
slug: html-coder-tool-pro
name: html-coder-tool-pro
version: "1.0.0"
displayName: HTML编码工具-专业版
summary: 企业级HTML开发引擎，支持HTML5高级API、Web Components、WCAG全面合规与性能优化。
license: MIT
edition: pro
description: |-
  HTML编码工具专业版，面向团队的企业级HTML开发平台。

  核心能力：
  - HTML5 全API覆盖（Canvas/SVG/Storage/Geolocation/Drag&Drop/Web Workers）
  - Web Components 与 Shadow DOM 组件化开发
  - WCAG 2.1 AA/AAA 全面合规检查
  - 性能优化策略（关键路径/预加载/懒加载）
  - 企业级表单系统（复杂验证/多步骤/条件逻辑）
  - 结构化数据与SEO优化
  - 跨浏览器兼容性保障

  适用场景：
  - 企业级 Web 应用开发
  - 复杂交互页面与数据可视化
  - 可访问性合规项目
  - 高性能网站优化

  差异化：专业版在免费版基础上扩展至HTML5高级API、Web Components、WCAG全面合规与性能优化。与免费版语义化HTML能力完全兼容。

  触发关键词: html, HTML5, Canvas, SVG, Web Components, Shadow DOM, WCAG, 可访问性, 性能优化, 结构化数据, SEO, 企业级
tags:
- Creative
- HTML
- Enterprise
- WebStandards
tools:
- read
- exec
---

# HTML编码工具（专业版）

## 概述

HTML编码工具专业版是企业级 HTML 开发平台，覆盖 HTML5 全部 API、Web Components 组件化开发、WCAG 2.1 全面合规检查和性能优化策略。从基础语义化标记到高级 Canvas 绘图、SVG 操作、Web Storage 和地理定位，专业版提供完整的 HTML 开发能力。

本版本与免费版完全兼容——免费版的语义化 HTML、表单验证和响应式图片能力在专业版中完整保留。专业版新增 HTML5 高级 API、Web Components、WCAG 全面合规和性能优化等能力。

## 核心能力

### 能力对比

| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 语义化HTML | 支持 | 支持 |
| 表单验证 | HTML5基础 | 企业级复杂验证 |
| 响应式图片 | picture/srcset | +性能优化策略 |
| 可访问性 | 基础ARIA | WCAG 2.1 AA/AAA全面合规 |
| Canvas/SVG | 不支持 | 完整API支持 |
| Web Storage | 不支持 | localStorage/sessionStorage/IndexedDB |
| Geolocation | 不支持 | 地理定位API |
| Drag & Drop | 不支持 | 拖放API |
| Web Workers | 不支持 | 多线程处理 |
| Web Components | 不支持 | Custom Elements + Shadow DOM |
| 结构化数据 | 不支持 | Schema.org + JSON-LD |
| 性能优化 | 基础懒加载 | 关键路径+预加载+懒加载 |

### 专业版核心能力

```text
HTML5 高级API:
  - Canvas: 2D绘图、图表、游戏渲染
  - SVG: 矢量图形、动画、交互
  - Web Storage: localStorage / sessionStorage
  - IndexedDB: 客户端数据库
  - Geolocation: 地理定位
  - Drag & Drop: 拖放交互
  - Web Workers: 后台多线程
  - WebSockets: 实时通信
  - History API: 单页应用路由

Web Components:
  - Custom Elements: 自定义HTML标签
  - Shadow DOM: 样式与DOM隔离
  - HTML Templates: 可复用模板
  - 组件生命周期管理

WCAG 合规:
  - A级: 基础可访问性
  - AA级: 主流合规标准
  - AAA级: 最高可访问性
  - 自动检查 + 修复建议

性能优化:
  - 关键CSS内联
  - 资源预加载（preload/prefetch）
  - 懒加载（loading=lazy + Intersection Observer）
  - 字体加载优化（font-display）
  - 图片格式优化（WebP/AVIF）

企业级表单:
  - 多步骤表单
  - 条件逻辑字段
  - 异步验证
  - 自定义验证器
  - 表单状态管理

结构化数据:
  - Schema.org 标记
  - JSON-LD 格式
  - Open Graph 标签
  - Twitter Card 标签
```

## 使用场景

### 场景一：Canvas 数据可视化

使用 Canvas API 创建数据可视化图表。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>销售数据可视化</title>
</head>
<body>
  <section aria-labelledby="chart-title">
    <h2 id="chart-title">月度销售趋势</h2>
    <canvas
      id="sales-chart"
      width="800"
      height="400"
      role="img"
      aria-label="月度销售趋势柱状图，显示1月至6月的销售数据"
    >
      <!-- 降级内容：不支持Canvas时显示 -->
      <table>
        <caption>月度销售数据</caption>
        <thead><tr><th>月份</th><th>销售额</th></tr></thead>
        <tbody>
          <tr><td>1月</td><td>120万</td></tr>
          <tr><td>2月</td><td>150万</td></tr>
        </tbody>
      </table>
    </canvas>
  </section>

  <script>
    // Canvas 数据可视化
    const canvas = document.getElementById('sales-chart');
    const ctx = canvas.getContext('2d');

    const data = [
      { month: '1月', value: 120 },
      { month: '2月', value: 150 },
      { month: '3月', value: 180 },
      { month: '4月', value: 165 },
      { month: '5月', value: 200 },
      { month: '6月', value: 220 },
    ];

    // 绘制柱状图
    const barWidth = 80;
    const gap = 40;
    const maxHeight = 300;
    const maxValue = Math.max(...data.map(d => d.value));

    data.forEach((item, index) => {
      const x = 60 + index * (barWidth + gap);
      const barHeight = (item.value / maxValue) * maxHeight;
      const y = 350 - barHeight;

      // 绘制柱子
      ctx.fillStyle = '#1a1a2e';
      ctx.fillRect(x, y, barWidth, barHeight);

      // 绘制数值
      ctx.fillStyle = '#e94560';
      ctx.font = '14px IBM Plex Sans';
      ctx.textAlign = 'center';
      ctx.fillText(`${item.value}万`, x + barWidth / 2, y - 10);

      // 绘制月份
      ctx.fillStyle = '#8892b0';
      ctx.fillText(item.month, x + barWidth / 2, 380);
    });
  </script>
</body>
</html>
```

### 场景二：Web Components 组件化

创建可复用的自定义组件。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>Web Components 示例</title>
</head>
<body>
  <!-- 使用自定义组件 -->
  <product-card
    name="无线降噪耳机"
    price="1299"
    rating="4.5"
    image="headphones.jpg"
  ></product-card>

  <script>
    // 定义产品卡片组件
    class ProductCard extends HTMLElement {
      constructor() {
        super();
        // Shadow DOM 隔离样式
        const shadow = this.attachShadow({ mode: 'open' });

        shadow.innerHTML = `
          <style>
            :host {
              display: block;
              max-width: 300px;
              font-family: 'IBM Plex Sans', sans-serif;
            }
            .card {
              border: 1px solid #e0e0e0;
              border-radius: 12px;
              overflow: hidden;
              transition: transform 0.3s ease;
            }
            .card:hover { transform: translateY(-4px); }
            .card img { width: 100%; height: 200px; object-fit: cover; }
            .card-body { padding: 1rem; }
            .card-title { font-size: 1.1rem; font-weight: 600; margin: 0 0 0.5rem; }
            .card-price { color: #e94560; font-size: 1.3rem; font-weight: 700; }
            .card-rating { color: #f5a623; }
          </style>
          <div class="card">
            <img src="${this.getAttribute('image')}" alt="${this.getAttribute('name')}">
            <div class="card-body">
              <h3 class="card-title">${this.getAttribute('name')}</h3>
              <p class="card-price">¥${this.getAttribute('price')}</p>
              <p class="card-rating">评分: ${this.getAttribute('rating')}★</p>
            </div>
          </div>
        `;
      }

      // 生命周期: 挂载
      connectedCallback() {
        console.log('产品卡片已挂载');
      }

      // 生命周期: 卸载
      disconnectedCallback() {
        console.log('产品卡片已卸载');
      }

      // 属性变化监听
      static get observedAttributes() {
        return ['name', 'price', 'rating', 'image'];
      }

      attributeChangedCallback(name, oldValue, newValue) {
        if (oldValue !== newValue) {
          console.log(`属性 ${name} 变更: ${oldValue} → ${newValue}`);
        }
      }
    }

    // 注册自定义元素
    customElements.define('product-card', ProductCard);
  </script>
</body>
</html>
```

### 场景三：WCAG 全面合规检查

```python
# WCAG 2.1 合规检查器
class WCAGComplianceChecker:
    """WCAG 2.1 AA/AAA 合规检查器"""

    def __init__(self, level="AA"):
        self.level = level
        self.violations = []

    def check_full_compliance(self, html_content):
        """全面合规检查"""
        checks = {
            "1.1.1": self._check_non_text_content,    # 非文本内容
            "1.3.1": self._check_info_relationship,   # 信息与关系
            "1.4.3": self._check_color_contrast,      # 对比度
            "1.4.4": self._check_text_resize,         # 文本缩放
            "2.1.1": self._check_keyboard_accessible,  # 键盘可访问
            "2.4.1": self._check_skip_navigation,     # 跳过导航
            "2.4.2": self._check_page_titled,         # 页面标题
            "2.4.4": self._check_link_purpose,        # 链接目的
            "3.1.1": self._check_lang_attribute,      # 语言属性
            "3.3.2": self._check_labels_instructions,  # 标签与说明
            "4.1.1": self._check_html_valid,          # HTML有效
            "4.1.2": self._check_name_role_value,     # 名称角色值
        }

        for rule_id, check_func in checks.items():
            violations = check_func(html_content)
            self.violations.extend(violations)

        return self._generate_report()

    def _check_non_text_content(self, html):
        violations = []
        if '<img' in html and 'alt=' not in html:
            violations.append({
                "rule": "1.1.1 (A)",
                "severity": "critical",
                "message": "图片缺少 alt 属性",
                "fix": "为所有 img 添加 alt 描述文本"
            })
        return violations

    def _check_info_relationship(self, html):
        violations = []
        if '<table>' in html and '<th' not in html:
            violations.append({
                "rule": "1.3.1 (A)",
                "severity": "serious",
                "message": "表格缺少表头单元格 (th)",
                "fix": "使用 th 标签标记表头"
            })
        return violations

    def _check_color_contrast(self, html):
        return [{
            "rule": "1.4.3 (AA)",
            "severity": "serious",
            "message": "需验证文本对比度 ≥ 4.5:1",
            "fix": "使用对比度检查工具验证所有文本"
        }]

    def _check_keyboard_accessible(self, html):
        violations = []
        if 'onclick' in html and 'onkeydown' not in html and 'onkeypress' not in html:
            violations.append({
                "rule": "2.1.1 (A)",
                "severity": "critical",
                "message": "鼠标事件缺少键盘等价处理",
                "fix": "为 onclick 添加 onkeydown 等价处理"
            })
        return violations

    def _check_skip_navigation(self, html):
        if 'skip' not in html.lower():
            return [{
                "rule": "2.4.1 (A)",
                "severity": "moderate",
                "message": "缺少跳过导航链接",
                "fix": "添加 <a href='#main'>跳到主内容</a>"
            }]
        return []

    def _check_page_titled(self, html):
        if '<title>' not in html:
            return [{
                "rule": "2.4.2 (A)",
                "severity": "serious",
                "message": "页面缺少 title 标签",
                "fix": "添加描述性的 <title> 标签"
            }]
        return []

    def _check_lang_attribute(self, html):
        if 'lang=' not in html.split('<html')[1].split('>')[0]:
            return [{
                "rule": "3.1.1 (A)",
                "severity": "serious",
                "message": "html 标签缺少 lang 属性",
                "fix": "添加 lang='zh-CN' 等语言属性"
            }]
        return []

    def _check_labels_instructions(self, html):
        violations = []
        if '<input' in html and '<label' not in html and 'aria-label' not in html:
            violations.append({
                "rule": "3.3.2 (A)",
                "severity": "critical",
                "message": "表单输入缺少关联标签",
                "fix": "使用 <label> 或 aria-label 关联输入"
            })
        return violations

    def _check_html_valid(self, html):
        return []  # 实际实现会检查HTML有效性

    def _check_name_role_value(self, html):
        return []  # 实际实现会检查ARIA属性

    def _generate_report(self):
        critical = [v for v in self.violations if v["severity"] == "critical"]
        serious = [v for v in self.violations if v["severity"] == "serious"]
        moderate = [v for v in self.violations if v["severity"] == "moderate"]
        return {
            "level": self.level,
            "total_violations": len(self.violations),
            "critical": len(critical),
            "serious": len(serious),
            "moderate": len(moderate),
            "compliant": len(critical) == 0,
            "details": self.violations
        }

# 执行检查
checker = WCAGComplianceChecker("AA")
report = checker.check_full_compliance("<html><body><img src='test.jpg'></body></html>")
print(f"合规: {report['compliant']}")
print(f"严重问题: {report['critical']}, 重要问题: {report['serious']}")
```

## 快速开始

### 第一步：选择能力级别

```text
能力配置:
  基础能力: 语义化HTML + 表单 + 响应式图片（免费版功能）
  高级API: Canvas / SVG / Storage / Geolocation / Workers
  组件化: Web Components / Shadow DOM
  可访问性: WCAG 2.1 AA / AAA
  性能: 关键路径 / 预加载 / 懒加载
  SEO: 结构化数据 / Open Graph
```

### 第二步：创建高级页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- 性能优化: 预加载关键资源 -->
  <link rel="preload" href="critical.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="hero.jpg" as="image">

  <!-- SEO: 结构化数据 -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "页面标题",
    "description": "页面描述"
  }
  </script>

  <!-- Open Graph -->
  <meta property="og:title" content="页面标题">
  <meta property="og:description" content="页面描述">
  <meta property="og:image" content="og-image.jpg">

  <title>高级HTML页面</title>
</head>
<body>
  <!-- 可访问性: 跳过导航 -->
  <a href="#main" class="skip-link">跳到主内容</a>

  <header role="banner"><!-- 导航 --></header>

  <main id="main" role="main">
    <!-- Web Component -->
    <data-chart type="bar" data='[{"label":"A","value":10}]'></data-chart>
  </main>

  <footer role="contentinfo"><!-- 页脚 --></footer>
</body>
</html>
```

### 第三步：运行合规检查

```bash
# WCAG 合规检查
python3 wcag-checker.py --file index.html --level AA

# 性能审计
npx lighthouse https://example.com --output html --output-path ./report.html
```

## 配置示例

### 性能优化配置

```html
<!-- 资源预加载 -->
<link rel="preload" href="critical-font.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="hero-image.webp" as="image">
<link rel="prefetch" href="next-page.html">

<!-- 字体优化 -->
<style>
  @font-face {
    font-family: 'CustomFont';
    src: url('font.woff2') format('woff2');
    font-display: swap;  /* 加载期间使用回退字体 */
  }
</style>

<!-- 图片格式优化 -->
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="描述" loading="lazy" decoding="async">
</picture>

<!-- 脚本优化 -->
<script src="non-critical.js" defer></script>
<script type="module" src="app.js"></script>
```

### Web Storage 配置

```javascript
// localStorage 持久化存储
localStorage.setItem('userPrefs', JSON.stringify({
  theme: 'dark',
  fontSize: 'medium'
}));

// sessionStorage 会话级存储
sessionStorage.setItem('formData', JSON.stringify(formData));

// IndexedDB 客户端数据库
const db = indexedDB.open('AppDB', 1);
db.onupgradeneeded = (event) => {
  const database = event.target.result;
  if (!database.objectStoreNames.contains('items')) {
    database.createObjectStore('items', { keyPath: 'id' });
  }
};
```

## 最佳实践

1. **渐进增强**：先确保基础功能可用，再添加高级特性。
2. **降级方案**：Canvas 降级为表格，Web Components 降级为标准 HTML。
3. **可访问性内建**：从设计阶段就考虑 WCAG 合规，而非事后修补。
4. **性能预算**：设定加载时间预算，优先加载关键资源。
5. **组件化思维**：用 Web Components 封装可复用功能，Shadow DOM 隔离样式。

```text
专业版检查清单:
[ ] HTML5 高级API使用正确（含降级方案）
[ ] Web Components 含 Shadow DOM 隔离
[ ] WCAG 2.1 AA 合规检查通过
[ ] 关键资源已预加载
[ ] 图片使用 AVIF/WebP 优化格式
[ ] 字体使用 font-display: swap
[ ] 结构化数据 JSON-LD 已添加
[ ] 免费版语义化HTML能力正常
```

## 常见问题

### Q: 如何从免费版升级到专业版？

A: 免费版的语义化 HTML、表单验证和响应式图片能力在专业版中完整保留。专业版新增 HTML5 高级 API、Web Components 和 WCAG 全面合规检查，无需迁移已有代码。

### Q: Web Components 浏览器兼容性如何？

A: 现代浏览器（Chrome/Firefox/Safari/Edge）全面支持 Web Components。对于旧浏览器可使用 polyfill（webcomponentsjs）补充支持。

### Q: WCAG AA 和 AAA 的区别？

A: AA 是主流合规标准（对比度 4.5:1），AAA 是最高标准（对比度 7:1）。建议先达到 AA，部分关键页面追求 AAA。

### Q: Canvas 和 SVG 如何选择？

A: Canvas 适合复杂动画和像素级控制（游戏、图表），SVG 适合矢量图形和可缩放场景（图标、地图）。SVG 可被屏幕阅读器访问，Canvas 需要额外 aria 支持。

### Q: 结构化数据对 SEO 有什么帮助？

A: JSON-LD 结构化数据帮助搜索引擎理解页面内容，可触发富文本搜索结果（Rich Snippets），提升点击率和搜索可见性。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **浏览器**: 现代浏览器（Chrome 90+/Firefox 88+/Safari 14+）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 浏览器 | 工具 | 必需 | 现代浏览器 |
| Lighthouse（可选） | 工具 | 推荐 | `npm install -g lighthouse`（性能审计） |
| webcomponentsjs（可选） | Polyfill | 可选 | 旧浏览器兼容支持 |

### API Key 配置
- 本Skill采用纯Markdown指令驱动，无需额外API Key
- HTML5 API 为浏览器原生支持，无需额外配置

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 企业级AI Skill，支持HTML5全API、Web Components与WCAG全面合规
- **适用规模**: 团队与企业级，复杂Web应用开发
- **兼容性**: 与免费版语义化HTML能力完全兼容，支持无缝升级
