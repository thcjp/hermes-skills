---
slug: ui-ux-dev-tool-pro
name: ui-ux-dev-tool-pro
version: "1.0.0"
displayName: UI/UX开发工具专业版
summary: 多页面React项目生成+设计系统持久化+批量截图+Zip导出,面向团队的专业页面开发引擎
license: MIT
edition: pro
description: |-
  面向开发团队和代理机构的专业级React页面生成引擎,支持多页面项目管理、
  设计系统持久化、自动化截图审查循环、批量图片处理和Zip打包导出。

  核心能力:
  - 多页面项目管理与配置持久化
  - 设计系统引用与跨页面一致性保障
  - 自动化多分辨率截图审查(桌面/平板/移动)
  - 批量图片WebP转换与优化报告
  - Zip打包导出与独立部署支持
  - 企业级设计原则自动应用与质量门禁
  - 组件化React开发与状态管理

  适用场景:
  - 代理机构多客户多页面项目交付
  - 企业多页面Web应用快速开发
  - 设计系统驱动的批量页面生成
  - 自动化视觉质量保障流程

  差异化:专业版在免费版基础上扩展至多页面项目管理、设计系统持久化、
  自动化截图循环和批量导出。完全兼容免费版单页面生成流程,可无缝升级。

  触发关键词: 多页面项目, 设计系统持久化, 批量截图审查, Zip导出, 自动化审查, 企业页面开发, 组件化React, 状态管理, 质量门禁, 项目交付
tags:
- 设计
- UI
- UX
- React
- 前端
- 原型
- 开发
- 企业级
- 项目管理
- 批量处理
tools:
- read
- exec
---

# UI/UX开发工具 - 专业版

## 概述

UI/UX开发工具专业版是一款面向开发团队和代理机构的专业级React页面生成引擎。在免费版单页面生成能力之上,扩展至多页面项目管理、设计系统持久化引用、自动化多分辨率截图审查循环、批量图片处理和Zip打包导出。

专业版保障跨页面设计一致性,支持自动化视觉质量门禁,是代理机构多客户交付和企业多页面应用的理想选择。完全兼容免费版单页面生成流程,可无缝升级。

## 核心能力

### 1. 多页面项目管理

支持完整的多页面项目结构,每个项目独立管理配置和设计系统:

```text
serve/
├── client-a/
│   ├── project.json              # 项目配置+设计系统引用
│   ├── assets/
│   │   ├── logo.webp
│   │   ├── hero-banner.webp
│   │   └── team-photos/
│   │       ├── member-1.webp
│   │       └── member-2.webp
│   ├── landing/index.html        # 落地页
│   ├── about/index.html          # 关于我们
│   ├── pricing/index.html        # 定价方案
│   ├── contact/index.html        # 联系我们
│   └── dashboard/index.html      # 用户仪表盘
├── client-b/
│   ├── project.json
│   ├── assets/
│   └── landing/index.html
```

### 2. 设计系统持久化与引用

项目配置中引用设计系统,保障跨页面一致性:

```json
{
  "name": "enterprise-app",
  "version": "2.0.0",
  "preferences": {
    "style": "professional",
    "font": "Inter",
    "primary_color": "#2563EB",
    "dark_mode": true
  },
  "design_system": {
    "reference": "design-system/MASTER.md",
    "max_width": "max-w-7xl",
    "spacing_scale": "tailwind-default",
    "border_radius": "rounded-xl",
    "color_tokens": {
      "primary": "#2563EB",
      "secondary": "#64748B",
      "accent": "#22D3EE",
      "background": "#0F172A",
      "surface": "#1E293B",
      "text_primary": "#F8FAFC",
      "text_secondary": "#CBD5E1"
    }
  },
  "pages": [
    {"slug": "landing", "title": "首页", "status": "completed"},
    {"slug": "pricing", "title": "定价", "status": "completed"},
    {"slug": "dashboard", "title": "仪表盘", "status": "in-progress"},
    {"slug": "settings", "title": "设置", "status": "pending"}
  ]
}
```

### 3. 自动化多分辨率截图审查

专业版支持自动化多分辨率截图,全面覆盖各设备尺寸:

```bash
# 桌面端审查(1920x1080)
bash scripts/screenshot.sh "http://localhost:5174/project/page/" /tmp/desktop-full.png 1920 1080

# 标准桌面(1440x900)
bash scripts/screenshot.sh "http://localhost:5174/project/page/" /tmp/desktop.png 1440 900

# 平板横屏(1024x768)
bash scripts/screenshot.sh "http://localhost:5174/project/page/" /tmp/tablet.png 1024 768

# 平板竖屏(768x1024)
bash scripts/screenshot.sh "http://localhost:5174/project/page/" /tmp/tablet-portrait.png 768 1024

# 大屏手机(390x844)
bash scripts/screenshot.sh "http://localhost:5174/project/page/" /tmp/mobile.png 390 844

# 小屏手机(320x568)
bash scripts/screenshot.sh "http://localhost:5174/project/page/" /tmp/mobile-small.png 320 568
```

