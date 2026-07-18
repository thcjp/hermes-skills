---
slug: ui-ux-promax-tool-pro
name: ui-ux-promax-tool-pro
version: "1.0.0"
displayName: UIUX设计助手(专业版)
summary: 面向团队的企业级UI/UX设计工程平台,含完整设计系统、UX流程、可访问性审查与脚本生成。
license: MIT
edition: pro
description: |-
  UI/UX设计助手专业版为团队与企业提供端到端UI/UX设计工程能力,涵盖完整设计系统、用户体验流程、WCAG AA可访问性审查与设计系统脚本生成。

  核心能力:
  - 完整设计系统(颜色/排版/间距/圆角/阴影/动效令牌)
  - 用户体验流程图与关键路径设计
  - WCAG AA可访问性审查与增强
  - 设计系统脚本(Python)生成与令牌导出
  - 组件规范与状态定义
  - 实施计划与文件级编辑指导

  适用场景:
  - 中大型团队设计系统从0到1搭建
  - 企业产品UX流程设计与评审
  - 可访问性合规改造(WCAG AA)
  - 跨平台设计令牌统一管理

  差异化:专业版兼容免费版的所有设计建议与令牌输出,扩展完整设计系统、UX流程、可访问性审查与脚本能力,适合规模化团队与生产级产品。

  触发关键词: ui, ux, 设计系统, design system, 用户体验, WCAG, 可访问性, design tokens, 设计脚本, 流程图
tags:
- UI/UX
- 设计系统
- 企业开发
- 可访问性
- 用户体验
- 团队协作
tools:
- read
- exec
---

# UI/UX 设计助手(专业版)

## 概述

`ui-ux-promax-tool-pro` 是面向团队与企业的 UI/UX 设计工程平台。它在免费版基础设计建议之上,扩展了完整设计系统(含动效令牌)、用户体验流程图、WCAG AA 可访问性审查、设计系统脚本生成与实施计划能力,帮助团队构建可访问、可维护、跨平台一致的设计体系。

本版本完全兼容免费版输出的所有设计建议与令牌,可平滑升级。所有指令通过 Markdown 驱动 Agent,配套 Python 脚本用于结构化令牌导出。

## 核心能力

| 能力 | 说明 | 是否兼容免费版 |
| --- | --- | --- |
| 基础设计建议 | 免费版全部布局、配色、排版、令牌能力 | 完全兼容 |
| 完整设计系统 | 颜色/排版/间距/圆角/阴影/动效全令牌 | Pro 新增 |
| UX 流程设计 | 用户旅程、关键路径、状态机(空/加载/错误) | Pro 新增 |
| WCAG AA 审查 | 自动审查与增强,达到 WCAG AA 合规 | Pro 新增 |
| 设计系统脚本 | Python 脚本生成令牌与页面覆盖 | Pro 新增 |
| 组件规范 | 组件状态、交互、可访问性 notes | Pro 新增 |
| 实施计划 | 文件级编辑指导与验收标准 | Pro 新增 |
| 多平台输出 | Web/iOS/Android/桌面跨平台令牌 | Pro 新增 |

## 使用场景

### 场景 1:完整设计系统生成

为团队生成涵盖所有维度的设计系统令牌,含动效与多平台输出。

