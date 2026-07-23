---
slug: ebook-factory
name: ebook-factory
version: "1.0.1"
displayName: "电子书工厂"
summary: "三天写完一本专业电子书,Markdown输入EPUB输出,KDP/微信读书多平台发布"
license: Proprietary
description: |-
  电子书工厂是一款从Markdown大纲生成完整电子书的工具。支持逐节生成、多格式导出(EPUB/PDF)、
  多平台发布(KDP/微信读书/豆瓣阅读)、封面图生成。三天写完一本专业电子书。

  核心能力:
  - Markdown驱动结构化写作:三级大纲自动解析为目录树,支持预览确认
  - 逐节生成+自动汇总:每节500-3000字,支持断点续写
  - 多格式导出:EPUB(Kindle/手机阅读器)、PDF(印刷版)、Markdown(源文件备份)
  - 多平台发布:KDP/微信读书/豆瓣阅读,自动适配各平台格式要求
  - 封面图与版权页自动生成:调用图像API生成封面,自动生成版权页
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tags: [内容创作, 电子书, 出版, 知识付费]
tools:
  - read
  - exec
pricing_rationale: "文案创作类, large市场, enterprise复杂度, daily频次, standard层 → 高频通用工具,大市场,低单价走量"
---
# 电子书工厂

从Markdown大纲生成完整电子书,支持逐节生成、多格式导出(EPUB/PDF)、多平台发布(KDP/微信读书/豆瓣阅读)、封面图生成。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

