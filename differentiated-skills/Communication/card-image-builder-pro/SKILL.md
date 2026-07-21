---
slug: card-image-builder-pro
name: card-image-builder-pro
version: "1.0.0"
displayName: 卡片图生成器-专业版
summary: 企业级卡片图生成平台,支持全模板/批量生成/自定义模板/品牌定制/X长图
license: Proprietary
edition: pro
description: |-
  卡片图生成器专业版,面向企业和专业内容团队的全功能卡片图片生成平台。核心能力:
  - 全模板支持(海报/长文卡片/X风格长图/公众号封面/自定义模板)
  - X/Twitter风格帖子分享长图生成
  - 批量生成与目录递归处理
  - 自定义模板创建与管理
  - 全平台配色预设与品牌定制
  - 高级高亮(整行+按词+组合高亮)
  - 水印与版权信息嵌入
  - 模板版本管理与团队共享

  适用场景:
  - 企业社交媒体内容矩阵的配图生产
  - 内容团队的批量卡片图生成
  - X/Twitter帖子分享长图制作
  - 品牌统一的...
tags:
- 沟通协作
- 图片生成
- 卡片图
- 企业级
- 批量生成
- 品牌定制
tools:
  - - read
- exec
# 卡片图生成器(专业版)
## 概述
---
卡片图生成器专业版是一款面向企业和专业内容团队的全功能卡片图片生成平台。在免费版基础模板之上,PRO版新增了X/Twitter风格帖子分享长图、自定义模板创建、批量生成、全平台配色预设、企业品牌定制、水印嵌入等高级功能,帮助团队实现卡片图的标准化、批量化生产。

PRO版与免费版完全兼容,升级后原有模板和配置继续使用。适合企业社交媒体内容矩阵生产、内容团队批量出图、X/Twitter帖子长图制作等场景。

### PRO版增强能力总览
| 能力分类 | 具体功能 | 免费版 | PRO版 |
|:---------|:---------|:-------|:------|
| 基础模板 | 文字海报(3:4) | 支持 | 支持 |
| 基础模板 | 长文分页卡片(3:4) | 支持 | 支持 |
| 基础模板 | 公众号封面(335:100) | 支持 | 支持 |
| 高级模板 | X风格帖子长图 | - | 支持 |
| 高级模板 | 自定义模板 | - | 支持 |
| 高级模板 | 模板版本管理 | - | 支持 |
| 高亮功能 | 整行高亮 | 支持 | 支持 |
| 高亮功能 | 按词高亮 | - | 支持 |
| 高亮功能 | 组合高亮 | - | 支持 |
| 平台预设 | 公众号/小红书 | 支持 | 支持 |
| 平台预设 | 全平台+自定义 | - | 支持 |
| 批量处理 | 批量生成 | - | 支持 |
| 批量处理 | 目录递归 | - | 支持 |
| 品牌定制 | 企业配色方案 | - | 支持 |
| 品牌定制 | 水印嵌入 | - | 支持 |
| 品牌定制 | 版权信息 | - | 支持 |
| 输入校验 | 自动拆分/缩写 | 支持 | 支持 |
| 输入校验 | 智能内容适配 | - | 支持 |
| 团队协作 | 模板共享 | - | 支持 |

## 核心能力
### 1. X风格帖子分享长图(x-like-posts)
PRO版独有功能,将帖子类型数据渲染为X/Twitter风格的分享长图。

```bash
python3 render_x_like_posts.py \
  --input posts.json \
  --out tmp/x_posts.png

python3 render_x_like_posts.py \
  --input posts.json \
  --platform twitter \
  --out tmp/x_posts_twitter.png
```

**输入数据格式(posts.json):**

```json
{
  "posts": [
    {
      "author": {"name": "张三", "handle": "@zhangsan", "avatar": "https://example.com/avatar1.jpg"},
      "text": "今天分享一个关于AI的最新思考:未来的竞争不是技术竞争,而是认知竞争。",
      "createdAt": "2026-07-18T10:30:00+08:00",
      "metrics": {"replies": 15, "retweets": 42, "likes": 128}
    },
    {
      "author": {"name": "李四", "handle": "@lisi", "avatar": "https://example.com/avatar2.jpg"},
      "text": "完全同意。认知决定了我们能看到什么机会,而技术只是实现手段。",
      "createdAt": "2026-07-18T10:35:00+08:00",
      "metrics": {"replies": 3, "retweets": 8, "likes": 35}
    }
  ]
}
```

