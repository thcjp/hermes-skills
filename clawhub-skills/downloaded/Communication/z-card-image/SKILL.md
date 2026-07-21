---
slug: z-card-image
name: z-card-image
version: "1.1.0"
displayName: z-card-image
summary: 生成配图、封面图、卡片图、文字海报、公众号文章封面图、微信公众号头图、X 风格帖子分享图、帖子长图、社媒帖子长图。适用于帖子类型数据、post data、social
  posts、tweet/t...
license: MIT-0
description: |-
  生成配图、封面图、卡片图、文字海报、公众号文章封面图、微信公众号头图、X 风格帖子分享图、帖子长图、社媒帖子长图。适用于帖子类型数据、post
  data、social posts、tweet/t。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Communication
- Creative
tools:
  - - read
- exec
---

# z-card-image

将用户提供的文案渲染成 PNG 卡片图。
支持短文案封面图、长文分页图、X 风格帖子分享长图，以及公众号文章封面图。只要输入是“帖子类型数据”并希望导出成 X 风格长图，都应走 `x-like-posts`。

## 环境要求

* Python 3
* Google Chrome（macOS：`/Applications/Google Chrome.app`；Linux：`chromium` 需修改脚本路径）

## 执行流程

0. **环境提示**（用户触发时检测一次，有问题给提示，不中止流程）：

   * `python3 --version` → 失败则告知：「⚠️ 未检测到 Python 3，渲染可能失败」
   * 检查 Chrome 路径 → 失败则提示安装
1. **识别场景**：

   * 短文案封面图 → `poster-3-4`
   * 长文分页图 → `article-3-4`
   * X 风格帖子分享图 / 帖子长图 / 帖子类型数据 → `x-like-posts`
   * 公众号文章封面图 → `wechat-cover-split`
2. **查模板规则**：根据模板在「模板索引」中找到对应规范文档，读取后按其规则处理文案和参数。**如用户要求高亮：整行用 `--hl1/hl2/hl3`，按词用 `--highlight-words`（逗号分隔），两者可同时使用，不能忽略**
3. **识别平台**：按「平台预设」自动设置配色；推特长图默认使用 Twitter 风格蓝白灰配色
4. **渲染输出**：

   * `poster-3-4` → 执行 `render_card.py`
   * `article-3-4` → 执行 `render_article.py`
   * `x-like-posts` → 执行 `render_x_like_posts.py`
   * `wechat-cover-split` → 执行 `render_card.py`
   * 默认 `--out` 填 `tmp/...png`；如用户指定导出位置，可直接传绝对路径或相对路径
5. **输出产物**：生成 PNG 到指定路径，供后续发送、裁切或复用；如需给外部工具上传，仍应避免写入系统 `/tmp/`

## x-like-posts 导航

`x-like-posts` 用于“帖子类型数据 → X 风格分享长图”。

当命中这条路线时，继续读取：

* [references/x-like-posts.md](/api/v1/skills/z-card-image/file?path=references%2Fx-like-posts.md&ownerHandle=aatrooox)：输入 JSON 格式、可显示字段、时间规则、导出规则
* [references/tweet-thread.md](/api/v1/skills/z-card-image/file?path=references%2Ftweet-thread.md&ownerHandle=aatrooox)：旧命名兼容说明

## 输入校验

* **比例不存在**：驳回请求，告知当前支持的比例列表，询问是否新增模板
* **文案超出模板字数上限**：先自动拆分/缩写后再渲染，不要直接塞入
* **帖子过多**：按规范拆成多张 `Part 1 / Part 2`，不要把超长内容强行塞进一张
* **公众号封面标题过长**：先压缩成 2~3 行短标题，再渲染，不能把完整长标题硬塞进模板

## 平台预设

| 平台 | `--footer` | `--bg` | `--highlight` |
| --- | --- | --- | --- |
| 公众号（默认） | `公众号 · 早早集市` | `#e6f5ef` | `#22a854` |
| 小红书 | `小红书 · 阿康` | `#fdecea` | `#e53935` |

> 用户提到"小红书配图"时使用小红书预设；"小绿书"= 公众号配图，使用公众号预设；否则默认公众号。

## 模板索引

| 模板名 | 比例 | 尺寸 | 用途 | 规范文档 |
| --- | --- | --- | --- | --- |
| `poster-3-4` | 3:4 | 900×1200 | 文字海报（金句/大字报/封面） | [references/poster-3-4.md](/api/v1/skills/z-card-image/file?path=references%2Fposter-3-4.md&ownerHandle=aatrooox) |
| `article-3-4` | 3:4 | 900×1200 | 长文分页卡片 | [references/article-3-4.md](/api/v1/skills/z-card-image/file?path=references%2Farticle-3-4.md&ownerHandle=aatrooox) |
| `x-like-posts` | 自适应长图 | 900px 宽 | X 风格帖子分享长图 | [references/x-like-posts.md](/api/v1/skills/z-card-image/file?path=references%2Fx-like-posts.md&ownerHandle=aatrooox) |
| `wechat-cover-split` | 335:100 | 1340×400 | 公众号文章封面长条图（左标题右 icon） | [references/wechat-cover-split.md](/api/v1/skills/z-card-image/file?path=references%2Fwechat-cover-split.md&ownerHandle=aatrooox) |

## 新增模板

1. 新建 `assets/templates/<name>.html`
2. 在 `render_card.py` 的 `size_map` 里注册尺寸
3. 在上方模板索引中添加一行
4. 创建对应 `references/<name>.md`，记录该模板的参数、字数上限、配图选取规则

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 生成配图、封面图、卡片图、文字海报、公众号文章封面图、微信公众号头图、X 风格帖子分享图、帖子长图、社媒帖子长图
- 适用于帖子类型数据、post
  data、social posts、tweet/t
- 触发关键词: 文字海报, 卡片图, z-card-image, card, social, 封面图, posts, data

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用z-card-image？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: z-card-image有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
