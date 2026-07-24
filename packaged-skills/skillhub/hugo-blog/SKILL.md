---
slug: "hugo-blog"
name: "hugo-blog"
version: 1.0.1
displayName: "Hugo博客发布专业版"
summary: "企业级 Hugo 博客管理方案，支持批量发布、多语言站点、SEO 优化与 CI/CD 集成。。面向专业博主的 Hugo 博客管理工具，提供批量发布与站点级管理能力。核心能力: - 批量文章发"
license: "Proprietary"
edition: "pro"
description: |-
  面向专业博主的 Hugo 博客管理工具，提供批量发布与站点级管理能力。核心能力:
  - 批量文章发布与定时发布调度
  - 多语言站点（i18n）内容管理
  - SEO 优化（结构化数据、站点地图、元信息）
  - CI/CD 自动化部署集成
  - 文章系列管理与交叉引用
  - 图片资源自动优化与 CDN 集成

  适用场景:
  - 多作者博客团队的协作发布
  - 多语言博客站点的同步管理
  - SEO 优化的技术博客运营
  - 自动化部署的持续发布流程

  差异化: 专业版兼容免费版所有发布能力...
tags:
  - 开发工具
  - 博客
  - Hugo
  - 内容运营
  - SEO
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Hugo博客发布专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Hugo博客发布专业版博客管理 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
|:-----|:-----|:-----|
| 文章发布 | 单篇发布 | 批量发布 + 定时调度 |
| Front Matter | 基础字段 | SEO 元信息 + 结构化数据 |
| 标签管理 | 英文 slug 映射 | 多语言标签 + 标签云生成 |
| 图片处理 | - | 自动压缩 + CDN 集成 |
| 部署 | Git 推送 | CI/CD 自动化部署 |
| 多语言 | - | i18n 多语言站点管理 |
| 内容组织 | - | 文章系列 + 交叉引用 |
| 性能 | - | 站点性能优化与监控 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 文章发布

针对文章,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供文章发布相关的配置参数、输入数据和处理选项.
**输出**: 返回文章发布的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`文章发布`的配置文档进行参数调优
### Front Matter

针对Front Matter,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Front Matter相关的配置参数、输入数据和处理选项.
**输出**: 返回Front Matter的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Front Matter`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：批量发布文章系列
团队需要一次性发布一个包含 5 篇文章的技术系列.
```bash
#!/bin/bash
SERIES_NAME="go-concurrency-series"
BLOG_DIR="${BLOG_DIR:-~/blog}"
POSTS_DIR="$BLOG_DIR/content/posts"
# ...
echo "=== 批量发布系列：$SERIES_NAME ==="
# ...
declare -a POSTS=(
  "go-goroutine-basics"
  "go-channel-patterns"
  "go-context-usage"
  "go-worker-pool"
  "go-concurrency-best-practices"
)
# ...
for i in "${!POSTS[@]}"; do
  SLUG="${POSTS[$i]}"
  CHAPTER=$((i + 1))
# ...
  cat > "$POSTS_DIR/$SLUG.md" << FRONTMATTER
title: "$(echo $SLUG | tr '-' ' ' | sed 's/\b\(.\)/\u\1/g')"
date: 2026-07-18
draft: false
tags: ["go", "programming", "concurrency"]
categories: ["tech"]
series: ["$SERIES_NAME"]
series_weight: $CHAPTER
description: "Go 并发编程系列第 $CHAPTER 篇"
aliases:
  - /posts/$SERIES_NAME-$CHAPTER/
FRONTMATTER
# ...
  echo "  [$CHAPTER/${#POSTS[@]}] $SLUG 已准备"
done
# ...
cd "$BLOG_DIR"
git add content/posts/
git commit -m "新增：Go 并发编程系列（5 篇）"
git push
# ...
echo "=== 系列发布完成 ==="
```

### 场景二：多语言站点管理
博客需要同时维护中文和英文版本.
```bash
cat > hugo.toml << 'EOF'
defaultContentLanguage = "zh"
defaultContentLanguageInSubdir = true
# ...
[languages]
  [languages.zh]
    weight = 1
    title = "技术博客"
    languageName = "中文"
  [languages.en]
    weight = 2
    title = "Tech Blog"
    languageName = "English"
# ...
EOF
# ...
create_bilingual_post() {
  local slug=$1
  local zh_title=$2
  local en_title=$3
# ...
  mkdir -p "content/zh/posts/$slug"
  mkdir -p "content/en/posts/$slug"
# ...
  cat > "content/zh/posts/$slug/_index.md" << EOF
title: "$zh_title"
date: 2026-07-18
draft: false
tags: ["tech"]
EOF
# ...
  cat > "content/en/posts/$slug/_index.md" << EOF
title: "$en_title"
date: 2026-07-18
draft: false
tags: ["tech"]
EOF
}
```

### 场景三：CI/CD 自动化部署
博客需要通过 CI/CD 实现推送即部署.
```yaml
name: 部署博客
on:
  push:
    branches: [main]
    paths:
      - 'content/**'
      - 'static/**'
      - 'hugo.toml'
# ...
jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: 检出代码
        uses: actions/checkout@v4
        with:
          submodules: true
# ...
      - name: 安装 Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true
# ...
      - name: 安装图片优化工具
        run: |
          sudo apt-get install -y jpegoptim optipng
          npm install -g imagemin-cli
# ...
      - name: 优化图片
        run: |
          find static/images -name "*.jpg" -exec jpegoptim --max=80 {} \;
          find static/images -name "*.png" -exec optipng -o7 {} \;
# ...
      - name: 构建站点
        run: hugo --minify --gc
