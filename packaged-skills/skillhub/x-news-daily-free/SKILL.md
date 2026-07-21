---
slug: x-news-daily-free
name: x-news-daily-free
version: "1.0.0"
displayName: X News Daily LITE
summary: 抓取 X.com 关键词热门新闻 Top 10，生成基础中文海报。
license: MIT
description: |-
  X News Daily 免费版。抓取 X.com 上指定关键词的热门新闻 Top 10，自动将英文标题翻译为中文，
  渲染为基础 HTML 海报图片。支持 Headless Chrome 大视口截图方案。
  适用于每日新闻简报、关键词热搜查看等基础场景。
tags:
  - Automation
  - Research
tools:
  - read
  - exec
---

# X News Daily LITE

X News Daily 免费版。抓取 X.com 上指定关键词的热门新闻 Top 10，翻译为中文，生成基础 HTML 海报并发送给用户。

## 核心能力

- **关键词热搜检索**：支持任意关键词在 X.com 上的热门排序检索（`f=top` 参数），如 "NBA"、"AI"、"Skill平台"。无显式关键词时使用默认值 "Skill平台"
- **Top 10 提取**：从 X.com 搜索结果页面提取 10 条新闻，包含标题与正文摘要
- **自动中英翻译**：将英文新闻标题自动翻译为中文，专有名词（如 GPT-4、Claude）保留英文原文
- **基础 HTML 海报渲染**：
  - 背景：浅灰渐变（`#f8f9fa` 渐变到 `#e9ecef`）
  - 卡片：纯白（`#ffffff`）+ 细微阴影
  - 主题色：红色（`#e63946`）
  - 标题：28px 加粗，深黑色（`#212529`）
  - 摘要：20px，灰色（`#6c757d`）
- **大视口截图**：使用 Headless Chrome `--window-size=1600,2400` 截图生成 PNG

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 每日早报 | 关键词 "AI" + 当前日期 2026-07-20 | 10 条 AI 领域热闻的基础海报 `2026-07-20.png` |
| 关键词热搜查看 | 关键词 "NBA" | 10 条 NBA 相关 X 帖子海报 PNG |

**不适用于**：多平台分发、定时任务推送、舆情互动数据监测等高级场景。

## 使用流程

1. **获取关键词**：从用户输入中提取关键词，无显式关键词时使用默认值 "Skill平台"
2. **访问 X.com 搜索页**：使用浏览器访问 `https://x.com/search?q=<URL编码后的关键词>&f=top`
3. **提取 Top 10 新闻**：解析搜索结果，提取每条帖子的标题与正文摘要
4. **翻译标题**：将英文标题翻译为中文，专有名词保留英文
5. **构建 HTML 海报**：按上述配色与字号生成全屏 HTML 文件，文件名采用当天日期（如 `2026-07-20.html`）
6. **截图渲染**：执行 `chrome --headless --disable-gpu --screenshot=output.png --window-size=1600,2400 "file:///path/to/html"`
7. **返回海报**：将生成的 PNG 海报返回给用户

## 截图命令参考

| 方案 | 命令 | 适用场景 |
|------|------|---------|
| 大视口截图（免费版） | `chrome --headless --disable-gpu --screenshot=out.png --window-size=1600,2400 "file:///path/news.html"` | 直接生成 PNG，分发友好 |
| 图片压缩 | `pngquant --quality=80 out.png` | 超 10MB 时压缩至平台限制内 |

**注意**：免费版仅支持大视口截图方案。若页面内容超出 2400px 高度，底部可能被裁切，需拆分多张海报或升级付费版使用 PDF 打印方案。

## 案例展示

### 案例 1：每日 AI 简报

**用户请求**：`X新闻简报 AI`

**执行过程**：
- 关键词提取：`AI`
- 访问：`https://x.com/search?q=AI&f=top`
- 提取 10 条热闻
- 翻译示例：`"OpenAI announces GPT-5"` 翻译为 `"OpenAI 发布 GPT-5"`

