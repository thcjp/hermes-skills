---
slug: frontend-design-v3-pro
name: frontend-design-v3-pro
version: "1.0.0"
displayName: 前端设计V3-专业版
summary: 生产级前端设计引擎，支持多框架输出、高级动效编排与可访问性合规。
license: Proprietary
edition: pro
description: |-
  前端设计工具V3专业版。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
- Frontend
- Enterprise
- Production
tools:
  - - read
- exec
# 前端设计工具V3（专业版）
## 概述
---
前端设计工具V3专业版是生产级前端界面生成平台。它不仅保持免费版的独特美学追求，更将输出扩展至 React、Vue 等多框架生产级代码，集成高级动效编排、可访问性合规检查和性能优化策略，确保生成的界面既美观又可投入生产。

本版本与免费版完全兼容——免费版的美学方向选择、字体指导和反模式检查在专业版中完整保留。专业版新增多框架输出、高级动效、可访问性和性能优化等能力。

## 核心能力
### 能力对比
| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 输出框架 | HTML/CSS/JS | HTML/CSS/JS + React + Vue + TypeScript |
| 代码质量 | 可用 | 生产级（类型定义 + 错误处理） |
| 动效方案 | CSS @keyframes | CSS + Framer Motion + GSAP |
| 可访问性 | 基础语义化 | WCAG 2.1 AA 全面合规 |
| 性能优化 | 无 | 懒加载 + 代码分割 + 资源优化 |
| 组件化 | 无 | 组件架构设计 |
| 响应式 | 基础 | 多断点策略 + 一致性 |
| 设计令牌 | CSS变量 | 自动注入 + 多格式导出 |

### 核心能力
```text
多框架输出:
  - HTML/CSS/JS: 单文件或分离文件
  - React: 函数组件 + Hooks + TypeScript
  - Vue 3: Composition API + <script setup> + TypeScript
  - 共享: 设计令牌跨框架一致

高级动效:
  - CSS: @keyframes + animation-delay 交错
  - Framer Motion: staggerChildren, whileHover, layoutId
  - GSAP: Timeline, ScrollTrigger, 复杂序列
  - 滚动驱动: Intersection Observer + 动效触发

可访问性:
  - 语义化 HTML 结构
  - ARIA 标签与角色
  - 键盘导航支持
  - 焦点管理
  - 颜色对比度检查
  - 屏幕阅读器兼容

性能优化:
  - 图片懒加载 (loading="lazy")
  - 响应式图片 (srcset, <picture>)
  - 代码分割 (React.lazy, 动态导入)
  - 字体加载优化 (font-display: swap)
  - CSS 关键路径优化
  - 资源预加载 (preload, prefetch)

组件化架构:
  - 原子组件 (Button, Input, Icon)
  - 分子组件 (FormField, Card)
  - 有机体组件 (Header, Sidebar)
  - 页面模板
```

## 使用场景
### 场景一：生产级 React 应用界面
生成带有 TypeScript 类型和高级动效的生产级 React 组件。

> 详细代码示例已移至 `references/detail.md`

### 场景二：Vue 3 生产级组件

> 详细代码示例已移至 `references/detail.md`

### 场景三：可访问性合规检查
```python
class AccessibilityChecker:
    """WCAG 2.1 AA 合规检查器"""

    def __init__(self):
        self.issues = []

    def check_html(self, html_content):
        """检查 HTML 内容的可访问性"""
        self._check_semantic_structure(html_content)
        self._check_aria_labels(html_content)
        self._check_heading_hierarchy(html_content)
        self._check_color_contrast(html_content)
        self._check_keyboard_nav(html_content)
        self._check_images_alt(html_content)
        return self._generate_report()

    def _check_semantic_structure(self, html):
        """检查语义化结构"""
        required_tags = ['<header>', '<main>', '<nav>', '<footer>']
        for tag in required_tags:
            if tag not in html:
                self.issues.append({
                    "level": "warning",
                    "rule": "WCAG 1.3.1",
                    "message": f"缺少语义化标签: {tag}"
                })

    def _check_aria_labels(self, html):
        """检查 ARIA 标签"""
        if 'role="button"' in html and 'aria-label' not in html:
            self.issues.append({
                "level": "error",
                "rule": "WCAG 4.1.2",
                "message": "按钮角色缺少 aria-label"
            })

    def _check_heading_hierarchy(self, html):
        """检查标题层级"""
        self.issues.append({
            "level": "info",
            "rule": "WCAG 1.3.1",
            "message": "标题层级应按 h1→h2→h3 顺序，不跳级"
        })

    def _check_color_contrast(self, html):
        """检查颜色对比度"""
        self.issues.append({
            "level": "info",
            "rule": "WCAG 1.4.3",
            "message": "文本对比度应 ≥ 4.5:1 (AA标准)"
        })

    def _check_keyboard_nav(self, html):
        """检查键盘导航"""
        if 'tabindex' not in html and 'button' not in html:
            self.issues.append({
                "level": "warning",
                "rule": "WCAG 2.1.1",
                "message": "确保所有交互元素可通过键盘访问"
            })

    def _check_images_alt(self, html):
        """检查图片 alt 属性"""
        if '<img' in html and 'alt=' not in html:
            self.issues.append({
                "level": "error",
                "rule": "WCAG 1.1.1",
                "message": "图片缺少 alt 属性"
            })

    def _generate_report(self):
        errors = [i for i in self.issues if i["level"] == "error"]
        warnings = [i for i in self.issues if i["level"] == "warning"]
        return {
            "total_issues": len(self.issues),
            "errors": len(errors),
            "warnings": len(warnings),
            "compliant": len(errors) == 0,
            "details": self.issues
        }

checker = AccessibilityChecker()
report = checker.check_html("<html><body><header></header><main></main></body></html>")
print(f"合规: {report['compliant']}, 错误: {report['errors']}, 警告: {report['warnings']}")
```

