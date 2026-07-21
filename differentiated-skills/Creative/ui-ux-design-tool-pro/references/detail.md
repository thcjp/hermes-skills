# 详细参考 - ui-ux-design-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (css)

```css
/* 设计令牌 - 语义化命名 */
:root {
  /* 色彩令牌 */
  --color-brand-primary:    #2563eb;
  --color-brand-secondary:  #64748b;
  --color-brand-accent:     #22d3ee;

  /* 语义色彩 */
  --color-action-primary:   var(--color-brand-primary);
  --color-action-hover:     #1d4ed8;
  --color-action-disabled:  #93c5fd;

  --color-feedback-success: #10b981;
  --color-feedback-error:   #ef4444;
  --color-feedback-warning: #f59e0b;
  --color-feedback-info:    #3b82f6;

  /* 表面色彩 */
  --color-surface-base:     #ffffff;
  --color-surface-raised:   #f8fafc;
  --color-surface-overlay:  rgba(255, 255, 255, 0.8);

  /* 文字色彩 */
  --color-text-primary:     #0f172a;
  --color-text-secondary:   #475569;
  --color-text-disabled:    #94a3b8;
  --color-text-inverse:     #ffffff;

  /* 间距令牌 */
  --space-xs:  4px;
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  24px;
  --space-xl:  32px;
  --space-2xl: 48px;
  --space-3xl: 64px;

  /* 圆角令牌 */
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-full: 9999px;

  /* 阴影令牌 */
  --shadow-sm:  0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md:  0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg:  0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl:  0 20px 25px rgba(0, 0, 0, 0.15);
}

/* 暗色主题令牌覆盖 */
[data-theme="dark"] {
  --color-surface-base:     #0f172a;
  --color-surface-raised:   #1e293b;
  --color-text-primary:     #f8fafc;
  --color-text-secondary:   #cbd5e1;
}
```

## 代码示例 (javascript)

```javascript
// tailwind.config.ts
import type { Config } from 'tailwindcss';

const config: Config = {
  darkMode: ['class'],
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
};
export default config;
```

## 代码示例 (css)

```css
/* 状态转换动画 */
.button {
  /* 基础态 */
  background-color: var(--color-action-primary);
  transform: scale(1);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.button:hover {
  background-color: var(--color-action-hover);
  transform: scale(1.02);
  box-shadow: var(--shadow-md);
}

.button:active {
  transform: scale(0.98);
  box-shadow: var(--shadow-sm);
}

.button:disabled {
  background-color: var(--color-action-disabled);
  cursor: not-allowed;
  transform: none;
}

/* 加载状态 */
.button.loading {
  color: transparent;
  position: relative;
}
.button.loading::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

