# 详细参考 - minimalist-design-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
color:
  brand:
    primary: "#0052FF"
    secondary: "#4D7CFF"
    accent: "#FF6B35"
  neutral:
    background: "#FAFAFA"
    foreground: "#0F172A"
    muted: "#F1F5F9"
    border: "#E2E8F0"
    card: "#FFFFFF"
  semantic:
    success: "#10B981"
    warning: "#F59E0B"
    error: "#EF4444"
    info: "#3B82F6"
  dark:
    background: "#0F172A"
    foreground: "#F1F5F9"
    muted: "#1E293B"
    border: "#334155"
    card: "#1E293B"

typography:
  display: { family: "Calistoga, serif", sizes: [2, 3, 4, 5] }
  body: { family: "Inter, sans-serif", sizes: [0.875, 1, 1.125] }
  mono: { family: "JetBrains Mono, monospace" }

spacing:
  scale: [0, 0.25, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 12, 16]

shadow:
  sm: "0 1px 3px rgba(0,0,0,0.06)"
  md: "0 4px 6px rgba(0,0,0,0.07)"
  xl: "0 20px 25px rgba(0,0,0,0.1)"
  accent: "0 4px 14px rgba(0,82,255,0.25)"

radius:
  sm: 4
  md: 8
  lg: 12
  xl: 16
  full: 9999
```

## 代码示例 (python)

```python
design_audit = {
    "checks": [
        {
            "name": "色彩合规",
            "test": "all_colors_from_tokens",
            "scan": ["src/**/*.jsx", "src/**/*.tsx", "src/**/*.css"],
            "report": "hardcoded_colors"
        },
        {
            "name": "字体一致",
            "test": "font_usage_matches_spec",
            "scan": ["src/**/*"],
            "report": "non_standard_fonts"
        },
        {
            "name": "间距规范",
            "test": "spacing_uses_scale",
            "scan": ["src/**/*"],
            "report": "non_standard_spacing"
        },
        {
            "name": "组件覆盖",
            "test": "components_use_library",
            "scan": ["src/**/*"],
            "report": "custom_components"
        },
        {
            "name": "可访问性",
            "test": "wcag_aa_compliance",
            "scan": ["src/**/*"],
            "report": "a11y_violations"
        }
    ],
    "report_format": "html",
    "auto_fix_suggestions": True
}
```

## 代码示例 (javascript)

```javascript
// 多主题配置
const themes = {
  light: {
    "--color-bg": "#FAFAFA",
    "--color-fg": "#0F172A",
    "--color-muted": "#F1F5F9",
    "--color-accent": "#0052FF",
    "--color-border": "#E2E8F0",
    "--color-card": "#FFFFFF"
  },
  dark: {
    "--color-bg": "#0F172A",
    "--color-fg": "#F1F5F9",
    "--color-muted": "#1E293B",
    "--color-accent": "#4D7CFF",
    "--color-border": "#334155",
    "--color-card": "#1E293B"
  },
  brand_custom: {
    "--color-bg": "#FFF8F0",
    "--color-fg": "#2D1B0E",
    "--color-muted": "#F5E6D3",
    "--color-accent": "#E67E22",
    "--color-border": "#E8D5BC",
    "--color-card": "#FFFFFF"
  }
};

// 主题切换
function applyTheme(themeName) {
  const root = document.documentElement;
  Object.entries(themes[themeName]).forEach(([key, value]) => {
    root.style.setProperty(key, value);
  });
}
```

