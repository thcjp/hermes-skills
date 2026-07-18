---
slug: ebook-factory
name: ebook-factory
version: "1.0.0"
displayName: "电子书流水线"
summary: "一个人就是一家出版社,选题到成书全自动,AI逐章生成+封面+PDF/EPUB双输出"
license: MIT
description: |-
  电子书流水线——一个人就是一家出版社,从主题大纲到成品电子书一键成书,AI逐章生成双格式输出。

  核心能力: 主题大纲解析 / AI逐章连贯生成 / 封面图自动生成 / Markdown排版 / PDF+EPUB双格式输出 / 自定义样式模板

  适用场景: 知识IP打包课程资料变现 / 博主文章合集成书 / 副业达人做电子书变现 / 教程系列结构化输出 / 企业白皮书制作

  差异化: 无大纲时AI自动生成3-5章默认结构,从选题到成书全自动;AI逐章生成保持逻辑连贯不跑题;封面图自动生成,PDF/EPUB双格式输出,排版失败降级保留Markdown源文件确保不丢内容。

  触发关键词: 电子书生成、教程打包、课程资料导出、电子书制作、出书、书籍编排、知识打包
homepage: "https://skillhub.cn"
tags: [电子书, 知识变现, 内容创作, 自动化]
tools: [read, exec]
---

# 电子书流水线 Ebook Factory

通用电子书生成器,支持从主题大纲到成品电子书的完整流程。AI逐章生成内容,自动编排章节,生成封面图,输出PDF/EPUB格式。

## 使用场景

- 将知识体系打包为电子书(如"AI运营实战指南")
- 课程资料导出为可分发格式
- 教程系列整理为结构化电子书
- 博客/文章合集编排为电子书
- 系列内容一键成书分发

## 工作流

1. **接收主题和大纲**: 读取用户提供的电子书主题、目标读者、章节大纲。若无大纲则AI根据主题自动生成章节结构
2. **AI逐章生成内容**: 按章节顺序调用AI生成每章内容,每章包含标题、正文、小结。章节间保持逻辑连贯
3. **封面图生成**: 根据电子书主题生成封面图。封面需包含书名和视觉主题元素
4. **排版格式化**: 将所有章节内容合并为Markdown,添加目录、页眉页脚、章节分隔。支持自定义样式模板
5. **输出PDF/EPUB**: 调用排版工具将Markdown转换为PDF和EPUB格式。输出文件保存到指定目录

## 输入格式

```json
{
  "topic": "AI运营实战指南",
  "audience": "电商从业者",
  "chapters": ["AI选品策略", "AI文案写作", "AI客服自动化", "AI数据分析"],
  "format": "pdf",
  "output_dir": "./output/ebooks"
}
```

字段说明:
- `topic`: 电子书主题
- `audience`: 目标读者
- `chapters`: 章节大纲(为空时AI自动生成3-5章默认结构)
- `format`: 输出格式(pdf/epub/both)
- `output_dir`: 输出目录(不存在时自动创建)

## 输出格式

```json
{
  "success": true,
  "data": {
    "topic": "AI运营实战指南",
    "chapters_generated": 4,
    "cover_image": "./output/ebooks/ai-ops-guide-cover.png",
    "output_files": ["./output/ebooks/ai-ops-guide.pdf", "./output/ebooks/ai-ops-guide.epub"],
    "total_words": 12000
  },
  "error": null,
  "code": null
}
```

## 异常处理

| 异常场景 | 处理方式 | 降级策略 |
|:---------|:---------|:---------|
| AI章节生成失败 | 重试1次,仍失败则跳过该章 | 标记章节为"待完善",继续后续章节 |
| 封面图生成失败 | 跳过封面步骤 | 使用纯文本封面,不影响正文输出 |
| 排版转换失败 | 输出原始Markdown | 保留Markdown源文件作为备选 |
| 章节大纲为空 | AI自动生成大纲 | 基于主题生成3-5章默认结构 |
| 输出目录不存在 | 自动创建目录 | 无 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 |
| 封面图生成 | API | 可选 | AI绘画引擎(失败时使用纯文本封面) |
| PDF/EPUB转换工具 | 工具 | 可选 | pandoc/calibre等(失败时输出Markdown) |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - 逐章生成内容/大纲生成
- **IMAGE_API_KEY**: 可选 - 封面图生成(可跳过)
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
排版转换失败时输出原始Markdown。封面图生成失败时使用纯文本封面。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例: 生成"AI运营实战指南"电子书

输入:
```json
{
  "topic": "AI运营实战指南",
  "audience": "电商从业者",
  "chapters": ["AI选品策略", "AI文案写作", "AI客服自动化", "AI数据分析"],
  "format": "pdf",
  "output_dir": "./output/ebooks"
}
```

执行流程: 接收大纲 → 逐章生成4章内容 → 生成封面图 → 合并排版 → 输出PDF+EPUB

输出:
```json
{
  "success": true,
  "data": {
    "topic": "AI运营实战指南",
    "chapters_generated": 4,
    "cover_image": "./output/ebooks/ai-ops-guide-cover.png",
    "output_files": ["./output/ebooks/ai-ops-guide.pdf"],
    "total_words": 12000
  }
}
```

### 示例: 无大纲自动生成

输入:
```json
{
  "topic": "短视频运营入门",
  "audience": "新媒体新手",
  "chapters": [],
  "format": "both",
  "output_dir": "./output/ebooks"
}
```

执行流程: AI根据主题生成5章大纲 → 逐章生成内容 → 生成封面 → 输出PDF+EPUB