### 4. 批量截图审查脚本

```bash
#!/bin/bash
# batch-screenshot.sh - 批量截图所有页面所有分辨率
PROJECT=$1
BASE_URL="http://localhost:5174/${PROJECT}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="/tmp/reviews/${PROJECT}_${TIMESTAMP}"

mkdir -p "$OUTPUT_DIR"

PAGES=("landing" "about" "pricing" "contact" "dashboard")
RESOLUTIONS=("1920x1080" "1440x900" "768x1024" "390x844")

for page in "${PAGES[@]}"; do
  for res in "${RESOLUTIONS[@]}"; do
    width=$(echo $res | cut -d'x' -f1)
    height=$(echo $res | cut -d'x' -f2)
    output="${OUTPUT_DIR}/${page}_${res}.png"
    bash scripts/screenshot.sh "${BASE_URL}/${page}/" "$output" "$width" "$height"
    echo "截图完成: ${page} @ ${res}"
  done
done

echo "批量截图完成,输出目录: ${OUTPUT_DIR}"
```

### 5. 批量图片转换与优化报告

```bash
#!/bin/bash
# batch-convert-images.sh - 批量转换图片为WebP
INPUT_DIR=$1
QUALITY=${2:-80}

total_before=0
total_after=0
count=0

for img in "$INPUT_DIR"/*.{png,jpg,jpeg}; do
  if [ -f "$img" ]; then
    filename=$(basename "$img" | sed 's/\.[^.]*$//')
    output="$INPUT_DIR/${filename}.webp"

    before_size=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img")
    bash scripts/convert-image.sh "$img" "$output" "$QUALITY"
    after_size=$(stat -f%z "$output" 2>/dev/null || stat -c%s "$output")

    reduction=$((100 - (after_size * 100 / before_size)))
    total_before=$((total_before + before_size))
    total_after=$((total_after + after_size))
    count=$((count + 1))

    echo "转换: $(basename $img) -> ${filename}.webp"
    echo "  大小: $(numfmt --to=iec $before_size) -> $(numfmt --to=iec $after_size) (减少${reduction}%)"
  fi
done

echo ""
echo "=== 批量转换报告 ==="
echo "处理文件数: ${count}"
echo "原始总大小: $(numfmt --to=iec $total_before)"
echo "转换后大小: $(numfmt --to=iec $total_after)"
echo "总节省: $(numfmt --to=iec $((total_before - total_after)))"
```

### 6. Zip打包导出

```bash
# 导出整个项目为Zip
cd serve && zip -r /tmp/enterprise-app.zip enterprise-app/

# 导出时排除临时文件
cd serve && zip -r /tmp/enterprise-app.zip enterprise-app/ \
  -x "*.DS_Store" "*/tmp/*" "*/.git/*"
```

## 使用场景

### 场景一:代理机构多客户项目交付

代理机构需要同时为3个客户开发各自的落地页,每个客户有独立的设计偏好。

```bash
# 客户A:科技公司,极简风格
# 1.创建项目
mkdir -p serve/client-a/{landing,assets}
# 2.配置项目
cat > serve/client-a/project.json << 'EOF'
{
  "name": "client-a",
  "preferences": {"style": "minimal", "font": "Inter", "primary_color": "#2563EB"},
  "design_system": {"max_width": "max-w-6xl", "border_radius": "rounded-lg"},
  "pages": [{"slug": "landing", "title": "首页", "status": "in-progress"}]
}
EOF
# 3.生成页面 -> 4.截图审查 -> 5.导出Zip

# 客户B:美妆品牌,优雅风格
mkdir -p serve/client-b/{landing,assets}
# ... 独立配置和生成

# 客户C:健身应用,活力风格
mkdir -p serve/client-c/{landing,assets}
# ... 独立配置和生成
```

### 场景二:企业多页面Web应用

一家企业需要开发包含5个页面的产品官网,要求设计一致性。

```bash
# 步骤1:创建项目并配置统一设计系统
mkdir -p serve/enterprise/{landing,features,pricing,about,contact,assets}

# 步骤2:批量生成所有页面(引用同一设计系统)
# 每个页面生成后自动截图审查

# 步骤3:批量截图审查所有页面
bash scripts/batch-screenshot.sh enterprise

# 步骤4:批量转换所有图片
bash scripts/batch-convert-images.sh serve/enterprise/assets 85

# 步骤5:导出项目Zip
cd serve && zip -r /tmp/enterprise.zip enterprise/
```

### 场景三:自动化视觉质量门禁

在CI/CD流程中集成自动化截图审查作为质量门禁:

```bash
#!/bin/bash
# quality-gate.sh - 视觉质量门禁检查
PROJECT=$1
ISSUES_FOUND=0

# 截图所有页面
bash scripts/batch-screenshot.sh "$PROJECT"

# 检查常见视觉问题
for screenshot in /tmp/reviews/${PROJECT}_*/*.png; do
  # Agent分析截图:布局错位、对比度、响应式问题
  # 如果发现问题,ISSUES_FOUND=$((ISSUES_FOUND + 1))
  echo "检查: $(basename $screenshot)"
done

if [ $ISSUES_FOUND -gt 0 ]; then
  echo "质量门禁未通过:发现 ${ISSUES_FOUND} 个问题"
  exit 1
else
  echo "质量门禁通过"
  exit 0
fi
```

## 快速开始

### 专业版项目初始化

```bash
# 第1步:启动本地服务
bash scripts/setup.sh 5174

# 第2步:创建多页面项目结构
PROJECT_NAME="my-enterprise-app"
mkdir -p serve/${PROJECT_NAME}/{landing,about,pricing,contact,assets}

# 第3步:创建项目配置(含设计系统)
cat > serve/${PROJECT_NAME}/project.json << 'EOF'
{
  "name": "my-enterprise-app",
  "version": "1.0.0",
  "preferences": {
    "style": "professional",
    "font": "Inter",
    "primary_color": "#2563EB",
    "dark_mode": false
  },
  "design_system": {
    "max_width": "max-w-7xl",
    "border_radius": "rounded-xl",
    "spacing_scale": "tailwind-default"
  },
  "pages": [
    {"slug": "landing", "title": "首页"},
    {"slug": "about", "title": "关于我们"},
    {"slug": "pricing", "title": "定价方案"},
    {"slug": "contact", "title": "联系我们"}
  ]
}
EOF

# 第4步:逐页生成并审查
# (Agent根据配置生成每个页面)

# 第5步:批量截图审查
bash scripts/batch-screenshot.sh ${PROJECT_NAME}

# 第6步:批量图片处理
bash scripts/batch-convert-images.sh serve/${PROJECT_NAME}/assets 85

# 第7步:导出Zip
cd serve && zip -r /tmp/${PROJECT_NAME}.zip ${PROJECT_NAME}/
```

## 配置示例

### 企业级React页面模板(CDN)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>企业应用 - 首页</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: { sans: ['Inter', 'system-ui', 'sans-serif'] },
          colors: {
            primary: { DEFAULT: '#2563EB', hover: '#1D4ED8' }
          }
        }
      }
    }
  </script>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
    const { useState, useEffect } = React;

    // 组件化开发
    function Navbar() {
      const [menuOpen, setMenuOpen] = useState(false);
      return (
        <header className="fixed top-4 left-4 right-4 z-50">
          <nav className="bg-white/80 backdrop-blur-md rounded-2xl shadow-lg px-6 py-4">
            <div className="flex items-center justify-between max-w-7xl mx-auto">
              <span className="text-xl font-bold text-slate-900">企业应用</span>
              <button className="md:hidden" onClick={() => setMenuOpen(!menuOpen)}>
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                    d={menuOpen ? "M6 18L18 6M6 6l12 12" : "M4 6h16M4 12h16M4 18h16"} />
                </svg>
              </button>
              <div className={`${menuOpen ? 'block' : 'hidden'} md:flex gap-6`}>
                <a href="/" className="text-slate-600 hover:text-primary cursor-pointer transition-colors">首页</a>
                <a href="/about" className="text-slate-600 hover:text-primary cursor-pointer transition-colors">关于</a>
                <a href="/pricing" className="text-slate-600 hover:text-primary cursor-pointer transition-colors">定价</a>
              </div>
            </div>
          </nav>
        </header>
      );
    }

    function App() {
      return (
        <div className="min-h-screen bg-slate-50">
          <Navbar />
          <main className="max-w-7xl mx-auto px-4 pt-32 pb-16">
            <h1 className="text-5xl font-bold text-slate-900 mb-6">企业级解决方案</h1>
          </main>
        </div>
      );
    }
    ReactDOM.createRoot(document.getElementById('root')).render(<App />);
  </script>