```css
/* design-tokens.css — 完整设计系统令牌 */
:root {
  /* === 颜色令牌 === */
  --color-primary-50: #e6f0ff;
  --color-primary-100: #b3d1ff;
  --color-primary-500: #0066ff;
  --color-primary-700: #0052cc;
  --color-primary-900: #003d99;
  --color-success-500: #00875a;
  --color-warning-500: #ffab00;
  --color-danger-500: #cc0000;
  --color-neutral-0: #ffffff;
  --color-neutral-100: #f5f5f5;
  --color-neutral-500: #888888;
  --color-neutral-900: #1a1a1a;

  /* === 排版令牌 === */
  --font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-family-mono: 'SF Mono', Monaco, Consolas, monospace;
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 2rem;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
  --line-height-tight: 1.25;
  --line-height-base: 1.5;
  --line-height-relaxed: 1.75;

  /* === 间距令牌(8px 基准) === */
  --spacing-0: 0;
  --spacing-1: 0.25rem;
  --spacing-2: 0.5rem;
  --spacing-3: 0.75rem;
  --spacing-4: 1rem;
  --spacing-6: 1.5rem;
  --spacing-8: 2rem;
  --spacing-12: 3rem;
  --spacing-16: 4rem;

  /* === 圆角令牌 === */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* === 阴影令牌 === */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 2px 8px rgba(0,0,0,0.1);
  --shadow-lg: 0 8px 24px rgba(0,0,0,0.15);
  --shadow-xl: 0 16px 48px rgba(0,0,0,0.2);

  /* === 动效令牌 === */
  --motion-duration-fast: 150ms;
  --motion-duration-base: 250ms;
  --motion-duration-slow: 400ms;
  --motion-ease-in: cubic-bezier(0.4, 0, 1, 1);
  --motion-ease-out: cubic-bezier(0, 0, 0.2, 1);
  --motion-ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --motion-ease-spring: cubic-bezier(0.68, -0.55, 0.265, 1.55);

  /* === Z-index 层级 === */
  --z-base: 0;
  --z-dropdown: 1000;
  --z-sticky: 1100;
  --z-modal: 1300;
  --z-toast: 1400;
}

/* 暗色模式覆盖 */
@media (prefers-color-scheme: dark) {
  :root {
    --color-neutral-0: #1a1a1a;
    --color-neutral-100: #2a2a2a;
    --color-neutral-900: #f5f5f5;
  }
}
```

### 场景 2:用户体验流程设计

为产品功能设计完整的 UX 流程,涵盖关键路径与所有状态。

```
我们在设计一个"忘记密码"流程,需要完整的UX流程图与状态定义。
```

工具会输出:

| 阶段 | 屏幕 | 状态 | 交互 | 可访问性 |
| --- | --- | --- | --- | --- |
| 1 | 入口(登录页) | 默认 | 点击"忘记密码" | 链接可键盘聚焦 |
| 2 | 邮箱输入 | 默认/空/错误/加载 | 输入邮箱→提交 | 输入框有 label,错误有 aria-live |
| 3 | 邮箱发送成功 | 默认 | 点击"重新发送" | 倒计时用 aria-live 播报 |
| 4 | 重置密码 | 默认/不匹配/弱密码 | 输入新密码→提交 | 密码强度有文字描述 |
| 5 | 重置成功 | 默认 | 点击"去登录" | 成功用 status role |
| 错误 | 网络失败 | 错误态 | 点击"重试" | 错误用 alert role |
| 边界 | 链接过期 | 错误态 | 点击"重新申请" | 提供明确恢复路径 |

### 场景 3:WCAG AA 可访问性审查

生成审查脚本,对页面进行 WCAG AA 合规检查。

