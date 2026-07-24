---
slug: novel-autopilot
name: novel-autopilot
version: 1.0.1
displayName: "网文全自动写手"
summary: "一人顶一个网文工作室,8步管道批量产章+黄金三章+三平台分发。网文全自动写手是一款8步管道完成网文从大纲到章节全自动写作与多平台分发的工具. 一人顶一个网文工作室,支持6大题材、黄金三章打磨"
license: Proprietary
description: |-
  网文全自动写手是一款8步管道完成网文从大纲到章节全自动写作与多平台分发的工具.
  一人顶一个网文工作室,支持6大题材、黄金三章打磨、品牌词软广告植入、批量产章与三平台一键分发.
  核心能力:
  - 8步全自动管道:初始化→章节生成→标题→营销注入→SEO优化→内容审核→多平台发布→状态回写
  - 6大题材支持:都市/玄幻/历史/科幻/悬疑/言情,各题材独立模板与人设库
  - 黄金三章开篇:前三章重点打磨钩子/人设/冲突,提升读者留存率
  - 品牌词软广告植入:标题/营销/SEO步骤自动注入品牌词,大小写不敏感去重
  - 批量产章与多平台分发:每章3000字,一次生成10章,知乎/头条/微信公众号一键分发
homepage: ""
tags:
  - 网文创作
  - 内容创作
  - 自动化写作
  - 多平台分发
  - 副业变现
  - 工具
  - 效率
  - 自动化
  - 写作
  - 电商
  - 创意
  - 图像
  - string
  - 默认
  - seo
  - 标题
  - 异常处理
tools:
  - read
  - exec
  - write
category: "Automation"
---
# 网文全自动写手 v1.1.0

> 定位: 8步管道完成网文从大纲到章节的全自动写作与多平台分发
> 设计: 初始化→章节生成→标题→营销注入→SEO优化→内容审核→多平台发布→发布状态回写

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

1. **8步全自动管道**: 初始化→章节生成→标题→营销注入→SEO优化→内容审核→多平台发布→状态回写,端到端闭环
2. **6大题材支持**: 都市/玄幻/历史/科幻/悬疑/言情,各题材独立模板与人设库
3. **黄金三章开篇**: 前三章重点打磨钩子/人设/冲突,提升读者留存率
4. **品牌词软广告植入**: 标题/营销/SEO步骤自动注入品牌词,大小写不敏感去重
5. **批量产章与多平台分发**: 每章3000字,一次生成10章,基于前序章节保持连贯;知乎/头条/微信公众号一键分发
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 网文小说自动化创作 | genre题材+chapter_words字数+count章数 | chapters[](章节号/标题/正文/字数) |
| 黄金三章开篇打磨 | genre+count=3 | 前三章重点优化(钩子/人设/冲突) |
| 多平台分发 | platforms数组+optimized_content | publish_results[](平台/post_id/url/状态) |
| 品牌词软广告注入 | brand_keywords+chapters | 注入品牌词的标题/营销/SEO内容 |
| 章节发布状态闭环管理 | book_id+chapter_number | publish_status(状态/发布时间/平台URL) |

**不适用于**: 学术论文写作、新闻报道、非虚构文学、短篇散文(单篇<1000字)、海外平台分发(仅支持国内三平台).
## 使用流程

### Step 1: 环境准备
- 确认Agent已加载本SKILL.md,且支持exec工具
- 在Agent环境变量中配置 `LLM_API_KEY`(必需)和 `PLATFORM_API_KEY`(可选,用于自动发布)
- 如仅需写作不需自动发布,可跳过平台API配置,手动复制发布

### Step 2: 调用初始化(init_novel)
- 输入: `genre`(默认urban)、`chapter_words`(默认3000,范围1000-5000)
- 输出: book_id + novel_meta(title/author/genre/total_chapters_planned)
- 异常处理: genre不支持→默认urban;chapter_words超限→截断为5000

