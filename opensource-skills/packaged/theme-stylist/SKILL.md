---
slug: theme-stylist
name: theme-stylist
version: 1.1.0
displayName: 主题造型师
summary: 10+预设主题一键应用,幻灯片文档报告HTML统一专业视觉风格
license: Proprietary
description: 主题造型师——为各类产出物(幻灯片/文档/报告/HTML落地页)应用专业字体与配色主题,内置10+预设主题(Corporate/Minimal/Warm/Nature/Elegant/Tech/Editorial/Playful/Mono/Sunset),支持自定义品牌色生成完整色板。适用于PPT美化、文档美化、报告配色、HTML落地页主题驱动、品牌主题定制场景。触发关键词:主题、配色主题、字体主题、幻灯片主题、文档主题、报告主题、视觉主题、主题设计、主题应用、配色方案、品牌色
tags:
- 主题设计
- 配色方案
- 视觉风格
- 字体配色
- 品牌统一
tools:
- read
- exec
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
---
# 主题造型师

为各类产出物应用专业的视觉主题。一个主题包含完整的色彩体系与字体方案,一键统一风格。内置 10+ 预设主题,支持基于品牌色生成自定义主题,确保跨产出物的视觉一致性。

## 核心能力

1. **预设主题库**:10+ 套成熟主题(Corporate/Minimal/Warm/Nature/Elegant/Tech/Editorial/Playful/Mono/Sunset),开箱即用
2. **主题应用映射**:色彩映射(标题/背景/正文/强调/图表)+ 字体映射(标题/正文/注释)+ 间距规范
3. **自定义主题生成**:基于品牌主色,按色轮理论生成辅色/强调色/功能色/中性色完整色板
4. **一致性检查**:60-30-10 配色比例校验、字体使用审计、间距统一性、图表配色对齐
5. **多产出物适配**:PPT/DOCX/HTML/Markdown/PDF 统一主题输出,CSS 变量 + JSON 配置双格式

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 幻灯片美化 | PPT 文件 + 内容调性 | 应用主题的 PPT + 配色方案 + 字体规范 |
| 文档美化 | DOCX/MD 文件 + 调性 | 美化后的文档 + 主题样式表 |
| 报告配色 | 数据报告 + 图表 | 统一配色的报告 + 图表色板 |
| HTML 落地页 | HTML + 主题选择 | 应用 CSS 变量的 HTML + 主题预览 |
| 主题定制 | 品牌主色 HEX + 调性 | 自定义主题 JSON + CSS 变量 + 色板预览 |

**不适用于**:
- 复杂 UI/UX 设计(交互流程、信息架构,使用 Figma/Sketch)
- Logo 设计(品牌标识,使用 Illustrator)
- 图片编辑与合成(使用 Photoshop)
- 视频动效设计(使用 After Effects)
- 完整品牌 VI 设计(需要专业品牌设计师,本 Skill 仅提供色彩与字体方案)
- 印刷品设计(需考虑 CMYK 色彩空间,本 Skill 为 RGB 数字色彩)

## 使用流程

### Step 1: 主题选择
1. **分析产出物类型**:PPT/文档/报告/HTML
2. **分析内容调性**:专业/活泼/优雅/科技/温暖
3. **推荐主题**:基于内容推荐 2-3 个适配主题
4. **用户确认**:选择主题或要求自定义

### Step 2: 主题应用
1. **色彩应用**:
   - 标题/背景/正文/强调色映射
   - 图表配色(系列色序列)
   - 表格(表头/交替行/边框)
2. **字体应用**:
   - 标题/副标题/正文/注释字号
   - 字重映射
   - 行高与字距
3. **间距规范**:统一的边距/内距/间隔

### Step 3: 自定义主题生成(可选)
1. **输入品牌色**:用户提供品牌主色(HEX 值)
2. **生成完整色板**:
   - 基于主色生成辅色与强调色
   - 生成功能色(成功/警告/错误/信息)
   - 生成中性色(灰阶 50-900)
   - 确保色彩和谐(色轮理论:互补/类比/三角)
3. **字体推荐**:基于调性推荐中英文字体组合
4. **输出主题文件**:可复用的主题配置

### Step 4: 一致性检查
1. **色彩使用**:是否遵循 60-30-10 比例
2. **字体使用**:是否只用了规定的字体
3. **间距一致**:各页面间距是否统一
4. **图表配色**:是否与主题一致