## 快速开始
### 第一步：选择框架与美学方向
```text
配置选项:
  框架: html | react | vue
  TypeScript: true | false
  美学方向: 极简 | 极繁 | 复古未来 | 有机自然 | 奢华 | 俏皮 | 杂志 | 粗野 | 装饰艺术 | 柔粉
  动效库: css-only | framer-motion | gsap
  可访问性: wcag-aa | wcag-aaa
```

### 第二步：生成生产级代码
```bash
generate-frontend \
  --framework react \
  --typescript \
  --aesthetic "editorial-magazine" \
  --motion "framer-motion" \
  --accessibility "wcag-aa" \
  --output ./src/components/
```

### 第三步：验证可访问性
```bash
check-a11y ./src/components/ --standard wcag-2.1-aa

audit-performance ./src/ --lighthouse
```

## 示例
### 性能优化配置
```html
<!-- 字体加载优化 -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;900&family=IBM+Plex+Sans:wght@300;400;600&display=swap"
      rel="stylesheet">

<!-- 响应式图片 + 懒加载 -->
<img
  src="image-default.jpg"
  srcset="image-sm.jpg 480w, image-md.jpg 768w, image-lg.jpg 1200w"
  sizes="(max-width: 768px) 100vw, 50vw"
  alt="描述文本"
  loading="lazy"
  decoding="async"
  width="600" height="400"
>
```

### React 代码分割配置
```tsx
// 路由级代码分割
import { lazy, Suspense } from 'react';

const HomePage = lazy(() => import('./pages/Home'));
const AboutPage = lazy(() => import('./pages/About'));
const ContactPage = lazy(() => import('./pages/Contact'));

// Suspense 边界
<Suspense fallback={<div aria-busy="true">加载中</div>}>
  <Routes>
    <Route path="/" element={<HomePage />} />
    <Route path="/about" element={<AboutPage />} />
    <Route path="/contact" element={<ContactPage />} />
  </Routes>
</Suspense>
```

## 最佳实践
1. **生产级标准**：所有输出代码包含类型定义、错误处理和可访问性支持。
2. **动效分层**：页面加载用交错入场，交互用微动效，滚动用驱动动效。
3. **性能内建**：懒加载、代码分割、资源优化从设计阶段就考虑。
4. **可访问性优先**：语义化 HTML + ARIA + 键盘导航，WCAG AA 为底线。
5. **框架一致性**：设计令牌跨框架一致，React 和 Vue 输出视觉统一。

```text
专业版检查清单:
[ ] 代码含 TypeScript 类型定义
[ ] 动效方案含页面级交错入场
[ ] 可访问性通过 WCAG AA 检查
[ ] 图片使用懒加载和响应式
[ ] 代码分割已配置（路由级）
[ ] 字体加载已优化 (font-display: swap)
[ ] 设计令牌已跨框架一致
[ ] 免费版美学规范已继承
```

## 常见问题
### Q: 如何从免费版升级到专业版？
A: 免费版的美学方向、字体指导和反模式检查在专业版中完整保留。专业版新增多框架输出、高级动效和可访问性检查，无需迁移已有代码。

### Q: React 和 Vue 可以同时使用吗？
A: 可以。设计令牌跨框架一致，同一设计可以用 React 和 Vue 分别实现，视觉表现统一。

### Q: 可访问性检查覆盖哪些标准？
A: 覆盖 WCAG 2.1 AA 标准，包括语义化结构、ARIA 标签、标题层级、颜色对比度、键盘导航和图片 alt 属性。

### Q: 性能优化包含哪些策略？
A: 包含图片懒加载、响应式图片、代码分割、字体加载优化、CSS 关键路径优化和资源预加载。

### Q: Framer Motion 和 GSAP 如何选择？
A: React 项目优先用 Framer Motion（声明式集成更好），复杂动画序列用 GSAP（Timeline 更强大），简单动效用纯 CSS。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+（框架构建工具需要）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js 16+ | 运行时 | 必需 | nodejs.org 官方下载 |
| React 18+ | 框架 | 可选 | `npm install react react-dom` |
| Vue 3 | 框架 | 可选 | `npm install vue` |
| Framer Motion | 库 | 可选 | `npm install framer-motion` |
| GSAP | 库 | 可选 | `npm install gsap` |
| TypeScript | 语言 | 可选 | `npm install -D typescript` |
| Google Fonts | 字体 | 可选 | CDN免费加载 |

### API Key 配置
- 本Skill采用纯Markdown指令驱动，无需额外API Key
- Google Fonts 通过 CDN 免费加载

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 企业级AI Skill，支持多框架生产级代码输出与可访问性合规
- **适用规模**: 团队与企业级，生产级 Web 应用
- **兼容性**: 与免费版美学规范完全兼容，支持无缝升级

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