```python
#!/usr/bin/env python3
# scripts/a11y_audit.py — WCAG AA 可访问性审查
import json
import re
import sys
from pathlib import Path

def audit_html(file_path):
    """审查单个 HTML 文件的 WCAG AA 合规性"""
    content = Path(file_path).read_text(encoding='utf-8')
    issues = []

    # 1. 图片必须有 alt
    for match in re.finditer(r'<img[^>]*>', content):
        if 'alt=' not in match.group():
            issues.append({
                'rule': 'WCAG 1.1.1',
                'level': 'A',
                'file': str(file_path),
                'issue': '图片缺少 alt 属性',
                'snippet': match.group()[:80]
            })

    # 2. 表单输入必须有 label 关联
    for match in re.finditer(r'<input[^>]*>', content):
        tag = match.group()
        if 'type="hidden"' in tag:
            continue
        if 'aria-label=' not in tag and 'id=' not in tag:
            issues.append({
                'rule': 'WCAG 1.3.1',
                'level': 'A',
                'file': str(file_path),
                'issue': '输入框缺少 label 关联',
                'snippet': tag[:80]
            })

    # 3. 按钮必须有可访问文本
    for match in re.finditer(r'<button[^>]*>(\s*)</button>', content):
        issues.append({
            'rule': 'WCAG 4.1.2',
            'level': 'A',
            'file': str(file_path),
            'issue': '按钮无可访问文本',
            'snippet': match.group()[:80]
        })

    # 4. 颜色对比度(简化检查:内联样式)
    for match in re.finditer(r'style="[^"]*color:\s*(#[0-9a-fA-F]{3,6})[^"]*background[^"]*:\s*(#[0-9a-fA-F]{3,6})', content):
        issues.append({
            'rule': 'WCAG 1.4.3',
            'level': 'AA',
            'file': str(file_path),
            'issue': '内联颜色需人工验证对比度 ≥ 4.5:1',
            'snippet': match.group()[:80]
        })

    return issues

def main():
    if len(sys.argv) < 2:
        print("用法: python a11y_audit.py <目录或文件>")
        sys.exit(1)

    target = Path(sys.argv[1])
    files = []
    if target.is_file():
        files = [target]
    else:
        files = list(target.rglob('*.html')) + list(target.rglob('*.tsx'))

    all_issues = []
    for f in files:
        all_issues.extend(audit_html(f))

    print(f"=== WCAG AA 审查报告 ===")
    print(f"扫描文件: {len(files)}")
    print(f"发现问题: {len(all_issues)}")
    print()
    for issue in all_issues:
        print(f"[{issue['rule']} ({issue['level']})] {issue['file']}")
        print(f"  问题: {issue['issue']}")
        print(f"  片段: {issue['snippet']}")
        print()

    # 输出 JSON 报告
    report_path = Path('reports/a11y-report.json')
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(json.dumps(all_issues, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"JSON 报告已保存: {report_path}")

if __name__ == '__main__':
    main()
```

## 快速开始

### 第一步:声明团队上下文

在对话中说明团队、产品与设计目标,例如:

```
我们是 12 人的产品团队,正在重构一个面向B端的管理后台。
技术栈:React + Tailwind,目标:WCAG AA 合规,支持暗色模式,
需要完整设计系统与"用户管理"模块的UX流程。
```

### 第二步:获取工程方案

工具会输出完整设计令牌、UX 流程图、可访问性审查脚本与实施计划。

### 第三步:落地与验证

```bash
# 应用设计令牌
cp design-tokens.css src/styles/

# 运行可访问性审查
python3 scripts/a11y_audit.py src/

# 启动设计系统文档站点
npm run storybook
```

## 配置示例

### 多平台令牌导出

```python
#!/usr/bin/env python3
# scripts/export_tokens.py — 多平台令牌导出
import json
from pathlib import Path

tokens = {
    "color": {
        "primary": {"50": "#e6f0ff", "500": "#0066ff", "900": "#003d99"},
        "neutral": {"0": "#ffffff", "900": "#1a1a1a"}
    },
    "spacing": {"1": "0.25rem", "4": "1rem", "8": "2rem"},
    "radius": {"sm": "4px", "md": "8px", "lg": "12px"}
}

# CSS 变量
css_lines = [":root {"]
for category, items in tokens.items():
    for name, value in items.items():
        if isinstance(value, dict):
            for shade, color in value.items():
                css_lines.append(f"  --{category}-{name}-{shade}: {color};")
        else:
            css_lines.append(f"  --{category}-{name}: {value};")
css_lines.append("}")
Path("dist/tokens.css").write_text("\n".join(css_lines), encoding='utf-8')

# iOS Swift
swift_lines = ["import UIKit", "", "enum DesignTokens {"]
for category, items in tokens.items():
    for name, value in items.items():
        if isinstance(value, dict):
            for shade, color in value.items():
                swift_lines.append(f"    static let {category}{name}{shade} = UIColor(hex: \"{color}\")")
        else:
            swift_lines.append(f"    static let {category}{name} = \"{value}\"")
swift_lines.append("}")
Path("dist/Tokens.swift").write_text("\n".join(swift_lines), encoding='utf-8')

# JSON(供设计工具导入)
Path("dist/tokens.json").write_text(json.dumps(tokens, indent=2), encoding='utf-8')

print("令牌已导出: dist/tokens.css, dist/Tokens.swift, dist/tokens.json")
```

### 组件规范模板

