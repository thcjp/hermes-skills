---
slug: "minimalist-design"
name: "minimalist-design"
version: 1.0.1
displayName: "极简设计系统专业版"
summary: "企业级极简设计系统解决方案,支持完整组件库、多主题切换、设计审计与CI/CD集成,适合团队与商业项目"
license: "Proprietary"
edition: "pro"
description: |-
  极简设计系统专业版为企业与专业团队提供系统化的极简现代主义设计系统解决方案。在免费版核心设计令牌之上,增加完整组件库、多主题切换、设计系统文档自动生成、
  设计审计与CI/CD集成能力。
tags:
  - 设计系统
  - 企业级
  - 组件库
  - 多主题
  - CI/CD
  - 前端开发
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 极简设计系统专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 核心能力

### 完整企业级组件库
```python
component_library = {
    "buttons": ["primary", "secondary", "ghost", "icon", "fab", "loading"],
    "cards": ["basic", "media", "interactive", "pricing", "testimonial", "feature"],
    "forms": ["input", "textarea", "select", "checkbox", "radio", "toggle", "slider", "datepicker"],
    "navigation": ["breadcrumb", "pagination", "tabs", "stepper", "navbar", "sidebar"],
    "feedback": ["alert", "toast", "modal", "dialog", "progress", "skeleton", "spinner"],
    "data_display": ["table", "timeline", "accordion", "badge", "chip", "avatar", "tooltip"],
    "layout": ["container", "grid", "stack", "divider", "spacer"],
    "overlay": ["dropdown", "popover", "context-menu", "drawer"]
}
# .
python3 generate_components.py \
  --config components.yml \
  --output ./components/ \
  --with-docs \
  --with-tests \
  --with-stories
```- 验证返回数据的完整性和格式正确性
- 参考`完整企业级组件库`的配置文档进行参数调优
### 多主题系统
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供多主题系统所需的指令和必要参数。
**处理**: 解析多主题系统的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回多主题系统的处理结果,包含执行状态码、结果数据和执行日志。### 设计令牌多平台导出
```python
export_config = {
    "source": "design-tokens.yml",
    "formats": [
        {"name": "css_variables", "output": "tokens.css"},
        {"name": "tailwind_config", "output": "tailwind.config.js"},
        {"name": "figma_tokens", "output": "figma-tokens.json"},
        {"name": "scss_variables", "output": "_tokens.scss"},
        {"name": "json", "output": "tokens.json"},
        {"name": "android_xml", "output": "colors.xml"},
        {"name": "ios_swift", "output": "Tokens.swift"}
    ]
}
# .
python3 export_tokens.py --config export_config
```

### 设计系统文档自动生成
```python
doc_config = {
    "sections": [
        {"name": "设计原则", "source": "principles.md"},
        {"name": "色彩系统", "source": "colors.yml", "auto_examples": True},
        {"name": "字体系统", "source": "typography.yml", "auto_examples": True},
        {"name": "间距系统", "source": "spacing.yml", "auto_examples": True},
        {"name": "阴影系统", "source": "shadows.yml", "auto_examples": True},
        {"name": "组件库", "source": "components/", "auto_docs": True},
        {"name": "使用规范", "source": "guidelines.md"},
        {"name": "代码示例", "source": "examples/", "auto_extract": True}
    ],
    "output_formats": ["html", "markdown", "pdf"],
    "interactive": True,
    "searchable": True
}
```

**输入**: 用户提供设计系统文档自动生成所需的指令和必要参数。
**处理**: 解析设计系统文档自动生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 视觉一致性审计
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供视觉一致性审计所需的指令和必要参数。
**处理**: 解析视觉一致性审计的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回视觉一致性审计的处理结果,包含执行状态码、结果数据和执行日志。### Framer Motion高级动效
```javascript
// 高级动效系统
const motionSystem = {
  presets: {
    fadeIn: {
      initial: { opacity: 0 },
      animate: { opacity: 1 },
      exit: { opacity: 0 }
    },
    slideUp: {
      initial: { y: 20, opacity: 0 },
      animate: { y: 0, opacity: 1 },
      exit: { y: -20, opacity: 0 }
    },
    scale: {
      initial: { scale: 0.95, opacity: 0 },
      animate: { scale: 1, opacity: 1 },
      exit: { scale: 0.95, opacity: 0 }
    },
    stagger: {
      animate: {
        transition: { staggerChildren: 0.1 }
      }
    }
  },
  defaults: {
    duration: 0.7,
    ease: [0.16, 1, 0.3, 1]
  },
  reduced_motion: {
    respect: True,
    fallback: { duration: 0.01 }
  }
};
```

**输入**: 用户提供Framer Motion高级动效所需的指令和必要参数。
**处理**: 解析Framer Motion高级动效的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回Framer Motion高级动效的处理结果,包含执行状态码、结果数据和执行日志。

#
## 适用场景

### 场景一:企业SaaS设计系统
需求:为SaaS公司建立完整的设计系统,覆盖所有产品。

```bash
python3 init_design_system.py \
  --name "EnterpriseDS" \
  --version "2.0.0" \
  --themes "light,dark,brand" \
  --output ./design-system/
# .
python3 generate_components.py \
  --config components.yml \
  --output ./design-system/components/ \
  --with-docs \
  --with-tests \
  --with-stories
# .
python3 export_tokens.py \
  --source design-tokens.yml \
  --formats "css,tailwind,figma,scss,json"
# .
python3 generate_docs.py \
  --config doc-config.yml \
  --output ./design-system/docs/
```