1. **Markdown驱动结构化写作**:用户用三级Markdown(主标题# /章节标题## /section标题###)编写大纲,工具自动解析为目录树,支持书籍目录树(JSON格式)预览确认
2. **逐节生成+自动汇总**:按大纲顺序逐节生成内容,每节500-3000字,生成完成后自动汇总为完整电子书,支持断点续写
3. **多格式导出**:EPUB(电子书标准格式,适配Kindle/微信读书/手机阅读器)、PDF(印刷版格式,适配打印分发)、Markdown(源文件备份)
4. **多平台发布**:KDP(亚马逊Kindle Direct Publishing)、微信读书、豆瓣阅读,自动适配各平台格式要求(封面尺寸/章节结构/元数据)
5. **封面图与版权页自动生成**:调用图像生成API生成书籍封面图(支持自定义风格描述),自动生成版权页(书名/作者/出版日期/版权声明/ISBN占位)
#
## 适用场景

| 场景 | 输入 | 输出 | 是否适用 |
|:-----|:-----|:-----|:---------|
| 知识付费电子书制作 | Markdown大纲+主题 | EPUB/PDF电子书+封面+版权页 | 适用 |
| 专业技能书出版 | 大纲+专业技能内容 | 多格式电子书+多平台发布 | 适用 |
| 内容沉淀整理 | 已有文章系列+大纲结构 | 整合电子书 | 适用 |
| 系列丛书批量生产 | 多个大纲+统一风格 | 多本电子书批量生成 | 适用 |
| 实时交互式写作对话 | 实时对话式内容共创 | 不适用(本Skill为大纲驱动批量生成) | 不适用 |
| 纸质书印刷排版设计 | 印刷级专业排版设计 | 不适用(本Skill输出PDF为标准排版非印刷级) | 不适用 |
| 有声书音频制作 | 文字转语音音频 | 不适用(本Skill主输出电子书文本非音频) | 不适用 |

## 使用流程

### Step 1: 提供书籍大纲
- 用户用Markdown编写大纲,三级结构:
  - `# 主标题` (书名,1个)
  - `## 章节标题` (章节,多个)
  - `### section标题` (小节,每章节下多个)
- 提供书籍主题、目标读者、写作风格(可选)

**大纲示例**:
```markdown
# Python自动化实战

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,参考错误处理章节获取恢复步骤。


## 第一章 自动化基础
### 1.1 为什么要自动化
### 1.2 Python自动化工具生态

## 第二章 办公自动化
### 2.1 Excel自动化处理
### 2.2 Word文档批量生成
```

### Step 2: 目录树预览与确认
- 解析大纲生成目录树(JSON格式)
- 展示目录树供用户确认
- 用户可调整章节结构(增删改)
- 确认后进入生成阶段

### Step 3: 逐节生成内容
- 按目录树顺序逐节生成,每节500-3000字
- 每节生成时注入:书名/章节上下文/前文摘要/目标读者/写作风格
- 支持断点续写(记录已生成section_id)
- 生成失败时重试,3次失败跳过该节并标记

### Step 4: 汇总成书
- 将所有section按目录树顺序拼接
- 自动生成目录页(TOC)
- 自动生成版权页(书名/作者/出版日期/版权声明/ISBN占位)
- 输出完整Markdown书籍文件

### Step 5: 封面图生成
- 调用图像生成API生成封面图
- 输入:书名+主题+风格描述(可选)
- 输出:封面图PNG文件(适配EPUB封面尺寸)

### Step 6: 多格式导出
- **EPUB导出**:Markdown→EPUB转换,嵌入封面图,生成标准EPUB文件
- **PDF导出**:Markdown→PDF转换,标准排版(非印刷级)
- **Markdown备份**:保留原始Markdown源文件

### Step 7: 多平台发布(可选)
- **KDP(亚马逊)**:适配Kindle格式,上传EPUB,填写元数据(书名/作者/分类/价格)
- **微信读书**:适配微信读书格式,上传EPUB
- **豆瓣阅读**:适配豆瓣阅读格式,上传EPUB
- 各平台发布结果独立记录,失败不阻塞其他平台

## 输入格式

### 提供大纲
```json
{
  "action": "generate",
  "book_title": "Python自动化实战",
  "outline_markdown": "# Python自动化实战\n## 第一章 自动化基础\n

### 1.1 为什么要自动化\n### 1.2 Python自动化工具生态",
  "target_audience": "Python初学者到中级开发者",
  "writing_style": "实用教程风格,代码示例丰富",
  "cover_style": "技术书籍封面,蓝色科技感",
  "platforms": ["kdp", "wechat_read", "douban_read"]
}
```

### 预览目录树
```json
{"action": "preview_outline", "outline_markdown": "# 书名\n## 章节\n### 小节"}
```

## 输出格式

```json
{
  "success": true,
  "data": {
    "book_id": "book_20260717_001",
    "book_title": "Python自动化实战",
    "outline_tree": {"title": "Python自动化实战", "chapters": [...]},
    "sections_generated": 15,
    "total_words": 25000,
    "files": {
      "markdown": "output/books/book_20260717_001/book.md",
      "epub": "output/books/book_20260717_001/book.epub",
      "pdf": "output/books/book_20260717_001/book.pdf",
      "cover": "output/books/book_20260717_001/cover.png"
    },
    "publish_results": [
      {"platform": "kdp", "success": true, "book_url": "..."},
      {"platform": "wechat_read", "success": true, "book_url": "..."}
    ]
  },
  "error": null,
  "code": null
}
```

## 异常处理


| 异常场景 | 原因 | 处理方式 | 错误码 |
|:---------|:-----|:---------|:-------|
| 大纲格式错误 | Markdown结构不规范(缺少#或层级混乱) | 返回错误+正确格式示例 | OUTLINE_FORMAT_ERROR |
| section生成失败 | LLM调用失败或超时 | 3次,仍失败跳过该节并标记SECTION_FAILED | SECTION_FAILED |
| 封面图生成失败 | 图像API不可用 | 跳过封面,使用默认封面,不阻塞 | COVER_FAILED |
| EPUB转换失败 | Markdown→EPUB转换错误 | 返回错误,检查Markdown格式 | EPUB_CONVERT_ERROR |
| PDF转换失败 | Markdown→PDF转换错误 | 返回错误,检查Markdown格式 | PDF_CONVERT_ERROR |
| 平台发布失败 | 平台API不可用或鉴权失败 | 记录失败平台,不阻塞其他平台 | PUBLISH_FAILED |
| 断点续写冲突 | 同一book_id正在生成中 | 返回错误,提示稍后 | BOOK_LOCKED |

## 数据存储

| 存储位置 | 说明 |
|:---------|:-----|
| output/books/{book_id}/book.md | 完整电子书Markdown源文件 |
| output/books/{book_id}/book.epub | EPUB格式电子书 |
| output/books/{book_id}/book.pdf | PDF格式电子书 |
| output/books/{book_id}/cover.png | 封面图 |
| output/books/{book_id}/outline.json | 目录树JSON |
| output/books/{book_id}/progress.json | 生成进度(支持断点续写) |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:-------|:-----|:---------|:---------|:-------------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | DeepSeek/通义千问/文心一言/Kimi等国内模型 |
| 图像生成API | API | 可选 | 封面图生成(可跳过使用默认封面) | 通义万相/文心一格/即时AI等国内绘画API |
| Markdown转EPUB | 工具 | 必需 | pandoc(开源工具) | 系统包管理器安装,无海外依赖 |
| Markdown转PDF | 工具 | 可选 | pandoc+LaTeX或wkhtmltopdf | 系统包管理器安装,无海外依赖 |
| JSON文件存储 | 文件系统 | 必需 | exec工具创建output/books/目录 | 本地文件系统,无海外依赖 |

### API Key 配置与安全要求
- **LLM_API_KEY**: 必需(通常由Agent内置) - 逐节内容生成
- **IMAGE_API_KEY**: 可选 - 封面图生成(可跳过使用默认封面)
- 配置方式: 在Agent的环境变量中设置
- **零暴露原则**: API Key必须通过环境变量注入(如`$env:IMAGE_API_KEY`),严禁硬编码在SKILL.md或脚本源码中;所有示例代码中Key位置使用环境变量占位符;禁止在日志、错误信息、输出JSON中打印Key明文

### 使用流程
封面图生成失败时跳过使用默认封面,不阻塞。EPUB/PDF转换依赖pandoc(开源工具),无海外依赖。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 完整电子书生成

**输入**:
```json
{
  "action": "generate",
  "book_title": "Python自动化实战",
  "outline_markdown": "# Python自动化实战\n## 第一章 自动化基础\n

### 1.1 为什么要自动化\n### 1.2 Python自动化工具生态\n## 第二章 办公自动化\n### 2.1 Excel自动化处理\n### 2.2 Word文档批量生成",
  "target_audience": "Python初学者到中级开发者",
  "writing_style": "实用教程风格,代码示例丰富",
  "cover_style": "技术书籍封面,蓝色科技感",
  "platforms": ["kdp", "wechat_read"]
}
```

**执行流程**: 解析大纲→预览目录树→逐节生成(4节)→汇总成书→生成封面图→EPUB导出→PDF导出→KDP发布→微信读书发布

**输出**:
```json
{
  "success": true,
  "data": {
    "book_id": "book_20260717_001",
    "book_title": "Python自动化实战",
    "sections_generated": 4,
    "total_words": 8500,
    "files": {
      "markdown": "output/books/book_20260717_001/book.md",
      "epub": "output/books/book_20260717_001/book.epub",
      "pdf": "output/books/book_20260717_001/book.pdf",
      "cover": "output/books/book_20260717_001/cover.png"
    },
    "publish_results": [
      {"platform": "kdp", "success": true, "book_url": "https://kdp.amazon.com/book/xxx"},
      {"platform": "wechat_read", "success": true, "book_url": "https://weread.qq.com/book/yyy"}
    ]
  },
  "error": null,
  "code": null
}
```

### 示例2: 目录树预览

**输入**:
```json
{"action": "preview_outline", "outline_markdown": "# Python自动化实战\n## 第一章 自动化基础\n

### 1.1 为什么要自动化\n### 1.2 Python自动化工具生态"}
```

**输出**:
```json
{
  "success": true,
  "data": {
    "outline_tree": {
      "title": "Python自动化实战",
      "chapters": [
        {
          "title": "第一章 自动化基础",
          "sections": [
            {"title": "1.1 为什么要自动化"},
            {"title": "1.2 Python自动化工具生态"}
          ]
        }
      ]
    },
    "total_chapters": 1,
    "total_sections": 2
  },
  "error": null,
  "code": null
}
```

### 示例3: section生成失败跳过

**输入**: 部分section生成失败
```json
{"action": "generate", "book_title": "测试书", "outline_markdown": "# 测试书\n## 第一章\n

### 1.1 节\n### 1.2 节"}
```

**输出**: 1.2节生成失败跳过
```json
{
  "success": true,
  "data": {
    "book_id": "book_20260717_002",
    "book_title": "测试书",
    "sections_generated": 1,
    "sections_failed": 1,
    "failed_sections": ["1.2 节"],
    "total_words": 2000,
    "files": {"markdown": "output/books/book_20260717_002/book.md", "epub": "output/books/book_20260717_002/book.epub"}
  },
  "error": "1个section生成失败已跳过",
  "code": "SECTION_FAILED"
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 知识付费电子书制作(Python自动化,EPUB+PDF+封面)

**输入**:
```json
{
  "action": "generate",
  "book_title": "Python自动化实战",
  "outline_markdown": "# Python自动化实战\n## 第一章 自动化基础\n

### 1.1 为什么要自动化\n### 1.2 Python自动化工具生态\n## 第二章 办公自动化\n### 2.1 Excel自动化处理\n### 2.2 Word文档批量生成\n## 第三章 网页自动化\n### 3.1 网页数据抓取\n### 3.2 自动化测试入门",
  "target_audience": "Python初学者到中级开发者",
  "writing_style": "实用教程风格,代码示例丰富",
  "cover_style": "技术书籍封面,蓝色科技感",
  "platforms": ["kdp", "wechat_read", "douban_read"]
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "book_id": "book_20260720_001",
    "book_title": "Python自动化实战",
    "outline_tree": {
      "title": "Python自动化实战",
      "chapters": [
        {"title": "第一章 自动化基础", "sections": ["1.1 为什么要自动化", "1.2 Python自动化工具生态"]},
        {"title": "第二章 办公自动化", "sections": ["2.1 Excel自动化处理", "2.2 Word文档批量生成"]},
        {"title": "第三章 网页自动化", "sections": ["3.1 网页数据抓取", "3.2 自动化测试入门"]}
      ]
    },
    "sections_generated": 6,
    "total_words": 18500,
    "files": {
      "markdown": "output/books/book_20260720_001/book.md",
      "epub": "output/books/book_20260720_001/book.epub",
      "pdf": "output/books/book_20260720_001/book.pdf",
      "cover": "output/books/book_20260720_001/cover.png"
    },
    "publish_results": [
      {"platform": "kdp", "success": true, "book_url": "https://kdp.amazon.com/book/B0XXXXX"},
      {"platform": "wechat_read", "success": true, "book_url": "https://weread.qq.com/book/XXXXX"},
      {"platform": "douban_read", "success": true, "book_url": "https://read.douban.com/book/XXXXX"}
    ]
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓6个section全部生成(18500字) ✓EPUB/PDF/Markdown三格式导出 ✓封面图自动生成(蓝色科技感) ✓三平台发布成功 ✓目录树结构正确解析

### 案例2: 目录树预览(preview_outline,结构校验)

**输入**:
```json
{
  "action": "preview_outline",
  "outline_markdown": "# AI写作指南\n## 第一章 AI写作基础\n

### 1.1 什么是AI写作\n### 1.2 AI写作工具对比\n## 第二章 提示词工程\n### 2.1 提示词基础\n### 2.2 高级提示词技巧"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "book_title": "AI写作指南",
    "outline_tree": {
      "title": "AI写作指南",
      "chapters": [
        {"chapter_index": 1, "title": "第一章 AI写作基础", "sections": [{"section_index": "1.1", "title": "什么是AI写作"}, {"section_index": "1.2", "title": "AI写作工具对比"}]},
        {"chapter_index": 2, "title": "第二章 提示词工程", "sections": [{"section_index": "2.1", "title": "提示词基础"}, {"section_index": "2.2", "title": "高级提示词技巧"}]}
      ]
    },
    "total_chapters": 2,
    "total_sections": 4,
    "validation": "passed"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓三级Markdown结构正确解析 ✓2章4节目录树完整生成 ✓章节/小节编号自动识别 ✓校验通过(validation=passed) ✓输出格式合规

### 案例3: 断点续写(部分章节已生成,继续未完成章节)

**输入**:
```json
{
  "action": "generate",
  "book_title": "副业赚钱指南",
  "outline_markdown": "# 副业赚钱指南\n## 第一章 副业认知\n

### 1.1 副业的本质\n### 1.2 常见副业误区\n## 第二章 副业实操\n### 2.1 自媒体副业\n### 2.2 电商副业",
  "target_audience": "想做副业的上班族",
  "writing_style": "通俗易懂,案例驱动",
  "resume_from": "2.1"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "book_id": "book_20260720_002",
    "book_title": "副业赚钱指南",
    "sections_generated": 2,
    "sections_resumed": ["2.1 自媒体副业", "2.2 电商副业"],
    "total_words": 6200,
    "files": {
      "markdown": "output/books/book_20260720_002/book.md",
      "epub": "output/books/book_20260720_002/book.epub",
      "pdf": "output/books/book_20260720_002/book.pdf",
      "cover": "output/books/book_20260720_002/cover.png"
    },
    "resume_info": {
      "previous_sections": ["1.1 副业的本质", "1.2 常见副业误区"],
      "resumed_from": "2.1 自媒体副业",
      "all_sections_complete": true
    }
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓断点续写从2.1正确恢复 ✓前2节已有内容保留 ✓后续2节成功生成 ✓all_sections_complete=true(全书完成) ✓EPUB/PDF重新汇总导出

### 案例4: 封面图生成失败降级(使用默认封面)

**输入**:
```json
{
  "action": "generate",
  "book_title": "时间管理手册",
  "outline_markdown": "# 时间管理手册\n## 第一章 时间管理概述\n

### 1.1 为什么需要时间管理\n## 第二章 实用技巧\n### 2.1 番茄工作法\n### 2.2 GTD方法",
  "target_audience": "职场人士",
  "cover_style": "简约商务风格"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "book_id": "book_20260720_003",
    "book_title": "时间管理手册",
    "sections_generated": 3,
    "total_words": 8500,
    "files": {
      "markdown": "output/books/book_20260720_003/book.md",
      "epub": "output/books/book_20260720_003/book.epub",
      "pdf": "output/books/book_20260720_003/book.pdf",
      "cover": "output/books/book_20260720_003/cover_default.png"
    },
    "publish_results": []
  },
  "error": "封面图生成失败(图像API不可用),已使用默认封面,不影响电子书内容",
  "code": "COVER_FAILED"
}
```

**效果验证**: ✓封面图生成失败正确降级 ✓默认封面使用(cover_default.png) ✓电子书内容不受影响(3节8500字) ✓EPUB/PDF正常导出 ✓错误码COVER_FAILED正确返回

### 案例5: 大纲格式错误(层级跳跃,返回格式示例)

**输入**:
```json
{
  "action": "generate",
  "book_title": "测试书籍",
  "outline_markdown": "# 测试书籍\n### 直接跳到小节"
}
```

**LLM生成输出**:
```json
{
  "success": false,
  "data": null,
  "error": "大纲格式错误:层级跳跃(从#直接到###,缺少##章节标题)。正确格式: # 主标题 → ## 章节标题 → ### section标题,层级不能跳跃。",
  "code": "OUTLINE_FORMAT_ERROR"
}
```

**效果验证**: ✓大纲格式错误正确检测(层级跳跃) ✓错误原因清晰描述 ✓正确格式示例提示 ✓错误码OUTLINE_FORMAT_ERROR正确返回 ✓不执行生成(避免错误输出)

## 常见问题

### Q1: 大纲Markdown格式有什么要求?
A: 大纲必须使用三级Markdown结构:`# 主标题`(书名,1个) / `## 章节标题`(章节,多个) / `### section标题`(小节,每章节下多个)。层级不能跳跃(如#直接到###)。格式不规范返回OUTLINE_FORMAT_ERROR错误并给出正确格式示例。建议先用preview_outline预览目录树确认结构无误后再生成。

### Q2: section生成失败怎么办?
A: 单个section生成失败会重试3次,仍失败则跳过该节并标记SECTION_FAILED,不阻塞其他section生成。最终电子书会包含已成功生成的section,失败section位置会留空标记。建议:1)检查LLM服务是否正常;2)重新生成失败的section(提供section_id);3)手动补充失败section内容。

### Q3: 支持哪些发布平台?格式有什么差异?
A: 支持KDP(亚马逊Kindle)、微信读书、豆瓣阅读。各平台格式要求:KDP需要EPUB格式+封面图(推荐1600x2560)+元数据(书名/作者/分类/价格);微信读书需要EPUB格式;豆瓣阅读需要EPUB格式。各平台发布独立执行,一个平台失败不阻塞其他平台(PUBLISH_FAILED)。

### Q4: 断点续写如何工作?
A: 生成进度保存在progress.json文件中,记录已生成的section_id。如果生成中断(如LLM超时或手动停止),下次使用相同book_id继续生成时,会从上次中断的section继续,跳过已生成的section。同一book_id正在生成时再次请求会返回BOOK_LOCKED错误,需等待前一个完成。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **PDF为标准排版非印刷级**:PDF导出为标准排版(适合电子阅读和普通打印),不支持印刷级专业排版(如bleed/CMYK/字体嵌入等印刷要求),需印刷级排版请使用专业排版软件
2. **section生成失败跳过不补全**:section生成失败3次后跳过,最终电子书该section位置留空,需手动补充,不会自动重试补全
3. **封面图生成依赖图像API**:封面图生成依赖图像生成API,API不可用时使用默认封面(COVER_FAILED),无法自定义封面
4. **EPUB/PDF转换依赖pandoc**:EPUB和PDF格式转换依赖pandoc开源工具,未安装pandoc时无法导出对应格式(EPUB_CONVERT_ERROR/PDF_CONVERT_ERROR)
5. **不支持实时交互式写作**:本Skill为大纲驱动批量生成模式,不支持实时对话式内容共创,需先提供完整大纲再批量生成

## 变更历史

| 版本 | 日期 | 变更说明 |
|:-----|:-----|:---------|
| v1.0.0 | 2026-07-17 | 初版创建,Markdown大纲驱动+逐节生成+多格式导出+多平台发布+封面生成+断点续写 |
