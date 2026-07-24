---
slug: "rss-fetcher"
name: "rss-fetcher"
version: 1.1.1
displayName: "Rss Fetcher"
summary: "统一的RSS采集与管理系统 | Unified RSS Feed Fetcher and Manager 支持增量抓取、自动去重、自动标签、源健康监控、HTML报告生成"
license: "Proprietary"
description: |-
  统一的RSS采集与管理系统 | Unified RSS Feed Fetcher and Manager 支持增量抓取、自动去重、自动标签、源健康监控、HTML报告生成\
  \ Incremental 。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估.
tags:
  - Research
  - Lifestyle
  - RSS
  - 订阅
  - 信息
  - html
  - python3
tools:
  - read
  - exec
homepage: ""
# 定价元数据
category: "Knowledge"
---
# Rss Fetcher

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Rss Fetcher统一的RSS采集 | 不支持 | 支持 |
| Rss Fetcher支持增量抓取 | 不支持 | 支持 |
| Rss Fetcher源健康监控 | 不支持 | 支持 |
| 多源数据聚合与去重 | 不支持 | 支持 |
| 语义搜索与智能摘要 | 不支持 | 支持 |

## 核心能力

* **增量抓取 / Incremental Fetching** - 只抓取新文章，基于URL哈希自动去重 | Only fetch new articles, auto-deduplicate 基于 URL hash
* **自动标签 / Auto-tagging** - 优先使用RSS自带category，无则自动提取标题关键词 | Prioritize RSS category, auto-extract keywords from title if absent
* **HTML报告 / HTML Reports** - 生成可筛选的静态HTML页面，支持日期/分类/标签多维度筛选 | Generate filterable static HTML pages with date/category/tag filters
* **源健康监控 / Source Health Monitoring** - 检测RSS源可用性，支持批量检查 | Monitor RSS source availability with batch checking
* **分类管理 / Category Management** - 文章自动继承源的分类，支持多维度筛选 | Articles inherit source categories, multi-dimensional filtering
* **超时设置 / Timeout Setting** - 单源30秒超时，避免长时间阻塞 | 30-second timeout per source to avoid blocking

---
### 增量抓取 / Incremental Fetching

针对增量抓取 / Incremental Fetching,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供增量抓取 / Incremental Fetching相关的配置参数、输入数据和处理选项.
**输出**: 返回增量抓取 / Incremental Fetching的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`增量抓取 / Incremental Fetching`的配置文档进行参数调优
### 自动标签 / Auto-tagging

针对自动标签 / Auto-tagging,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供自动标签 / Auto-tagging相关的配置参数、输入数据和处理选项.
**输出**: 返回自动标签 / Auto-tagging的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`自动标签 / Auto-tagging`的配置文档进行参数调优
### HTML报告 / HTML Reports

针对HTML报告 / HTML Reports,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供HTML报告 / HTML Reports相关的配置参数、输入数据和处理选项.
**输出**: 返回HTML报告 / HTML Reports的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`HTML报告 / HTML Reports`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 增量抓取 | RSS源配置与时间范围 | 去重后的新文章数据 |
| HTML报告 | 抓取的文章数据 | 可筛选的静态HTML报告页 |
| 源健康监控 | RSS源URL列表 | 源可用性状态检查结果 |
| 源管理 | 源ID/名称/URL/分类 | 源的增删启停操作结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 1. 初始化数据库 | Initialize Database

```bash
cd skills/rss_fetcher
python3 （请参考skill目录中的脚本文件）
```

### 2. 配置RSS源 | Configure RSS Sources

编辑 `config/sources.json`，添加你的RSS源：
Edit `config/sources.json` to add your RSS sources:

```json
{
  "sources": [
    {
      "id": "openai",
      "name": "OpenAI Blog",
      "url": "https://openai.com/blog/rss.xml",
      "category": "tech",
      "enabled": true
    }
  ]
}
```

### 3. 执行抓取 | Execute Fetch

```bash
python3 （请参考skill目录中的脚本文件）
# ...
python3 （请参考skill目录中的脚本文件） --sources openai huggingface
# ...
python3 （请参考skill目录中的脚本文件） --hours 48
# ...
python3 （请参考skill目录中的脚本文件） --workers 50
```