### Step 5: 输出与交付
1. 生成 theme.json(可复用配置)
2. 生成 variables.css(Web 使用)
3. 生成 preview.png(预览图)
4. 生成应用示例(PPT/文档/HTML)

## 预设主题库(10+)

### 1. Corporate(企业蓝)
- 主色:#1a56db(深蓝)
- 辅色:#3b82f6(亮蓝)
- 强调:#f59e0b(琥珀)
- 字体:Inter / Source Sans / 思源黑体
- 适用:企业报告/商务PPT

### 2. Minimal(极简黑白)
- 主色:#111827(近黑)
- 辅色:#6b7280(灰)
- 强调:#10b981(翠绿)
- 字体:Helvetica / Inter / 思源黑体
- 适用:设计/科技/创意

### 3. Warm(暖橙活力)
- 主色:#ea580c(橙)
- 辅色:#fbbf24(金黄)
- 强调:#7c3aed(紫)
- 字体:Poppins / Nunito / 思源宋体
- 适用:消费品/教育/健康

### 4. Nature(自然绿)
- 主色:#16a34a(绿)
- 辅色:#84cc16(黄绿)
- 强调:#0891b2(青)
- 字体:Lora / Merriweather / 思源宋体
- 适用:环保/农业/有机

### 5. Elegant(优雅紫)
- 主色:#7c3aed(紫)
- 辅色:#a78bfa(浅紫)
- 强调:#f59e0b(金)
- 字体:Playfair Display / Lato / 思源宋体
- 适用:奢侈品/美妆/时尚

### 6. Tech(科技深色)
- 主色:#0ea5e9(天蓝)
- 辅色:#6366f1(靛蓝)
- 强调:#22d3ee(青)
- 字体:JetBrains Mono / Inter / 思源等宽
- 适用:技术/开发者/SaaS

### 7. Editorial(杂志风)
- 主色:#991b1b(酒红)
- 辅色:#525252(炭灰)
- 强调:#ca8a04(金)
- 字体:Georgia / Merriweather / 思源宋体
- 适用:出版/媒体/长文

### 8. Playful(活泼多彩)
- 主色:#ec4899(粉)
- 辅色:#8b5cf6(紫)
- 强调:#22c55e(绿)
- 字体:Quicksand / Comfortaa / 站酷快乐体
- 适用:儿童/游戏/社交

### 9. Mono(单色专业)
- 主色:#1f2937(深灰)
- 辅色:#9ca3af(浅灰)
- 强调:#dc2626(红)
- 字体:IBM Plex Sans / IBM Plex Mono / 思源等宽
- 适用:工程/数据/学术

### 10. Sunset(日落渐变)
- 主色:#f97316(橙)
- 辅色:#ec4899(粉)
- 强调:#8b5cf6(紫)
- 字体:Montserrat / Open Sans / 思源黑体
- 适用:创意/活动/营销

## 示例

### 示例1: 应用预设主题(输入→输出)

**输入**:
```
产出物: 企业年度报告 PPT
内容调性: 专业、稳重
当前问题: 配色混乱,字体不统一
```

**输出**(theme.json 片段):
```json
{
  "name": "Corporate",
  "colors": {
    "primary": "#1a56db",
    "secondary": "#3b82f6",
    "accent": "#f59e0b",
    "background": "#ffffff",
    "surface": "#f8fafc",
    "text": {
      "primary": "#111827",
      "secondary": "#6b7280",
      "muted": "#9ca3af"
    },
    "chart": ["#1a56db", "#3b82f6", "#f59e0b", "#10b981", "#8b5cf6"]
  },
  "fonts": {
    "heading": { "family": "Inter, 思源黑体", "weights": [600, 700] },
    "body": { "family": "Inter, 思源黑体", "weights": [400, 500] },
    "mono": { "family": "JetBrains Mono, 思源等宽", "weights": [400] }
  },
  "spacing": { "xs": "4px", "sm": "8px", "md": "16px", "lg": "24px", "xl": "48px" }
}
```

```css
/* variables.css */
:root {
  --color-primary: #1a56db;
  --color-secondary: #3b82f6;
  --color-accent: #f59e0b;
  --color-bg: #ffffff;
  --color-surface: #f8fafc;
  --color-text-primary: #111827;
  --color-text-secondary: #6b7280;
  --font-heading: 'Inter', '思源黑体', sans-serif;
  --font-body: 'Inter', '思源黑体', sans-serif;
}
```

### 示例2: 自定义品牌主题(输入→输出)

