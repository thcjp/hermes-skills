---
slug: novel-autopilot
name: novel-autopilot
version: "1.0.0"
displayName: "网文全自动写手"
summary: "一人顶一个网文工作室,8步管道批量产章+黄金三章+三平台分发"
license: MIT
description: |-
  网文全自动写手——一人顶一个网文工作室,8步管道从大纲到章节全自动生成,黄金三章重点打磨开篇留存,品牌词软广告自动注入,一键分发知乎/头条/微信公众号三平台。

  核心能力:
  - 8步全自动管道:初始化→章节生成→标题→营销注入→SEO优化→内容审核→多平台发布→状态回写
  - 6大题材支持:都市/玄幻/历史/科幻/悬疑/言情
  - 黄金三章开篇:前三章重点打磨钩子/人设/冲突,提升读者留存率
  - 品牌词软广告植入:标题/营销/SEO步骤自动注入品牌词
  - 批量产章:每章3000字,一次生成10章,基于前序章节保持连贯
  - 多平台分发+状态闭环:三平台发布+发布状态回写

  适用场景:
  - 网文作者批量产章:日更压力大,AI辅助批量生成保持更新
  - 副业达人做小说矩阵:多题材多平台,低成本铺量变现
  - IP孵化方快速验证题材:批量生成测试市场反应再决定投入
  - 一人创作者多平台分发:一次写作三平台同步,最大化曝光

  差异化:不是单章生成器,而是8步端到端全自动管道,从初始化到发布状态回写闭环,黄金三章打磨+品牌词注入+SEO优化+敏感词审核,一条龙产出可直接发布的网文内容。

  触发关键词:小说生成、章节创作、网文创作、小说发布、网文写作、黄金三章、小说连载、网文大纲、批量写章
homepage: "https://skillhub.cn"
tags: [网文创作, 内容创作, 自动化写作, 多平台分发, 副业变现]
tools: [read, exec]
---

# 网文全自动写手 v1.0.0

> 定位: 8步管道完成网文从大纲到章节的全自动写作与多平台分发
> 设计: 初始化→章节生成→标题→营销注入→SEO优化→内容审核→多平台发布→发布状态回写

## 使用场景

- 网文小说自动化创作(每章3000字,可批量生成10章/次)
- 网文分发(知乎/头条/微信公众号三平台)
- 小说章节发布状态闭环管理(发布后回写章节状态)
- 多题材支持: 都市/玄幻/历史/科幻/悬疑/言情
- 黄金三章开篇: 前三章重点打磨,吸引读者留存
- 品牌词软广告植入: 标题/营销/SEO步骤自动注入品牌词

## 工作流(8步管道)

1. **小说初始化** (init_novel)
   - 输入: genre="urban"(默认), chapter_words=3000(默认)
   - 输出: book_id, novel_meta{title, author, genre, total_chapters_planned}
   - 异常: genre不支持→默认urban;chapter_words超限→截断为5000
   - 支持题材: urban(都市)/fantasy(玄幻)/history(历史)/scifi(科幻)/mystery(悬疑)/romance(言情)

2. **章节生成** (generate_chapters)
   - 输入: count=10(默认,每次生成10章), words=3000(默认,每章3000字)
   - 输出: chapters[] (每个chapter含chapter_number, title, content, word_count)
   - 异常: count超限→截断为10;words超限→截断为5000;API超时→降级单章生成
   - 说明: 章节生成基于前序章节上下文,保持剧情连贯性
   - 黄金三章: 前三章重点打磨开篇钩子、人设建立、冲突铺垫,提升读者留存率

3. **标题生成** (generate_titles)
   - 输入: content_type="novel", chapter_content(透传)
   - 输出: titles[] (含主标题+副标题+SEO标题)
   - 异常: 生成失败→使用章节默认标题"第N章";标题过长→截断为30字
   - 说明: 标题生成遵循SEO优化原则,包含关键词+情绪点

4. **营销注入** (adapt_platform)
   - 输入: content_type="novel", chapters[], titles[]
   - 输出: marketing_copy{title, description, tags[], cover_suggestion, excerpt}
   - 异常: 营销生成失败→使用默认模板"精彩小说连载中";tags为空→使用默认tags["小说","连载"]

5. **SEO优化** (optimize)
   - 输入: chapters[], marketing_copy
   - 输出: optimized_content{title_seo, description_seo, keywords[], meta_tags}
   - 异常: SEO失败→使用原始内容;keywords过多→截断为10个
   - 说明: SEO优化包含关键词密度/标题长度/描述长度/meta标签生成

6. **内容审核** (check_sensitive_words)
   - 输入: chapters[], optimized_content
   - 输出: audit_report{passed: bool, sensitive_words[], suggested_replacements[]}
   - 异常: 发现敏感词→阻断发布,返回替换建议;审核失败→默认通过(降级)

7. **多平台发布** (publish_content)
   - 输入: platforms=["zhihu", "toutiao", "wechat_official"](默认), optimized_content, marketing_copy
   - 输出: publish_results[] (每平台{platform, post_id, url, status})
   - 异常: 单平台失败→跳过该平台继续发布其他;全部失败→返回完整错误清单

8. **发布状态回写** (publish_chapter)
   - 输入: book_id, chapter_number, publish_results(透传)
   - 输出: publish_status{book_id, chapter_number, status="published", published_at, platform_urls}
   - 异常: 回写失败→记录日志但不阻断管道;book_id无效→跳过回写

