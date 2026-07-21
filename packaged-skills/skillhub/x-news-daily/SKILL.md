---
slug: x-news-daily
name: x-news-daily
version: "1.0.0"
displayName: X News Daily
summary: 抓取 X.com 关键词热门新闻 Top 10，生成全屏中文海报，支持多平台分发。
license: MIT
description: |-
  抓取 X.com 上指定关键词的热门新闻 Top 10，自动将英文标题翻译为中文，为每条新闻生成 1-2 句中文摘要，
  最终渲染为全屏 HTML 海报图片。支持 Headless Chrome 打印 PDF、大视口截图、kiosk 模式配合 screencapture 三种截图方案。
  生成的海报可作为文件分发到 QQ、Telegram、Discord、微信等任意 IM 平台。
  适用于每日新闻简报、关键词舆情监测、内容运营自动化、定时任务推送等场景。
tags:
  - Automation
  - Research
  - Content
tools:
  - read
  - exec
---

# X News Daily

抓取 X.com 上指定关键词的热门新闻 Top 10，翻译为中文，生成全屏精美 HTML 海报并发送给用户。

## 核心能力

- **关键词热搜检索**：支持任意关键词在 X.com 上的热门排序检索（`f=top` 参数），如 "NBA"、"上海F1"、"AI 大模型"、"Skill平台" 等。无显式关键词时使用默认值 "Skill平台"
- **Top 10 精确提取**：从 X.com 搜索结果页面解析出恰好 10 条新闻，每条包含标题、正文摘要、点赞数、转发数、评论数。条数不足时自动扩展近义词或切换 `f=live` 实时排序补充
- **自动中英翻译**：将英文新闻标题自动翻译为中文，专有名词（如 GPT-4、Claude、Anthropic）保留英文原文，确保中文用户可读
- **智能摘要生成**：为每条新闻生成 1-2 句中文摘要，凝练核心信息点，控制在 60 字以内，避免直接复制原文
- **HTML 海报渲染**：使用全屏 HTML 模板替代 Canvas，获得更稳定的字体渲染与渐变效果
  - 背景：浅灰渐变（`#f8f9fa` 渐变到 `#e9ecef`）
  - 卡片：纯白（`#ffffff`）+ 细微阴影
  - 主题色：红色（`#e63946`）呼应 SkillHub 主题
  - 标题：28px 加粗，深黑色（`#212529`），高对比度
  - 摘要：20px，灰色（`#6c757d`）
  - 底部：Skill 网址 + Powered by SkillHub
- **三种截图方案**：
  - 方案 1（推荐）：Headless Chrome `--print-to-pdf` 输出 PDF，完整保留全页内容
  - 方案 2：Headless Chrome 大视口截图，`--window-size=1600,2400`
  - 方案 3：Chrome kiosk 模式 + macOS `screencapture` 命令
- **多平台文件分发**：作为文件发送到 QQ（`<qqimg>` 标签）、Telegram（图片消息）、Discord（附件上传）、微信（文件发送）等任意 IM

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 每日早报生成 | 关键词 "AI 大模型" + 当前日期 2026-07-20 | 10 条 AI 领域热闻的全屏海报 `2026-07-20.png`，1600×2400 像素 |
| 关键词舆情监测 | 关键词 "上海F1" | 10 条上海 F1 相关 X 帖子海报，含点赞/转发/评论互动数据栏 |
| 定时任务推送 | cron 每日 08:00 触发 + 默认关键词 "Skill平台" | 自动生成当日海报并推送至用户 Telegram 账号 |
| 多平台内容运营 | 关键词 "NBA 总决赛" + 目标平台 QQ+Discord | 同一张海报分别以 `<qqimg>` 标签和 Discord 附件形式发送 |

**不适用于**：需要人工深度编辑的长文内容创作、需要英文原文版海报的场景、非 X.com 平台的新闻抓取、需要超过 10 条新闻的批量导出。

## 使用流程

1. **获取关键词**：从用户输入中提取关键词（如 "X新闻简报 NBA" 提取 "NBA"），无显式关键词时使用默认值 "Skill平台"
2. **访问 X.com 搜索页**：使用浏览器访问 `https://x.com/search?q=<URL编码后的关键词>&f=top`，启用热门排序
3. **提取 Top 10 新闻**：解析搜索结果 DOM，提取每条帖子的标题、正文摘要、点赞数、转发数、评论数。确保恰好 10 条，不足则扩展近义词或切换 `f=live` 补充
4. **翻译标题**：将英文标题翻译为中文，专有名词保留英文（如 "GPT-4"、"Claude 3.5" 不翻译）
5. **生成摘要**：为每条新闻生成 1-2 句中文摘要，单条控制在 60 字以内
6. **构建 HTML 海报**：按上述配色与字号生成全屏 HTML 文件，文件名采用当天日期（如 `2026-07-20.html`）
7. **截图渲染**：按以下优先级选择截图方案
   - 优先：`chrome --headless --disable-gpu --print-to-pdf=output.pdf --virtual-time-budget=10000 "file:///path/to/html"`
   - 备选：`chrome --headless --disable-gpu --screenshot=output.png --window-size=1600,2400 "file:///path/to/html"`
   - 兜底：Chrome kiosk 模式（`--kiosk` 参数）+ macOS `screencapture` 命令，页面超长则滚动截取多部分