### Step 3: 批量章节生成(generate_chapters)
- 输入: `count`(默认10,范围1-10)、`words`(默认3000)
- 输出: chapters[](chapter_number/title/content/word_count)
- 黄金三章: 前三章重点打磨开篇钩子、人设建立、冲突铺垫
- 异常处理: API超时→降级单章生成;count超限→截断为10

### Step 4: 标题生成(generate_titles)
- 输入: content_type="novel" + chapter_content(透传)
- 输出: titles[](主标题+副标题+SEO标题)
- 异常处理: 生成失败→使用默认标题"第N章";标题过长→截断为30字

### Step 5: 营销注入(adapt_platform)
- 输入: content_type="novel" + chapters[] + titles[]
- 输出: marketing_copy(title/description/tags/cover_suggestion/excerpt)
- 异常处理: 营销生成失败→使用默认模板"精彩小说连载中";tags为空→使用默认tags["小说","连载"]

### Step 6: SEO优化(optimize)
- 输入: chapters[] + marketing_copy
- 输出: optimized_content(title_seo/description_seo/keywords/meta_tags)
- 异常处理: SEO失败→使用原始内容;keywords过多→截断为10个

### Step 7: 内容审核(check_sensitive_words)
- 输入: chapters[] + optimized_content
- 输出: audit_report(passed/sensitive_words/suggested_replacements)
- 异常处理: 发现敏感词→阻断发布,返回替换建议;审核失败→默认通过(降级)

### Step 8: 多平台发布与状态回写(publish_content + publish_chapter)
- 输入: platforms(默认[zhihu,toutiao,wechat_official]) + optimized_content + marketing_copy
- 输出: publish_results[](platform/post_id/url/status) + publish_status(book_id/chapter_number/status/published_at/platform_urls)
- 异常处理: 单平台失败→跳过该平台继续发布其他;全部失败→返回完整错误清单;回写失败→记录日志但不阻断管道

## 输入格式

```json
{
  "genre": "string (可选,默认urban,支持urban/fantasy/history/scifi/mystery/romance)",
  "chapter_words": "int (可选,默认3000,范围1000-5000)",
  "count": "int (可选,默认10,范围1-10)",
  "platforms": "array (可选,默认[zhihu,toutiao,wechat_official])",
  "brand_keywords": "array (可选,品牌词列表,自动注入标题/营销/SEO)"
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

| 异常场景 | 原因 | 处理方式 |
|---:|---:|---:|
| genre不支持 | 输入的题材不在6大支持范围内 | 默认使用urban模板,标注warning |
| chapter_words超限 | 输入值>5000或<1000 | 截断为5000(上限)或1000(下限) |
| count超限 | 输入值>10 | 截断为10,标注warning |
| 章节生成API超时 | LLM响应超过30秒 | 降级为单章生成,仅生成1章 |
| 标题生成失败 | LLM返回格式异常 | 使用默认标题"第N章" |
| 营销注入失败 | LLM调用失败或返回为空 | 使用默认模板"精彩小说连载中",tags使用["小说","连载"] |
| SEO优化失败 | 关键词提取异常 | 使用原始内容,跳过SEO增强 |
| keywords过多 | 超过10个关键词 | 截断为10个,保留权重最高项 |
| 敏感词发现 | 内容含违禁词/敏感词 | 阻断发布,返回sensitive_words和suggested_replacements |
| 审核服务失败 | 审核API不可用 | 默认通过(降级),标注warning提示人工复核 |
| 单平台发布失败 | 平台API超时或鉴权失败 | 跳过该平台,继续发布其他平台,返回partial_success |
| 全部平台发布失败 | 所有平台API不可用 | 返回完整错误清单,内容仍可手动复制发布 |
| 发布状态回写失败 | book_id无效或存储异常 | 记录日志但不阻断管道,内容已成功发布 |
| LLM_API_KEY未配置 | 环境变量缺失 | 返回error,提示配置环境变量 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:---:|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | 国内可用: 通义千问/文心一言/智谱GLM/DeepSeek/Kimi |
| 知乎发布API | API | 可选 | 知乎开放平台申请 | 不可用时手动复制发布 |
| 头条发布API | API | 可选 | 头条号开放平台申请 | 不可用时手动复制发布 |
| 微信公众号API | API | 可选 | 微信公众平台申请 | 不可用时手动复制发布 |
| JSON文件存储 | 文件系统 | 可选 | exec工具保存章节和发布状态 | 本地文件系统,无海外依赖 |

### API Key 配置(零暴露原则)
- **LLM_API_KEY**: 必需(通常由Agent内置) - 章节生成/标题生成/营销注入/SEO优化
- **PLATFORM_API_KEY**: 可选 - 多平台发布(可手动复制发布)
- **配置方式**: 必须通过Agent环境变量注入,严禁在SKILL.md或代码中硬编码API Key
- **安全检查**: 本SKILL.md中不包含任何API Key示例,所有Key均通过 `$env:LLM_API_KEY` 等环境变量读取

### 使用流程(补充)
发布环节可手动完成,核心写作流程仅需Agent内置LLM.
只需将SKILL.md文件放入Agent的skills目录即可直接使用.
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力.
### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 都市题材批量产章(完整管道)

**输入**:
```json
{
  "genre": "urban",
  "chapter_words": 3000,
  "count": 2,
  "platforms": ["zhihu", "toutiao", "wechat_official"]
}
```

**输出**:
```json
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