输出结构:

```
design-system/
├── tokens/
│   ├── tokens.css
│   ├── tailwind.config.js
│   ├── figma-tokens.json
│   └── _tokens.scss
├── components/
│   ├── buttons/
│   ├── cards/
│   ├── forms/
│   ├── navigation/
│   └── feedback/
├── themes/
│   ├── light.css
│   ├── dark.css
│   └── brand.css
├── docs/
│   ├── index.html
│   ├── principles.md
│   └── component-api.md
├── audit/
│   └── consistency-report.html
└── motion/
    └── motion-presets.js
```

### 场景二:多品牌设计系统管理
需求:集团企业需要为多个子品牌统一管理设计系统。

```python
brands = {
    "brand_a": {
        "name": "品牌A",
        "theme": {"accent": "#0052FF", "bg": "#FAFAFA"},
        "fonts": {"display": "Inter", "body": "Inter"},
        "components": "inherit_base"
    },
    "brand_b": {
        "name": "品牌B",
        "theme": {"accent": "#E67E22", "bg": "#FFF8F0"},
        "fonts": {"display": "Playfair Display", "body": "Source Sans Pro"},
        "components": "custom_override"
    }
}
# .
for brand_id, config in brands.items():
    generate_brand_package(brand_id, config)
```

### 场景三:设计到开发自动化交付
需求:设计团队更新令牌后,自动同步到代码库。

```yaml
name: Design System Sync
on:
  push:
    paths: ["design-tokens.yml"]
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Export Tokens
        run: |
          python3 export_tokens.py \
            --source design-tokens.yml \
            --formats "css,tailwind,figma"
      - name: Generate Components
        run: |
          python3 generate_components.py \
            --config components.yml \
            --output ./src/components/
      - name: Audit Design
        run: |
          python3 audit_design.py \
            --scan ./src/ \
            --report ./audit/
      - name: Generate Docs
        run: |
          python3 generate_docs.py \
            --output ./docs/
```

## 使用流程

### 步骤一:初始化设计系统
```bash
python3 init_design_system.py \
  --name "MyDesignSystem" \
  --base-theme "light" \
  --output ./design-system/
```

### 步骤二:生成组件库
```bash
python3 generate_components.py \
  --config components.yml \
  --output ./design-system/components/ \
  --with-docs \
  --with-tests
```

### 步骤三:审计与文档
```bash
python3 audit_design.py --scan ./src/ --report ./audit/
# .
python3 generate_docs.py --output ./docs/
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | minimalist-design处理的内容输入 |,  |
| content | string | 否 | minimalist-design处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "design 相关配置参数",
    result: "design 相关配置参数",
    result: "design 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
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
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md规范的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+(用于组件库构建)
- **Python**: 3.10+(用于令牌导出与审计)

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Tailwind CSS | 构建工具 | 推荐 | npm install tailwindcss |
| Framer Motion | 动效库 | 可选 | npm install framer-motion |
| Lucide React | 图标库 | 可选 | npm install lucide-react |
| Storybook | 组件文档 | 推荐 | npm install storybook |

### API Key 配置
- 本Skill基于指令驱动驱动,无需额外API Key
- 设计令牌与组件库为本地生成,无需云端服务
- 如集成Figma,需配置Figma API Token

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令+脚本执行能力)
- **说明**: 专业版基于Markdown指令驱动Agent执行设计系统构建任务,通过Python/Node.js脚本实现组件生成、令牌导出与CI/CD集成
- **PRO版增强**: 完整组件库、多主题系统、文档生成、设计审计、多平台导出、CI/CD集成、团队协作

## 案例展示

### 企业级设计令牌

> 详细代码示例已移至 `references/detail.md`

### 组件生成配置
```yaml
components:
  buttons:
    variants: [primary, secondary, ghost, icon, fab]
    sizes: [sm, md, lg]
    states: [default, hover, active, disabled, loading]
# .
  cards:
    types: [basic, media, interactive, pricing, testimonial]
    features: [hover_effect, gradient_border, shadow_glow]
# .
  forms:
    inputs: [text, email, password, search, number]
    selects: [single, multi, searchable]
    feedback: [error, success, warning]
```

## 常见问题

### Q1: 如何从免费版迁移至PRO版?
A: PRO版完全兼容免费版。现有的Tailwind配置与设计令牌可直接使用。运行迁移脚本升级为完整设计系统。

### Q2: 组件库支持哪些框架?
A: 默认生成React组件,同时支持Vue、Svelte、Angular等框架。可根据项目技术栈选择对应格式。

### Q3: 多主题如何实现?
A: 使用CSS Variables实现主题切换。所有颜色令牌导出为CSS变量,通过切换变量值实现主题切换,无需重新渲染组件。

### Q4: 设计审计能检测哪些问题?
A: 可检测:硬编码颜色、非标准字体、非标尺间距、自定义组件(未使用组件库)、可访问性违规等。生成HTML报告并提供修复建议。

### Q5: 如何集成到CI/CD?
A: 提供标准CLI接口与配置文件。设计令牌变更时自动导出多平台格式、重新生成组件、执行审计并部署文档。

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