```markdown
# Component: Button

## 状态
| 状态 | 视觉 | 可访问性 |
| --- | --- | --- |
| Default | 主色背景,白色文字 | 对比度 ≥ 4.5:1 |
| Hover | 深一阶背景 | 鼠标与键盘均可见 |
| Focus | 3px 蓝色 outline | 键盘可见 |
| Disabled | 灰色背景,降低透明度 | aria-disabled="true" |
| Loading | 旋转图标,文字保留 | aria-busy="true" |

## 交互
- 点击:触发 onClick
- 键盘 Enter/Space:触发 onClick
- Tab:可聚焦

## 可访问性 Notes
- 按钮文本必须可访问(非空)
- 图标按钮必须有 aria-label
- Loading 状态用 aria-busy 通知屏幕阅读器
```

## 最佳实践

1. **令牌覆盖全维度**:颜色、排版、间距、圆角、阴影、动效、z-index 都应令牌化,禁止硬编码。
2. **WCAG AA 内建**:组件默认合规,而非作为可选附加项;对比度、键盘、屏幕阅读器全覆盖。
3. **状态全覆盖**:每个组件与流程必须覆盖空/加载/错误/禁用状态,而非仅理想态。
4. **多平台令牌统一**:通过单一令牌源(JSON)导出 CSS/iOS/Android 各平台格式。
5. **动效令牌化**:duration 与 easing 令牌化,保证全站动效一致。
6. **暗色模式工程化**:通过令牌覆盖实现,而非为每个组件单独写暗色样式。
7. **设计系统文档化**:每个组件配 README,包含状态、交互、可访问性 notes。
8. **可访问性自动化**:CI 中运行 `a11y_audit.py` 与 `axe-core`,违规阻断 PR。

## 常见问题

### Q1: 设计系统如何与 Tailwind 协同?

在 `tailwind.config.js` 中将令牌映射为 theme 字段:`colors: { primary: 'var(--color-primary-500)' }`。这样既用 Tailwind 工具类,又保持令牌驱动。

### Q2: UX 流程图用什么工具绘制?

推荐 Figma / Whimsical / Excalidraw。Pro 版输出的流程表格可直接作为绘制依据,也可用 Mermaid 生成可版本化的流程图。

### Q3: 可访问性审查脚本能否集成到 CI?

可以。将 `a11y_audit.py` 集成到 CI,对每个 PR 触发审查,违规阻断合并。更深入的可访问性测试推荐 `@axe/playwright`。

### Q4: 多平台令牌如何同步?

以 JSON 为单一源,通过 `export_tokens.py` 脚本导出各平台格式。CI 中运行导出脚本,若产物与仓库中不一致则阻断 PR。

### Q5: Pro 版与免费版如何协同?

Pro 版完全兼容免费版的所有设计建议与令牌。个人开发者可继续使用免费版,团队场景启用 Pro 版获得完整设计系统与企业级能力。两个版本可在同一仓库并存。

### Q6: 如何度量设计系统的健康度?

跟踪四个指标:令牌覆盖率(代码中硬编码值占比)、WCAG AA 合规率、组件复用率、文档覆盖率。四者共同反映设计系统健康度。

## 依赖说明

### 运行环境

- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **Python**:建议 3.10+(用于设计系统脚本)
- **Node.js**:建议 20 LTS+(用于文档站点)
- **浏览器**:任意现代浏览器

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python | 运行时 | 推荐 | 官方安装包 |
| Node.js | 运行时 | 推荐 | 官方安装包 |
| Storybook | 文档工具 | 推荐 | `npx storybook init` |
| axe-core / @axe/playwright | 可访问性 | 推荐 | `npm i -D axe-core` |
| Figma / Whimsical | 设计工具 | 可选 | 官方注册 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 本 Skill 完全基于 Markdown 指令,无需额外 API Key
- 设计工具(Figma)如需 API 集成,配置 `FIGMA_TOKEN` 环境变量
- 视觉回归工具(Chromatic)需配置 `CHROMATIC_TOKEN`

### 可用性分类

- **分类**: MD+EXEC(纯 Markdown 指令,部分功能需要 exec 命令行执行能力)
- **说明**: 基于自然语言指令驱动 Agent 输出企业级设计工程方案;Python 脚本与 CI 集成需在仓库中落地并由本地或 CI 执行