## 输入格式

```json
{
  "genre": "string (可选,默认urban,支持urban/fantasy/history/scifi/mystery/romance)",
  "chapter_words": "int (可选,默认3000,范围1000-5000)",
  "count": "int (可选,默认10,范围1-10)",
  "platforms": "array (可选,默认[zhihu,toutiao,wechat_official])"
}
```

## 输出格式

```json
{
  "success": true,
  "data": {
    "book_id": "string",
    "chapters": [
      {
        "chapter_number": "int",
        "title": "string",
        "content": "string",
        "word_count": "int"
      }
    ],
    "marketing_copy": {
      "title": "string",
      "description": "string",
      "tags": ["string"],
      "cover_suggestion": "string",
      "excerpt": "string"
    },
    "optimized_content": {
      "title_seo": "string",
      "description_seo": "string",
      "keywords": ["string"],
      "meta_tags": "object"
    },
    "audit_passed": "bool",
    "publish_results": [
      {
        "platform": "zhihu",
        "post_id": "string",
        "url": "string",
        "status": "published"
      }
    ],
    "publish_status": {
      "book_id": "string",
      "chapter_number": "int",
      "status": "published",
      "published_at": "ISO8601",
      "platform_urls": ["string"]
    }
  },
  "error": null,
  "code": null
}
```

## 异常处理

| 异常场景 | 处理策略 | 降级方案 |
|:---------|:---------|:---------|
| genre不支持 | 默认urban | 使用urban模板 |
| chapter_words超限 | 截断为5000 | - |
| count超限 | 截断为10 | - |
| 章节生成API超时 | 降级单章生成 | 仅生成1章 |
| 标题生成失败 | 使用默认标题"第N章" | - |
| 营销注入失败 | 使用默认模板 | "精彩小说连载中" |
| SEO优化失败 | 使用原始内容 | - |
| 敏感词发现 | 阻断发布 | 返回替换建议 |
| 单平台发布失败 | 跳过该平台 | 继续发布其他平台 |
| 发布状态回写失败 | 记录日志 | 不阻断管道 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 |
| 平台发布API | API | 可选 | 知乎/头条/微信公众号发布(可手动发布) |
| JSON文件存储 | 文件系统 | 可选 | exec工具保存章节和发布状态 |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - 章节生成/标题生成/营销注入/SEO优化
- **PLATFORM_API_KEY**: 可选 - 多平台发布(可手动复制发布)
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
发布环节可手动完成,核心写作流程仅需Agent内置LLM。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 生成都市小说2章并发布

```json
输入:
{
  "genre": "urban",
  "chapter_words": 3000,
  "count": 2,
  "platforms": ["zhihu", "toutiao", "wechat_official"]
}

输出:
{
  "success": true,
  "data": {
    "book_id": "book_20260713_001",
    "chapters": [
      {
        "chapter_number": 1,
        "title": "第一章 重生归来",
        "content": "李明睁开眼,发现自己回到了十年前...",
        "word_count": 3015
      },
      {
        "chapter_number": 2,
        "title": "第二章 商场初遇",
        "content": "李明走进商场,迎面撞上了一个女孩...",
        "word_count": 2985
      }
    ],
    "marketing_copy": {
      "title": "重生都市:逆袭人生从今天开始",
      "description": "一个重生者的都市传奇,商战+爱情+逆袭",
      "tags": ["都市", "重生", "商战", "爱情", "逆袭"],
      "cover_suggestion": "都市夜景+西装男背影",
      "excerpt": "李明睁开眼,发现自己回到了十年前..."
    },
    "optimized_content": {
      "title_seo": "重生都市:逆袭人生从今天开始|都市小说连载",
      "description_seo": "重生都市小说连载,商战+爱情+逆袭,每日更新",
      "keywords": ["都市小说", "重生小说", "商战小说", "都市连载"],
      "meta_tags": {"og:type": "article", "og:title": "重生都市"}
    },
    "audit_passed": true,
    "publish_results": [
      {"platform": "zhihu", "post_id": "zh_001", "url": "https://zhihu.com/...", "status": "published"},
      {"platform": "toutiao", "post_id": "tt_001", "url": "https://toutiao.com/...", "status": "published"},
      {"platform": "wechat_official", "post_id": "wx_001", "url": "https://mp.weixin.qq.com/...", "status": "published"}
    ],
    "publish_status": {
      "book_id": "book_20260713_001",
      "chapter_number": 2,
      "status": "published",
      "published_at": "2026-07-13T16:35:00+08:00",
      "platform_urls": ["https://zhihu.com/...", "https://toutiao.com/...", "https://mp.weixin.qq.com/..."]
    }
  },
  "error": null,
  "code": null
}
```

### 示例2: 敏感词阻断

```json
输入:
{
  "genre": "fantasy",
  "count": 1
}

输出:
{
  "success": false,
  "data": {
    "book_id": "book_20260713_002",
    "chapters": [
      {
        "chapter_number": 1,
        "title": "第一章 觉醒",
        "content": "...",
        "word_count": 3000
      }
    ],
    "audit_passed": false,
    "sensitive_words": ["敏感词1", "敏感词2"],
    "suggested_replacements": {"敏感词1": "替换词1", "敏感词2": "替换词2"}
  },
  "error": "内容审核未通过:发现2个敏感词",
  "code": "AUDIT_FAILED"
}
```
