---
slug: "x-news-daily-free"
name: "x-news-daily-free"
version: "1.0.0"
displayName: "X News Daily LITE"
summary: "抓取 X.com 关键词热门新闻 Top 10，生成基础中文海报。"
license: "MIT"
description: |-
  X News Daily 免费版。抓取 X.com 上指定关键词的热门新闻 Top 10，自动将英文标题翻译为中文，
  渲染为基础 HTML 海报图片。支持 Headless Chrome 大视口截图方案.
  适用于每日新闻简报、关键词热搜查看等基础场景.
tags:
  - 研发工具
  - Research
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# X News Daily LITE

X News Daily 免费版。抓取 X.com 上指定关键词的热门新闻 Top 10，翻译为中文，生成基础 HTML 海报并发送给用户.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | X News Daily LITE处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

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
### 关键词热搜检索

针对关键词热搜检索,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供关键词热搜检索相关的配置参数、输入数据和处理选项.
**输出**: 返回关键词热搜检索的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`关键词热搜检索`的配置文档进行参数调优
### Top 10 提取

针对Top 10 提取,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供Top 10 提取相关的配置参数、输入数据和处理选项.
**输出**: 返回Top 10 提取的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`Top 10 提取`的配置文档进行参数调优
### 自动中英翻译

针对自动中英翻译,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供自动中英翻译相关的配置参数、输入数据和处理选项.
**输出**: 返回自动中英翻译的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`自动中英翻译`的配置文档进行参数调优
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 每日早报 | 关键词 "AI" + 当前日期 2026-07-20 | 10 条 AI 领域热闻的基础海报 `2026-07-20.png` |
| 关键词热搜查看 | 关键词 "NBA" | 10 条 NBA 相关 X 帖子海报 PNG |

**不适用于**：多平台分发、定时任务推送、舆情互动数据监测等高级场景.
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
|---:|---:|---:|
| 大视口截图（免费版） | `chrome --headless --disable-gpu --screenshot=out.png --window-size=1600,2400 "file:///path/news.html"` | 直接生成 PNG，分发友好 |
| 图片压缩 | `pngquant --quality=80 out.png` | 超 10MB 时压缩至平台限制内 |

**注意**：免费版仅支持大视口截图方案。若页面内容超出 2400px 高度，底部可能被裁切，需拆分多张海报或升级付费版使用 PDF 打印方案.
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
|:---:|:---:|:---:|
| X.com 返回登录页 | 未登录或 Cookie 过期 | 检查浏览器登录态，重新登录后检查网络连接和配置后重试 |
| 搜索结果不足 10 条 | 关键词冷门或被 X 限流 | 扩展关键词（追加 OR 近义词）补充 |
| Chrome 未安装或 PATH 未配置 | 系统未装 Chrome | 使用 `where chrome.exe` 定位，指定绝对路径调用 |
| 截图空白或仅截到视口 | Headless Chrome 默认只截视口 | 显式设置 `--window-size=1600,2400` 撑高视口 |
| 海报中文字体渲染异常 | 系统缺失中文字体 | 安装思源黑体或微软雅黑；HTML 中显式 `font-family` 指定 fallback 字体链 |

## 常见问题

### Q1：为什么必须返回恰好 10 条新闻？
A：海报排版按 10 条网格设计，少于 10 条会出现空白卡片。若搜索结果不足，会通过扩展近义词补充至 10 条.
### Q2：可以抓取英文原文版海报吗？
A：免费版默认翻译为中文。如需英文原文版、自定义配色、多平台分发等高级功能，请升级付费版.
### Q3：截图为什么是空白的？
A：Headless Chrome 默认只截取视口范围。需显式设置 `--window-size=1600,2400` 撑高视口才能截取完整页面.
### Q4：免费版支持哪些分发平台？
A：免费版仅生成 PNG 海报文件返回给用户，不支持自动分发到 QQ、Telegram、Discord、微信等 IM 平台.
## 已知限制

- 依赖 X.com 搜索页 DOM 结构，若 X 调整页面布局可能导致解析失败
- 翻译质量受底层 LLM 影响，专业术语可能出现偏差
- 仅支持 Headless Chrome 大视口截图方案，不支持 PDF 打印与 kiosk 模式
- 不支持自动分发到 IM 平台，需用户手动获取海报文件
- 不支持定时任务配置与互动数据展示
- 海报分辨率固定为 1600×2400，不可自定义

## 代码示例

### Python: X.com 热门新闻抓取与解析