**输出文件**：`2026-07-20.png`，1600×2400 像素基础海报，底部含 `https://SkillHub.ai/skill/x-news-daily`

### 案例 2：NBA 热搜查看

**用户请求**：`X新闻简报 NBA`

**执行过程**：
- 关键词：`NBA`
- 访问：`https://x.com/search?q=NBA&f=top`
- 提取 10 条 NBA 相关热闻，含赛事结果与球员动态
- 翻译示例：`"Lakers defeat Celtics in overtime"` 翻译为 `"湖人加时击败凯尔特人"`

**输出文件**：`2026-07-20.png`，1600×2400 像素基础海报

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| X.com 返回登录页 | 未登录或 Cookie 过期 | 检查浏览器登录态，重新登录后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 |
| 搜索结果不足 10 条 | 关键词冷门或被 X 限流 | 扩展关键词（追加 OR 近义词）补充 |
| Chrome 未安装或 PATH 未配置 | 系统未装 Chrome | 使用 `where chrome.exe` 定位，指定绝对路径调用 |
| 截图空白或仅截到视口 | Headless Chrome 默认只截视口 | 显式设置 `--window-size=1600,2400` 撑高视口 |
| 海报中文字体渲染异常 | 系统缺失中文字体 | 安装思源黑体或微软雅黑；HTML 中显式 `font-family` 指定 fallback 字体链 |

## 常见问题

### Q1：为什么必须返回恰好 10 条新闻？
A：海报排版按 10 条网格设计，少于 10 条会出现空白卡片。若搜索结果不足，会通过扩展近义词补充至 10 条。

### Q2：可以抓取英文原文版海报吗？
A：免费版默认翻译为中文。如需英文原文版、自定义配色、多平台分发等高级功能，请升级付费版。

### Q3：截图为什么是空白的？
A：Headless Chrome 默认只截取视口范围。需显式设置 `--window-size=1600,2400` 撑高视口才能截取完整页面。

### Q4：免费版支持哪些分发平台？
A：免费版仅生成 PNG 海报文件返回给用户，不支持自动分发到 QQ、Telegram、Discord、微信等 IM 平台。

## 已知限制

- 依赖 X.com 搜索页 DOM 结构，若 X 调整页面布局可能导致解析失败
- 翻译质量受底层 LLM 影响，专业术语可能出现偏差
- 仅支持 Headless Chrome 大视口截图方案，不支持 PDF 打印与 kiosk 模式
- 不支持自动分发到 IM 平台，需用户手动获取海报文件
- 不支持定时任务配置与互动数据展示
- 海报分辨率固定为 1600×2400，不可自定义

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **浏览器**：Chrome 或 Chromium 90+

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Chrome / Chromium | 软件 | 必需 | 系统包管理器或官方安装包 |
| 中文字体 | 字体 | 必需 | 思源黑体 / 微软雅黑 / 苹方 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供翻译能力 |

### API Key 配置
- 本 Skill 基于 Markdown 指令，无需额外 API Key

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，截图功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务

---

## 升级提示

当前为免费版，仅支持基础新闻抓取与大视口截图。如需以下完整功能，请升级付费版：

- **三种截图方案**：Headless Chrome 打印 PDF（推荐）、大视口截图、kiosk 模式 + screencapture
- **多平台自动分发**：QQ（`<qqimg>` 标签）、Telegram（图片消息）、Discord（附件上传）、微信（文件发送）
- **互动数据展示**：每条新闻含点赞数、转发数、评论数
- **智能摘要生成**：为每条新闻生成 1-2 句中文摘要
- **自定义配色与字号**：CSS 变量自由调整海报样式
- **定时任务推送**：cron 定时触发自动生成并分发
- **图片压缩**：超 10MB 自动压缩至平台限制内

升级至付费版：`https://SkillHub.ai/skill/x-news-daily`