8. **分发发送**：根据目标平台选择发送方式
   - QQ：使用 `<qqimg>` 标签包裹图片
   - Telegram：直接以图片消息发送
   - Discord：以附件形式上传
   - 微信：发送文件
9. **校验条数与底部**：返回前再次确认海报恰好包含 10 条新闻，底部含 `https://SkillHub.ai/skill/x-news-daily` 网址

## HTML 海报模板结构

海报 HTML 采用单文件结构，内联 CSS 避免外部依赖，关键结构如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    :root {
      --bg-gradient: linear-gradient(135deg, #f8f9fa, #e9ecef);
      --card-bg: #ffffff;
      --accent: #e63946;
      --headline-color: #212529;
      --summary-color: #6c757d;
      --headline-size: 28px;
      --summary-size: 20px;
    }
    body { margin: 0; padding: 40px; background: var(--bg-gradient);
           font-family: "Source Han Sans", "Microsoft YaHei", sans-serif; }
    .card { background: var(--card-bg); border-radius: 12px; padding: 24px;
            margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    .title { font-size: var(--headline-size); font-weight: 700;
             color: var(--headline-color); margin: 0 0 8px; }
    .summary { font-size: var(--summary-size); color: var(--summary-color); }
    .stats { color: var(--accent); font-size: 16px; }
    .footer { text-align: center; padding: 24px; color: var(--summary-color); }
  </style>
</head>
<body>
  <h1 style="color: var(--accent);">X News Daily - <关键词></h1>
  <!-- 10 张 .card 卡片 -->
  <div class="footer">
    <a href="https://SkillHub.ai/skill/x-news-daily">SkillHub.ai/skill/x-news-daily</a>
    <p>Powered by SkillHub</p>
  </div>
</body>
</html>
```

**字号与对比度规范**：标题 28px 加粗 `#212529` 对背景对比度达 12:1，满足 WCAG AAA；摘要 20px `#6c757d` 对比度 4.6:1 满足 AA。卡片间距 16px，圆角 12px，阴影 `0 2px 8px rgba(0,0,0,0.08)`。

## 截图命令参考

| 方案 | 命令 | 适用场景 |
|------|------|---------|
| 打印 PDF（推荐） | `chrome --headless --disable-gpu --print-to-pdf=out.pdf --virtual-time-budget=10000 "file:///path/news.html"` | 全页内容，不受视口限制 |
| 大视口截图 | `chrome --headless --disable-gpu --screenshot=out.png --window-size=1600,2400 "file:///path/news.html"` | 直接生成 PNG，分发友好 |
| kiosk + screencapture | `chrome --kiosk "file:///path/news.html"` 后执行 `screencapture -x out.png` | macOS 本地调试，需人工触发截图 |
| PDF 转 PNG | `magick convert -density 150 out.pdf out.png` | 由 PDF 转换得到高分辨率 PNG |
| 图片压缩 | `pngquant --quality=80 out.png` | 超 10MB 时压缩至 Telegram 限制内 |

**注意**：Headless Chrome 默认只截取视口范围。使用 `--print-to-pdf` 或显式 `--window-size=1600,2400` 才能截取完整页面。

## 案例展示

### 案例 1：每日 AI 大模型简报

**用户请求**：`X新闻简报 AI 大模型`

**执行过程**：
- 关键词提取：`AI 大模型`
- 访问：`https://x.com/search?q=AI%20大模型&f=top`
- 提取 10 条热闻，含 OpenAI、Anthropic、Google DeepMind 等账号发言
- 翻译示例：`"OpenAI announces GPT-5 with 1M context window"` 翻译为 `"OpenAI 发布 GPT-5，支持 100 万上下文窗口"`
- 摘要示例：`"GPT-5 在 MMLU 与 HumanEval 基准上较 GPT-4 提升 23%，定价较前代下调 40%"`

**输出文件**：`2026-07-20.png`，1600×2400 像素全屏海报，底部含 `https://SkillHub.ai/skill/x-news-daily`

### 案例 2：上海 F1 赛事舆情监测

**用户请求**：`X新闻简报 上海F1`

**执行过程**：
- 关键词：`上海F1`
- 提取包含赛事结果、车手动态、票务信息的 10 条热闻
- 互动数据示例：某条帖子点赞 12.5k、转发 3.2k、评论 870
- 渲染海报含互动数据栏，每条新闻右侧展示点赞/转发/评论数

**输出文件**：`2026-07-20-上海F1.png`，海报含赛事主题色块与互动数据栏

### 案例 3：定时任务推送 Skill平台 关键词

**触发方式**：cron 任务每日 08:00 自动执行

**执行过程**：
- 默认关键词：`Skill平台`
- 抓取 10 条与 Skill 平台生态相关的 X 帖子
- 自动生成海报 `2026-07-20.png`
- 推送至用户 Telegram 账号

**输出**：用户 Telegram 收到一张 1600×2400 的海报图片，文件名 `2026-07-20.png`

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| X.com 返回登录页而非搜索结果 | 未登录或 Cookie 过期 | 检查浏览器登录态，重新登录后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令；或改用未登录可访问的热门搜索接口 |
| 搜索结果不足 10 条 | 关键词冷门或被 X 限流 | 扩展关键词（追加 OR 近义词），或降级 `f=top` 改用 `f=live` 实时排序补充 |
| Chrome 未安装或 PATH 未配置 | 系统未装 Chrome 或环境变量缺失 | 使用 `which chrome` 或 `where chrome.exe` 定位，调用时指定绝对路径 |
| 截图空白或仅截到视口大小 | Headless Chrome 默认只截视口 | 改用 `--print-to-pdf`，或显式设置 `--window-size=1600,2400` 撑高视口 |
| 翻译失败或术语错误 | LLM 翻译偏差或术语未识别 | 对专有名词（GPT-4、Claude 等）设置白名单不翻译；保留原文并列展示 |
| HTML 文件写入失败 | 磁盘空间不足或路径无权限 | 检查目标目录权限与剩余空间，改用用户可写目录如 `~/Desktop/` |
| IM 平台发送失败 | accountId 缺失或图片体积超限 | 确认平台 SDK 配置；超 10MB 的 PNG 先用 `pngquant` 或 `magick convert` 压缩再发送 |
| 海报中文字体渲染异常 | 系统缺失中文字体 | 安装思源黑体或微软雅黑；HTML 中显式 `font-family` 指定 fallback 字体链 |

## 常见问题

### Q1：为什么必须返回恰好 10 条新闻？
A：海报排版按 10 条网格设计，少于 10 条会出现空白卡片，多于 10 条会超出全屏视口。若搜索结果不足，会通过扩展近义词或切换 `f=live` 实时排序补充至 10 条。

### Q2：可以抓取英文原文版海报吗？
A：当前版本默认翻译为中文。如需英文版，可在关键词后追加 `--lang=en` 提示，跳过翻译步骤直接渲染英文标题。也可在 HTML 模板中设置 `data-lang` 属性切换。

### Q3：为什么推荐 Headless Chrome 打印 PDF 而非直接截图？
A：PDF 能完整保留全页内容，不受视口高度限制；截图方案需显式指定 `--window-size`，长内容可能被裁切。最终分发时 PNG 更通用，可由 PDF 经 `magick convert output.pdf output.png` 转换得到。

### Q4：如何在 Windows 上使用 screencapture？
A：screencapture 是 macOS 专有命令。Windows 环境应优先使用 Headless Chrome 方案（方案 1 或 2），或改用 PowerShell `Add-Type` 调用 BitBlt 截屏，也可使用 `nircmd savescreenshot output.png` 等第三方工具。

### Q5：海报可以自定义配色与字号吗？
A：可以。修改 HTML 模板中的 CSS 变量即可：`--bg-gradient`、`--card-bg`、`--accent`、`--headline-color`、`--summary-color`、`--headline-size`、`--summary-size`。建议保持标题与背景对比度 ≥ 4.5:1 确保可读性。

### Q6：定时任务如何配置？
A：在 Agent 平台配置 cron 表达式触发本 Skill，传入默认关键词。macOS/Linux 用 crontab（如 `0 8 * * *`），Windows 用任务计划程序，Agent 平台内置调度器亦可。触发后 Skill 自动执行抓取-翻译-渲染-分发全流程。

## 已知限制

- 依赖 X.com 搜索页 DOM 结构，若 X 调整页面布局可能导致解析失败，需更新选择器
- 翻译质量受底层 LLM 影响，专业术语可能出现偏差，建议设置术语白名单
- Headless Chrome 截图对中文字体渲染依赖系统字体，服务器环境需预装中文字体包（思源黑体/微软雅黑）
- 单次抓取受 X.com 限流影响，高频请求可能触发 429，建议两次抓取间隔 ≥ 5 分钟
- 海报分辨率固定为 1600×2400，超过 10 条的内容不支持，需分页生成多张海报
- 不抓取 X.com 付费内容（Premium 订阅专属帖子）与私密账号帖子
- macOS screencapture 方案不适用于 Windows/Linux，需切换至 Headless Chrome 方案

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **浏览器**：Chrome 或 Chromium 90+（用于 Headless 截图与 PDF 渲染）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Chrome / Chromium | 软件 | 必需 | 系统包管理器或官方安装包 |
| 中文字体 | 字体 | 必需 | 思源黑体 / 微软雅黑 / 苹方 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供翻译能力 |
| IM 平台 SDK | SDK | 可选 | 按目标分发平台配置（QQ/TG/Discord/微信） |

### API Key 配置
- 本 Skill 基于 Markdown 指令，无需额外 API Key（除目标 IM 平台自身的鉴权配置）

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，截图与分发功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