**⚠️ 抓取后记得更新HTML报告** - 新抓取的文章需要重新生成页面才能在浏览器中查看
**⚠️ Remember to update HTML report after fetching** - New articles require regeneration to view in browser

```bash
python3 （请参考skill目录中的脚本文件） && python3 （请参考skill目录中的脚本文件）
```

### 4. 生成HTML报告 | Generate HTML Report

**注意：每次抓取新文章后，必须重新生成HTML页面才能看到最新内容。**
**Note: Must regenerate HTML after fetching new articles to see latest content.**

```bash
python3 （请参考skill目录中的脚本文件） && python3 （请参考skill目录中的脚本文件）
# ...
python3 （请参考skill目录中的脚本文件）
# ...
open data/index.html  # Mac
```

**HTML报告功能 / HTML Report Features**:

1. 📅 **日期筛选 / Date Filter** - 起止日期选择 | Start/end date selection
2. 🏷️ **分类筛选 / Category Filter** - 按文章分类筛选 | Filter by article category
3. 🔍 **关键词搜索 / Keyword Search** - 实时搜索标题 | Real-time title search
4. ☑️ **标签多选 / Multi-tag Selection** - 多标签组合筛选（AND逻辑）| Multi-tag combo filter (AND logic)
5. 📊 **实时统计 / Real-time Stats** - 显示筛选结果数量 | Show filtered results count

### 5. 源管理 | Source Management

```bash
python3 （请参考skill目录中的脚本文件） check
# ...
python3 （请参考skill目录中的脚本文件） stats
# ...
python3 （请参考skill目录中的脚本文件） add myblog "My Blog" "https://example.com/feed.xml" tech
# ...
python3 （请参考skill目录中的脚本文件） disable myblog
python3 （请参考skill目录中的脚本文件） enable myblog
python3 （请参考skill目录中的脚本文件） remove myblog
```

### 6. 查看文章列表 | View Article List

```bash
python3 （请参考skill目录中的脚本文件）
# ...
python3 （请参考skill目录中的脚本文件） --hours 48
# ...
python3 （请参考skill目录中的脚本文件） --category tech
# ...
python3 （请参考skill目录中的脚本文件） --json
```

---

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | rss-fetcher处理的内容输入 |,  |
| content | string | 否 | rss-fetcher处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "fetcher 相关配置参数",
    result: "fetcher 相关配置参数",
    result: "fetcher 相关配置参数",
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
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 获取今天所有文章 | Get Today's Articles

```sql
SELECT title, url, source_id
FROM articles
WHERE date(fetched_at, 'unixepoch') = date('now')
ORDER BY published_at DESC;
```

### 获取某分类的文章 | Get Articles by Category

```sql
SELECT * FROM articles
WHERE category = 'tech'
AND published_at > strftime('%s', 'now', '-24 hours');
```

### 获取带标签的文章 | Get Articles with Tags

```sql
SELECT a.title, a.url, GROUP_CONCAT(t.name) as tags
FROM articles a
LEFT JOIN article_tags at ON a.id = at.article_id
LEFT JOIN tags t ON at.tag_id = t.id
WHERE a.category = 'tech'
GROUP BY a.id;
```

### 获取热门标签 | Get Popular Tags

```sql
SELECT t.name, COUNT(*) as count
FROM tags t
JOIN article_tags at ON t.id = at.tag_id
GROUP BY t.id
ORDER BY count DESC;
```

---

## 常见问题

### Q1: 如何开始使用Rss Fetcher？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **首次抓取会比较慢** - 需要抓所有历史文章
   **First fetch is slow** - Need to fetch all historical articles
2. **SQLite并发** - 单进程访问，避免并发写入
   **SQLite concurrency** - Single process access, avoid concurrent writes
3. **时间不可靠文章** - published_at = 0 的文章需人工审核
   **Unreliable time articles** - Articles with published_at = 0 need manual review
4. **标签自动累积** - 随着文章增多，标签会自动丰富
   **Tags auto-accumulate** - Tags enrich as more articles are fetched
5. **定期重新生成HTML** - 抓取新文章后需重新运行 `generate_html.py`
   **Regularly regenerate HTML** - Must rerun `generate_html.py` after fetching new articles

---

*Part of Skill平台 Daily Research System*