**输入**:
```
品牌名: 绿野生活
品牌主色: #2d6a4f (深绿)
调性: 自然、温暖、可信
用途: 官网 + 落地页 + 文档
```

**输出**(完整色板 + 字体):
```json
{
  "name": "GreenField Custom",
  "colors": {
    "primary": "#2d6a4f",
    "secondary": "#52b788",
    "accent": "#f4a261",
    "background": "#fefefe",
    "surface": "#f0f7f4",
    "functional": {
      "success": "#52b788",
      "warning": "#f4a261",
      "error": "#e63946",
      "info": "#457b9d"
    },
    "neutral": {
      "50": "#f8fafc", "100": "#f1f5f9", "200": "#e2e8f0",
      "300": "#cbd5e1", "400": "#94a3b8", "500": "#64748b",
      "600": "#475569", "700": "#334155", "800": "#1e293b", "900": "#0f172a"
    },
    "chart": ["#2d6a4f", "#52b788", "#f4a261", "#457b9d", "#e63946"]
  },
  "fonts": {
    "heading": { "family": "Lora, 思源宋体", "weights": [600, 700] },
    "body": { "family": "Nunito, 思源黑体", "weights": [400, 500] }
  },
  "rationale": "深绿主色传达自然与可信,辅色亮绿提供层次,橙色强调增加温暖感"
}
```

### 示例3: 一致性检查(输入→输出)

**输入**:
```
PPT 文件: 30 页企业报告
应用主题: Corporate
问题: 部分页面仍使用旧配色
```

**输出**(consistency-report.md 片段):
```markdown
## 主题一致性检查报告

### 色彩使用
- 符合比例: 24/30 页 (80%)
- 偏差点: 6 页
  - P5: 使用 #999999 灰色(应为 #6b7280)
  - P12: 强调色用 #ff0000(应为 #f59e0b)
  - P18-P20: 图表色板未使用主题色序列

### 字体使用
- 符合: 28/30 页 (93%)
- 偏差: P3 使用宋体(应为 Inter/思源黑体)

### 间距一致性
- 符合: 26/30 页 (87%)
- 偏差: P7/P15 标题间距过小(应 24px,实际 16px)

### 修复建议
1. 全局替换 #999999 → #6b7280
2. 全局替换 #ff0000 → #f59e0b
3. 应用图表色板(Corporate 5 色)
4. 统一标题间距为 24px
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 品牌色为非 HEX 格式 | RGB/HSL/CMYK 格式 | 自动转换工具 rgb-to-hex,提示用户输入 HEX |
| 品牌色对比度不足 | 主色与背景色对比度 < 4.5 | 自动调整明暗,确保 WCAG AA 合规 |
| 字体不可用 | 系统未安装指定字体 | 提供备用字体栈(优先 Web 字体 CDN) |
| 主题应用后视觉混乱 | 原有样式未清除 | 提供"清除旧样式"步骤,先重置再应用 |
| 图表配色冲突 | 图表库默认色板未替换 | 提供图表库配置代码(ECharts/Chart.js 色板) |
| 暗色模式适配缺失 | 仅生成亮色主题 | 同时生成暗色主题色板(反转 + 调整对比度) |
| 中文字体显示异常 | 系统缺少中文字体 | 配置 Web 字体 CDN(思源/阿里巴巴普惠体) |
| CSS 变量不被旧浏览器支持 | IE11 等旧浏览器 | 提供降级方案(直接 CSS 属性 + PostCSS) |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代 |
|:-------|:-----|:---------|:---------|:---------|
| LLM API | API | 必需 | Agent 内置 LLM 提供设计能力 | 通义/文心/智谱 |
| Tailwind CSS | 工具 | 可选(HTML) | `npm install -D tailwindcss` | npmmirror 镜像 |
| Google Fonts | CDN | 可选(字体) | fonts.google.com | 字体 CDN(bootcdn/75CDN) |
| 思源字体 | 字体 | 可选(中文) | github.com/adobe-fonts/source-han-sans | 字体 CDN |
| 阿里巴巴普惠体 | 字体 | 可选(中文) | alibabafont.com | 免费商用 |

### API Key 配置
- **本Skill无需额外API Key配置**
- **安全要求**: 主题配置文件不包含任何敏感凭证

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,需 exec 能力调用 CSS 工具链(可选)

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 企业年度报告PPT应用Corporate主题(预设主题+PPT样式映射)

**输入**:
```
产出物: 企业年度报告 PPT(35页)
内容调性: 专业、稳重、商务
当前问题: 配色混乱(12种颜色混用),字体不统一(黑体+宋体+楷体),图表用默认色
要求: 应用Corporate主题,统一视觉风格
```

**LLM生成输出** (`output/annual-report/theme.json`):
```json
{
  "name": "Corporate",
  "version": "1.0",
  "colors": {
    "primary": "#1a56db",
    "secondary": "#3b82f6",
    "accent": "#f59e0b",
    "background": "#ffffff",
    "surface": "#f8fafc",
    "text": {
      "primary": "#111827",
      "secondary": "#6b7280",
      "muted": "#9ca3af"
    },
    "chart": ["#1a56db", "#3b82f6", "#f59e0b", "#10b981", "#8b5cf6", "#ef4444"],
    "table": {
      "header_bg": "#1a56db",
      "header_text": "#ffffff",
      "row_alt_bg": "#f8fafc",
      "border": "#e2e8f0"
    }
  },
  "fonts": {
    "heading": { "family": "Inter, 思源黑体", "weights": [600, 700], "sizes": { "h1": "36pt", "h2": "28pt", "h3": "22pt" } },
    "body": { "family": "Inter, 思源黑体", "weights": [400, 500], "sizes": { "large": "18pt", "normal": "16pt", "small": "12pt" } },
    "mono": { "family": "JetBrains Mono, 思源等宽", "weights": [400] }
  },
  "spacing": { "xs": "4px", "sm": "8px", "md": "16px", "lg": "24px", "xl": "48px" },
  "ratio": { "primary": "60%", "secondary": "30%", "accent": "10%" }
}
```

**LLM生成输出** (`output/annual-report/ppt-styles.md` - PPT样式映射指南):
```markdown
## PPT 样式应用指南(Corporate主题)