# ...
      - name: 生成站点地图
        run: hugo --renderToMemory --templateMetrics
# ...
      - name: 部署到 GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: $相关信息
          publish_dir: ./public
# ...
      - name: 通知部署结果
        if: always()
        uses: slackapi/slack-github-action@v1
        with:
          slack-message: "博客部署 $相关信息"
        env:
          SLACK_WEBHOOK_URL: $相关信息
```

## 使用流程

### SEO 优化 Front Matter
```yaml
title: "Go 并发编程完全指南"
date: 2026-07-18
lastmod: 2026-07-19
draft: false
description: "深入讲解 Go 语言并发编程，涵盖 goroutine、channel、context 等核心概念"
tags: ["go", "programming", "concurrency"]
categories: ["tech"]
series: ["go-concurrency"]
series_weight: 1
# ...
keywords: ["Go 并发", "goroutine", "channel", "Go 教程"]
# ...
images:
  - /images/go-concurrency-cover.png
# ...
schema:
  type: "TechArticle"
  author:
    name: "作者名"
  publisher:
    name: "博客名称"
# ...
aliases:
  - /posts/go-concurrency-guide/
  - /posts/2025/go-concurrency/
# ...
readingTime: true
toc: true
```

### 图片优化脚本
```bash
#!/bin/bash
IMAGE_DIR="static/images"
# ...
echo "=== 图片优化 ==="
# ...
find "$IMAGE_DIR" -name "*.jpg" -o -name "*.jpeg" | while read f; do
  jpegoptim --max=80 --strip-all "$f"
  echo "  优化: $f"
done
# ...
find "$IMAGE_DIR" -name "*.png" | while read f; do
  optipng -o7 "$f"
  echo "  优化: $f"
done
# ...
find "$IMAGE_DIR" -name "*.jpg" -o -name "*.png" | while read f; do
  cwebp -q 80 "$f" -o "${f%.*}.webp"
  echo "  WebP: ${f%.*}.webp"
done
# ...
find "$IMAGE_DIR" -name "*.jpg" | while read f; do
  convert "$f" -resize 300x300^ -gravity center -extent 300x300 "${f%.*}-thumb.jpg"
  echo "  缩略图: ${f%.*}-thumb.jpg"
done
# ...
echo "=== 优化完成 ==="
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | hugo-blog处理的内容输入 |,  |
| content | string | 否 | hugo-blog处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "blog 相关配置参数",
    result: "blog 相关配置参数",
    result: "blog 相关配置参数",
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
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Hugo 版本**: 建议 0.110 及以上（扩展版）
- **CI/CD 平台**: GitHub Actions / GitLab CI 等

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Hugo | 静态站点生成器 | 必需 | gohugo.io 下载（扩展版） |
| Git | 命令行工具 | 必需 | 系统包管理器安装 |
| jpegoptim | 图片优化 | 推荐 | `apt install jpegoptim` |
| optipng | 图片优化 | 推荐 | `apt install optipng` |
| cwebp | WebP 生成 | 可选 | `apt install webp` |
| ImageMagick | 缩略图 | 可选 | `apt install imagemagick` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- Git 推送需要配置 SSH Key 或个人访问令牌
- CI/CD 部署需要在平台配置对应的访问令牌
- CDN 集成需要配置 CDN 服务的访问密钥

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 执行博客管理流程，专业版功能依赖 Hugo CLI、图片优化工具和 CI/CD 平台

## 案例展示

### 文章系列配置
```yaml
title: "Go 并发基础"
series: ["go-concurrency"]
series_weight: 1
title: "Go Channel 模式"
series: ["go-concurrency"]
series_weight: 2
相关信息
相关信息
  相关信息
  <nav class="series-nav">
    <h3>系列文章</h3>
    相关信息
      相关信息
        <a href="相关信息">上一篇：hugo-blog</a>
      相关信息
    相关信息
    相关信息
      相关信息
        <a href="相关信息">下一篇：hugo-blog</a>
      相关信息
    相关信息
  </nav>
相关信息
```

### 站点性能优化配置
```toml
[minify]
  minifyOutput = true
  disableHTML = false
  disableCSS = false
  disableJS = false
  disableJSON = false
  disableSVG = false
  disableXML = false
# ...
[build]
  writeStats = true
# ...
[imaging]
  quality = 75
  resampleFilter = "Lanczos"
  hint = "photo"
# ...
[markup.goldmark.renderer]
  unsafe = true
```

## 常见问题

### Q1：如何实现定时发布？
```bash
title: "定时发布文章"
date: 2026-12-25
draft: false
on:
  schedule:
    - cron: '0 0 * * *'  # 每天 UTC 0点
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 构建并部署
        run: hugo --minify && （请参考skill目录中的脚本文件）
```

### Q2：多语言站点的标签如何管理？
```bash
title: "Go 语言"
title: "Go"
```

### Q3：如何处理文章的交叉引用？
```markdown
<!-- 使用 ref 短码引用其他文章 -->
相关信息
# ...
<!-- 多语言引用 -->
相关信息
# ...
<!-- 系列内引用 -->
参见 [本系列优秀篇](相关信息)
```

### Q4：如何生成站点地图？
```bash
hugo --minify
# ...
[sitemap]
  changeFreq = "weekly"
  priority = 0.5
  filename = "sitemap.xml"
```

### Q5：如何集成 CDN？
```toml
[params]
  cdnURL = "https://cdn.example.com"
# ...
<img src="相关信息/images/相关信息">
```

### Q6：如何统计文章字数和阅读时间？
```html
<!-- layouts/partials/reading-time.html -->
相关信息
相关信息
<span class="reading-time">
  相关信息 字 · 约 相关信息 分钟
</span>
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