**帖子长图特性:**
- 自适应长度(根据帖子数量自动调整图片高度)
- 固定宽度900px
- 支持头像、用户名、时间戳显示
- 支持互动数据(回复/转发/点赞)
- Twitter风格蓝白灰配色(默认)
- 帖子过多时自动分页(Part 1 / Part 2)

### 2. 自定义模板创建
PRO版支持创建和管理自定义模板,满足品牌个性化需求。

> 详细代码示例已移至 `references/detail.md`

### 3. 批量生成
支持从数据文件批量生成卡片图,大幅提升内容生产效率。

> 详细代码示例已移至 `references/detail.md`

### 4. 高级高亮功能
PRO版支持整行高亮、按词高亮和组合高亮三种模式。

```bash
python3 render_card.py \
  --template poster-3-4 \
  --text "第一行内容\n第二行内容\n第三行内容" \
  --hl1 "第一行内容" \
  --hl2 "第三行内容" \
  --out tmp/highlight_lines.png

python3 render_card.py \
  --template poster-3-4 \
  --text "AI正在改变世界,从医疗到教育,从交通到娱乐" \
  --highlight-words "AI,医疗,教育,交通,娱乐" \
  --out tmp/highlight_words.png

python3 render_card.py \
  --template poster-3-4 \
  --text "重要通知:本周五举行产品发布会\n主题:AI驱动的未来\n地点:线上直播" \
  --hl1 "重要通知:本周五举行产品发布会" \
  --highlight-words "AI,未来,线上直播" \
  --out tmp/highlight_combined.png
```

### 5. 全平台配色预设与品牌定制

> 详细代码示例已移至 `references/detail.md`

### 6. 水印与版权信息
```bash
python3 render_card.py \
  --template poster-3-4 \
  --text "优质内容值得分享" \
  --watermark "© 2026 优品科技" \
  --watermark-position "bottom-right" \
  --watermark-opacity 0.3 \
  --out tmp/with_watermark.png

python3 render_card.py \
  --template poster-3-4 \
  --text "原创文章,转载请注明出处" \
  --footer "© 2026 优品科技 | All Rights Reserved" \
  --out tmp/with_copyright.png
```

## 使用场景
### 场景一:企业社交媒体内容矩阵
企业内容团队使用PRO版批量生成多个平台的配图,统一品牌视觉风格。

```python
brand = BrandPresetManager("优品科技")
content = "2026年AI技术趋势报告:大模型、多模态、Agent三大方向"
for platform in ["公众号", "小红书", "微博", "知乎"]:
    preset = brand.get_preset(platform)
    subprocess.run(["python3", "render_card.py", "--template", "poster-3-4",
        "--text", content, "--footer", preset["footer"],
        "--bg", preset["bg"], "--highlight", preset["highlight"],
        "--out", f"tmp/matrix/{platform}.png"])
    print(f"[{platform}] 已生成")
```

### 场景二:X/Twitter帖子长图分享
将有趣的Twitter对话或帖子串制作为分享长图。

```bash
python3 render_x_like_posts.py \
  --input twitter_thread.json \
  --platform twitter \
  --out tmp/twitter_thread.png

```

### 场景三:批量金句海报生成
从文案库批量生成金句海报,用于日常社交媒体运营。

```bash
python3 batch_generate.py \
  --template poster-3-4 \
  --input quotes_library.json \
  --output-dir tmp/quotes_batch/ \
  --platform 公众号

```

## 不适用场景

以下场景卡片图生成器-专业版不适合处理：

- 3D建模和动画制作
- 照片级写实渲染
- 手绘原创插画


## 触发条件

需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于非本工具能力范围的需求。


## 快速开始
### 从免费版升级
```bash
skill-platform skills install card-image-builder-pro
skill-platform gateway restart

```

### 全新安装
```bash
python3 --version
ls "/Applications/Google Chrome.app"  # macOS
skill-platform skills install card-image-builder-pro

python3 init_brand.py --name "你的品牌名"

python3 render_x_like_posts.py --input sample.json --out tmp/test.png
```