</body>
</html>
```

### 专业版与免费版完整对比

| 功能维度 | 免费版 | 专业版 |
|----------|--------|--------|
| 页面生成 | 单页面 | 多页面项目管理 |
| 项目配置 | 基础JSON | 设计系统持久化引用 |
| 截图审查 | 桌面+移动(2种) | 6种分辨率全覆盖 |
| 截图自动化 | 手动单次 | 批量脚本+CI集成 |
| 图片处理 | 单张WebP转换 | 批量转换+优化报告 |
| 导出 | 静态文件 | Zip打包+排除规则 |
| 设计系统 | 基础原则 | 跨页面一致性引用 |
| 质量保障 | 手动审查 | 自动化质量门禁 |
| 组件化 | 基础组件 | 完整组件+状态管理 |
| 多项目管理 | 单项目 | 多客户并行管理 |
| 适用对象 | 个人开发者 | 团队/代理机构 |
| 兼容性 | - | 完全兼容免费版流程 |

## 最佳实践

### 1. 设计系统跨页面一致性

所有页面引用同一设计系统配置,确保视觉一致:

```text
项目配置(project.json) -> 设计系统引用 -> 每个页面读取相同令牌
```

### 2. 迭代审查循环

```text
生成页面 -> 桌面截图 -> 分析问题 -> 修复 -> 重新截图
         -> 移动截图 -> 分析问题 -> 修复 -> 重新截图
         -> 平板截图 -> 分析问题 -> 修复 -> 重新截图
         -> 质量门禁通过 -> 交付
```

### 3. 每步操作告知用户

专业版要求更详细的操作日志:

```text
-> 正在读取项目配置 enterprise-app/project.json...
-> 发现4个页面:landing, about, pricing, contact
-> 正在生成 landing 页面...
-> landing 页面生成完成
-> 正在截图审查 landing(6种分辨率)...
-> 桌面1920x1080: 通过
-> 桌面1440x900: 发现导航栏遮挡内容,修复中...
-> 平板768x1024: 通过
-> 移动390x844: 发现按钮过小,修复中...
-> 修复完成,重新截图...
-> landing 页面质量门禁通过
-> 正在生成 about 页面...
```

### 4. 交付前质量检查矩阵

| 检查维度 | 分辨率 | 通过标准 |
|----------|--------|----------|
| 大屏桌面 | 1920x1080 | 布局完整,无溢出 |
| 标准桌面 | 1440x900 | 导航可用,内容居中 |
| 平板横屏 | 1024x768 | 网格适配,间距合理 |
| 平板竖屏 | 768x1024 | 单列布局,可读性 |
| 大屏手机 | 390x844 | 汉堡菜单,触摸达标 |
| 小屏手机 | 320x568 | 无溢出,文字可读 |

## 常见问题

### Q1: 专业版是否兼容免费版的单页面流程?

完全兼容。专业版支持免费版的所有操作,包括单页面生成、基础截图审查和WebP转换。专业版额外提供多页面管理、批量操作和导出功能。

### Q2: 如何管理多个客户项目?

每个客户项目使用独立目录(serve/client-a/, serve/client-b/),各自维护project.json配置和设计系统。通过批量脚本可一次性截图审查所有项目。

### Q3: 自动化截图审查如何集成到CI/CD?

将quality-gate.sh脚本集成到CI/CD流水线中,在代码提交后自动运行截图审查。如果发现视觉问题,CI流程失败并报告问题详情。

### Q4: Zip导出的页面可以独立部署吗?

可以。CDN方式的React页面是独立HTML文件,Zip解压后可通过任意静态服务器(Nginx/Apache/CDN)部署,无需构建步骤。

### Q5: 设计系统如何在团队中共享?

将project.json中的设计系统配置纳入版本控制(Git),团队成员克隆仓库后即可使用相同的设计令牌和偏好设置,确保所有人生成的页面视觉一致。

### Q6: 批量图片转换支持哪些格式?

支持PNG、JPG、JPEG转WebP。转换后自动生成优化报告,包括每张文件的原始大小、转换后大小和压缩比例。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **浏览器**: Chrome/Chromium(用于截图审查)
- **本地服务器**: Python http.server或Node.js静态服务器
- **Bash**: 批量脚本执行(Windows需Git Bash或WSL)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Bash | 运行时 | 必需 | 系统内置或Git Bash |
| Chrome/Chromium | 截图工具 | 必需 | 浏览器安装 |
| cwebp | 图片转换 | 必需 | libwebp工具包 |
| zip | 打包工具 | 必需 | 系统内置 |
| numfmt | 报告格式化 | 推荐 | coreutils(GNU) |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| CDN资源 | 前端库 | 必需 | 自动从CDN加载 |

安装依赖:

```bash
# macOS
brew install webp

# Ubuntu/Debian
sudo apt install webp zip coreutils

# Windows(Git Bash环境)
# 安装Git for Windows(包含bash)
# 下载libwebp并添加到PATH
```

### API Key 配置

本Skill基于Markdown指令和本地脚本运行,无需额外API Key。页面生成由Agent内置LLM驱动,截图、图片转换和打包均为本地工具执行。CDN前端库通过公网加载,无需配置。

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务。多页面管理、批量截图、图片转换和Zip导出均依赖exec工具执行Bash脚本。自动化质量门禁可集成到CI/CD流水线,需确保Bash和Chrome/Chromium环境可用。
