---
slug: poetry-craftsman
name: poetry-craftsman
version: "1.0.0"
displayName: "诗词匠心"
summary: "一人做古诗词内容厂牌,6种融合模式+平仄校验+意境评分,图文短视频双输出"
license: MIT
description: |-
  诗词匠心——一人做古诗词内容厂牌,6种融合模式让诗词自然融入故事,平仄校验意境评分双保障。

  核心能力: 6种融合模式(直接引用/化用/意境延伸/正经对比/打油诗改编/双角色对比) / 平仄韵律自动校验 / 意境融合度评分 / 图文+短视频脚本双输出 / 画外音解说 / 诗词数据库查询

  适用场景: 历史内容创作者 / 古风IP运营者 / 教育内容生产者 / 副业达人做古诗词短视频 / 文化类博主

  差异化: 6种融合模式覆盖从正经到搞笑全风格,打油诗改编和双角色对比制造反差爆款;平仄韵律自动校验保证专业度,意境融合度评分量化评估,图文短视频双输出适配多平台。

  触发关键词: 故事中融入诗词、诗词化用、古风故事创作、历史人物故事编写、打油诗、古诗短视频、古诗图文、平仄校验
homepage: "https://skillhub.cn"
tags: [古诗词, 内容创作, 短视频, 文化IP]
tools: [read, exec]
---

# 诗词匠心 Poetry Craftsman

古诗词融合故事编织工具,将历史人物诗词自然融入故事叙述,支持6种融合模式与图文/短视频双输出格式,可选画外音解说。

## 使用场景

- 历史人物故事连载中,将诗词自然融入叙事
- 六种融合模式灵活选择:
  - quote: 直接引用(原诗入文)
  - paraphrase: 化用(改写为白话)
  - blend: 意境延伸(诗词意境扩展为场景描写)
  - contrast: 对比模式(正经解读+搞笑解读,极致反差)
  - parody: 打油诗改编(古诗词→打油诗/顺口溜/网络梗版本)
  - dual_character: 双角色对比(真实人物念原诗,虚构孪生兄弟用打油诗重说)
- 确保诗词与故事情节有机融合,不生硬插入
- 诗词平仄韵律校验与意境评分

## 工作流

1. 接收故事上下文+人物名+融合模式
2. 调用诗词数据库API查询该人物相关诗词
3. 调用历史人物档案API获取人物背景资料
4. 根据融合模式,用LLM将诗词融入故事段落
5. 校验诗词平仄韵律(古体诗/词模式)
6. 评估意境融合度评分
7. 输出融合后的故事段落+诗词标注

## 输入格式

```json
{
  "character": "李白",
  "story_context": "李白被赐金放还,离开长安...",
  "poem_title": "行路难",
  "mode": "blend",
  "target_audience": "elementary",
  "output_format": "article",
  "voiceover": "off"
}
```

字段说明:
- `character`: 历史人物名(必填)
- `story_context`: 故事上下文背景
- `poem_title`: 指定诗词标题(可选,不指定则自动匹配)
- `mode`: 融合模式,可选: quote(直接引用)/paraphrase(化用)/blend(意境延伸)/contrast(对比)/parody(打油诗改编)/dual_character(双角色对比)
- `target_audience`: 目标受众,可选: elementary(小学)/middle(中学)/adult(成人)
- `output_format`: 输出格式,可选: article(图文,默认)/short_video(短视频脚本)
- `voiceover`: 画外音,可选: off(无画外音,默认)/on(有画外音解说)

## 输出格式

### 图文模式(output_format=article)

```json
{
  "success": true,
  "data": {
    "paragraph": "融合后的故事段落...",
    "poem_used": {"title": "行路难", "author": "李白", "lines_used": ["长风破浪会有时"]},
    "mode": "blend",
    "output_format": "article",
    "audience": "elementary",
    "voiceover": "off",
    "meter_check": {"passed": true, "notes": "平仄韵律校验结果"},
    "imagery_score": 0.88
  }
}
```

### 短视频脚本模式(output_format=short_video)

```json
{
  "success": true,
  "data": {
    "script": [
      {"shot": 1, "duration": "5s", "visual": "画面描述", "dialogue": "台词", "character": "画外音"},
      {"shot": 2, "duration": "8s", "visual": "画面描述", "dialogue": "台词", "character": "李白"}
    ],
    "total_duration": "60s",
    "poem_used": {"title": "静夜思", "author": "李白", "lines_used": ["床前看月光"]},
    "mode": "dual_character",
    "output_format": "short_video",
    "audience": "elementary",
    "voiceover": "on"
  }
}
```

## 异常处理

| 异常场景 | 处理方式 |
|:---------|:---------|
| 人物名缺失 | success=false, error="必须提供character参数" |
| 诗词未找到 | 降级为无诗词融合的纯故事,标注poem_used=null |
| LLM调用失败 | success=false, error="故事编织LLM调用失败" |
| 诗词数据库不可用 | 降级为纯LLM创作(无诗词数据支撑) |
| 历史人物档案不可用 | 降级为通用历史知识创作 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 |
| 诗词数据库 | API | 可选 | 诗词查询(不可用时降级为纯LLM创作) |
| 历史人物档案 | API | 可选 | 人物背景资料(不可用时降级为通用知识) |

### API Key 配置
- **LLM_API_KEY**: 必需(通常由Agent内置) - 诗词融入故事/平仄校验/意境评分
- 配置方式: 在Agent的环境变量中设置

### 纯Markdown使用说明
诗词数据库不可用时降级为纯LLM创作。历史人物档案不可用时使用通用历史知识。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 意境延伸模式

输入: `{"character":"李白","story_context":"李白月下独酌","mode":"blend","target_audience":"elementary"}`

输出: 将"月下独酌"意境融入故事段落,扩展为月光、独饮的场景描写

### 示例2: 化用模式

输入: `{"character":"杜甫","poem_title":"春望","mode":"paraphrase","target_audience":"elementary"}`

输出: 将"国破山河在"化用为适合小学生理解的叙述

### 示例3: 对比模式

输入: `{"character":"孔子","story_context":"孔子讲学","mode":"contrast","target_audience":"elementary"}`

输出: 正经解读"人不知而不愠,不亦君子乎" + 搞笑版"有人不知道我的大名,可我还没发怒,这已经很君子了"

### 示例4: 打油诗改编模式

输入: `{"character":"李白","poem_title":"静夜思","mode":"parody","target_audience":"elementary"}`

输出: 原诗"床前明月光" + 打油诗版"空调坏了没电咯,月光照进被窝窝..."

### 示例5: 双角色对比模式

输入: `{"character":"李白","poem_title":"静夜思","mode":"dual_character","target_audience":"elementary"}`

输出: 李白念"举头望明月,低头思故乡" + 李黑打油诗版"抬头瞅月亮,低头想老家"

### 示例6: 短视频脚本输出

输入: `{"character":"李白","poem_title":"静夜思","mode":"dual_character","output_format":"short_video","voiceover":"on"}`

输出: 分镜脚本(画面+台词+时长),总时长60秒,含画外音解说