## 配置示例
### PRO版企业级配置
```yaml
card_image:
  templates:
    builtin: [poster-3-4, article-3-4, x-like-posts, wechat-cover-split]
    custom_dir: "assets/templates/"
    version_control: true

  batch:
    parallel_workers: 2
    output_dir: "tmp/batch/"
    supported_formats: [json, txt]

  brand:
    name: "优品科技"
    presets:
      公众号: {bg: "#e6f5ef", highlight: "#22a854"}
      小红书: {bg: "#fdecea", highlight: "#e53935"}
      微博: {bg: "#e3f2fd", highlight: "#1976d2"}
      抖音: {bg: "#1a1a1a", highlight: "#fe2c55"}
      twitter: {bg: "#ffffff", highlight: "#1da1f2"}
    custom:
      品牌主视觉: {bg: "#0a0e27", highlight: "#00d4ff"}

  watermark:
    enabled: true
    text: "© 2026 优品科技"
    position: "bottom-right"
    opacity: 0.3

  highlight:
    line_mode: true     # 整行高亮
    word_mode: true     # 按词高亮
    combined: true      # 组合高亮
```

### 模板索引(含PRO版模板)
| 模板名 | 比例 | 尺寸 | 用途 | 版本 |
|:-------|:-----|:-----|:-----|:-----|
| poster-3-4 | 3:4 | 900x1200 | 文字海报 | 免费+PRO |
| article-3-4 | 3:4 | 900x1200 | 长文分页卡片 | 免费+PRO |
| wechat-cover-split | 335:100 | 1340x400 | 公众号封面 | 免费+PRO |
| x-like-posts | 自适应 | 900px宽 | X风格帖子长图 | PRO独有 |
| 自定义模板 | 自定义 | 自定义 | 品牌定制 | PRO独有 |

## 最佳实践
### 1. X长图内容规划
```text
X风格长图制作建议:
1. 选择有价值的帖子串(对话、分析、教程)
2. 控制帖子数量:3-10条为佳
3. 超过10条时自动分页(Part 1 / Part 2)
4. 确保头像和用户名准确
5. 时间戳保持原始顺序
```

### 2. 批量生成工作流
| 步骤 | 操作 | 工具 |
|:-----|:-----|:-----|
| 1 | 准备文案数据(JSON/TXT) | 文本编辑器 |
| 2 | 选择模板和平台预设 | 品牌预设管理器 |
| 3 | 执行批量生成 | 批量生成器 |
| 4 | 检查生成结果 | 文件管理器 |
| 5 | 失败项重试 | 批量生成器 |
| 6 | 发布到各平台 | 社交媒体工具 |

### 3. 品牌视觉一致性
品牌视觉一致性要点:配色统一(品牌标准色)、字体统一(品牌指定字体)、品牌模板包含logo、页脚格式统一(平台 · 品牌名)、重要内容添加版权水印、同类型卡片统一尺寸。

## 常见问题
### Q1: PRO版可以创建多少个自定义模板?
**A:** 没有数量限制。每个模板包含HTML文件和JSON配置文件,存储在 `assets/templates/` 目录下。

### Q2: X风格长图支持多少条帖子?
**A:** 单张建议3-10条。超过10条自动分页(Part 1 / Part 2),宽度固定900px,高度自适应。

### Q3: 批量生成时如何处理失败?
**A:** 批量生成器记录每张图状态,失败项可在统计中查看并重试。常见原因:文案过长、Chrome未就绪、路径不可写。

### Q4: 自定义模板需要什么技术能力?
**A:** 需要基本HTML+CSS知识。模板用HTML编写,通过JSON配置参数,渲染器自动注入。

### Q5: 水印支持哪些样式?
**A:** 支持文字水印,可配置位置、透明度和字体大小。暂不支持图片水印。

### Q6: 如何与免费版用户协作?
**A:** PRO版与免费版完全兼容。免费版用户可使用PRO版创建的自定义模板(需共享文件),免费版三个基础模板在PRO版中继续可用。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+
- **浏览器**: Google Chrome(渲染引擎依赖)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| Google Chrome | 浏览器 | 必需 | google.com/chrome 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Pillow | Python库 | 推荐 | `pip install Pillow` |
| Jinja2 | Python库 | 可选 | `pip install jinja2`(模板渲染) |

### API Key 配置
- 本Skill为本地渲染工具,无需额外API Key
- 所有图片渲染在本地通过Chrome完成
- 不依赖外部图片生成服务
- 自定义模板的HTML/CSS在本地解析渲染

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行卡片图渲染和批量生成任务
- **运行模式**: 本地渲染,依赖Python和Chrome;支持批量处理和自定义模板
- **安全等级**: 本地处理,不涉及网络请求;水印支持版权保护;模板版本可追溯
- **兼容性**: 与免费版(card-image-builder-free)完全兼容,支持无缝升级

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