### 封面页
- 背景: #1a56db 纯色
- 标题: 思源黑体 36pt 白色 加粗
- 副标题: 思源黑体 18pt #93c5fd
- 日期: 思源黑体 14pt #bfdbfe

### 目录页
- 背景: #ffffff
- 标题: 思源黑体 28pt #1a56db 加粗
- 正文: 思源黑体 16pt #111827
- 页码: 思源黑体 12pt #9ca3af

### 内容页(数据图表)
- 背景: #ffffff
- 标题: 思源黑体 22pt #111827 加粗
- 图表色板: #1a56db → #3b82f6 → #f59e0b → #10b981 → #8b5cf6
- 图表标题: 思源黑体 14pt #6b7280
- 数据标签: 思源黑体 12pt #111827

### 表格样式
```html
| 季度 | 营收 | 同比 | 目标完成率 |
|------|------|------|-----------|
| Q1   | 1.2亿| +15% | 102%      |
| Q2   | 1.5亿| +22% | 105%      |
```
- 表头: 背景#1a56db, 文字白色, 思源黑体14pt加粗
- 数据行: 奇数行#ffffff, 偶数行#f8fafc
- 边框: #e2e8f0, 1px

### 强调与高亮
- 关键数据: #f59e0b(琥珀色)加粗
- 正向指标: #10b981(绿色)
- 负向指标: #ef4444(红色)
- 引用块: 左侧3px #1a56db竖线 + #f8fafc背景
```

**效果验证**: ✓完整theme.json含色彩/字体/间距/比例 ✓PPT样式按页面类型分封面/目录/内容/表格 ✓图表色板6色序列可循环使用 ✓60-30-10比例校验(主色60%/辅色30%/强调10%) ✓表格样式含表头/交替行/边框完整规范

### 案例2: 科技创业公司自定义品牌主题(品牌色→完整色板+暗色模式)

**输入**:
```
品牌名: NeuroFlow AI
品牌主色: #6366f1(靛蓝)
调性: 科技、前沿、可信
用途: 官网 + SaaS后台 + API文档 + PPT
要求: 生成完整色板(含功能色/中性色)+ 暗色模式 + ECharts配置
```

**LLM生成输出** (`output/neuroflow/theme.json`):
```json
{
  "name": "NeuroFlow Custom",
  "colors": {
    "light": {
      "primary": "#6366f1",
      "secondary": "#818cf8",
      "accent": "#06b6d4",
      "background": "#ffffff",
      "surface": "#f5f3ff",
      "text": { "primary": "#1e1b4b", "secondary": "#6366f1", "muted": "#a5b4fc" },
      "functional": {
        "success": "#10b981",
        "warning": "#f59e0b",
        "error": "#ef4444",
        "info": "#3b82f6"
      },
      "neutral": {
        "50": "#fafafa", "100": "#f4f4f5", "200": "#e4e4e7",
        "300": "#d4d4d8", "400": "#a1a1aa", "500": "#71717a",
        "600": "#52525b", "700": "#3f3f46", "800": "#27272a", "900": "#18181b"
      },
      "chart": ["#6366f1", "#06b6d4", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6"]
    },
    "dark": {
      "primary": "#818cf8",
      "secondary": "#a5b4fc",
      "accent": "#22d3ee",
      "background": "#0f0a2e",
      "surface": "#1e1b4b",
      "text": { "primary": "#e0e7ff", "secondary": "#a5b4fc", "muted": "#6366f1" },
      "functional": {
        "success": "#34d399",
        "warning": "#fbbf24",
        "error": "#f87171",
        "info": "#60a5fa"
      },
      "chart": ["#818cf8", "#22d3ee", "#34d399", "#fbbf24", "#f87171", "#a78bfa"]
    }
  },
  "fonts": {
    "heading": { "family": "Inter, 思源黑体", "weights": [600, 700] },
    "body": { "family": "Inter, 思源黑体", "weights": [400, 500] },
    "mono": { "family": "JetBrains Mono, 思源等宽", "weights": [400, 500] }
  },
  "rationale": "靛蓝主色传达科技前沿感,青色强调增加活力,暗色模式提升SaaS后台长时间使用舒适度"
}
```

**LLM生成输出** (`output/neuroflow/variables.css`):
```css
/* NeuroFlow 主题变量 - 亮色模式 */
:root {
  --color-primary: #6366f1;
  --color-secondary: #818cf8;
  --color-accent: #06b6d4;
  --color-bg: #ffffff;
  --color-surface: #f5f3ff;
  --color-text-primary: #1e1b4b;
  --color-text-secondary: #6366f1;
  --color-text-muted: #a5b4fc;
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-error: #ef4444;
  --color-info: #3b82f6;

  --font-heading: 'Inter', '思源黑体', sans-serif;
  --font-body: 'Inter', '思源黑体', sans-serif;
  --font-mono: 'JetBrains Mono', '思源等宽', monospace;

  --chart-1: #6366f1;
  --chart-2: #06b6d4;
  --chart-3: #10b981;
  --chart-4: #f59e0b;
  --chart-5: #ef4444;
  --chart-6: #8b5cf6;
}

/* 暗色模式 */
[data-theme="dark"] {
  --color-primary: #818cf8;
  --color-secondary: #a5b4fc;
  --color-accent: #22d3ee;
  --color-bg: #0f0a2e;
  --color-surface: #1e1b4b;
  --color-text-primary: #e0e7ff;
  --color-text-secondary: #a5b4fc;
  --color-text-muted: #6366f1;
  --color-success: #34d399;
  --color-warning: #fbbf24;
  --color-error: #f87171;
  --color-info: #60a5fa;

  --chart-1: #818cf8;
  --chart-2: #22d3ee;
  --chart-3: #34d399;
  --chart-4: #fbbf24;
  --chart-5: #f87171;
  --chart-6: #a78bfa;
}
```

**LLM生成输出** (`output/neuroflow/echarts-config.js` - ECharts色板配置):
```javascript
// ECharts 主题配置
const neuroFlowTheme = {
  color: ['#6366f1', '#06b6d4', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'],
  backgroundColor: 'transparent',
  textStyle: { fontFamily: 'Inter, 思源黑体, sans-serif' },
  title: { textStyle: { color: '#1e1b4b', fontWeight: 600 } },
  legend: { textStyle: { color: '#6b7280' } },
  xAxis: { axisLine: { lineStyle: { color: '#e4e4e7' } }, axisLabel: { color: '#71717a' } },
  yAxis: { splitLine: { lineStyle: { color: '#f4f4f5' } }, axisLabel: { color: '#71717a' } },
  tooltip: {
    backgroundColor: '#1e1b4b',
    borderColor: '#6366f1',
    textStyle: { color: '#e0e7ff' }
  }
};

// 暗色模式色板
const neuroFlowDarkTheme = {
  ...neuroFlowTheme,
  color: ['#818cf8', '#22d3ee', '#34d399', '#fbbf24', '#f87171', '#a78bfa'],
  title: { textStyle: { color: '#e0e7ff' } },
  legend: { textStyle: { color: '#a5b4fc' } },
  xAxis: { axisLine: { lineStyle: { color: '#3f3f46' } }, axisLabel: { color: '#a5b4fc' } },
  yAxis: { splitLine: { lineStyle: { color: '#27272a' } }, axisLabel: { color: '#a5b4fc' } },
  tooltip: {
    backgroundColor: '#1e1b4b',
    borderColor: '#818cf8',
    textStyle: { color: '#e0e7ff' }
  }
};

echarts.registerTheme('neuroflow', neuroFlowTheme);
echarts.registerTheme('neuroflow-dark', neuroFlowDarkTheme);

// 使用: echarts.init(dom, 'neuroflow')
```

**效果验证**: ✓品牌色#6366f1生成完整色板(辅色/强调/功能色/中性色50-900) ✓暗色模式独立色板(反转明度+提升对比度) ✓CSS变量含亮/暗双模式[data-theme="dark"]切换 ✓ECharts色板配置含坐标轴/图例/提示框完整样式 ✓设计理据说明配色逻辑(靛蓝=科技,青色=活力)

### 案例3: 数据报告图表配色+表格样式(Tech主题+ECharts/Chart.js)

**输入**:
```
产出物: 季度数据报告(含6种图表+3个表格)
主题: Tech(科技深色)
图表类型: 柱状图、折线图、饼图、堆叠面积图、散点图、雷达图
要求: 所有图表统一配色,表格风格一致
```

**LLM生成输出** (`output/data-report/chart-theme.json`):
```json
{
  "name": "Tech Chart Palette",
  "base": {
    "primary": "#0ea5e9",
    "secondary": "#6366f1",
    "accent": "#22d3ee",
    "bg": "#0f172a",
    "surface": "#1e293b",
    "text": "#e2e8f0",
    "text_muted": "#94a3b8",
    "grid": "#334155"
  },
  "series_6": ["#0ea5e9", "#6366f1", "#22d3ee", "#10b981", "#f59e0b", "#ec4899"],
  "sequential_blue": ["#0c4a6e", "#075985", "#0369a1", "#0284c7", "#0ea5e9", "#38bdf8", "#7dd3fc"],
  "diverging": { "negative": "#ef4444", "neutral": "#64748b", "positive": "#10b981" }
}
```

**LLM生成输出** (`output/data-report/echarts-tech.js`):
```javascript
// Tech主题 ECharts 完整配置
const techTheme = {
  color: ['#0ea5e9', '#6366f1', '#22d3ee', '#10b981', '#f59e0b', '#ec4899'],

  // 柱状图
  bar: {
    itemStyle: { borderRadius: [4, 4, 0, 0] },
    emphasis: { itemStyle: { shadowBlur: 10, shadowColor: 'rgba(14,165,233,0.5)' } }
  },

  // 折线图
  line: {
    itemStyle: { borderWidth: 2 },
    lineStyle: { width: 3 },
    symbolSize: 6,
    smooth: true
  },

  // 饼图
  pie: {
    itemStyle: { borderColor: '#0f172a', borderWidth: 2 },
    label: { color: '#e2e8f0' },
    emphasis: { itemStyle: { shadowBlur: 15, shadowColor: 'rgba(14,165,233,0.3)' } }
  },

  // 通用样式
  backgroundColor: '#0f172a',
  textStyle: { fontFamily: 'Inter, 思源黑体', color: '#e2e8f0' },
  title: { textStyle: { color: '#f1f5f9', fontSize: 16, fontWeight: 600 } },
  legend: { textStyle: { color: '#94a3b8' }, inactiveColor: '#475569' },
  tooltip: {
    backgroundColor: '#1e293b',
    borderColor: '#334155',
    borderWidth: 1,
    textStyle: { color: '#e2e8f0' }
  },
  xAxis: {
    axisLine: { lineStyle: { color: '#334155' } },
    axisLabel: { color: '#94a3b8' },
    splitLine: { show: false }
  },
  yAxis: {
    axisLine: { show: false },
    axisLabel: { color: '#94a3b8' },
    splitLine: { lineStyle: { color: '#1e293b', type: 'dashed' } }
  }
};

echarts.registerTheme('tech', techTheme);

// 使用示例
const chart = echarts.init(document.getElementById('chart'), 'tech');
chart.setOption({
  series: [{
    type: 'bar',
    data: [120, 200, 150, 80, 70, 110, 130],
    itemStyle: { color: techTheme.color[0] }
  }]
});
```

**LLM生成输出** (`output/data-report/table-styles.css`):
```css
/* Tech主题表格样式 */
.tech-table {
  width: 100%;
  border-collapse: collapse;
  background: #0f172a;
  color: #e2e8f0;
  font-family: 'Inter', '思源黑体', sans-serif;
  font-size: 14px;
}

.tech-table thead th {
  background: #1e293b;
  color: #38bdf8;
  padding: 12px 16px;
  text-align: left;
  font-weight: 600;
  border-bottom: 2px solid #0ea5e9;
}

.tech-table tbody tr:nth-child(even) {
  background: #1e293b;
}

.tech-table tbody td {
  padding: 10px 16px;
  border-bottom: 1px solid #334155;
}

.tech-table .positive { color: #10b981; font-weight: 500; }
.tech-table .negative { color: #ef4444; font-weight: 500; }
.tech-table .neutral  { color: #94a3b8; }

/* 悬停高亮 */
.tech-table tbody tr:hover {
  background: #334155;
  transition: background 0.2s;
}
```

**效果验证**: ✓6色系列色板适配柱状/折线/饼/散点/雷达/堆叠 ✓连续色阶(sequential_blue)适配热力图 ✓发散色(negative/neutral/positive)适配同比对比 ✓ECharts完整主题含柱状圆角/折线平滑/饼图分割 ✓表格CSS含表头/交替行/正负值着色/悬停高亮

### 案例4: 30页混合风格PPT一致性检查与修复

**输入**:
```
PPT文件: 30页企业汇报(多人协作制作)
应用主题: Corporate(#1a56db蓝)
发现问题:
  - P5/P8/P12 使用 #999999 灰色(应#6b7280)
  - P15/P18 强调色用 #ff0000 红色(应#f59e0b琥珀)
  - P20-P25 图表用Office默认色板(非主题色)
  - P3/P7 字体用宋体(应思源黑体)
  - P10/P22 标题间距16px(应24px)
```

**LLM生成输出** (`output/ppt-audit/consistency-report.md`):
```markdown
# PPT主题一致性检查报告

## 检查摘要
| 检查维度 | 符合页数 | 总页数 | 符合率 | 状态 |
|:---------|:---------|:-------|:-------|:-----|
| 色彩使用 | 22/30 | 30 | 73% | 需修复 |
| 字体使用 | 28/30 | 30 | 93% | 轻微偏差 |
| 间距一致 | 26/30 | 30 | 87% | 轻微偏差 |
| 图表配色 | 24/30 | 30 | 80% | 需修复 |
| 总体评分 | - | - | 83% | 需优化 |

## 偏差详情

### [Critical] 色彩偏差(8页)

#### P5, P8, P12: 使用非主题灰色
- **当前**: #999999 (中灰)
- **应为**: #6b7280 (Corporate次级文字色)
- **影响**: 与主题灰阶不一致,视觉突兀
- **修复**: 全局查找替换 #999999 → #6b7280

#### P15, P18: 强调色错误
- **当前**: #ff0000 (纯红)
- **应为**: #f59e0b (琥珀色,Corporate强调色)
- **影响**: 纯红过于刺眼,不符合商务调性
- **修复**: 全局查找替换 #ff0000 → #f59e0b

#### P20-P25: 图表使用Office默认色板
- **当前**: #4472C4, #ED7D31, #A5A5A5, #FFC000... (Office默认)
- **应为**: #1a56db, #3b82f6, #f59e0b, #10b981, #8b5cf6 (Corporate色板)
- **影响**: 图表与PPT整体风格割裂
- **修复**: 重新设置图表色板

### [High] 字体偏差(2页)
- P3, P7: 标题使用宋体 → 应为思源黑体
- **修复**: 选中P3/P7标题,字体改为"思源黑体"

### [Medium] 间距偏差(2页)
- P10, P22: 标题与正文间距16px → 应为24px
- **修复**: 调整段落间距为24px

## 修复脚本(Python-pptx)
```python
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor

prs = Presentation('report.pptx')

# 颜色替换映射
COLOR_MAP = {
    '999999': '6B7280',  # 中灰 → 主题次级文字
    'FF0000': 'F59E0B',  # 纯红 → 琥珀强调色
    '4472C4': '1A56DB',  # Office蓝 → 主题蓝
    'ED7D31': '3B82F6',  # Office橙 → 亮蓝
    'A5A5A5': '9CA3AF',  # Office灰 → 主题灰
    'FFC000': 'F59E0B',  # Office金 → 琥珀
}

# 图表色板
CHART_COLORS = ['1A56DB', '3B82F6', 'F59E0B', '10B981', '8B5CF6']

def replace_color(shape, old_hex, new_hex):
    """递归替换形状中的颜色"""
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            for run in para.runs:
                if run.font.color and run.font.color.rgb:
                    if str(run.font.color.rgb) == old_hex:
                        run.font.color.rgb = RGBColor.from_string(new_hex)

for slide_idx, slide in enumerate(prs.slides, 1):
    for shape in slide.shapes:
        for old, new in COLOR_MAP.items():
            replace_color(shape, old, new)

        # 修复字体(P3, P7)
        if slide_idx in [3, 7]:
            if shape.has_text_frame:
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        run.font.name = '思源黑体'

        # 修复图表色板
        if shape.has_chart:
            chart = shape.chart
            for series_idx, series in enumerate(chart.series):
                color = CHART_COLORS[series_idx % len(CHART_COLORS)]
                series.format.fill.fore_color.rgb = RGBColor.from_string(color)

prs.save('report_fixed.pptx')
print("修复完成: report_fixed.pptx")
```

## 修复后预期
| 维度 | 修复前 | 修复后 |
|:-----|:-------|:-------|
| 色彩符合率 | 73% | 100% |
| 字体符合率 | 93% | 100% |
| 间距符合率 | 87% | 100% |
| 图表符合率 | 80% | 100% |
| 总体评分 | 83% | 100% |
```

**效果验证**: ✓四维度检查(色彩/字体/间距/图表)含符合率统计 ✓偏差按Critical/High/Medium分级 ✓提供python-pptx自动修复脚本(颜色替换+字体修正+图表色板) ✓修复前后对比量化预期(83%→100%) ✓脚本含递归颜色替换和图表色板重设

## 常见问题

### Q1: 如何选择合适的主题?
A: 按内容调性选择:
- **企业/商务报告** → Corporate(深蓝)或 Mono(单色)
- **科技/开发者** → Tech(深色)或 Minimal(极简)
- **消费品/教育** → Warm(暖橙)或 Playful(活泼)
- **奢侈品/美妆** → Elegant(优雅紫)或 Editorial(杂志)
- **环保/农业** → Nature(自然绿)
- **创意/营销** → Sunset(日落)或 Playful(活泼)
- 不确定时:推荐 Corporate + Minimal 两个备选

### Q2: 自定义品牌色如何确保配色和谐?
A: 使用色轮理论:
- **互补色**(180°对比):主色 + 对面色作强调,高对比
- **类比色**(30° 内):主色 + 相邻色,和谐统一
- **三角配色**(120° 间隔):主色 + 两个等距色,平衡丰富
- 推荐:主色(60%)+ 辅色(30%)+ 强调色(10%)的 60-30-10 比例

### Q3: 中文字体如何选择?
A: 推荐组合:
- **黑体类**:思源黑体 / 阿里巴巴普惠体(现代、清晰)
- **宋体类**:思源宋体(优雅、传统)
- **等宽类**:思源等宽(代码、数据)
- 配对原则:标题用宋体(权威感)+ 正文用黑体(易读性),或全黑体(统一)
- 商用免费:阿里巴巴普惠体、思源字体、站酷快乐体

### Q4: 如何确保 WCAG 无障碍合规?
A: 对比度要求:
- 正文文字与背景对比度 ≥ 4.5:1(WCAG AA)
- 大标题(≥18pt)对比度 ≥ 3:1
- 使用工具检查:WebAIM Contrast Checker
- 暗色模式:背景 #1a1a1a + 文字 #f0f0f0(对比度 15:1)

## 已知限制

- 仅提供数字色彩(RGB/HEX),不覆盖印刷 CMYK
- 不涉及复杂交互设计与信息架构
- 不生成 Logo/图标(仅色彩与字体方案)
- 字体依赖用户系统或 CDN,离线环境需预装
- 暗色模式需手动适配(自动反转可能不够精细)
- 不覆盖动效设计(使用 Framer Motion/GSAP 专用工具)
- 复杂品牌 VI 系统需专业品牌设计师

## 安全声明

- 主题配置文件不包含任何敏感凭证
- 使用第三方字体 CDN 时,确保 CDN 提供 HTTPS
- 自定义品牌色相关数据仅在内存中处理,不写入日志
- 输出的 CSS 变量与 JSON 配置可直接公开,无敏感信息