### 示例2: 敏感词阻断(审核失败场景)

**输入**:
```json
{
  "genre": "fantasy",
  "count": 1
}
```

**输出**:
```json
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

### 示例3: 仅写作不发布(手动发布场景)

**输入**:
```json
{
  "genre": "romance",
  "chapter_words": 2500,
  "count": 3,
  "platforms": []
}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "book_id": "book_20260713_003",
    "chapters": [
      {"chapter_number": 1, "title": "第一章 初遇", "content": "...", "word_count": 2510},
      {"chapter_number": 2, "title": "第二章 误会", "content": "...", "word_count": 2485},
      {"chapter_number": 3, "title": "第三章 心动", "content": "...", "word_count": 2502}
    ],
    "marketing_copy": {"title": "初遇心动:都市言情三部曲", "description": "...", "tags": ["言情","都市","爱情"]},
    "optimized_content": {"title_seo": "初遇心动|都市言情小说连载", "keywords": ["言情小说","都市言情"]},
    "audit_passed": true,
    "publish_results": [],
    "publish_status": null
  },
  "error": null,
  "code": null
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成.
### 案例1: 玄幻小说批量章节生成(黄金三章打磨,8步全流程)

**输入**:
```json
{
  "genre": "fantasy",
  "chapter_words": 3000,
  "count": 3,
  "platforms": ["zhihu", "toutiao", "wechat_official"],
  "brand_keywords": ["玄幻世界", "修仙"]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "book_id": "novel_20260720_001",
    "chapters": [
      {
        "chapter_number": 1,
        "title": "第一章 天降灵根",
        "content": "少年林逸站在断崖边,脚下是万丈深渊,身后是追杀他的家族护卫。\"交出灵根,饶你不死!\"护卫队长厉声喝道。林逸嘴角微微上扬,右手探入怀中,那块从古墓中得来的玉佩正散发着幽幽蓝光。他不知道的是,这块玉佩将彻底改变他的命运...",
        "word_count": 3012
      },
      {
        "chapter_number": 2,
        "title": "第二章 玉佩传承",
        "content": "蓝光暴涨,林逸只觉一股洪流涌入体内,经脉中沉寂多年的灵力开始疯狂运转。\"这是...上古传承?\"他难以置信地感受着体内翻天覆地的变化。护卫们被蓝光震退,惊恐地看着少年的气息以肉眼可见的速度攀升...",
        "word_count": 2985
      },
      {
        "chapter_number": 3,
        "title": "第三章 初入宗门",
        "content": "三日后,林逸站在云霄宗的山门前。经过玉佩传承,他的修为已突破炼气三层。\"新弟子考核?\"他看着眼前高耸入云的阶梯,嘴角勾起一抹弧度。这场考核,他不仅要通过,还要一鸣惊人。因为那个追杀他的家族,就在云霄宗的附属势力之中...",
        "word_count": 3056
      }
    ],
    "marketing_copy": {
      "title": "玄幻世界:灵根觉醒",
      "description": "少年林逸偶得上古传承,从此踏上修仙之路。家族追杀、宗门争斗、秘境探险,且看他如何一步步逆天改命!",
      "tags": ["玄幻", "修仙", "逆袭", "热血", "连载"],
      "cover_suggestion": "少年立于断崖,手持蓝色玉佩,身后追兵逼近,画面色调蓝金对比",
      "excerpt": "交出灵根,饶你不死!少年嘴角微扬,怀中玉佩散发幽幽蓝光..."
    },
    "optimized_content": {
      "title_seo": "玄幻世界灵根觉醒-修仙小说连载-第三章初入宗门",
      "description_seo": "少年林逸偶得上古传承,踏上修仙之路。家族追杀、宗门争斗,看他如何逆天改命。玄幻世界修仙小说连载中。",
      "keywords": ["玄幻世界", "修仙", "灵根", "上古传承", "云霄宗", "炼气", "逆袭"],
      "meta_tags": {"category": "玄幻", "tags": "修仙,逆袭,热血"}
    },
    "audit_passed": true,
    "publish_results": [
      {"platform": "zhihu", "post_id": "zh_123456", "url": "https://zhuanlan.zhihu.com/p/123456", "status": "published"},
      {"platform": "toutiao", "post_id": "tt_789012", "url": "https://toutiao.com/article/789012", "status": "published"},
      {"platform": "wechat_official", "post_id": "wx_345678", "url": "https://mp.weixin.qq.com/s/345678", "status": "published"}
    ],
    "publish_status": {
      "book_id": "novel_20260720_001",
      "chapter_number": 3,
      "status": "published",
      "published_at": "2026-07-20T15:30:00Z",
      "platform_urls": ["https://zhuanlan.zhihu.com/p/123456", "https://toutiao.com/article/789012", "https://mp.weixin.qq.com/s/345678"]
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓黄金三章打磨(钩子+人设+冲突) ✓3章共9053字(每章约3000字) ✓品牌词注入(玄幻世界/修仙) ✓8步全流程完成 ✓三平台发布成功

### 案例2: 都市小说章节生成+营销注入(SEO优化)

**输入**:
```json
{
  "genre": "urban",
  "chapter_words": 3000,
  "count": 5,
  "brand_keywords": ["都市职场", "逆袭人生"]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "book_id": "novel_20260720_002",
    "chapters": [
      {"chapter_number": 1, "title": "第一章 被裁员的那天", "content": "周一早晨,陈默像往常一样走进公司。只是这一次,HR已经在会议室等着他了...", "word_count": 3008},
      {"chapter_number": 2, "title": "第二章 意外继承", "content": "整理遗物时,陈默发现了父亲留下的一个旧皮箱。打开的瞬间,他愣住了...", "word_count": 2975},
      {"chapter_number": 3, "title": "第三章 第一桶金", "content": "用继承的资金,陈默开始了第一次投资。他押注的那个赛道,正在悄然爆发...", "word_count": 3022},
      {"chapter_number": 4, "title": "第四章 旧同事的震惊", "content": "半年后的同学聚会上,曾经看不起他的前同事看到他的名片时,表情精彩极了...", "word_count": 2988},
      {"chapter_number": 5, "title": "第五章 新的挑战", "content": "就在一切看似顺风顺水时,一个意想不到的人出现了,带着一个无法拒绝的提议...", "word_count": 3001}
    ],
    "marketing_copy": {
      "title": "都市职场:逆袭人生",
      "description": "被裁员的程序员意外继承神秘资产,从谷底到巅峰的都市逆袭之路。商战、投资、人情冷暖,尽在都市职场逆袭人生!",
      "tags": ["都市职场", "逆袭人生", "商战", "投资", "连载"],
      "cover_suggestion": "都市天际线背景,一个西装革履的背影从阴影走向光明",
      "excerpt": "被裁员那天,陈默以为人生完了。直到他打开父亲的旧皮箱..."
    },
    "optimized_content": {
      "title_seo": "都市职场逆袭人生-被裁员后意外继承-都市小说连载",
      "description_seo": "程序员陈默被裁员后意外继承神秘资产,开启都市逆袭之路。商战投资、人情冷暖,都市职场逆袭人生小说连载。",
      "keywords": ["都市职场", "逆袭人生", "裁员", "继承", "投资", "商战", "程序员"],
      "meta_tags": {"category": "都市", "tags": "职场,逆袭,商战"}
    },
    "audit_passed": true,
    "publish_results": [],
    "publish_status": {"book_id": "novel_20260720_002", "chapter_number": 5, "status": "draft", "published_at": null, "platform_urls": []}
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓5章批量生成(共14994字) ✓都市题材模板正确应用 ✓品牌词注入(都市职场/逆袭人生) ✓SEO标题/描述/关键词优化 ✓审核通过(无敏感词)

### 案例3: API超时降级(批量→单章生成)

**输入**:
```json
{
  "genre": "mystery",
  "chapter_words": 3000,
  "count": 10
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "book_id": "novel_20260720_003",
    "chapters": [
      {
        "chapter_number": 1,
        "title": "第一章 消失的房客",
        "content": "老旧公寓楼404室的房客已经三天没有出现了。房东王阿姨敲门时,门缝里渗出的气味让她立刻报了警。刑警李峰到达现场后,发现房间里的东西摆放得整整齐齐,唯独缺少了一样东西——房客的身份证。一个活人,怎么可能只带走身份证,却留下手机、钱包和所有衣物?",
        "word_count": 3015
      }
    ],
    "marketing_copy": {"title": "消失的房客", "description": "404室房客神秘失踪...", "tags": ["悬疑", "推理", "连载"], "cover_suggestion": "", "excerpt": "活人怎么可能只带走身份证?"},
    "optimized_content": {"title_seo": "消失的房客-悬疑推理小说连载", "description_seo": "404室房客神秘失踪...", "keywords": ["悬疑", "推理", "失踪"], "meta_tags": {}},
    "audit_passed": true,
    "publish_results": [],
    "publish_status": {"book_id": "novel_20260720_003", "chapter_number": 1, "status": "draft", "published_at": null, "platform_urls": []}
  },
  "error": "章节生成API超时(10章批量请求超过30秒),已降级为单章生成,仅完成第1章。建议重新调用生成后续章节。",
  "code": "GENERATE_TIMEOUT_DOWNGRADE"
}
```

**效果验证**: ✓API超时正确降级(10章→1章) ✓降级原因在error字段标注 ✓悬疑题材模板正确应用 ✓第1章质量不受影响(3015字) ✓错误码GENERATE_TIMEOUT_DOWNGRADE正确返回

### 案例4: 敏感词阻断发布(返回替换建议)

**输入**:
```json
{
  "genre": "history",
  "chapter_words": 3000,
  "count": 1
}
```

**LLM生成输出**:
```json
{
  "success": false,
  "data": {
    "book_id": "novel_20260720_004",
    "chapters": [
      {"chapter_number": 1, "title": "第一章 朝堂风云", "content": "建安十三年,丞相曹操率大军南下...", "word_count": 2998}
    ],
    "marketing_copy": {"title": "朝堂风云", "description": "...", "tags": ["历史"], "cover_suggestion": "", "excerpt": ""},
    "optimized_content": {"title_seo": "朝堂风云-历史小说", "description_seo": "...", "keywords": ["历史"], "meta_tags": {}},
    "audit_passed": false,
    "sensitive_words": ["[敏感词1]", "[敏感词2]"],
    "suggested_replacements": {"[敏感词1]": "[替换词A]", "[敏感词2]": "[替换词B]"},
    "publish_results": [],
    "publish_status": {"book_id": "novel_20260720_004", "chapter_number": 1, "status": "blocked", "published_at": null, "platform_urls": []}
  },
  "error": "内容审核未通过:发现2处敏感词,已阻断发布。请根据suggested_replacements修改后重新发布。",
  "code": "SENSITIVE_WORDS_FOUND"
}
```

**效果验证**: ✓敏感词审核正确检测(2处) ✓发布正确阻断(blocked) ✓替换建议返回 ✓错误码SENSITIVE_WORDS_FOUND正确返回 ✓内容已生成仅阻断发布(不浪费)

## 常见问题

### Q1: 如何开始使用网文全自动写手?
A: 三步启动:(1)将SKILL.md放入Agent的skills目录;(2)确认Agent环境变量已配置LLM_API_KEY(通常由Agent内置);(3)调用init_novel传入genre和chapter_words即可开始。如需自动发布,额外配置对应平台的PLATFORM_API_KEY;不配置也可手动复制发布.
### Q2: 章节生成API超时怎么办?
A: 系统会自动降级为单章生成模式,仅生成1章而非批量10章。如频繁超时,建议:(1)减小chapter_words到2000以下;(2)减小count到3以下;(3)检查LLM服务稳定性;(4)切换为响应更快的国内LLM(如DeepSeek/通义千问).
### Q3: 敏感词审核阻断发布如何处理?
A: 审核返回sensitive_words列表和suggested_replacements建议替换。处理方式:(1)按建议替换敏感词后重新调用check_sensitive_words;(2)手动调整剧情规避敏感话题;(3)如确认为误报,可人工确认后跳过审核(标注warning).
### Q4: 平台发布失败但内容已生成,如何补救?
A: 内容已生成并保存在chapters字段中,即使发布失败也不会丢失。处理方式:(1)查看publish_results中各平台status字段,定位失败平台;(2)手动复制optimized_content和marketing_copy到对应平台发布;(3)如全部平台失败,检查PLATFORM_API_KEY配置是否正确.
### Q5: 黄金三章和普通章节有什么区别?
A: 黄金三章(前三章)会重点打磨三个维度:(1)开篇钩子(前300字抓注意力);(2)人设建立(主角性格/动机/背景);(3)冲突铺垫(核心矛盾初现)。普通章节(第四章起)更侧重剧情推进和连贯性。建议新作品优先确保黄金三章质量以提升读者留存率.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **LLM依赖**: ;章节质量受底层模型能力限制,小模型可能出现剧情断裂或人设不一致
- **字数精度**: 实际生成字数可能有±5%偏差(LLM Token计算与中文字符不完全对应),chapter_words为目标值非精确值
- **题材模板固定**: 仅支持6大题材(都市/玄幻/历史/科幻/悬疑/言情),不支持跨界融合题材(如科幻+玄幻混合)
- **平台限制**: 仅支持知乎/头条/微信公众号三平台自动分发,不支持起点/晋江/番茄等网文平台API自动发布
- **敏感词库时效**: 敏感词库依赖LLM内置知识,可能滞后于最新监管要求,发布前建议人工复核
- **章节连贯性**: 批量生成10章时,后段章节可能出现剧情细节与前段不一致,建议生成后人工通读校对
- **并发限制**: 单次调用仅支持一本书的章节生成,不支持多本书并行写作

## 安全

### API Key 零暴露原则
- **环境变量注入**: 所有API Key(LLM_API_KEY/PLATFORM_API_KEY)必须通过Agent环境变量注入,严禁在SKILL.md、配置文件或代码中硬编码
- **本文件无Key示例**: 本SKILL.md中不包含任何真实或示例API Key,所有引用均使用 `$env:LLM_API_KEY` 占位
- **日志脱敏**: exec工具记录日志时,自动过滤包含"key"/"token"/"secret"字段的值
- **平台鉴权隔离**: 各平台API Key独立配置,互不通用,避免单平台泄露影响其他平台

### 内容安全
- **敏感词审核**: 发布前强制执行check_sensitive_words,阻断含违禁词的内容发布
- **平台合规**: 自动适配各平台内容规范(知乎/头条/微信公众号),过滤平台禁发内容
- **版权提示**: 生成的网文内容基于LLM创作,用户需自行确认不侵犯他人版权,商业使用前建议查重