```python
import requests
from urllib.parse import quote
from datetime import datetime
import json
import re
# ...
def fetch_xcom_trending(keyword: str, top_n: int = 10) -> list[dict]:
    """
    抓取 X.com 指定关键词的热门新闻(Top N)
    返回: [{"rank": 1, "title": "...", "summary": "...", "url": "..."}]
    """
    encoded_keyword = quote(keyword)
    search_url = f"https://x.com/search?q={encoded_keyword}&f=top"
# ...
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml",
    }
# ...
    # 使用已登录的 Cookie(需用户自行配置)
    cookies = {"auth_token": "YOUR_AUTH_TOKEN", "ct0": "YOUR_CT0_TOKEN"}
# ...
    response = requests.get(search_url, headers=headers, cookies=cookies, timeout=30)
    response.raise_for_status()
# ...
    # 解析搜索结果页面
    articles = parse_search_results(response.text, top_n)
    return articles
# ...
def parse_search_results(html: str, top_n: int) -> list[dict]:
    """
    从 X.com 搜索结果 HTML 中提取帖子标题与摘要
    """
    articles = []
    # 匹配帖子数据(基于 X.com 页面结构)
    tweet_pattern = re.compile(
        r'data-testid="tweetText"[^>]*>(.*?)</div>',
        re.DOTALL
    )
    matches = tweet_pattern.findall(html)
# ...
    for i, match in enumerate(matches[:top_n], 1):
        # 清理 HTML 标签
        clean_text = re.sub(r'<[^>]+>', '', match).strip()
        if not clean_text:
            continue
# ...
        articles.append({
            "rank": i,
            "title": clean_text[:100],
            "summary": clean_text[100:300] if len(clean_text) > 100 else "",
            "url": f"https://x.com/search?q=placeholder&f=top"
        })
# ...
    return articles
# ...
def translate_titles(articles: list[dict]) -> list[dict]:
    """
    将英文标题翻译为中文(专有名词保留英文)
    调用 Agent 内置 LLM 能力进行翻译
    """
    preserved_terms = ["GPT", "Claude", "AI", "NBA", "GPU", "API", "CEO", "IPO"]
# ...
    for article in articles:
        title = article["title"]
        # 标记需保留的专有名词
        for term in preserved_terms:
            title = title.replace(term, f"<<{term}>>")
        # 此处调用 LLM 翻译(伪代码,实际由 Agent 执行)
        # translated = llm_translate(title, source="en", target="zh")
        # article["title_zh"] = restore_terms(translated)
        article["title_zh"] = title  # 占位,实际由 Agent LLM 翻译
# ...
    return articles
# ...
# 使用示例
if __name__ == "__main__":
    keyword = "AI"
    print(f"正在抓取 X.com 热门新闻: {keyword}")
# ...
    articles = fetch_xcom_trending(keyword, top_n=10)
    articles = translate_titles(articles)
# ...
    today = datetime.now().strftime("%Y-%m-%d")
    output_file = f"news_{today}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"keyword": keyword, "date": today, "articles": articles},
                  f, ensure_ascii=False, indent=2)
# ...
    print(f"已保存 {len(articles)} 条新闻到 {output_file}")
    for a in articles:
        print(f"  [{a['rank']}] {a.get('title_zh', a['title'])}")
```

### HTML: 新闻海报模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1600px;
      min-height: 2400px;
      background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
      font-family: "Microsoft YaHei", "PingFang SC", "Noto Sans SC", sans-serif;
      padding: 60px 80px;
    }
    .header {
      text-align: center;
      margin-bottom: 40px;
      border-bottom: 4px solid #e63946;
      padding-bottom: 24px;
    }
    .header h1 {
      font-size: 48px;
      color: #e63946;
      font-weight: 700;
    }
    .header .date {
      font-size: 24px;
      color: #6c757d;
      margin-top: 12px;
    }
    .news-card {
      background: #ffffff;
      border-radius: 12px;
      padding: 32px;
      margin-bottom: 24px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .news-card .rank {
      display: inline-block;
      background: #e63946;
      color: #fff;
      font-size: 20px;
      font-weight: 700;
      width: 40px;
      height: 40px;
      line-height: 40px;
      text-align: center;
      border-radius: 50%;
      margin-right: 16px;
    }
    .news-card .title {
      font-size: 28px;
      font-weight: 700;
      color: #212529;
      display: inline;
      vertical-align: middle;
    }
    .news-card .summary {
      font-size: 20px;
      color: #6c757d;
      margin-top: 16px;
      line-height: 1.6;
    }
    .footer {
      text-align: center;
      margin-top: 40px;
      font-size: 18px;
      color: #adb5bd;
    }
  </style>
</head>
<body>
  <div class="header">
    <h1>X News Daily</h1>
    <div class="date">2026-07-22 | AI 热门 Top 10</div>
  </div>
# ...
  <div class="news-card">
    <span class="rank">1</span>
    <span class="title">OpenAI 发布 GPT-5</span>
    <div class="summary">OpenAI 宣布推出 GPT-5 模型,支持多模态推理与超长上下文窗口</div>
  </div>
# ...
  <!-- 其余 9 条新闻卡片按相同结构重复 -->
# ...
  <div class="footer">https://SkillHub.ai/skill/x-news-daily</div>
</body>
</html>
```

### Shell: Headless Chrome 截图命令

```bash
# 大视口截图:将 HTML 海报渲染为 PNG
chrome --headless --disable-gpu \
  --screenshot=2026-07-22.png \
  --window-size=1600,2400 \
  "file:///path/to/news_2026-07-22.html"
# ...
# 如果 Chrome 不在 PATH 中,指定绝对路径
"C:\Program Files\Google\Chrome\Application\chrome.exe" \
  --headless --disable-gpu \
  --screenshot=2026-07-22.png \
  --window-size=1600,2400 \
  "file:///path/to/news_2026-07-22.html"
# ...
# 如果生成的 PNG 超过 10MB,使用 pngquant 压缩
pngquant --quality=80 --output=2026-07-22-compressed.png 2026-07-22.png
```

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **浏览器**：Chrome 或 Chromium 90+

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "X News Daily LITE处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "x-news-daily"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
